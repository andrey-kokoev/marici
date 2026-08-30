from fractions import Fraction
import json
from pathlib import Path


PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def main() -> None:
    harmonic = Fraction(0, 1)
    square_sum = Fraction(0, 1)
    rows = []
    previous_diagonal_operator_norm = None
    previous_residual_hs_square = None

    for prime in PRIMES:
        harmonic += Fraction(1, prime)
        square_sum += Fraction(1, prime * prime)
        diagonal_operator_norm = Fraction(1, 2) / harmonic
        diagonal_hs_square = square_sum / (harmonic * harmonic)
        residual_hs_square = 1 - diagonal_hs_square

        if previous_diagonal_operator_norm is not None:
            assert diagonal_operator_norm < previous_diagonal_operator_norm
        previous_diagonal_operator_norm = diagonal_operator_norm

        if previous_residual_hs_square is not None:
            assert residual_hs_square > previous_residual_hs_square
        previous_residual_hs_square = residual_hs_square

        rows.append(
            {
                "cutoff_prime": prime,
                "seam_operator_norm": "1",
                "seam_trace_norm": "1",
                "diagonal_trace_norm": "1",
                "diagonal_operator_norm": str(diagonal_operator_norm),
                "diagonal_hilbert_schmidt_square": str(diagonal_hs_square),
                "residual_hilbert_schmidt_square": str(residual_hs_square),
            }
        )

    result = {
        "schema": "marici.nima.euler-operator-trace-coronas.v1",
        "cutoffs": rows,
        "operator_corona_retains_seam_class": True,
        "operator_corona_retains_diagonal_class": False,
        "trace_corona_retains_seam_class": True,
        "trace_corona_retains_diagonal_class": True,
        "relationship_residual_persists": True,
        "single_untyped_corona_is_sufficient": False,
    }
    output = Path(__file__).parents[1] / "results" / "euler-operator-trace-coronas.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

