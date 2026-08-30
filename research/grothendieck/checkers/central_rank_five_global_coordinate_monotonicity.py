"""Close rank-five coordinate monotonicity by two mean-value transports."""
import json
from decimal import Decimal as D, localcontext, ROUND_CEILING, ROUND_FLOOR
from pathlib import Path

ROOT = Path(__file__).parents[1]
CELL_L1_RADIUS = D('.0025')


def up_add(a, b):
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        return a + b


def up_mul(a, b):
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        return a * b


def down_sub(a, b):
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_FLOOR
        return a - b


def main():
    derivative = json.loads((ROOT / 'results' /
        'central-rank-five-derivative-interval-grid.json').read_text())
    cover = json.loads((ROOT / 'results' /
        'central-rank-five-third-tensor-six-chart-cover.json').read_text())
    hessian_files = [
        'central-rank-five-hessian-interval-distinct-grid.json',
        'central-rank-five-hessian-interval-two-value-grid.json',
        'central-rank-five-hessian-interval-three-value-grid.json',
        'central-rank-five-hessian-interval-four-value-grid.json',
    ]
    hessians = [json.loads((ROOT / 'results' / name).read_text())
                for name in hessian_files]
    anchor_count = sum(row['anchor_count'] for row in hessians)
    if anchor_count != derivative['anchor_count'] or anchor_count != 3003:
        raise RuntimeError('anchor strata do not form the complete grid')
    if not all(row['all_directed_hessians_completed'] and row['interval_certified']
               for row in hessians):
        raise RuntimeError('an anchor Hessian stratum is uncertified')
    if not cover['interval_certified'] or not cover['all_3003_ordered_half_grid_cells_covered']:
        raise RuntimeError('six-chart continuum cover is uncertified')

    anchor_hessian = max(D(row['hostile_anchor']['maximum_hessian_row_sum'])
                         for row in hessians)
    tensor = D(cover['uniform_third_tensor_l1_bound'])
    hessian_transport = up_mul(tensor, CELL_L1_RADIUS)
    continuum_hessian = up_add(anchor_hessian, hessian_transport)
    derivative_transport = up_mul(continuum_hessian, CELL_L1_RADIUS)
    anchor_margin = -D(derivative['closest_upper_endpoint_to_zero']['value'])
    continuum_margin = down_sub(anchor_margin, derivative_transport)
    proved = continuum_margin > 0
    result = {
        'ordered_grid_anchor_count': anchor_count,
        'coordinate_derivative_count': derivative['coordinate_derivative_count'],
        'ordered_half_cell_l1_radius': str(CELL_L1_RADIUS),
        'anchor_hessian_row_sum_maximum': str(anchor_hessian),
        'uniform_third_tensor_l1_bound': str(tensor),
        'hessian_transport_bound': str(hessian_transport),
        'continuum_hessian_row_sum_bound': str(continuum_hessian),
        'derivative_transport_bound': str(derivative_transport),
        'smallest_anchor_derivative_margin': str(anchor_margin),
        'continuum_derivative_margin_lower': str(continuum_margin),
        'all_five_coordinate_derivatives_strictly_negative_on_ordered_simplex': proved,
        'ordered_simplex': '0 <= x1 <= ... <= x5 <= .01',
        'analytic_source_and_rational_remainders_included': True,
        'directed_decimal_rounding': True,
        'interval_certified': proved,
        'rh_proved': False,
    }
    output = ROOT / 'results' / 'central-rank-five-global-coordinate-monotonicity.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
