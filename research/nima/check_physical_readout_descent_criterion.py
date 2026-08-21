"""Exhaustive finite-field audit of the physical readout descent criterion."""

from itertools import product
import json
from pathlib import Path


def rank(rows, p):
    a = [list(r) for r in rows]
    m, n, out, col = len(a), (len(a[0]) if a else 0), 0, 0
    while out < m and col < n:
        pivot = next((i for i in range(out, m) if a[i][col] % p), None)
        if pivot is None:
            col += 1
            continue
        a[out], a[pivot] = a[pivot], a[out]
        inv = pow(a[out][col] % p, -1, p)
        a[out] = [(x * inv) % p for x in a[out]]
        for i in range(m):
            if i != out and a[i][col] % p:
                c = a[i][col] % p
                a[i] = [(a[i][j] - c * a[out][j]) % p for j in range(n)]
        out += 1
        col += 1
    return out


def dot(a, b, p):
    return sum(x * y for x, y in zip(a, b)) % p


def mv(q, v, p):
    return tuple(dot(row, v, p) for row in q)


matrix_checks = functional_checks = 0
for p, max_dim in ((2, 3), (3, 2)):
    for n in range(1, max_dim + 1):
        vectors = list(product(range(p), repeat=n))
        for m in range(1, n + 1):
            targets = list(product(range(p), repeat=m))
            for flat in product(range(p), repeat=m * n):
                q = [flat[i * n:(i + 1) * n] for i in range(m)]
                if rank(q, p) != m:
                    continue
                matrix_checks += 1
                kernel = [v for v in vectors if mv(q, v, p) == (0,) * m]
                pullbacks = {
                    tuple(sum(c[i] * q[i][j] for i in range(m)) % p for j in range(n)): c
                    for c in targets
                }
                for ell in vectors:
                    annihilates = all(dot(ell, k, p) == 0 for k in kernel)
                    factors = ell in pullbacks
                    assert annihilates == factors
                    if factors:
                        c = pullbacks[ell]
                        assert all(dot(ell, v, p) == dot(c, mv(q, v, p), p) for v in vectors)
                    functional_checks += 1

result = {
    "schema": "marici.physical_readout_descent_criterion.v1",
    "fields_and_dimensions": ["F2, dimensions <= 3", "F3, dimensions <= 2"],
    "surjective_matrix_checks": matrix_checks,
    "functional_checks": functional_checks,
    "passed": True,
    "theorem": "ell factors uniquely through surjective q iff ell annihilates ker(q) iff ell lies in im(q^*)",
}
out = Path(__file__).with_name("results") / "physical-readout-descent-criterion.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
