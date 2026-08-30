"""Exact contextual rank and kernel of the visible Higgs mixing port."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
s, mh2, mx2, kappa = sp.symbols("s mh2 mx2 kappa", real=True)
a, b, phi1, phi2 = sp.symbols("a b phi1 phi2", real=True)

inverse_propagator = sp.Matrix([[s - mh2, -kappa], [-kappa, s - mx2]])
propagator = sp.simplify(inverse_propagator.inv())
visible_higgs = sp.factor(propagator[0, 0])

k1 = a + b * phi1
k2 = a + b * phi2
readout = sp.Matrix([k1**2, k2**2])
jacobian = readout.jacobian([a, b])

checks = {
    "visible_propagator_exact": sp.simplify(visible_higgs - (s - mx2) / ((s - mh2) * (s - mx2) - kappa**2)) == 0,
    "visible_port_is_even_in_mixing": sp.simplify(visible_higgs.subs(kappa, -kappa) - visible_higgs) == 0,
    "two_bin_jacobian_exact": sp.simplify(jacobian.det() - 4 * k1 * k2 * (phi2 - phi1)) == 0,
    "global_sign_pair_is_collapsed": sp.simplify(readout.subs({a: -a, b: -b}) - readout) == sp.zeros(2, 1),
    "coincident_contexts_collapse_rank": sp.simplify(jacobian.det().subs(phi2, phi1)) == 0,
    "zero_response_bin_collapses_local_rank": sp.simplify(jacobian.det().subs(a, -b * phi1)) == 0,
    "generic_rational_witness_has_rank_two": jacobian.det().subs({a: 1, b: 2, phi1: 0, phi2: 3}) == 84,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP692",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "two real radial scalars with nondegenerate inverse propagator away from poles and a momentum-dependent real mixing response kappa_i=a+b Phi_i",
    "detector_projection": "ordinary visible Higgs production and decay couples to the hh propagator entry",
    "contextual_partition": "two distinct bins are locally rank two when both kappa_i are nonzero, but the visible port identifies (a,b) with (-a,-b)",
    "classification": "candidate physical readout and contextual rank repair; neither a numerical selector nor a globally faithful source identifier",
    "smallest_exact_falsifier": "Phi1=Phi2 or either kappa_i=0 makes the two-bin Jacobian singular",
    "reference_gate": "an observable odd in kappa would require an independently sourced exit-odd reference and would define a richer relational experiment",
    "remaining_instrument_gate": "derive the complete momentum-dependent mixing self-energy from the messenger grammar and bind the hh propagator deformation to calibrated visible final-state bins with widths, backgrounds, resolution, and uncertainties",
}
(ROOT / "results" / "wp692_higgs_port_mixing_kernel.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
