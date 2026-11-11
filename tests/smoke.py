#!/usr/bin/env python3
"""Neon Protocol: Uprising, smoke checks.

Serves this folder on a free local port, opens the game in headless Chromium (Playwright for Python) and checks that:

  1. boot      the title screen comes up with no console errors
  2. scenario  a tiny two-turn battle can be played with real mouse clicks: select, preview, fire, end turn,
               an enemy turn, then the win and the after-action screen
  3. resume    a mid-mission save written by v0.6.10 (tests/fixtures/save-v0610.json) still loads, keeps its
               state and plays a full enemy round
  4. campaign  T-1 starts from a fresh profile, and one turn for each side runs without errors
  5. horde     each Horde modifier changes its wave, and a round plays out
  6. phone     at 390x844 with touch: the HUD fits, every visible button is a 44px tap target, and a unit can be
               selected and moved by tapping

Usage:  python3 tests/smoke.py [--headed] [--only boot,scenario,...]
Needs:  pip install playwright && python3 -m playwright install chromium
Exit code 0 when every check passes.
"""
import functools, http.server, json, os, socketserver, sys, threading, time

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIXTURE = os.path.join(ROOT, 'tests', 'fixtures', 'save-v0610.json')

# A 9x5 street: one tank against two weak drones. The tank kills one on turn 1; the other walks into range.
TINY = {
    'id': 'SMOKE', 'name': 'Smoke Test', 'custom': True, 'size': [9, 5], 'theme': 'urban', 'weather': 'clear', 'dark': 0,
    'civilians': 0, 'gen': 'tally', 'ai': 'rusher', 'fog': False, 'build': None, 'maxTier': 1, 'music': 'act1',
    'paint': [['fill', '.'], ['h', 'r', 0, 2, 9]], 'props': [], 'civ': [],
    'units': [['r_tank', 2, 2, 1], ['o_inf', 4, 2, 2, 20], ['o_inf', 7, 1, 2, 20]],
    'win': [{'type': 'rout'}], 'lose': [{'type': 'rout'}], 'funds': [0, 0], 'par': 4, 'budget': 0, 'tips': [],
}


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass


def serve():
    httpd = socketserver.ThreadingTCPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=ROOT))
    httpd.daemon_threads = True
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd, 'http://127.0.0.1:%d/index.html' % httpd.server_address[1]


class Game:
    def __init__(self, browser, url, phone=False, storage=None):
        opts = dict(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True) if phone \
            else dict(viewport={'width': 1280, 'height': 800})
        self.ctx = browser.new_context(**opts)
        self.pg = self.ctx.new_page()
        self.errors = []
        self.pg.on('pageerror', lambda e: self.errors.append('page error: %s' % e))
        self.pg.on('console', lambda m: m.type == 'error' and self.errors.append('console: %s' % m.text))
        if storage is not None:   # seed localStorage before the game boots
            self.pg.add_init_script('(() => { if (sessionStorage.getItem("np_seeded")) return; sessionStorage.setItem("np_seeded", "1"); '
                                    'const s = %s; for (const k in s) localStorage.setItem(k, s[k]); })()' % json.dumps(storage))
        self.pg.goto(url)
        self.pg.wait_for_function('() => document.querySelector("#title.on") || (typeof MODAL !== "undefined" && MODAL)', timeout=30000)
        if self.ev('() => !!MODAL && /WHAT\'S NEW/.test(document.querySelector("#mbox").innerText)'):   # a returning player sees What's New first
            self.ev('() => document.querySelector("#mbox button").click()')
            self.pg.wait_for_function('() => document.querySelector("#title.on")', timeout=20000)
        self.pg.evaluate('() => { SET.aiFast = true; SET.tips = false; }')

    def ev(self, js, arg=None): return self.pg.evaluate(js, arg)

    def state(self):
        return self.ev('() => ({g: G && G.L.id, turn: G && G.turn, day: G && G.day, busy, modal: !!MODAL, dlg: !!DLG, over: G && G.over, me: ME})')

    def until(self, js, t=60):
        end = time.time() + t
        while time.time() < end:
            try:
                if self.ev(js): return True
            except Exception: pass
            time.sleep(.2)
        return False

    def to_my_turn(self, t=90):
        """Click through dialogue, the briefing card and banners until it is the player's free turn (or the battle ends)."""
        end = time.time() + t
        while time.time() < end:
            s = self.state()
            if s['over'] or (s['g'] and not s['busy'] and not s['modal'] and not s['dlg'] and s['turn'] == s['me']): return s
            if s['modal']:
                self.ev("() => { const b = document.querySelector('#mbox [data-act=\"go\"]') || [...document.querySelectorAll('#mbox button')].find(b => b.classList.contains('end')); if (b) b.click(); }")
            elif s['dlg']:
                self.pg.keyboard.press('Space')                          # (only in dialogue: on the map, Space ends the turn)
            self.pg.wait_for_timeout(350)
        raise AssertionError('never reached the player turn: %s' % self.state())

    def tile_xy(self, x, y):
        return self.ev('([x, y]) => { const f = () => [(x*16+8-cam.x)*cam.z, (y*16+8-cam.y)*cam.z]; let s = f();'
                       ' if (s[0] < 70 || s[1] < 110 || s[0] > innerWidth - 70 || s[1] > innerHeight - 150) { centerOn(x, y); camTween = null; s = f(); } return s; }', [x, y])

    def click_tile(self, x, y, touch=False):
        sx, sy = self.tile_xy(x, y)
        if touch: self.pg.touchscreen.tap(sx, sy)
        else: self.pg.mouse.click(sx, sy)
        self.pg.wait_for_timeout(450)

    def start_level(self, L):
        self.ev('L => { const li = registerLevel(L); Object.assign(NEXT, {mode:"skirmish", li, fog:"off", gen:"", co:"vanguard", armies:null, coop:false, fmt:null, side:"R"}); hideModal(); newGame(li); }', L)

    def close(self): self.ctx.close()


