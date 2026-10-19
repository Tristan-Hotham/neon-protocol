# Neon Protocol: Uprising: changelog

## v0.6.9 (in progress, not shipped)
From the 49-tester playtest of v0.6.8 (docs/playtest-v068/SUMMARY.md): tiers 0 and 1, plus the forecast and fog leaks.
- **Mission end:**
  - Every attack, on either side's turn, now ends with a win/lose check.
  - An enemy turn that fails part-way hands the turn back instead of hanging.
  - Once a second, a safety net checks for a wiped-out side, and restarts an enemy turn that nobody is running.
  - #25's exact softlock didn't reproduce here (a counter-kill on the AI's turn ended the mission correctly in testing), so these nets cover it rather than a single root-cause fix.
- **Saves:**
  - "Back to Map Maker" no longer deletes the real Resume save, and a test play's finish never clears it.
  - Starting Horde, Custom Battle or a skirmish sets the campaign save aside instead of overwriting it. The title screen shows "▶ Resume campaign …", and the set-aside save comes back when the side game ends.
  - The campaign map asks (Resume / Restart / Back) before starting over a mission in progress.
  - Units you buy are autosaved at once.
- **Resume:** couch co-op keeps Player 2 human, and capture and Secure progress is kept for both sides.
- **Overwatch:**
  - The warning is about the tile you stop on, because that's where overwatch fires (it used to warn about the whole route).
  - It asks every time. A map tap or Esc cancels it.
  - It no longer reopens after the move.
  - "Move anyway" can't lock the turn: `commit` is guarded, and no action runs mid-move.
- **Par and hours:**
  - Par N reads "hour (N−1)×3", the hour the HUD shows on turn N, everywhere ("par 6" = "win by hour 15").
  - The after-action graph axis is in hours (a later override still said "day").
  - Dialogue, barks, What's New, the Chronicle and story panels are no longer rewritten.
  - The "a day → a turn" rule is gone, and mechanics text was fixed at the source: civilian income "a turn", Horde "every second turn", crates "every other turn", the boss rules "every third turn", the How to Play day–night line, and cloak fuel. Dai's "ten words a shift" is written that way at the source.
- **Squad:** only introductions go out over the radio. Bond scenes play as a briefing scene again.
- **Forecast:** the counter range is capped at your HP, so it never prints backwards. Damage shows at most 100%. When your shot may kill, the counter row says "(only if it survives your shot)".
- **Fog:**
  - Tapping a hidden enemy's tile says "You can't stop there".
  - "No shot" reasons stay silent for hidden targets.
  - Floating text inside the fog is not shown.
  - Under fog, the objective strip hides unit counts and the pause menu hides enemy funds.
  - The tile panel and the fog shading use the viewing player's vision (they used the Resistance's even on the Overmind side).
- **Gamepad:** a pad press during a battle scene no longer leaves battle scenes switched off for the session.
- **Phone layout, redesigned:**
  - **Portrait:** one row of badges (hour, funds, units, power), then the objective line with 👁 and ☰ at its end. 62px in all, against 170px in v0.6.8. The unit card is a one-line strip (name, type, HP); tap it for the full card. The bar keeps Back, Next and End Turn, plus Build or Power when they apply. Rewind, threat ranges, highlight units, minimap, sound and the enemy general sit behind a "⋯" button, and toggles show "· ON". With a unit selected, the map gets about 79% of an 812px-tall screen.
  - **Landscape:** the HUD is a 66px rail on the left and the buttons an 80px rail on the right, with End Turn at the bottom under the right thumb. The objective floats as a slim line at the top, and the unit strip sits bottom-left. The map gets the full height of the screen, where it used to get about 240 of 375px. The action menu, preview, tips and minimap all sit clear of the rails.
  - PC and tablet layouts are unchanged.
- **Panning:** the map pans past each edge by the HUD covering it plus a quarter of the screen, so the top and bottom rows can be dragged into the middle.
- **Hide the HUD:** a 👁 button (and H on a keyboard) hides everything but the map. Tap "👁 Show UI", press H or Esc, or select a unit to bring it back. It works on PC too.
- **Phones, factory tap:** tapping a factory opened the build list on finger-up, and the browser's follow-up click then landed on the row under the finger, buying it (usually the tank). A touch click whose press began on the map is now ignored. Mouse, keyboard and deliberate taps are unaffected.
- **Characters:**
  - Dai is now Davi "Dai" Ferreira, a white Portuguese-Pacifican docker: lighter skin, brown hair, blue eyes. His lines are unchanged apart from the name.
  - The Architect is now Wren Okada, an East Asian engineer: lighter skin, straight black hair (she keeps her braids), dark eyes. She was Wren Okafor; the name changed everywhere, including the Overmind campaign and the trailer script.
