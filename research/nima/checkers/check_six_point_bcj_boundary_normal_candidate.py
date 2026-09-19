from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research/benincasa/.tmp_sympy"))
import sympy as sp

OUT = ROOT / "research/nima/results/six-point-bcj-boundary-normal-candidate.json"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    enlargement = load("research/nima/results/six-point-bcj-minimal-source-enlargement.json")
    boundary = load("research/nima/results/six-point-bcj-worldsheet-boundary-residues.json")
    naturality = load("research/nima/results/mbar06-scattering-equation-boundary-naturality.json")

    s12, s13, s14, s15 = sp.symbols('s12 s13 s14 s15')
    coefficient_vector = sp.Matrix([s12, s13, s14, s15, -(s12 + s13 + s14 + s15)])
    coefficient_matrix = coefficient_vector.jacobian([s12, s13, s14, s15])
    left_relation = sp.Matrix([[1, 1, 1, 1, 1]])

    checks = {
        'minimal_cr_enlargement_is_four': enlargement['ranks']['new_source_directions'] == 4,
        'five_pair_collision_residues_constructed': len(boundary['boundaries']) == 5,
        'all_collision_residues_factorize': boundary['checks']['all_five_collision_residues_factorize'],
        'collision_coefficient_module_rank_four': coefficient_matrix.rank() == 4,
        'unique_momentum_conservation_relation': left_relation * coefficient_matrix == sp.zeros(1, 4),
        'all_stable_divisor_scattering_equations_factorize': naturality['checks']['all_25_stable_divisors'] and naturality['checks']['cluster_equations_factorize'],
    }

    out = {
        'schema': 'marici.nima.six-point-bcj-boundary-normal-candidate.v1',
        'status': 'rank_matched_boundary_normal_candidate_identification_open' if all(checks.values()) else 'failed',
        'checks': checks,
        'cr_requirement': {
            'new_directions': enlargement['ranks']['new_source_directions'],
            'role': 'preprojection directions carrying residue defects invisible to the fixed-leg ordering relation span',
        },
        'worldsheet_candidate': {
            'generators': ['z1=z2', 'z1=z3', 'z1=z4', 'z1=z5', 'z1=z6'],
            'coefficients': ['s12', 's13', 's14', 's15', '-(s12+s13+s14+s15)'],
            'rank_mod_momentum_conservation': coefficient_matrix.rank(),
            'source_provenance': 'logarithmic pair-collision normals of the fundamental BCJ worldsheet identity',
        },
        'why_promising': 'The independently sourced collision-normal coefficient module has exactly the four dimensions required by the minimal CR enlargement, and scattering-equation factorization is stable on all 25 boundary divisors.',
        'missing_identification': 'Construct a label-natural 4x4 map from the CR invisible-defect quotient to the collision-normal Mandelstam module and verify that every one of the 24 labelled CR defects is the residue image of its corresponding worldsheet relation. Rank agreement alone does not choose this map.',
        'first_falsifier': 'Any linear dependency among labelled collision-normal residue vectors whose corresponding CR defect combination is nonzero rules out the candidate, just as in the earlier un-enlarged factorization test.',
        'claim_boundary': 'This identifies a source-derived rank-matched candidate for the four required directions; it does not establish the comparison map or twisted-cohomology chain compatibility.',
    }
    OUT.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    if out['status'] == 'failed':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
