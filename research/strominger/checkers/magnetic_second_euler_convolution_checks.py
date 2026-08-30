"""Extract the invariant second-threshold Euler convolution circuit."""
import json
import math
import os
from fractions import Fraction

prefix_path = os.path.join(os.path.dirname(__file__),
                           "magnetic_beta_deformation_checks.py")
namespace = {"__file__": prefix_path, "__name__": "second_euler_prefix"}
with open(prefix_path, encoding="utf-8") as handle:
    prefix = handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
canonical_column = namespace["canonical_column"]
rising = namespace["rising"]


def subtract(left, right, scalar):
    for key, value in right.items():
        left[key] = left.get(key, Fraction(0)) - scalar * value
        if not left[key]:
            del left[key]


def branch_column(beta, g, q, depth, branch):
    center = 1 - g
    displacement = q + 2
    m = (center - displacement - depth
         if branch == "minus"
         else center + displacement - depth)
    return canonical_column(g, depth, m, beta)


def relation(beta, g):
    q = 2 * g + beta - 3
    labels = [(0, "minus")]
    labels += [(beta + r, "plus") for r in range(g - 1)]
    labels += [(beta + g, "plus")]
    basis = {}
    provenance = {}
    dependency = None
    for index, (depth, branch) in enumerate(labels):
        vector = {key: Fraction(value) for key, value in
                  branch_column(beta, g, q, depth, branch).items()}
        rel = {index: Fraction(1)}
        while vector:
            pivot = min(vector)
            if pivot in basis:
                scalar = vector[pivot]
                subtract(vector, basis[pivot], scalar)
                subtract(rel, provenance[pivot], scalar)
                continue
            scalar = vector[pivot]
            normalized = {key: value / scalar
                          for key, value in vector.items()}
            normalized_rel = {key: value / scalar
                              for key, value in rel.items()}
            for old_pivot in list(basis):
                if pivot in basis[old_pivot]:
                    factor = basis[old_pivot][pivot]
                    subtract(basis[old_pivot], normalized, factor)
                    subtract(provenance[old_pivot], normalized_rel, factor)
            basis[pivot] = normalized
            provenance[pivot] = normalized_rel
            break
        else:
            dependency = rel
    if dependency is None:
        return labels, None
    target = dependency[len(labels) - 1]
    normalized = {labels[key]: value / target
                  for key, value in dependency.items()}
    return labels, normalized


rows = []
failures = []
for beta in range(2, 9):
    for g in range(2, 21):
        labels, rel = relation(beta, g)
        row = {
            "beta": beta,
            "g": g,
            "q": 2 * g + beta - 3,
            "labels": [f"{depth},{branch}" for depth, branch in labels],
            "predicted_m0_coefficient": f"{((-1) ** g * Fraction(g * rising(beta + g, g - 2), rising(beta, g - 1))).numerator}/{((-1) ** g * Fraction(g * rising(beta + g, g - 2), rising(beta, g - 1))).denominator}",
            "target_normalized_coefficients": {
                f"{depth},{branch}":
                    f"{value.numerator}/{value.denominator}"
                for (depth, branch), value in rel.items()
            } if rel else None,
        }
        rows.append(row)
        if rel is None:
            failures.append(row)

support_failures = []
for beta in range(2, 9):
    for g in range(2, 21):
        q = 2 * g + beta - 3
        m0_support = set(branch_column(beta, g, q, 0, "minus"))
        expected_m0 = {0, 1}
        if m0_support != expected_m0:
            support_failures.append({
                "beta": beta, "g": g, "label": "M_0",
                "actual": sorted(m0_support),
                "expected": sorted(expected_m0),
            })
        for r in list(range(g - 1)) + [g]:
            actual = set(branch_column(
                beta, g, q, beta + r, "plus"))
            expected_min = g - r - 1 if r < g else 0
            if not actual or min(actual) != expected_min:
                support_failures.append({
                    "beta": beta, "g": g, "label": f"P_beta+{r}",
                    "actual": sorted(actual),
                    "expected_frontier": expected_min,
                })

output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_second_euler_convolution_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "exact rational circuit extraction",
        "audit": "2<=beta<=8, 2<=g<=20",
    },
    "support_law": (
        "M_0 has support {0,1}; each admitted P has nonzero lower "
        "frontier min=g-r-1; upper and internal cancellations are permitted"
    ),
    "case_count": len(rows),
    "support_case_count": 7 * 19,
    "support_failures": support_failures,
    "parity_checksum_failures": [
        row for row in rows
        if sum(
            Fraction(value) * ((-1) ** (int(label.split(",")[0]) - row["beta"]))
            for label, value in row["target_normalized_coefficients"].items()
            if label.endswith(",plus")
        ) + Fraction(row["target_normalized_coefficients"]["0,minus"]) != 0
    ],
    "memory_growth_failures": [
        row for row in rows
        if len(row["target_normalized_coefficients"]) < row["g"]
    ],
    "support_sizes_by_grade": {
        str(g): sorted({
            len(row["target_normalized_coefficients"])
            for row in rows if row["g"] == g
        }) for g in range(2, 21)
    },
    "failures": failures,
    "endpoint_formula_failures": [
        row for row in rows
        if row["target_normalized_coefficients"]["0,minus"]
        != row["predicted_m0_coefficient"]
    ],
    "rows": rows,
    "verdict": (
        "Every tested second-threshold terminal column has one exact "
        "grade-length convolution relation on the predicted support."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_second_euler_convolution.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(json.dumps({
    "case_count": len(rows),
    "failure_count": len(failures),
    "endpoint_formula_failure_count": len(output["endpoint_formula_failures"]),
    "support_failure_count": len(support_failures),
    "memory_growth_failure_count": len(output["memory_growth_failures"]),
    "parity_checksum_failure_count": len(output["parity_checksum_failures"]),
    "sample": rows[:5],
}, sort_keys=True))
raise SystemExit(0 if not failures and not output["endpoint_formula_failures"] and not support_failures and not output["memory_growth_failures"] and not output["parity_checksum_failures"] else 1)