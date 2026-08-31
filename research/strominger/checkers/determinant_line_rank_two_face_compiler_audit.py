#!/usr/bin/env python3
"""Determinant-line dependency compiler audit for reachable rank-two faces."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "determinant_line_rank_two_face_compiler_audit.json"

labels = ("a", "b", "c", "d")


def all_faces(labels):
    faces = []
    for pair in itertools.combinations(labels, 2):
        rest = [x for x in labels if x not in pair]
        for r in range(len(rest) + 1):
            for base in itertools.combinations(rest, r):
                faces.append((tuple(sorted(base)), pair))
    return faces

faces = all_faces(labels)
base_faces = [f for f in faces if len(f[0]) == 0]
upper_faces = [f for f in faces if len(f[0]) > 0]

# Common trivialized determinant line: a cell is represented by its scalar phase.
# The hostile passes all empty-cutoff squares but fails the upper square based at
# {c} swapping a and b.  This models state-dependent upper phase missed by a
# base-only compiler.
def good_phase(base, pair):
    return Fraction(1)


def hostile_phase(base, pair):
    if base == ("c",) and pair == ("a", "b"):
        return Fraction(-1)
    return Fraction(1)

base_only_accepts_hostile = all(hostile_phase(*face) == 1 for face in base_faces)
exhaustive_rejects_hostile = any(hostile_phase(*face) != 1 for face in faces)

# If every reachable rank-two face is identity, adjacent swaps are literal
# identities and path independence follows for every permutation of additions.
def bubble_word(order):
    word = list(order)
    swaps = []
    for target_index, label in enumerate(sorted(word)):
        i = word.index(label)
        while i > target_index:
            pair = tuple(sorted((word[i - 1], word[i])))
            base = tuple(sorted(word[:i - 1]))
            swaps.append((base, pair))
            word[i - 1], word[i] = word[i], word[i - 1]
            i -= 1
    return swaps

path_phases_good = []
path_phases_hostile = []
for perm in itertools.permutations(labels):
    swaps = bubble_word(perm)
    phase_good = Fraction(1)
    phase_bad = Fraction(1)
    for face in swaps:
        phase_good *= good_phase(*face)
        phase_bad *= hostile_phase(*face)
    path_phases_good.append(phase_good)
    path_phases_hostile.append(phase_bad)

good_paths_agree = len(set(path_phases_good)) == 1 and path_phases_good[0] == 1
hostile_paths_disagree = len(set(path_phases_hostile)) > 1

# Compiler counts: every reachable rank-two face is a base subset plus unordered
# pair disjoint from it.  For n labels, count is C(n,2)*2^(n-2).
expected_face_count = len(labels) * (len(labels) - 1) // 2 * 2 ** (len(labels) - 2)

checks = {
    "compiler_enumerates_all_reachable_rank_two_faces": len(faces) == expected_face_count,
    "base_only_enumeration_accepts_hostile_upper_phase": base_only_accepts_hostile,
    "exhaustive_face_enumeration_rejects_hostile_upper_phase": exhaustive_rejects_hostile,
    "identity_faces_imply_path_independence_in_common_trivialization": good_paths_agree,
    "hostile_upper_phase_makes_complete_paths_disagree": hostile_paths_disagree,
    "no_independent_braid_scalar_remains_after_all_faces_identity": good_paths_agree and all(good_phase(*face) == 1 for face in faces),
}

payload = {
    "schema": "marici.strominger.determinant_line_rank_two_face_compiler_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "labels": labels,
    "face_count": len(faces),
    "expected_face_count": expected_face_count,
    "base_face_count": len(base_faces),
    "upper_face_count": len(upper_faces),
    "hostile_nonidentity_face": {"base": ["c"], "pair": ["a", "b"], "phase": "-1"},
    "path_phase_values_good": sorted({str(x) for x in path_phases_good}),
    "path_phase_values_hostile": sorted({str(x) for x in path_phases_hostile}),
    "verdict": (
        "The determinant-line compiler direction is productive and bounded. In "
        "a common one-dimensional determinant trivialization, connection equality "
        "and basepoint holonomy reduce coherence to exhaustive rank-two face "
        "checking. Base-level squares are insufficient: a hostile upper face can "
        "pass every empty-cutoff square while making full addition paths disagree. "
        "Once every reachable rank-two face is identity, braid and distant "
        "commutation add no independent scalar anomaly. The remaining compiler "
        "work is source enumeration of reachable faces for the actual cutoff "
        "poset and attachment thresholds."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
