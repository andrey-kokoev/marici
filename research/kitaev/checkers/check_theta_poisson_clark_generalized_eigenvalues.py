import json
from pathlib import Path
import sympy as sp


def generalized_roots(E, Q):
    lam = sp.symbols("lambda", real=True)
    polynomial = sp.factor((E - lam * Q).det())
    roots = sp.solve(polynomial, lam)
    return polynomial, roots


def main():
    Q = sp.diag(1, 2)
    positive = sp.Matrix([[1, 1], [1, 2]])
    positive_poly, positive_roots = generalized_roots(positive, Q)
    expected = [1 - sp.sqrt(2) / 2, 1 + sp.sqrt(2) / 2]
    assert all(sp.simplify(a - b) == 0 for a, b in zip(positive_roots, expected))

    kernel = sp.diag(0, 2)
    _, kernel_roots = generalized_roots(kernel, Q)
    negative = sp.diag(-1, 2)
    _, negative_roots = generalized_roots(negative, Q)
    assert kernel_roots == [0, 1]
    assert negative_roots == [-1, 1]

    N = sp.symbols("N", positive=True, integer=True)
    scalar_cancel_residual = sp.diag(1, -1)
    assert sp.trace(scalar_cancel_residual) == 0
    assert scalar_cancel_residual != sp.zeros(2)

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "exact_finite_matrix_theorem_and_completion_compiler",
        "positive_fixture": {
            "characteristic_polynomial": str(positive_poly),
            "sharp_interval": [str(v) for v in positive_roots],
        },
        "kernel_fixture_interval": [str(v) for v in kernel_roots],
        "negative_fixture_interval": [str(v) for v in negative_roots],
        "upper_escape": {"c_N": "1", "C_N": "N"},
        "lower_collapse": {"c_N": "1/N", "C_N": "1"},
        "scalar_zero_typed_residual_nonzero": True,
        "theta_E_X": "undefined",
        "theta_R_X": "undefined",
        "theta_generalized_eigenvalue_interval": "undefined",
        "scalar_target": "off_seam_divisor_avoidance_nonvanishing",
    }
    out = Path(__file__).parents[1] / "results" / "theta-poisson-clark-generalized-eigenvalues.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
