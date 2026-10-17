# Neon Protocol: Uprising: changelog

## v0.5 (2026-10-17)

A research and testing pass. It draws on reviews of Advance Wars 1+2: Re-Boot Camp and Wargroove, Into the Breach's design talk, and colour-blind accessibility guides (see docs/research-v05.md). It also adds a persona-bot difficulty sweep across all five acts, and four new AI playtesters: story, phone, stability and accessibility.

### Fairness and pacing
- **Deterministic luck (Into the Breach):**
  - Each attack's luck comes from the battle state, so a rewound attack lands exactly the same way and rewind can't be used to re-roll.
  - The odds are unchanged, and a different move or attacker still rolls differently.
- **Escort missions were the campaign's difficulty spikes:** the persona panel lost 1-5, 2-5, 3-5 and 5-5 within a week every time, because the AI focus-fires an exposed VIP.
  - Your VIP now has protective plating: +25% defence, or +40% on Recruit.
  - When your VIP ends a move somewhere it could be hit, the game warns how much damage it could take next turn.
- **The AI closes out won games:** with a 2× army or the enemy down to two units, its whole army hunts the remaining enemy units and structures. This addresses the biggest complaint about Re-Boot Camp's AI.
- **Rank targets:** the briefing shows what an S rank needs (win by par, budget, and at most one loss per four kills).
- **Battle scene speed:** Normal or Fast. Wargroove's scenes were criticised as too long.

### Balance and AI, using Iron Front '44's playbook
- **Symmetry test** (mirrored maps, both sides of the board):
  - With TALLY as the Overmind general, the Overmind won 7 of 16 games, the Resistance 0, and the Overmind led 8 of the 9 that timed out.
  - With identical passives the factions are even.
  - **The cause was TALLY's +20% income, now +10%** (Advance Wars' Sasha has +10%).
- **Build-list trace** found monocultures: 24 troopers a side in 1-9, 17 skiffs from one port in 2-1, and almost no tanks.
  - The AI now prefers variety, caps any one unit type at 6 (except needed capturers), and banks money for armour once it has enough troopers.
  - Kova's Street Recruit and WARDEN's Conscription were being used on every civilian. The AI stops recruiting once it fields 8 foot units.
- **End-state map trace** found 40 units circling an undefended enemy base for 10+ days. Their main guns were dry and the AI never went home. Units now go back to resupply at a friendly property, repair bay or supply carrier when their main weapon is empty.
- **Escort missions** (lost by every persona by day 6–12, in two runs):
  - The enemy still targets the VIP, but no longer to the exclusion of everything else (priority 3× + 6,000 → 1.6× + 2,500).
  - VIP plating is now +35% defence (+50% on Recruit).
- **Escort AI** (when the AI escorts: assist, co-op allies, and the Overmind side):
  - The VIP no longer marches ahead of its army or into fire.
  - It stays within a few tiles of the army's median, moves only once two escorts are further along, and never stops to capture or secure buildings on the way.
  - Traced: the VIP now survives to day 15+, where it used to die on day 6–9.
- **3-5 "Avalanche Pass":**
  - The player had no factory at all while the Overmind had one, so money piled up unspendable (¢22–27k in every persona run). Your city is now a Fabricator.
  - The Overmind starts with ¢1,500 instead of ¢5,000.
- **5-1 "Outer Grid"** (lost by every persona, in two runs): the Overmind's reanimation raised every corpse each turn. It's now capped at two a turn.
- **Horde:**
  - Live enemy units are capped at 24 + the wave number.
  - The status line scouts the next wave (tech tier, waves to the next boss).
  - Every wave brings the defenders a supply drop.
- **Persona suite:**
  - Six new personas: methodical, aggressive, cautious, opportunist, reckless and sniper.
  - Automatic flags: the rusher counts only on rushable objectives, the turtle only if it wins within 60% of the time limit. Also flags a mission over by day 2, units that never moved, and crashes.
  - A per-mission table with measured difficulty verdicts, and reports saved to disk.