def check(name, cond, msg=''):
    if not cond: raise AssertionError('%s: %s' % (name, msg))


def t_boot(b, url):
    g = Game(b, url)
    labels = g.ev('() => [...document.querySelectorAll("#title [data-t]")].filter(e => e.offsetParent).map(e => e.dataset.t)')
    check('boot', 'campaign' in labels and 'skirmish' in labels and 'maker' in labels, labels)
    check('boot', g.ev('() => typeof GAME_VERSION') == 'string', 'no GAME_VERSION')
    check('boot', not g.errors, g.errors)
    g.close()


def t_scenario(b, url):
    g = Game(b, url)
    g.start_level(TINY)
    g.to_my_turn()
    check('scenario', g.state()['day'] == 1, g.state())
    g.click_tile(2, 2)                                                   # select the tank
    check('scenario', g.ev('() => UI.sel && UI.sel.id') == 'r_tank', 'tank not selected')
    g.click_tile(4, 2)                                                   # first click on the drone: forecast
    check('scenario', g.until('() => document.querySelector("#preview").classList.contains("on")', 5),
          'no damage forecast (mode %s, tip %s)' % (g.ev('() => UI.mode'), g.ev('() => (document.querySelector("#tip")||{}).innerText')))
    g.pg.click('#preview button:has-text("Attack")', force=True)        # fire
    g.until('() => !busy && G.units.filter(u => u.team === 2).length === 1', 20)
    check('scenario', g.ev('() => G.units.filter(u => u.team === 2).length') == 1, 'the first drone survived')
    g.until('() => !busy && !MODAL && !DLG', 15)
    g.pg.click('#bar button:has-text("End Turn")', force=True)
    check('scenario', g.until('() => G.turn === 2 || G.day === 2', 20), 'the enemy turn never started')
    g.to_my_turn(90)
    s = g.state()
    if not s['over']:                                                    # (the drone may already have died to the tank's return fire)
        check('scenario', s['day'] == 2 and s['turn'] == 1, 'enemy turn did not hand back: %s' % s)
        foe = g.ev('() => { const u = G.units.find(u => u.team === 2); return u && [u.x, u.y]; }')
        g.click_tile(*g.ev('() => { const u = G.units.find(u => u.team === 1); return [u.x, u.y]; }'))
        g.click_tile(*foe)
        if g.until('() => document.querySelector("#preview").classList.contains("on")', 3):
            g.pg.click('#preview button:has-text("Attack")', force=True)
        else:                                                            # out of reach this turn: let the game's AI finish the job
            g.ev('() => { resetUI(); G.teams[ME].ai = true; runAI(ME); }')
    check('scenario', g.until('() => G.over && G.over.win', 90), 'the battle did not end in a win: %s' % g.state())
    for _ in range(40):                                                  # the victory line, then the result card
        if g.ev('() => !!MODAL && /COMPLETE|VICTORY/i.test(document.querySelector("#mbox").innerText)'): break
        if g.ev('() => !!DLG'): g.pg.keyboard.press('Space')
        g.pg.wait_for_timeout(400)
    check('scenario', g.ev('() => !!MODAL && /COMPLETE|VICTORY/i.test(document.querySelector("#mbox").innerText)'), 'no result screen')
    check('scenario', g.ev('() => !!document.querySelector("#mbox canvas, #mbox svg")'), 'the after-action report has no graph')
    check('scenario', not g.errors, g.errors)
    g.close()


