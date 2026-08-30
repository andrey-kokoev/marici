"""Exact checks for conjugate-reciprocal normal displacement."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def sub(z, w):
    return z[0] - w[0], z[1] - w[1]


def conjugate(z):
    return z[0], -z[1]


def reciprocal_conjugate(s):
    c = conjugate(s)
    return Fraction(1) - c[0], -c[1]


def holomorphic_reflection(s):
    return Fraction(1) - s[0], -s[1]


samples = [
    (Fraction(3, 4), Fraction(0)),
    (Fraction(3, 4), Fraction(5, 3)),
    (Fraction(1, 2), Fraction(7, 2)),
    (Fraction(1, 4), Fraction(-11, 5)),
]

records = []
for s in samples:
    dagger_difference = sub(s, reciprocal_conjugate(s))
    holomorphic_difference = sub(s, holomorphic_reflection(s))
    assert dagger_difference == (2 * s[0] - 1, Fraction(0))
    assert holomorphic_difference == (2 * s[0] - 1, 2 * s[1])
    records.append({
        "s": [str(s[0]), str(s[1])],
        "dagger_difference": [str(x) for x in dagger_difference],
        "holomorphic_difference": [str(x) for x in holomorphic_difference],
    })

critical = (Fraction(1, 2), Fraction(7, 2))
assert sub(critical, reciprocal_conjugate(critical)) == (0, 0)
assert sub(critical, holomorphic_reflection(critical)) != (0, 0)

# Formal additive-Haar adjoint check on x^m and x^n over [0,1]:
# integral x^m (E x^n) + integral ((E+1)x^m) x^n = boundary value 1.
adjoint_records = []
for m, n in [(0, 0), (1, 2), (3, 4), (2, 7)]:
    left = Fraction(n, m + n + 1)
    shifted_left = Fraction(m + 1, m + n + 1)
    boundary = Fraction(1)
    assert left + shifted_left == boundary
    adjoint_records.append({"m": m, "n": n, "boundary_identity": True})

payload = {
    "schema": "marici.research.check.v1",
    "claim": "conjugate reciprocal sewing extracts the real normal displacement while holomorphic reflection does not",
    "spectral_samples": records,
    "critical_line_tangential_sample": [str(x) for x in critical],
    "holomorphic_reflection_fails_line_test": True,
    "additive_haar_adjoint_samples": adjoint_records,
    "verdict": "candidate normal genesis is daggered reciprocal dilation with typed boundary term",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["sha256"] = hashlib.sha256(canonical).hexdigest()

out = Path(__file__).parents[1] / "results" / "rh-conjugate-reciprocal-normal-action.json"
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
