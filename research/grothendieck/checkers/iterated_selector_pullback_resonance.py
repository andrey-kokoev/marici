from math import gcd, lcm


G = tuple(range(12))
H = tuple(range(6))
J = tuple(range(2))


def phi(g):
    return g % 6


def psi(h):
    return h % 2


delta_J = {j: int(j == 0) for j in J}
pull_H = {h: delta_J[psi(h)] for h in H}
pull_G_stepwise = {g: pull_H[phi(g)] for g in G}
pull_G_direct = {g: delta_J[psi(phi(g))] for g in G}

assert pull_G_stepwise == pull_G_direct


def stabilizer(modulus, selector):
    return frozenset(k for k in range(modulus) if all(selector[(g + k) % modulus] == selector[g] for g in range(modulus)))


cores = [stabilizer(2, delta_J), stabilizer(6, pull_H), stabilizer(12, pull_G_direct)]
assert [len(K) for K in cores] == [1, 3, 6]

labels = [1, 3, 6]
assert labels[2] == lcm(2, labels[1]) == lcm(2, 3, labels[0])

indices = range(1, 25)
spectra = [{n for n in indices if gcd(n, R) == 1} for R in labels]
assert spectra[2] == {n for n in indices if gcd(n, 2) == 1} & spectra[1]

print({
    "tower": "C12->C6->C2",
    "terminal_kernel_orders": [len(K) for K in cores],
    "radical_labels": labels,
    "spectrum_sizes_1_to_24": [len(U) for U in spectra],
    "stepwise_equals_direct": pull_G_stepwise == pull_G_direct,
    "checks": "pass",
})
