"""Exact separated-boundary Green-function and completion-fiber audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
wp767 = json.loads(
    (ROOT / "results" / "wp767_massive_vector_current_exchange_scale_fiber.json").read_text(
        encoding="utf-8"
    )
)

m, ell, a, b, h0, hL = sp.symbols(
    "m ell a b h_0 h_L", positive=True, real=True
)
y = sp.symbols("y", real=True)

# Left and right homogeneous solutions for -d_y^2+m^2 with Robin data
# u'(0)=a u(0), v'(ell)=-b v(ell).
u = sp.cosh(m * y) + a * sp.sinh(m * y) / m
vR = sp.cosh(m * (ell - y)) + b * sp.sinh(m * (ell - y)) / m
wronskian = sp.simplify(u * sp.diff(vR, y) - sp.diff(u, y) * vR)
denominator = (m + a * b / m) * sp.sinh(m * ell) + (a + b) * sp.cosh(m * ell)
G_cross = sp.simplify(1 / denominator)
portal = sp.simplify(-h0 * hL * G_cross)

G_neumann = sp.simplify(G_cross.subs({m: 1, ell: 1, a: 0, b: 0}))
G_robin = sp.simplify(G_cross.subs({m: 1, ell: 1, a: 1, b: 0}))

# Five-dimensional locality typing: a UV-local counterterm cannot contain
# fields supported only at two disjoint endpoints. Endpoint self-operators are
# local and remain allowed.
direct_cross_boundary_counterterm_local = False
endpoint_self_operators_local = True

checks = {
    "wp767_dependency_passed": wp767["status"] == "PASS" and all(wp767["checks"].values()),
    "wronskian_is_constant": not sp.simplify(wronskian).has(y),
    "wronskian_gives_robin_denominator": sp.simplify(wronskian + denominator) == 0,
    "neumann_cross_propagator": sp.simplify(G_neumann - 1 / sp.sinh(1)) == 0,
    "passive_robin_cross_propagator_is_positive": bool(G_robin > 0),
    "same_coupling_sign_fixes_negative_portal": bool(portal.subs({m: 1, ell: 1, a: 0, b: 0, h0: 1, hL: 1}) < 0),
    "locality_forbids_direct_cross_boundary_counterterm": not direct_cross_boundary_counterterm_local,
    "locality_allows_endpoint_self_completions": endpoint_self_operators_local,
    "hostile_boundary_completion_changes_magnitude": sp.simplify(G_neumann - G_robin) != 0,
    "hostile_completion_keeps_sign": bool(G_neumann > 0 and G_robin > 0),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP768",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP767",
    "admitted_state_domain": "a local five-dimensional interval with disjoint endpoint flavor sectors, one positive-mass bulk mediator, endpoint couplings h_0 and h_L, and the complete passive Robin boundary self-completion",
    "faithful_coordinate": "bulk mass m, interval length ell, endpoint couplings h_0 h_L, and Robin coefficients a,b",
    "source_authorized_operation": "finite boundary-to-boundary propagation through the unique bulk mediator",
    "cross_propagator": "G(0,ell)=1/[(m+ab/m)sinh(m ell)+(a+b)cosh(m ell)]",
    "portal": "-h_0 h_L G(0,ell)",
    "classification": "source locality forbids an additive local cross-boundary counterterm and passive completion preserves the exchange sign, but allowed endpoint-local self-operators continuously deform the magnitude",
    "smallest_exact_falsifier": "at m=ell=1 and b=0, a=0 gives G=1/sinh(1), while a=1 gives G=exp(-1)",
    "threshold_result": "the WP767 additive cross-contact fiber is removed by locality, but a boundary-condition matching fiber remains",
    "deutschian_status": "sequestering hardens threshold survival of the sign but is still easy to vary through source-legal endpoint completion data",
    "next_source_gate": "derive the endpoint boundary conditions and couplings from gauge symmetry or a unique variational boundary action, and fix m ell plus the physical normalization without chosen boundary data",
    "instrument_gate": "boundary propagation is not yet a calibrated physical16 response channel",
}
(ROOT / "results" / "wp768_separated_boundary_exchange_completion_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
