from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research/benincasa/.tmp_sympy"))
import sympy as sp

OUT = ROOT / "research/nima/results/six-point-bcj-all-labelled-boundary-residues.json"
REPAIR = ROOT / "research/nima/results/six-point-minimal-bcj-chain-repair.json"


def oriented_cyclic_class(word: tuple[int, ...]) -> tuple[tuple[int, ...], int]:
    rotations = [word[i:] + word[:i] for i in range(len(word))]
    reverse = tuple(reversed(word))
    reversed_rotations = [reverse[i:] + reverse[:i] for i in range(len(word))]
    direct_min = min(rotations)
    reversed_min = min(reversed_rotations)
    # PT reversal has sign (-1)^n, hence -1 at five points.
    return (direct_min, 1) if direct_min < reversed_min else (reversed_min, -1)


def main() -> None:
    labels = list(itertools.permutations((2, 3, 4, 5)))
    classes = sorted({oriented_cyclic_class(p + (6,))[0] for p in labels})
    class_index = {word: i for i, word in enumerate(classes)}
    collision_coefficients = [sp.Integer(2), sp.Integer(3), sp.Integer(5), sp.Integer(7), sp.Integer(-17)]

    # Rows are the residues of the 24 generators. Columns retain both the five
    # collision normals and the oriented cyclic five-point PT class.
    residue = sp.zeros(24, 5 * len(classes))
    assignments = []
    for row, p in enumerate(labels):
        cls, sign = oriented_cyclic_class(p + (6,))
        q = class_index[cls]
        for collision, coefficient in enumerate(collision_coefficients):
            residue[row, collision * len(classes) + q] = sign * coefficient
        assignments.append({'permutation': list(p), 'lower_pt_class': list(cls), 'orientation_sign': sign})

    repair = json.loads(REPAIR.read_text(encoding='utf-8'))
    defects = sp.Matrix([
        [sp.Rational(repair['relation_coordinates'][j]['defect_coordinates'][i]) for j in range(24)]
        for i in range(4)
    ])
    dependencies = residue.T.nullspace()
    dependency_matrix = sp.Matrix.hstack(*dependencies)
    defect_on_dependencies = defects * dependency_matrix

    checks = {
        'twenty_four_generators': residue.rows == 24,
        'twelve_oriented_cyclic_five_point_classes': len(classes) == 12,
        'labelled_residue_rank_twelve': residue.rank() == 12,
        'twelve_residue_dependencies': len(dependencies) == 12,
        'cr_defects_violate_labelled_residue_dependencies': defect_on_dependencies.rank() > 0,
        'generic_collision_coefficients_obey_momentum_conservation': sum(collision_coefficients) == 0,
    }

    witness = next(v for v in dependencies if defects * v != sp.zeros(4, 1))
    support = [i for i, x in enumerate(witness) if x != 0]
    out = {
        'schema': 'marici.nima.six-point-bcj-all-labelled-boundary-residues.v1',
        'status': 'cyclically_labelled_pair_collision_module_still_does_not_factor_cr_defects' if all(checks.values()) else 'failed',
        'checks': checks,
        'dimensions': {
            'collision_normals': 5,
            'independent_mandelstam_coefficients': 4,
            'oriented_cyclic_lower_pt_classes': len(classes),
            'labelled_residue_rank': residue.rank(),
            'cr_defect_rank_on_residue_dependencies': defect_on_dependencies.rank(),
        },
        'assignments': assignments,
        'dependency_witness': {
            'relation_indices': support,
            'coefficients': [str(witness[i]) for i in support],
            'permutations': [list(labels[i]) for i in support],
            'labelled_boundary_residue_zero': residue.T * witness == sp.zeros(residue.cols, 1),
            'cr_defect_combination': [str(x) for x in defects * witness],
        },
        'conclusion': 'Retaining collision normals and oriented cyclic lower-point Parke-Taylor labels is still insufficient for the fixed CR defect assignment: a dependency of the full labelled residue vectors is violated by the CR defects.',
        'next_required_structure': 'Retain finer ordering/orientation data than cyclic-reversal PT forms, or change the CR assignment. Before proposing a quotient, require its dependency kernel to be contained in the kernel of the CR defect map.',
        'claim_boundary': 'The test uses exact generic Mandelstam values satisfying momentum conservation and the sourced pair-collision factorization. It does not include all stable divisors, twisted local-system coefficients, or a compactification orientation line.',
    }
    OUT.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    if out['status'] == 'failed':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
