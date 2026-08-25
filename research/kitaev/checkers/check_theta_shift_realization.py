import json
from pathlib import Path
import sympy as sp


def main():
    t = sp.symbols("t", real=True)
    gaussian = sp.exp(-t**2)

    # Derivatives of a Gaussian are Hermite polynomials times the Gaussian;
    # the first six polynomial factors have strictly increasing degree.
    factors = [sp.expand(sp.diff(gaussian, t, k) / gaussian) for k in range(6)]
    coefficient_matrix = sp.zeros(6, 6)
    for col, poly in enumerate(factors):
        P = sp.Poly(poly, t)
        for (degree,), coefficient in P.terms():
            coefficient_matrix[degree, col] = coefficient
    assert coefficient_matrix.rank() == 6

    # Finite shift: output coordinate 0, then shift the next coordinate into it.
    n = 5
    A = sp.zeros(n, n)
    for i in range(n - 1):
        A[i, i + 1] = 1
    J = sp.Matrix([[1, 0, 0, 0, 0]])
    rows = [J * (A**k) for k in range(n)]
    O_full = sp.Matrix.vstack(*rows)
    O_short = sp.Matrix.vstack(*rows[:3])
    full_gram = O_full.T * O_full
    short_gram = O_short.T * O_short
    assert full_gram == sp.eye(n)
    assert O_short.rank() == 3
    hidden = sp.Matrix([0, 0, 0, 1, 0])
    assert O_short * hidden == sp.zeros(3, 1)

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "source_typed_finite_realization_obstruction_and_shift_replacement",
        "gaussian_derivative_factors": [str(f) for f in factors],
        "derivative_factor_rank_through_order_5": coefficient_matrix.rank(),
        "finite_constant_coefficient_closure": False,
        "discrete_shift_full_horizon_gram": [[int(v) for v in row]
                                             for row in full_gram.tolist()],
        "discrete_shift_short_horizon_rank": O_short.rank(),
        "short_horizon_hidden_state": [int(v) for v in hidden],
        "infinite_horizon_observation": "identity_on_L2",
        "point_evaluation_bounded_on_bare_L2": False,
        "physical_infinite_horizon_authority": "not_established",
    }
    out = Path(__file__).parents[1] / "results" / "theta-shift-realization.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