- **Unit chatter:** English mixed with Japanese, Chinese and Korean only. The Tagalog, Hindi, Vietnamese, Indonesian and Singlish ("lah") lines are replaced.
- **Not yet:** the counter-attacker's REND/FLANK/AEGIS and Echo Shard reflection in the forecast, sound in the fog, the Map Maker and superweapon "day" labels. These and tiers 2–5 are queued for v0.7.0 and later.

## v0.6.8 (in progress, not shipped)
From a phone playthrough of 1-2 (375×812, thumbs only, Recruit).
- **Overwatch:** moving through enemy overwatch now opens a card with 48px "✕ Cancel" and "Move anyway ▶" buttons. The old warning was a floating line that was easy to miss, so the second tap walked units into fire. Any other tap dismisses the card.
- **Hours on the result screen:** the row reads "Hours 45 (par 36)", and the after-action graph axis is in hours.
- **Turn start:**
  - The turn banner always clears after 1.5 s.
  - Tips wait while "While you waited" is open, and that report closes after 8 s.
  - The report is a compact card (at most 250px wide on phones).
  - The objective strip, barks and the overwatch card hide during dialogue.
- **1-2:**
  - From turn 6, an Act 1 enemy with half your army or less stops buying, so the last Shredders don't refill every turn.
  - The S-rank budget rises from ¢16,000 to ¢24,000.
- **Secure:** a message gives the progress (e.g. "10/20") and what the building gives you.
- **Factories:** new units leave by the side with the most open ground, not into the doorway.
- **Squad screen:** a member who fights in the slot's unit shows "This mission: fights as a Streetline Trooper".
- **Result card:** a wounded MVP under Casual reads "wounded: sits out the next mission", not "fell in battle".
- **Not changed:**
  - The briefing's map preview looked like an empty strip in the tester's hidden pane. That's very likely its reveal animation not running there, so it needs checking on a real phone.
  - The empty space under the map on phones didn't reproduce. At 375×812 the map is already taller than the space between the bars.
  - The tester read tanks as unable to fire at range 2 after moving. The rules don't do that; what they saw is the machine gun's 1-tile reach against infantry, which the unit card shows as "(MG 1)".

## v0.6.7 (in progress, not shipped)
- **Hours, not days:**
  - A turn is 3 hours. The 8-step day/night cycle is one day on a clock: day at 09:00, 12:00 and 15:00, dusk at 18:00, night at 21:00, 00:00 and 03:00, dawn at 06:00.
  - Missions where the light changes show the clock. Missions locked to one time of day count hours ("HOUR 12"), so a dark map never shows 09:00.
  - On screen, "day N" becomes hour (N−1)×3, "by day N" becomes hour N×3 (so it matches par), and "N days" becomes N×3 hours. The result table reads "Hours".
  - Internally a turn is still `G.day`, so missions, events and saves are unchanged.
- **1-2 pile-up:** in Act 1 the enemy stops buying once its combat units reach about 1.1× your army plus one (at least 5), and keeps the money.
- **One layer at a time:** tips, barks, the action menu, the forecast and toasts hide while a panel or dialogue is open.
- **Shorter intros:** the squad's introductions play as radio barks during your first turn, not as a second dialogue before it.
- **Enemy turns:** the counter adds "IN THE FOG" for unseen units, and "While you waited" counts the moves made in fog.
- **Art:**
  - Ridges are pixel-art mountain ranges with two broad peaks per tile (sometimes a foothill), lit from the left, merged inside a range, snow-capped in winter.
  - Water glints and drifts, slower in the subway. Off with Reduced motion.
  - Day battle scenes dim the window lights, so a rainy day no longer reads as night.
- **Trailer:** `trailer/neon-protocol-story-trailer-web.mp4`, 720p H.264 at 18 MB (the original is 107 MB).
- **Checked:**
  - Saves from v0.6.2 (1-2 and 2-4, mid-mission) load in v0.6.7, keep their state and play a full enemy round with no errors.

