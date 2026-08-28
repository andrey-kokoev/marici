import json
from pathlib import Path

import sympy as sp


a, b, lu, lv, kappa, epsilon = sp.symbols(
    "a b lambda_u lambda_v kappa epsilon", positive=True
)

e4 = sp.Matrix([0, 0, 0, 1, 0])
e5 = sp.Matrix([0, 0, 0, 0, 1])
u = a * e5
v = b * e4
Pu = e5 * e5.T
Pv = e4 * e4.T
P3 = sp.eye(5) - Pu - Pv

# The two radial modes and the one physical relative-angle mode. The other
# seven tangent directions are the SO(5)/SO(3) gauge orbit.
physical_hessian = sp.diag(2 * lu * a**2, 2 * lv * b**2, kappa * (a**2 + b**2))
full_hessian = sp.Matrix.vstack(
    sp.Matrix.hstack(2 * lu * u * u.T + kappa * v * v.T, kappa * v * u.T),
    sp.Matrix.hstack(kappa * u * v.T, 2 * lv * v * v.T + kappa * u * u.T),
)
z = sp.symbols("z")
expected_characteristic = sp.expand(
    z**7
    * (z - 2 * lu * a**2)
    * (z - 2 * lv * b**2)
    * (z - kappa * (a**2 + b**2))
)

# A residual singlet rotation is not source-preserving except at discrete
# angles. The pi/2 witness exchanges the projectors.
R = sp.eye(5)
R[3, 3] = 0
R[3, 4] = -1
R[4, 3] = 1
R[4, 4] = 0

m3, mv, mu = sp.symbols("m_3 m_v m_u", real=True)
M2 = m3 * P3 + mv * Pv + mu * Pu
off_diagonal_threshold = epsilon * (u * v.T + v * u.T)

tests = {
    "ordered_vectors_are_orthogonal": (u.dot(v) == 0),
    "three_projectors_resolve_identity": (P3 + Pv + Pu == sp.eye(5)),
    "projectors_are_pairwise_orthogonal": (Pu * Pv == sp.zeros(5) and Pu * P3 == sp.zeros(5) and Pv * P3 == sp.zeros(5)),
    "joint_stabilizer_has_three_dimensional_carrier": (P3.rank() == 3),
    "physical_hessian_has_three_positive_modes": all(value.is_positive for value in physical_hessian.diagonal()),
    "full_hessian_has_seven_gauge_zeros_and_exact_physical_spectrum": sp.expand(full_hessian.charpoly(z).as_expr()) == expected_characteristic,
    "physical_hessian_determinant_is_positive": sp.factor(physical_hessian.det()) == 4 * a**2 * b**2 * kappa * lu * lv * (a**2 + b**2),
    "wp739_pi_over_two_rotation_no_longer_preserves_u_projector": (R * Pu * R.T != Pu),
    "wp739_pi_over_two_rotation_no_longer_preserves_v_projector": (R * Pv * R.T != Pv),
    "source_functional_mass_preserves_both_projectors": (M2 * Pu == Pu * M2 and M2 * Pv == Pv * M2),
    "off_diagonal_threshold_breaks_projector_intertwining": sp.simplify(off_diagonal_threshold * Pu - Pu * off_diagonal_threshold) != sp.zeros(5),
}
tests = {name: bool(value) for name, value in tests.items()}

result = {
    "work_package": "WP877",
    "status": "PASS" if all(tests.values()) else "FAIL",
    "summary": {"passed": sum(tests.values()), "total": len(tests), "all_passed": all(tests.values())},
    "tests": tests,
    "source_domain": "two ordered SO(5) fundamental breaking fields required to realize SO(5)->SO(4)->SO(3), with positive sum-of-squares potential coefficients",
    "faithful_coordinate": "ordered projector packet (P3,Pv,Pu) together with radial scales and source identity",
    "vacuum": {"u": "a e5", "v": "b e4", "stabilizer": "SO(3)"},
    "physical_hessian_eigenvalues": ["2 lambda_u a^2", "2 lambda_v b^2", "kappa(a^2+b^2)"],
    "classification": "source-generated singlet-projector selector and source-functional threshold rigidifier; not a portal-magnitude or RG-basin selector",
    "smallest_exact_falsifier": "kappa=0 restores a flat relative angle; an epsilon(uv^T+vu^T) threshold breaks both projector intertwiners",
    "remaining_source_gate": "derive the complete anomaly-free Spin(5) gauge-Yukawa action and solve its fixed point with both compulsory breaking fundamentals",
    "remaining_instrument_gate": "derive mass-resolved labelled channels and calibrated physical16 detector response in the same ordered source frame",
}

out = Path(__file__).resolve().parents[1] / "results" / "wp877_sequential_so5_two_vector_projector_repair.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
if not all(tests.values()):
    raise SystemExit(1)
