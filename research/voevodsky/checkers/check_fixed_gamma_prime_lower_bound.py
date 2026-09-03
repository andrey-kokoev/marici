from __future__ import annotations

import json
import math


def von_mangoldt(n: int) -> float:
    prime = None
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            if prime is not None:
                return 0.0
            prime = p
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        if prime is not None:
            return 0.0
        prime = m
    return math.log(prime) if prime is not None else 0.0


def main() -> None:
    gamma_at_zero = 10.0  # Any fixed finite value has the same disposition.
    cutoffs = [10, 30, 100, 300, 1000]
    joint_values = []
    for N in cutoffs:
        prime_zero = -sum(von_mangoldt(n) / math.sqrt(n) for n in range(2, N + 1))
        joint_values.append(gamma_at_zero + prime_zero)
    assert all(joint_values[i + 1] < joint_values[i] for i in range(len(joint_values) - 1))
    assert joint_values[-1] < 0

    result = {
        "schema":"marici.voevodsky.fixed-gamma-prime-lower-bound-check.v1",
        "status":"fixed_local_gamma_cannot_uniformly_semibound_prime_cutoffs",
        "illustrative_fixed_gamma_value":gamma_at_zero,
        "cutoffs":cutoffs,
        "joint_values_at_zero":joint_values,
        "uniform_full_L2_lower_bound":False,
        "analytic_probe_core_lower_bound_excluded":False,
        "source_regularized_joint_limit_excluded":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
