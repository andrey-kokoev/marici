import json
from pathlib import Path

import sympy as sp


theta, theta_dot, g, g_dot = sp.symbols("theta theta_dot g g_dot", real=True)
J = sp.Matrix([[0, -1], [1, 0]])
H0 = sp.diag(-1, 1)
R = sp.Matrix([[sp.cos(theta), -sp.sin(theta)], [sp.sin(theta), sp.cos(theta)]])
H = sp.simplify(R * H0 * R.T)
dH = sp.simplify(H.diff(theta) * theta_dot)
Omega = theta_dot * J
comm = sp.simplify(Omega * H - H * Omega)
reconstructed = sp.simplify(sp.trace(J * H * dH) / 4)

K = sp.Matrix([[0, 1], [1, 0]])
alpha = sp.symbols("alpha", real=True)
moving_U = sp.Matrix([[sp.cos(alpha), -sp.sin(alpha)], [sp.sin(alpha), sp.cos(alpha)]])
Hprime = sp.simplify(moving_U * H0 * moving_U.T)
dHprime = sp.simplify(Hprime.diff(alpha))
Omega_prime = J

tests = {
    "J_squared_is_minus_identity": J * J == -sp.eye(2),
    "H_squared_is_identity": sp.simplify(H * H) == sp.eye(2),
    "J_anticommutes_with_H": sp.simplify(J * H + H * J) == sp.zeros(2),
    "moving_projector_derivative_is_commutator": sp.simplify(dH - comm) == sp.zeros(2),
    "covariant_derivative_vanishes": sp.simplify(dH - comm) == sp.zeros(2),
    "angular_velocity_reconstructs_from_germ": sp.simplify(reconstructed - theta_dot) == 0,
    "frozen_connection_fails_in_moving_basis": dHprime != sp.zeros(2),
    "inhomogeneous_connection_repairs_moving_basis": sp.simplify(dHprime - (Omega_prime * Hprime - Hprime * Omega_prime)) == sp.zeros(2),
    "portal_covariant_derivative_retains_only_gain_flow": sp.simplify((g_dot * H + g * dH) - g * comm - g_dot * H) == sp.zeros(2),
    "scalar_spectrum_forgets_frame_angle": H.eigenvals() == {-1: 1, 1: 1},
    "constant_and_rotating_histories_share_spectrum": Hprime.eigenvals() == H0.eigenvals(),
}

passed = sum(bool(v) for v in tests.values())
result = {
    "work_package": "WP882",
    "status": "PASS" if passed == len(tests) else "FAIL",
    "summary": {"passed": passed, "total": len(tests), "all_passed": passed == len(tests)},
    "classification": "rigidifier_only: source-projector germ supplies covariant frame transport but no scalar RG selector",
    "connection": "Omega=dot(R) R^T=dot(theta) J",
    "reconstruction": "dot(theta)=tr(J H dot(H))/4",
    "descent_rule": "Omega'=U Omega U^-1+dot(U) U^-1",
    "remaining_kernel": "dot(g)=beta_g and threshold matching are not selected",
    "smallest_falsifier": "a nontrivial moving basis makes dot(H') nonzero when Omega is incorrectly frozen to zero",
    "tests": tests,
}

output = Path(__file__).parents[1] / "results" / "wp882_ordered_hodge_comoving_connection.json"
output.write_text(json.dumps(result, indent=2, default=bool) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
