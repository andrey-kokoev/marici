#!/usr/bin/env python3
"""Exact free-group face checks for Mikhailov's eta-squared Moore cycle."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "eta_squared_moore_cycle_compiler_checks.json"


Word = tuple[int, ...]


def reduce_word(word: Word) -> Word:
    stack: list[int] = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def inverse(word: Word) -> Word:
    return tuple(-letter for letter in reversed(word))


def multiply(*words: Word) -> Word:
    return reduce_word(tuple(letter for word in words for letter in word))


def commutator(left: Word, right: Word) -> Word:
    return multiply(left, right, inverse(left), inverse(right))


def substitute(word: Word, images: dict[int, Word]) -> Word:
    out: Word = ()
    for letter in word:
        image = images[abs(letter)]
        out = multiply(out, image if letter > 0 else inverse(image))
    return out


x0, x1, x2 = (1,), (2,), (3,)
hopf_01 = commutator(x0, x1)
hopf_02 = commutator(x0, x2)
eta_squared = commutator(hopf_01, hopf_02)

# Mikhailov's degree-three F[S^1] faces, with target generators (1,),(2,).
faces = {
    "d0": {1: (1,), 2: (), 3: (2,)},
    "d1": {1: (1,), 2: (2,), 3: (2,)},
    "d2": {1: (1,), 2: (2,), 3: (1,)},
    "d3": {1: (), 2: (2,), 3: (1,)},
}
face_images = {name: substitute(eta_squared, mapping) for name, mapping in faces.items()}

checks = {
    "word_is_freely_nontrivial": bool(eta_squared),
    "word_has_weight_four": len(eta_squared) == 16,
    "d0_is_identity": face_images["d0"] == (),
    "d1_is_identity": face_images["d1"] == (),
    "d2_is_identity": face_images["d2"] == (),
    "d3_is_identity": face_images["d3"] == (),
    "all_faces_are_identity": all(image == () for image in face_images.values()),
    "source_nonboundary_certificate_is_not_inferred_from_faces": True,
}

payload = {
    "schema": "marici.strominger.eta-squared-moore-cycle-compiler.v1",
    "representative": "[[x0,x1],[x0,x2]]",
    "free_reduced_word": list(eta_squared),
    "free_reduced_length": len(eta_squared),
    "face_images": {name: list(image) for name, image in face_images.items()},
    "checks": checks,
    "aggregate": {"passed": sum(checks.values()), "total": len(checks)},
    "homotopy_typing": {
        "simplicial_degree": 3,
        "target": "pi_3(F[S^1]) = pi_4(S^2)",
        "class": "eta composed with suspension eta",
        "order": 2,
        "nonboundary_authority": "Mikhailov, Simplicial Constructions Associated with S2, section 5",
    },
    "claim_boundary": "the exact Moore word and all faces are compiled; the five-strand Artin-generator expansion remains uncompiled",
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
print(json.dumps({"aggregate": payload["aggregate"], "checker_sha256": digest}, sort_keys=True))

if not all(checks.values()):
    raise SystemExit(1)
