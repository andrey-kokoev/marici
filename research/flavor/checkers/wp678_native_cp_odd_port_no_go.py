"""Exact no-go for a native CP-odd port in the unpolarized two-step cascade."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
u, v = sp.symbols("u v", positive=True)
phi = sp.symbols("phi", real=True)
A, C, L, D = sp.symbols("A C L D", positive=True)

# Three final spatial momenta in the parent rest frame obey momentum closure.
nx, ny, nz, qx, qy, qz = sp.symbols("nx ny nz qx qy qz", real=True)
pn = sp.Matrix([nx, ny, nz])
pq = sp.Matrix([qx, qy, qz])
pX = -pn-pq
native_triple = sp.expand(pn.dot(pq.cross(pX)))

W = A*(u+v)+C*sp.sqrt(u*v)*sp.cos(phi)
N = L*(u-v)
S_native = sp.Integer(0)
S_reference = D*sp.sqrt(u*v)*sp.sin(phi)
J_native = sp.Matrix([W, N, S_native]).jacobian([u, v, phi])
J_reference = sp.Matrix([W, N, S_reference]).jacobian([u, v, phi])
det_reference = sp.factor(J_reference.det())

witness = {u: 4, v: 1, phi: sp.pi/3, A: 3, C: 4, L: 1, D: 2}

checks = {
    "three_body_momentum_triple_is_identically_zero": native_triple == 0,
    "native_three_port_rank_is_at_most_two": J_native.rank() == 2,
    "native_record_is_conjugation_even": W.subs(phi, -phi) == W and N.subs(phi, -phi) == N,
    "reference_pseudoscalar_is_conjugation_odd": S_reference.subs(phi, -phi) == -S_reference,
    "reference_port_can_restore_rank_three": J_reference.det().subs(witness) != 0,
    "reference_port_vanishes_without_phase_or_reference_gain": S_reference.subs(phi, 0) == 0 and S_reference.subs(D, 0) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP678",
    "status": "PASS",
    "checks": checks,
    "native_experiment": "unpolarized parent, sequential two-body decay, final momenta p_n,p_q,p_X with p_n+p_q+p_X=0",
    "native_cp_odd_candidate": "p_n dot (p_q cross p_X)=0 identically",
    "native_stabilizer": "complex conjugation phi<->-phi",
    "native_classification": "no source-generated CP-odd third port; the WP677 phase kernel survives",
    "reference_repair": "an added oriented spin or beam vector permits S=D sqrt(uv) sin(phi) and generically restores rank three",
    "reference_jacobian_determinant": str(det_reference),
    "groupoid_change": "the oriented reference defines a new relational experiment over its stabilizer groupoid; it does not reveal an absolute phase of the original cascade",
    "smallest_exact_falsifier": "momentum closure makes the only momentum-only scalar triple product exactly zero",
    "remaining_instrument_gate": "derive a polarized production process and calibrated signed triple-product analysis in the physical pole basis",
}
(ROOT / "results" / "wp678_native_cp_odd_port_no_go.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
