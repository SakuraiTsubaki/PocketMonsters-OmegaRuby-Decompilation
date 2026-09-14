# Public Source Census — Pokémon Omega Ruby

This repository assumes **no local retail ROM, CCI, CIA, RomFS, ExeFS, save dump, or extracted game asset is available**. The project therefore reconstructs knowledge from public source code, reverse-engineering documentation, preserved datasets, official material, and independently verifiable secondary references.

This is the master census. Listing a source does not certify every claim in it; facts are promoted only after source review and, where possible, independent cross-checking.

## Evidence classes

- **A — implementation evidence:** source code that parses/writes/validates/emulates/edits the structure.
- **B — technical documentation:** reverse-engineering notes and platform/file-format documentation.
- **C — structured preservation data:** event archives, entity/save corpora, machine-readable datasets and preserved metadata.
- **D — official / contemporaneous reference:** official sites, manuals, patch notes, interviews and Nintendo/Pokémon material.
- **E — secondary cross-check:** encyclopedias, databases, guides, forums and community documentation.

## Core public reverse-engineering sources

| Source | Class | Main value | ORAS relevance | Local policy |
|---|---|---|---|---|
| `kwsch/pk3DS` | A | Gen VI GARC handling; personal data, moves, learnsets, evolutions, trainers, encounters, marts and CRO-related editing | direct ORAS support | Treat behavior as implementation evidence; audit license before copying code |
| `TeamEXR/shutan-dev-wiki` | B | Gen VI formats and research notes: GARC, BinLinker, LZ11, scripts, sequences, text/localization, battle, field, UI | Gen VI baseline, partly XY-centric | Verify ORAS applicability independently |
| `Rynbo/CTRMap` | A | Gen VI world/zone editing, collision, props, cameras and NPCs | ORAS + XY | Cross-check parsers and format assumptions |
| `hdent1232/CTRMap-F5` | A | Modern ORAS-heavy world/script research; byte-identical round-trip validation across zones/trainers/areas, script assembler/disassembler, geometry/collision | exceptionally high-value ORAS source | High-priority audit; separate measured facts from README claims until code paths are inspected |
| `gdkchan/Ohana3DS-Rebirth` | A | BCH/model/texture/animation parsing | ORAS graphics | Compare with SPICA and newer importers |
| `gdkchan/SPICA` | A | H3D/BCH serialization/deserialization | ORAS 3D assets | Independent implementation reference |
| `sxrmss/n3ds_importer` | A | GFModel, GFMotion, GFTexture, BCH, PICA200 attributes/materials/textures/animations | explicitly tested for ORAS-era assets | Modern graphics cross-check; keep tested-vs-synthetic distinction |
| `kwsch/PKHeX` | A/C | ORAS save structures, PK6/EK6, WC6, legality/game-version handling | direct ORAS support | Primary public source for save/entity/event formats |
| `projectpokemon/EventsGallery` + Project Pokémon Gen 6 gallery | C/E | WC6/WC6FULL distributions, region/language/event metadata, Secret Base/event preservation | ORAS + XY | Archive metadata/hashes; verify restrictions and completeness |
| `abcboy101/poke-corpus` | C | standardized text corpora and format notes | text-format comparison | Do not mirror bulk copyrighted game text; use format/metadata observations |

## Nintendo 3DS platform sources

- 3dbrew: NCCH/CXI/CFA, RomFS, ExeFS, filesystem services, CRO and related platform structures.
- `3DSGuy/Project_CTR`: `ctrtool`/`makerom` for reading/extracting/building NCCH/CXI/CFA/CCI/CIA, ExeFS and RomFS.
- `azahar-emu/azahar`: Citra-lineage implementation of loaders, filesystems, modules/CROs, GPU and system services.
- devkitPro `citro3d` / `tex3ds`: PICA200 texture formats and compression cross-checks including LZ11.

## ORAS-specific mandatory sweeps

In addition to generic Gen VI structures, this repository must separately census public evidence for:

