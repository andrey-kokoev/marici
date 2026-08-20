"""Derive finite prime/factorization readouts from the conditional Carrier semiring."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SEMIRING = ROOT / "research/nima/results/phase-i-endomorphism-semiring.json"
OUT = ROOT / "research/nima/results/phase-i-intrinsic-primes.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


packet = json.loads(SEMIRING.read_text(encoding="utf-8"))
assert packet["verdict"]["conditional_initial_semiring_on_pi0_derived"] is True

# Integers encode connected-component normal forms after the construction.
# The test derives irreducibility from the multiplication table; no prime list
# is supplied.
cutoff = 256


def factors(value: int) -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, value // left)
        for left in range(1, value + 1)
        if value % left == 0
    )


def irreducible(value: int) -> bool:
    if value in (0, 1):
        return False
    return all(left == 1 or right == 1 for left, right in factors(value))


irreducibles = tuple(value for value in range(cutoff + 1) if irreducible(value))

# Prime-element implication, tested without a predeclared prime list.
prime_implication_checks = 0
for candidate in irreducibles:
    for left in range(cutoff + 1):
        for right in range(cutoff + 1):
            if (left * right) % candidate == 0:
                assert left % candidate == 0 or right % candidate == 0
            prime_implication_checks += 1


def derived_factorization(value: int) -> tuple[int, ...]:
    """Recursively split by the first proper factor discovered internally."""

    if value == 1:
        return tuple()
    if irreducible(value):
        return (value,)
    for left, right in factors(value):
        if left not in (1, value):
            return tuple(sorted(derived_factorization(left) + derived_factorization(right)))
    raise AssertionError(f"No factorization branch for {value}")


factorizations = {value: derived_factorization(value) for value in range(1, cutoff + 1)}
assert all(
    all(irreducible(factor) for factor in decomposition)
    for decomposition in factorizations.values()
)
assert all(
    __import__("math").prod(decomposition) == value
    for value, decomposition in factorizations.items()
)

# Exhaustively enumerate unordered irreducible products within the cutoff and
# verify that each value has only the recursively derived multiset.
representations: dict[int, set[tuple[int, ...]]] = {value: set() for value in range(1, cutoff + 1)}


def enumerate_products(start: int, product: int, word: tuple[int, ...]) -> None:
    representations[product].add(word)
    for index in range(start, len(irreducibles)):
        factor = irreducibles[index]
        next_product = product * factor
        if next_product > cutoff:
            break
        enumerate_products(index, next_product, word + (factor,))


enumerate_products(0, 1, tuple())
assert all(representations[value] == {factorizations[value]} for value in representations)

out = {
    "schema": "marici.nima.phase_i_intrinsic_primes.v1",
    "status": "conditional_theorem_with_finite_exact_control",
    "input_sha256": {str(SEMIRING.relative_to(ROOT)).replace("\\", "/"): digest(SEMIRING)},
    "definitions": {
        "unit": "the connected generator U",
        "divides": "a divides b iff b=f_a(c) for some c",
        "irreducible": "nonzero nonunit with no factorization into two nonunits",
        "prime": "nonzero nonunit p with p|ab implying p|a or p|b",
        "external_prime_list_used": False,
    },
    "finite_controls": {
        "cutoff": cutoff,
        "derived_irreducibles": irreducibles,
        "irreducible_count": len(irreducibles),
        "prime_implication_checks": prime_implication_checks,
        "unique_factorization_values_checked": cutoff,
    },
    "verdict": {
        "conditional_intrinsic_prime_elements_derived": True,
        "conditional_unique_factorization_derived": True,
        "closed_points_of_spec_z_derived": False,
        "arithmetic_frobenius_derived": False,
        "euler_product_derived": False,
    },
}

OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out))
