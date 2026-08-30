"""Exact falsifier: a positive even source measure need not have Loewner curvature."""
import json
from fractions import Fraction
from pathlib import Path


Q = Fraction


def cumulants(radii, weights):
    """Even cumulants through order eight for mass on the pairs +/- radii."""
    total = sum(weights)

    def moment(power):
        return sum(weight * radius**power for radius, weight in zip(radii, weights)) / total

    m2, m4, m6, m8 = (moment(power) for power in (2, 4, 6, 8))
    return (
        m2,
        m4 - 3 * m2**2,
        m6 - 15 * m4 * m2 + 30 * m2**3,
        m8 - 28 * m6 * m2 - 35 * m4**2 + 420 * m4 * m2**2 - 630 * m2**4,
    )


def boundary_jet(radii, weights):
    """Jet of F(t)=(4t-1) ell'(t) at zero from even cumulants."""
    k2, k4, k6, k8 = cumulants(radii, weights)
    f1 = 2 * k2 - k4 / 12
    f2 = 2 * k4 / 3 - k6 / 120
    f3 = k6 / 10 - k8 / 1680
    numerator = 2 * f1 * f3 - 3 * f2**2
    loewner_curvature = numerator / 12
    return (k2, k4, k6, k8), (f1, f2, f3), numerator, loewner_curvature


# The measure assigns probabilities 2/5 to each of +/-1 and 1/10 to each of +/-3.
radii = (Q(1), Q(3))
pair_weights = (Q(4), Q(1))
kappa, jet, numerator, curvature = boundary_jet(radii, pair_weights)

assert jet == (Q(821, 150), Q(-854, 375), Q(14261, 13125))
assert numerator == Q(-721471, 196875)
assert jet[0] > 0
assert curvature < 0

# Record the bounded hostile search that first exposed the witness. This is a
# lexicographic minimality statement only in the displayed finite search box.
first = None
for outer_radius in range(2, 11):
    for inner_radius in range(1, outer_radius):
        for inner_weight in range(1, 11):
            for outer_weight in range(1, 11):
                candidate = boundary_jet(
                    (Q(inner_radius), Q(outer_radius)),
                    (Q(inner_weight), Q(outer_weight)),
                )
                if candidate[1][0] > 0 and candidate[2] < 0:
                    first = (inner_radius, outer_radius, inner_weight, outer_weight)
                    break
            if first is not None:
                break
        if first is not None:
            break
    if first is not None:
        break

assert first == (1, 3, 4, 1)

result = {
    "measure": {
        "support": ["-3", "-1", "1", "3"],
        "probabilities": ["1/10", "2/5", "2/5", "1/10"],
        "pair_radii": [str(value) for value in radii],
        "pair_weight_ratio": [str(value) for value in pair_weights],
    },
    "even_cumulants_k2_k4_k6_k8": [str(value) for value in kappa],
    "F_derivatives_at_zero_1_through_3": [str(value) for value in jet],
    "curvature_numerator_2F1F3_minus_3F2_squared": str(numerator),
    "loewner_curvature_F1F3_over_6_minus_F2_squared_over_4": str(curvature),
    "positive_slope": jet[0] > 0,
    "loewner_curvature_fails": curvature < 0,
    "bounded_search": {
        "integer_radii": "1 <= inner < outer <= 10",
        "integer_pair_weights": "1 <= each <= 10",
        "first_lexicographic_falsifier": list(first),
    },
    "conclusion": "positive even source measure alone does not imply local Loewner positivity",
    "does_not_falsify_actual_xi": True,
    "rh_proved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "positive-even-measure-loewner-curvature-falsifier.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
