"""Finite cyclic support-rigidity model for the exact modular theorem."""

import cmath


def dft(vector):
    n = len(vector)
    return [
        sum(
            vector[x] * cmath.exp(-2j * cmath.pi * k * x / n)
            for x in range(n)
        )
        for k in range(n)
    ]


n = 8
h = {0, 2, 4, 6}
annihilator = {0, 4}

constant = [1.0 if x in h else 0.0 for x in range(n)]
constant_hat = dft(constant)
assert all(abs(constant_hat[k]) < 1e-12 for k in range(n) if k not in annihilator)

perturbed = constant[:]
perturbed[2] += 0.25
assert min(perturbed[x] for x in h) > 0
perturbed_hat = dft(perturbed)
leaks = {
    k: perturbed_hat[k]
    for k in range(n)
    if k not in annihilator and abs(perturbed_hat[k]) > 1e-12
}
assert leaks

# Translation invariance on H forces equality of the four supported weights.
translated = [constant[(x - 2) % n] for x in range(n)]
assert translated == constant
translated_perturbed = [perturbed[(x - 2) % n] for x in range(n)]
assert translated_perturbed != perturbed

print("subgroup:", sorted(h))
print("dual annihilator:", sorted(annihilator))
print("constant-weight off-annihilator leakage:", 0)
print("perturbed leakage frequencies:", sorted(leaks))
print("PASS: dual-lattice support rigidly forces translation-constant weights")
