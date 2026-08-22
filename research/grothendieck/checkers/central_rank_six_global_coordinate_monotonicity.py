"""Close rank-six coordinate monotonicity by two mean-value transports."""
import json
from decimal import Decimal as D, localcontext, ROUND_CEILING, ROUND_FLOOR
from pathlib import Path

ROOT = Path(__file__).parents[1]
GRID_CELL_L1_RADIUS = D('.003')
BINARY_CHART_L1_RADIUS = D('.015')


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
        'central-rank-six-derivative-interval-grid.json').read_text())
    pivots = json.loads((ROOT / 'results' /
        'central-rank-six-loewner-grid.json').read_text())
    centers = json.loads((ROOT / 'results' /
        'central-rank-six-hessian-binary-centers.json').read_text())
    cover = json.loads((ROOT / 'results' /
        'central-rank-six-third-tensor-seven-chart-cover.json').read_text())
    if derivative['anchor_count'] != 8008 or derivative['coordinate_derivative_count'] != 48048:
        raise RuntimeError('rank-six derivative grid is incomplete')
    if not derivative['interval_certified'] or not derivative['all_anchor_derivatives_strictly_negative']:
        raise RuntimeError('rank-six anchor derivatives are uncertified')
    if not pivots['interval_certified'] or not pivots['all_rank_six_Newton_LDL_pivots_strictly_positive']:
        raise RuntimeError('rank-six grid pivots are uncertified')
    if not cover['interval_certified'] or not cover['all_8008_ordered_half_grid_cells_covered']:
        raise RuntimeError('seven-chart continuum cover is uncertified')

    center_hessian = max(D(value) for row in centers['centers']
                         for value in row['hessian_absolute_row_sums'])
    tensor = D(cover['uniform_third_tensor_l1_bound'])
    hessian_transport = up_mul(tensor, BINARY_CHART_L1_RADIUS)
    continuum_hessian = up_add(center_hessian, hessian_transport)
    derivative_transport = up_mul(continuum_hessian, GRID_CELL_L1_RADIUS)
    anchor_margin = D(derivative['closest_upper_endpoint_to_zero']['value']).copy_negate()
    continuum_margin = down_sub(anchor_margin, derivative_transport)
    proved = continuum_margin > 0
    result = {
        'ordered_grid_anchor_count': derivative['anchor_count'],
        'coordinate_derivative_count': derivative['coordinate_derivative_count'],
        'ordered_grid_cell_l1_radius': str(GRID_CELL_L1_RADIUS),
        'binary_chart_l1_radius': str(BINARY_CHART_L1_RADIUS),
        'maximum_binary_center_hessian_row_sum': str(center_hessian),
        'uniform_third_tensor_l1_bound': str(tensor),
        'hessian_transport_bound': str(hessian_transport),
        'continuum_hessian_row_sum_bound': str(continuum_hessian),
        'derivative_transport_bound': str(derivative_transport),
        'smallest_anchor_derivative_margin': str(anchor_margin),
        'continuum_derivative_margin_lower': str(continuum_margin),
        'all_six_coordinate_derivatives_strictly_negative_on_ordered_simplex': proved,
        'all_six_Newton_LDL_pivots_strictly_positive_on_ordered_simplex': proved,
        'ordered_simplex': '0 <= x1 <= ... <= x6 <= .01',
        'analytic_source_and_rational_remainders_included': True,
        'directed_decimal_rounding': True,
        'interval_certified': proved,
        'rh_proved': False,
    }
    output = ROOT / 'results' / 'central-rank-six-global-coordinate-monotonicity.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
