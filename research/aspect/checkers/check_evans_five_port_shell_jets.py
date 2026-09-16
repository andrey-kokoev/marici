#!/usr/bin/env python3
"""Check supplied finite-multiplicity five-port shell jets without fitting."""
import argparse, json
from pathlib import Path

PORTS = ["ordinary_tail", "regular_derivative", "wall", "reciprocal", "ordered_link"]


def cv(x):
    if isinstance(x, list) and len(x) == 2:
        return complex(x[0], x[1])
    return complex(x)


def pair(z):
    return [z.real, z.imag]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("packet", type=Path)
    ap.add_argument("--tol", type=float, default=1e-12)
    ns = ap.parse_args()
    x = json.loads(ns.packet.read_text(encoding="utf-8"))
    m = x.get("multiplicity")
    rows = x.get("jet_rows", [])
    errors = []
    if not isinstance(m, int) or m < 1:
        errors.append("invalid_multiplicity")
    if not isinstance(rows, list) or (isinstance(m, int) and len(rows) != m):
        errors.append("jet_row_count_mismatch")
    out = []
    for j, row in enumerate(rows if isinstance(rows, list) else []):
        missing = [p for p in PORTS if row.get(p) is None]
        if missing:
            errors.append(f"jet_{j}_missing:" + ",".join(missing))
            continue
        vals = {p: cv(row[p]) for p in PORTS}
        total = sum(vals.values())
        out.append({"jet": j, "ordinary_nonzero": abs(vals[PORTS[0]]) > ns.tol,
                    "total": pair(total), "vanishes": abs(total) <= ns.tol})
    passed = not errors and len(out) == m and all(r["vanishes"] for r in out)
    result = {"complete": not errors, "errors": errors, "jets": out, "passed": passed,
              "claim_boundary": "Checks supplied source-frozen shell values only; it does not establish provenance, all-shell validity, completion, Xi divisibility beyond the stated multiplicity, or RH."}
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if passed else (2 if errors else 1))

if __name__ == "__main__":
    main()
