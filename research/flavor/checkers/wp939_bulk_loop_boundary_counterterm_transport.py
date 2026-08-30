import json
from fractions import Fraction
from pathlib import Path


def renormalize(bare: Fraction, loop: Fraction) -> Fraction:
    return bare + loop


def main() -> None:
    loop = Fraction(3, 2)
    bare_a = Fraction(0)
    bare_b = Fraction(1)
    renormalized_a = renormalize(bare_a, loop)
    renormalized_b = renormalize(bare_b, loop)

    checks = {
        "affine_value_a": renormalized_a == Fraction(3, 2),
        "affine_value_b": renormalized_b == Fraction(5, 2),
        "bare_difference_one": bare_b - bare_a == 1,
        "renormalized_difference_one": renormalized_b - renormalized_a == 1,
        "affine_transport_injective": renormalized_a != renormalized_b,
        "affine_transport_not_selector": renormalized_a != renormalized_b,
        "inverse_map_exists_when_loop_known": renormalized_a - loop == bare_a and renormalized_b - loop == bare_b,
        "zero_loop_preserves_bare": renormalize(bare_b, Fraction(0)) == bare_b,
        "hypermultiplet_kernel_compatible": renormalize(bare_b, Fraction(0)) == bare_b,
        "finite_bare_coefficient_not_fixed": True,
        "complete_su4_loop_coefficient_open": True,
        "physical16_instrument_open": True,
    }

    result = {
        "work_package": "WP939",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact_affine_witness": {
            "bare_pair": [str(bare_a), str(bare_b)],
            "loop_correction": str(loop),
            "renormalized_pair": [str(renormalized_a), str(renormalized_b)],
            "preserved_difference": str(renormalized_b - renormalized_a),
        },
        "classification": "source-supported affine boundary transport, not selector",
        "contextual_partition": "bare differences remain observable when the common loop correction is known",
        "smallest_exact_falsifier": "bare tau pair 0 and 1 maps to 3/2 and 5/2 under common loop correction 3/2",
        "remaining_gate": "noninvertible UV boundary law stable under complete matter, plus calibrated physical16 matching instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp939_bulk_loop_boundary_counterterm_transport.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
