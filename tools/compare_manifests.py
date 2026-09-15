#!/usr/bin/env python3
"""Compare two decompilation inventory manifests by relative path and SHA-256."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def _index(manifest: dict) -> dict[str, dict]:
    return {entry["path"]: entry for entry in manifest.get("entries", [])}

def compare(left: dict, right: dict) -> dict:
    a, b = _index(left), _index(right)
    result = {"same": [], "changed": [], "only_left": [], "only_right": []}
    for path in sorted(set(a) | set(b)):
        if path not in a: result["only_right"].append(path)
        elif path not in b: result["only_left"].append(path)
        elif a[path].get("sha256") == b[path].get("sha256") and a[path].get("size") == b[path].get("size"): result["same"].append(path)
        else: result["changed"].append({"path": path, "left": a[path], "right": b[path]})
    result["summary"] = {k: len(v) for k, v in result.items() if isinstance(v, list)}
    return result

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("left", type=Path); p.add_argument("right", type=Path); p.add_argument("-o", "--output", type=Path); args = p.parse_args()
    text = json.dumps(compare(json.loads(args.left.read_text(encoding="utf-8")), json.loads(args.right.read_text(encoding="utf-8"))), indent=2, ensure_ascii=False) + "\n"
    if args.output: args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(text, encoding="utf-8")
    else: print(text, end="")
    return 0
if __name__ == "__main__": raise SystemExit(main())
