"""Export the C3 character constraint for higher sextic specializations."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def matmul(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]


def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("orbits", type=Path)
    parser.add_argument("naturality", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    orbits = json.loads(args.orbits.read_text(encoding="utf-8"))
    naturality = json.loads(args.naturality.read_text(encoding="utf-8"))

    sigma = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
    sigma2 = matmul(sigma, sigma)
    sigma3 = matmul(sigma2, sigma)
    identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    if sigma3 != identity:
        raise AssertionError("C3 permutation does not close")
    character = [trace(identity), trace(sigma), trace(sigma2)]
    if character != [3, 0, 0]:
        raise AssertionError("unexpected regular character")
    if not orbits["all_occurrence_orbits_free_of_size_three"]:
        raise AssertionError("occurrence action is not free")
    if not naturality["all_naturality_squares_close"]:
        raise AssertionError("generic Kato-Gysin transitions do not close")

    orbit_rows = []
    for orbit in orbits["orbits"]:
        orbit_rows.append({
            "representative_in_G12": orbit["representative_in_G12"],
            "occurrence_orbit_size": 3,
            "generic_transition_units": [1, 1, 1],
            "specialized_rank_if_local_rank_is_r": "3*r",
            "C3_character_if_local_rank_is_r": ["3*r", "0", "0"],
            "rational_decomposition": "r copies of (Q_trivial plus Q[zeta_3])",
            "scalar_polynomial_orbit_size": orbit["scalar_polynomial_orbit_size"],
        })

    result = {
        "schema": "marici.nima.higher_specialization_cyclic_constraint.v1",
        "sources": [str(args.orbits).replace("\\", "/"), str(args.naturality).replace("\\", "/")],
        "invariant_degeneration_divisors": ["E=0", "Lambda(P1,P2,P3)=0"],
        "C3_generator_matrix": sigma,
        "regular_character": character,
        "rational_regular_decomposition": "Q[C3] = Q_trivial direct_sum Q[zeta_3]",
        "orbits": orbit_rows,
        "aggregate_if_common_local_rank_is_r": {
            "dimension": "24*r",
            "character": ["24*r", "0", "0"],
            "trivial_multiplicity": "8*r",
            "cyclotomic_plane_multiplicity": "8*r",
        },
        "falsifier": "For each free labelled orbit, a functorial specialization of local rank r must have total rank 3r and zero trace for sigma and sigma^2. Any smaller rank on the scalar-invariant polynomial orbit means labels or charts were forgotten; any nonzero nonidentity trace requires extra fixed-point or transition data.",
        "scope": "This constrains equivariant assembly but does not determine the local ranks r_E, r_Lambda, or their intersection extension.",
        "allocator_claim": "seqclaim-899ead803eee49569b9856b7",
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"orbits": len(orbit_rows), "regular_character": character, "aggregate_character_per_local_rank": [24, 0, 0]}))


if __name__ == "__main__":
    main()
