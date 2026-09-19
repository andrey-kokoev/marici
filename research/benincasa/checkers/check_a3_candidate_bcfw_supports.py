from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research/benincasa/.tmp_sympy"))
import sympy as sp

OUT = ROOT / "research/benincasa/results/a3_candidate_bcfw_supports.json"


def main() -> None:
    lift = json.loads((ROOT / "research/nima/results/n8-selected-facet-form-lift.json").read_text())['rows']
    ext = json.loads((ROOT / "research/nima/results/n8-complete-external-pushforward.json").read_text())
    physical = [f for f in ext['facets'] if f['target_rank'] == 7]
    divisors = sorted(tuple(map(int, key.split())) for key in ext['physical_bracket_multiplicities'])
    index = {divisor: i for i, divisor in enumerate(divisors)}

    rows = []
    vectors = []
    for item in lift:
        if item['history']['boundary_updates']:
            continue
        history = item['history_index']
        facets = [f for f in physical if f['history_index'] == history]
        support = sorted(tuple(f['target_brackets'][0]) for f in facets)
        vector = [0] * len(divisors)
        for bracket in support:
            vector[index[bracket]] += 1
        vectors.append(vector)
        rows.append({
            'positive_root': item['positive_root'],
            'history_index': history,
            'source_facet_count': len(facets),
            'physical_divisor_support': [list(x) for x in support],
            'support_has_no_duplicates': len(support) == len(set(support)),
        })

    matrix = sp.Matrix(vectors)
    pairwise = []
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            overlap = sorted(set(map(tuple, rows[i]['physical_divisor_support'])) & set(map(tuple, rows[j]['physical_divisor_support'])))
            pairwise.append({
                'roots': [rows[i]['positive_root'], rows[j]['positive_root']],
                'overlap': [list(x) for x in overlap],
                'overlap_size': len(overlap),
            })

    union = set()
    for row in rows:
        union.update(map(tuple, row['physical_divisor_support']))
    checks = {
        'exactly_three_uncorrected_histories': len(rows) == 3,
        'each_history_support_is_intrinsically_defined': all(row['support_has_no_duplicates'] for row in rows),
        'candidate_support_vectors_are_independent': matrix.rank() == 3,
        'all_twenty_divisors_indexed': len(divisors) == 20,
        'candidate_union_is_proper': 0 < len(union) < 20,
    }

    result = {
        'schema': 'marici.benincasa.a3-candidate-bcfw-supports.v1',
        'status': 'three_composite_facet_supports_canonical_normalization_still_open' if all(checks.values()) else 'failed',
        'checks': checks,
        'candidate_supports': rows,
        'pairwise_overlaps': pairwise,
        'support_matrix_rank': matrix.rank(),
        'union_divisor_count': len(union),
        'conclusion': 'For the three uncorrected composite-root histories, the completed BCFW atlas canonically fixes three independent 20-divisor support vectors. Therefore their combinatorial pushforward support need not be guessed. The remaining comparison is form-level coefficient and normalization equality to the three A3 K0 densities.',
        'claim_boundary': 'Support incidence does not supply canonical-form coefficients, signs, or normalization and does not repair the three transported simple roots or three B_ii differences.',
    }
    OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    if result['status'] == 'failed':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
