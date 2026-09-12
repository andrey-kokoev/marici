#!/usr/bin/env python3
"""Check mixed half-line shift/contraction residuals on four prime axes."""

import json
import math
from pathlib import Path

PRIMES = (2, 3, 5, 7)


def f(x):
    return math.exp(-x)


def R(b, g, x):
    return g(x + b)


def S(a, g, x):
    return 0.0 if x < a else g(x - a)


def mixed(a, b, x):
    """(R_b S_a-S_a R_b)f at x."""
    return R(b, lambda y: S(a, f, y), x) - S(a, lambda y: R(b, f, y), x)


def predicted(a, b, x):
    if b > a:  # P_a R_(b-a)
        return f(x + b - a) if 0 <= x < a else 0.0
    if a > b:  # 1_[a-b,a) S_(a-b)
        return f(x - (a - b)) if a - b <= x < a else 0.0
    return f(x) if 0 <= x < a else 0.0


def witness(a, b):
    if b >= a:
        return a / 2
    return a - b / 2


def main():
    pairs = []
    for p in PRIMES:
        for q in PRIMES:
            if p == q:
                continue
            a, b = math.log(p), math.log(q)
            x = witness(a, b)
            actual = mixed(a, b, x)
            expected = predicted(a, b, x)
            assert abs(actual - expected) < 1e-12, (p, q, actual, expected)
            assert abs(actual) > 1e-12, (p, q, x)
            support = (
                f"[0,log({p}))" if q > p
                else f"[log({p}/{q}),log({p}))"
            )
            pairs.append({
                "contraction_axis_p": p,
                "creation_axis_q": q,
                "operator": f"K_{{{q},{p}}}=R_{q} S_{p}-S_{p} R_{q}",
                "support": support,
                "witness_x": x,
                "witness_value": actual,
                "nonzero": True,
            })

    result = {
        "schema": "marici.coherence.four-prime-halfline-window-residual.v1",
        "primes": PRIMES,
        "ordered_mixed_pairs": len(pairs),
        "all_mixed_residuals_nonzero": all(row["nonzero"] for row in pairs),
        "identity": "d_q h_p+h_p d_q=c_q i_p tensor (R_q S_p-S_p R_q), p != q",
        "consequence": "single-axis contraction defects do not assemble into an uncorrected contraction of the total differential",
        "pairs": pairs,
    }
    target = Path(__file__).with_name("four-prime-halfline-window-residual.v1.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("primes", "ordered_mixed_pairs", "all_mixed_residuals_nonzero", "consequence")}, indent=2))


if __name__ == "__main__":
    main()
