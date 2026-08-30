"""Test fixed constant-coefficient recurrence compression of Euler circuits."""
import json
import os
from fractions import Fraction


def rank(matrix):
    work = [row[:] for row in matrix]
    if not work:
        return 0
    rows = len(work)
    columns = len(work[0])
    pivot = 0
    for column in range(columns):
        selected = next((r for r in range(pivot, rows)
                         if work[r][column]), None)
        if selected is None:
            continue
        work[pivot], work[selected] = work[selected], work[pivot]
        value = work[pivot][column]
        work[pivot] = [entry / value for entry in work[pivot]]
        for r in range(rows):
            if r != pivot and work[r][column]:
                value = work[r][column]
                work[r] = [work[r][j] - value * work[pivot][j]
                           for j in range(columns)]
        pivot += 1
        if pivot == rows:
            break
    return pivot


def admits_order(sequence, order):
    equations = len(sequence) - order
    if equations <= 0:
        return True
    coefficients = []
    augmented = []
    for n in range(order, len(sequence)):
        row = [sequence[n - j - 1] for j in range(order)]
        coefficients.append(row)
        augmented.append(row + [sequence[n]])
    return rank(coefficients) == rank(augmented)


def minimal_order(sequence):
    for order in range(len(sequence) + 1):
        if admits_order(sequence, order):
            return order
    raise AssertionError("finite sequence always has a vacuous recurrence")


def minimal_ratio_degree(sequence):
    for degree in range(len(sequence) + 1):
        matrix = [
            ([sequence[r + 1] * (r ** power)
              for power in range(degree + 1)]
             + [-sequence[r] * (r ** power)
                for power in range(degree + 1)])
            for r in range(len(sequence) - 1)
        ]
        if rank(matrix) < 2 * (degree + 1):
            return degree
    raise AssertionError("finite interpolation must terminate")


def admits_ore_bidegree(sequence, order, degree):
    matrix = [
        [
            sequence[r + shift] * (r ** power)
            for shift in range(order + 1)
            for power in range(degree + 1)
        ]
        for r in range(len(sequence) - order)
    ]
    return rank(matrix) < (order + 1) * (degree + 1)


source_path = os.path.join(os.path.dirname(__file__), "..", "results",
                           "magnetic_second_euler_convolution.json")
with open(source_path, encoding="ascii") as handle:
    source = json.load(handle)

rows = []
for record in source["rows"]:
    beta = record["beta"]
    g = record["g"]
    coefficients = record["target_normalized_coefficients"]
    sequence = [
        Fraction(coefficients.get(f"{beta + r},plus", "0/1"))
        for r in range(g + 1)
    ]
    order = minimal_order(sequence)
    rows.append({
        "beta": beta,
        "g": g,
        "sequence_length": len(sequence),
        "minimal_constant_recurrence_order": order,
        "minimal_first_order_ratio_degree": minimal_ratio_degree(sequence),
    })

ore_bidegrees = [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2)]
ore_audit = []
for order, degree in ore_bidegrees:
    unknowns = (order + 1) * (degree + 1)
    first_determined_grade = order + unknowns - 1
    survivors = []
    for row in rows:
        if row["g"] < first_determined_grade:
            continue
        beta = row["beta"]
        g = row["g"]
        source_row = next(
            record for record in source["rows"]
            if record["beta"] == beta and record["g"] == g)
        coefficients = source_row["target_normalized_coefficients"]
        sequence = [
            Fraction(coefficients.get(f"{beta + r},plus", "0/1"))
            for r in range(g + 1)
        ]
        if admits_ore_bidegree(sequence, order, degree):
            survivors.append({"beta": beta, "g": g})
    ore_audit.append({
        "order": order,
        "degree": degree,
        "unknown_count": unknowns,
        "first_determined_grade": first_determined_grade,
        "survivors_at_or_above_determined_grade": survivors,
    })

grade_shift_residuals = []
for beta in range(2, 9):
    for g in range(2, 20):
        current_record = next(
            record for record in source["rows"]
            if record["beta"] == beta and record["g"] == g)
        next_record = next(
            record for record in source["rows"]
            if record["beta"] == beta and record["g"] == g + 1)
        current = [
            Fraction(current_record["target_normalized_coefficients"].get(
                f"{beta + r},plus", "0/1"))
            for r in range(g + 1)
        ]
        following = [
            Fraction(next_record["target_normalized_coefficients"].get(
                f"{beta + r},plus", "0/1"))
            for r in range(g + 2)
        ]
        residual = [
            following[index] - (current[index - 1] if index else 0)
            for index in range(g + 2)
        ]
        grade_shift_residuals.append({
            "beta": beta,
            "g_to_g_plus_one": g,
            "nonzero_residual_count": sum(bool(value) for value in residual),
        })

orders_by_grade = {
    str(g): sorted({
        row["minimal_constant_recurrence_order"]
        for row in rows if row["g"] == g
    })
    for g in range(2, 21)
}
max_order_by_grade = {
    str(g): max(orders_by_grade[str(g)]) for g in range(2, 21)
}
growth_witnesses = [
    {
        "grade": g,
        "maximum_order": max_order_by_grade[str(g)],
    }
    for g in range(2, 21)
]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_second_euler_recurrence_checks.py",
    "author": "marici.Strominger",
    "scope": {
        "strength": "exact rational finite-sequence recurrence census",
        "audit": "2<=beta<=8, 2<=g<=20",
        "recurrence_class": "homogeneous constant coefficients",
    },
    "rows": rows,
    "fixed_bidegree_ore_audit": ore_audit,
    "grade_shift_residuals": grade_shift_residuals,
    "grade_shift_width_failures": [
        row for row in grade_shift_residuals
        if row["g_to_g_plus_one"] >= 3
        and row["nonzero_residual_count"] != row["g_to_g_plus_one"]
    ],
    "fixed_bidegree_survivor_count": sum(
        len(item["survivors_at_or_above_determined_grade"])
        for item in ore_audit),
    "orders_by_grade": orders_by_grade,
    "growth_witnesses": growth_witnesses,
    "ratio_degrees_by_grade": {
        str(g): sorted({
            row["minimal_first_order_ratio_degree"]
            for row in rows if row["g"] == g
        }) for g in range(2, 21)
    },
    "fixed_ratio_degree_four_falsified": any(
        row["minimal_first_order_ratio_degree"] > 4 for row in rows),
    "order_formula_failures": [
        row for row in rows
        if row["minimal_constant_recurrence_order"] != row["g"] // 2 + 1
    ],
    "maximum_observed_order": max(
        row["minimal_constant_recurrence_order"] for row in rows),
    "bounded_order_four_falsified": any(
        row["minimal_constant_recurrence_order"] > 4 for row in rows),
    "verdict": (
        "Fixed low-order homogeneous constant-coefficient transport is "
        "falsified; this does not exclude variable-coefficient or "
        "source-augmented recurrences."
    ),
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_second_euler_recurrence.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(json.dumps({
    "orders_by_grade": orders_by_grade,
    "maximum_observed_order": output["maximum_observed_order"],
    "bounded_order_four_falsified": output["bounded_order_four_falsified"],
    "order_formula_failure_count": len(output["order_formula_failures"]),
    "fixed_ratio_degree_four_falsified": output["fixed_ratio_degree_four_falsified"],
    "maximum_ratio_degree": max(row["minimal_first_order_ratio_degree"] for row in rows),
    "fixed_bidegree_survivor_count": output["fixed_bidegree_survivor_count"],
    "grade_shift_width_failure_count": len(output["grade_shift_width_failures"]),
}, sort_keys=True))