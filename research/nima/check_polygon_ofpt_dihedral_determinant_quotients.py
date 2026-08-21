#!/usr/bin/env python3
"""Test oriented dihedral determinant quotients for triangle, square, and pentagon OFPT packets."""

import json
import sys
from pathlib import Path

from sage.all import QQ, identity_matrix, matrix, vector

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research/benincasa/checkers"))
sys.path.insert(0, str(ROOT / "research/nima"))

from derive_polygon_ofpt_packet import polygon
from check_five_site_ofpt_dihedral_selector import (
    boundary, oriented_action, reflect_site, rotate_site,
)

OUTPUT = ROOT / "research/nima/results/polygon-ofpt-dihedral-determinant-quotients.json"


def audit(n):
    packet = polygon(n)
    terms = packet["terms"]
    facets = sorted({label for term in terms for label in term})
    order = {label: position for position, label in enumerate(facets)}
    simplices = [tuple(sorted(term, key=order.__getitem__)) for term in terms]
    index = {frozenset(simplex): column for column, simplex in enumerate(simplices)}
    faces = sorted({face for simplex in simplices for face, _ in boundary(simplex)})
    face_index = {face: row for row, face in enumerate(faces)}
    d = matrix(QQ, len(faces), len(simplices), sparse=True)
    for column, simplex in enumerate(simplices):
        for face, sign in boundary(simplex):
            d[face_index[face], column] = sign

    rotation = oriented_action(
        simplices, index, order, rotate_site, n
    )
    reflection = oriented_action(
        simplices, index, order, reflect_site, n
    )
    unit = identity_matrix(QQ, len(simplices), sparse=True)
    cyclic = d.stack(rotation-unit).right_kernel()
    even = d.stack(rotation-unit).stack(reflection-unit).right_kernel()
    odd = d.stack(rotation-unit).stack(reflection+unit).right_kernel()
    determinant = vector(QQ, packet["ordered_denominator_determinants"])
    determinant_rotation_character = (
        1 if determinant*rotation == determinant else
        -1 if determinant*rotation == -determinant else None
    )
    determinant_reflection_character = (
        1 if determinant*reflection == determinant else
        -1 if determinant*reflection == -determinant else None
    )
    determinant_character_sector = (
        d.stack(rotation-determinant_rotation_character*unit)
         .stack(reflection-determinant_reflection_character*unit)
         .right_kernel()
    )
    determinant_character_values = [
        determinant.dot_product(item)
        for item in determinant_character_sector.basis()
    ]
    even_values = [determinant.dot_product(item) for item in even.basis()]
    odd_values = [determinant.dot_product(item) for item in odd.basis()]

    assert rotation**n == unit
    assert reflection**2 == unit
    assert reflection*rotation*reflection == rotation**(n-1)
    return {
        "n": n,
        "term_count": len(terms),
        "boundary_kernel_dimension": int(d.right_kernel().dimension()),
        "cyclic_invariant_dimension": int(cyclic.dimension()),
        "reflection_even_dimension": int(even.dimension()),
        "reflection_odd_dimension": int(odd.dimension()),
        "determinant_rotation_character": determinant_rotation_character,
        "determinant_reflection_character": determinant_reflection_character,
        "determinant_nonzero_on_even": any(even_values),
        "determinant_nonzero_on_odd": any(odd_values),
        "determinant_even_basis_values": list(map(str, even_values)),
        "determinant_odd_basis_values": list(map(str, odd_values)),
        "determinant_character_sector_dimension": int(determinant_character_sector.dimension()),
        "determinant_character_basis_values": list(map(str, determinant_character_values)),
        "canonical_rank_one_character_quotient": (
            bool(determinant_character_sector.dimension()) and
            any(determinant_character_values)
        ),
    }


def main():
    audits = [audit(n) for n in (3, 4, 5, 6)]
    output = {
        "schema": "marici.polygon_ofpt.dihedral_determinant_quotients.v2",
        "audits": audits,
        "determinant_character_quotient_exists_at_all_tested_arities": all(
            item["canonical_rank_one_character_quotient"] for item in audits
        ),
        "scope": "Exact source facet packets for n=3,4,5,6; no physical-chain activation asserted.",
        "passed": True,
    }
    OUTPUT.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
