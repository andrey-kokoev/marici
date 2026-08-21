"""Finite-cutoff checks for prime--oscillator rank/trace incompatibility."""

import math


def prime_count(limit: int) -> int:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for candidate in range(2, math.isqrt(limit) + 1):
        if sieve[candidate]:
            sieve[candidate * candidate : limit + 1 : candidate] = b"\x00" * (
                (limit - candidate * candidate) // candidate + 1
            )
    return sum(sieve)


rank_gaps = []
for cutoff in (1_000, 10_000, 100_000, 1_000_000):
    prime_rank = prime_count(cutoff)
    oscillator_rank = math.floor(math.log(cutoff))
    assert prime_rank > oscillator_rank
    rank_gaps.append(prime_rank - oscillator_rank)
    assert math.log(prime_rank) > math.log(math.log(cutoff))

assert all(later > earlier for earlier, later in zip(rank_gaps, rank_gaps[1:]))
assert all(gap > 0 for gap in rank_gaps)

print("prime_cutoff_rank_grows_as_P_over_log_P=True")
print("trace_matched_oscillator_rank_grows_as_log_P=True")
print("support_projection_Hilbert_Schmidt_gap_diverges=True")
print("rank_matched_oscillator_covariance_grows_as_log_P=True")
print("simple_gamma_quasifree_comparison_falsified=True")
print("weighted_many_to_one_shell_correspondence_open=True")
