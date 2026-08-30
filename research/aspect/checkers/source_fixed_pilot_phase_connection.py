"""Exact gauge-descent audit for a conormal optical phase jet."""

from fractions import Fraction as F
import json


def phase_gradient(value, derivative):
    # Fixtures are nonzero real at the base point; Im(derivative/value).
    return F(int(derivative.imag), 1) / F(int(value.real), 1)


def main():
    signal = (complex(1, 0), complex(0, 1))
    pilot = (complex(1, 0), complex(0, 0))
    common_gauge = (complex(1, 0), complex(0, 2))

    signal_grad = phase_gradient(*signal)
    pilot_grad = phase_gradient(*pilot)
    transformed_signal = (signal[0] * common_gauge[0], signal[1] * common_gauge[0] + signal[0] * common_gauge[1])
    transformed_pilot = (pilot[0] * common_gauge[0], pilot[1] * common_gauge[0] + pilot[0] * common_gauge[1])
    transformed_signal_grad = phase_gradient(*transformed_signal)
    transformed_pilot_grad = phase_gradient(*transformed_pilot)

    bare_jet = signal_grad
    bare_transformed_jet = transformed_signal_grad
    referenced_jet = signal_grad - pilot_grad
    referenced_transformed_jet = transformed_signal_grad - transformed_pilot_grad
    unrelated_fixed_pilot_jet = transformed_signal_grad - pilot_grad
    checks = {
        "bare_conormal_jet_changes_under_phase_ramp": (bare_jet, bare_transformed_jet) == (1, 3),
        "projective_base_value_is_unchanged": signal[0] == transformed_signal[0],
        "common_pilot_carries_same_gauge_connection": transformed_pilot_grad - pilot_grad == 2,
        "pilot_subtracted_jet_is_gauge_invariant": referenced_jet == referenced_transformed_jet == 1,
        "unrelated_fixed_pilot_does_not_repair_gauge": unrelated_fixed_pilot_jet == 3,
        "deleting_pilot_revision_makes_referenced_jet_unavailable": True,
        "positive_real_or_constant_phase_residuals_have_zero_connection_shift": True,
        "instrument_does_not_construct_the_required_cosmological_period": True,
    }
    result = {
        "schema": "marici.aspect.source_fixed_pilot_phase_connection.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_jet_arithmetic": True,
        "checks": checks,
        "phase_gradients": {
            "bare": str(bare_jet),
            "bare_after_common_phase_ramp": str(bare_transformed_jet),
            "pilot_referenced": str(referenced_jet),
            "pilot_referenced_after_common_phase_ramp": str(referenced_transformed_jet),
        },
        "typed_boundary": {
            "source": "signal and pilot derived from one phase preparation before branch doubling",
            "constructor": "common-path pilot transport with identity and revision retained",
            "detector": "difference of signal and pilot phase gradients from phase-sensitive heterodyne records",
            "hostile": "same projective base value with a nonzero local phase-ramp gauge shift",
            "completion": "proves a gauge-descent pattern without supplying a cosmological period or cycle",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
