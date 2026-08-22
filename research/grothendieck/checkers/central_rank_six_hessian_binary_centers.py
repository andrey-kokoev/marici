"""Directed sixth-pivot Hessians at the seven ordered binary macro-centers."""
import json
from pathlib import Path

import central_rank_five_hessian_interval_anchor as H

if H.N != 6:
    raise RuntimeError("run with MARICI_RANK=6")

ROOT = Path(__file__).parents[1]
LOW, HIGH = '.0025', '.0075'


def main():
    rows = []
    for low_count in range(7):
        center = [LOW] * low_count + [HIGH] * (6-low_count)
        row = H.evaluate(center)
        row['low_coordinate_count'] = low_count
        rows.append(row)
    maximum = max(max(float(x) for x in row['hessian_absolute_row_sums'])
                  for row in rows)
    result = {
        'ordered_binary_pattern_count': len(rows),
        'centers': rows,
        'maximum_hessian_row_sum_float_reconnaissance': repr(maximum),
        'analytic_source_tail_included': True,
        'directed_interval_centers_certified': True,
        'rh_proved': False,
    }
    output = ROOT / 'results' / 'central-rank-six-hessian-binary-centers.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({
        'ordered_binary_pattern_count': len(rows),
        'maximum_hessian_row_sum_float_reconnaissance': repr(maximum),
        'center_row_sums': [row['hessian_absolute_row_sums'] for row in rows],
        'rh_proved': False}, indent=2))


if __name__ == '__main__':
    main()
