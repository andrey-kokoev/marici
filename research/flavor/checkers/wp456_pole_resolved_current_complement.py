"""Exact pole resolution of the WP453 hostile flavor-current response."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
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
wp453 = json.loads(
    (root / "results" / "wp453_current_orientation_fiber.json").read_text(
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
k_inverse = sp.Matrix(
    [[sp.sympify(entry) for entry in row] for row in wp448["zero_momentum_kernel"]]
)

r1 = sp.simplify((transition.T * p1 * transition)[0])
r3 = sp.simplify((transition.T * p3 * transition)[0])
weighted = sp.simplify(r1 + r3 / 3)
direct = sp.simplify((transition.T * k_inverse * transition)[0])

g_f, mu, s = sp.symbols("g_F mu s", positive=True, real=True)
alpha = g_f**2 / (4 * sp.pi)
m1_squared = g_f**2 * mu**2
m3_squared = 3 * m1_squared
zero_width_amplitude = sp.simplify(
    g_f**2 * (r1 / (s - m1_squared) + r3 / (s - m3_squared))
)
fixed_width_amplitude = sp.simplify(
    g_f**2
    * (
        r1 / (s - (1 - I * alpha) * m1_squared)
        + r3 / (s - (1 - I * alpha) * m3_squared)
    )
)
zero_momentum_exact = sp.simplify(zero_width_amplitude.subs(s, 0))
zero_momentum_fixed_width = sp.simplify(fixed_width_amplitude.subs(s, 0))
high_energy_leading_residue = sp.simplify(r1 + r3)

checks = {
    "wp448_dependency_passed": wp448["passed"],
    "wp449_dependency_passed": wp449["passed"],
    "wp453_dependency_passed": wp453["passed"],
    "triplet_transition_residue_exact": r1 == -sp.Rational(1, 4),
    "quintet_transition_residue_exact": r3 == sp.Rational(1, 4),
    "leading_high_energy_residue_cancels": high_energy_leading_residue == 0,
    "mass_weighted_residues_reproduce_wp453": weighted == -sp.Rational(1, 6)
    and direct == weighted,
    "zero_momentum_propagator_response_exact": zero_momentum_exact
    == sp.Rational(1, 6) / mu**2,
    "constant_width_is_illegal_for_wilson_matching": sp.simplify(
        zero_momentum_fixed_width
        - zero_momentum_exact / (1 - I * alpha)
    )
    == 0
    and sp.im(zero_momentum_fixed_width) != 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP456",
    "domain": "WP447 fixed vacuum and WP453 rotated hostile Yukawa pair.",
    "transition": "Mass-basis generation 1 to 2 Delta-F=2 bilinear.",
    "pole_residues_before_common_current_factor": {
        "triplet": str(r1),
        "quintet": str(r3),
    },
    "unweighted_residue_sum": str(high_energy_leading_residue),
    "inverse_mass_weighted_sum": str(weighted),
    "zero_momentum_propagator_response": str(zero_momentum_exact),
    "fixed_width_zero_momentum_response": str(zero_momentum_fixed_width),
    "contextual_partition": "The two source-derived pole ports resolve opposite transition residues whose leading unresolved sum vanishes but whose mass-weighted low-energy response is nonzero.",
    "classification": "Source-derived complementary probe family; neither selector nor rigidifier.",
    "reference_port_required": False,
    "instrument": "Potential flavor-tagged two-pole collider scan; detector response and reach are not yet supplied.",
    "smallest_exact_falsifier": "Either residue differs from (-1/4,+1/4), or their inverse-mass weighted sum differs from -1/6.",
    "remaining_gate": "Freeze a flavor-tagged detector response, resolution, luminosity, backgrounds, and uncertainties for both pole neighborhoods; keep the fixed-width model out of zero-momentum matching.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp456_pole_resolved_current_complement.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
