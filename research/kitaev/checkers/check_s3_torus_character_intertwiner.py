#!/usr/bin/env python3
"""Canonical commuting-pair-orbit to D(S3) character-basis intertwiner."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


OUT = Path(__file__).parents[1] / "results" / "s3-torus-character-intertwiner.json"


def compose(p, q):
    return tuple(p[q[i]] for i in range(3))


def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def conjugate(q, p):
    return compose(compose(q, p), inverse(q))


def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    return "e" if fixed == 3 else ("t" if fixed == 1 else "c")


def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) % 2 else 1


def main() -> None:
    group = list(itertools.permutations(range(3)))
    e, t, c = (0, 1, 2), (1, 0, 2), (1, 2, 0)
    reps = {"e": e, "t": t, "c": c}
    classes = {name: [g for g in group if cycle_type(g) == name] for name in reps}
    transporters = {
        name: {g: next(q for q in group if conjugate(q, rep) == g) for g in elements}
        for name, (rep, elements) in {
            name: (reps[name], classes[name]) for name in reps
        }.items()
    }
    labels = [
        ("A", "e", "triv"), ("B", "e", "sign"), ("C", "e", "std"),
        ("D", "t", "plus"), ("E", "t", "minus"),
        ("F", "c", "triv"), ("G", "c", "omega"), ("H", "c", "omega2"),
    ]
    omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2

    def centralizer_character(sector, irrep, z):
        if sector == "e":
            if irrep == "triv": return sp.Integer(1)
            if irrep == "sign": return sp.Integer(parity(z))
            return sp.Integer({"e": 2, "t": 0, "c": -1}[cycle_type(z)])
        if sector == "t":
            return sp.Integer(1 if irrep == "plus" or z == e else -1)
        power = {e: 0, c: 1, compose(c, c): 2}[z]
        exponent = power * {"triv": 0, "omega": 1, "omega2": 2}[irrep] % 3
        return (sp.Integer(1), omega, sp.conjugate(omega))[exponent]

    def character(label, g, x):
        _, sector, irrep = label
        if g not in classes[sector] or compose(g, x) != compose(x, g):
            return sp.Integer(0)
        q = transporters[sector][g]
        z = conjugate(inverse(q), x)
        return centralizer_character(sector, irrep, z)

    commuting = [(g, x) for g in group for x in group if compose(g, x) == compose(x, g)]
    assert len(commuting) == 18

    # Simultaneous-conjugacy orbits are the gauge-invariant flat torus basis.
    remaining = set(commuting)
    orbits = []
    while remaining:
        seed = min(remaining)
        orbit = {tuple((conjugate(q, seed[0]), conjugate(q, seed[1]))) for q in group}
        assert orbit <= set(commuting)
        orbits.append(sorted(orbit))
        remaining -= orbit
    orbits.sort(key=lambda orbit: orbit[0])
    assert len(orbits) == 8

    # W maps normalized orbit states to irreducible-character coordinates.
    # Characters are constant on simultaneous-conjugacy orbits.
    W = sp.zeros(8)
    for a, label in enumerate(labels):
        for o, orbit in enumerate(orbits):
            values = {sp.simplify(character(label, g, x)) for g, x in orbit}
            assert len(values) == 1
            value = values.pop()
            W[a, o] = sp.simplify(sp.sqrt(sp.Rational(len(orbit), 6)) * sp.conjugate(value))
    assert sp.simplify(W * W.H) == sp.eye(8)
    assert sp.simplify(W.H * W) == sp.eye(8)

    # The C-F protected action transported back to orbit coordinates is a
    # canonical involution.  It is not a mere permutation of orbit basis states.
    P = sp.eye(8)
    P[2, 2] = P[5, 5] = 0
    P[2, 5] = P[5, 2] = 1
    U_orbit = sp.simplify(W.H * P * W)
    assert sp.simplify(U_orbit.H * U_orbit) == sp.eye(8)
    assert sp.simplify(U_orbit * U_orbit) == sp.eye(8)
    nonzero_per_row = [sum(sp.simplify(U_orbit[i, j]) != 0 for j in range(8)) for i in range(8)]
    orbit_action_is_permutation = all(count == 1 for count in nonzero_per_row)
    assert not orbit_action_is_permutation
    intertwines = sp.simplify(W * U_orbit - P * W) == sp.zeros(8)
    assert intertwines

    # Abstract coherent record isometry: character label a is retained and a
    # distinct three-bit residue is copied.  Orthogonality proves isometry, but
    # this statement contains no gate decomposition.
    residues = (0, 1, 2, 3, 4, 5, 6, 7)
    record_columns_orthonormal = len(set(residues)) == 8
    assert record_columns_orthonormal

    def perm_text(p):
        return "".join(str(x) for x in p)

    result = {
        "schema": "marici.kitaev.s3-torus-character-intertwiner.v1",
        "source_packet": {
            "commuting_pairs": len(commuting),
            "simultaneous_conjugacy_orbits": len(orbits),
            "orbit_sizes": [len(orbit) for orbit in orbits],
            "orbit_representatives": [[perm_text(g), perm_text(x)] for g, x in (orbit[0] for orbit in orbits)],
        },
        "canonical_character_transform": {
            "shape": [8, 8],
            "left_unitarity": True,
            "right_unitarity": True,
            "normalization": "sqrt(|orbit|/|S3|) times conjugate quantum-double character",
        },
        "protected_CF_transport": {
            "character_basis_action": "swap C and F",
            "orbit_basis_nonzero_entries_per_row": nonzero_per_row,
            "orbit_basis_action_is_permutation": orbit_action_is_permutation,
            "unitary": True,
            "involution": True,
            "intertwining_equation_WU_equals_PW": intertwines,
        },
        "record_boundary": {
            "abstract_nondemolition_record_isometry_exists": record_columns_orthonormal,
            "physical_centralizer_Fourier_bus_on_torus_code": "unproved",
            "existing_bus_scope": "36-dimensional regular endpoint packet with conditional gates",
            "missing_proof": "lift the bus circuit to gauge-invariant torus states and verify W plus code-space preservation and recovery",
            "measurement_only_alternative": "projective character measurement followed by a classical label record destroys C-F coherence",
        },
        "verdict": "The torus-to-sector-label map exists canonically as the exact quantum-double character transform on eight simultaneous-conjugacy orbits, and it intertwines the protected C-F action. This resolves the mathematical coordinate map. It does not resolve executable hybrid composition: the existing centralizer-Fourier bus has not been proven to realize this coherent transform on the torus code space, while measurement followed by a classical record dephases the very C-F coherence needed for unitary S8 control.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
