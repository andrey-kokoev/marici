from itertools import permutations
from math import gcd, lcm


S3 = tuple(permutations(range(3)))
e3 = (0, 1, 2)
G = tuple((p, z) for p in S3 for z in range(5))
identity = (e3, 0)


def pmul(a, b):
    return tuple(a[b[i]] for i in range(3))


def pinv(a):
    out = [0] * 3
    for i, value in enumerate(a):
        out[value] = i
    return tuple(out)


def mul(a, b):
    return pmul(a[0], b[0]), (a[1] + b[1]) % 5


def inv(a):
    return pinv(a[0]), (-a[1]) % 5


def conj(g, k):
    return mul(mul(g, k), inv(g))


def order(x):
    y = identity
    for n in range(1, 31):
        y = mul(y, x)
        if y == identity:
            return n
    raise AssertionError("order bound")


def exponent(K):
    value = 1
    for k in K:
        value = lcm(value, order(k))
    return value


def action_exponent(K):
    ordered = tuple(sorted(K))
    index = {k: i for i, k in enumerate(ordered)}
    actions = {tuple(index[conj(g, k)] for k in ordered) for g in G}
    value = 1
    for permutation in actions:
        seen = set()
        action_order = 1
        for i in range(len(permutation)):
            if i in seen:
                continue
            j = i
            cycle = 0
            while j not in seen:
                seen.add(j)
                cycle += 1
                j = permutation[j]
            action_order = lcm(action_order, cycle)
        value = lcm(value, action_order)
    return value


def radical(n):
    out = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            out *= p
            while n % p == 0:
                n //= p
        p += 1
    return out * n


def even(p):
    return sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2 == 0


K = frozenset((p, 0) for p in S3 if even(p))
L = frozenset((e3, z) for z in range(5))
J = frozenset(mul(k, ell) for k in K for ell in L)

labels = [radical(exponent(M) * action_exponent(M)) for M in (K, L, J)]
assert labels == [6, 5, 30]
assert labels[2] == lcm(labels[0], labels[1])

indices = range(1, 61)
spectra = [{n for n in indices if gcd(n, R) == 1} for R in labels]
assert spectra[2] == spectra[0] & spectra[1]

print({
    "group": "S3xC5",
    "kernel_orders": [len(K), len(L), len(J)],
    "radical_labels": labels,
    "spectrum_sizes_1_to_60": [len(U) for U in spectra],
    "checks": "pass",
})
