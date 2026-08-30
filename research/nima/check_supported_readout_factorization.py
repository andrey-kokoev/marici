"""Exhaustive audit of factorization and extension ambiguity for arbitrary maps."""

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


matrix_checks = functional_checks = extension_checks = 0
for p, max_dim in ((2, 3), (3, 2)):
    for n in range(1, max_dim + 1):
        domain = list(product(range(p), repeat=n))
        for m in range(1, max_dim + 1):
            codual = list(product(range(p), repeat=m))
            for flat in product(range(p), repeat=m * n):
                q = [flat[i * n:(i + 1) * n] for i in range(m)]
                rq = rank(q, p)
                kernel = [v for v in domain if mv(q, v, p) == (0,) * m]
                pullbacks = {}
                for c in codual:
                    ell = tuple(sum(c[i] * q[i][j] for i in range(m)) % p for j in range(n))
                    pullbacks.setdefault(ell, []).append(c)
                matrix_checks += 1
                for ell in domain:
                    annihilates = all(dot(ell, k, p) == 0 for k in kernel)
                    extensions = pullbacks.get(ell, [])
                    assert annihilates == bool(extensions)
                    if extensions:
                        assert len(extensions) == p ** (m - rq)
                        # All extensions agree on im(q).
                        for v in domain:
                            values = {dot(c, mv(q, v, p), p) for c in extensions}
                            assert values == {dot(ell, v, p)}
                            extension_checks += len(extensions)
                    functional_checks += 1

result = {
    "schema": "marici.supported_readout_factorization.v1",
    "fields_and_dimensions": ["F2, domain/codomain <= 3", "F3, domain/codomain <= 2"],
    "matrix_checks": matrix_checks,
    "functional_checks": functional_checks,
    "extension_agreement_checks": extension_checks,
    "passed": True,
    "theorem": "ell annihilates ker(q) iff it factors uniquely on im(q); extensions to W form an affine space of size p^(dim W-rank q)",
}
out = Path(__file__).with_name("results") / "supported-readout-factorization.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result))
