"""Derive the exact sufficient rank-six continuum transport target."""
import json
from decimal import Decimal as D, localcontext, ROUND_CEILING, ROUND_FLOOR
from pathlib import Path

ROOT = Path(__file__).parents[1]
HALF_GRID_L1_RADIUS = D('.003')
BINARY_CHART_L1_RADIUS = D('.015')


def main():
    derivatives = json.loads((ROOT / 'results' /
        'central-rank-six-derivative-interval-grid.json').read_text())
    centers = json.loads((ROOT / 'results' /
        'central-rank-six-hessian-binary-centers.json').read_text())
    margin = D(derivatives['closest_upper_endpoint_to_zero']['value']).copy_negate()
    center_hessian = max(D(value) for row in centers['centers']
                         for value in row['hessian_absolute_row_sums'])
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_FLOOR
        allowed_hessian = margin / HALF_GRID_L1_RADIUS
        remaining_hessian = allowed_hessian - center_hessian
        required_tensor = remaining_hessian / BINARY_CHART_L1_RADIUS
    result = {
        'smallest_anchor_derivative_margin': str(margin),
        'half_grid_cell_l1_radius': str(HALF_GRID_L1_RADIUS),
        'allowed_uniform_hessian_row_sum': str(allowed_hessian),
        'maximum_binary_center_hessian_row_sum': str(center_hessian),
        'remaining_hessian_allowance': str(remaining_hessian),
        'binary_chart_l1_radius': str(BINARY_CHART_L1_RADIUS),
        'sufficient_uniform_third_tensor_l1_ceiling': str(required_tensor),
        'ordered_binary_chart_count': 7,
        'directed_decimal_rounding': True,
        'interval_inputs_certified': True,
        'rh_proved': False,
    }
    output = ROOT / 'results' / 'central-rank-six-continuum-target.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
