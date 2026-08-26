"""Exact provisional Delta m_K likelihood under declared Gaussian assumptions."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp455 = json.loads(
    (root / "results" / "wp455_correlated_kaon_response_constructor.json").read_text(
        encoding="utf-8"
    )
)
wp459 = json.loads(
    (root / "results" / "wp459_executable_kaon_likelihood_kernel.json").read_text(
        encoding="utf-8"
    )
)

# All dimensional entries are in 10^-12 MeV, exactly as displayed in the
# lattice proceedings.  The systematic PDF is an explicit WP460 assumption.
experimental = sp.Rational(871, 250)
experimental_sigma = sp.Rational(3, 500)
sm_lattice = sp.Rational(29, 5)
sm_statistical_sigma = sp.Rational(3, 5)
sm_systematic_sigma = sp.Rational(23, 10)

x = sp.symbols("x", real=True)
x_hat = sp.simplify((experimental - sm_lattice) / experimental)
variance_dimensional = sp.simplify(
    experimental_sigma**2
    + sm_statistical_sigma**2
    + sm_systematic_sigma**2
)
sigma_x = sp.simplify(sp.sqrt(variance_dimensional) / experimental)
minus_two_delta_log_likelihood = sp.simplify((x - x_hat) ** 2 / sigma_x**2)
response_jacobian = sp.diff(sm_lattice / experimental + x, x)

z_95 = sp.Rational(49, 25)
interval_lower = sp.simplify(x_hat - z_95 * sigma_x)
interval_upper = sp.simplify(x_hat + z_95 * sigma_x)

checks = {
    "wp455_dependency_passed": wp455["passed"],
    "wp459_dependency_passed": wp459["passed"],
    "normalized_residual_exact": x_hat == -sp.Rational(579, 871),
    "combined_variance_exact": variance_dimensional
    == sp.Rational(1_412_509, 250_000),
    "normalized_sigma_exact": sigma_x == sp.sqrt(1_412_509) / 1742,
    "cp_even_response_rank_one": response_jacobian == 1,
    "likelihood_curvature_positive": sp.diff(
        minus_two_delta_log_likelihood, x, 2
    )
    > 0,
    "zero_is_inside_working_interval": interval_lower < 0 < interval_upper,
    "central_residual_is_negative": x_hat < 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP460",
    "units": "10^-12 MeV",
    "frozen_inputs": {
        "experimental": str(experimental),
        "experimental_sigma": str(experimental_sigma),
        "SM_lattice": str(sm_lattice),
        "SM_statistical_sigma": str(sm_statistical_sigma),
        "SM_systematic_sigma": str(sm_systematic_sigma),
    },
    "assumptions": [
        "experimental, lattice-statistical, and lattice-systematic errors are independent",
        "all errors are Gaussian",
        "the real BSM mixing contribution is additive",
        "the lattice estimated systematic is used as a Gaussian standard deviation",
    ],
    "normalized_BSM_coordinate": "x=Delta m_K^BSM/Delta m_K^exp=Sigma_K for a real amplitude",
    "x_hat": str(x_hat),
    "sigma_x": str(sigma_x),
    "minus_two_delta_log_likelihood": str(minus_two_delta_log_likelihood),
    "working_95_percent_interval": {
        "exact_lower": str(interval_lower),
        "exact_upper": str(interval_upper),
        "decimal_lower": float(interval_lower.evalf()),
        "decimal_upper": float(interval_upper.evalf()),
    },
    "response_rank": int(response_jacobian),
    "classification": "Provisional executable CP-even likelihood under an added Gaussian systematic model; neither selector nor rigidifier.",
    "selector": False,
    "rigidifier": False,
    "reference_port_required": False,
    "instrument": "Delta m_K experiment plus preliminary lattice SM prediction; likelihood typing is conditional on the declared Gaussian systematic completion.",
    "smallest_exact_falsifier": "Zero response derivative, nonpositive combined variance, or loss of every finite interval under an admitted hostile systematic completion.",
    "remaining_gate": "Perform WP447 pole-by-pole matching in the same convention and test non-Gaussian/enlarged lattice-systematic completions before admitting a numerical scale bound.",
    "sources": [
        "https://arxiv.org/abs/2301.01387",
        "https://pdg.lbl.gov/2025/reviews/rpp2025-rev-conservation-laws.pdf",
    ],
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp460_provisional_deltamk_likelihood.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
