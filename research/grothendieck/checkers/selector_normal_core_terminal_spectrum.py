from itertools import permutations


G = tuple(permutations(range(3)))
identity = (0, 1, 2)


def mul(a, b):
    return tuple(a[b[i]] for i in range(3))


def inv(a):
    out = [0] * 3
    for i, value in enumerate(a):
        out[value] = i
    return tuple(out)


t = (1, 0, 2)
H = frozenset((identity, t))
right_cosets = []
for g in G:
    coset = frozenset(mul(g, h) for h in H)
    if coset not in right_cosets:
        right_cosets.append(coset)

selector = {g: right_cosets.index(next(c for c in right_cosets if g in c)) for g in G}
stabilizer = frozenset(k for k in G if all(selector[mul(g, k)] == selector[g] for g in G))
core = frozenset(
    k for k in H if all(mul(mul(g, k), inv(g)) in H for g in G)
)

subgroups = []
for mask in range(1 << len(G)):
    subset = frozenset(G[i] for i in range(len(G)) if mask & (1 << i))
    if identity not in subset:
        continue
    if all(mul(a, b) in subset and inv(a) in subset for a in subset for b in subset):
        subgroups.append(subset)

normal = [K for K in subgroups if all(mul(mul(g, k), inv(g)) in K for g in G for k in K)]
admissible = [K for K in normal if K <= stabilizer]

assert stabilizer == H
assert core == frozenset((identity,))
assert admissible == [core]

print({
    "group_order": len(G),
    "stabilizer_order": len(stabilizer),
    "normal_core_order": len(core),
    "normal_subgroup_orders": sorted(len(K) for K in normal),
    "admissible_kernel_orders": sorted(len(K) for K in admissible),
    "checks": "pass",
})
