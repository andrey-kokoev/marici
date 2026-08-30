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


def stabilizer(selector):
    return frozenset(k for k in G if all(selector[mul(g, k)] == selector[g] for g in G))


def core(S):
    return frozenset(k for k in S if all(mul(mul(g, k), inv(g)) in S for g in G))


def is_subgroup(K):
    return identity in K and all(mul(a, b) in K and inv(a) in K for a in K for b in K)


def is_normal(K):
    return all(mul(mul(g, k), inv(g)) in K for g in G for k in K)


fine = {g: i for i, g in enumerate(G)}
t = (1, 0, 2)
H = frozenset((identity, t))
cosets = []
for g in G:
    C = frozenset(mul(g, h) for h in H)
    if C not in cosets:
        cosets.append(C)
coarse = {g: cosets.index(next(C for C in cosets if g in C)) for g in G}

S_fine = stabilizer(fine)
S_coarse = stabilizer(coarse)
assert len(S_fine) == 1
assert S_coarse == H and len(S_coarse) == 2
assert core(S_fine) == core(S_coarse) == frozenset((identity,))

subgroups = []
for mask in range(1 << len(G)):
    K = frozenset(G[i] for i in range(len(G)) if mask & (1 << i))
    if is_subgroup(K) and is_normal(K):
        subgroups.append(K)

admitted_fine = [K for K in subgroups if K <= S_fine]
admitted_coarse = [K for K in subgroups if K <= S_coarse]
assert admitted_fine == admitted_coarse == [frozenset((identity,))]

print({
    "group": "S3",
    "stabilizer_orders": [len(S_fine), len(S_coarse)],
    "core_orders": [len(core(S_fine)), len(core(S_coarse))],
    "admitted_kernel_orders": [[len(K) for K in admitted_fine], [len(K) for K in admitted_coarse]],
    "checks": "pass",
})
