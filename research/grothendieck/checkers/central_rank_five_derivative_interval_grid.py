"""Audit directed fifth-pivot derivatives at all central grid anchors."""
import json
from concurrent.futures import ProcessPoolExecutor
from decimal import Decimal as D
from itertools import combinations_with_replacement
from pathlib import Path


GRID = [D(i) / D(1000) for i in range(11)]
ANCHORS = list(combinations_with_replacement(GRID, 5))


def audit_chunk(chunk):
    import central_rank_five_derivative_interval_anchor as A
    audited = []
    for nodes in chunk:
        result = A.evaluate(nodes)
        intervals = result['fifth_pivot_coordinate_derivative_intervals']
        audited.append({
            'anchor': result['anchor'],
            'fifth_pivot_interval': result['fifth_pivot_interval'],
            'derivatives': intervals,
            'certified': result['interval_certified'],
        })
    return audited


def main():
    chunks = [ANCHORS[i::3] for i in range(3)]
    with ProcessPoolExecutor(max_workers=3) as pool:
        rows = [row for chunk in pool.map(audit_chunk, chunks) for row in chunk]
    rows.sort(key=lambda row: tuple(D(x) for x in row['anchor']))
    failures = [row for row in rows if not row['certified']]
    upper_extremum = max(
        (D(interval[1]), row['anchor'], variable, interval)
        for row in rows for variable, interval in enumerate(row['derivatives']))
    lower_extremum = min(
        (D(interval[0]), row['anchor'], variable, interval)
        for row in rows for variable, interval in enumerate(row['derivatives']))
    result = {
        'grid': [str(x) for x in GRID],
        'anchor_count': len(rows),
        'coordinate_derivative_count': 5 * len(rows),
        'uncertified_anchor_count': len(failures),
        'all_anchor_derivatives_strictly_negative': not failures,
        'closest_upper_endpoint_to_zero': {
            'value': str(upper_extremum[0]), 'anchor': upper_extremum[1],
            'variable': upper_extremum[2], 'interval': upper_extremum[3]},
        'most_negative_lower_endpoint': {
            'value': str(lower_extremum[0]), 'anchor': lower_extremum[1],
            'variable': lower_extremum[2], 'interval': lower_extremum[3]},
        'analytic_tail_bounds_included': True,
        'directed_decimal_rounding': True,
        'interval_certified': not failures,
        'rh_proved': False,
        'anchors': rows,
    }
    output = (Path(__file__).parents[1] / 'results' /
              'central-rank-five-derivative-interval-grid.json')
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in result.items()
                      if key != 'anchors'}, indent=2))


if __name__ == '__main__':
    main()
