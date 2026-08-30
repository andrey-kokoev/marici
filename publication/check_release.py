#!/usr/bin/env python3
"""Fail closed unless the RH arXiv package satisfies its local release ledger."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "publication" / "rh-proof-ledger.json"
MANUSCRIPTS = [
    ROOT / "papers" / "rh-main" / "main.tex",
    ROOT / "papers" / "rh-foundations" / "main.tex",
]

def main() -> int:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    open_gates = [g["id"] for g in data["gates"] if g["status"] != "closed"]
    missing = [str(path.relative_to(ROOT)) for path in MANUSCRIPTS if not path.is_file()]
    if missing:
        print("FAIL missing manuscript files:", ", ".join(missing))
        return 2
    if open_gates:
        print("NOT RELEASE-READY; open gates:", ", ".join(open_gates))
        return 1
    print("LOCAL RELEASE GATES CLOSED; external submission still requires explicit operator authority.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
