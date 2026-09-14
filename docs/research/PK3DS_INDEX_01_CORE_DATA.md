# pk3DS Index 01 — Generation VI core data structures

## Scope and evidence state

This is the first source-level index of `kwsch/pk3DS` for Generation VI with **Omega Ruby / ORAS emphasis**. It records what the public implementation does; it is not direct observation of this repository's retail target because no local retail image is available.

Pinned upstream revision reviewed:

- repository: `kwsch/pk3DS`
- branch: `master`
- commit: `6daaca934ca2284a73ab743bf89c848c57cd9de1`
- commit date: `2026-02-27`

Evidence class: **A — public implementation evidence**.

## 1. Game selection and initialization

Source: `pk3DS.Core/Game/GameConfig.cs`.

pk3DS classifies extracted layouts with these Generation VI file counts:

| family | file count |
| --- | ---: |
| XY | 271 |
| ORAS demo | 301 |
| ORAS | 299 |

These values are a pk3DS heuristic, not retail fingerprints or proof of equality across markets/revisions.

For ORAS, `GameConfig` selects `GARCReference_AO`, ORAS text-variable/text-reference tables, `PersonalInfoORAS`, `Learnset6`, `Move6`, and `EvolutionSet6`. GARC version is reported as version 4.

### ORAS move-container behavior

Unlike XY, pk3DS reads ORAS move data by taking file 0 of the `move` GARC and unpacking a `Mini` container identified as `WD`; contained records are then parsed as `Move6`.

## 2. pk3DS ORAS logical GARC map

Source: `pk3DS.Core/Game/GARCReference.cs`.

`GARCReference` maps a three-digit logical number to `a/<hundreds>/<tens>/<ones>`. The following are pk3DS's current ORAS labels:

| logical name | number | pk3DS path |
| --- | ---: | --- |
| `encdata` | 013 | `a/0/1/3` |
| `trdata` | 036 | `a/0/3/6` |
| `trclass` | 037 | `a/0/3/7` |
| `trpoke` | 038 | `a/0/3/8` |
| `mapGR` | 039 | `a/0/3/9` |
| `mapMatrix` | 040 | `a/0/4/0` |
| `move` | 189 | `a/1/8/9` |
| `eggmove` | 190 | `a/1/9/0` |
| `levelup` | 191 | `a/1/9/1` |
| `evolution` | 192 | `a/1/9/2` |
| `megaevo` | 193 | `a/1/9/3` |
| `personal` | 195 | `a/1/9/5` |
| `item` | 197 | `a/1/9/7` |
| `gametext` | 071 | `a/0/7/1` + language-relative offset |
| `storytext` | 079 | `a/0/7/9` + language-relative offset |

Normal/super Maison Pokémon/trainer resources, wallpaper and title-screen resources are also named in the same mapping table.

For comparison, XY uses different numbers/paths for essentially all of these major archives. Therefore the project must maintain separate XY and ORAS maps.

### Language-relative paths

pk3DS marks ORAS `gametext` and `storytext` as `LanguageVariant` and applies the selected language integer as an offset from the base GARC number. The retail language-index mapping and cross-region byte identity remain unverified in this project.

## 3. ORAS Pokémon personal data

Sources:

- `PersonalInfoXY.cs`
- `PersonalInfoORAS.cs`
- `PersonalTable.cs`

pk3DS models:

| format | size |
| --- | ---: |
| XY | `0x40` bytes |
| ORAS | `0x50` bytes |

ORAS inherits the XY field model, which exposes six stats, types, catch rate, evolution-stage field, packed EV yield, three held-item slots, gender, hatch cycles, base friendship, EXP growth, egg groups, three abilities, escape rate, form pointers/count, color/sprite bits, base EXP, height, weight, TM/HM and type-tutor compatibility.

pk3DS leaves `0x3C..0x3F` unknown.

ORAS then adds four `0x04`-byte `SpecialTutors` bitfield groups at:

- `0x40..0x43`,
- `0x44..0x47`,
- `0x48..0x4B`,
- `0x4C..0x4F`.

This is a concrete implementation-level ORAS extension over XY.

## 4. Move data

Source: `pk3DS.Core/Structures/Moves/Move6.cs`.

The underlying Generation VI move record is modeled as `0x22` bytes with fields for type, quality, category, power, accuracy, PP, priority, hit count, inflicted-effect metadata, effect probability/duration, turn range, critical stage, flinch, effect-sequence ID, recoil, healing, target, three stat effects/stages/probabilities, and a 32-bit flag field.

For ORAS the additional `WD` Mini packaging layer must be treated separately from the record structure itself.

## 5. Learnsets

Source: `pk3DS.Core/Structures/Learnset.cs`.

`Learnset6` uses 4-byte ordinary entries:

- signed 16-bit move ID,
- signed 16-bit level,

followed by a 32-bit `-1` sentinel in the writer. ORAS uses the same `Learnset6` record model as XY but at a different logical GARC path.

## 6. Evolutions

Source: `pk3DS.Core/Structures/Gen6/Evolutions.cs`.

`EvolutionSet6` is eight 6-byte slots (`0x30` bytes total). Each slot contains 16-bit method, 16-bit method-dependent argument, and 16-bit resulting species.

## 7. Trainer data — explicit ORAS difference

Source: `pk3DS.Core/Structures/Gen6/TrainerData6.cs`.

The class explicitly branches based on ORAS:

### ORAS header

- `Format`: 16-bit,
- `Class`: 16-bit,
- additional 16-bit field (`uORAS` in the reader).

### XY comparison

- `Format`: 8-bit,
- `Class`: 8-bit,
- no corresponding extra 16-bit header field in the same location.

Shared trainer fields include battle type, party count, four items, AI, several unknown bytes, healer flag, money and prize.

Party Pokémon records contain IV byte, packed configuration/PID byte, 16-bit level/species/form, optional held item, and optional four 16-bit moves depending on format flags.

Omega Ruby trainer parsing must therefore not reuse an XY header layout unchanged.

## 8. Encounter handling — ORAS lead

pk3DS separates the wild editors:

- XY: `Gen6/XYWE.cs`
- ORAS: `Gen6/RSWE.cs`

`RSWE.cs` includes commentary contrasting ORAS slot counts/layout with an older XY layout. Detailed encounter parsing is deferred to the next dedicated audit so no UI-code assumptions are prematurely canonicalized.

## 9. Mega Evolution / Rayquaza lead

`Gen6/MegaEvoEditor6.cs` contains an ORAS-specific branch for species entry `384` (Rayquaza), warning that Rayquaza uses a different activation rule and can Mega Evolve if it knows Dragon Ascent.

This is strong implementation evidence for a special-case data/tool path, but the full battle-engine rule still requires independent cross-checking.

## Confidence table

| Finding | State |
| --- | --- |
| reviewed pk3DS revision and listed source files | Reviewed |
| ORAS branch behavior in `GameConfig` / `TrainerData6` / personal table | Public implementation evidence |
| record sizes and offsets | Public implementation evidence |
| ORAS logical GARC purpose/path mapping | Public implementation evidence; retail verification pending |
| Omega Ruby ↔ Alpha Sapphire equality for each mapped resource | Not established by this batch |
| Japan ↔ other-market equality | Unknown |
| retail byte/hash match | Unavailable |

## Next pk3DS batch

1. ORAS wild/DexNav encounter table structure,
2. egg moves,
3. Mega Evolution table,
4. items,
5. Maison,
6. text-reference and language-index tables,
7. ExeFS/CRO mappings and ORAS-specific editors.

Each result must remain pinned to an upstream commit and then be cross-checked against another public implementation where possible.
