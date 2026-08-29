"""Extract exact primitive circuits for finite plus-cap Hall holes."""
import json
import math
import os
from fractions import Fraction

prefix_path = os.path.join(os.path.dirname(__file__),
                           "magnetic_beta_deformation_checks.py")
namespace = {"__file__": prefix_path, "__name__": "cap_circuit_prefix"}
with open(prefix_path, encoding="utf-8") as handle:
    prefix = handle.read().split("checks = []")[0]
exec(compile(prefix, prefix_path, "exec"), namespace)
canonical_column = namespace["canonical_column"]


def subtract(left, right, scalar):
    for key, value in right.items():
        left[key] = left.get(key, Fraction(0)) - scalar * value
        if not left[key]:
            del left[key]


def primitive(relation):
    denominators = [value.denominator for value in relation.values()]
    scale = math.lcm(*denominators)
    integers = {key: int(value * scale) for key, value in relation.items()}
    divisor = math.gcd(*(abs(value) for value in integers.values()))
    integers = {key: value // divisor for key, value in integers.items()}
    first = integers[min(integers)]
    if first < 0:
        integers = {key: -value for key, value in integers.items()}
    return integers


def circuits(beta, g, q, cutoff=20):
    center = 1 - g
    labels = []
    columns = []
    for a in range(cutoff + 1):
        for branch, m in (
            ("minus", center - (q + 2) - a),
            ("plus", center + (q + 2) - a),
        ):
            labels.append((a, branch))
            columns.append(canonical_column(g, a, m, beta))

    basis_by_pivot = {}
    relation_by_pivot = {}
    dependent_plus = []
    retained_plus = []
    for index, (label, source) in enumerate(zip(labels, columns)):
        vector = {key: Fraction(value) for key, value in source.items()}
        relation = {index: Fraction(1)}
        while vector:
            pivot = min(vector)
            if pivot in basis_by_pivot:
                scalar = vector[pivot]
                subtract(vector, basis_by_pivot[pivot], scalar)
                subtract(relation, relation_by_pivot[pivot], scalar)
                continue
            scalar = vector[pivot]
            normalized = {key: value / scalar
                          for key, value in vector.items()}
            normalized_relation = {key: value / scalar
                                   for key, value in relation.items()}
            for old_pivot in list(basis_by_pivot):
                old_basis = basis_by_pivot[old_pivot]
                if pivot in old_basis:
                    factor = old_basis[pivot]
                    subtract(old_basis, normalized, factor)
                    subtract(relation_by_pivot[old_pivot],
                             normalized_relation, factor)
            basis_by_pivot[pivot] = normalized
            relation_by_pivot[pivot] = normalized_relation
            if label[1] == "plus":
                retained_plus.append(label[0])
            break
        else:
            if label[1] == "plus":
                coefficients = primitive(relation)
                dependent_plus.append({
                    "depth": label[0],
                    "support": [
                        {"depth": labels[key][0],
                         "branch": labels[key][1],
                         "coefficient": value}
                        for key, value in coefficients.items()
                    ],
                })
    cap_end = max(retained_plus)
    return [hole for hole in dependent_plus if hole["depth"] <= cap_end]


cases = [
    (4, 2, 4),
    (4, 2, 6),
    (4, 3, 5),
    (4, 4, 1),
    (4, 4, 6),
    (4, 4, 7),
    (4, 2, 5),
    (4, 3, 7),
    (4, 4, 9),
    (3, 3, 6),
]
rows = []
for beta, g, q in cases:
    holes = circuits(beta, g, q)
    rows.append({"beta": beta, "g": g, "q": q, "holes": holes})

output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_cap_circuit_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "exact primitive relation witnesses",
        "cutoff": 20,
        "ordering": "increasing depth, minus before plus",
    },
    "cases": rows,
    "checks": {
        "first_euler_threshold_has_primitive_hole": bool(circuits(4, 2, 4)),
        "first_actual_native_hole_has_primitive_witness":
            bool(circuits(4, 2, 6)),
    },
    "verdict": (
        "The Euler threshold holes carry exact primitive circuits in the full "
        "jet packet; rank-invariant elimination distinguishes them from the "
        "dependent tail."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_cap_circuits.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(json.dumps({
    "case_hole_counts": [
        [row["beta"], row["g"], row["q"], len(row["holes"])]
        for row in rows
    ],
    "checks": output["checks"],
}, sort_keys=True))
raise SystemExit(0 if all(output["checks"].values()) else 1)