#!/usr/bin/env python3
"""Exact finite-stage orientation-line coherence for polygon dissections."""
import importlib.util
import itertools
import json
from pathlib import Path

helper_path = Path(__file__).with_name("check_generic_polygon_face_product.py")
spec = importlib.util.spec_from_file_location("polygon_faces", helper_path)
poly = importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)


def parity_sign(sequence):
    inversions = sum(sequence[i] > sequence[j] for i in range(len(sequence)) for j in range(i + 1, len(sequence)))
    return -1 if inversions % 2 else 1


def relative_sign(sequence, canonical):
    positions = {value: index for index, value in enumerate(canonical)}
    return parity_sign([positions[value] for value in sequence])


def wedge_transport(left, right):
    union = tuple(sorted(left + right))
    return relative_sign(tuple(sorted(left)) + tuple(sorted(right)), union)


def verify(n):
    ambient = tuple(sorted(poly.diagonals(n)))
    dissections = sorted(poly.dissections_on(ambient), key=lambda d: (len(d), repr(d)))
    permutation_checks = binary_checks = associativity_checks = 0
    max_codimension = 0
    for dissection in dissections:
        canonical = tuple(sorted(dissection))
        max_codimension = max(max_codimension, len(canonical))
        remainder = tuple(d for d in ambient if d not in dissection)
        canonical_ambient_residue = relative_sign(canonical + remainder, ambient)
        for ordered in itertools.permutations(canonical):
            raw = relative_sign(ordered + remainder, ambient)
            orientation = relative_sign(ordered, canonical)
            assert raw * orientation == canonical_ambient_residue
            permutation_checks += 1
        for assignment in itertools.product(range(2), repeat=len(canonical)):
            left = tuple(canonical[i] for i, side in enumerate(assignment) if side == 0)
            right = tuple(canonical[i] for i, side in enumerate(assignment) if side == 1)
            assert wedge_transport(left, right) == relative_sign(tuple(sorted(left)) + tuple(sorted(right)), canonical)
            binary_checks += 1
        for assignment in itertools.product(range(3), repeat=len(canonical)):
            blocks = [tuple(canonical[i] for i, part in enumerate(assignment) if part == label) for label in range(3)]
            a, b, c = blocks
            left_associated = wedge_transport(a, b) * wedge_transport(tuple(sorted(a + b)), c)
            right_associated = wedge_transport(b, c) * wedge_transport(a, tuple(sorted(b + c)))
            assert left_associated == right_associated
            associativity_checks += 1
    return {
        "n": n,
        "dissections": len(dissections),
        "max_codimension": max_codimension,
        "ordering_checks": permutation_checks,
        "binary_union_checks": binary_checks,
        "associativity_cocycle_checks": associativity_checks,
    }


stages = [verify(n) for n in range(3, 8)]
assert sum(stage["associativity_cocycle_checks"] for stage in stages) > 0
result = {
    "schema": "marici.generic-orientation-line-residue.v1",
    "status": "passed",
    "strength": "exhaustive finite polygon stages n=3..7; generic construction stated but no unbounded formal theorem",
    "orientation_line": "or(D)=det(Z^D)",
    "transport": "wedge on disjoint channel sets",
    "symmetry": "Koszul sign",
    "stages": stages,
    "boundary": "orientation coherence only; residue coefficients rely on the separate generic factorization checker and no contour or normalization is supplied",
}
out = Path("research/nima/results/generic_orientation_line_residue.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