### Stability (from the "Max" systems-QA pass)
- **Resume lost story objectives:** resuming or loading dropped objective changes made by story events, so 1-5 and 2-5 could be won instantly. A misplaced code comment had disabled the restore.
- **Leaving mid power or mid superweapon:** the power or strike used to finish in the *next* game (stuck "busy", old damage on the new map). It now stops cleanly.
- **Map Maker test games:** they no longer autosave over your real Resume save.
- **Leaving a game:** closes any dialogue, story card or transmission still open.
- **Rewinding a Power:** stops its theme music.
- **Horde's objective line:** reads "hold out as long as you can".
- **Faster enemy turns on huge maps (Fast):** off-screen AI moves are instant. Max measured 22–35 s per turn before.
- **Confirmed solid:**
  - Save, resume and load with every system live.
  - Co-op rewind.
  - 1,400 random inputs with zero errors.
  - 100 AI-vs-AI missions with zero errors.
  - No memory leak across 10 loads.

### Story (from the "Sol" narrative review)
- **Scripted scenes stand alone:** they no longer end with a generic "Job's done. Count heads." or start with "Point me at it."
- **Bond conversations:** at most one per briefing, and none before boss missions or the finale.
- **One consistent timeline:**
  - Sector 4 went first, three years ago, and Sector 9 is next.
  - Eight sectors have been processed by Act V.
  - The Overmind is twenty years old everywhere.
  - Sector 9 holds four hundred thousand people; eleven million is the whole city.
- **Side stories:** the key reveals in S-1 and S-2 always play, even if you win another way.
- **Answered threads:**
  - **The Bloom argument:** answered at 4-10 ("We dig it out by hand. Ninety years.").
  - **Act V's question** ("save this city or win"): answered at 5-10 ("Count heads, Mara. All of them.").
  - **ORACLE's fear of "what happens after us":** answered in the epilogue.
  - **The 2-7 hunger figure:** returns in 5-7.
- **Mara and the squad come back:** Mara has moments in Acts III and IV. The Resistance epilogue gets a Mara card and a squad card, and anyone who fell in Classic mode is remembered by name.
- **Rewrites:** ten scenes rewritten, including 3-7, 4-4, 4-10, 5-1, 5-5 and 5-10. MIRROR's catchphrase is cut from seven uses to two.
- **The Overmind campaign gets an arc:** "doubt managed, not resolved".
  - One interlude per act.
  - Act blurbs that admit the front is collapsing toward the Core.
  - The 4-3 convoy scene, and 5-5's "Somebody should be wrong carefully".
  - Three more intercepted Resistance broadcasts.
  - Its own mission names for every act.
  - Two new epilogue cards.
- **Act title cards:** now always play before an act's opening interlude.

### Map Maker
- **First-run tour:** a five-step guide to the tools, shapes and symmetry, palette, Populate and Balance, and Test and sharing. Wargroove's editor was praised but called hard to learn.

## v0.4 (released as part of v0.5)

A bigger build: a training act, a deeper story, new portraits and sprites, voices, and a proper map editor. Tested by AI playtesters with different personalities (Ruth, plus a new round) and by AI-vs-AI runs of every mission.

### Campaign
- **Act 0 Boot Camp:** four short training missions (T-1 "First Steps" to T-4 "Signal Fire"), each teaching one idea, with Mara Seo as instructor.
  - New players start here, and a "Skip training" button is always there.
  - T-4 ends with the Overmind naming Sector 9 for recycling and leads straight into 1-1.