## v0.6.6 (in progress, not shipped)
From the v0.6.5 recheck by four testers.
- **Battle scenes:**
  - Snowy maps fight in the snow. The snow check now runs before the industrial one, so 3-3 and 3-5 no longer show a foundry.
  - Every Flooded Subway tile, canals included, gets the tunnel backdrop.
  - The Overmind panel glitch is a brief 2px flicker in the sky, not a tinted band drifting across units.
- **Boss:**
  - The unit card shows real HP (e.g. 76/180), not "10/10".
  - It no longer says "Fogged" while the boss is visible.
  - The boss bar text is 16px and bright.
- **No silent failures:**
  - Booby-trapped and cash crates show a message.
  - Sidebar clicks that can't go through say why: open panel, enemy turn, battle over.
  - A queued unit says when low power is the reason.
  - Campaign missions warn at 80% of the budget and when over it.
- **Enemy turns:**
  - Units you can't see skip camera pans into the fog and the pauses between units.
  - Armies over 24 units move faster.
  - The "processing" line counts the units moved.
- **Phone:**
  - The unit card hides 3.5 s after a tap when nothing is selected.
  - The action menu is slimmer.
  - The enemy-turn report docks top-left.
- **Art:**
  - Spent units stay in their colours, darker, instead of grey.
  - Lakes count as water, so they get foam shorelines.
  - All water has lighter shallows along the shore (so open water reads deeper), rounded corners and thicker foam.
  - Snow ground is desaturated and cool white, with fewer specks.
  - Ridges get rock bands, and snow caps in snow.
  - The Wisp's underside is steel with white jets.
- **Flooded Subway:**
  - Always clear and at least 0.55 dark.
  - Named once ("Flooded Subway", not "Flooded Subway · Neon City").
- **Weather:** snowy missions roll snow instead of rain.
- **Words:**
  - Touch players no longer see "Space / Enter" or "(or O)".
  - Kova's Street Recruit, Informants and Conscription note when a map has no civilians.
  - A first-time Forward Base Rig tip.

## v0.6.5 (in progress, not shipped)
From the second test wave of seven testers, plus two calls from the designer.
- **Balance:**
  - The Overmind's tanks, artillery, rockets, anti-air and SAM are back on tracks like their Resistance twins. Hovering let them cross every river and canal that stopped the identical Resistance units. Only the troop carrier still hovers.
- **Civilians:**
  - Civilians appear only in the story missions that write them in.
  - Custom Battle can still add them, but the setting now defaults to None.
  - Generated campaign maps, Horde and Conquest have none.
  - Civilian buildings stay.
- **Regressions fixed:**
  - Orbital Elevator: tanks always have a road to the enemy base.
  - The first harvester really starts half full, whichever way the Refinery is placed.
  - Snow, ice and terrain backdrops now appear on campaign maps, including 3-1, 3-3 and 3-5, plus industrial backdrops for the foundry and toxic flats.
  - No rain inside the subway.
  - Fallen units stay sharp and rest on the ground.
  - Machine sprites show steel instead of pink, and the Spider-Mech's legs no longer tangle.
  - Beams are thinner.
  - The boss bar shows for either side, in bigger text, and fades when you work under it.
- **Bosses in real HP:** the battle-scene panel, the forecast and the objective line all show boss HP as numbers. The 1-10 and 2-10 tips no longer promise "three bars".
- **Tips:**
  - Tips dock wherever they cover least: away from the selected unit, its move tiles, the forecast, the menu and your army.
  - "While you waited" steps aside while a forecast is open.
  - Leftover radio captions and sidebar messages clear between missions.
- **AI pacing:**
  - The AI pokes from day one.
  - Near its cap it buys at most one or two units a turn.
  - Swarm Node drones count towards its cap.
  - Big armies take shorter pauses.
- **Playing the Overmind:**
  - Boss tips speak to the defender.
  - The civilian line is said once.
  - Tally only promises a replacement it can build.
  - The camera finds your army.
  - Results log a CORRECTION.
  - Civilians who change sides get a line.
- **Fixes:**
  - Overwatch now warns on plain moves too.
  - "No shot" always gives a reason.
  - Counter forecasts have 2 HP of headroom.
  - S rank needs par and budget.
  - Squad last lines fit any vehicle.
  - Tap-to-attack avoids parking on civilian buildings.
  - No two civilians share a tile.
  - Team rings are drawn as pixels, and spent units keep their colour.
- **Accessibility and phones:**
  - Settings → Display → Clear view, offered when you pick Largest text.
  - Largest text now reaches the title screen and story cards.
  - Touch wording on short screens.
  - The power meter shows its stars as numbers.
  - Lighter dusk and rain maps.

