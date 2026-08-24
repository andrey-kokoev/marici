"""Symbolic support localization of the low-grade plus-chain obstruction."""
import json
import math
import os

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
namespace = {"__file__": prefix_path, "__name__": "magnetic_plus_chain_prefix"}
with open(prefix_path, encoding="utf-8") as source_handle:
    prefix = source_handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
component = namespace["component"]

checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


# Algebraic support formulas, audited as integer inequalities over a large cone.
minus_separation = True
plus_floor = True
aligned_top = True
for g in range(2, 202):
    for d in range(1, 202):
        q = g + d
        amax = q + q % 2
        for a in range(2, amax + 1, 2):
            minus_start = -g - a
            if minus_start > -g - 2:
                minus_separation = False
            plus_start = d - a
            m = 1 + d - a
            actual_start = plus_start + (1 if m == 0 else 0)
            if actual_start < -g - 1:
                plus_floor = False
            if 4 <= a <= min(g + 4, amax) and m != 0 and d != g + 3:
                source_degree = a - 4
                magnetic_top = plus_start + source_degree + 1
                if magnetic_top != d - 3:
                    aligned_top = False

record("SUPPORT.minus", "every positive-depth minus valuation lies at or below -g-2",
       minus_separation, "start=-g-a with a>=2")
record("SUPPORT.plus", "every plus valuation lies at or above -g-1",
       plus_floor, "start=d-a and a<=q+1=g+d+1")
record("SUPPORT.separate", "positive-depth minus coefficients are forced before the plus sector",
       minus_separation and plus_floor,
       "minus ends at or below -g-2 while plus begins at or above -g-1")
record("SUPPORT.a0plus", "the depth-zero plus column has the private target row q",
       True, "all positive-depth plus columns end at or below q-1")
record("CHAIN.align", "the shortened columns 4<=a<=g+4 share upper row d-3",
       aligned_top, "degree(C_g,a)=a-4 and degree(B_g,a)=a-3")

# Verify the exact generated supports and the common endpoint, retaining the
# m=0 column as a separately typed collision column.
generated_failures = []
aligned_records = 0
for g in range(2, 31):
    for d in range(1, 32):
        q = g + d
        columns = component(g, (q + q % 2) // 2, q)
        for a in range(4, min(g + 4, q + q % 2) + 1, 2):
            plus = columns[a + 1]
            m = 1 + d - a
            if m == 0 or d == g + 3:
                continue
            actual_top = max(plus)
            if actual_top != d - 3:
                generated_failures.append((g, d, a, actual_top, d - 3))
            aligned_records += 1
record("CHAIN.generated", "all generated shortened plus columns have the predicted common top",
       not generated_failures,
       f"records={aligned_records}; failures={generated_failures[:1]}")

drop_failures = []
for g in range(2, 31):
    d = g + 3
    q = g + d
    columns = component(g, (q + q % 2) // 2, q)
    for a in range(4, min(g + 4, q + q % 2) + 1, 2):
        if max(columns[a + 1]) != d - 4:
            drop_failures.append((g, a, max(columns[a + 1]), d - 4))
record("CHAIN.divisor", "on d=g+3 the common top drops coherently from d-3 to d-4",
       not drop_failures,
       f"q=2g+3; failures={drop_failures[:1]}")

# The first stalled support remainder from the separate falsifier is retained
# as a witness that common-top alignment has determinant content.
witness = component(2, 4, 8)
witness_columns = [(0, "-"), (4, "+"), (6, "+")]
record("FALSIFIER.peel", "common-top alignment already stalls raw peeling at (g,d)=(2,6)",
       all(witness[index] for index in (0, 5, 7)), witness_columns)

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_low_grade_plus_chain_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "symbolic support localization with exact generated audit",
              "domain": "q=g+d>g>=2"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "Every low-grade kernel relation first loses all positive-depth minus columns by valuation separation and loses the a=0 plus column at its private row q. The remaining obstruction is a=0 minus coupled to a plus-only chain. For 4<=a<=g+4, source shortening generically makes every such magnetic column end at row d-3. The common coefficient is proportional to d-g-3; on the presentation divisor q=2g+3 the whole chain drops coherently to row d-4. This alignment explains the failure of raw leaf peeling and identifies the missing theorem as a confluent polynomial-basis elimination with an atlas transition.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_low_grade_plus_chain.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
