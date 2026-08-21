from math import gcd


G = frozenset((a, b) for a in range(2) for b in range(2))
zero = (0, 0)


def add(x, y):
    return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)


K = frozenset((zero, (1, 0)))
L = frozenset((zero, (0, 1)))
meet = K & L
join = frozenset(add(k, ell) for k in K for ell in L)

R_K = 2
R_L = 2
R_meet = 1
R_join = 2

assert meet == frozenset((zero,))
assert join == G
assert R_meet < gcd(R_K, R_L)

indices = range(1, 25)
U_K = {n for n in indices if gcd(n, R_K) == 1}
U_L = {n for n in indices if gcd(n, R_L) == 1}
U_meet = {n for n in indices if gcd(n, R_meet) == 1}
U_join = {n for n in indices if gcd(n, R_join) == 1}

assert U_join == U_K & U_L
assert U_K | U_L < U_meet

print({
    "group": "C2xC2",
    "kernel_orders": [len(K), len(L), len(meet), len(join)],
    "radical_labels": [R_K, R_L, R_meet, R_join],
    "meet_spectrum_size_1_to_24": len(U_meet),
    "input_spectrum_size_1_to_24": len(U_K),
    "checks": "pass",
})
