"""Finite-range maximal-minor atlas complexity checker."""
from collections import defaultdict
import json
import os
import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
with open(prefix_path, encoding="utf-8") as source_handle:
    exec(source_handle.read().split("checks = []")[0])


checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


summary = defaultdict(lambda: {"max_exchange": 0, "patterns": set()})
nonnested = []
multi_exchange = []
rank_defects = []
cases = 0
for g in range(2, 9):
    for q in range(1, 31):
        previous_alternate = None
        for k in range(0, 21):
            columns = component(g, k, q)
            all_rows = sorted(set().union(*(item.keys() for item in columns)))
            full = sp.Matrix([[item.get(row, 0) for item in columns]
                              for row in all_rows])
            pivot_indices = full.T.rref()[1]
            if len(pivot_indices) < len(columns):
                rank_defects.append((g, q, k, len(columns) - len(pivot_indices)))
                previous_alternate = None
                continue
            primary = hall_rows(columns)
            alternate = [all_rows[index] for index in pivot_indices]
            drop = tuple(sorted(set(primary) - set(alternate)))
            add = tuple(sorted(set(alternate) - set(primary)))
            exchange_count = len(drop)
            summary[(g, q)]["max_exchange"] = max(
                summary[(g, q)]["max_exchange"], exchange_count)
            summary[(g, q)]["patterns"].add((drop, add))
            if exchange_count > 1:
                multi_exchange.append((g, q, k, drop, add))
            if previous_alternate is not None and not set(previous_alternate) <= set(alternate):
                nonnested.append((g, q, k,
                                  sorted(set(previous_alternate) - set(alternate))))
            previous_alternate = alternate
            cases += 1

record("ATLAS.bound", "every injective component needs at most one row exchange",
       not multi_exchange, f"cases={cases}; failures={multi_exchange[:1]}")
record("ATLAS.nested", "every canonical alternate chart remains nested in cutoff",
       not nonnested, f"cases={cases}; failures={nonnested[:1]}")

nontrivial = {key for key, value in summary.items() if value["max_exchange"]}
expected_nontrivial = {(2, 12), (4, 16), (5, 4), (5, 12), (6, 20), (8, 24)}
record("ATLAS.locus", "the nontrivial chart locus is the displayed sparse six-pair set",
       nontrivial == expected_nontrivial, str(sorted(nontrivial)))

patterns = {key: value["patterns"] - {((), ())} for key, value in summary.items()
            if value["max_exchange"]}
expected_patterns = {
    (2, 12): {((1,), (3,))}, (4, 16): {((1,), (3,))},
    (6, 20): {((1,), (3,))}, (8, 24): {((1,), (3,))},
    (5, 4): {((-4,), (-6,))}, (5, 12): {((4,), (2,))}}
record("ATLAS.patterns", "every chart transition is one of three explicit row swaps",
       patterns == expected_patterns, str(patterns))

record("RANK.defects", "rank defects remain confined to the known grade-two loci",
       {(g, q) for g, q, _, _ in rank_defects} == {(2, 1), (2, 7)},
       f"defect_steps={len(rank_defects)}")
record("ATLAS.first", "the first lexicographic nontrivial chart is (g,q)=(2,12)",
       min(nontrivial) == (2, 12), str(min(nontrivial)))

failed = [check for check in checks if check["status"] != "pass"]
serial_patterns = {f"{g},{q}": [[list(drop), list(add)] for drop, add in sorted(value)]
                   for (g, q), value in patterns.items()}
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_atlas_complexity_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "finite-range two-chart atlas theorem",
              "g": [2, 8], "q": [1, 30], "k": [0, 20]},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "transition_patterns": serial_patterns,
    "verdict": "Across every injective component in the scan, a canonical nonzero maximal-minor chart differs from the preferred Hall chart by at most one target row and remains nested with cutoff. Only six (g,q) pairs require any exchange, using three explicit swaps. No three-chart event or nonnested replacement occurs. Rank defects remain only at (2,1),(2,7). This is finite-range evidence for a two-chart Plucker atlas, not an unbounded atlas theorem."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_atlas_complexity.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
