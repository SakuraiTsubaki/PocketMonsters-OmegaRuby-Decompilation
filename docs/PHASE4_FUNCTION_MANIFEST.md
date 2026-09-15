# Phase 4 — Function Boundary and Symbol Manifest

Phase 4 provides the normalized record format used when real ARM11 executable analysis begins for Pokémon X, Y, Omega Ruby, and Alpha Sapphire.

Function boundaries and semantic names are separate claims. A function may be recorded as soon as an address and size are observed, while its neutral identifier remains `sub_XXXXXXXX`. A semantic rename is allowed only when evidence supports it.

`tools/function_manifest.py` records start/end address, size, symbol, validation status (`provisional`, `observed`, `reproduced`, `matched`), evidence, overlap diagnostics, and optional text-segment coverage.

Record boundaries independently per exact title/revision; compare X↔Y and OR↔AS only after each side has its own manifest. Promote behavior to XY common, ORAS common, or Generation VI common only with direct cross-title evidence.

Once the verified local `.code` text segment is available, function-boundary discovery, call/xref extraction, strings/data references, and reconstructed source files can begin. Every reconstructed function retains provenance to its exact observed address range and target identity.
