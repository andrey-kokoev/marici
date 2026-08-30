"""Exact parameter-identifiability audit for the WP448-WP449 pole clock."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp447 = json.loads(
    (root / "results" / "wp447_irreducible_adjoint_triplet.json").read_text(
        encoding="utf-8"
    )
)
wp448 = json.loads(
    (root / "results" / "wp448_triplet_pole_residue_packet.json").read_text(
        encoding="utf-8"
    )
)
wp449 = json.loads(
    (root / "results" / "wp449_triplet_width_packet.json").read_text(
        encoding="utf-8"
    )
)
wp456 = json.loads(
    (root / "results" / "wp456_pole_resolved_current_complement.json").read_text(
        encoding="utf-8"
    )
)

g_f, mu, v = sp.symbols("g_F mu v", positive=True, real=True)
m1 = g_f * mu
m3 = sp.sqrt(3) * g_f * mu
width1 = g_f**3 * mu / (4 * sp.pi)
width3 = sp.sqrt(3) * g_f**3 * mu / (4 * sp.pi)
fractional_width = sp.simplify(width1 / m1)
readouts = sp.Matrix([m1, fractional_width])
parameters = sp.Matrix([g_f, mu])
jacobian = readouts.jacobian(parameters)
determinant = sp.factor(jacobian.det())

g_reconstructed = sp.sqrt(4 * sp.pi * fractional_width)
mu_reconstructed = sp.simplify(m1 / g_reconstructed)
f_reconstructed = sp.sqrt(6) * mu_reconstructed
dimensionless_product = sp.simplify(g_reconstructed * f_reconstructed / v)

checks = {
    "wp447_dependency_passed": wp447["passed"],
    "wp448_dependency_passed": wp448["passed"],
    "wp449_dependency_passed": wp449["passed"],
    "wp456_dependency_passed": wp456["passed"],
    "response_jacobian_exact": jacobian
    == sp.Matrix([[mu, g_f], [g_f / (2 * sp.pi), 0]]),
    "response_rank_two_on_positive_domain": determinant == -g_f**2 / (2 * sp.pi),
    "gauge_coupling_reconstruction_exact": sp.simplify(g_reconstructed - g_f) == 0,
    "vacuum_scale_reconstruction_exact": sp.simplify(mu_reconstructed - mu) == 0,
    "dimensionless_product_is_pole_clock_readout": dimensionless_product
    == sp.sqrt(6) * m1 / v,
    "quintet_mass_overidentifies_representation": sp.simplify(m3 / m1)
    == sp.sqrt(3),
    "quintet_width_overidentifies_representation": sp.simplify(width3 / width1)
    == sp.sqrt(3),
    "source_scale_remains_continuous": sp.diff(m1, mu) == g_f,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP457",
    "domain": "WP447 positive g_F,mu vacuum and WP449 conditional above-top, quark-only width support.",
    "source_parameters": ["g_F", "mu"],
    "formal_readouts": ["m_triplet=g_F mu", "Gamma_triplet/m_triplet=g_F^2/(4 pi)"],
    "response_jacobian": [[str(entry) for entry in row] for row in jacobian.tolist()],
    "jacobian_determinant": str(determinant),
    "inverse_reconstruction": {
        "g_F": str(g_reconstructed),
        "mu": str(mu_reconstructed),
        "f": str(f_reconstructed),
        "g_F_f_over_v": str(dimensionless_product),
    },
    "overidentifying_relations": {
        "m_quintet_over_m_triplet": str(sp.simplify(m3 / m1)),
        "Gamma_quintet_over_Gamma_triplet": str(sp.simplify(width3 / width1)),
    },
    "classification": "Rank-two formal parameter-identification readout; neither selector nor rigidifier.",
    "numerical_selector": False,
    "reference_port_required": False,
    "instrument": "Requires a detector-calibrated flavor-tagged two-pole experiment; formal masses and widths alone do not establish reach.",
    "smallest_exact_falsifier": "The positive-domain Jacobian determinant vanishes, or either square-root-three overidentifying relation fails.",
    "remaining_gate": "Derive detector convolution and uncertainty support for a real production/decay channel and test whether its calibrated Jacobian retains rank two at reachable masses.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp457_pole_clock_parameter_identifiability.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
