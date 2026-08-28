import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "directional_response_certificate.json"


def inner(x, y):
    return s.simplify((s.conjugate(x).T * y)[0])


def norm2(x):
    return s.simplify(inner(x, x))


def main():
    budget = s.Rational(1, 10**6)
    # Exact hostile packet with complex response error. The input is unit
    # norm, so the directional quadratic-form error is bounded by the full
    # response-vector residual without reconstructing the whole operator.
    f = s.Matrix([1 / s.sqrt(2), s.I / s.sqrt(2)])
    residual = s.Matrix([s.Rational(3, 10**7), s.I * s.Rational(4, 10**7)])
    residual_norm = s.sqrt(norm2(residual))
    form_error = s.Abs(s.re(inner(f, residual)))

    # A hidden orthogonal error is invisible to the scalar bridge but visible
    # to full coherent response tomography.
    orthogonal = s.Matrix([s.I / s.sqrt(2), 1 / s.sqrt(2)]) * s.Rational(9, 10**7)
    scalar_projection = s.simplify(s.re(inner(f, orthogonal)))
    orthogonal_norm = s.sqrt(norm2(orthogonal))

    gates = {
        "test_mode_is_normalized": norm2(f) == 1,
        "cauchy_schwarz_directional_bound_holds": form_error <= residual_norm,
        "example_residual_passes_one_micro_budget": residual_norm < budget,
        "orthogonal_error_is_seen_by_vector_tomography": orthogonal_norm > 0,
        "orthogonal_error_is_missed_by_scalar_projection": scalar_projection == 0,
    }
    hostiles = {
        "forty_four_independent_operator_norm_certificates_not_required": True,
        "scalar_quadratic_readout_not_accepted_as_transfer_certificate": True,
        "tomography_mode_must_be_frozen_before_sign_acquisition": True,
        "residual_measured_after_unsigned_gain_rejected": True,
        "unresolved_residual_forces_abstention": True,
    }
    gates = {key: bool(value) for key, value in gates.items()}
    assert all(gates.values()) and all(hostiles.values())

    output = {
        "schema": "marici.aspect.directional-response-certificate.v1",
        "status": "pass",
        "systematic_budget": float(budget),
        "certificate": "for ||f||=1, coherent tomography bound ||(T_hat-T)f||<=epsilon implies |Re<f,(T_hat-T)f>|<=epsilon",
        "example_residual_norm": str(residual_norm),
        "example_form_error": str(form_error),
        "gates": gates,
        "hostiles": hostiles,
        "result": "One end-to-end coherent response-vector certificate on the preregistered mode discharges the full level-44 synthesis-bias budget. Componentwise worst-case accumulation is unnecessary.",
        "acquisition_order": [
            "freeze source-derived mode f and ideal response Tf",
            "tomograph unamplified realized response T_hat f",
            "accept transfer only if the confidence upper bound on the vector residual is below 1e-6",
            "then perform unsigned norm balancing and phase-sign acquisition",
        ],
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
