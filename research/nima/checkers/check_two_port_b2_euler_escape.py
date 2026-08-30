from fractions import Fraction
import json
from pathlib import Path


PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)


def main() -> None:
    rows = []
    harmonic = Fraction(0, 1)
    previous_max_diagonal = None
    previous_fixed_cross_square = None

    for index, prime in enumerate(PRIMES, start=1):
        harmonic += Fraction(1, prime)
        max_diagonal = Fraction(1, 2) / harmonic
        fixed_cross_square = None
        if index >= 2:
            fixed_cross_square = Fraction(1, 6) / (harmonic * harmonic)
            if previous_fixed_cross_square is not None:
                assert fixed_cross_square < previous_fixed_cross_square
            previous_fixed_cross_square = fixed_cross_square
        if previous_max_diagonal is not None:
            assert max_diagonal < previous_max_diagonal
        previous_max_diagonal = max_diagonal

        normalized_trace = sum(
            (Fraction(1, p) / harmonic for p in PRIMES[:index]),
            Fraction(0, 1),
        )
        assert normalized_trace == 1
        rows.append(
            {
                "cutoff_prime": prime,
                "prime_count": index,
                "harmonic_mass": str(harmonic),
                "normalized_trace": str(normalized_trace),
                "largest_fixed_diagonal": str(max_diagonal),
                "fixed_2_3_cross_coefficient_square": (
                    str(fixed_cross_square)
                    if fixed_cross_square is not None
                    else None
                ),
            }
        )

    result = {
        "schema": "marici.nima.two-port-b2-euler-escape.v1",
        "cutoffs": rows,
        "trace_is_one_at_every_cutoff": True,
        "fixed_diagonal_coordinates_decrease": True,
        "fixed_cross_coordinate_square_decreases": True,
        "euler_vacuum_belongs_to_b2": False,
        "coordinatewise_zero_implies_zero_carrier": False,
        "completion_claim": "requires_corona_port",
    }
    output = Path(__file__).parents[1] / "results" / "two-port-b2-euler-escape.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

