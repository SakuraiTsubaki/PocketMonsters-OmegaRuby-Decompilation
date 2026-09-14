# Project Status

**Current stage:** Phase 0 — public-source target definition and region/language census

This document tracks decompilation progress, target-version coverage, validation level, and the next major milestones.

## Current operating condition

No local retail ROM, CCI, CIA, RomFS, ExeFS, save dump, or extracted retail asset is available. Current progress is therefore based on public official material, public reverse-engineering implementations, preserved research, and independently reviewable metadata.

The comparison origin is the **Japan-market release**, while market/region and in-game language are tracked separately. Omega Ruby and Alpha Sapphire remain distinct targets even where public tools use shared handlers.

## Version inventory

| Target | Region / market | Language | Revision / update | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| Omega Ruby | Japan | selectable; exact set pending registration | Base / 1.0 | Reference only | Official JP site/manual reviewed; no retail hashes available. |
| Omega Ruby | Japan | selectable; exact set pending registration | Ver.1.4 | Reference only | Nintendo Japan currently records 2015-04-23; binary identity not locally verified. |
| Omega Ruby | Japan | selectable; exact set pending registration | Ver.1.1–1.3 | Unverified | Non-JP official notices corroborate the update series; Japanese-market notices still need explicit recovery. |
| Omega Ruby | Other markets | TBD | Base + applicable updates | Unverified | Region/SKU census pending. |

See `VERSIONS.md` for the authoritative target inventory and `../manifests/source-inventory.csv` for provenance.

## Progress

- [x] Establish repository research/verification conventions.
- [x] Record the no-ROM public-source research condition.
- [x] Adopt Japan-market baseline with separate region/language axes.
- [x] Create initial public-source census and machine-readable source inventory.
- [x] Document initial GARC / BinLinker / LZ11 public-source findings.
- [x] Add synthetic BinLinker/LZ11 tools, tests, and CI.
- [ ] Complete authoritative region/SKU/language/revision/update inventory.
- [ ] Recover and register all Omega Ruby update-history sources by market, with JP notices prioritized.
- [ ] Fully index pk3DS Gen VI/ORAS structures and game configuration mappings.
- [ ] Audit CTRMap-F5 ORAS world/script structures and tests against original CTRMap.
- [ ] Document executable and section layout from public platform/game-specific evidence.
- [ ] Reconstruct scripts, events, data, and asset pipelines from independently documented formats.
- [ ] Add retail-target verification only if a lawful target image becomes available later.

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly in a target build or extracted data.
- **Reproduced** — behavior or data can be recreated with documented steps.
- **Matched** — reconstructed output is verified against the intended target.
- **Reference only** — supported by public evidence and useful for the census, but not directly verified against a local retail target.

Because no retail target is available, public documentation alone must not be mislabeled `Observed` or `Matched` against retail bytes.

## Next milestones

1. Finish the Japan-market Omega Ruby version/update baseline from official and preserved official sources.
2. Enumerate every discovered market/SKU and its selectable language set without conflating market and language.
3. Index `pk3DS` Gen VI/ORAS source in reviewable subsystem batches.
4. Cross-check ORAS world/script claims with CTRMap-F5 and original CTRMap.
5. Update `VERSIONS.md`, manifests, and this status file whenever meaningful coverage is added.
