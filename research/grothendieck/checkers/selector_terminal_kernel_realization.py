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


def is_subgroup(K):
    return identity in K and all(mul(a, b) in K and inv(a) in K for a in K for b in K)


def is_normal(K):
    return all(mul(mul(g, k), inv(g)) in K for g in G for k in K)


def quotient_selector(K):
    cosets = []
    for g in G:
        coset = frozenset(mul(g, k) for k in K)
        if coset not in cosets:
            cosets.append(coset)
    return {g: cosets.index(next(C for C in cosets if g in C)) for g in G}


def stabilizer(selector):
    return frozenset(k for k in G if all(selector[mul(g, k)] == selector[g] for g in G))


subgroups = []
for mask in range(1 << len(G)):
    K = frozenset(G[i] for i in range(len(G)) if mask & (1 << i))
    if is_subgroup(K):
        subgroups.append(K)

normal = [K for K in subgroups if is_normal(K)]
realized = []
for K in normal:
    c_K = quotient_selector(K)
    assert stabilizer(c_K) == K
    realized.append(len(K))

assert sorted(realized) == [1, 3, 6]

print({
    "group": "S3",
    "subgroup_count": len(subgroups),
    "normal_kernel_orders": sorted(len(K) for K in normal),
    "realized_terminal_kernel_orders": sorted(realized),
    "checks": "pass",
})
