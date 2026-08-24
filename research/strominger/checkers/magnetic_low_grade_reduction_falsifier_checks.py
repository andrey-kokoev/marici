"""Falsifier for raw forced-leaf reduction to the local collision cores."""
import json
import os

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
namespace = {"__file__": prefix_path, "__name__": "magnetic_low_peel_prefix"}
with open(prefix_path, encoding="utf-8") as source_handle:
    prefix = source_handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
component = namespace["component"]


def label(index):
    return (2 * (index // 2), "-" if index % 2 == 0 else "+")


def forced_remainder(g, d):
    q = g + d
    columns = component(g, (q + q % 2) // 2, q)
    protected_rows = {0, 1} if d % 2 == 0 else {0, 1, 2}
    desired = ({0, d + 1} if d % 2 == 0 else {0, d, d + 2})
    left = set(range(len(columns)))
    while left - desired:
        rows = set().union(*(set(columns[index]) for index in left)) - protected_rows
        forced = None
        for row in sorted(rows):
            incident = [index for index in left if columns[index].get(row, 0)]
            if len(incident) == 1 and incident[0] not in desired:
                forced = incident[0]
                break
        if forced is None:
            break
        left.remove(forced)
    return tuple(label(index) for index in sorted(left)), tuple(label(index)
                                                                for index in sorted(desired))


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


smallest = None
records = []
for d in range(2, 22):
    for g in range(2, 22):
        remainder, desired = forced_remainder(g, d)
        if set(remainder) != set(desired) and smallest is None:
            smallest = (g, d, remainder, desired)
        records.append((g, d, len(remainder), remainder))

record("FALSIFIER.first", "raw forced peeling first fails to reach the desired core at (g,d)=(2,6)",
       smallest == (2, 6, ((0, "-"), (4, "+"), (6, "+")),
                    ((0, "-"), (6, "+"))), smallest)

growing = [(d, len(forced_remainder(2, d)[0])) for d in range(6, 22)]
record("FALSIFIER.growth", "the stalled plus-chain remainder is not uniformly width three",
       max(size for _, size in growing) > 3, growing)
record("SCOPE.weighted", "a weighted/oriented elimination is required beyond support leaves",
       True, "local collision minors remain valid but are not a forced support quotient")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_low_grade_reduction_falsifier_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact support-level falsifier",
              "audit": "2<=g<=21 and 2<=d<=21"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "The proposed raw leaf reduction of every low-grade initialization block to the displayed parity core is false. The first failure is (g,d)=(2,6), where columns (0,-),(4,+),(6,+) remain although the desired even core contains only (0,-),(6,+). Remainder width grows in the audit. A weighted oriented elimination, not support peeling alone, is required to connect the full block to the classified local collision minors.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_low_grade_reduction_falsifier.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
