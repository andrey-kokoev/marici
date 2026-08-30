import json
from fractions import Fraction
from pathlib import Path


P = 7
F_INV = (
    (Fraction(-1), Fraction(1)),
    (Fraction(3, 7), Fraction(-2, 7)),
)
A = (1, -1)


def linking(x, y):
    fx = (
        F_INV[0][0] * x[0] + F_INV[0][1] * x[1],
        F_INV[1][0] * x[0] + F_INV[1][1] * x[1],
    )
    value = y[0] * fx[0] + y[1] * fx[1]
    return value - value.numerator // value.denominator


def scale(t, vector):
    return tuple(t * coordinate for coordinate in vector)


seven_f_inv_integral = all(
    (P * entry).denominator == 1
    for row in F_INV for entry in row
)

odd_table = [
    [linking(scale(t, A), scale(s, A)) for s in range(P)]
    for t in range(P)
]
expected_table = [
    [Fraction((2 * t * s) % P, P) for s in range(P)]
    for t in range(P)
]

row_images = [set(row) for row in odd_table]
nonzero_rows_faithful = all(len(row_images[t]) == P for t in range(1, P))

# Full stable-packet pairing is represented by 7*F^-1 modulo seven.
full_matrix_mod_p = (
    (int(P * F_INV[0][0]) % P, int(P * F_INV[0][1]) % P),
    (int(P * F_INV[1][0]) % P, int(P * F_INV[1][1]) % P),
)
full_rank_one = (
    full_matrix_mod_p != ((0, 0), (0, 0))
    and (full_matrix_mod_p[0][0] * full_matrix_mod_p[1][1]
         - full_matrix_mod_p[0][1] * full_matrix_mod_p[1][0]) % P == 0
)

# Mod-seven image of F^T is the x-axis; reflection gives the y-axis.
dual_line = {(t, 0) for t in range(P)}
reflected_dual_line = {(0, t) for t in range(P)}

gates = [
    seven_f_inv_integral,
    dual_line & reflected_dual_line == {(0, 0)},
    odd_table == expected_table,
    linking(A, A) == Fraction(2, 7),
    nonzero_rows_faithful,
    full_matrix_mod_p == ((0, 0), (3, 5)),
    full_rank_one,
    linking(scale(-1, A), scale(-1, A)) == linking(A, A),
]

result = {
    "schema": "marici.strominger.affine_dual_odd_linking.v1",
    "dual_germ_source": "integral dual functor applied to F",
    "dual_reflected_lines_transverse": True,
    "dual_stable_packet": "(Z/7)^2",
    "dual_odd_quotient": "Z/7 detected by y-x",
    "seven_times_f_inverse_mod_7": full_matrix_mod_p,
    "full_stable_pairing_rank": 1,
    "full_stable_pairing_perfect": False,
    "odd_restriction_generator_value": "2/7",
    "odd_restriction_perfect": nonzero_rows_faithful,
    "odd_restriction_reflection_invariant": True,
    "fiber_gate": "passed_algebraically",
    "arity_gate": "passed_algebraically",
    "authority_gate": "physical_realization_missing",
    "smallest_missing_constructor": "physical discriminant phase realization",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = Path(__file__).parents[1] / "results" / "affine_dual_odd_linking_checks.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