- **Story:** ten new interludes across Acts I–V (Lantern Street, Mara's brother Jin, the Overmind's address to the city, the flood-gates dilemma, ORACLE-7's doubts, and more).
- **Side stories:** S-1 "Ledger of Names" (after 2-5) and S-2 "Quiet Arithmetic" (after 3-5). Both are optional and lock nothing.
- **Playing the Overmind:** the machine generals taunt, doubt and comment on the fight as it happens.
- **Overmind 1-8:** keeping the bomber wing alive until day 11 now wins the mission. Before, it was escort-only and the AI panel lost every time; now it's about 50/50.

### Battle scenes (Advance Wars)
- **What it shows:** every attack involving your army plays a 1.5–2.3 second split-screen fight.
  - The attacker is on the left, the defender on the right, each on a backdrop of the terrain they stand on: Shin-Pacifica skylines, jungle, ridges, sea, open sky for aircraft.
  - Time of day and weather carry through.
- **HP counts:** infantry show one soldier per 2 HP, and vehicles, aircraft and ships show 1–3. Figures fall, explode, crash or sink as HP ticks down, then the counter-attack plays.
- **Weapons:** each weapon type has its own visuals (tracers, rail beams, shells, rockets, flak, bombs, torpedoes).
- **Skipping:** tap or press any key to skip; hold to skip the rest of the turn.
- **Settings → Battle scenes:** All, Mine (the default) or Off. Instant enemy turns never show them.
- **Outcome:** the scene replays the real result, so the game plays exactly the same with scenes off.

### Briefing room (C&C)
- **Tactical display:** every campaign briefing has an animated tactical map.
  - A scanline sweep, then numbered objective markers (HQ to take, escort route, tiles to hold, survive clocks).
  - The enemy's estimated strength by type. In fog it's approximate, with a NO INTEL zone.
- **Overmind transmissions (Kane-style)** break into eight Resistance briefings (1-1, 1-5, 1-10, 2-5, 2-10, 3-10, 4-10, 5-5).
  - The Overmind or the act's general speaks on a glitching CRT with its animated portrait, a voice and typed text.
  - Playing the Overmind, you intercept four Resistance pirate broadcasts (Mara, Kova).
  - Each plays once, with a Replay button afterwards.
- **Settings → Briefing display:** Animated or Simple.

### Tactics layer (Fire Emblem, XCOM, FFT)
- **Rewind (⟲ button or U):**
  - Undoes your turn one step at a time: a move plus its order, a build, a capture or a power. You can go all the way back to the start of your turn.
  - A run of rewinds costs one charge, like Fire Emblem's Turnwheel.
  - Charges: 3 per mission on Recruit, 1 on Veteran, none on Nightmare, unlimited in Boot Camp.
  - Story dialogue never replays.
- **Overwatch:**
  - Troopers, Breachers and anti-air can give up their attack to watch.
  - During the next enemy turn they fire once at the first enemy that ends a move in range: 80% damage, no counter.
  - Watchers show an eye icon and their range shows as an amber zone.
  - The AI uses overwatch to hold posts, and it avoids walking into yours.
- **Flanking:** +15% damage when one of your units is next to the target on the far side from the attacker (a pincer). It shows in the damage preview and the Why line. The AI uses it too.
- **Telegraphs:** a superweapon target the enemy has queued is marked with hatched red tiles before it fires.
- **Settings:** Rewind charges (Standard, Unlimited, Off) and Overwatch & flanking (On, Off).
- **AI-vs-AI check:** across acts I–II, win rates stay within normal run-to-run noise.

### The Squad (Fire Emblem, FFT and XCOM)
- **The squad:** five named Resistance soldiers join over training and Act I:

  | Soldier | Role |
  |---|---|
  | Rin Kealoha | trooper |
  | Dai Ferreira | rail-tank |
  | Yuna Okoye-Hara | recon bike |
  | Hemi Paewai-Tanaka | engineer |
  | Mika Arakaki | anti-air |

  - Each takes the place of a matching starting unit, so the squad never adds power.
  - Each has a portrait, a bio, barks and an introduction scene.
- **Persistence:** kills and rank carry across the campaign. Classic mode makes deaths permanent, with an "In memory" card. Casual mode means wounded, sitting out one mission.
- **Specialisations:** at ELITE you choose one of two perks for each role, for example Breacher or Field Medic, Reactive Armour or AP Rounds, Flak Burst or Long Watch.
  - Perks show in the damage preview's "Why:" line.
- **Bonds:** squad members who end turns side by side build bonds, which give +5% attack and later −5% damage taken. Each bond unlocks two short conversations.
- **📜 Chronicle:** every squad member's story, stats, bonds, and a memorial for the fallen.

### Art and sound
- **Portraits:** all 14 generals and cast members are redrawn at 96px, with talking, blinking and character effects. Examples: the Overmind's eye wanders and dilates, Sable glitches, and TALLY prints receipts.
- **Sprites:** units are redrawn with more detail.
- **Voices:** characters speak in dialogue and units bark.
- **Sounds:** new sounds for weapon variants, carpet bombing, superweapons, terrain hits, and faction capture and build.

### Map Maker III
- **Drawing tools:** shapes (line, rectangle, ellipse, flood fill), brush sizes and five symmetry modes.
- **Stamps:** city block, base, river bend, forest, island and ruins.
- **Populate and Balance:** Populate adds civilian life, and a Balance check compares the two sides.
- **Test-play:** placed supply crates, and test-play as either side or as AI vs AI.
- **My Maps:** a gallery of thumbnails, plus short `NPM1:` share codes.

### Debrief and pace
- **After-action report:** the result screen shows a day-by-day graph of each side's army strength and territory, plus your MVP unit (most kills, its veterancy, and whether it survived). This is the C&C and Advance Wars style debrief.
- **Settings → Your animations: Fast:** your own units move at the fast enemy-turn speed.

### Modes and AI
- **Horde:** Easy, Normal and Hard waves. Best runs are kept per difficulty.
- **Custom Battle:** in formats with more than one army a side, you choose each ally and enemy army's leader, or leave it random.
- **AI:** units an army must keep alive now hang back near their HQ, with an escort.
- **AI aggression pass (Veteran and Nightmare; Recruit stays forgiving):**
  - **Attacks:** units attack when the trade is good, or when the shot costs them nothing.
  - **Massing:** units only wait for the pack when the army really is behind.
  - **Finishing:** the AI pushes for your HQ sooner when it's clearly ahead.
  - **Spending:** it spends banked money on the best unit for the fight, sharing the budget across factories.
  - **Bug fixes on every difficulty:**
    - The AI no longer parks on its own factories.
    - Troopers no longer keep resetting a civilian building a squad-mate is already securing. This was why enemy infantry sat still for days in 1-2.
    - Landers and lifters ferry stranded troopers to island objectives.
    - An AI escort VIP walks home when it's safe instead of waiting for ever.
    - A side switched to AI clears the player's leftover build orders.
  - **Result:** on a large skirmish map, AI attacks in the first 10 days went from 0–1 to 19–26.
- **AI expansion fixed:**
  - Every capturing trooper used to head for the same nearest target. On big maps they all jammed around one civilian building beside their own HQ: 1 of 62 neutral properties was taken in 9 days.
  - Now each trooper claims its own target, and targets already being captured are left alone. Over the same 10 days the AIs captured 14.

### Accessibility and fixes
- **Accessibility:**
  - colour-blind mode (shapes as well as colours)
  - a text-size setting
  - clearer markers on finished units
  - a focus trap in dialogs
- **Pause menu:** the ☰ menu was missing Save and Report. Fixed.
- **Pause:** pausing now really stops the enemy's turn.
- **Free move:** ending your turn while a move was pending gave a free move. Fixed.
- **Kova:** referred to as "he" consistently.

### The voice of the base (C&C)
- **Announcer:** Mara on the field radio (Resistance) or a cold system voice (Overmind) calls out events, each with an on-screen caption:
  - construction and units ready
  - base or HQ under attack
  - units lost
  - captures
  - insufficient funds
  - low power
  - superweapons charging, ready or detected, and launches
  - reinforcements
  - power ready
  - mission accomplished or failed
- **Settings → Base announcer:** On, Captions only or Off.
- **Power themes (Advance Wars):** when you fire a Power, the music switches to that leader's own power theme until your turn ends.
- **Superweapon clock:** both sides see a countdown badge and a pulsing marker on the superweapon.

### Fixes from the "Hana" story-first playtest
- **Text size:** "Largest" no longer pushes Settings off-screen, and story cards follow the text-size setting.
- **Tap an enemy to attack (Fire Emblem style):** with a unit selected, tapping a red-outlined enemy moves to the best tile to hit it from and opens the attack preview. Tap again to fire.
- **Rail-tank range is explained:**
  - The unit card shows "RNG 1-2 (MG 1)".
  - The 1-1 tip explains that the cannon hits vehicles at 2 tiles, while the machine gun only reaches adjacent tiles.
  - Tapping a target you can't hit says why.
- **Tips:** they no longer catch taps meant for the map, and they clear when a mission ends.
- **"While you waited":** it waits for dialogue to finish instead of covering the speaker.
- **Commander card:** no longer shows the writers' voice notes.
- **Story cards:** say "tap, click or press Space" instead of "press A".
- **HP numbers:** sit on a softer badge.
- **Plurals:** "own 1 Uplink Tower" and "1 day left".
- **New players:** no longer greeted with the whole changelog.
- **Boot Camp tips:**
  - Mara's lessons come first; generic tips (weather, field abilities, income) are held back in training.
  - Tips are never lost when you end your turn.
  - 1-1 and 1-2 give a short recap instead of re-teaching what training covered.
- **T-2:** the Fabricator lesson sits in the build panel, which lists just three units in plain words. It also explains that a unit standing on the Fabricator blocks it.
- **T-3 "Hold the Line" now tests holding:**
  - The enemy assaults the ridge line, with a day-5 wave.
  - Before, the drones wandered off to secure random civilian buildings.
  - Par matches the survival length, and the mortar range text matches the unit.
- **T-4 into Act I:** the Act I title card no longer gets swallowed after T-4.
- **Act I follows on from Boot Camp:**
  - TALLY is already known.
  - The Overmind already knew Kova's name.
  - There's one consistent story: Sector 4 (Jin's ward) went three years ago, Sector 9 is next, and Lantern Street is the street under the Uplink Tower from T-4.
