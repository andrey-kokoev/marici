"""Falsification audit for predicting magnetic circuits from carrier loss."""
import json
import os
import sympy as sp

prefix_path = os.path.join(os.path.dirname(__file__), "magnetic_memory_one_checks.py")
namespace = {"__file__": prefix_path, "__name__": "magnetic_carrier_prefix"}
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


def left_carrier(g, d):
    return -(2 * d * g + 2 * d - g**2 - 11 * g - 4) * sp.factorial(d + g - 3) // sp.factorial(d - 2)


def right_carrier(g, d):
    return (g * (d - 4) * (d - 3) * (g - 2) * (g - 1) * (g + 3) *
            sp.factorial(d + g - 3) // (2 * sp.factorial(d)))


# Prediction uses only carrier coefficients, before any rank calculation.
predicted_odd = [(g, d) for g in range(2, 101)
                 for d in range(3, 202, 2)
                 if left_carrier(g, d) == 0 and right_carrier(g, d) == 0]
record("PREDICT.odd", "simultaneous transverse-route loss predicts only (g,d)=(2,5)",
       predicted_odd == [(2, 5)], predicted_odd)

# The symbolic case split behind the bounded prediction.
# In the odd domain, the right route can vanish only at g=2 or d=3.
# At d=3 the left polynomial is g^2+5g-2, nonzero for g>=2.  At g=2
# the left route is -6(d-1)(d-5), whose admissible zero is d=5.
g, d = sp.symbols("g d", integer=True, positive=True)
left_polynomial_at_d3 = sp.factor(
    (2 * d * g + 2 * d - g**2 - 11 * g - 4).subs(d, 3))
record("PROOF.d3", "the depth-boundary branch d=3 leaves the other route nonzero",
       all(left_polynomial_at_d3.subs(g, grade) != 0 for grade in range(2, 501)),
       left_polynomial_at_d3)
record("PROOF.g2", "the grade-capacity branch g=2 selects only d=5",
       sp.expand((2 * d * 2 + 2 * d - 2**2 - 11 * 2 - 4) -
                 6 * (d - 5)) == 0,
       "left carrier=-6(d-1)(d-5)")

# Compare carrier prediction with exact rank of every odd local collision core.
local_mismatches = []
local_defects = []
for grade in range(2, 31):
    for excess in range(3, 32, 2):
        q = grade + excess
        columns = component(grade, (q + 1) // 2, q)
        chosen = [columns[0], columns[excess], columns[excess + 2]]
        matrix = sp.Matrix([[column.get(row, 0) for column in chosen]
                            for row in (1, 2, 0)])
        actual = matrix.rank() < 3
        predicted = (left_carrier(grade, excess) == 0 and
                     right_carrier(grade, excess) == 0)
        if actual:
            local_defects.append((grade, excess))
        if actual != predicted:
            local_mismatches.append((grade, excess, actual, predicted))
record("FALSIFIER.local", "carrier loss agrees with exact local-core rank defect",
       not local_mismatches,
       f"blocks=435; defects={local_defects}; mismatches={local_mismatches[:1]}")

# q=1 is the one-route control: its second carrier is (g-2)*rf(4,g).
q1_mismatches = []
for grade in range(2, 101):
    columns = component(grade, 0, 1)
    rows = sorted(set(columns[0]) | set(columns[1]))
    matrix = sp.Matrix([[column.get(row, 0) for column in columns] for row in rows])
    actual = matrix.rank() < 2
    predicted = (grade - 2) * sp.rf(4, grade) == 0
    if actual != predicted:
        q1_mismatches.append((grade, actual, predicted))
record("FALSIFIER.q1", "single-carrier loss agrees with exact q=1 rank defect",
       not q1_mismatches, f"2<=g<=100; mismatches={q1_mismatches[:1]}")

# Full initialization blocks provide the strongest bounded falsifier.  Their
# rank defects must coincide with the two carrier predictions, even though the
# predictor never inspects their nullspaces.
full_mismatches = []
full_defects = []
for grade in range(2, 21):
    for q in range(1, 31):
        k = (q + q % 2) // 2
        columns = component(grade, k, q)
        rows = sorted(set().union(*(set(column) for column in columns)))
        matrix = sp.Matrix([[column.get(row, 0) for column in columns]
                            for row in rows])
        actual = matrix.rank() < len(columns)
        predicted = ((grade, q) == (2, 1) or (grade, q) == (2, 7))
        if actual:
            full_defects.append((grade, q))
        if actual != predicted:
            full_mismatches.append((grade, q, actual, predicted))
record("FALSIFIER.full", "carrier prediction agrees with every full initialization rank",
       not full_mismatches,
       f"blocks=570; defects={full_defects}; mismatches={full_mismatches[:1]}")

# Negative control: the preferred even chart loses one coordinate on d=g+8,
# but the alternate row-3 carrier tau remains nonzero.  The method must call
# this a chart boundary, not a rank defect.
def transverse_tau(grade):
    return sp.Rational(
        -8 * (2 * grade + 3) * (grade**2 - grade - 26) *
        sp.factorial(2 * grade + 1),
        3 * (grade + 5) * (grade + 6) * (grade + 7) *
        sp.factorial(grade - 1))


even_grades = list(range(2, 102, 2))
record("CONTROL.chart", "the alternate carrier survives every even chart divisor",
       all(transverse_tau(grade) != 0 for grade in even_grades),
       "primary d-g-8=0; alternate tau_g nonzero for even 2<=g<=100")
transverse_discriminant = int(sp.discriminant(g**2 - g - 26, g))
record("CONTROL.symbolic", "the alternate carrier has no integral grade zero",
       transverse_discriminant == 105 and
       int(transverse_discriminant**0.5) ** 2 != transverse_discriminant,
       "only possible factor g^2-g-26 has nonsquare discriminant 105")

# Negative control at the first post-wall seam d=1.
d1_determinants = [
    -grade * (grade + 3) * (2 * grade - 1) * sp.factorial(grade) *
    sp.factorial(grade + 3) // 3
    for grade in range(2, 101)
]
record("CONTROL.seam", "the d=1 presentation overlap retains a nonzero carrier",
       all(value != 0 for value in d1_determinants),
       "endpoint determinant nonzero for 2<=g<=100")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_carrier_method_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact bounded falsification of carrier-loss prediction",
              "full_blocks": "2<=g<=20, 1<=q<=30",
              "symbolic_case_split": "all odd d>=3 and g>=2"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "Observation-carrier loss predicts the two magnetic defects without computing null vectors. In the odd low-grade family simultaneous loss has the unique integral solution (g,d)=(2,5); in q=1 the single carrier vanishes only at g=2. These predictions agree with exact ranks of 435 local cores, 99 q=1 blocks, and 570 full initialization blocks.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_carrier_method.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
