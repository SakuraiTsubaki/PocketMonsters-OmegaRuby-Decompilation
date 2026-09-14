# Version Coverage

Use this document as the authoritative inventory of game versions targeted by this decompilation project.

## Baseline policy

The comparison origin for this repository is the **Japan-market release of Pokémon Omega Ruby**. This is a research baseline, not a claim that the Japanese retail build is the development master for every worldwide release.

No local retail ROM, CCI, CIA, RomFS, ExeFS, save dump, or retail hash is currently available. Public documentation and public implementations are therefore reference evidence, not direct retail-byte verification.

Market/region and in-game language are separate axes. The official Japanese Omega Ruby manual confirms that the player selects the in-game language before reaching the title screen and that the selected language cannot be changed during that save. The exact selectable-language set for this title must be separately registered from a directly supporting source rather than inferred only from X/Y.

## Current target inventory

| Status | Market / region | Language | Revision / update | Platform / build | Hashes | Evidence / notes |
| --- | --- | --- | --- | --- | --- | --- |
| Reference only | Japan | selectable; exact set pending source registration | Base / 1.0 | Nintendo 3DS; package and download releases | unknown | Official JP Pokémon/Nintendo pages give a 2014-11-21 domestic release date. Retail build identity and hashes remain unavailable. |
| Reference only | Japan | selectable; exact set pending source registration | Ver. 1.4 | Nintendo 3DS update data | unknown | Nintendo Japan currently records Ver.1.4 distribution on 2015-04-23. Exact update-title metadata and hashes remain unverified locally. |
| Planned | Japan | selectable; exact set pending source registration | Ver. 1.1–1.3 | Nintendo 3DS update data | unknown | Intermediate versions are documented by historical Nintendo material in other markets and secondary preservation sources; Japanese-market notices require explicit recovery/registration before being promoted here. |
| Planned | Markets outside Japan | TBD by market/SKU | Base and all applicable updates | Nintendo 3DS | unknown | Every market/SKU must be enumerated independently; language support must not be used as a proxy for market identity. |

## Official baseline observations already established

- Official Japanese ORAS site: domestic release date `2014-11-21`.
- Nintendo Japan product page: package/download releases and current `Ver.1.4` update notice dated `2015-04-23`.
- Official Japanese Omega Ruby manual: the in-game language is selected before the title screen; the selected language cannot be changed during the save.
- Nintendo Japan states that Nintendo 3DS online-play services for this title ended on `2024-04-09 09:00 JST`; historical functionality and current service state must remain separate in documentation.

These observations do **not** establish retail hashes, title IDs, update-title IDs, executable identities, archive paths, or binary equality with Alpha Sapphire or other markets.

## Required region / language census

For every discovered retail or update target, record independently:

1. game (`Omega Ruby`),
2. market / distribution region,
3. physical vs download distribution where relevant,
4. selectable in-game language set,
5. revision / update version,
6. release or distribution date,
7. title/update identifiers when supported by reliable evidence,
8. hashes when a lawful verified source later becomes available,
9. source IDs from `../manifests/source-inventory.csv`,
10. known differences from the Japan-market baseline and from Alpha Sapphire.

## Status vocabulary

- **Planned** — intended for investigation but not yet verified.
- **Verified** — identity and hashes confirmed.
- **Mapped** — executable/data layout documented.
- **In progress** — active source reconstruction.
- **Matched** — reconstruction verified against the target.
- **Reference only** — supported by public evidence but not directly verified against a local retail target.

## Recording rules

1. Record exact revision/update information whenever known.
2. Prefer cryptographic hashes over filenames as identity evidence.
3. Do not commit retail game images or console keys.
4. Record regional or language differences instead of assuming two releases are identical.
5. Link version-specific findings to relevant documentation or verification issues.
6. Keep market/region, language, version, revision, and update as separate axes.
7. Use the Japan-market release as the comparison origin without treating Japanese-market data as automatically ancestral to every other build.
8. Keep Omega Ruby and Alpha Sapphire as distinct targets even when public tools share handlers for both.
9. Use `unknown`, `TBD`, or `null` rather than filling gaps by inference.