- **Training endings:** the generic "Job's done" line no longer cuts across them. Kova's T-2 line matches your result.
- **Instant enemy turns:** they no longer skip the story interludes.

### Map Maker fixes from the "Marisol" level-designer playtest
- **Test-play difficulty:** test games have their own difficulty, defaulting to Veteran (neutral). Before, the Recruit handicap was applied even to AI vs AI, so balance couldn't be judged.
- **Side-2 tests:** the objective line and briefing are shown from your side.
- **Enemy leader:** the test dialog starts from the map's own enemy general.
- **Enter:** no longer skips the test options.
- **Diagonal lines:** roads, rivers and walls drawn diagonally now join up.
- **Objective counter:** it says what it counts, e.g. "(5 units + 12 buildings left)".
- **Auto-simulate:** Balance can run 4 or 8 headless AI-vs-AI games of your map and report win %, stalemates (and who they leaned to), game length and why each game ended.
- **Copy, cut and paste:** a Select tool (key 9) copies, cuts and pastes regions, with rotate and flip. "Save as stamp" keeps up to 20 custom stamps.
- **Resize:** pick an anchor (9 positions) and get a warning listing anything that would be cut off.
- **Palette:**
  - Each tool keeps its own scroll position.
  - The team swatches are now a compact dropdown.
  - Units can be searched and filtered by category.
