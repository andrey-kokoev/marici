"""Audit the finite-cover geometry and dual norms in rank-six transport."""
import json
import math
from decimal import Decimal as D, Context, ROUND_FLOOR
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).parents[1]
RANK = 6
GRID_SUBDIVISIONS = 10
GRID_STEP = Q(1, 1000)
HALF_GRID_LINF_RADIUS = GRID_STEP / 2
BINARY_CHART_LINF_RADIUS = Q(1, 400)
DISPLAY = Context(prec=90, rounding=ROUND_FLOOR)


def rational(text):
    return Q(D(text))


def decimal_text(value):
    return str(DISPLAY.divide(D(value.numerator), D(value.denominator)))


derivatives = json.loads((ROOT / 'results' /
    'central-rank-six-derivative-interval-grid.json').read_text())
centers = json.loads((ROOT / 'results' /
    'central-rank-six-hessian-binary-centers.json').read_text())
target = json.loads((ROOT / 'results' /
    'central-rank-six-continuum-target.json').read_text())
pivots = json.loads((ROOT / 'results' /
    'central-rank-six-loewner-grid.json').read_text())
source_tail = json.loads((ROOT / 'results' /
    'central-rank-six-source-remainder-binomial-identity.json').read_text())

expected_anchors = math.comb((GRID_SUBDIVISIONS + 1) + RANK - 1, RANK)
assert expected_anchors == 8008
assert derivatives['anchor_count'] == expected_anchors
assert derivatives['coordinate_derivative_count'] == expected_anchors * RANK
assert derivatives['all_anchor_derivatives_strictly_negative']
assert derivatives['interval_certified']
assert derivatives.get('directed_scalar_arithmetic_version') == 2
assert centers['ordered_binary_pattern_count'] == RANK + 1
assert len(centers['centers']) == RANK + 1
assert centers['directed_interval_centers_certified']
assert centers.get('directed_scalar_arithmetic_version') == 2
assert all(row.get('directed_scalar_arithmetic_version') == 2
           for row in centers['centers'])
assert pivots.get('directed_scalar_arithmetic_version') == 2
assert pivots['nondecreasing_anchor_count'] == expected_anchors
assert pivots['all_rank_six_Newton_LDL_pivots_strictly_positive']
assert pivots['interval_certified']
assert source_tail['all_factorial_binomial_identities_hold']
assert source_tail['source_degree_tail_ratio_below_one']
assert source_tail['anchor_tail_ratio_within_allowance']
assert source_tail['interval_certified']

margin = -rational(derivatives['closest_upper_endpoint_to_zero']['value'])
center_hessian = max(rational(value) for row in centers['centers']
                     for value in row['hessian_absolute_row_sums'])
stored_ceiling = rational(target['sufficient_uniform_third_tensor_l1_ceiling'])
exact_ceiling = (margin / HALF_GRID_LINF_RADIUS - center_hessian) / BINARY_CHART_LINF_RADIUS
assert stored_ceiling <= exact_ceiling
assert D(target['half_grid_cell_linf_radius']) == D('.0005')
assert D(target['binary_chart_linf_radius']) == D('.0025')

result = {
    'rank': RANK,
    'grid_value_count': GRID_SUBDIVISIONS + 1,
    'ordered_anchor_count_formula': 'binomial(11+6-1,6)',
    'ordered_anchor_count': expected_anchors,
    'coordinate_derivative_count': expected_anchors * RANK,
    'all_six_pivots_positive_at_every_anchor': True,
    'source_tail_identity_certificate': (
        'central-rank-six-source-remainder-binomial-identity.json'),
    'nearest_anchor_lemma': (
        'coordinatewise nearest-grid quantization is monotone, preserves '
        'coordinate order, and has linf error at most half a grid step'),
    'half_grid_linf_radius': decimal_text(HALF_GRID_LINF_RADIUS),
    'ordered_binary_pattern_count': RANK + 1,
    'binary_pattern_lemma': (
        'thresholding an ordered tuple at .005 produces a low prefix and a '
        'high suffix; the seven prefix lengths exhaust the ordered simplex'),
    'binary_chart_linf_radius': decimal_text(BINARY_CHART_LINF_RADIUS),
    'dual_norm_lemma': (
        'sum_k |a_k dx_k| <= (sum_k |a_k|) ||dx||_infinity, applied '
        'first to each Hessian row and then to each third-tensor slice'),
    'smallest_anchor_derivative_margin': decimal_text(margin),
    'maximum_center_hessian_row_sum': decimal_text(center_hessian),
    'exact_sufficient_third_tensor_ceiling': decimal_text(exact_ceiling),
    'stored_downward_rounded_ceiling': target['sufficient_uniform_third_tensor_l1_ceiling'],
    'stored_ceiling_no_greater_than_exact': True,
    'strict_transport_rule': (
        'any uniform third-tensor slice-l1 bound strictly below the stored '
        'ceiling preserves all six negative coordinate derivatives'),
    'all_8008_ordered_half_grid_cells_covered': True,
    'all_seven_ordered_binary_macro_charts_cover_simplex': True,
    'interval_inputs_certified': True,
    'rh_proved': False,
}


if __name__ == '__main__':
    output = ROOT / 'results' / 'central-rank-six-continuum-transport-geometry.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
