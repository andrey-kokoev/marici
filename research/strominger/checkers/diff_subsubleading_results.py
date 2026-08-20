"""Zero-mismatch differ for the rung-3 dual-engine exact-check results.

Compares research/strominger/results/subsubleading_triangle_exact_checks.json
(sympy) against subsubleading_triangle_symbolica_checks.json (Symbolica):
identical check-ID sets and identical pass/FAIL status per ID.  Prints every
mismatch; exit code 0 iff there are zero mismatches.
"""
import json
import os
import sys

HERE = os.path.dirname(__file__)
RES = os.path.join(HERE, "..", "results")

with open(os.path.join(RES, "subsubleading_triangle_exact_checks.json"),
          encoding="utf-8") as fh:
    sym = json.load(fh)
with open(os.path.join(RES, "subsubleading_triangle_symbolica_checks.json"),
          encoding="utf-8") as fh:
    rus = json.load(fh)

sym_map = {c["id"]: c["status"] for c in sym["checks"]}
rus_map = {c["id"]: c["status"] for c in rus["checks"]}

mismatches = []
for cid in sorted(set(sym_map) - set(rus_map)):
    mismatches.append(f"{cid}: only in sympy ({sym_map[cid]})")
for cid in sorted(set(rus_map) - set(sym_map)):
    mismatches.append(f"{cid}: only in symbolica ({rus_map[cid]})")
for cid in sorted(set(sym_map) & set(rus_map)):
    if sym_map[cid] != rus_map[cid]:
        mismatches.append(f"{cid}: sympy={sym_map[cid]} symbolica={rus_map[cid]}")

n_common = len(set(sym_map) & set(rus_map))
print(f"sympy checks: {len(sym_map)}, symbolica checks: {len(rus_map)}, "
      f"common: {n_common}")
print(f"sympy summary: {sym['summary']['passed']}/{sym['summary']['total']} passed; "
      f"symbolica summary: {rus['summary']['passed']}/{rus['summary']['total']} passed")
if mismatches:
    print(f"{len(mismatches)} MISMATCH(es):")
    for m in mismatches:
        print("  " + m)
else:
    print("0 mismatches: identical check-ID sets, identical verdict per ID")
sys.exit(1 if mismatches else 0)