- **Stamps:**
  - A "keep background" option.
  - The Fortified base now includes power.
- **Flood fill:** previews its area. Fills over 600 tiles ask first.
- **Marks:** placing a VIP, goal or target mark switches on the matching objective. Marks are easier to see zoomed out.
- **Watch AI vs AI:**
  - Skips the briefing.
  - Says why a side won.
  - A stalemate says who was ahead.
- **Back from a test:**
  - Restores zoom and undo history.
  - The minimap docks again.
  - Test games no longer overwrite your Resume save.
- **Side 2 tests:** open centred on your own HQ, clear of the build panel.
- **Import, export and readability:**
  - Imported maps with a duplicate name get "(imported)".
  - Export has "Copy short code".
  - Turrets and walls get a team-coloured outline.
- **Phones:** all tools reachable, and Help's button stays pinned.

### Fixes from the "Kenta" playtest (Advance Wars veteran, Veteran difficulty)
- **Tap an enemy to attack:**
  - It never walks into enemy overwatch when another tile works, and warns when it has to.
  - If your unit is shot on the way in, the next tap shows the updated forecast instead of firing blind.
  - Tapping an enemy you can't reach says "Out of reach this turn".
- **Fast enemy turns are quicker:** a quiet five-unit turn on Fast takes about 3.4 s.
- **Announcer captions:** they always time out and never show outside a battle.
- **Leaving a battle:** clears its banner.
- **Result screen:** if it ever fails, a fallback screen still lets you continue or retry.
- **Esc:** closes an enemy's info card before opening Pause, and closes What's New on the title screen.
- **Briefings:**
  - Overmind transmissions wait for the squad's dialogue instead of talking over it.
  - They address your actual commander, e.g. "Commander Okafor".
  - 1-1's transmission no longer assumes you played Boot Camp.
  - Duplicate markers are merged, and labels stay on the map.
