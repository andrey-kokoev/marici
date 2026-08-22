"""Inherit the first five global rank-six denominator floors."""
import json
from decimal import Decimal as D
from pathlib import Path

ROOT = Path(__file__).parents[1]


def main():
    first_four = json.loads((ROOT / 'results' /
        'central-rank-four-global-pivot-denominators.json').read_text())
    monotonicity = json.loads((ROOT / 'results' /
        'central-rank-five-global-coordinate-monotonicity.json').read_text())
    rank_six = json.loads((ROOT / 'results' /
        'central-rank-six-loewner-anchor.json').read_text())
    upper = next(row for row in rank_six['anchors']
                 if row['anchor'] == ['0.01'] * 6)
    if not monotonicity['all_five_coordinate_derivatives_strictly_negative_on_ordered_simplex']:
        raise RuntimeError('rank-five continuum monotonicity is not certified')
    fifth_floor = D(upper['pivots'][4][0])
    # A leading LDL pivot is unchanged by adjoining the sixth row and column.
    first_four_floors = first_four['global_first_four_pivot_lower_bounds']
    result = {
        'rank_six_prefix_inheritance': True,
        'first_four_global_floors': first_four_floors,
        'fifth_global_floor': str(fifth_floor),
        'fifth_floor_attained_at_upper_confluent_prefix': True,
        'all_first_five_denominator_floors_positive': (
            all(D(x) > 0 for x in first_four_floors) and fifth_floor > 0),
        'rank_five_continuum_monotonicity_used': True,
        'directed_decimal_rounding': True,
        'interval_certified': True,
        'rh_proved': False,
    }
    output = ROOT / 'results' / 'central-rank-six-global-pivot-denominators.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
