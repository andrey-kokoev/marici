"""Exact WP448 pole and residue packet for the irreducible triplet vacuum."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp447 = json.loads((root / "results" / "wp447_irreducible_adjoint_triplet.json").read_text(encoding="utf-8"))
I = sp.I
g_f, mu, q2 = sp.symbols("g_F mu q_squared", positive=True, real=True)
lambdas = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2)/sp.sqrt(3),
]
generators = [matrix/2 for matrix in lambdas]
J = [
    sp.Matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])/sp.sqrt(2),
    sp.Matrix([[0, -I, 0], [I, 0, -I], [0, I, 0]])/sp.sqrt(2),
    sp.diag(1, 0, -1),
]

K = sp.Matrix(8, 8, lambda a, b: sp.simplify(sum(
    sp.trace((generators[a]*matrix-matrix*generators[a]).conjugate().T
             *(generators[b]*matrix-matrix*generators[b])) for matrix in J
)))
identity = sp.eye(8)
P_triplet = sp.simplify((3*identity-K)/2)
P_quintet = sp.simplify((K-identity)/2)
propagator = sp.simplify(g_f**2*(q2*identity-g_f**2*mu**2*K).inv())
spectral_form = sp.simplify(
    g_f**2*P_triplet/(q2-g_f**2*mu**2)
    + g_f**2*P_quintet/(q2-3*g_f**2*mu**2)
)

checks = {
    "wp447_dependency_passed": wp447["passed"],
    "mass_shape_has_triplet_and_quintet_spectrum": K.eigenvals() == {sp.Integer(1): 3, sp.Integer(3): 5},
    "triplet_projector_is_idempotent": P_triplet*P_triplet == P_triplet,
    "quintet_projector_is_idempotent": P_quintet*P_quintet == P_quintet,
    "projectors_are_orthogonal": P_triplet*P_quintet == sp.zeros(8),
    "projectors_resolve_identity": P_triplet+P_quintet == identity,
    "projector_ranks_match_multiplets": P_triplet.rank() == 3 and P_quintet.rank() == 5,
    "exact_two_pole_spectral_decomposition": sp.simplify(propagator-spectral_form) == sp.zeros(8),
    "zero_momentum_kernel_cancels_gauge_coupling": sp.simplify((-propagator.subs(q2, 0))-K.inv()/mu**2) == sp.zeros(8),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP448",
    "state_domain": "WP447 irreducible spin-one vacuum with canonical diagonal-SU(3)_F quark currents.",
    "mass_shape": [[str(x) for x in row] for row in K.tolist()],
    "pole_masses_squared": {"triplet": "g_F^2 mu^2", "quintet": "3 g_F^2 mu^2"},
    "multiplicities": {"triplet": 3, "quintet": 5},
    "residue_operators": {"triplet": "g_F^2 P_1", "quintet": "g_F^2 P_3"},
    "triplet_projector": [[str(x) for x in row] for row in P_triplet.tolist()],
    "quintet_projector": [[str(x) for x in row] for row in P_quintet.tolist()],
    "zero_momentum_kernel": [[str(x) for x in row] for row in K.inv().tolist()],
    "widths": None,
    "instrument": None,
    "classification": "Pole locations and labelled current-space residues are independently frozen by source representation theory; widths and detector response are not supplied.",
    "smallest_exact_falsifier": "A third pole, a projector rank other than 3 or 5, or failure of the exact propagator decomposition.",
    "remaining_gate": "Derive total and partial widths from the independently declared particle spectrum and open decay channels, then rotate residues through a viable messenger-to-physical16 map.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp448_triplet_pole_residue_packet.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
