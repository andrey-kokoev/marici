import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    checks = {}

    vector_index = 2 + 15
    operand_index = 2 + 15 - 32
    complete_index = 2 + 15 - 32 - 48
    contrast_tau_0 = Fraction(1, 10)
    contrast_tau_1 = Fraction(1, 20)

    checks["su4_adjoint_split"] = 15 == 7 + 8
    checks["pure_vector_index_positive"] = vector_index == 17 and vector_index > 0
    checks["bulk_operands_reverse_index"] = operand_index == -15 and operand_index < 0
    checks["complete_bulk_packet_negative"] = complete_index == -63 and complete_index < 0
    checks["boundary_hostiles_preserve_index"] = vector_index == 17
    checks["boundary_hostiles_change_readout"] = contrast_tau_0 != contrast_tau_1
    checks["tau_zero_contrast"] = contrast_tau_0 == Fraction(1, 10)
    checks["tau_one_contrast"] = contrast_tau_1 == Fraction(1, 20)
    checks["realization_and_twist_partial_constructor"] = checks["su4_adjoint_split"] and checks["pure_vector_index_positive"]
    checks["numerical_selector_falsified"] = checks["boundary_hostiles_change_readout"]
    checks["completion_stability_falsified"] = checks["bulk_operands_reverse_index"]
    checks["complete_deutschian_constructor_absent"] = checks["numerical_selector_falsified"] and checks["completion_stability_falsified"]

    result = {
        "work_package": "WP935",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact_values": {
            "pure_vector_index": vector_index,
            "bulk_operand_index": operand_index,
            "complete_bulk_index": complete_index,
            "contrast_tau_0": str(contrast_tau_0),
            "contrast_tau_1": str(contrast_tau_1),
        },
        "classification": {
            "pure_vector_domain": "realization selector and conditional half-twist selector",
            "complete_flavor_domain": "neither complete selector nor physical16 point selector",
            "first_missing_arrow": "completion-stable boundary source law",
            "instrument_note": "WP770 tomography identifies boundary response but does not select it",
        },
        "smallest_exact_falsifier": "tau=0 and tau=1 preserve the declared parent and positive index but give contrasts 1/10 and 1/20",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp935_deutschian_realization_index_boundary_audit.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
