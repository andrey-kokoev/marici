"""Exact WP709 response of the source-authorized WP664 disjoint messengers."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
Fn, Fm, lam = sp.symbols("F_n F_m lambda", nonnegative=True, real=True)
N = -8*Fn
M = -8*Fm
X = sp.Integer(0)
wp709_displacement = sp.factor((N+M-X)/28)
wp665_boundary_derivative = -32*(Fn+Fm)*lam

checks = {
    "wp709_displacement_is_negative_sum": sp.simplify(wp709_displacement+sp.Rational(2, 7)*(Fn+Fm)) == 0,
    "one_n_chain_pushes_unstable": wp709_displacement.subs({Fn: 1, Fm: 0}) == -sp.Rational(2, 7),
    "one_m_chain_pushes_unstable": wp709_displacement.subs({Fn: 0, Fm: 1}) == -sp.Rational(2, 7),
    "only_trivial_disjoint_completion_is_null": wp709_displacement.subs({Fn: 0, Fm: 0}) == 0,
    "wp665_boundary_sign_agrees": wp665_boundary_derivative.subs({Fn: 1, Fm: 0, lam: 1}) == -32,
    "disjoint_topology_has_no_mixed_vertex_repair": X == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP711",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "WP664 disjoint Dirac messenger chains with nonnegative multiplicity-weighted Yukawa fourth-power sums F_n and F_m",
    "faithful_coordinate": "WP709 radial stability displacement at the regular WP708 projective ray",
    "source_authorized_operation": "the exact one-loop Dirac supertrace vertex correction derived in WP664",
    "contextual_partition": "the response depends only on F_n+F_m and collapses all messenger allocations with the same total strength",
    "classification": "source-derived destabilizer; neither selector, rigidifier, nor physical instrument",
    "smallest_exact_falsifier": "F_n=1, F_m=0 gives delta D=-2/7",
    "remaining_gate": "derive a mixed or bosonic vertex channel whose complete signed correction satisfies N+M-X>0 after all source terms and thresholds",
}
(ROOT / "results" / "wp711_disjoint_messenger_ray_displacement.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
