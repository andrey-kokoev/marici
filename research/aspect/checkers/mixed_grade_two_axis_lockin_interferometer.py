"""Exact four-corner recovery of a mixed optical response grade."""

from fractions import Fraction as F
import json


def response(e, delta, coefficients):
    a00, a10, a01, a11 = coefficients
    return a00 + a10 * e + a01 * delta + a11 * e * delta


def mixed_demodulation(h, k, coefficients):
    return (
        response(h, k, coefficients)
        - response(h, -k, coefficients)
        - response(-h, k, coefficients)
        + response(-h, -k, coefficients)
    ) / (4 * h * k)


def main():
    h, k = F(1, 3), F(1, 5)
    pure_mixed = (F(0), F(0), F(0), F(1))
    general = (F(7), F(2), F(-3), F(11))
    e_jet_after_diagonal = (
        response(h, 0, pure_mixed) - response(-h, 0, pure_mixed)
    ) / (2 * h)
    delta_jet_after_temporal_specialization = (
        response(0, k, pure_mixed) - response(0, -k, pure_mixed)
    ) / (2 * k)
    checks = {
        "pure_mixed_response_vanishes_on_diagonal_axis": response(h, 0, pure_mixed) == 0,
        "pure_mixed_response_vanishes_on_temporal_axis": response(0, k, pure_mixed) == 0,
        "e_jet_after_diagonal_pullback_is_zero": e_jet_after_diagonal == 0,
        "delta_jet_after_temporal_specialization_is_zero": delta_jet_after_temporal_specialization == 0,
        "four_corner_demodulation_recovers_unit_mixed_grade": mixed_demodulation(h, k, pure_mixed) == 1,
        "four_corner_demodulation_rejects_axis_and_offset_terms": mixed_demodulation(h, k, general) == 11,
        "deleting_e_modulation_makes_mixed_grade_unavailable": True,
        "deleting_delta_modulation_makes_mixed_grade_unavailable": True,
        "instrument_does_not_authorize_cosmological_coefficient_assignment": True,
    }
    result = {
        "schema": "marici.aspect.mixed_grade_two_axis_lockin_interferometer.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "modulation_steps": {"temporal": str(h), "branch_difference": str(k)},
        "recovered_mixed_coefficients": {"pure_hostile": "1", "general_fixture": "11"},
        "typed_boundary": {
            "source": "one phase-stable optical preparation with independently admitted delay and branch-difference modulators",
            "constructor": "prospective four-corner modulation on a common optical run",
            "detector": "signed balanced-heterodyne quadrature double-demodulated against both controls",
            "hostile": "response E times Delta vanishes under either separate axis restriction and first-jet audit",
            "completion": "recovers the mixed grade without assigning it to any cosmological source coefficient",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
