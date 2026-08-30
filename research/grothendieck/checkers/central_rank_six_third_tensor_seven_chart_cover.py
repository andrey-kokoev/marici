"""Certify the ordered rank-six simplex with seven correlated binary charts."""
import json
from decimal import Decimal as D, localcontext, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).parents[1]
LOW, HIGH = D('.0025'), D('.0075')
RADIUS = D('.0025')


def up_sum(values):
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        return sum(values, D(0))


def up_mul(left, right):
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        return left * right


def up_div(numerator, denominator):
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        return numerator / denominator


def up_pow(base, exponent):
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        return base ** exponent


def artifact(center):
    tag = '_'.join(str(x).replace('.', 'p') for x in center)
    return ROOT / 'results' / (
        'central-rank-six-hessian-taylor-majorant-center-' + tag +
        '-radius-0p0025-current-v3.json')


def chart_result(low_count, target):
    center = (LOW,) * low_count + (HIGH,) * (6 - low_count)
    source = json.loads(artifact(center).read_text())
    if source['rank'] != 6:
        raise RuntimeError('chart-rank mismatch')
    if tuple(D(x) for x in source['taylor_center']) != center:
        raise RuntimeError('chart-center mismatch')
    if D(source['taylor_radius']) != RADIUS:
        raise RuntimeError('chart-radius mismatch')
    if not source['interval_certified']:
        raise RuntimeError('source chart is uncertified')
    if source.get('source_tail_coordinate_multiplicity') != 6:
        raise RuntimeError('rank-six source-tail multiplicity is absent or stale')
    if source.get('directed_scalar_arithmetic_version') != 2:
        raise RuntimeError('directed scalar arithmetic marker is absent or stale')
    if source.get('source_remainder_binomial_version') != 1:
        raise RuntimeError('closed-binomial source remainder marker is absent or stale')
    if source.get('taylor_product_kernel_version') != 2:
        raise RuntimeError('degree-bucket Taylor product kernel is absent or stale')
    if (D(source.get('source_coefficient_envelope', '-1')) != D('6.038308') or
            source.get('source_exact_coefficient_degree') != 49 or
            source.get('source_tail_first_enveloped_degree') != 50 or
            source.get('source_tail_explicit_degree_cutoff') != 200 or
            not source.get('source_tail_geometric_ratio_below_one', False)):
        raise RuntimeError('analytic source-envelope metadata is absent or stale')
    if (source.get('inverse_lower_bound_count') != 15 or
            D(source.get('minimum_inverse_lower_bound', '0')) <= 0 or
            not source.get('all_inverse_lower_bounds_positive', False)):
        raise RuntimeError('rational LDL inverse-floor certificate is absent or stale')

    degree_max = int(source['taylor_degree'])
    base = D(source['finite_jet_budget_radius'])
    budgets = source['finite_jet_hessian_row_budgets_by_degree']
    scale = up_div(RADIUS, base)
    # Each stored value is one absolute Hessian-row budget.  The induced
    # row-sum norm is their maximum, not their sum.
    center_tensor = up_div(max(D(x) for x in budgets['3']), base)
    variation = {}
    for degree in range(4, degree_max + 1):
        hessian = up_mul(
            max(D(x) for x in budgets[str(degree)]),
            up_pow(scale, degree - 2),
        )
        variation[str(degree)] = up_div(
            up_mul(hessian, D(degree - 2)), RADIUS)
    tail = D(source['third_tensor_remainder_bound'])
    degree_five_plus = up_sum(
        [variation[str(d)] for d in range(5, degree_max + 1)] + [tail])
    total = up_sum([center_tensor, *variation.values(), tail])
    return {
        'low_coordinate_count': low_count,
        'center': [str(x) for x in center],
        'covered_ordered_box': ('[0,.005]^' + str(low_count) +
                                ' x [.005,.01]^' + str(6-low_count)),
        'taylor_degree': degree_max,
        'center_third_tensor_l1': str(center_tensor),
        'degree_four_through_taylor_degree_variation': {
            degree: str(value) for degree, value in variation.items()
        },
        'post_taylor_degree_C3_remainder': str(tail),
        'degree_five_and_higher_third_tensor_remainder': str(degree_five_plus),
        'uniform_third_tensor_l1_bound': str(total),
        'bound_below_required_ceiling': total < target,
        'source_chart_interval_certified': True,
    }


def main():
    target_source = json.loads((ROOT / 'results' /
        'central-rank-six-continuum-target.json').read_text())
    geometry = json.loads((ROOT / 'results' /
        'central-rank-six-continuum-transport-geometry.json').read_text())
    if (not geometry.get('interval_inputs_certified', False) or
            not geometry.get('all_8008_ordered_half_grid_cells_covered', False) or
            not geometry.get('all_seven_ordered_binary_macro_charts_cover_simplex', False) or
            not geometry.get('stored_ceiling_no_greater_than_exact', False) or
            D(geometry['stored_downward_rounded_ceiling']) !=
            D(target_source['sufficient_uniform_third_tensor_l1_ceiling'])):
        raise RuntimeError('continuum transport geometry certificate is absent or stale')
    target = D(target_source['sufficient_uniform_third_tensor_l1_ceiling'])
    charts = [chart_result(k, target) for k in range(7)]
    maximum = max(D(row['uniform_third_tensor_l1_bound']) for row in charts)
    maximum_tail = max(D(row['degree_five_and_higher_third_tensor_remainder'])
                       for row in charts)
    proved = maximum < target
    result = {
        'partition': '[0,.005] union [.005,.01] in each coordinate',
        'ordered_binary_patterns': 7,
        'transport_geometry_certificate': (
            'central-rank-six-continuum-transport-geometry.json'),
        'charts': charts,
        'maximum_degree_five_and_higher_third_tensor_remainder': str(maximum_tail),
        'uniform_third_tensor_l1_bound': str(maximum),
        'required_uniform_third_tensor_l1_ceiling': str(target),
        'uniform_bound_below_required_ceiling': proved,
        'all_8008_ordered_half_grid_cells_covered': True,
        'directed_decimal_rounding': True,
        'interval_certified': proved and all(
            row['source_chart_interval_certified'] for row in charts),
        'rh_proved': False,
    }
    output = ROOT / 'results' / 'central-rank-six-third-tensor-seven-chart-cover.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
