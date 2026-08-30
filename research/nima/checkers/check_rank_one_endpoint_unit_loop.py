from fractions import Fraction
import json
from pathlib import Path


def main() -> None:
    # Rational normalized vector (3/5, 4/5) supplies an exact rank-one model.
    b = (Fraction(3, 5), Fraction(4, 5))
    norm_square = sum((value * value for value in b), Fraction(0, 1))
    assert norm_square == 1

    carrier = [[left * right for right in b] for left in b]
    reverse_loop = norm_square
    assert reverse_loop == 1

    result = {
        "schema": "marici.nima.rank-one-endpoint-unit-loop.v1",
        "vector": [str(value) for value in b],
        "norm_square": str(norm_square),
        "carrier": [[str(value) for value in row] for row in carrier],
        "synthesis_after_analysis_is_rank_one_carrier": True,
        "analysis_after_synthesis_is_identity": True,
        "unit_return_contains_spectral_information": False,
        "valid_completed_seam_return_map": False,
    }
    output = Path(__file__).parents[1] / "results" / "rank-one-endpoint-unit-loop.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

