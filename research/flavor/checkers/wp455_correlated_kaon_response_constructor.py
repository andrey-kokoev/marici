"""Exact WP455 contraction of the published colorless-vector kaon response."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp454 = json.loads(
    (root / "results" / "wp454_kaon_instrument_interface_gate.json").read_text(
        encoding="utf-8"
    )
)

# Leading z_q^12,z_d^12 terms in equation (121) of arXiv:2009.07276.
# Their decimal scientific notation denotes the exact displayed integers below.
lr = -sp.Integer(5_300_000)
rr = sp.Integer(18_000)
ll = sp.Integer(18_000)
response_matrix = sp.Matrix([[ll, lr, rr]])

# Monomial packet (z_q^2, z_q*z_d, z_d^2).  A vectorlike source sets z_q=z_d=z.
vectorlike_monomials = sp.Matrix([1, 1, 1])
correlated_coefficient = (response_matrix * vectorlike_monomials)[0]
same_chirality_ratio = sp.cancel(correlated_coefficient / ll)

# On the coefficient coordinate s=z^2, the response is a nonzero linear map.
s = sp.symbols("s")
sigma = correlated_coefficient * s
coefficient_jacobian = sp.diff(sigma, s)

checks = {
    "wp454_dependency_passed": wp454["passed"],
    "published_response_reads_all_three_source_monomials": response_matrix.rank() == 1
    and all(entry != 0 for entry in response_matrix),
    "vectorlike_ray_is_not_in_response_kernel": correlated_coefficient != 0,
    "correlated_coefficient_exact": correlated_coefficient == -sp.Integer(5_264_000),
    "same_chirality_ratio_exact": same_chirality_ratio == -sp.Rational(2632, 9),
    "coefficient_coordinate_response_rank_one": coefficient_jacobian != 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP455",
    "domain": "Colorless Z-prime down-basis model at 5 TeV; only z_q^12=z_d^12=z is nonzero.",
    "source_restriction": "Vectorlike equality of left- and right-handed off-diagonal couplings, frozen before readout.",
    "monomial_basis": ["(z_q^12)^2", "z_q^12 z_d^12", "(z_d^12)^2"],
    "published_response_row": [int(ll), int(lr), int(rr)],
    "vectorlike_monomial_ray": [1, 1, 1],
    "correlated_response_coefficient": int(correlated_coefficient),
    "ratio_to_one_same_chirality_term": str(same_chirality_ratio),
    "readout": "Sigma_K_Zprime = 2 [M12_K]_BSM/(Delta M_K)_exp, with the displayed mass normalization removed.",
    "classification": "Positive common-frame response constructor; neither selector nor rigidifier.",
    "selector_authority": False,
    "reference_port_required": False,
    "physical_instrument": "Neutral-kaon mixing is physical, but a covariance-bearing complex-amplitude likelihood is not supplied by the response formula.",
    "smallest_exact_falsifier": "The equal-coupling contraction would vanish; instead it equals -5264000.",
    "remaining_gate": "Attach an independently declared likelihood or acceptance region for the complex kaon mixing amplitude, including Standard Model long-distance uncertainty and correlations, in this normalization.",
    "source": "Aebischer et al., arXiv:2009.07276, equations (114), (115), (121) and the Sigma normalization following equations (44)-(46).",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp455_correlated_kaon_response_constructor.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
