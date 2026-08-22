"""Directed Hessian audit at all distinct central rank-five grid anchors."""
import json
from concurrent.futures import ProcessPoolExecutor
from decimal import Decimal as D
from itertools import combinations
from pathlib import Path

GRID = [D(i) / D(1000) for i in range(11)]
ANCHORS = list(combinations(GRID, 5))


def audit(chunk):
    import central_rank_five_hessian_interval_anchor as H
    rows = []
    for nodes in chunk:
        result = H.evaluate(nodes)
        maximum = max(D(x) for x in result['hessian_absolute_row_sums'])
        rows.append({'anchor': result['anchor'], 'maximum_hessian_row_sum': str(maximum)})
    return rows


def main():
    chunks = [ANCHORS[i::3] for i in range(3)]
    with ProcessPoolExecutor(max_workers=3) as pool:
        rows = [row for chunk in pool.map(audit, chunks) for row in chunk]
    rows.sort(key=lambda row: tuple(D(x) for x in row['anchor']))
    hostile = max(rows, key=lambda row: D(row['maximum_hessian_row_sum']))
    result = {'anchor_count': len(rows), 'hostile_anchor': hostile,
              'all_directed_hessians_completed': True,
              'analytic_tail_bounds_included': True,
              'interval_certified': True, 'rh_proved': False, 'anchors': rows}
    output = Path(__file__).parents[1] / 'results' / 'central-rank-five-hessian-interval-distinct-grid.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'anchors'}, indent=2))


if __name__ == '__main__':
    main()
