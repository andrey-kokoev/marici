import json
import math


prime_count = 10000
bound = 110000
sieve = bytearray(b"\x01") * bound
sieve[0:2] = b"\x00\x00"
for value in range(2, int(bound**0.5) + 1):
    if sieve[value]:
        start = value * value
        count = ((bound - 1 - start) // value) + 1
        sieve[start::value] = b"\x00" * count

primes = [value for value, is_prime in enumerate(sieve) if is_prime][:prime_count]
assert len(primes) == prime_count

checkpoints = {100, 1000, 5000, 10000}
records = []
partial_sum = 0.0
for index, prime in enumerate(primes, 1):
    partial_sum += 1.0 / prime
    if index in checkpoints:
        ordinary_scale = partial_sum / math.log(index + 1)
        prime_scale = partial_sum / math.log(math.log(prime))
        records.append(
            {
                "prime_count": index,
                "largest_prime": prime,
                "partial_sum": partial_sum,
                "ordinary_log_scale": ordinary_scale,
                "prime_double_log_scale": prime_scale,
            }
        )

ordinary = [record["ordinary_log_scale"] for record in records]
prime_scaled = [record["prime_double_log_scale"] for record in records]

assert all(ordinary[index + 1] < ordinary[index] for index in range(len(ordinary) - 1))
assert ordinary[-1] < 0.30
assert all(1.0 < value < 1.2 for value in prime_scaled)

result = {
    "schema": "marici.nima.primitive-mertens-dixmier-scale.v1",
    "records": records,
    "ordinary_log_normalization_decreases": True,
    "ordinary_dixmier_trace_limit": 0,
    "prime_double_log_scale_remains_nonzero": True,
    "mertens_finite_part_is_standard_dixmier_trace": False,
    "required_functional": "prime_labelled_double_log_finite_part",
}
print(json.dumps(result, indent=2, sort_keys=True))

