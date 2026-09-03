from __future__ import annotations

import json
from fractions import Fraction

import sympy as sp


def main() -> None:
    ratio = Fraction(1, 1)  # Q/phi(Q)
    rows = []
    for p in sp.primerange(2, 100):
        ratio *= Fraction(p, p - 1)
        # ||M_sqrt(w_Q)|| = sqrt(Q/phi(Q)); A_Q^-1 is the same.
        renormalized_norm_squared = ratio * ratio
        rows.append({
            "p": p,
            "Q_over_phi": f"{ratio.numerator}/{ratio.denominator}",
            "renormalized_norm_squared": (
                f"{renormalized_norm_squared.numerator}/"
                f"{renormalized_norm_squared.denominator}"
            ),
        })

    q_over_phi = [Fraction(row["Q_over_phi"]) for row in rows]
    assert all(q_over_phi[i + 1] > q_over_phi[i] for i in range(len(q_over_phi) - 1))

    # Multiplication operators commute; a multiplication-generated commutator is zero.
    a, b, c, d = sp.symbols("a b c d", real=True)
    density = sp.diag(a, b, c, d)
    local_generator = sp.diag(2, 3, 5, 7)
    assert density * local_generator - local_generator * density == sp.zeros(4)

    result = {
        "schema": "marici.voevodsky.hellinger-renormalized-density-channel-check.v1",
        "status": "scalar_renormalized_density_channel_rejected",
        "density_operator_norm": "sqrt(Q/phi(Q))",
        "inverse_affinity": "sqrt(Q/phi(Q))",
        "renormalized_operator_norm": "Q/phi(Q)",
        "infinite_divergence": "uses divergence of sum_p 1/p",
        "multiplication_commutator": 0,
        "nonlocal_source_channel_excluded": False,
        "rh_implication": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
