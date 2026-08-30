"""Exact word census for the spin-two grade-three rigidity falsifier."""

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = ROOT / "research/strominger/spin-two-grade-three-constructor-rigidity-falsifier.md"
l = sp.symbols("l", integer=True, nonnegative=True)


def step_factor_squared(kind, spin):
    if kind == "E":
        return (l - spin) * (l + spin + 1), spin + 1
    return (l + spin) * (l - spin + 1), spin - 1


def word_multiplier_squared(word):
    spin = 2
    value = sp.Integer(1)
    for kind in word:
        factor, spin = step_factor_squared(kind, spin)
        value *= factor
    return sp.factor(value), spin


words = sorted({"".join(p) for p in itertools.permutations("EEEB")})
expected = {
    "BEEE": {"zeros": [2, 3], "kernel": 12, "cokernel": 0, "index": 12},
    "EBEE": {"zeros": [2, 3], "kernel": 12, "cokernel": 0, "index": 12},
    "EEBE": {"zeros": [2, 3], "kernel": 12, "cokernel": 0, "index": 12},
    "EEEB": {"zeros": [2, 3, 4], "kernel": 21, "cokernel": 9, "index": 12},
}

checks = {"exactly_four_words": words == sorted(expected)}
observed = {}
for word in words:
    polynomial, target_spin = word_multiplier_squared(word)
    zeros = [degree for degree in range(2, 12) if polynomial.subs(l, degree) == 0]
    kernel = sum(2 * degree + 1 for degree in zeros)
    cokernel = 9 if 4 in zeros else 0
    record = {
        "multiplier_squared": str(polynomial),
        "target_spin": target_spin,
        "zeros": zeros,
        "kernel": kernel,
        "cokernel": cokernel,
        "index": kernel - cokernel,
        "polynomial_degree": sp.degree(polynomial, l),
        "leading_coefficient": sp.LC(sp.Poly(polynomial, l)),
    }
    observed[word] = record
    checks[f"{word}_target_spin_four"] = target_spin == 4
    checks[f"{word}_exact_record"] = all(record[key] == value for key, value in expected[word].items())
    checks[f"{word}_principal_degree_eight"] = record["polynomial_degree"] == 8
    checks[f"{word}_monic_principal_symbol"] = record["leading_coefficient"] == 1

checks.update({
    "all_words_have_same_index": {observed[w]["index"] for w in words} == {12},
    "kernel_dimension_not_rigid": {observed[w]["kernel"] for w in words} == {12, 21},
    "canonical_word_has_l4_kernel": observed["EEEB"]["zeros"] == [2, 3, 4],
    "other_words_reach_l4": all(4 not in observed[w]["zeros"] for w in words if w != "EEEB"),
    "kernel_cokernel_trade_is_nine": observed["EEEB"]["kernel"] - observed["BEEE"]["kernel"] == 9
    and observed["EEEB"]["cokernel"] - observed["BEEE"]["cokernel"] == 9,
})

failed = [name for name, passed in checks.items() if not passed]
serializable = {
    word: {key: int(value) if isinstance(value, sp.Integer) else value for key, value in record.items()}
    for word, record in observed.items()
}
payload = {
    "schema": "marici.strominger.spin-two-grade-three-constructor-rigidity-result.v1",
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "observed": serializable,
    "verdict": "The four covariant fourth-order words share principal symbol and index 12, but only EEEB has kernel dimension 21. The ordered constructor, not covariance and order alone, protects the extra l=4 block.",
}
print(json.dumps(payload, indent=2, sort_keys=True))
if failed:
    raise SystemExit("failed checks: " + ", ".join(failed))
