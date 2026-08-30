"""Exact WP597 two-doublet selector-versus-stability dichotomy."""

import json
from pathlib import Path

import sympy as sp


x, y, u, v = sp.symbols("x y u v", real=True)
alpha, beta = sp.symbols("alpha beta", real=True)
kappa_phi, kappa_psi, eta = sp.symbols(
    "kappa_phi kappa_psi eta", positive=True, real=True
)

R = sp.Matrix([[0, -1], [1, 0]])
C = sp.diag(1, -1)
phi = sp.Matrix([x, y])
psi = sp.Matrix([u, v])
axis_vacuum = sp.Matrix([1, 0])
diagonal_vacuum = sp.Matrix([1, 1]) / sp.sqrt(2)


def simultaneous_substitution(matrix):
    transformed_phi = matrix * phi
    transformed_psi = matrix * psi
    return {
        x: transformed_phi[0],
        y: transformed_phi[1],
        u: transformed_psi[0],
        v: transformed_psi[1],
    }


cross_quartic = sp.expand((phi.dot(psi)) ** 2)
rotation_difference = sp.expand(
    cross_quartic.subs(simultaneous_substitution(R), simultaneous=True)
    - cross_quartic
)
cp_difference = sp.expand(
    cross_quartic.subs(simultaneous_substitution(C), simultaneous=True)
    - cross_quartic
)

generalized_cps = [R**power * C for power in range(4)]
common_stabilizers = [
    power
    for power, transformation in enumerate(generalized_cps)
    if transformation * axis_vacuum == axis_vacuum
    and transformation * diagonal_vacuum == diagonal_vacuum
]
phi_stabilizers = [
    power
    for power, transformation in enumerate(generalized_cps)
    if transformation * axis_vacuum == axis_vacuum
]
psi_stabilizers = [
    power
    for power, transformation in enumerate(generalized_cps)
    if transformation * diagonal_vacuum == diagonal_vacuum
]

independent_rotation_difference = sp.expand(
    cross_quartic.subs(
        {
            x: (R * phi)[0],
            y: (R * phi)[1],
        },
        simultaneous=True,
    )
    - cross_quartic
)

angular_potential = (
    kappa_phi * sp.sin(2 * alpha) ** 2 / 4
    + kappa_psi * sp.cos(2 * beta) ** 2 / 4
    + eta * sp.cos(alpha - beta) ** 2 / 2
)
candidate = {alpha: 0, beta: sp.pi / 4}
candidate_gradient = sp.simplify(
    sp.Matrix(
        [sp.diff(angular_potential, alpha), sp.diff(angular_potential, beta)]
    ).subs(candidate)
)
uncoupled_gradient = sp.simplify(candidate_gradient.subs(eta, 0))
hostile_gradient = sp.simplify(candidate_gradient.subs(eta, 1))

checks = {
    "axis_and_diagonal_have_no_common_generalized_cp": common_stabilizers == [],
    "axis_has_a_generalized_cp_stabilizer": phi_stabilizers == [0],
    "diagonal_has_a_generalized_cp_stabilizer": psi_stabilizers == [1],
    "independent_doublets_preserve_componentwise_generalized_cp": (
        phi_stabilizers and psi_stabilizers
    ),
    "cross_quartic_is_common_d4_invariant": rotation_difference == 0
    and cp_difference == 0,
    "cross_quartic_is_forbidden_by_independent_rotations": (
        independent_rotation_difference != 0
    ),
    "uncoupled_axis_diagonal_pair_is_stationary": uncoupled_gradient
    == sp.zeros(2, 1),
    "allowed_common_d4_cross_term_moves_candidate": candidate_gradient
    == sp.Matrix([eta / 2, -eta / 2]),
    "deliberate_hostile_eta_one_has_nonzero_gradient": hostile_gradient
    == sp.Matrix([sp.Rational(1, 2), sp.Rational(-1, 2)]),
}

if not all(checks.values()):
    raise SystemExit(f"WP597 check failed: {checks}")

result = {
    "work_package": "WP597",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "domain": "two ordered real D4 doublets at renormalizable degree, with either one common rotation group or independent rotation groups",
    "candidate_vacuum": {
        "phi": "axis angle 0",
        "psi": "diagonal angle pi/4",
    },
    "common_group_result": "the misaligned pair has no common generalized CP R^k*C, but the allowed invariant (phi dot psi)^2 moves the candidate for every nonzero eta",
    "independent_group_result": "the cross-term is forbidden, but independent generalized CP choices k=0 and k=1 stabilize the two components",
    "candidate_gradient_with_cross_term": ["eta/2", "-eta/2"],
    "classification": "minimal two-doublet selector-versus-stability obstruction; not a hard-to-vary physical CP selector",
    "smallest_exact_falsifier": "eta=1 gives angular gradient (1/2,-1/2) at the proposed axis/diagonal vacuum",
    "surviving_architecture_gate": "derive an enlarged source symmetry or representation that forbids every angle-moving cross invariant while allowing only one common generalized-CP family and leaving no stabilizer of the full vacuum",
    "instrument_gate": "derive a portal from the full source representation to a calibrated physical16 CP-odd invariant and an independently executable scalar/threshold readout",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp597_two_doublet_selector_stability_dichotomy.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
