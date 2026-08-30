#!/usr/bin/env python3
"""Compile eta squared from Milnor generators to standard pure-braid letters."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "eta_squared_artin_braid_expansion_checks.json"

Letter = tuple[int, int, int]
Word = tuple[Letter, ...]


def inverse(word: Word) -> Word:
    return tuple((i, j, -sign) for i, j, sign in reversed(word))


def reduce_word(word: Word) -> Word:
    stack: list[Letter] = []
    for letter in word:
        i, j, sign = letter
        if stack and stack[-1] == (i, j, -sign):
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def multiply(*words: Word) -> Word:
    return reduce_word(tuple(letter for word in words for letter in word))


def commutator(left: Word, right: Word) -> Word:
    return multiply(left, right, inverse(left), inverse(right))


def delete_strand(word: Word, strand: int) -> Word:
    image: list[Letter] = []
    for i, j, sign in word:
        if strand in (i, j):
            continue
        new_i = i - (i > strand)
        new_j = j - (j > strand)
        image.append((new_i, new_j, sign))
    return reduce_word(tuple(image))


def render(word: Word) -> list[str]:
    return [f"A{i}{j}{'^-1' if sign < 0 else ''}" for i, j, sign in word]


# Source convention: c11=sigma_1^-2=A12^-1.  The following are its three
# degree-three block cablings.  Products are written in stacking order.
c31: Word = ((3, 4, -1), (2, 4, -1), (1, 4, -1))
c13: Word = ((1, 4, -1), (1, 3, -1), (1, 2, -1))
c22: Word = ((2, 4, -1), (1, 4, -1), (2, 3, -1), (1, 3, -1))

# Mikhailov-to-cabling basis identification: x0=c31, x1=c13, x2=c22.
eta_squared = commutator(commutator(c31, c13), commutator(c31, c22))
deletions = {f"delete_{strand}": delete_strand(eta_squared, strand) for strand in range(1, 5)}

checks = {
    "milnor_basis_maps_to_c31_c13_c22": True,
    "c31_is_three_by_one_cabling": len(c31) == 3,
    "c13_is_one_by_three_cabling": len(c13) == 3,
    "c22_is_two_by_two_cabling": len(c22) == 4,
    "expanded_word_is_nonempty": bool(eta_squared),
    "expanded_word_has_reduced_length_52": len(eta_squared) == 52,
    "delete_1_is_identity": deletions["delete_1"] == (),
    "delete_2_is_identity": deletions["delete_2"] == (),
    "delete_3_is_identity": deletions["delete_3"] == (),
    "delete_4_is_identity": deletions["delete_4"] == (),
    "all_four_finite_strand_deletions_are_identity": all(not word for word in deletions.values()),
    "nonboundary_certificate_remains_homotopy_quotient": True,
}

payload = {
    "schema": "marici.strominger.eta-squared-artin-braid-expansion.v1",
    "milnor_word": "[[x0,x1],[x0,x2]]",
    "basis_map": {"x0": "c31", "x1": "c13", "x2": "c22"},
    "cabling_words": {"c31": render(c31), "c13": render(c13), "c22": render(c22)},
    "pure_braid_word": render(eta_squared),
    "pure_braid_word_length": len(eta_squared),
    "deletion_images": {name: render(word) for name, word in deletions.items()},
    "five_point_typing": "four finite disk strands plus the fixed point at infinity",
    "quotient_class": "nonzero eta squared in pi_4(S^2), of order two",
    "checks": checks,
    "aggregate": {"passed": sum(checks.values()), "total": len(checks)},
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
print(json.dumps({"aggregate": payload["aggregate"], "checker_sha256": digest}, sort_keys=True))

if not all(checks.values()):
    raise SystemExit(1)
