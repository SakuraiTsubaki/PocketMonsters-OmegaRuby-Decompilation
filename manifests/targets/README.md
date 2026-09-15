# Target Manifests

Store metadata-only identity manifests for locally verified targets here. Do not commit game-image bytes, decrypted keys, console keys, or private local paths.

Recommended naming: `<title>_<region>_<language>_<revision-or-update>_<kind>.json`.
Kinds should distinguish at least `source`, `extracted`, `exefs`, and `romfs`. Every manifest should contain hashes/sizes only.