def t_resume(b, url):
    if not os.path.exists(FIXTURE): raise AssertionError('resume: missing %s' % FIXTURE)
    store = json.load(open(FIXTURE))
    g = Game(b, url, storage=store)
    want = json.loads(store['np_save'])
    label = g.ev('() => document.querySelector("#tResume").innerText')
    check('resume', want['id'] in label, 'title has no Resume for %s: %r' % (want['id'], label))
    g.ev('() => document.querySelector("#tResume").click()')
    g.to_my_turn()
    s = g.state()
    check('resume', s['g'] == want['id'] and s['day'] == want['day'], 'wrong mission or hour: %s' % s)
    check('resume', g.ev('() => G.units.length') == len(want['units']), 'unit count changed')
    g.ev('() => { G.teams[ME].ai = true; runAI(ME); }')                   # a full round: our side (AI-driven), then the enemy
    check('resume', g.until('() => G.over || G.day === %d' % (want['day'] + 1), 240), 'the round did not complete: %s' % g.state())
    check('resume', not g.errors, g.errors)
    g.close()


def t_campaign(b, url):
    g = Game(b, url)
    g.ev('() => { CAMP.squadMode = CAMP.squadMode || "casual"; startMission("T-1"); }')
    g.to_my_turn()
    check('campaign', g.state()['g'] == 'T-1', g.state())
    g.ev('() => { G.teams[ME].ai = true; runAI(ME); }')
    check('campaign', g.until('() => G.over || (G.day === 2 && G.turn === ME)', 120), 'turn 1 did not complete: %s' % g.state())
    check('campaign', not g.errors, g.errors)
    g.close()


def t_phone(b, url):
    g = Game(b, url, phone=True)
    g.start_level(TINY)
    g.to_my_turn()
    g.pg.wait_for_timeout(600)
    small = g.ev('''() => [...document.querySelectorAll('#top button, #bar button, #info button')].filter(e => e.offsetParent && getComputedStyle(e).visibility !== 'hidden')
        .map(e => { const r = e.getBoundingClientRect(); return [e.id || e.innerText.trim().slice(0, 12), Math.round(r.width), Math.round(r.height)]; })
        .filter(([, w, h]) => w > 0 && (w < 44 || h < 44))''')
    check('phone', not small, 'tap targets under 44px: %s' % small)
    over = g.ev('() => { const r = document.querySelector("#bar").getBoundingClientRect(); return r.right > innerWidth + 1 || r.bottom > innerHeight + 1; }')
    check('phone', not over, 'the button bar runs off the screen')
    g.click_tile(2, 2, touch=True)
    check('phone', g.ev('() => UI.sel && UI.sel.id') == 'r_tank', 'tap did not select the tank')
    g.click_tile(3, 1, touch=True)
    check('phone', g.until('() => UI.mode === "action" || (UI.sel && UI.sel.x === 3)', 10), 'tap did not move the tank: %s' % g.ev('() => UI.mode'))
    check('phone', not g.errors, g.errors)
    g.close()


def t_horde(b, url):
    g = Game(b, url)
    for mod in ('elite', 'lean', 'blackout'):
        g.ev('m => { leaveGame(); Object.assign(HORDE_OPTS, {theme:"urban", size:"m", side:"R", co:"vanguard", diff:"n", mod:m}); hordeStart(HORDE_OPTS); }', mod)
        g.to_my_turn()
        check('horde', g.ev('() => G.L.hordeMod') == mod, 'modifier %s not applied' % mod)
        funds = g.ev('() => G.teams[ME].funds')
        g.ev('() => hordeWave()')
        foes = g.ev('() => G.units.filter(u => u.team && !allied(u.team, ME)).map(u => u.vet || 0)')
        check('horde', foes, 'wave 1 spawned nothing')
        if mod == 'elite': check('horde', all(v >= 1 for v in foes), 'elite wave not veteran: %s' % foes)
        if mod == 'lean': check('horde', g.ev('() => G.teams[ME].funds') == funds and not g.ev('() => !!G.L.crates'), 'lean times still paid out')
        if mod == 'blackout': check('horde', g.ev('() => G.fog && G.L.tod === "night"'), 'blackout is not dark')
    g.ev('() => { G.teams[ME].ai = true; runAI(ME); }')                   # a round with a modified wave on the board
    check('horde', g.until('() => G.over || G.day === 2', 240), 'the round did not complete: %s' % g.state())
    check('horde', not g.errors, g.errors)
    g.close()


TESTS = [('boot', t_boot), ('scenario', t_scenario), ('resume', t_resume), ('campaign', t_campaign), ('horde', t_horde), ('phone', t_phone)]

if __name__ == '__main__':
    only = None
    if '--only' in sys.argv: only = set(sys.argv[sys.argv.index('--only') + 1].split(','))
    httpd, url = serve()
    failed = 0
    with sync_playwright() as p:
        b = p.chromium.launch(headless='--headed' not in sys.argv, args=['--autoplay-policy=no-user-gesture-required'])
        for name, fn in TESTS:
            if only and name not in only: continue
            t0 = time.time()
            try:
                fn(b, url); print('PASS %-9s %5.1fs' % (name, time.time() - t0))
            except Exception as e:
                failed += 1; print('FAIL %-9s %5.1fs  %s' % (name, time.time() - t0, str(e)[:900]))
        b.close()
    httpd.shutdown()
    print('%d failed' % failed if failed else 'all passed')
    sys.exit(1 if failed else 0)
