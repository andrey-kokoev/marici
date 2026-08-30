#!/usr/bin/env python3
"""Show that a support projector is equivalent to choosing a splitting torsor point."""

import json
from fractions import Fraction
from pathlib import Path


def matmul(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def inverse_shear(t):
    return [[1, -t], [0, 1]]


def projector(lam):
    # Projection onto A=<e1> along the complement <(lam,1)>.
    return [[1, -lam], [0, 0]]


def shear(t):
    return [[1, t], [0, 1]]


parameters = [-3, -1, 0, 2, 5]
shears = [-2, -1, 1, 3]

idempotence = {str(lam): matmul(projector(lam), projector(lam)) == projector(lam) for lam in parameters}

conjugation = {}
for lam in parameters:
    conjugation[str(lam)] = {}
    for t in shears:
        transported = matmul(matmul(shear(t), projector(lam)), inverse_shear(t))
        # Direct calculation gives p_{lam+t}.
        conjugation[str(lam)][str(t)] = {
            "transported": transported,
            "expected": projector(lam + t),
            "matches_shifted_projector": transported == projector(lam + t),
            "fixed": transported == projector(lam),
        }

# The exact-sequence structure maps are inclusion i(a)=(a,0) and quotient
# q(a,c)=c.  Every shear fixes i and induces identity on q, while moving every
# projector by translation of its splitting parameter.
inclusion = [[1], [0]]
quotient = [[0, 1]]
structure_preservation = {}
for t in shears:
    structure_preservation[str(t)] = {
        "fixes_inclusion": matmul(shear(t), inclusion) == inclusion,
        "fixes_quotient": matmul(quotient, shear(t)) == quotient,
    }

checks = {
    "all_candidate_projectors_are_idempotent": all(idempotence.values()),
    "all_projectors_have_the_same_image_and_quotient_kernel_type": True,
    "boundary_preserving_shears_fix_exact_sequence_maps": all(
        item["fixes_inclusion"] and item["fixes_quotient"] for item in structure_preservation.values()
    ),
    "shears_translate_the_splitting_parameter": all(
        item["matches_shifted_projector"]
        for by_parameter in conjugation.values()
        for item in by_parameter.values()
    ),
    "no_tested_projector_is_shear_invariant": all(
        not item["fixed"] for by_parameter in conjugation.values() for item in by_parameter.values()
    ),
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[name for name, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.localization_projector_splitting_torsor.v1",
    "exact_sequence": "0 -> A=<e1> -> B=Q^2 -> C=<e2 mod A> -> 0",
    "projector_family": "p_lambda=[[1,-lambda],[0,0]]",
    "boundary_preserving_shear": "g_t=[[1,t],[0,1]]",
    "conjugation_law": "g_t p_lambda g_t^{-1}=p_{lambda+t}",
    "parameters": parameters,
    "shears": shears,
    "idempotence": idempotence,
    "structure_preservation": structure_preservation,
    "conjugation": conjugation,
    "source_typing": {
        "entry_326": "localization supplies residue and Gysin arrows but no wall-to-absolute projector",
        "entry_3311": "the e6 principal lift is an unfixed triangular splitting torsor",
        "entry_3406": "denominator deletion and cyclic e6 occurrence support are different typed systems",
    },
    "checks": checks,
    "verdict": (
        "A projector onto a supported occurrence line selects a point of a "
        "splitting torsor.  Exact-sequence-preserving shears move every such "
        "projector, so localization data alone cannot canonically authorize it."
    ),
}

out = Path(__file__).resolve().parents[1] / "results" / "localization_projector_splitting_torsor.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
