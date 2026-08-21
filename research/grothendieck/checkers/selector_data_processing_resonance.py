from math import gcd


G = tuple(range(6))


def stabilizer(selector):
    return frozenset(k for k in G if all(selector[(g + k) % 6] == selector[g] for g in G))


fine = {g: g for g in G}
parity = {g: fine[g] % 2 for g in G}
constant = {g: 0 for g in G}

K_fine = stabilizer(fine)
K_parity = stabilizer(parity)
K_constant = stabilizer(constant)

assert K_fine < K_parity < K_constant
assert [len(K_fine), len(K_parity), len(K_constant)] == [1, 3, 6]

indices = range(1, 25)
U_fine = list(indices)
U_parity = [n for n in indices if gcd(n, 3) == 1]
U_constant = [n for n in indices if gcd(n, 6) == 1]

assert set(U_constant) < set(U_parity) < set(U_fine)

print({
    "group": "C6",
    "kernel_orders": [1, 3, 6],
    "radical_labels": [1, 3, 6],
    "spectrum_sizes_1_to_24": [len(U_fine), len(U_parity), len(U_constant)],
    "constant_spectrum_1_to_24": U_constant,
    "checks": "pass",
})
