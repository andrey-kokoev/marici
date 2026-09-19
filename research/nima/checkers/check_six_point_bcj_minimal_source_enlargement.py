from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research/benincasa/.tmp_sympy"))
sys.path.insert(0, str(ROOT / "research/nima/checkers"))
import sympy as sp

from check_six_point_bcj_quotient_rank import INDEX, kk_reduce
from check_six_point_nmhv_ordering_relations import sij

OUT = ROOT / "research/nima/results/six-point-bcj-minimal-source-enlargement.json"
REPAIR = ROOT / "research/nima/results/six-point-minimal-bcj-chain-repair.json"


def main() -> None:
    labels = list(itertools.permutations((2, 3, 4, 5)))
    relation_rows = []
    for p in labels:
        row = [sp.Integer(0)] * 24
        weight = sp.Integer(0)
        for k in range(1, 5):
            weight += sij(1, p[k - 1])
            order = p[:k] + (1,) + p[k:] + (6,)
            for ddm, coefficient in kk_reduce(order).items():
                row[INDEX[ddm]] += weight * coefficient
        relation_rows.append(row)
    relations = sp.Matrix(relation_rows)

    repair = json.loads(REPAIR.read_text(encoding="utf-8"))
    defects = sp.Matrix([
        [sp.Rational(repair['relation_coordinates'][j]['defect_coordinates'][i]) for j in range(24)]
        for i in range(4)
    ])

    # Each of the 24 labelled generators maps to a worldsheet relation vector
    # and a CR residue-defect coordinate.  The graph/pushout source retains both.
    graph = relations.T.col_join(defects).T  # 24 labelled rows in 24+4 coordinates
    relation_rank = relations.rank()
    graph_rank = graph.rank()
    added_rank = graph_rank - relation_rank

    # The defect information invisible to the relation vectors is measured by
    # the image of ker(relations^T) under defects.
    dependency_basis = relations.T.nullspace()
    dependency_matrix = sp.Matrix.hstack(*dependency_basis)
    invisible_defects = defects * dependency_matrix

    checks = {
        'fixed_leg_relation_rank_six': relation_rank == 6,
        'joint_relation_defect_graph_rank_ten': graph_rank == 10,
        'minimal_added_dimension_four': added_rank == 4,
        'all_four_defect_directions_occur_on_relation_dependencies': invisible_defects.rank() == 4,
        'matches_mapping_cone_defect_rank': added_rank == repair['ranks']['residue_defect_span'],
        'labels_match': labels == [tuple(row['permutation']) for row in repair['relation_coordinates']],
    }

    out = {
        'schema': 'marici.nima.six-point-bcj-minimal-source-enlargement.v1',
        'status': 'minimal_four_dimensional_preprojection_enlargement_required' if all(checks.values()) else 'failed',
        'checks': checks,
        'ranks': {
            'worldsheet_fixed_leg_relation_span': relation_rank,
            'joint_relation_defect_graph': graph_rank,
            'new_source_directions': added_rank,
            'defects_on_worldsheet_dependencies': invisible_defects.rank(),
        },
        'canonical_finite_candidate': 'the graph of the labelled map generator -> (worldsheet BCJ relation vector, CR residue-defect vector)',
        'universal_property': 'Any linear source carrying both the fixed worldsheet relation assignment and the stored CR defect assignment factors through their joint image. Its quotient over the worldsheet relation image has dimension at least four.',
        'consequence': 'Changing only the target map cannot repair the current CR assignment. A minimal linear source enlargement must retain four preprojection directions, exactly matching the mapping-cone defect rank.',
        'authority_gate': 'The joint graph is canonical relative to the two stored assignments, but the four added directions are not thereby physical or source-derived. They must be identified with independently constructed worldsheet/twisted-cohomology data before this becomes a CR-to-Koszul chain map.',
        'claim_boundary': 'Minimality is finite-fixture linear algebra for the fixed 24 labelled generators. It does not establish a global twisted cocycle or authorize the enlarged directions physically.',
    }
    OUT.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    if out['status'] == 'failed':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
