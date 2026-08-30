"""B_s viability forces loss of the quark-only width-closure certificate."""

import json
import multiprocessing as mp
from pathlib import Path


_original_get_context = mp.get_context
mp.get_context = lambda method=None: _original_get_context(
    "spawn" if method == "fork" else method
)

import flavio
from scipy.optimize import brentq
from wilson import Wilson


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp511 = load("wp511_neutral_b_current_instrument.json")
wp513 = load("wp513_aligned_closure_current_no_go.json")


def delta_ms(coefficient):
    wilson = Wilson(
        {
            "CVLL_bsbs": coefficient,
            "CVRR_bsbs": coefficient,
            "CVLR_bsbs": 2 * coefficient,
        },
        scale=160.0,
        eft="WET",
        basis="flavio",
    )
    return float(flavio.np_prediction("DeltaM_s", wilson))


# Reconstruct the exact quadratic form of DeltaM_s squared along the real
# correlated source ray. The observable is the modulus of an affine mixing
# amplitude, so this is the complete one-dimensional response rather than a
# local linear extrapolation.
fit_step = 1e-10
value_zero = delta_ms(0.0)
value_plus = delta_ms(fit_step)
value_minus = delta_ms(-fit_step)
quadratic_a = (
    value_plus**2 + value_minus**2 - 2 * value_zero**2
) / (2 * fit_step**2)
quadratic_b = (value_plus**2 - value_minus**2) / (2 * fit_step)
quadratic_c = value_zero**2

measurement = flavio.combine_measurements("DeltaM_s")
theory_variance = float(
    wp511["physical_instrument"]["frozen_theory_covariance"][1][1]
)
total_sigma = (
    theory_variance + float(measurement.standard_deviation) ** 2
) ** 0.5
z_95 = 49 / 25
lower_observable = float(measurement.central_value) - z_95 * total_sigma
upper_observable = float(measurement.central_value) + z_95 * total_sigma

# The outer negative endpoint is the more negative root of
# A x^2+B x+C=upper^2. Every negative source point compatible with the stated
# interval has magnitude no larger than this endpoint, including the second
# allowed interval on the far side of the quadratic minimum.
discriminant = quadratic_b**2 - 4 * quadratic_a * (
    quadratic_c - upper_observable**2
)
quadratic_outer_negative = (
    -quadratic_b - discriminant**0.5
) / (2 * quadratic_a)
outer_negative = brentq(
    lambda coefficient: delta_ms(coefficient) - upper_observable,
    2 * quadratic_outer_negative,
    quadratic_outer_negative / 2,
    xtol=1e-25,
    rtol=1e-14,
)
endpoint_prediction = delta_ms(outer_negative)

v_phys_gev = 246.0
maximum_b_over_a_squared = 4 * v_phys_gev**2 * abs(outer_negative)
maximum_b_over_a = maximum_b_over_a_squared**0.5
minimum_cubic_determinant_ratio = 1 / maximum_b_over_a_squared
minimum_global_squared_mass_spread = minimum_cubic_determinant_ratio ** (1 / 3)

checks = {
    "wp511_dependency_passed": bool(wp511["passed"]),
    "wp513_dependency_passed": bool(wp513["passed"]),
    "zero_source_prediction_is_inside_frozen_95_interval": bool(
        lower_observable < value_zero < upper_observable
    ),
    "quadratic_coefficient_is_positive": bool(quadratic_a > 0),
    "outer_likelihood_root_is_negative": bool(outer_negative < 0),
    "full_executable_endpoint_matches_upper_boundary": bool(
        abs(endpoint_prediction - upper_observable) / upper_observable < 1e-10
    ),
    "bs_likelihood_forces_b_over_a_below_three_thousandths": bool(
        maximum_b_over_a < 0.003
    ),
    "cubic_determinant_ratio_exceeds_one_hundred_thousand": bool(
        minimum_cubic_determinant_ratio > 100_000
    ),
    "global_squared_mass_spread_exceeds_forty_eight": bool(
        minimum_global_squared_mass_spread > 48
    ),
    "quark_only_pair_closure_certificate_is_impossible": bool(
        minimum_global_squared_mass_spread > 4
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP515",
    "instrument_interval": {
        "confidence_coordinate": "frozen Gaussian 1.96-sigma interval using WP511 experimental plus theory variance",
        "lower_delta_ms": lower_observable,
        "upper_delta_ms": upper_observable,
        "outer_negative_xs_GeV^-2": outer_negative,
        "endpoint_prediction": endpoint_prediction,
    },
    "source_implication": {
        "aligned_matching": "x_s=-(b/a)^2/(4 v_phys^2)",
        "maximum_b_over_a_squared": maximum_b_over_a_squared,
        "maximum_b_over_a": maximum_b_over_a,
        "minimum_a_squared_over_b_squared": minimum_cubic_determinant_ratio,
    },
    "spectral_implication": {
        "exact_product_identity": "prod(m_a,i^2)/prod(m_b,i^2)=a^2/b^2",
        "minimum_global_squared_mass_spread": minimum_global_squared_mass_spread,
        "old_pair_closure_requirement": "global squared-mass spread below 4",
        "disposition": "The sufficient quark-only total-width certificate is impossible on the aligned B_s-compatible domain. This does not by itself prove a nonzero open decay vertex.",
    },
    "classification": "Executable flavor viability forces a heavy-pole hierarchy incompatible with WP510's quark-only pair-closure certificate on the aligned source branch.",
    "selector": False,
    "rigidifier": False,
    "instrument": "WP511 full quadratic DeltaM_s response with frozen total covariance",
    "smallest_exact_falsifier": "The outer negative 95-percent endpoint implies b/a below about 0.002935 and hence a global squared-pole spread above about 48.79, rather than below four.",
    "remaining_gate": "Compute the mass-ordered gauge eigenvectors, nonabelian and scalar vertices, and every kinematically allowed decay width on a B_s-compatible source domain. Failure of the old sufficient certificate is not permission to set those widths to zero.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp515_bmixing_forced_pole_hierarchy.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
