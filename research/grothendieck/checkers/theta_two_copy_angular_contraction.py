"""Exact finite algebra audit of the two-copy angular contraction identity."""
import json
from fractions import Fraction as Q
from pathlib import Path


def add(left, right):
    return left[0] + right[0], left[1] + right[1]


def multiply(left, right):
    return left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0]


def conjugate(value):
    return value[0], -value[1]


atoms = (Q(-2), Q(1), Q(3))
weights = (Q(2, 7), Q(3, 8), Q(5, 11))
# Rational unit-circle placeholders for exp(i b u). The symmetrization is an
# algebra identity for arbitrary phases, so transcendental evaluation is not needed.
phases = ((Q(1), Q(0)), (Q(3, 5), Q(4, 5)), (Q(-5, 13), Q(12, 13)))
assert all(real * real + imag * imag == 1 for real, imag in phases)

D = (Q(0), Q(0))
N = (Q(0), Q(0))
for atom, weight, phase in zip(atoms, weights, phases):
    D = add(D, (weight * phase[0], weight * phase[1]))
    N = add(N, (weight * atom * phase[0], weight * atom * phase[1]))

product = multiply(N, conjugate(D))
two_copy_real = Q(0)
two_copy_imag = Q(0)
for u, wu, phase_u in zip(atoms, weights, phases):
    for v, wv, phase_v in zip(atoms, weights, phases):
        phase_difference = multiply(phase_u, conjugate(phase_v))
        two_copy_real += wu * wv * (u + v) * phase_difference[0] / 2
        two_copy_imag += wu * wv * (u - v) * phase_difference[1] / 2

assert product[0] == two_copy_real
assert product[1] == two_copy_imag

alpha, beta = Q(-7, 9), Q(13, 10)
cleared_direct = beta * product[0] + alpha * product[1]
cleared_two_copy = beta * two_copy_real + alpha * two_copy_imag
assert cleared_direct == cleared_two_copy

# At b=0, the imaginary derivative of B'/B is the variance of the real tilted
# law. Audit this with the same positive finite measure.
total_weight = sum(weights)
mean = sum(weight * atom for atom, weight in zip(atoms, weights)) / total_weight
second_moment = sum(weight * atom * atom for atom, weight in zip(atoms, weights)) / total_weight
variance = second_moment - mean * mean
assert variance > 0

result = {
    "atoms": [str(value) for value in atoms],
    "weights": [str(value) for value in weights],
    "rational_unit_phases": [[str(part) for part in phase] for phase in phases],
    "N_times_conjugate_D": [str(value) for value in product],
    "two_copy_real_imag": [str(two_copy_real), str(two_copy_imag)],
    "test_alpha_beta": [str(alpha), str(beta)],
    "cleared_direct": str(cleared_direct),
    "cleared_two_copy": str(cleared_two_copy),
    "exact_symmetrization_verified": True,
    "positive_boundary_tilted_mean_test": str(mean),
    "positive_boundary_imaginary_ingress_variance": str(variance),
    "strict_boundary_ingress_for_nondegenerate_measure": True,
    "zero_locations_used": False,
    "inequality_for_riemann_theta_proved": False,
    "rh_proved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-two-copy-angular-contraction.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