1. DexNav: search level, potential, hidden abilities, special moves, encounter generation and UI/state data.
2. PokéNav Plus: AreaNav, DexNav, BuzzNav and PlayNav structures.
3. Soaring in the Sky and Mirage Spot data, conditions, timers and encounter tables.
4. Super-Secret Base data, QR/base sharing structures, decorations and trainer teams.
5. Pokémon Contest Spectacular rules/data/UI and Cosplay Pikachu handling.
6. Primal Reversion, Red/Blue Orb behavior, strong-weather abilities and Mega Rayquaza exception logic.
7. Delta Episode scripts, Zinnia, Rayquaza and Deoxys encounter flow.
8. OR↔AS story/team/version differences and exclusive encounters/items.
9. Hoenn map reconstruction versus Ruby/Sapphire/Emerald, including radically changed locations.
10. ORAS move tutors, new Mega Evolutions, new moves/abilities and changed learnsets.
11. Trainer Horde Battles and ORAS-specific battle formats/events.
12. Demo-version structures and differences where public implementations expose them.

## Full domain checklist

- NCCH / ExeFS / RomFS / update-title layout.
- `.code`, CRO modules, relocations and executable boundaries.
- GARC, BinLinker and compression variants.
- Text/control codes/languages/fonts.
- Scripts, engine/native command IDs, sequences and triggers.
- Zones, areas, geometry, collision, props, cameras, NPCs, warps.
- Pokémon personal/form data; moves/learnsets/evolution/TM/tutors.
- Trainers, parties, AI, rewards and battle types.
- Wild/DexNav/horde/fishing/special encounter systems.
- Items/shops/berries/key items/Mega Stones/Orbs.
- Battle mechanics, Mega Evolution, Primal Reversion and weather.
- Models/materials/textures/shaders/animations/UI/icons.
- Audio archives/sequences/banks/streams/cries.
- Saves, PK6/EK6, battle videos, WC6, Pokémon Link and online persisted data.
- PSS/GTS/Wonder Trade/Battle Spot/O-Powers/Amie/Super Training.
- OR↔AS, language, region and revision differences.
- Patch deltas and unused/debug/inaccessible/leftover content.
- Later Gen VII+ descendants only as reverse cross-checks.

## Official and historical material to inventory

- Pokémon/Nintendo official ORAS pages, manuals, launch/promotional material and support pages.
- All ORAS update revisions from 1.0 through 1.4, with official changelogs where recoverable.
- Official localized terminology in every supported language.
- Developer interviews and contemporaneous technical/design descriptions.
- Archived official pages when current sites no longer expose the original material.

## Verification rules

- Never invent offsets, GARC paths, command IDs, file counts, hashes or asset identities.
- Every technical claim must carry a state: observed in implementation / documented / cross-confirmed / provisional.
- Prefer two independent implementations over a single wiki statement.
- XY behavior is not automatically ORAS behavior.
- Omega Ruby behavior is not automatically Alpha Sapphire behavior.
- Patch-specific findings must not be generalized to 1.0.
- Code reuse requires license compatibility and attribution review.
- Publicly downloadable copyrighted game data is not automatically suitable for mirroring; prioritize formats, metadata, checksums, tooling and original documentation.

## Current audit order

1. Index every `pk3DS` Gen6/ORAS structure and GARC/config mapping.
2. Inspect CTRMap-F5 source and tests domain-by-domain, then compare with original CTRMap.
3. Index Project Shutan while tagging XY-only/uncertain statements.
4. Index PKHeX ORAS save/entity/WC6 implementations.
5. Build graphics crosswalk: Ohana3DS ↔ SPICA ↔ n3ds_importer ↔ citro3d/tex3ds.
6. Build platform crosswalk: 3dbrew ↔ Project_CTR ↔ Azahar.
7. Inventory Project Pokémon ORAS events/Secret Base records by language and distribution metadata.
8. Sweep official/archived ORAS material, patch history and localization.
9. Sweep secondary databases, historical forum posts and preservation notes for remaining gaps.

## Status

**Open-ended exhaustive census in progress.** Completeness is tracked by explicit domain coverage and maintained gaps, not by assuming one repository, wiki, search engine or archive is exhaustive.