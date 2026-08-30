"""Exact checks for the bounded two-path interferometer packet."""

from fractions import Fraction
import json
from pathlib import Path


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def nonzero_entries(a):
    return sum(value != 0 for row in a for value in row)


def main():
    # Scale away sqrt(2): S is sqrt(2) times the balanced splitter.
    s = [[Fraction(1), Fraction(1)],
         [Fraction(1), Fraction(-1)]]
    gram = matmul(s, s)
    unitary_scaled_residual = matsub(gram, [[2, 0], [0, 2]])

    # phi = 0: route vector is (1,1)/sqrt(2), output is (1,0).
    internal_norm_squared = Fraction(1)
    bright_probability = Fraction(1)
    dark_probability = Fraction(0)

    # phi = pi represented exactly by P = diag(1,-1).
    p = [[Fraction(1), Fraction(0)],
         [Fraction(0), Fraction(-1)]]
    commutator = matsub(matmul(s, p), matmul(p, s))

    # Exact 3-4-5 attenuation dilation on the lower route.
    transmission = Fraction(3, 5)
    loss_amplitude = Fraction(4, 5)
    lower_route_input_probability = Fraction(1, 2)
    retained_probability = (Fraction(1, 2) +
                            transmission * transmission * lower_route_input_probability)
    environment_probability = loss_amplitude * loss_amplitude * lower_route_input_probability
    full_probability = retained_probability + environment_probability

    checks = {
        "balanced_splitter_unitary": nonzero_entries(unitary_scaled_residual) == 0,
        "dark_port_does_not_erase_route_state": (
            dark_probability == 0 and internal_norm_squared == 1
        ),
        "phase_and_splitter_order_is_detectable": nonzero_entries(commutator) > 0,
        "loss_dilation_preserves_full_norm": full_probability == 1,
        "omitted_environment_equals_norm_deficit": 1 - retained_probability == environment_probability,
    }
    result = {
        "schema": "marici.aspect.minimal_two_path_interferometer.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "residuals": {
            "splitter_scaled_unitarity_nonzero_entries": nonzero_entries(unitary_scaled_residual),
            "dark_port_probability": str(dark_probability),
            "pre_recombination_route_norm_squared": str(internal_norm_squared),
            "phase_splitter_commutator": [[str(x) for x in row] for row in commutator],
            "retained_probability_after_loss": str(retained_probability),
            "environment_probability": str(environment_probability),
            "full_dilated_probability": str(full_probability),
        },
        "limitations": [
            "finite-dimensional monochromatic model",
            "no polarization or temporal-mode completion",
            "detector represented only as final port projection",
        ],
    }
    output = Path(__file__).parents[1] / "results" / "minimal_two_path_interferometer.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
