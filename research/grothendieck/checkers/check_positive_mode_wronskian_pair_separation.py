#!/usr/bin/env python3
"""Checks the exact pair-separation formula on finite positive mode packets."""


alphas = [0.7, 1.4, 2.8, 4.5]
weights = [1.2, 0.8, 2.0, 0.5]
z = complex(0.4, 1.3)

b = [c / (alpha * alpha - z * z) for alpha, c in zip(alphas, weights)]

direct = 0j
for m, alpha_m in enumerate(alphas):
    for n, alpha_n in enumerate(alphas):
        direct += alpha_m * b[m] * b[n].conjugate() / (alpha_m + alpha_n)
J_direct = direct.imag

pair_sum = 0.0
pair_contributions = []
for m in range(len(alphas)):
    for n in range(m + 1, len(alphas)):
        numerator = weights[m] * weights[n] * (alphas[m] - alphas[n]) ** 2
        denominator = abs(alphas[m] ** 2 - z * z) ** 2 * abs(alphas[n] ** 2 - z * z) ** 2
        term = numerator / denominator
        pair_sum += term
        pair_contributions.append(-((z * z).imag) * term)

J_pair = -((z * z).imag) * pair_sum

checks = {
    "pair_formula_matches_direct": abs(J_direct - J_pair) < 1e-12,
    "all_pairs_same_orientation": all(x < 0 for x in pair_contributions),
    "pair_current_nonzero": abs(J_pair) > 1e-6,
}

# One mode has no pair current.
single_b = weights[0] / (alphas[0] ** 2 - z * z)
single_J = (alphas[0] * single_b * single_b.conjugate() / (2 * alphas[0])).imag
checks["single_mode_is_neutral"] = abs(single_J) < 1e-12

# Reversing either spectral coordinate reverses the orientation.
z_reversed = complex(-z.real, z.imag)
J_reversed = -((z_reversed * z_reversed).imag) * pair_sum
checks["horizontal_reflection_reverses_current"] = abs(J_reversed + J_pair) < 1e-12

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))

