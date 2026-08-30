#!/usr/bin/env python3
"""Compare subsubleading_memory_exact_checks.json with subsubleading_memory_symbolica_checks.json.

Usage: python checkers/diff_subsubleading_memory_results.py
Exits non-zero on any disagreement in check id sets or per-check passed flags.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RESULTS_DIR = Path(__file__).resolve().parents[1] / "results"
SYMPY_JSON = RESULTS_DIR / "subsubleading_memory_exact_checks.json"
SYMBOLICA_JSON = RESULTS_DIR / "subsubleading_memory_symbolica_checks.json"


def load(path: Path) -> dict:
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    sympy = load(SYMPY_JSON)
    symbolica = load(SYMBOLICA_JSON)
    sympy_checks = {c["id"]: c for c in sympy["checks"]}
    symbolica_checks = {c["id"]: c for c in symbolica["checks"]}

    only_sympy = sorted(set(sympy_checks) - set(symbolica_checks))
    only_symbolica = sorted(set(symbolica_checks) - set(sympy_checks))
    def passed(check: dict) -> bool:
        if "passed" in check:
            return bool(check["passed"])
        return check.get("status") == "pass"

    mismatched = [
        check_id
        for check_id in sorted(set(sympy_checks) & set(symbolica_checks))
        if passed(sympy_checks[check_id]) != passed(symbolica_checks[check_id])
    ]

    print(f"sympy checks: {len(sympy_checks)} from {SYMPY_JSON.name}")
    print(f"symbolica checks: {len(symbolica_checks)} from {SYMBOLICA_JSON.name}")
    print(f"common check ids: {len(set(sympy_checks) & set(symbolica_checks))}")
    print(f"only in sympy: {only_sympy if only_sympy else 'none'}")
    print(f"only in symbolica: {only_symbolica if only_symbolica else 'none'}")
    print(f"passed mismatches: {mismatched if mismatched else 'none'}")

    if only_sympy or only_symbolica or mismatched:
        print("DIFF: engines disagree", file=sys.stderr)
        return 1
    print("DIFF: engines agree on all common checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
