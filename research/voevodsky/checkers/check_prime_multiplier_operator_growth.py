from __future__ import annotations

import json
import math


def von_mangoldt(n: int) -> float:
    factors = []
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            factors.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        factors.append(m)
    return math.log(factors[0]) if len(factors) == 1 else 0.0


def main() -> None:
    cutoffs = [10, 30, 100, 300, 1000]
    sums = []
    for N in cutoffs:
        value = sum(von_mangoldt(n) / math.sqrt(n) for n in range(2, N + 1))
        sums.append(value)
    assert all(sums[i + 1] > sums[i] for i in range(len(sums) - 1))

    result = {
        "schema":"marici.voevodsky.prime-multiplier-operator-growth-check.v1",
        "status":"cutoff_operator_norm_divergence_witnessed",
        "cutoffs":cutoffs,
        "minus_W_at_zero":sums,
        "operator_norm_lower_bound":"||M_W_P,N|| >= |W_P,N(0)| = sum_(n<=N) Lambda(n)/sqrt(n)",
        "bounded_operator_limit":False,
        "form_or_distributional_limit_excluded":False,
        "completed_gamma_cancellation_excluded":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
