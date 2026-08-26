"""Exact positive production residues and conditional rate identifiability."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp448 = json.loads(
    (root / "results" / "wp448_triplet_pole_residue_packet.json").read_text(
        encoding="utf-8"
    )
)
wp453 = json.loads(
    (root / "results" / "wp453_current_orientation_fiber.json").read_text(
        encoding="utf-8"
    )
)
wp456 = json.loads(
    (root / "results" / "wp456_pole_resolved_current_complement.json").read_text(
        encoding="utf-8"
    )
)
wp461 = json.loads(
    (root / "results" / "wp461_kaon_conditioned_pole_width_reach.json").read_text(
        encoding="utf-8"
    )
)

I = sp.I
lambdas = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2) / sp.sqrt(3),
]
generators = [matrix / 2 for matrix in lambdas]
rotation = sp.Matrix(
    [
        [1 / sp.sqrt(2), 0, 1 / sp.sqrt(2)],
        [0, 1, 0],
        [-1 / sp.sqrt(2), 0, 1 / sp.sqrt(2)],
    ]
)
transition = sp.Matrix(
    [
        (rotation.conjugate().T * generator * rotation)[0, 1]
        for generator in generators
    ]
)
p1 = sp.Matrix(
    [[sp.sympify(entry) for entry in row] for row in wp448["triplet_projector"]]
)
p3 = sp.Matrix(
    [[sp.sympify(entry) for entry in row] for row in wp448["quintet_projector"]]
)

signed_triplet = sp.simplify((transition.T * p1 * transition)[0])
signed_quintet = sp.simplify((transition.T * p3 * transition)[0])
positive_triplet = sp.simplify((transition.conjugate().T * p1 * transition)[0])
positive_quintet = sp.simplify((transition.conjugate().T * p3 * transition)[0])

g_f, mu, mass, kappa = sp.symbols(
    "g_F mu mass kappa_detector", positive=True, real=True
)
n_color = sp.Integer(3)
entrance_width = sp.simplify(
    n_color * g_f**2 * mass * positive_triplet / (6 * sp.pi)
)
m1 = g_f * mu
event_yield = sp.simplify(kappa * g_f**2 * positive_triplet)
jacobian = sp.Matrix([m1, event_yield]).jacobian(sp.Matrix([g_f, mu]))
determinant = sp.factor(jacobian.det())
g_reconstructed = sp.simplify(2 * sp.sqrt(event_yield / kappa))
mu_reconstructed = sp.simplify(m1 / g_reconstructed)

checks = {
    "wp448_dependency_passed": wp448["passed"],
    "wp453_dependency_passed": wp453["passed"],
    "wp456_dependency_passed": wp456["passed"],
    "wp461_dependency_passed": wp461["passed"],
    "signed_residues_reproduce_wp456": signed_triplet == -sp.Rational(1, 4)
    and signed_quintet == sp.Rational(1, 4),
    "triplet_production_weight_positive": positive_triplet == sp.Rational(1, 4),
    "quintet_production_weight_positive": positive_quintet == sp.Rational(1, 4),
    "production_weights_do_not_cancel": positive_triplet + positive_quintet
    == sp.Rational(1, 2),
    "inclusive_entrance_width_exact": entrance_width
    == g_f**2 * mass / (8 * sp.pi),
    "mass_rate_jacobian_exact": jacobian
    == sp.Matrix([[mu, g_f], [kappa * g_f / 2, 0]]),
    "conditional_rate_response_rank_two": determinant == -kappa * g_f**2 / 2,
    "conditional_inverse_reconstruction_exact": sp.simplify(g_reconstructed - g_f)
    == 0
    and sp.simplify(mu_reconstructed - mu) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP462",
    "domain": "WP447 fixed vacuum, WP453 hostile orientation, and WP449 quark-only pole support.",
    "signed_DeltaF2_residues": {
        "triplet": str(signed_triplet),
        "quintet": str(signed_quintet),
    },
    "positive_production_weights": {
        "triplet": str(positive_triplet),
        "quintet": str(positive_quintet),
    },
    "summed_ds_entrance_width_per_multiplet": str(entrance_width),
    "conditional_event_yield": str(event_yield),
    "mass_rate_jacobian": [[str(entry) for entry in row] for row in jacobian.tolist()],
    "jacobian_determinant": str(determinant),
    "classification": "Source-derived positive production probe and conditional rank-two parameter readout; neither selector nor rigidifier.",
    "selector": False,
    "rigidifier": False,
    "reference_port_required": False,
    "instrument": "A generic dijet rate class exists, but source-specific PDFs, normalization, acceptance, and likelihood are not yet attached.",
    "smallest_exact_falsifier": "Either positive pole weight differs from 1/4 or the mass-rate Jacobian vanishes for positive detector factor and coupling.",
    "remaining_gate": "Freeze a source-specific dsbar+sbar d parton-luminosity, acceptance, efficiency, luminosity, and background likelihood to determine kappa_detector and reach.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp462_positive_production_rate_portal.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
