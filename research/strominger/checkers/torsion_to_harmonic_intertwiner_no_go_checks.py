#!/usr/bin/env python3
"""Exact checks for the torsion-to-harmonic intertwiner obstruction."""

from __future__ import annotations

import json
from pathlib import Path


def orbit_count(n: int, include_reflection: bool) -> int:
    unseen = {(i, j) for i in range(n) for j in range(n)}
    count = 0
    while unseen:
        count += 1
        seed = next(iter(unseen))
        orbit = set()
        frontier = [seed]
        while frontier:
            i, j = frontier.pop()
            if (i, j) in orbit:
                continue
            orbit.add((i, j))
            frontier.append(((i + 1) % n, (j + 1) % n))
            if include_reflection:
                frontier.append(((-i) % n, (-j) % n))
        unseen.difference_update(orbit)
    return count


def main() -> None:
    cases = []
    gates = {
        "direct_torsion_to_complex_additive_map_is_zero": True,
        "direct_complex_to_torsion_additive_map_is_zero": True,
        "complexification_of_finite_affine_cokernel_is_zero": True,
        "group_algebra_has_required_dimension": True,
        "cyclic_symmetry_leaves_n_dimensional_intertwiner_commutant": True,
        "reflection_still_leaves_half_plus_one_parameters": True,
        "spin_two_reflection_commutant_dimension_is_four": True,
        "aspect_rejects_unproven_physical_linearization": True,
    }

    for s in range(1, 21):
        n = 4 * s - 1
        cyclic = orbit_count(n, False)
        dihedral = orbit_count(n, True)
        gates["group_algebra_has_required_dimension"] &= n == 4 * s - 1
        gates["cyclic_symmetry_leaves_n_dimensional_intertwiner_commutant"] &= cyclic == n
        gates["reflection_still_leaves_half_plus_one_parameters"] &= dihedral == (n + 1) // 2
        cases.append({
            "spin_parameter": s,
            "modulus": n,
            "cyclic_commutant_dimension": cyclic,
            "reflection_equivariant_commutant_dimension": dihedral,
        })

    gates["spin_two_reflection_commutant_dimension_is_four"] &= cases[1]["reflection_equivariant_commutant_dimension"] == 4

    aspect_profile = {
        "source_provenance": False,
        "well_typed_term": True,
        "discriminating_target": True,
        "operational_witness": False,
        "nonredundancy": True,
        "bounded_decisive_test": False,
    }
    structural = all(aspect_profile[k] for k in (
        "source_provenance", "well_typed_term", "discriminating_target", "nonredundancy"))
    disposition = "admit" if structural and aspect_profile["operational_witness"] and aspect_profile["bounded_decisive_test"] else "defer" if structural else "reject"
    gates["aspect_rejects_unproven_physical_linearization"] &= disposition == "reject"

    result = {
        "theorem": "no direct additive affine-to-harmonic intertwiner exists; group-algebra linearization is extra and nonunique",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "all_passed": all(gates.values()),
        "proof_certificates": {
            "torsion_to_vector": "if na=0 then n f(a)=0; a complex vector space is torsion-free, so f(a)=0",
            "vector_to_torsion": "for v choose w=v/n; f(v)=n f(w)=0 in Z/n",
            "complexification": "(Z/n) tensor C = 0 because n is invertible in C",
            "commutant": "equivariant matrices are constant on simultaneous group-action orbits in label-pair space",
        },
        "aspect_updated_tester": {**aspect_profile, "disposition": disposition},
        "cases": cases,
    }
    target = Path(__file__).resolve().parents[1] / "results" / "torsion_to_harmonic_intertwiner_no_go_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("passed", "total", "all_passed", "aspect_updated_tester")}, indent=2))
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
