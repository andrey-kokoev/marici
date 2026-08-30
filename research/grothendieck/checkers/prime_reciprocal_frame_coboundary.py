import json
from pathlib import Path

import sympy as sp


theta_p, theta_q, theta_r = sp.symbols("theta_p theta_q theta_r", real=True)
i = sp.I
sigma_1 = sp.Matrix([[0, 1], [1, 0]])


def frame(theta):
    return sp.diag(sp.exp(-i * theta / 2), sp.exp(i * theta / 2))


def exchange(theta):
    return sp.Matrix([[0, sp.exp(-i * theta)], [sp.exp(i * theta), 0]])


R_p, R_q, R_r = map(frame, (theta_p, theta_q, theta_r))
X_p, X_q = map(exchange, (theta_p, theta_q))

checks = {
    "prime_axis_is_conjugate_of_universal_axis": sp.simplify(R_p * sigma_1 * R_p.inv() - X_p) == sp.zeros(2),
    "prime_axis_normalizes_to_universal_axis": sp.simplify(R_p.inv() * X_p * R_p - sigma_1) == sp.zeros(2),
    "transition_cocycle_telescopes": sp.simplify((R_p.inv() * R_q) * (R_q.inv() * R_r) - R_p.inv() * R_r) == sp.zeros(2),
    "cycle_holonomy_is_identity": sp.simplify((R_p.inv() * R_q) * (R_q.inv() * R_r) * (R_r.inv() * R_p) - sp.eye(2)) == sp.zeros(2),
    "common_frame_axes_commute": sp.simplify((R_p.inv() * X_p * R_p) * (R_q.inv() * X_q * R_q) - (R_q.inv() * X_q * R_q) * (R_p.inv() * X_p * R_p)) == sp.zeros(2),
    "raw_commutator_is_preserved": sp.simplify(sp.expand_complex(X_p * X_q - X_q * X_p - 2 * i * sp.sin(theta_q - theta_p) * sp.diag(1, -1))) == sp.zeros(2),
}

result = {
    "schema": "marici.grothendieck.prime-reciprocal-frame-coboundary.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "interpretation": "The raw cross-prime commutator is a frame-mismatch channel. Source-native prime frames normalize every exchange to one universal involution, and their transition cocycle is exact.",
}

out = Path(__file__).parents[1] / "results" / "prime_reciprocal_frame_coboundary.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
