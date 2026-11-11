# Playtest of v0.6.10: summary

One tester (a scripted run in headless Chromium through Playwright), from a fresh save, at 1280×800 with a mouse and at 390×844 and 844×390 with touch. The game's own AI stood in for the player on long stretches, so balance notes are flagged as such. Ranked by severity, tier 0 first.

## What was played

| Area | Covered |
|---|---|
| Campaign (Resistance) | New save, squad choice, prologue, T-1 by hand (select, move, forecast, fire, end turn, enemy turn), T-2 to T-4, 1-1, 1-2 to hour 90 |
| Campaign (Overmind) | 1-1 from the Overmind side, one full round |
| Horde | Neon City medium, nine turns; then each new modifier |
| Custom Battle | Small, base building, 2 v 2 couch co-op, fog, night, civilians: seven rounds with both human seats |
| Skirmish rules | A purpose-built range: indirect fire (mortar), overwatch (visible and in fog), threat ranges, the fog tap, losing |
| Map Maker | New 24×16 map, a road drawn by dragging, HQs, a Fabricator and six units placed, Check, Test (Play side 1) to a win |
| Saves | Resume mid-mission (1-2 at hour 90), the set-aside campaign save beside a Horde run, co-op resume, a Map Maker test play leaving the real save alone |
| Menus | Settings, Intel, How to Play, What's new, Load, War Room, Battle Shop and its Sound Room, pause |
| Performance | Boot, long tasks, a draw profile on a 64×48 map with about 190 units |

No console errors or page errors in any of it.

## Tier 0: crashes and soft locks

None found.

- A co-op run looked stuck on the pre-battle taunt. Traced to the test script: it pressed Space during a hand-over, and Space on the map is End Turn (the confirm box caught it). Not a game fault, but worth knowing: a player who mashes Space to skip dialogue can land on "END TURN?" when the last line closes. The confirm makes it safe.

## Tier 1: save and resume

None found. Checked and working:

- Resume of 1-2 at hour 90 restores units, HP, funds and the hour exactly.
- Starting Horde sets the campaign save aside; the title shows both "Resume Horde" and "Resume campaign 1-2".
- Co-op resume keeps both seats human.
- A Map Maker test play leaves the real save untouched.
- A v0.6.10 save (kept as `tests/fixtures/save-v0610.json`) loads in v0.6.11 and plays a full round.

## Tier 2: rules and AI

1. **1-2 can stalemate for a weak player** (AI stand-in, so treat with care). With the AI playing the Resistance, 1-2 ran 30 turns without an end: the Act 1 buying cap (1.1 × your army + 1) lets the enemy rebuild to parity every time you lose units, so a player who falls behind never catches up. *Repro:* play 1-2 passively, losing a unit every couple of turns; the enemy count tracks yours. *Not changed:* needs a human run before touching the cap.
2. **Overwatch hidden in fog fires without a warning.** A tank moving next to a watching drone it cannot see takes the overwatch shot with no card first. This is right (the card would give the hidden unit away), but it may read as unfair. *Not changed.*

Indirect fire, the forecast ("Indirect fire: no counter"), threat ranges, the fog tap ("You can't stop there") and losing (MISSION FAILED with the after-action graph and Retry) all behaved.

## Tier 3: onboarding and clarity

1. **Turn banner hard to read.** "HOUR 6" floats over the units and the army name under it is small grey type that vanishes on a busy map; nothing says whose turn it is. *Repro:* end any turn on a busy map. *Fixed:* a dark band edged in the army's colour, and YOUR TURN, ENEMY TURN or ALLY TURN under the hour.
2. **Days and hours mixed.** The resume bark said "Welcome back. Day 31" under a HUD reading HOUR 90. The Map Maker's balance check said "Income / day" and its AI-vs-AI report "(day 12)" and "9 days". *Fixed.*
3. **The Sound Room gave no feedback.** Forty-eight ▶ buttons in the Battle Shop with no sign of what was playing, no pause and no way to play more than one track. *Fixed:* a player deck (see tier 6).
4. **The Sound Room is hard to find**: it sits near the bottom of the Battle Shop. *Not changed*; suggested as a title-screen link later.
5. The T-1 hour 3 tip says the drones "move and shoot too" on a turn where they only moved. *Not changed:* tutorial and story lines are kept as written.

## Tier 4: phone layout and touch

1. **👁 and ☰ were 34×34px** in both phone layouts (target 44). *Repro:* 390×844, any mission, measure `#bHide` and `#bMenu`. *Fixed:* 44px, with the objective line narrowed so ☰ stays on its row.
2. **Title menu buttons were 40px tall** on any screen under 860px tall, which is every phone. *Fixed:* 44px on touch screens.
3. **Landscape: the radio bark covered 👁 and ☰** in the left rail (and took their taps) for its few seconds. *Repro:* 844×390, resume any mission. *Fixed:* the bark starts beside the rail and ignores taps.
4. Narrow title: UPRISING sat 4px into NEON PROTOCOL's glow. *Fixed.*

The v0.6.9 phone layouts otherwise held up: no horizontal scroll, the bar fits, a tile can be selected and a unit moved by tapping.

## Tier 5: performance

1. **Team rings were a third of every frame in big battles.** Profiling a 64×48 map with about 190 units, the v0.6.4 ring overlay drew forty 1px squares and a dozen strips per unit per frame (35% of draw time). *Fixed:* each ring is drawn once per colour and stamped.
2. **Everything was drawn off screen too**: every unit (with its blurred dark edge), every unit glow and every ring, whatever the camera showed. *Fixed:* skipped outside the view. A frame at normal zoom on that map went from about 33 ms to 16 ms in the (software-rendered) test browser; zoomed right out, from about 60 ms to 50 ms.
3. **The per-unit blurred edge** (`shadowBlur`, v0.6.4) is still the costliest part of a unit, and the light pools are most of what is left. *Not changed:* removing the edge changes the look; caching outlined sprites is the next step.
4. **Ridges read the terrain canvas back pixel by pixel** while the map is built (Chrome warns about `willReadFrequently`). Measured at 54 ms for 160 ridge tiles on a 64×48 highland map, once per mission. *Not changed.*
5. Boot is quick (title in about 1.4 s from a local server); the 25 recorded effects load after the first tap and the music streams one track at a time. Nothing to fix.
6. On the 2-core test machine, "Choose Commander ▶" in Custom Battle took about 2 s to respond (map generation itself measured 10 to 20 ms, so the time is elsewhere). *Not changed:* worth profiling on a real phone.

## Tier 6: look and feel

1. **The camera showed empty sky beside the map.** Mission start, resume and camera follows used v0.6.9's loose drag limit, so a mission often opened with a quarter of the screen off the map. *Repro:* 1280×800, start 1-2 or any Horde map. *Fixed:* the game's own camera moves stop at the edge plus the HUD, or centre a map that fits; dragging still pans past.
2. **HP numbers hidden under the unit below.** Units are drawn top row first, so a sprite on the next row covered the HP number of the unit above it (two drones in a column read "5" and a blank). *Fixed.*
3. Selected tabs use cyan on the campaign side switch and magenta on the act tabs. *Not changed.*
4. The battle-cam cut-ins, death animations, team rings and power effects already give strong hit and destroy feedback; nothing added there.

## Smoke checks

`tests/smoke.py` (Playwright for Python) now covers boot, a tiny two-turn battle played with real clicks through to the result screen, resuming the v0.6.10 save, a campaign turn for each side, the Horde modifiers, and the phone layout and tap targets. Run it with `python3 tests/smoke.py`.
