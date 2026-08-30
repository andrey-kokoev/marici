import json
from pathlib import Path
import sympy as sp


def main():
    labels = [sp.Integer(0), sp.Integer(1), sp.Integer(3), sp.Integer(4)]
    vandermonde = sp.Matrix([[q**k for q in labels] for k in range(len(labels))])
    determinant = sp.factor(vandermonde.det())
    assert determinant != 0 and vandermonde.rank() == len(labels)

    repeated = [sp.Integer(0), sp.Integer(1), sp.Integer(1)]
    repeated_matrix = sp.Matrix([[q**k for q in repeated] for k in range(len(repeated))])
    assert repeated_matrix.det() == 0

    delta = sp.symbols("delta", positive=True)
    gaussian_difference = 2 * sp.sqrt(sp.pi / 2) * (1 - sp.exp(-delta**2 / 2))
    collapse_limit = sp.limit(gaussian_difference, delta, 0, dir="+")
    assert collapse_limit == 0

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "finite_packet_theorem_and_raw_coefficient_completion_obstruction",
        "finite_distinct_labels": [str(q) for q in labels],
        "vandermonde_determinant": str(determinant),
        "vandermonde_rank": vandermonde.rank(),
        "finite_full_germ_faithful": True,
        "repeated_label_determinant": str(repeated_matrix.det()),
        "gaussian_adjacent_difference_norm_squared": str(gaussian_difference),
        "adjacent_spacing_zero_limit": str(collapse_limit),
        "raw_l2_uniform_lower_bound": False,
        "constructor_gram_uniform_lower_bound": "not_decided",
        "required_assumptions": ["Phi nonzero", "Phi real analytic and L1",
                                 "labels distinct after source quotient"],
    }
    out = Path(__file__).parents[1] / "results" / "theta-full-seam-germ-faithfulness.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
