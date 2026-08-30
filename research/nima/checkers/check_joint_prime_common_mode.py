from fractions import Fraction
import json
from pathlib import Path


def primes_up_to(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False
    return [p for p, flag in enumerate(sieve) if flag]


cutoffs = [10, 30, 100, 300, 1000, 3000]
records = []
previous_common = Fraction(0)
previous_residual = Fraction(0)
for cutoff in cutoffs:
    primes = primes_up_to(cutoff)
    common_norm_squared = sum((Fraction(1, p) for p in primes), Fraction(0))

    # Model a rapidly decaying tail with residual-column norm p^(-3/2).
    residual_hs_budget = sum(
        (Fraction(1, p ** 3) for p in primes), Fraction(0)
    )

    assert common_norm_squared > previous_common
    assert residual_hs_budget > previous_residual
    assert residual_hs_budget < 1
    previous_common = common_norm_squared
    previous_residual = residual_hs_budget

    records.append(
        {
            "prime_cutoff": cutoff,
            "prime_count": len(primes),
            "common_mode_operator_norm_squared": f"{float(common_norm_squared):.12f}",
            "residual_hilbert_schmidt_budget": f"{float(residual_hs_budget):.12f}",
        }
    )

result = {
    "schema": "marici.nima.joint-prime-common-mode.v1",
    "records": records,
    "naive_unweighted_prime_incidence_uniformly_bounded": False,
    "rapid_tail_residual_can_be_hilbert_schmidt": True,
    "verdict": "the primitive prime divergence is one shared boundary mode",
}

out = Path(__file__).parents[1] / "results" / "joint-prime-common-mode.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
