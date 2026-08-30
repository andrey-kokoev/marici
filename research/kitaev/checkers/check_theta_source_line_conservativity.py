import json
from pathlib import Path
import sympy as sp


def main():
    n = sp.symbols("n", integer=True, positive=True)
    d_n = sp.Rational(1, 1) / n
    p_n = n

    assert sp.simplify(p_n * d_n - 1) == 0
    assert sp.limit(d_n, n, sp.oo) == 0
    assert sp.limit(p_n, n, sp.oo) == sp.oo

    # Each exact finite truncation is invertible, while its smallest singular
    # value is 1/N and the inverse norm is N.
    cutoff = 6
    diagonal = sp.diag(*[sp.Rational(1, k) for k in range(1, cutoff + 1)])
    inverse = diagonal.inv()
    assert diagonal.det() != 0
    assert diagonal * inverse == sp.eye(cutoff)
    assert min(abs(x) for x in diagonal.diagonal()) == sp.Rational(1, cutoff)
    assert max(abs(x) for x in inverse.diagonal()) == cutoff

    # Deliberate hostile comparison: identity detection has a uniform
    # parametrix, unlike the collapsing family.
    identity = sp.eye(cutoff)
    assert min(identity.diagonal()) == 1
    assert max(identity.inv().diagonal()) == 1

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_source_line_conservativity_compiler",
        "finite_cutoff": cutoff,
        "finite_detector_determinant": str(diagonal.det()),
        "finite_detector_invertible": True,
        "smallest_detector_singular_value": str(sp.Rational(1, cutoff)),
        "sharp_parametrix_norm": cutoff,
        "detector_limit_on_normalized_witness": str(sp.limit(d_n, n, sp.oo)),
        "parametrix_norm_limit": "infinity",
        "uniform_graph_estimate_exists": False,
        "metric_ultraproduct_witness": "[e_N] nonzero, [D_N e_N] zero",
        "finite_invertibility_implies_completion_conservativity": False,
        "legitimate_witnesses": [
            "source_derived_uniform_left_inverse",
            "coherent_uniform_contracting_homotopy",
            "uniform_graph_lower_bound",
        ],
        "theta_source_witness": "not_instantiated",
    }
    out = Path(__file__).parents[1] / "results" / "theta-source-line-conservativity.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
