"""Dependency-free finite Dirichlet-basis scout for prime translations."""

import json
import math
from pathlib import Path


def prime_power_terms(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    terms = []
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        power = p
        while power <= limit:
            terms.append((math.log(power), math.log(p) / math.sqrt(power)))
            if power > limit // p:
                break
            power *= p
        if p * p <= limit:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return terms


def one_sided_entry(L, m, n, a):
    if not 0 <= a < 2 * L:
        return 0.0
    alpha, beta = m * math.pi / (2 * L), n * math.pi / (2 * L)
    width = 2 * L - a
    if m == n:
        first = width * math.cos(beta * a)
    else:
        first = (math.sin((alpha - beta) * width - beta * a) + math.sin(beta * a)) / (alpha - beta)
    second = (math.sin((alpha + beta) * width + beta * a) - math.sin(beta * a)) / (alpha + beta)
    return (first - second) / (2 * L)


def matrix(L, size):
    result = [[0.0] * size for _ in range(size)]
    for a, weight in prime_power_terms(int(math.exp(2 * L))):
        one = [[one_sided_entry(L, m + 1, n + 1, a) for n in range(size)] for m in range(size)]
        for m in range(size):
            for n in range(size):
                result[m][n] += weight * (one[m][n] + one[n][m])
    return result


def matvec(A, x):
    return [sum(value * item for value, item in zip(row, x)) for row in A]


def transpose(A):
    return [list(column) for column in zip(*A)]


def spectral_norm(A, iterations=300):
    if not A or not A[0]:
        return 0.0
    AT = transpose(A)
    x = [1 / math.sqrt(len(A[0]))] * len(A[0])
    for _ in range(iterations):
        y = matvec(A, x)
        z = matvec(AT, y)
        norm = math.sqrt(sum(item * item for item in z))
        if norm == 0:
            return 0.0
        x = [item / norm for item in z]
    return math.sqrt(sum(item * item for item in matvec(A, x)))


L, N = 1.0, 5
rows = []
absolute_operator_mass = 2 * sum(weight for _, weight in prime_power_terms(int(math.exp(2 * L))))
for size in (20, 40, 80):
    P = matrix(L, size)
    tail = [row[N:] for row in P[N:]]
    mix = [row[N:] for row in P[:N]]
    d = [math.log1p((mode + 1) * math.pi / (2 * L)) for mode in range(size)]
    weighted_tail = [
        [P[m][n] / math.sqrt(d[m] * d[n]) for n in range(N, size)]
        for m in range(N, size)
    ]
    next_d = math.log1p((size + 1) * math.pi / (2 * L))
    rows.append({
        "matrix_size": size,
        "symmetry_residual_max": max(abs(P[m][n] - P[n][m]) for m in range(size) for n in range(size)),
        "full_spectral_norm": spectral_norm(P),
        "finite_tail_spectral_norm": spectral_norm(tail),
        "finite_low_tail_mix_norm": spectral_norm(mix),
        "weighted_finite_tail_norm": spectral_norm(weighted_tail),
        "absolute_weighted_beyond_cutoff_bound": absolute_operator_mass / next_d,
    })
result = {
    "schema": "marici.grothendieck.dirichlet-prime-translation-matrix-scout.v1",
    "L": L,
    "low_mode_count": N,
    "prime_power_limit": int(math.exp(2 * L)),
    "absolute_operator_mass": absolute_operator_mass,
    "weight_diagonal": "log(1+n*pi/(2L)); no bounded remainder subtracted",
    "rows": rows,
    "claim_boundary": "Double-precision finite sections with power-iteration norms; no beyond-cutoff remainder or explicit-formula prefactor.",
}
output = Path(__file__).parents[1] / "results" / "dirichlet-prime-translation-matrix-scout.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
