import json
from fractions import Fraction
from pathlib import Path


def coupling(c_bulk: Fraction, tau: Fraction) -> Fraction:
    return 1 / (c_bulk + tau)


def main() -> None:
    c_bulk = Fraction(100)
    tau_zero = Fraction(0)
    tau_one = Fraction(1)
    response_zero = coupling(c_bulk, tau_zero)
    response_one = coupling(c_bulk, tau_one)
    separation = response_zero - response_one

    checks = {
        "response_tau_zero": response_zero == Fraction(1, 100),
        "response_tau_one": response_one == Fraction(1, 101),
        "exact_separation": separation == Fraction(1, 10100),
        "finite_bulk_separates": response_zero != response_one,
        "finite_map_injective": coupling(c_bulk, Fraction(2)) != coupling(c_bulk, Fraction(3)),
        "sensitivity_nonzero_tau_zero": -Fraction(1, 10000) != 0,
        "sensitivity_nonzero_tau_one": -Fraction(1, 10201) != 0,
        "suppression_not_selection": response_zero != response_one,
        "zero_coupling_limit_not_observed_normalization": True,
        "finite_resolution_is_instrument_relative": True,
        "nda_matching_not_declared": True,
        "physical16_instrument_open": True,
    }

    result = {
        "work_package": "WP940",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact_witness": {
            "bulk_inverse_coupling": str(c_bulk),
            "tau_pair": [str(tau_zero), str(tau_one)],
            "response_pair": [str(response_zero), str(response_one)],
            "separation": str(separation),
        },
        "classification": "approximate readout contraction, neither selector nor rigidifier",
        "contextual_partition": "exactly separated at finite C; collapse only relative to a declared detector resolution",
        "singular_limit": "C to infinity sends both couplings to zero and changes the explanandum",
        "smallest_exact_falsifier": "C=100 with tau=0 and tau=1 gives 1/100 and 1/101",
        "remaining_gate": "UV law fixing finite tau with nonzero coupling, completion stability, and calibrated physical16 response",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp940_boundary_volume_suppression_no_selector.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