- **Overwatch tuned so it no longer freezes the front:**
  - The AI keeps at most a quarter of its eligible units on overwatch.
  - The AI never overwatches when it has a good attack or capture.
  - Damage drops from 80% to 65%.
  - Overwatch breaks when the unit is hit.
  - The enemy zone is easier to see.
  - With these changes the AI goes on overwatch less than half as often as before.
- **Rewind:**
  - A tip firing between rewinds no longer burns your charge.
  - The last charge asks "press again" so a stray U can't waste it.
- **Superweapon targets are marked a full turn ahead (Into the Breach):** hatched tiles plus a "fires next turn" badge, so you can get out of the way. The weapon fires at the marked tile.
- **Damage forecast:** the flank bonus is folded into the headline damage.
- **Overwatch shots:** they now play a battle scene.
- **Squad deploy screen (Fire Emblem):**
  - Before each Resistance mission you choose which squad member fills which slot, or bench them. Choices are remembered per mission.
  - Wider role matching means recruits always deploy on the mission they join, and nobody gains power.
  - Squad members rank up at 3, 8 (specialisation) and 14 kills.
  - A fallen member's death is recorded on the day it actually happened.
  - The MVP line names squad members.
  - The AI keeps named units safer when it controls your side.
  - Settings → Squad deploy screen: Show or Auto-deploy.
- **Skip story ▶▶:** one press skips the whole pre-mission chain (interlude cards, dialogue, act card, transmission). A replay button keeps the transmission available.

### Fixes from the "Lou" playtest (C&C veteran, Overmind side)
- **Factories on the Overmind side:** you couldn't buy anything from your own Fabricator, Airpad or Port. This hit every Overmind-side game: the campaign, skirmish, Horde and co-op player 2.
  - The engine assumed the human was always team 1.
  - Also fixed for the same reason: the camera now opens on your own HQ, and battle music intensity is measured from your side.
- **Playing side 2 anywhere:** in skirmish, custom battle and Conquest, the objective line now reads from your side. It used to count your own units as "enemy units left".
- **Overmind mission names:** the Overmind campaign's own names now appear in the briefing header, dialogue header and the "Unlocked mission" line.
- **1-8's survival goal:** the tactical display now shows "keep the wing alive until day 11" as a clock chip.
- **Minimap:** the camera can pan a minimap's width further, so units under the minimap can be reached.
- **Announcer:**
  - "Structure lost" when one of your buildings is destroyed.
  - Horde waves are announced.
