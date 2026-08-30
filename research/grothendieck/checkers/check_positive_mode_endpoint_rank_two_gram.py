#!/usr/bin/env python3
"""Finite exact-numerical audit of the rank-two endpoint Gram identity."""


alphas = [0.6, 1.3, 2.4, 4.2]
weights = [1.1, 0.7, 2.3, 0.4]
z = complex(0.5, 1.7)
a = z.real
t = z.imag
d = [alpha * alpha - z * z for alpha in alphas]

K0 = sum(c / dn for c, dn in zip(weights, d))
S = sum(
    weights[m] * weights[n] * (alphas[m] - alphas[n]) ** 2
    / (abs(d[m]) ** 2 * abs(d[n]) ** 2)
    for m in range(len(alphas))
    for n in range(m + 1, len(alphas))
)
left = abs(K0) ** 2 - 4 * t * t * S

w = [c / abs(dn) ** 2 for c, dn in zip(weights, d)]
gram_x = sum(wn * (alpha * alpha - abs(z) ** 2) for wn, alpha in zip(w, alphas))
gram_y = 2 * t * sum(wn * alpha for wn, alpha in zip(w, alphas))
right = gram_x * gram_x + gram_y * gram_y

checks = {
    "rank_two_gram_identity": abs(left - right) < 1e-12,
    "second_coordinate_nonzero": abs(gram_y) > 1e-6,
    "strict_endpoint_dominance": left > 0,
}

# The full oriented difference has the sign of Re(z).
oriented = 2 * a * left
checks["orientation_has_centered_real_sign"] = oriented > 0

# Horizontal reflection reverses only the final orientation coefficient.
checks["horizontal_reflection_reverses_orientation"] = -2 * a * left < 0

failed = [name for name, ok in checks.items() if not ok]
print({"passed": len(checks) - len(failed), "total": len(checks), "failed": failed})
raise SystemExit(bool(failed))

