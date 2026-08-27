"""Exact mixed-differential falsifier and Boolean closure counts."""
import json
import math
from pathlib import Path


p = 7
dh = ((0, 1), (0, 0))
dv = ((0, 0), (1, 0))
zero = ((0, 0), (0, 0))
identity = ((1, 0), (0, 1))


def add(a, b):
    return tuple(tuple((a[i][j] + b[i][j]) % p for j in range(2)) for i in range(2))


def mul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) % p for j in range(2))
        for i in range(2)
    )


mixed = add(mul(dh, dv), mul(dv, dh))
total = add(dh, dv)
counts = {
    str(r): {
        "singletons": math.comb(r, 1),
        "pairs": math.comb(r, 2) if r >= 2 else 0,
        "triples": math.comb(r, 3) if r >= 3 else 0,
        "all_nonempty_subsets": 2**r - 1,
        "binomial_sum": sum(math.comb(r, j) for j in range(1, r + 1)),
    }
    for r in range(1, 8)
}

tests = {
    "horizontal_square_zero": mul(dh, dh) == zero,
    "vertical_square_zero": mul(dv, dv) == zero,
    "mixed_anticommutator_is_identity": mixed == identity,
    "total_square_is_identity": mul(total, total) == identity,
    "three_axes_have_three_three_one_slots": counts["3"]["singletons"] == 3
    and counts["3"]["pairs"] == 3
    and counts["3"]["triples"] == 1,
    "three_axes_have_seven_nonempty_subsets": counts["3"]["all_nonempty_subsets"] == 7,
    "boolean_formula_r_1_through_7": all(
        row["all_nonempty_subsets"] == row["binomial_sum"] for row in counts.values()
    ),
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "deutschian_mixed_axes_boolean_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "mixed_curvature": mixed,
    "boolean_counts": counts,
    "verdict": "strict axiswise differentials do not imply mixed interchange closure",
}

out = Path(__file__).resolve().parents[1] / "results" / "deutschian_mixed_axes_boolean_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
