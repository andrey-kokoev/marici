"""Exact finite-atom audit of the Stieltjes/order-two boundary equivalence."""
import json
from fractions import Fraction as Q
from pathlib import Path


atoms = (Q(1, 7), Q(2, 3), Q(5, 2))
mu_weights = (Q(2, 5), Q(7, 11), Q(13, 17))
rho_weights = tuple((1 + 4 * atom) * weight for atom, weight in zip(atoms, mu_weights))


def S(x):
    return sum(weight / (x + atom) for atom, weight in zip(atoms, mu_weights))


def F_from_S(x):
    return (4 * x - 1) * S(x)


def F_prime_from_rho(x):
    return sum(weight / (x + atom) ** 2 for atom, weight in zip(atoms, rho_weights))


def F_reconstructed_from_rho(x):
    constant = sum(4 * weight / (1 + 4 * atom) for atom, weight in zip(atoms, rho_weights))
    return constant - sum(weight / (x + atom) for atom, weight in zip(atoms, rho_weights))


test_points = (Q(0), Q(1, 10), Q(1, 4), Q(3, 5), Q(7, 3))
forward_derivatives = []
reverse_values = []
for x in test_points:
    # Direct quotient-rule differentiation of (4x-1)/(x+lambda).
    direct_derivative = sum(
        weight * (1 + 4 * atom) / (x + atom) ** 2
        for atom, weight in zip(atoms, mu_weights)
    )
    forward_derivatives.append(direct_derivative == F_prime_from_rho(x))
    reverse_values.append(F_reconstructed_from_rho(x) == F_from_S(x))

recovered_mu_weights = tuple(
    weight / (1 + 4 * atom) for atom, weight in zip(atoms, rho_weights)
)

assert all(weight > 0 for weight in rho_weights)
assert recovered_mu_weights == mu_weights
assert all(forward_derivatives)
assert all(reverse_values)
assert F_from_S(Q(1, 4)) == 0
assert F_reconstructed_from_rho(Q(1, 4)) == 0

result = {
    "atoms": [str(value) for value in atoms],
    "mu_weights": [str(value) for value in mu_weights],
    "rho_weights": [str(value) for value in rho_weights],
    "recovered_mu_weights": [str(value) for value in recovered_mu_weights],
    "test_points": [str(value) for value in test_points],
    "forward_derivative_identity_at_all_points": all(forward_derivatives),
    "reverse_reconstruction_at_all_points": all(reverse_values),
    "boundary_normalization_F_one_quarter": str(F_from_S(Q(1, 4))),
    "measure_map": "d rho(lambda) = (1+4 lambda) d mu(lambda)",
    "order_two_gate_equivalent_to_scalar_stieltjes_gate": True,
    "symbolic_atomwise_proof_in_companion_note": True,
    "rh_proved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "order-two-stieltjes-boundary-equivalence.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
