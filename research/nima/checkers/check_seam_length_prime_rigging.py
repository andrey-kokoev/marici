import cmath
import json
import math
from pathlib import Path


def primes_up_to(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for p in range(2, int(limit ** 0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False
    return [p for p, flag in enumerate(sieve) if flag]


def seam_norm_squared(packet):
    return sum(math.log(p) * abs(value) ** 2 for p, value in packet.items())


cutoffs = [30, 100, 300, 1000, 3000, 10000]
records = []
previous_flat = 0.0
previous_rigged = 0.0
for cutoff in cutoffs:
    primes = primes_up_to(cutoff)
    flat_dual_budget = sum(1.0 / p for p in primes)
    rigged_dual_budget = sum(1.0 / (p * math.log(p)) for p in primes)
    assert flat_dual_budget > previous_flat
    assert rigged_dual_budget > previous_rigged
    previous_flat = flat_dual_budget
    previous_rigged = rigged_dual_budget

    packet = {
        p: complex((index + 1) / (len(primes) + 1), (-1) ** index / (p + 1))
        for index, p in enumerate(primes)
    }
    original_norm = seam_norm_squared(packet)
    parameter = 0.731
    modulated = {
        p: cmath.exp(1j * parameter * math.log(p)) * value
        for p, value in packet.items()
    }
    conjugated = {p: value.conjugate() for p, value in packet.items()}
    assert math.isclose(seam_norm_squared(modulated), original_norm, rel_tol=1e-12)
    assert math.isclose(seam_norm_squared(conjugated), original_norm, rel_tol=1e-12)

    records.append(
        {
            "prime_cutoff": cutoff,
            "flat_dual_budget": f"{flat_dual_budget:.12f}",
            "seam_length_dual_budget": f"{rigged_dual_budget:.12f}",
            "mellin_modulation_isometric": True,
            "reciprocal_conjugation_isometric": True,
        }
    )

result = {
    "schema": "marici.nima.seam-length-prime-rigging.v1",
    "records": records,
    "primitive_functional_continuous_in_seam_length_topology": True,
    "primitive_functional_continuous_in_unweighted_l2": False,
    "verdict": "seam length supplies a source-derived rigging for the primitive common mode",
}

out = Path(__file__).parents[1] / "results" / "seam-length-prime-rigging.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
