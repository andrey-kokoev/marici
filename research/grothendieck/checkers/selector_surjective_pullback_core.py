from math import gcd


G = tuple(range(4))
H = tuple(range(2))


def phi(g):
    return g % 2


delta_H = {h: int(h == 0) for h in H}
pullback = {g: delta_H[phi(g)] for g in G}


def stabilizer(group, selector):
    modulus = len(group)
    return frozenset(k for k in group if all(selector[(g + k) % modulus] == selector[g] for g in group))


S_target = stabilizer(H, delta_H)
S_pullback = stabilizer(G, pullback)
preimage = frozenset(g for g in G if phi(g) in S_target)

assert S_target == frozenset((0,))
assert pullback == {0: 1, 1: 0, 2: 1, 3: 0}
assert S_pullback == preimage == frozenset((0, 2))

indices = range(1, 25)
U_target = list(indices)
U_pullback = [n for n in indices if gcd(n, 2) == 1]
assert set(U_pullback) < set(U_target)

print({
    "surjection": "C4->C2",
    "target_core_order": len(S_target),
    "pullback_core_order": len(S_pullback),
    "target_spectrum_size_1_to_24": len(U_target),
    "pullback_spectrum_size_1_to_24": len(U_pullback),
    "checks": "pass",
})
