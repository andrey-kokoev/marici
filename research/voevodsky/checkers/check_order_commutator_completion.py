from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    # Strictly ordered symbolic labels; use rational fixture for exact integration.
    labels = [sp.Rational(0), sp.Rational(2), sp.Rational(5), sp.Rational(9)]
    n = len(labels)
    # Kernel of the order commutator on zero-sum vectors.
    K = sp.Matrix(n, n, lambda i, j: -abs(labels[i] - labels[j]))
    # Adjacent differences d_i=e_i-e_{i+1}.
    D = sp.zeros(n, n - 1)
    for i in range(n - 1):
        D[i, i] = 1
        D[i + 1, i] = -1
    gram = sp.simplify(D.T * K * D)
    expected = sp.diag(*[2 * (labels[i + 1] - labels[i]) for i in range(n - 1)])
    assert gram == expected
    assert all(sum(D[:, i]) == 0 for i in range(n - 1))

    result = {
        "schema":"marici.voevodsky.order-commutator-completion-check.v1",
        "status":"adjacent_interval_diagonalization_verified",
        "gram_diagonal":[int(expected[i, i]) for i in range(n - 1)],
        "completion":"weighted ell2 on adjacent logarithmic gaps",
        "weights":"2*(lambda_(i+1)-lambda_i)",
        "full_L2_interval_claim":False,
        "source_weil_comparison_constructed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
