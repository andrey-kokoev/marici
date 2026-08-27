"""Exact two-momentum tomography of the WP769 boundary response."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
wp769 = json.loads(
    (ROOT / "results" / "wp769_static_gauge_matching_finite_readout_fiber.json").read_text(
        encoding="utf-8"
    )
)

s, t = sp.symbols("s t", nonnegative=True, real=True)

def row(p):
    mu = sp.sqrt(1 + p**2)
    return sp.Matrix([[p**2 * sp.cosh(mu), p**4 * sp.sinh(mu) / mu]])

A1, B1 = list(row(sp.Integer(1)))
A2, B2 = list(row(sp.Integer(2)))
response = sp.Matrix([[A1, B1], [A2, B2]])
det_response = sp.simplify(response.det())

# One-port hostile pair. Packet A has (s,t)=(2,1), corresponding to r0=rL=1.
# Packet B has t'=0 and s'=2+B1/A1. Both give the same first residual.
s_a, t_a = sp.Integer(2), sp.Integer(1)
s_b, t_b = sp.simplify(2 + B1 / A1), sp.Integer(0)
y1_a = sp.simplify(A1 * s_a + B1 * t_a)
y1_b = sp.simplify(A1 * s_b + B1 * t_b)
y2_a = sp.simplify(A2 * s_a + B2 * t_a)
y2_b = sp.simplify(A2 * s_b + B2 * t_b)

y1, y2 = sp.symbols("Y_1 Y_2", real=True)
reconstructed = sp.simplify(response.inv() * sp.Matrix([y1, y2]))
round_trip = sp.simplify(response.inv() * response * sp.Matrix([s, t]))

checks = {
    "wp769_dependency_passed": wp769["status"] == "PASS" and all(wp769["checks"].values()),
    "response_is_two_by_two": response.shape == (2, 2),
    "two_momentum_response_has_positive_determinant": det_response.is_positive,
    "two_momentum_response_has_rank_two": response.rank() == 2,
    "one_port_hostile_pair_is_admissible": bool(s_b > 0 and t_b == 0),
    "one_port_hostile_pair_collapses": sp.simplify(y1_a - y1_b) == 0,
    "second_port_separates_hostile_pair": sp.simplify(y2_a - y2_b) != 0,
    "two_ports_reconstruct_sum": sp.simplify(round_trip[0] - s) == 0,
    "two_ports_reconstruct_product": sp.simplify(round_trip[1] - t) == 0,
    "unordered_endpoint_pair_is_roots_of_quadratic": sp.expand((sp.Symbol("z") - sp.Symbol("r_0")) * (sp.Symbol("z") - sp.Symbol("r_L"))).coeff(sp.Symbol("z"), 1) == -sp.Symbol("r_0") - sp.Symbol("r_L"),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP770",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP769",
    "admitted_state_domain": "the quadratic gauge-invariant boundary completion of WP769 at fixed calibrated m=ell=1, probed at two declared spacelike momentum magnitudes p=1 and p=2",
    "faithful_coordinate": "the response-relevant symmetric boundary invariants s=r_0+r_L and t=r_0 r_L",
    "source_authorized_probe_family": "boundary-to-boundary current transfer with independently calibrated injected momentum and amplitude at p=1 and p=2",
    "response_linearization": "Y(p)=G(p)^(-1)-mu sinh(mu)=p^2 cosh(mu) s + p^4 sinh(mu)/mu t, mu=sqrt(1+p^2)",
    "contextual_partition": "one momentum leaves affine one-dimensional fibers in (s,t); the two declared momenta give singleton fibers in (s,t), equivalently unordered endpoint pairs",
    "classification": "a two-momentum transfer instrument is jointly faithful on the complete quadratic boundary-response packet and calibrates the finite readout, but it does not identify labelled endpoint ontology or select the portal magnitude",
    "smallest_exact_falsifier": "(s,t)=(2,1) and (2+B_1/A_1,0) have identical p=1 response and distinct p=2 response",
    "reference_port_statement": "declaring momentum and transfer-amplitude standards creates a calibrated relational experiment; it does not reveal an absolute boundary coefficient outside that experiment",
    "physical_instrument_gate": "the transfer protocol is experimentally typed, but its realization and uncertainty matrix in the actual flavor production and decay channels remain to be supplied",
    "remaining_source_gate": "fix m ell and gauge normalization on an isolated RG trajectory, then map the calibrated response to physical16 observables",
}
(ROOT / "results" / "wp770_two_momentum_boundary_response_tomography.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
