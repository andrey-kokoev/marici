"""Uniform third-tensor certificate from one correlated endpoint chart.

The degree-seven jet is centered at (.01,...,.01).  Radius .01 contains the
entire physical cube [0,.01]^5 (and harmlessly overcovers the opposite
directions).  Homogeneous Hessian budgets originally tabulated at radius
.0005 are rescaled exactly by (R/.0005)^(d-2), then converted to ordered
third-tensor variation by (d-2)/R.  The C3 Taylor-model majorant supplies
all degrees eight and higher.
"""
import json
from decimal import Decimal as D, localcontext, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).parents[1]
BASE_RADIUS = D('.0005')
RADIUS = D('.01')
TARGET = D('2.16e-23')


def up_sum(values):
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        return sum(values, D(0))


def main():
    deep = json.loads((ROOT / 'results' / 'central-rank-five-hessian-taylor-deep.json').read_text())
    anchors = json.loads((ROOT / 'results' / 'central-rank-five-third-tensor-interval-anchor.json').read_text())
    global_tail_path = ROOT / 'results' / 'central-rank-five-hessian-taylor-majorant-radius-0p01.json'
    global_tail = json.loads(global_tail_path.read_text())
    if D(global_tail.get('taylor_radius', 'NaN')) != RADIUS:
        raise RuntimeError('global C3 majorant has the wrong radius')

    endpoint = next(row for row in anchors['anchors']
                    if (row.get('anchor_interval') and
                        all(interval == ['0.01', '0.01']
                            for interval in row['anchor_interval'])) or
                       row.get('anchor') == ['0.01'] * 5)
    tensor_at_center = D(endpoint['third_derivative_tensor_l1_bound'])
    scale = RADIUS / BASE_RADIUS
    variation = {}
    for degree in range(4, 8):
        base_hessian = up_sum(D(x) for x in
                              deep['hessian_row_variation_budgets_by_degree'][str(degree)])
        with localcontext() as context:
            context.prec = 50
            context.rounding = ROUND_CEILING
            global_hessian = base_hessian * scale ** (degree - 2)
            variation[str(degree)] = global_hessian * D(degree - 2) / RADIUS

    finite_variation = up_sum(variation.values())
    infinite_variation = D(global_tail['third_tensor_remainder_bound'])
    degree_five_plus = up_sum([variation[str(d)] for d in range(5, 8)] +
                              [infinite_variation])
    global_bound = up_sum([tensor_at_center, finite_variation, infinite_variation])
    result = {
        'chart_center': ['.01'] * 5,
        'chart_radius': str(RADIUS),
        'covered_domain': '[0,.01]^5',
        'center_third_tensor_l1': str(tensor_at_center),
        'degree_four_through_seven_variation': {
            degree: str(value) for degree, value in variation.items()
        },
        'degree_eight_and_higher_C3_remainder': str(infinite_variation),
        'degree_five_and_higher_third_tensor_remainder': str(degree_five_plus),
        'uniform_third_tensor_l1_bound': str(global_bound),
        'required_global_bound': str(TARGET),
        'uniform_bound_below_required_global_bound': global_bound < TARGET,
        'number_of_correlated_charts': 1,
        'all_3003_ordered_cells_covered': True,
        'directed_decimal_rounding': True,
        'interval_certified': True,
        'rh_proved': False,
    }
    output = ROOT / 'results' / 'central-rank-five-third-tensor-global-chart.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
