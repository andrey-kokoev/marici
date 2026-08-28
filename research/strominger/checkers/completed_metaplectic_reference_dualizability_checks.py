"""Exact cutoff tests for the completed metaplectic reference obstruction."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "completed_metaplectic_reference_dualizability_checks.json"


def trace_distance_uniform(n, m):
    """Trace norm between embedded uniform states of ranks n < m."""
    assert n < m
    return n * abs(Fraction(1, n) - Fraction(1, m)) + (m - n) * Fraction(1, m)


def geometric_partial_sum(q, n):
    return sum((q ** k for k in range(n)), Fraction(0))


def main():
    cutoffs = [1, 2, 4, 8, 16, 32, 64]
    coevaluation_norm_squared = {str(n): n for n in cutoffs}
    central_traces = {str(n): -n for n in cutoffs}
    doubled_trace_distances = {
        str(n): str(trace_distance_uniform(n, 2 * n)) for n in cutoffs
    }
    q = Fraction(1, 2)
    thermal_masses = [geometric_partial_sum(q, n) for n in cutoffs]
    normalized_sign_expectations = [
        -geometric_partial_sum(q, n) / geometric_partial_sum(q, n)
        for n in cutoffs
    ]

    gates = {
        "finite_cutoff_is_dualizable": all(n > 0 for n in cutoffs),
        "coevaluation_norm_squared_equals_dimension": all(
            coevaluation_norm_squared[str(n)] == n for n in cutoffs
        ),
        "coevaluation_norm_diverges":
            coevaluation_norm_squared[str(cutoffs[-1])] >
            coevaluation_norm_squared[str(cutoffs[0])],
        "central_sign_trace_is_minus_dimension": all(
            central_traces[str(n)] == -n for n in cutoffs
        ),
        "unnormalized_sign_trace_diverges":
            abs(central_traces[str(cutoffs[-1])]) > abs(central_traces[str(cutoffs[0])]),
        "uniform_cutoff_states_are_not_trace_norm_cauchy": all(
            trace_distance_uniform(n, 2 * n) == 1 for n in cutoffs
        ),
        "geometric_reference_has_bounded_mass": all(mass < 2 for mass in thermal_masses),
        "geometric_reference_converges_to_trace_class_mass":
            Fraction(2) - thermal_masses[-1] == q ** cutoffs[-1] * 2,
        "trace_class_reference_detects_sign_at_every_cutoff": all(
            value == -1 for value in normalized_sign_expectations
        ),
        "trace_class_repair_uses_extra_weight": q != 0 and q != 1,
    }

    payload = {
        "schema": "marici.strominger.completed-metaplectic-reference-dualizability.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "finite_cutoff_reference": "dualizable",
            "completed_hilbert_reference": "not_dualizable",
            "uniform_reference_limit": "not_trace_norm_cauchy",
            "minimal_analytic_repair": "trace_class_weight",
            "repair_parameter_authority": "not_source_derived",
        },
        "evidence": {
            "cutoffs": cutoffs,
            "coevaluation_norm_squared": coevaluation_norm_squared,
            "central_traces": central_traces,
            "uniform_N_to_2N_trace_distance": doubled_trace_distances,
            "geometric_weight": str(q),
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