## v0.6.4 (in progress, not shipped)
From the second AI playtest: eleven testers, judging looks and feel as well as rules.
- **Readability:**
  - Every unit stands on a ring in its army's colour, with a dark ground shadow. The rings sit above the night and fog passes, and can be turned off under Settings → Display.
  - Unit sprites get a dark edge, so they separate from neon props.
  - Bosses are drawn half as big again and get one big HP bar at the top of the screen. The forecast gives boss HP as numbers.
  - The neon and team light pools are softer, and much softer on snow, where they piled up into a magenta haze. The power flash is gentler.
  - A "POWER READY" banner appears, and your portrait pulses, when your power fills.
- **The machines look the part:**
  - The Overmind's sprites have darker plating, serrated dorsal spikes and blooming red eyes.
  - The Spider-Mech stands on long jointed legs, so it no longer reads as a Crawler.
  - The Golem rides on visible hover jets, which explains how it crosses canals.
  - Husk Drones get mandibles and a red spine.
- **Places look like themselves:**
  - Ground is tinted per theme.
  - Snow maps have snow on the ground and ice on the water.
  - Every shoreline has a foam edge.
  - The Flooded Subway has drowned rails and platform edges with yellow safety lines.
  - The Orbital Elevator's tether is one structure, a docking ring with a lit cable. Its info card says it's solid and aircraft only.
- **Battle scenes:**
  - Backdrops per terrain: beach, palms and sea; mountains (snow-capped in snow); dunes; a flooded tunnel; and the tether in the elevator sky. The neon city no longer appears behind everything.
  - One sun or moon per scene, drawn in pixels.
  - Rain falls on the pixel grid.
  - Soldiers drop flat instead of tumbling with sheared pixels.
  - Destroyed vehicles stay as burning wrecks instead of fading out.
- **AI pacing:**
  - The AI ramps up aggression with the day, its strength and its savings, so it no longer sits on ¢40,000 waiting.
  - It stops buying once it outnumbers you by a margin, so no more Shredder floods.
  - It builds from factories with its own unit parked on them.
  - Moves made entirely in fog don't animate.
  - Horde waves land about 14 tiles from your line.
  - A Refinery's free harvester arrives half full.
- **Interaction fixes:**
  - Paths go round civilians instead of stopping short and wasting the turn. Tapping a tile you can't stop on says why.
  - Tap-to-attack picks the safest tile: no overwatch on the way, keeps its distance, fewest enemies next to it. It asks for a second tap if the route crosses overwatch.
  - The forecast includes the enemy's luck on Cyber-Nightmare and warns in red when the counter-attack will destroy your unit.
  - The sidebar's $ Sell tool needs a second tap.
  - Factory panels close after a purchase and say how much you're short for units you can't afford.
  - The Rewind label resets after its 2-second window.
- **Modes:**
  - Co-op Player 2 gets their own commander.
  - Leaving a Conquest battle asks first.
  - Conquest's Port cruiser starts on water.
  - Horde saves your best wave when you quit.
  - Map Maker test games award no medals.
  - Disabled buttons look disabled.
- **Text and story:**
  - Intel matchups no longer list a unit as both strong and weak against the same enemy. Gleaner and Halcyon are listed, and Gleaners pay the raid bounty.
  - Briefings name the enemy units, warn when more are coming, show "Your setting" separately from "Mission difficulty", and hide Par on survival and Horde maps.
  - Tips:
    - Rule tips jump the queue.
    - Tips are opaque and move away from the unit you're using.
    - Stale tips close at your next turn.
    - Phones get touch wording.
  - How to Play has a contents bar. The result screen folds medals below Continue. What's New is filled in for 0.6.3 and 0.6.4.
  - Out-of-date tips fixed: the 2-4 HQ range, income totals, the allied-army tip in solo play, and "night comes next".
  - Named squad members say a last line when they fall.
  - Rin, Yuna and Hemi talk with contractions, and Rin builds the street's New Year kites.
  - Mara no longer recites rules mid-scene, and Yuna no longer yells "Drive-by!" on foot.
  - Japanese: 新パシフィカ, 抵抗軍, 八岐大蛇, portrait kanji now match the name cards, and there's a space before kanji name tags.
  - Difficulty labels show what they mean on your setting. 2-3 and 5-4 are re-rated Fair.

