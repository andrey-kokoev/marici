from math import gcd, lcm


# A4 -> C3 -> 1.
degree_first = 4
resonance_first = 6
degree_second = 3
resonance_second = 3
degree_composite = 12
resonance_composite = 6

assert degree_composite == degree_first * degree_second
assert resonance_composite == lcm(resonance_first, resonance_second)

norm_primes_first = {2}
resonance_primes_first = {2, 3}
assert norm_primes_first < resonance_primes_first

# Direct coefficient pull--push on C3: each target value has four lifts.
f = [2, -1, 5]
pull = [f[h] for h in range(3) for _ in range(degree_first)]
push_pull = [sum(pull[degree_first * h: degree_first * (h + 1)]) for h in range(3)]
assert push_pull == [degree_first * value for value in f]

indices = range(1, 25)
U_first = {n for n in indices if gcd(n, resonance_first) == 1}
U_second = {n for n in indices if gcd(n, resonance_second) == 1}
U_composite = {n for n in indices if gcd(n, resonance_composite) == 1}
assert U_composite == U_first & U_second

print({
    "tower": "A4->C3->1",
    "bidegrees": [[degree_first, resonance_first], [degree_second, resonance_second], [degree_composite, resonance_composite]],
    "first_norm_primes": sorted(norm_primes_first),
    "first_resonance_primes": sorted(resonance_primes_first),
    "pull_push_values": push_pull,
    "checks": "pass",
})
