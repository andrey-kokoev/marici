"""Uniform even/odd-q determinant-character discovery checker."""
import json
import os
import sympy as sp

# Reuse the exact path-column and Hall-minor constructors without executing
# the companion checker's census.
prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
with open(prefix_path, encoding="utf-8") as source_handle:
    exec(source_handle.read().split("checks = []")[0])


def predicted(g, q, k):
    a = 2 * k
    if q % 2 == 0:
        return int(q * g * (g + 3) * sp.rf(a, g) * sp.rf(a, g - 1) *
                   (a + g + q - 1))
    return int(-sp.rf(a, g) ** 2 * (a + g - q - 1) *
               (a + g + q - 1))


checks = []
def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


failures = []
skipped = []
ratios = 0
for g in range(2, 9):
    for q in range(2, 12):
        start = q // 2 + 2
        prior = None
        for k in range(0, start + 8):
            columns = component(g, k, q)
            try:
                current = determinant(g, k, q)
            except AssertionError:
                prior = None
                skipped.append((g, q, k))
                continue
            if prior is not None and k >= start:
                actual = sp.Rational(current, prior)
                expected = predicted(g, q, k)
                if actual != expected:
                    failures.append((g, q, k, actual, expected))
                ratios += 1
            prior = current
record("PARITY.closed", "all stable determinant ratios obey the uniform parity formulas",
       not failures, f"ratios={ratios}; failures={failures[:1]}")
record("PARITY.coverage", "the exact comparison covers more than five hundred stable steps",
       ratios > 500, f"ratios={ratios}; skipped={skipped}")

# The scalar chart itself fails at q=12 before the stable threshold, while
# the full component remains injective.  This is a coordinate-minor failure,
# not a new kernel class.
falsifier_columns = component(2, 5, 12)
falsifier_rows = hall_rows(falsifier_columns)
falsifier_minor = sp.Matrix([[item.get(row, 0) for item in falsifier_columns]
                             for row in falsifier_rows])
all_rows = sorted(set().union(*(item.keys() for item in falsifier_columns)))
full_matrix = sp.Matrix([[item.get(row, 0) for item in falsifier_columns]
                         for row in all_rows])
pivot_row_indices = full_matrix.T.rref()[1]
alternate_minor = full_matrix[list(pivot_row_indices), :]
record("CHART.first", "the deterministic scalar chart vanishes at (g,q,k)=(2,12,5)",
       falsifier_minor.det() == 0,
       f"selected_rows={falsifier_rows}")
record("CHART.injective", "the q=12 chart failure is not a kernel birth",
       full_matrix.rank() == len(falsifier_columns) and alternate_minor.det() != 0,
       f"rank={full_matrix.rank()}; alternate_det={alternate_minor.det()}")

even_nonzero = all(predicted(g, q, q // 2 + 2) > 0
                   for g in range(2, 101) for q in range(2, 101, 2))
odd_nonzero = all(predicted(g, q, q // 2 + 2) < 0
                  for g in range(2, 101) for q in range(3, 101, 2))
record("STABLE.even", "every displayed even-q stable character is positive",
       even_nonzero, "2<=g,q<=100")
record("STABLE.odd", "every displayed odd-q stable character is negative and nonzero",
       odd_nonzero, "2<=g,q<=100")

# The odd character's first factor detects the known q=7 circuit exactly.
known_zero = predicted(2, 7, 3)
record("EXCEPTION.q7", "the uniform odd character vanishes at (g,q,a)=(2,7,6)",
       known_zero == 0, f"value={known_zero}")
record("EXCEPTION.factor", "odd-q candidate singularity is exactly a+g=q+1",
       all((predicted(g, q, k) == 0) == (2 * k + g == q + 1)
           for g in range(2, 21) for q in range(3, 31, 2)
           for k in range(1, 16)), "bounded algebraic sweep")

# A parity-blind q=2 substitution must fail at q=4.
witness = (3, 4, 4)
actual = predicted(*witness)
wrong = int(2 * witness[0] * (witness[0] + 3) *
            sp.rf(2 * witness[2], witness[0]) *
            sp.rf(2 * witness[2], witness[0] - 1) *
            (2 * witness[2] + witness[0] + 1))
record("FALSIFIER.qdependence", "dropping explicit q dependence gives a nonzero residual",
       actual - wrong != 0, f"witness={witness}; residual={actual-wrong}")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_parity_transfer_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "finite-range parity law plus first scalar-chart falsifier",
              "g": [2, 8], "q_character": [2, 11],
              "stable_steps_per_block": 8,
              "first_chart_falsifier": {"g": 2, "q": 12, "k": 5}},
    "checks": checks, "n_pass": len(checks) - len(failed), "n_fail": len(failed),
    "verdict": "Stable nested determinant ratios obey uniform even/odd formulas through q=11 in the tested range. At (g,q,k)=(2,12,5), the deterministic nested Hall minor becomes zero and remains a bad scalar chart, although the full component has full column rank and an alternate nonzero maximal minor. Thus scalar determinant transport in one fixed chart is not global. A transfer atlas or invariant-factor state is required; the q=12 event is not a kernel exception."
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_parity_transfer.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
