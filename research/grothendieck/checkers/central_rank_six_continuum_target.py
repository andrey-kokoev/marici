"""Derive the exact sufficient rank-six continuum transport target."""
import json
from decimal import Decimal as D, localcontext, ROUND_CEILING, ROUND_FLOOR
from pathlib import Path

ROOT = Path(__file__).parents[1]
HALF_GRID_LINF_RADIUS = D('.0005')
BINARY_CHART_LINF_RADIUS = D('.0025')


def main():
    derivatives = json.loads((ROOT / 'results' /
        'central-rank-six-derivative-interval-grid.json').read_text())
    centers = json.loads((ROOT / 'results' /
        'central-rank-six-hessian-binary-centers.json').read_text())
    if (derivatives.get('directed_scalar_arithmetic_version') != 2 or
            not derivatives.get('interval_certified', False) or
            not derivatives.get('all_anchor_derivatives_strictly_negative', False)):
        raise RuntimeError('version-2 derivative-grid certificate is absent or stale')
    if (centers.get('directed_scalar_arithmetic_version') != 2 or
            not centers.get('directed_interval_centers_certified', False) or
            not all(row.get('directed_scalar_arithmetic_version') == 2
                    for row in centers['centers'])):
        raise RuntimeError('version-2 center-Hessian certificate is absent or stale')
    margin = D(derivatives['closest_upper_endpoint_to_zero']['value']).copy_negate()
    center_hessian = max(D(value) for row in centers['centers']
                         for value in row['hessian_absolute_row_sums'])
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_FLOOR
        allowed_hessian = margin / HALF_GRID_LINF_RADIUS
        remaining_hessian = allowed_hessian - center_hessian
        required_tensor = remaining_hessian / BINARY_CHART_LINF_RADIUS
    result = {
        'smallest_anchor_derivative_margin': str(margin),
        'half_grid_cell_linf_radius': str(HALF_GRID_LINF_RADIUS),
        'allowed_uniform_hessian_row_sum': str(allowed_hessian),
        'maximum_binary_center_hessian_row_sum': str(center_hessian),
        'remaining_hessian_allowance': str(remaining_hessian),
        'binary_chart_linf_radius': str(BINARY_CHART_LINF_RADIUS),
        'transport_norm_pairing': (
            'absolute Hessian row-sum and third-tensor slice-l1 norms pair '
            'with coordinate linf displacement'),
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