- **Conquest:** "Abandon war" asks first.
- **Small fixes:**
  - The thinking label names whose turn it is.
  - Top-bar funds refresh after queued purchases.
  - The two-tab warning comes from the Overmind's own voice when you play the Overmind.
  - The after-action graph's legend no longer overlaps the lines.

### Fixes from the "Dex" exploit-hunter playtest
- **Overmind-side resume softlock:** resuming a save where you play the Overmind (team 2) froze the game on the Resistance's turn. Saves now record whose turn it is.
- **Sable crash:** in missions with Sable's cloaking (e.g. 2-3), a unit in cover next to a civilian crashed the start of your turn and locked the pause menu.
- **Mid-move save exploit:** saving (or alt-tabbing, which autosaves) with a move not yet confirmed let the unit move again after loading. Uncommitted moves are now saved at their starting tile.
- **Silent barks:** two "bark" functions overwrote each other, so the v0.4 barks never showed (welcome back, TALLY's tips, unit lost, the Overmind's first-kill line).
- **Pause leak:** pause now holds the enemy's turn while you're in Settings, Save, Load or Intel, not only on the pause menu itself.
- **Imported maps are checked:**
  - Unknown leaders, NaN or negative HP, absurd funds and malformed objectives are repaired.
  - These used to crash the game or make units unkillable.
  - An unreadable map now shows an error.
- **Points farming:**
  - A replay pays a quarter unless you beat your best score, and training pays a small bonus.
  - Horde pays only for waves beyond your best, scaled by wave difficulty.
- **Overmind names:** the Overmind's mission names now appear in the briefing header too.
- **Horde result:** no longer shows a meaningless par and score.
- **"Report a problem":** no longer throws when the clipboard is blocked.
- **Two tabs:** a warning appears when the game is open in another tab, since both share one save.

## v0.3 (2026-10-16)

An iteration on v0.2's playtest findings, plus a new phone-player playtest.

### Balance
- **1-6 "Dead Air":** the Overmind's infantry no longer starts beside two of the three Uplink Towers, and the Resistance gets a second anti-air team and a trooper.
  - Each tower gives its owner +10% attack, and the bonus stacks, so the enemy used to start the mission with a free +20%.
- **Veteran and Cyber-Nightmare AI** fears losses less, so it presses instead of idling next to your units. Recruit keeps its cautious AI.

### Clarity
- **Line of sight:** the attack-range tiles show it. Grey tiles are in range, but a building blocks the shot.
- **Tips:** tutorial tips arrive when they're relevant instead of queueing behind stale ones.
- **Income:** your income pops up at your HQ each turn, and a one-time tip explains where the money comes from (cities, factories and the HQ pay ¢1,000 each).
- **Score:** the result screen explains Speed, Power and Economy, including why Economy is always 100 when a mission has no budget.
- **Civilians:** Fire never offers civilians as targets. A petrol station is offered only when an enemy is inside its blast.
- **Counter-attacks:** the Controls text now gives one consistent rule. A defender fires back only if you attack from inside its own range, and artillery never does.

### Controls
- **Esc and X** close every panel, including Controls.
- **Story cards** respond to A as their prompt says.
- **What's new** lists every version, newest first.

### Phones (from the new phone-player playtest, "Pip")
- **Stuck buttons:** after an attack, Next and End Turn stayed greyed out until you tapped one of your own units. Fixed.
- **Action menu:** on narrow screens it docks at the bottom, so it no longer covers the map.
- **Close button:** long panels such as Controls get a pinned ✕.
- **Targeting explains itself:**
  - Tapping something you can't shoot says why: out of range, no line of sight, or a civilian.
  - Target mode opens on a target you can actually hit.
  - Civilians and their buildings are never offered as targets.
