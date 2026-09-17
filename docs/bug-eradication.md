# Bug / Glitch / Error Eradication — Pocket Monsters Omega Ruby

Status: ACTIVE

## Goal

Remove every reproducible unintended defect from the selected Pocket Monsters Omega Ruby target while preserving intentional Generation VI mechanics, data, content, version-specific behavior, and compatibility constraints.

A defect is not considered fixed until it has: (1) a documented trigger, (2) a confirmed root cause in the selected binary/data, (3) a minimal fix, and (4) a regression test proving the trigger no longer fails and intended neighboring behavior still works.

## Target gate

`config/target.json` is currently unselected. No binary-specific address, symbol, patch, or root-cause claim may be treated as confirmed until the exact release/region/revision/update and hashes are populated.

The latest official ORAS update, Ver. 1.4, is the minimum behavioral baseline. Earlier official fixes must be preserved/backported, including the Ver. 1.2 Hall of Fame/end-credits freeze fix and all cumulative update behavior.

## Initial defect inventory

### Generation VI battle logic shared with XY/ORAS
- Baton Pass + Own Tempo confusion timing
- Charge Beam additional-effect overflow under Serene Grace + pledge rainbow
- Choice-item lock persisting through item-effect suppression/removal
- threshold held items not activating immediately after confusion self-damage

### ORAS battle / presentation
- fainted target briefly showing a newly inflicted status animation
- Hoopa Unbound horde crash edge case
- stale level display after semi-invulnerable turn level-up
- stale level/HP display after Volt Switch/U-turn level-up
- Primal Reversion + Zoroark Illusion interaction glitch
- Sky Drop invisible Pokémon state
- Symbiosis + Eject Button ordering/state glitch
- Toxic sure-hit behavior error
- Trick Room ordering/logic oversight
- type-changing Curse logic glitch
- White Herb + Contrary + O-Power interaction oversight

### ORAS systems / UI / event
- Battle Resort Move Tutor cancellation message uses move name where Pokémon name is expected
- Hall of Fame/end-video freeze in pre-1.2 behavior

### ORAS overworld / map / event
- Battle Resort Day-Care Lad facing/state inconsistency
- disappearing bike during Delta Episode Aster interaction
- Wailmer evolution while Surfing after fishing encounter leading to black-screen freeze
- Hiker TM70 Flash oversight
- Lilycove load-game softlock
- Route 112 Hiker movement glitch
- Route 119 Trainer rematch state glitch

### Shared XY/ORAS UI / graphics / integration
- case-conversion table omissions for added accented characters
- graphics cache flush oversight around 3D/2D transitions
- invalid-input / stale UI text state
- Pokémon-Amie first-interaction reaction state
- Pokémon-Amie sprite freeze/state mismatch
- Pokémon Bank friendship-evolution flag bug: classify as EXTERNAL DEPENDENCY; harden client-side validation if the received state can be detected safely

## Zero-defect workflow

1. Identify exact ROM/update and record hashes in `config/target.json`.
2. Extract and hash NCSD/NCCH, ExeFS, RomFS, code, CRO/modules, archives, scripts, maps, text, graphics, audio, and save-related structures.
3. Reproduce every known defect on the selected baseline and record unaffected/affected revisions.
4. Diff base game against every official update to recover Nintendo/Game Freak fixes before inventing replacements.
5. Audit adjacent code paths for same root-cause families: bounds, stale cache/state, bad flags, missing transaction rollback, race/order bugs, invalid enum/index handling, collision/render mismatch, text/data table omissions.
6. Patch the smallest root cause, not the symptom.
7. Add automated regression tests or deterministic replay/state tests for every fixed defect.
8. Fuzz parsers, save/state transitions, battle state machines, UI menus, script inputs, malformed/edge Pokémon data, map transitions, and communication serialization.
9. Run full story/event/battle/network-offline compatibility regression suites.
10. Mark FIXED only after clean-room reproduction fails on the patched build and all regression checks pass.

## Severity classes

- S0: data loss / save corruption / security / arbitrary invalid-state acceptance
- S1: crash / freeze / softlock / progression blocker
- S2: battle-rule or game-state corruption / duplication / transaction failure
- S3: incorrect data, event, map, UI, audio, graphics, or animation behavior
- S4: cosmetic-only defect with no persistent state impact

## Sources used to seed this inventory

- Nintendo Support — How to Update Pokémon Omega Ruby and Pokémon Alpha Sapphire
- Bulbapedia — List of glitches in Generation VI
- Bulbapedia — List of battle glitches in Generation VI
- Bulbapedia — List of overworld glitches in Generation VI

These sources are leads, not binary proof. The selected ROM/update is authoritative for final reproduction and fixes.
