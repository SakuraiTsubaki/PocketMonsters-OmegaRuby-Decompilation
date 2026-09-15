# Project Status

**Current stage:** Active decompilation — Phase 0 target identity

This document tracks decompilation progress, target-version coverage, validation level, and the next major milestones.

## Version inventory

| Target | Region | Language | Revision / update | Verification | Notes |
| --- | --- | --- | --- | --- | --- |
| Pokémon Omega Ruby retail target | TBD | TBD | TBD | Unverified | Awaiting locally available source for exact identity manifest |

## Progress

- [x] Establish repository baseline and ROM-exclusion policy
- [x] Add target identity manifest tooling
- [x] Add automated target identity tests
- [ ] Establish authoritative version/revision inventory
- [ ] Document ExeFS/RomFS and executable section layout
- [ ] Map symbols, functions, and major subsystems
- [ ] Document game-data formats and resource containers
- [ ] Reconstruct scripts, events, and behavior
- [ ] Reconstruct asset pipelines and metadata
- [ ] Add reproducible extraction/repacking tooling
- [ ] Add byte-level or behavior-level verification where practical

## Generation VI comparison buckets

- **Omega Ruby specific** — observed only in Omega Ruby or a specific region/revision/update.
- **ORAS common** — independently observed in both Omega Ruby and Alpha Sapphire.
- **Generation VI common** — independently observed across the relevant XY and ORAS targets.

No ORAS addition is projected backward onto XY without direct verification.

## Validation levels

- **Unverified** — proposed or recorded but not independently checked.
- **Observed** — confirmed directly in a target build or extracted data.
- **Reproduced** — behavior or data can be recreated with documented steps.
- **Matched** — reconstructed output is verified against the intended target.

## Next milestones

1. Generate the first exact Pokémon Omega Ruby target identity manifest from a local read-only source.
2. Inventory the extracted ExeFS and RomFS trees.
3. Establish executable/code image section boundaries and address conventions.
4. Select the first executable subsystem and first data archive for reconstruction.
5. Compare verified structures with Alpha Sapphire before promoting anything to **ORAS common**.
6. Compare ORAS-common findings with independently verified XY structures before promoting anything to **Generation VI common**.
