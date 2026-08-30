from fractions import Fraction
import json

# Two-sheet arithmetic witness with positive primitive and square weights.
weights_primitive = [Fraction(4), Fraction(9)]
weights_square = [Fraction(1), Fraction(1)]
x_plus = [Fraction(1), Fraction(-2)]
x_minus = [Fraction(3), Fraction(1)]


def saturated_energy(weights, plus, minus):
    return 2 * sum(w * (a * a + b * b) for w, a, b in zip(weights, plus, minus))


primitive_energy = saturated_energy(weights_primitive, x_plus, x_minus)
square_energy = saturated_energy(weights_square, x_plus, x_minus)

# J(plus,minus)=(-minus,plus) preserves every saturated diagonal grade.
j_plus = [-x for x in x_minus]
j_minus = list(x_plus)
primitive_after_j = saturated_energy(weights_primitive, j_plus, j_minus)
square_after_j = saturated_energy(weights_square, j_plus, j_minus)

# Archimedean five-cell Fourier action: (phi,one,delta,K,V)->(phi,delta,one,-V,K).
cell = [1, 2, 3, 4, 5]


def fourier_cell(v):
    phi, one, delta, k, pv = v
    return [phi, delta, one, -pv, k]


f1 = fourier_cell(cell)
f2 = fourier_cell(f1)
f3 = fourier_cell(f2)
f4 = fourier_cell(f3)

checks = {
    "primitive_saturated_grade_positive": primitive_energy > 0,
    "square_saturated_grade_positive": square_energy > 0,
    "primitive_grade_J_invariant": primitive_after_j == primitive_energy,
    "square_grade_J_invariant": square_after_j == square_energy,
    "archimedean_cell_fourier_fourth_power_identity": f4 == cell,
    "archimedean_cell_norm_preserved": sum(x * x for x in f1) == sum(x * x for x in cell),
    "finite_seminorm_family_separates_witness": primitive_energy > 0 and square_energy > 0,
}

out = {
    "schema": "marici.grothendieck.finite-full-boundary-pro-gram-closure.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "primitive_energy": str(primitive_energy),
        "square_energy": str(square_energy),
        "fourier_cell_once": f1,
        "fourier_cell_four_times": f4,
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

