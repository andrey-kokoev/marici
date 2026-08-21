from math import gcd


G = tuple(range(6))
K2 = frozenset((0, 3))
K3 = frozenset((0, 2, 4))


def coset_selector(K):
    cosets = []
    for g in G:
        coset = frozenset((g + k) % 6 for k in K)
        if coset not in cosets:
            cosets.append(coset)
    return {g: cosets.index(next(C for C in cosets if g in C)) for g in G}


def stabilizer(selector):
    return frozenset(k for k in G if all(selector[(g + k) % 6] == selector[g] for g in G))


c2 = coset_selector(K2)
c3 = coset_selector(K3)
paired = {g: (c2[g], c3[g]) for g in G}

assert stabilizer(c2) == K2
assert stabilizer(c3) == K3
assert stabilizer(paired) == K2 & K3 == frozenset((0,))

indices = range(1, 25)
U2 = [n for n in indices if gcd(n, 2) == 1]
U3 = [n for n in indices if gcd(n, 3) == 1]
U_paired = list(indices)
U_simultaneous = sorted(set(U2) & set(U3))

assert U_simultaneous == [n for n in indices if gcd(n, 6) == 1]
assert set(U_simultaneous) < set(U_paired)

print({
    "group": "C6",
    "kernel_orders": [len(K2), len(K3)],
    "paired_kernel_order": len(K2 & K3),
    "paired_refinement_indices_1_to_24": U_paired,
    "simultaneous_coarse_indices_1_to_24": U_simultaneous,
    "checks": "pass",
})
