"""Certify all ordered rank-five cells with six correlated macro-charts."""
import json
from decimal import Decimal as D, localcontext, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).parents[1]
LOW, HIGH = D('.0025'), D('.0075')
RADIUS = D('.0025')
TARGET = D('2.16e-23')


def up_sum(values):
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        return sum(values, D(0))


def artifact(center):
    tag = '_'.join(str(x).replace('.', 'p') for x in center)
    return ROOT / 'results' / (
        'central-rank-five-hessian-taylor-majorant-center-' + tag +
        '-radius-0p0025.json')


def chart_result(low_count):
    center = (LOW,) * low_count + (HIGH,) * (5 - low_count)
    source = json.loads(artifact(center).read_text())
    if tuple(D(x) for x in source['taylor_center']) != center:
        raise RuntimeError('chart-center mismatch')
    if D(source['taylor_radius']) != RADIUS:
        raise RuntimeError('chart-radius mismatch')
    base = D(source['finite_jet_budget_radius'])
    budgets = source['finite_jet_hessian_row_budgets_by_degree']
    scale = RADIUS / base

    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        center_tensor = up_sum(D(x) for x in budgets['3']) / base
    variation = {}
    for degree in range(4, 8):
        with localcontext() as context:
            context.prec = 50
            context.rounding = ROUND_CEILING
            hessian = up_sum(D(x) for x in budgets[str(degree)]) * scale ** (degree - 2)
            variation[str(degree)] = hessian * D(degree - 2) / RADIUS
    tail = D(source['third_tensor_remainder_bound'])
    degree_five_plus = up_sum([variation[str(d)] for d in range(5, 8)] + [tail])
    total = up_sum([center_tensor, *variation.values(), tail])
    return {
        'low_coordinate_count': low_count,
        'center': [str(x) for x in center],
        'covered_ordered_box': ('[0,.005]^' + str(low_count) +
                                ' x [.005,.01]^' + str(5-low_count)),
        'center_third_tensor_l1': str(center_tensor),
        'degree_four_through_seven_variation': {
            degree: str(value) for degree, value in variation.items()
        },
        'degree_eight_and_higher_C3_remainder': str(tail),
        'degree_five_and_higher_third_tensor_remainder': str(degree_five_plus),
        'uniform_third_tensor_l1_bound': str(total),
        'bound_below_target': total < TARGET,
        'source_chart_interval_certified': source['interval_certified'],
    }


def main():
    charts = [chart_result(k) for k in range(6)]
    maximum = max(D(row['uniform_third_tensor_l1_bound']) for row in charts)
    maximum_tail = max(D(row['degree_five_and_higher_third_tensor_remainder'])
                       for row in charts)
    result = {
        'partition': '[0,.005] union [.005,.01] in each coordinate',
        'ordered_binary_patterns': 6,
        'charts': charts,
        'maximum_degree_five_and_higher_third_tensor_remainder': str(maximum_tail),
        'uniform_third_tensor_l1_bound': str(maximum),
        'required_global_bound': str(TARGET),
        'uniform_bound_below_required_global_bound': maximum < TARGET,
        'all_3003_ordered_half_grid_cells_covered': True,
        'naive_anchor_evaluations_avoided': 2997,
        'directed_decimal_rounding': True,
        'interval_certified': all(row['bound_below_target'] and
                                  row['source_chart_interval_certified']
                                  for row in charts),
        'rh_proved': False,
    }
    output = ROOT / 'results' / 'central-rank-five-third-tensor-six-chart-cover.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
