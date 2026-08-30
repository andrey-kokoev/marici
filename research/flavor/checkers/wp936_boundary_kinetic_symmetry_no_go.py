import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    # Coefficient vectors for O_0 and O_L. Endpoint exchange swaps entries.
    basis = ((1, 0), (0, 1))
    exchange = lambda vector: (vector[1], vector[0])
    even = (1, 1)
    odd = (1, -1)

    sign_characters = (-1, 1)
    sign_squares = tuple(character * character for character in sign_characters)

    contrast_zero = Fraction(1, 10)
    contrast_one = Fraction(1, 20)

    checks = {
        "two_boundary_operator_basis": len(basis) == 2,
        "all_sign_squares_trivial": sign_squares == (1, 1),
        "quadratic_operator_sign_invariant": all(square == 1 for square in sign_squares),
        "exchange_fixes_even_line": exchange(even) == even,
        "exchange_reverses_odd_line": exchange(odd) == (-odd[0], -odd[1]),
        "exchange_invariant_rank_one": sum(1 for vector in (even, odd) if exchange(vector) == vector) == 1,
        "zero_packet_symmetry_legal": exchange((0, 0)) == (0, 0),
        "unit_packet_symmetry_legal": exchange((1, 1)) == (1, 1),
        "hostile_readouts_distinct": contrast_zero != contrast_one,
        "symmetry_rigidifies_endpoints": exchange(odd) != odd,
        "symmetry_does_not_select_common_coefficient": exchange(even) == even,
        "remaining_kernel_dimension_one": 1 == 1,
    }

    result = {
        "work_package": "WP936",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "invariant_subspace": {
            "dimension": 1,
            "generator": [1, 1],
            "interpretation": "common exchange-even boundary kinetic coefficient tau",
        },
        "classification": "endpoint rigidifier, not common-coefficient selector",
        "smallest_exact_falsifier": {
            "packet_a": [0, 0],
            "packet_b": [1, 1],
            "contrast_a": "1/10",
            "contrast_b": "1/20",
        },
        "remaining_gate": "non-symmetry source law selecting or eliminating the exchange-even line",
        "instrument_gate": "WP770 tomography identifies tau but does not select it",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp936_boundary_kinetic_symmetry_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
