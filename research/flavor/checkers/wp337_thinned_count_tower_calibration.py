"""WP337: exact detector-thinning calibration for the exchangeable count tower."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def zeta_matrix(size):
    return sp.Matrix([
        [sp.binomial(k, j) if k >= j else 0 for k in range(size + 1)]
        for j in range(size + 1)
    ])


def main():
    size = 6
    efficiency = sp.symbols("eta", real=True, positive=True)
    zeta = zeta_matrix(size)
    thinning = sp.diag(*[efficiency**order for order in range(size + 1)])
    composite = thinning * zeta
    determinant = sp.factor(composite.det())
    q = sp.Matrix(sp.symbols("q0:7"))
    detected_moments = composite * q
    recovered = sp.simplify(zeta.inv() * thinning.inv() * detected_moments)
    source_probability_a = sp.Rational(1, 2)
    efficiency_a = sp.Rational(1, 2)
    source_probability_b = sp.Rational(1, 4)
    efficiency_b = sp.Integer(1)
    detected_probability_a = source_probability_a * efficiency_a
    detected_probability_b = source_probability_b * efficiency_b
    iid_detected_law_a = [sp.binomial(size, k) * detected_probability_a**k * (1 - detected_probability_a) ** (size - k) for k in range(size + 1)]
    iid_detected_law_b = [sp.binomial(size, k) * detected_probability_b**k * (1 - detected_probability_b) ** (size - k) for k in range(size + 1)]
    checks = {
        "thinning_scales_factorial_order_j_by_eta_j": thinning.diagonal() == sp.Matrix(1, size + 1, [efficiency**j for j in range(size + 1)]),
        "composite_determinant_is_eta_power_21": determinant == efficiency**21,
        "calibrated_nonzero_efficiency_recovers_count_law": recovered == q,
        "hostile_sources_have_different_occupancy_probability": source_probability_a != source_probability_b,
        "hostile_detectors_have_different_efficiency": efficiency_a != efficiency_b,
        "hostile_packets_have_same_detected_probability": detected_probability_a == detected_probability_b,
        "hostile_packets_have_identical_complete_detected_count_law": iid_detected_law_a == iid_detected_law_b,
        "zero_efficiency_collapses_all_positive_orders": thinning.subs(efficiency, 0).rank() == 1,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP337",
        "admitted_state_domain": "exchangeable six-domain count laws observed through independent per-domain detection efficiency eta",
        "faithful_quotient_coordinate": "the source count law q_0 through q_6 conditional on independently calibrated eta>0",
        "candidate_probe_family": "detected factorial-count tower through order six plus an independent efficiency calibration channel",
        "detected_moment_rule": "tilde_m_j=eta^j*m_j",
        "composite_determinant": str(determinant),
        "determinant_exponent": sum(range(size + 1)),
        "hostile_uncalibrated_pair": {
            "packet_a": {"source_bernoulli_probability": str(source_probability_a), "efficiency": str(efficiency_a)},
            "packet_b": {"source_bernoulli_probability": str(source_probability_b), "efficiency": str(efficiency_b)},
            "common_detected_probability": str(detected_probability_a),
            "common_detected_count_law": [str(value) for value in iid_detected_law_a],
        },
        "contextual_partition": "fixed nonzero eta gives singleton source count-law fibers; floating eta groups distinct source laws with detector models that have the same thinned law",
        "classification": "the complete detected tower is faithful only after an independent efficiency-normal channel; raw moments contain deletion sectors and cannot identify the source law alone",
        "smallest_exact_falsifier": "source probability 1/2 at efficiency 1/2 and source probability 1/4 at efficiency 1 produce the identical complete detected count law",
        "remaining_physical_instrument_gate": "derive independent thinning, calibrate eta by a source-traceable normal channel with uncertainty and drift, and test occupancy-dependent or correlated missed detections",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp337_thinned_count_tower_calibration.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
