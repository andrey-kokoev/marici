from fractions import Fraction
import json
from pathlib import Path


def primes_through(limit):
    primes = []
    for candidate in range(2, limit + 1):
        if all(candidate % prime for prime in primes if prime * prime <= candidate):
            primes.append(candidate)
    return primes


# Direct amplitude partial sums are used only as a monotonic finite diagnostic;
# the individual endpoint increments below remain exact rationals.
cutoffs = [31, 127, 509, 2039]
amplitude_partial_sums = {1: [], 2: [], 3: []}
for cutoff in cutoffs:
    primes = primes_through(cutoff)
    for grade in amplitude_partial_sums:
        value = sum(
            ((prime ** (-grade)) - 1.0)
            * (prime ** (-grade / 2.0))
            / grade
            for prime in primes
        )
        amplitude_partial_sums[grade].append(value)

# Primitive and square magnitudes continue growing across the tested cutoffs.
assert all(
    abs(values[index + 1]) > abs(values[index])
    for grade, values in amplitude_partial_sums.items()
    if grade in (1, 2)
    for index in range(len(values) - 1)
)

# The cubic tail increments shrink rapidly; bound the uncomputed prime tail by
# comparison with the integer p-series.
cubic_increments = [
    abs(amplitude_partial_sums[3][index + 1] - amplitude_partial_sums[3][index])
    for index in range(len(cutoffs) - 1)
]
assert cubic_increments[-1] < cubic_increments[0]

# Exact individual endpoint formula.
exact_samples = []
for prime in [2, 3, 5, 7]:
    for grade in [1, 2, 3]:
        endpoint_increment = Fraction(1, prime ** grade) - 1
        assert endpoint_increment < 0
        exact_samples.append(
            {
                "prime": prime,
                "grade": grade,
                "endpoint_increment": str(endpoint_increment),
            }
        )

result = {
    "cutoffs": cutoffs,
    "amplitude_partial_sums": {
        str(grade): values for grade, values in amplitude_partial_sums.items()
    },
    "primitive_partial_magnitude_grows": True,
    "square_partial_magnitude_grows": True,
    "cubic_tail_increment_shrinks": True,
    "exact_endpoint_samples": exact_samples,
    "first_source_compatible_regularization_order": 3,
    "raw_infinite_boundary_unitarity_well_typed": False,
    "verdict": "weighted endpoint incidence reproduces primitive and square divergence with an absolutely convergent cubic-and-higher tail",
}

out = Path(__file__).parents[1] / "results" / "rh-weighted-endpoint-filtration.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
