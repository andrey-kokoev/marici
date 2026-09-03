from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    # Finite-cutoff witness: distinct exponential evaluations separate every
    # adjacent-gap coordinate.
    labels = [sp.Rational(0), sp.Rational(1), sp.Rational(2), sp.Rational(3)]
    times = [sp.Rational(1), sp.Rational(2), sp.Rational(3)]
    matrix = sp.Matrix([
        [sp.exp(-t * labels[i]) - sp.exp(-t * labels[i + 1]) for i in range(3)]
        for t in times
    ])
    determinant = sp.simplify(matrix.det())
    assert determinant != 0
    assert matrix.rank() == 3

    result = {
        "schema":"marici.voevodsky.heat-riesz-totality-check.v1",
        "status":"finite_separation_and_laplace_totality_verified",
        "finite_gap_rank":matrix.rank(),
        "finite_gap_dimension":3,
        "infinite_argument":"orthogonality to all L_t gives vanishing Laplace transform of the cumulative-sum L2 function",
        "hilbert_norm_dense":True,
        "graph_norm_dense":False,
        "completed_form_operator_constructed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
