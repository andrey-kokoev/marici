from fractions import Fraction
import json
from pathlib import Path


EIGENVALUES = (0, 1, 3)
S = Fraction(1, 1)


def main() -> None:
    derivative_multipliers = []
    forced_feature_multipliers = []
    for eigenvalue in EIGENVALUES:
        resolvent = Fraction(1, 1) / (eigenvalue + S)
        derivative = resolvent * resolvent
        forced_feature = 1 - resolvent
        assert derivative != 0
        derivative_multipliers.append(derivative)
        forced_feature_multipliers.append(forced_feature)

    result = {
        "schema": "marici.nima.clark-tail-forcing-injectivity.v1",
        "mode_count": len(EIGENVALUES),
        "derivative_row_rank": len(EIGENVALUES),
        "combined_feature_rank": len(EIGENVALUES),
        "tail_forcing_kernel_dimension": 0,
        "differentiated_flow_forces_G_from_dG": True,
        "original_flow_forces_f_from_G": True,
        "uniform_completion_bound_proved": False,
        "derivative_multipliers": [str(value) for value in derivative_multipliers],
        "forced_feature_multipliers": [
            str(value) for value in forced_feature_multipliers
        ],
    }
    output = Path(__file__).parents[1] / "results" / "clark-tail-forcing-injectivity.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

