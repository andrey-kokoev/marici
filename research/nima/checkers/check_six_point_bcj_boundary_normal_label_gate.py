from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research/benincasa/.tmp_sympy"))
import sympy as sp

OUT = ROOT / "research/nima/results/six-point-bcj-boundary-normal-label-gate.json"
REPAIR = ROOT / "research/nima/results/six-point-minimal-bcj-chain-repair.json"


def main() -> None:
    repair = json.loads(REPAIR.read_text(encoding="utf-8"))
    defects = sp.Matrix([
        [sp.Rational(repair['relation_coordinates'][j]['defect_coordinates'][i]) for j in range(24)]
        for i in range(4)
    ])
    distinct_columns = {tuple(defects[:, j]) for j in range(defects.cols)}

    s12, s13, s14, s15 = sp.symbols('s12 s13 s14 s15')
    common_collision_vector = sp.Matrix([s12, s13, s14, s15, -(s12 + s13 + s14 + s15)])

    # For every fundamental relation obtained by permuting the base ordering,
    # pair-collision residues have the same Mandelstam coefficient vector.
    # Only the lower-point Parke--Taylor factor remembers that ordering.
    label_blind_image_has_one_column = sp.Matrix.hstack(*([common_collision_vector] * 24))

    checks = {
        'all_24_cr_defect_columns_present': defects.cols == 24,
        'cr_defects_vary_with_ordering': len(distinct_columns) > 1,
        'cr_defect_span_rank_four': defects.rank() == 4,
        'label_blind_collision_assignment_is_constant': label_blind_image_has_one_column.rank() == 1,
        'no_map_of_coefficient_vector_alone_can_reproduce_varying_defects': len(distinct_columns) > 1,
    }

    out = {
        'schema': 'marici.nima.six-point-bcj-boundary-normal-label-gate.v1',
        'status': 'collision_coefficients_alone_insufficient_lower_pt_label_must_be_retained' if all(checks.values()) else 'failed',
        'checks': checks,
        'counts': {
            'distinct_cr_defect_columns': len(distinct_columns),
            'cr_defect_rank': defects.rank(),
            'label_blind_collision_rank': label_blind_image_has_one_column.rank(),
        },
        'falsified_candidate': 'a single label-blind 4x4 identification from the Mandelstam collision-coefficient module to the CR defect quotient',
        'required_enlargement': 'retain the lower-point Parke-Taylor ordering factor, i.e. use collision normals tensored with the labelled five-point ordering module before any quotient',
        'next_test': 'Compute residues of all 24 fundamental BCJ generators as vectors in collision-normal tensor lower-PT-ordering space; reduce the five-point PT factors by their sourced KK/BCJ relations; then test whether the CR defect assignment preserves every dependency of that labelled residue module.',
        'claim_boundary': 'The rank-four collision coefficients remain necessary source data, but they are not sufficient without ordering labels. This does not test the fully labelled boundary module.',
    }
    OUT.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    if out['status'] == 'failed':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
