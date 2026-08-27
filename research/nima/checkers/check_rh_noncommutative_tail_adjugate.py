"""Exact finite check for the noncommutative tail adjugate residual."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def add(a, b):
    n = max(len(a), len(b))
    return trim(
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(n)
    )


def scale(c, a):
    return trim(c * x for x in a)


def mul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def deriv(a):
    if len(a) == 1:
        return (Fraction(0),)
    return trim(Fraction(i) * a[i] for i in range(1, len(a)))


def sub(a, b):
    return add(a, scale(Fraction(-1), b))


z = Fraction(3, 2)
f = (Fraction(1), Fraction(2), Fraction(1))
fp = deriv(f)


def p(a):
    return deriv(a)


def ell(a):
    return add(p(a), scale(z, a))


def diagonal(a):
    return add(p(p(a)), scale(z, p(a)))


def d(pair):
    u, v = pair
    return add(ell(u), mul(f, v)), p(v)


def q(pair):
    x, y = pair
    return sub(p(x), mul(f, y)), ell(y)


tests = [
    ((Fraction(1), Fraction(2)), (Fraction(3), Fraction(-1), Fraction(2))),
    ((Fraction(0), Fraction(1), Fraction(1)), (Fraction(2),)),
    ((Fraction(-2), Fraction(0), Fraction(3)), (Fraction(1), Fraction(4))),
]

checks = []
for pair in tests:
    qd = q(d(pair))
    dq = d(q(pair))
    expected_diag = (diagonal(pair[0]), diagonal(pair[1]))
    qd_residual = (sub(qd[0], expected_diag[0]), sub(qd[1], expected_diag[1]))
    dq_residual = (sub(dq[0], expected_diag[0]), sub(dq[1], expected_diag[1]))
    positive = (mul(fp, pair[1]), (Fraction(0),))
    negative = (scale(Fraction(-1), mul(fp, pair[1])), (Fraction(0),))
    checks.append(qd_residual == positive and dq_residual == negative)

assert all(checks)
assert fp != (Fraction(0),)

payload = {
    "schema": "marici.research.check.v1",
    "claim": "naive noncommutative tail adjugate leaves opposite forcing-derivative residuals",
    "test_vectors": len(tests),
    "all_exact_identities_pass": all(checks),
    "forcing_derivative_coefficients": [str(x) for x in fp],
    "qd_off_diagonal_sign": 1,
    "dq_off_diagonal_sign": -1,
    "diagonal_operator": "P^2 + z P",
    "verdict": "naive reverse arrow falsified",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-noncommutative-tail-adjugate.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
