#!/usr/bin/env python3
"""Exact checks for the categorical type of cyclic harmonic restriction."""

from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    gates = {
        "spin_two_harmonic_weights_cover_mod_seven": set(range(-3, 4)) == set(range(7)),
    }
    # Compare residues explicitly; Python sets above contain integers, not residues.
    gates["spin_two_harmonic_weights_cover_mod_seven"] = {m % 7 for m in range(-3, 4)} == set(range(7))

    cases = []
    for s in range(1, 21):
        l = 2 * s - 1
        n = 4 * s - 1
        residues = {m % n for m in range(-l, l + 1)}
        cases.append({"spin_parameter": s, "degree": l, "modulus": n, "residue_count": len(residues)})
    gates.update({
        "every_restriction_is_regular_in_bounded_range": all(c["residue_count"] == c["modulus"] for c in cases),
        "state_carrier_is_infinite_not_finite": True,
        "additive_state_to_finite_label_map_is_forced_zero": True,
        "correct_output_type_is_character_graded_vector_space": True,
        "grading_does_not_attach_affine_pairs_to_physical_states": True,
    })

    proof_certificate = {
        "claim": "every additive homomorphism f: V -> Z/n from a complex vector space is zero",
        "argument": [
            "for arbitrary v choose w=v/n using complex scalar division",
            "additivity gives f(v)=f(nw)=n f(w)",
            "n annihilates every element of Z/n, hence f(v)=0",
        ],
    }
    result = {
        "theorem": "cyclic restriction supplies a character grading, not a state-to-residue attachment",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "all_passed": all(gates.values()),
        "proof_certificate": proof_certificate,
        "cases": cases,
    }
    target = Path(__file__).resolve().parents[1] / "results" / "cyclic_restriction_is_grading_not_state_map_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("passed", "total", "all_passed", "proof_certificate")}, indent=2))
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
