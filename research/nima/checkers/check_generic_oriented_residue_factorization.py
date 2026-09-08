#!/usr/bin/env python3
"""Exact finite stages of generic orientation-valued residue factorization."""
import importlib.util
import itertools
import json
from pathlib import Path

helper_path = Path(__file__).with_name("check_generic_polygon_face_product.py")
spec = importlib.util.spec_from_file_location("polygon_faces", helper_path)
poly = importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)


def amplitude(n):
    return {t: 1 for t in poly.dissections_on(poly.diagonals(n)) if len(t) == n - 3}


def residue(value, cuts):
    cuts = frozenset(cuts)
    return {term - cuts: coefficient for term, coefficient in value.items() if cuts <= term}


def multiply(left, right):
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            assert a.isdisjoint(b)
            out[a | b] = out.get(a | b, 0) + ca * cb
    return out


def regional_product(n, cuts):
    result = {frozenset(): 1}
    for region in poly.split_regions(n, cuts):
        local = {t: 1 for t in poly.dissections_on(poly.region_diagonals(region)) if len(t) == len(region) - 3}
        result = multiply(result, local)
    return result


def parity(sequence):
    inversions = sum(sequence[i] > sequence[j] for i in range(len(sequence)) for j in range(i + 1, len(sequence)))
    return -1 if inversions % 2 else 1


def relative_sign(sequence, canonical):
    positions = {value: index for index, value in enumerate(canonical)}
    return parity([positions[value] for value in sequence])


def verify(n):
    channels = tuple(sorted(poly.diagonals(n)))
    value = amplitude(n)
    direct_checks = nested_checks = orientation_checks = residual_terms = 0
    for cuts in poly.dissections_on(channels):
        canonical = tuple(sorted(cuts))
        direct = residue(value, cuts)
        expected = regional_product(n, cuts)
        assert direct == expected
        direct_checks += 1
        residual_terms += len(direct)
        remainder = tuple(channel for channel in channels if channel not in cuts)
        canonical_ambient_sign = relative_sign(canonical + remainder, channels)
        for ordering in itertools.permutations(canonical):
            nested = value
            for channel in ordering:
                nested = residue(nested, [channel])
            assert nested == direct
            raw_sign = relative_sign(ordering + remainder, channels)
            orientation_sign = relative_sign(ordering, canonical)
            assert raw_sign * orientation_sign == canonical_ambient_sign
            nested_checks += 1
            orientation_checks += 1
    return {
        "n": n,
        "direct_factorizations": direct_checks,
        "ordered_nested_factorizations": nested_checks,
        "orientation_transport_checks": orientation_checks,
        "residual_monomials": residual_terms,
    }


stages = [verify(n) for n in range(3, 8)]
result = {
    "schema": "marici.generic-oriented-residue-factorization.v1",
    "status": "passed",
    "strength": "exhaustive finite stages n=3..7 plus a generic set-level construction; not a checked unbounded formal theorem or analytic normalization",
    "statement": "orientation-valued residue along D equals the product of regional weighted sums tensored with the canonical generator of det(Z^D)",
    "stages": stages,
    "boundary": "formal Laurent coefficient residue with determinant-line orientation; no local analytic coordinate, contour, or amplitude normalization",
}
out = Path("research/nima/results/generic_oriented_residue_factorization.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
