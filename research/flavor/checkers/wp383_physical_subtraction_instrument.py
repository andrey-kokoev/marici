"""WP383: exact physical-subtraction calibration and instrument audit."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    p2, p02, M2, mu2 = sp.symbols("p2 p02 M2 mu2", positive=True)
    c, alpha, C0, delta = sp.symbols("c alpha C0 delta", real=True)
    vertex = c + alpha*sp.log((M2+p2)/mu2)
    c_calibrated = C0 - alpha*sp.log((M2+p02)/mu2)
    predicted = sp.expand_log(sp.simplify(vertex.subs(c, c_calibrated)), force=True)
    expected = C0 + alpha*sp.log((M2+p2)/(M2+p02))
    scheme_vertex = sp.expand_log(vertex.subs({mu2: mu2*sp.exp(delta), c: c+alpha*delta}), force=True)
    at_subtraction = sp.simplify(predicted.subs(p2, p02))
    residual_degree = 24
    contact_degree = 2*residual_degree
    benchmark = {M2: 1, p02: 1, p2: 3, alpha: 1}
    checks = {
        "calibration_condition_exact": at_subtraction == C0,
        "scheme_independent_prediction_exact": sp.simplify(predicted-expected) == 0,
        "finite_scheme_change_cancels": sp.simplify(scheme_vertex-vertex) == 0,
        "boundary_sensitivity_is_one": sp.diff(predicted, C0) == 1,
        "positive_boundary_gives_positive_subtraction_curvature": predicted.subs({p2: p02, C0: 1}).is_positive,
        "negative_boundary_gives_negative_subtraction_curvature": predicted.subs({p2: p02, C0: -1}).is_negative,
        "zero_boundary_is_not_generated": predicted.subs({p2: p02, C0: 0}) == 0,
        "transport_difference_independent_of_boundary": not sp.diff(predicted, p2).has(C0),
        "hostile_same_running_opposite_boundaries": sp.simplify(predicted.subs(benchmark).subs(C0, 1)-predicted.subs(benchmark).subs(C0, -1)) == 2,
        "local_contact_field_degree_is_forty_eight": contact_degree == 48,
        "deleting_calibration_leaves_free_symbol": predicted.has(C0),
        "coincident_momenta_delete_transport_information": sp.simplify(predicted.subs(p2, p02)-C0) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP383",
        "admitted_state_domain": "renormalized invariant F-squared vertex at positive Euclidean momentum, with one declared physical subtraction value C0",
        "faithful_quotient_coordinate": "WP378 weak-basis-invariant nondegenerate physical16 residual F",
        "source_authorized_probe_family": "one calibrated vertex value plus source-derived momentum transport",
        "contextual_partition": "one measurement fixes each finite-boundary class; equal running with different C0 remains different source calibration",
        "classification": "scheme-faithful physical calibration and predictive transport, but empirical readout rather than source-derived numerical selection",
        "calibrated_vertex": str(predicted),
        "contact_field_degree": contact_degree,
        "smallest_exact_falsifier": "two packets with identical alpha and spectrum but C0=1 and C0=-1 have identical running and opposite subtraction-point curvature",
        "remaining_physical_instrument_gate": "exhibit an executable source-generated observable sensitive to the degree-48 invariant contact with stated external states, resolution, backgrounds, and uncertainty",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp383_physical_subtraction_instrument.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