- **Tips:**
  - At most one per turn by default (Settings → Tips: one per turn, all, or off), and a "No more tips" button.
  - Tips that weren't shown in time are dropped when you end your turn, instead of popping up during the enemy's turn.
- **Damage preview:** damage is labelled as a percentage of the target's HP.
- **Tidy-ups:**
  - The enemy threat overlay clears when you end your turn.
  - Old banners no longer show in the next mission.
  - The "processing" label no longer covers buttons on phones.

### Tried and reverted
- I tried time pressure (armies getting bolder after par) to stop AI-vs-AI stalemates. It only made test bots charge into losing fights, so it was removed.

## v0.2 (2026-10-16)

v0.2 is a "make the first hour great" release. It was tested by a panel of AI playtesters before shipping:

- **Language-model players** played the game cold and reported where they got confused:
  - "Nao", a first-timer who has never played a tactics game.
  - "Kenji", an Advance Wars and XCOM veteran.
- **Six bot personalities** played the human side across Act I and the opening missions of Acts II–V, more than 150 games in all:
  - a first-timer
  - a distracted phone player
  - a rusher
  - a turtle
  - an expander
  - a min-maxer

### Story and onboarding
- A four-card story prologue before the first campaign map: Shin-Pacifica, the Overmind's arithmetic, the "recycling" of the city, and Kova Arashi.
- New players default to **Recruit**, which is now a real first-timer mode:
  - the enemy has 30% less income and loses a quarter of its ordinary starting units
  - you get 30% more starting money
- The first mission's own tutorial comes first. Weather, time and field-ability tips wait until day 2.
- With only one commander unlocked, the choose-commander screen is skipped.
- Tooltips explain jargon: par, APC, ARTY, MECH, indirect, fuel, terrain stars, Secure, MV.

### Balance (from the playtest panel)
- **Army cap:** enemy armies in campaign missions are capped at 14 units on Recruit and 24 on Veteran (no cap on Cyber-Nightmare). In v0.1 the Overmind could snowball to 40 units on income alone.
- **1-3, 1-6, 2-1, 2-2:** the strongest ordinary enemy units are removed (Resistance campaign only).
- **1-6:** the nearest Uplink Tower starts in Resistance hands.
- **2-2:** Wren's engineers arrive on day 2 instead of day 4.
- **Result:** in the hardest early missions, first-timer losses fell from 58–100% to about 17%.

### Clarity
- **Attack confirmation:** the first click on a target shows the damage preview and the second fires, for mouse as well as touch. There's a setting to turn this off.
- **Damage preview:** it now includes Rend, Aegis, Mirror's reflection, the Core's shield and how many enemies a splash will catch.
- **Attack range:** while moving a unit, faint red tiles show where it could fire from the tile under the cursor.
- **"While you waited":** a summary after every enemy turn lists units lost and hurt, properties taken, buildings destroyed, powers used and new enemies spotted. Each line jumps the camera to the spot.
- **Action menu:** it opens on the side away from the enemy, so it never covers a target.
- **Civilians:** they're outlined in amber when your units can reach them, not red like enemies.

### Quality and safety
- **Report a problem:** in the pause menu. It copies a ready-made bug report: version, mission, day, armies, settings and recent errors.
- **What's new:** a screen shown once per version, and from the title menu.
- **Save versions:** saves carry the game version, v0.1 saves still load, and a save that can't load says so.

### Fixes
- Black battle map on first load in a small or still-opening window. The draw loop now survives any single bad frame.
- Clicking past an act card also skipped the first line of dialogue.
- Four cut music tracks were still in the built-in fallback list (404s).
- The title logo was clipped on short windows.
- Leftover old character names in the source ("Brandt", "Mara Voss").
- A rare frozen screen when a unit's move path was interrupted.

### Known issues for v0.3
- 1-6 "Dead Air" is still the hardest early mission for every bot personality.
- AI-vs-AI games often stall after the enemy cap is reached. Human players should be able to break through, but this needs watching.