## v0.6.3 (in progress, not shipped)
- **The new rules teach themselves:**
  - A one-time tip the first time each rule matters: the build zone, automatic harvesters, claims, raids, gates, low power, and the ◎ highlight button.
  - The in-game help now describes the build zone, the harvester war and gates. It no longer says buildings go "within 3 tiles of your buildings" or that harvesters move "when you end the turn", both of which were out of date.
- **The build zone is always visible** on base maps, as a dashed ring around each Construction Yard or HQ.
- **The AI plays the harvester war:**
  - It builds Refineries where the most unclaimed Lumenite lies within reach, and puts defences between its Refinery and the enemy.
  - Enemies standing in its claims are worth more to it.
  - Every harvester, yours included, heads for its own side's claims first.
- **Battle scene quality** setting (Auto, High or Standard): Standard draws at 3× for older phones, and Auto picks it on small or low-memory devices.
- **Speech bubbles grow** with Settings → Text size.
- **Sounds** for gates opening and closing, a field changing hands, and a harvester raid.
- **Fixes from four AI playtesters** (a first-timer, a C&C veteran, an Advance Wars veteran, and a phone player on Largest text):
  - **Phones:** text size is now also capped on short screens. On a 390-pixel-tall landscape phone, Largest text pushed the action menu, info cards and damage forecast off the screen, so you couldn't Wait or Fire. Anything zoom pushes off an edge is now pulled back.
  - **Phones:** on short screens the minimap stands down on base maps, so it no longer covers End Turn and the build cameos.
  - Every panel opens scrolled to the top, instead of where the last panel was left.
  - Selling a building takes a second tap.
  - First-time tips about the new rules (build zone, low power, claims) jump the queue, so they arrive when the thing first happens, not days later.
  - **Low power is no longer a death spiral:** a Power Core always builds at full speed, and Refineries keep running.
  - The Orbital Elevator's tether is really solid now: no ground unit can walk on it, only aircraft fly past. Its other Megatowers are unchanged.
  - You can end a move in your own open gate. Before, the gate was offered as a destination but Wait did nothing.
  - A harvester heading for its own side's claim no longer hides the rest of the Lumenite from the game while it drives. Saves and drawing during the AI's turn could see fields missing.
  - In base skirmishes the Overmind starts with a fourth trooper instead of a Resistance engineer.
  - Out-of-date text: the build zone is 6 tiles (the help, Wren's 2-4 briefing and a sidebar error still said 3 or 4), and Boot Camp's Fabricator tip now describes the Factory choice.
  - Settings section counts match what's in each section, and links in panels are readable on the dark background.
  - Picking a building to place brings the camera to your build zone if it's off screen.
  - **REWRITE no longer backfires.** Stolen units used to go home with a full action from inside your lines. They now return dazed and sit out their army's next turn, without the ranks they earned for you. The picker lists every visible enemy, not just 12, with grid positions.
  - **No Fire button? The menu says why.** For example, "only its machine gun hurts Husk Drone, and that reaches 1 tile", or "it can't fire after moving".
  - **2-5 Data Vault:** the briefing now warns that you'll hold the vault for four days, and HYDRA's landing no longer drops a tank next to Doc Hale. The day-5 landing text now matches where the craft come ashore.
  - **A lost mission scores 0 for Speed.** A loss could score nearly as well as a win.
  - SINGULARITY's description says it hits enemy units: it read as though it hurt the Overmind's own army.
  - **Measured difficulty** re-measured with a second sweep. Base-building missions now rate one tier harder: AI-vs-AI play hides how the AI's base snowballs against a person, which the testers felt (1-9, 2-4 and 3-4 are now Hard, and 4-4 Very hard).

## v0.6.2 (2026-10-17)
- **Fix: moves no longer "start, then jump".**
  - A safety timer meant for background tabs also ran in a visible tab. Whenever one frame took longer than 0.25 s, it advanced the game by a quarter-second in one step: 2.5 tiles of movement at once.
  - It now runs only when the tab is really hidden. Tested by freezing the page for 0.4 s mid-move: the unit now carries on smoothly.
  - The tank start-up sound was also lightened (fewer sound generators at once), so the first frame of a tank move stays light on slower devices.

## v0.6.1 (2026-10-17)
From the first full game:
- **Base zone:** you build inside a circle around your Construction Yard (the deployed Rig) or HQ: 6 tiles, or 9 for docks so a coastal base reaches the water. Before, anything within 3 tiles of any of your buildings counted, so a base could creep across the map one wall at a time and the Rig stopped mattering. A second base now means driving a second Rig there.
- **Automatic harvesters:** idle harvesters mine, drive to the nearest Lumenite and unload at a Refinery at the start of your turn, with no camera jumps. Settings → Gameplay → Harvesters switches back to end of turn, so you can give orders first.
- **Civilians:** half as many, and drawn at 60% size so they read as people next to tanks.
- **Highlight my units:** ◎ on the toolbar (or the O key) puts a pulsing ring and a marker on every unit you command, for when army colours look alike.
- **Battle scenes, sharper:**
  - Drawn at three times the resolution, with sprites upscaled using Scale2x and lit from above: rim light, shaded undersides and a faint team-colour glow.
  - Tank treads roll, engines shudder and smoke, hover tanks glow, gunship rotors spin, and soldiers breathe.
  - Destroyed vehicles throw armour plates.
- **Battle-scene backgrounds:** repainted at the same 6× resolution, with finer window grids, shaded tower edges, haze between the city layers and glowing neon signs.
- **Title screen:**
  - Painted at the screen's real pixel density, with a third city layer and haze.
  - Air traffic with light trails, hologram billboards and distant lightning.
  - Three rim-lit Resistance silhouettes on a rooftop, two layers of rain with ripples on the harbour, and a vignette.
  - The menu buttons are frosted glass.
- **Rei's leftovers:**
  - REWRITE: you choose up to three targets from a list (the nearest useful ones are pre-ticked), and they stay yours for two turns. The AI picks nearby units instead of the priciest anywhere.
  - Factories: your own unit on a Fabricator no longer blocks it; the new unit rolls out beside it, one per pad per turn. Tapping a unit that has moved on your pad opens the factory; one that can still move offers Move or Factory.
  - Night briefings say "night (shorter sight)" instead of "Fog: off".
  - The squad deploy screen always appears before your first turn, even when you skip the story.
- **Measured difficulty** on every campaign briefing, from two AI-vs-AI runs per mission on Veteran:
  - Missions are ranked rather than given absolute thresholds, because the AI overstates difficulty by stalling instead of closing games out. The result is 13 Easy, 14 Fair, 16 Hard and 7 Very hard, rising across the acts, with bosses at least Hard.
  - On Recruit the briefing says how much easier the mission plays.
  - The sweep ran on the build before the base-zone and harvester changes, so base-mission labels may shift slightly when re-measured.
- **Chatter:**
  - New lines for capturing, being repaired, last stands, and first sight of a boss.
  - Generals now speak their power line in their own voice during the cut-in.
- **Base defence you can read:** walls join into one barrier, Gates show energy bars that part for your units, and unpowered buildings blink a red ⚡ and spark.
- **Harvester war:**
  - Killing an enemy harvester pays its load plus a ¢1,000 bounty, and the AI hunts harvesters too.
  - Lumenite within 6 tiles of a Refinery is that army's claim, outlined in its colour: +25% when you mine your own, −25% when you mine someone else's.
- **New skirmish terrains:**
  - Flooded Subway: streets drowned into canals, bridges at the crossings.
  - Orbital Elevator: the space-elevator tether in the middle, ringed by a road with spokes to both bases.
  - Both are in Custom Battle and Horde.
- **Fix:** the base-building sidebar no longer lingers over the title screen after you leave a base mission.
- **Dismemberment:**
  - Battle scenes: heavy weapons blow soldiers into head, torso, arms and legs that trail blood and land on the ground. Small arms sometimes take an arm.
  - Map: heavy kills throw recognisable limbs that leave permanent marks.
  - Human gore only appears with Mature on. Overmind drones shed metal limbs and heads with sparks and oil either way.

## v0.6 (2026-10-17)
- **Unit chatter:** speech bubbles over units when they're selected, move off, fire, score a kill or get hit, borrowed from Iron Front '44.
  - The Resistance talk Shin-Pacifica street slang: English code-switching with Japanese, Korean, Mandarin, Tagalog, Hindi, Vietnamese and Indonesian in their own scripts ("Move, 빨리!", "撃て!", "Tara na!", "चलो, चलो!"). Vehicle crews have their own lines.
  - ORACLE's frames talk in probabilities.
  - Overmind machines speak binary in dark red terminal bubbles. Some of it is real 8-bit ASCII (OK, GO, ZAP, DEL, ERR) for anyone who decodes it.
  - Only visible units talk, one bubble each, at most four on screen, and never during instant enemy turns. Settings → Display → Unit chatter turns it off.
- **Sound and picture in step:** every weapon's first report now lands on the frame the muzzle flashes (measured within 20 ms; the tank gun was 140 ms late and the Phantom 400 ms). Bursts finish inside the projectile's flight, and flak now bursts where its shells arrive. Each death sound plays with its animation: a body hits the ground when it lands, a blown-off turret clangs as it comes down, a crashing gunship's dive lasts as long as its fall, and every visual cook-off pop has its own bang.
- **Real recordings blended in:** 25 Freesound recordings (CC0 and CC BY 4.0, shared by Iron Front '44) under the synthesis. They add a recorded body under every explosion, ricochets and metal impacts, recorded death cries (pain grunts with Mature off), boots on gravel for human troops, and looping battlefield and gunfire beds under the map. Weapons stay synthesised. Each file is split into takes, normalised, pitch-nudged and never repeated twice running. Credits are in Settings → Sound → Sound credits and CREDITS.md.
- **Credits:** "Soundtrack composed by Tristan Hotham" on the title screen, the end credits, the now-playing line, the help page and the Settings soundtrack option.
- **Varied death animations:** each death now fits the unit and the weapon, picked at random from the ones that fit. 19 new animations:
  - **Troops:** blown backwards, crumpling to the knees, spun round by the hit, staggering before collapsing. Some lasers set them burning, and some Overmind bolts disintegrate them to ash. The old topple, gibbing and being run over stay in the mix.
  - **Drones:** short-circuit and twitch, have their head blown off, or burst into scrap.
  - **Vehicles:**
    - Any vehicle can be thrown onto its roof, cook off popping for a while, or shatter into four chunks.
    - Tanks can have the turret blown off; it lands a tile away from the hull.
    - Energy weapons sometimes melt a vehicle into slag.
    - Hover units can crash and skid, leaving scrape marks; walkers topple over.
    - The classic fireball wreck still happens too.
  - **Aircraft:** spiral down trailing smoke, or snap in two. **Ships:** capsize, or break their back with bow and stern rising.
  - Each animation leaves its body, wreck or slag on the map for the rest of the mission. With Mature off, there's no blood.
- **The sound of war:** every unit got its own weapon, movement and death sounds, all synthesised live (no samples):
  - **Weapons, each unit its own:** 30 weapon voices.
    - Resistance: rifle bursts with brass tinkle, the sniper's anti-materiel crack with bolt cycle, and the rail-tank's capacitor whine, main-gun boom and breech reload (it used to share a thin coil sound). Also the walker's 40 mm autocannon, a ground-shaking howitzer, a quad pom-pom, rocket ripples, and a rising-chord Prism laser.
    - Overmind: space-opera blasters, from the drones' three-bolt "pew" to rapid repeaters and twin heavy turbo-blasters. The grav tank pulls the bass out of the air before it fires; the Phantom reverse-swells. There's also a buzz-saw spitter, a bass-hum Glare lance, and the Echo lance, whose beam repeats into the distance.
  - **Artillery** is now three sounds: the launch blast, an incoming whistle (a falling moan from the Overmind) timed to the flight, then a heavy impact crump with concussion ring and soil raining down.
  - **Movement for every troop type:**
    - A Resistance fireteam: out-of-step boots, rattling kit and the odd radio squelch.
    - Exo-suit Breachers: heavy boots and servo whine.
    - Creeping snipers, engineers with clinking tools, and Scrappers with chains.
    - Overmind drones marching in lock-step, a limping Revenant, and ORACLE's chiming frames.
    - Footsteps change with the ground: splashing through water, crunching on snow, sharp on concrete, dull on dirt. Tanks rev off before their engine noise.
  - **Deaths:**
    - Infantry fall and their rifle clatters. Drones power down in sparks. Aircraft dive and crash. Ships groan and sink.
    - Vehicles die eight different ways: hull groan, turret blown off, ammo cook-off, fuel fireball, popping tyres with the horn stuck on, hover crash and scrape, a walker toppling, and an Overmind reactor discharge.
  - **Armour:** bullets always ricochet off armoured units, and shells sometimes skid off thick plate with a clang.
  - **War ambience:** distant artillery, machine-gun and rifle fire, aircraft passes, radio chatter, city sirens and Overmind walkers beyond the map edge. It's busier in boss missions, and can be turned off in Settings → Sound.
- **Smaller soundtrack:** re-encoded from Ogg Vorbis at ~127 kbps to Ogg Opus at 64 kbps stereo. 171 MB becomes 86 MB.
  - Every track's length and loudness match the original.
  - The originals are kept in build/music/orig-vorbis.
  - Tool: build/transcode-opus.js.
- **Advanced power:** the Fusion Core (Resistance) and Singularity Core (Overmind) cost ¢6,000 and give +25 power. They need a Tech Lab and a Power Core. Late bases no longer need a carpet of Power Cores, and the AI builds them too.
- **Faction identity:**

  | Faction | Units | Trait |
  |---|---|---|
  | Resistance | **Scrapper**: a field welder that repairs adjacent vehicles. **Kite Drone**: a spotter; indirect fire near it does +15%. | **Street Network**: foot units get +1 vision and +1 cover in cities |
  | Overmind | **Gleaner**: turns scrap into credits. **Swarm Node**: prints a Husk Drone every other turn, at most two alive. | **Nanite Mesh**: machines out of contact self-repair 5 HP a turn |

  The units are cost-matched pairs, and the classic-map mirrored test stays near even.
- **Every leader has a hand-written power theme:**
  - Kova's punk "Chrome Knuckles"
  - Wren's arpeggio "Blueprint Lattice"
  - Sable's near-silent "Dead Channel"
  - Juno's soaring "Above the Smog"
  - ORACLE's glass bells
  - WARDEN-9's drum-corps march
  - HYDRA's three-voice canon
  - MIRROR's palindromes
  - SCOURGE's toxic dub
  - TALLY's clockwork
  - VESPER's night drive
  - the Overmind's "Recycling Hymn" for organ and choir

  Hover a commander card to preview it.
- **Six new Custom Battle enemy styles:**
  - Methodical (masses, then advances)
  - Opportunist (captures and finishes off)
  - Sniper (artillery and trades)
  - Reckless
  - Fortress (walls up, hits back)
  - Blitz

  Every style's build preference now actually shapes what the AI buys. In Conquest, enemy leaders get their own temperament.
- **Story choices (Triangle Strategy style):** four decisions where the cast argues both sides and your pick changes a later mission and the epilogue.
  - **The Flood Gates** (after 2-7): volunteers in 4-2, or extra funds in 4-1 and a different 5-7.
  - **The Ledger of Names** (after S-1): publish it for volunteers and retaliation in 3-1, or keep it sealed.
  - **The Bloom** (before 4-10): burn it for a weaker Leviathan, or let ORACLE contain it, which adds a rig to protect.
  - **Category: Pending** (Overmind side, after 4-3): changes Overmind 4-5 and 4-8.
  - Every decision is listed on the campaign map's ⚖ Decisions panel, in the Chronicle, on affected briefings, and on a "What you chose" epilogue card.
- **4-3 "Evacuation":** this escort mission gave the player a city and an HQ but no factory, while the Overmind had two. Your city is now a Fabricator, the same fix as 3-5.
- **Late-campaign tuning (from "Rei", a hand-played Veteran playtest that won 1 of 9 late missions):**
  - **Bosses were 10–15 times as tough as a tank.** HP cut: WARDEN-9's Bastille Engine 300 → 180, Prism Walker 350 → 250, Toxic Leviathan 400 → 260, Overmind Core 500 → 350. On Recruit, bosses start at 60%.
  - **Bastille Engine** still fires at 1–3 tiles but only returns fire within 2, so mortars at 3 tiles are safe.
  - **Prism Walker** hits 35% softer, and after it fires it stays visible at night until the next day.
  - **Toxic Leviathan** reaches 2–4 tiles (was 2–5) and dives every third day (was every other day). You start 4-10 with three subs (was one).
  - **Weather lifts:** 5-10's storm breaks on day 7, so your bomber and VTOL can fly. 3-1's snow stops on day 9. Both are announced on the briefing.
  - **No hidden surprises:** 2-5's briefing names the 4-day hold at the vault and you start with a Mule transport. 3-5's avalanche lands mid-route instead of on the goal, with a warning the day before.
  - **Par turns** set above the travel time: 1-10 20 → 26, 2-5 14 → 20, 3-1 23 → 30, 3-5 22 → 26, 5-5 24 → 27.
  - **Overmind SINGULARITY** takes 10% off every enemy unit (was 20%).
  - **Squad slots:** a squad member no longer swaps a mortar or a transport for their own cheaper unit (Yuna's bike replaced a ¢6,000 mortar). They now fight in the slot's unit, named.

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
