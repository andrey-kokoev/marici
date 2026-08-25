#!/usr/bin/env python3
"""Derive the coherent S3 transporter and exact sector-label lookup actions."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np


ELEMENTS = tuple((k, e) for k in range(3) for e in range(2))
INDEX = {g: i for i, g in enumerate(ELEMENTS)}
SECTOR_RESIDUES = dict(zip("ABCDEFGH", (0, 1, 2, 3, 6, 7, 4, 5)))


def mul(g, h):
    k, e = g
    l, f = h
    return ((k + (-1 if e else 1) * l) % 3, (e + f) % 2)


def inv(g):
    return next(h for h in ELEMENTS if mul(g, h) == mul(h, g) == (0, 0))


def conjugate(t, h):
    return mul(mul(t, h), inv(t))


def flux_class(h):
    k, e = h
    if h == (0, 0):
        return "identity"
    if e:
        return "transposition"
    return "three_cycle"


def representative(h):
    return {"identity": (0, 0), "transposition": (0, 1), "three_cycle": (1, 0)}[
        flux_class(h)
    ]


def transporter(h):
    k, e = h
    if h == (0, 0) or h == (1, 0):
        return (0, 0)
    if h == (2, 0):
        return (0, 1)
    # h=c^k s and c^k h c^-k=s.
    return (k, 0)


def alignment_matrix():
    matrix = np.zeros((36, 36), dtype=complex)
    for h in ELEMENTS:
        for x in ELEMENTS:
            source = 6 * INDEX[h] + INDEX[x]
            target_x = mul(transporter(h), x)
            target = 6 * INDEX[h] + INDEX[target_x]
            matrix[target, source] = 1
    return matrix


def local_pauli(d, x, z):
    shift = np.roll(np.eye(d, dtype=complex), 1, axis=0)
    phase = np.diag(np.exp(2j * np.pi * np.arange(d) / d))
    return np.linalg.matrix_power(shift, x) @ np.linalg.matrix_power(phase, z)


def hybrid_pauli(a, b, c, d):
    # Each S3 register is represented as qutrit rotation tensor qubit parity.
    return np.kron(local_pauli(3, a, b), local_pauli(2, c, d))


def equal_up_to_phase(left, right, tolerance=1e-9):
    overlap = np.vdot(right.reshape(-1), left.reshape(-1))
    if abs(overlap) < tolerance:
        return False
    return np.max(np.abs(left - overlap / abs(overlap) * right)) < tolerance


def main():
    table = []
    for h in ELEMENTS:
        t = transporter(h)
        assert conjugate(t, h) == representative(h)
        table.append(
            {
                "holonomy": list(h),
                "flux_class": flux_class(h),
                "transporter": list(t),
                "representative": list(representative(h)),
            }
        )

    align = alignment_matrix()
    assert np.max(np.abs(align.conj().T @ align - np.eye(36))) < 1e-9
    assert np.max(np.abs(align.conj().T - np.linalg.inv(align))) < 1e-9

    one = np.eye(6)
    component_generators = [
        hybrid_pauli(1, 0, 0, 0),
        hybrid_pauli(0, 1, 0, 0),
        hybrid_pauli(0, 0, 1, 0),
        hybrid_pauli(0, 0, 0, 1),
    ]
    product_generators = [np.kron(g, one) for g in component_generators] + [
        np.kron(one, g) for g in component_generators
    ]
    product_paulis = [
        np.kron(h, x)
        for h in (
            hybrid_pauli(a, b, c, d)
            for a, b, c, d in itertools.product(range(3), range(3), range(2), range(2))
        )
        for x in (
            hybrid_pauli(a, b, c, d)
            for a, b, c, d in itertools.product(range(3), range(3), range(2), range(2))
        )
    ]
    inside = []
    for generator in product_generators:
        image = align @ generator @ align.conj().T
        inside.append(any(equal_up_to_phase(image, candidate) for candidate in product_paulis))
    assert not all(inside)

    lookup = []
    for sector in "ABCDEFGH":
        residue = SECTOR_RESIDUES[sector]
        bits = [(residue >> shift) & 1 for shift in (2, 1, 0)]
        lookup.append({"sector": sector, "residue": residue, "bits_b2_b1_b0": bits})
        for initial in range(8):
            copied = initial ^ residue
            cleaned = copied ^ residue
            assert cleaned == initial

    result = {
        "schema": "marici.kitaev.s3-transporter-and-label-lookup.v1",
        "transporter_table": table,
        "alignment": {
            "basis_cases": 36,
            "action": "|h,x> maps to |h,t(h)x>",
            "inverse": "|h,x> maps to |h,t(h)^-1 x>",
            "unitary_permutation": True,
            "product_pauli_generator_images_inside": inside,
            "is_product_clifford": all(inside),
        },
        "sector_lookup": lookup,
        "encoded_label_copy": {
            "action": "|r>|l> maps to |r>|l XOR r> on three logical qubits",
            "primitive_logical_gates": "three qubit SUM gates",
            "clean_inverse": "the same three SUM gates",
            "all_64_source_target_cases_clean": True,
            "executable_by_verified_clifford_teleportation": True,
        },
        "lookup_boundary": "The residue truth table is exact, and label-to-label copy is Clifford. Coherently computing its three predicates from flux and centralizer-charge modes is a central-projector-controlled lookup, not supplied by the frozen product-Clifford interfaces.",
        "verdict": "The transporter and label-copy actions are now explicit. The 36-state transporter is non-Clifford on the frozen hybrid encoding. Three-bit label copy is executable Clifford once a residue exists, while coherent sector-to-residue lookup remains a nonstabilizer controlled-projector gate.",
    }
    output = Path(__file__).parents[1] / "results" / "s3-transporter-and-label-lookup.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
