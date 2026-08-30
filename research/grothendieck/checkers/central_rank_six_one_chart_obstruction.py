"""Record the rigorous obstruction to the single radius-.01 rank-six chart."""
import json
from decimal import Decimal as D, localcontext, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).parents[1]


def main():
    source = json.loads((ROOT / 'results' /
        'central-rank-six-hessian-taylor-majorant-radius-0p01.json').read_text())
    target = json.loads((ROOT / 'results' /
        'central-rank-six-continuum-target.json').read_text())
    if source['rank'] != 6 or source['taylor_degree'] != 7:
        raise RuntimeError('unexpected one-chart Taylor model')
    if source['taylor_center'] != ['0.01'] * 6 or D(source['taylor_radius']) != D('.01'):
        raise RuntimeError('unexpected one-chart geometry')
    if not source['interval_certified']:
        raise RuntimeError('one-chart remainder is not interval-certified')
    if source.get('source_tail_coordinate_multiplicity') != 6:
        raise RuntimeError('rank-six source-tail multiplicity is absent or stale')
    if source.get('directed_scalar_arithmetic_version') != 2:
        raise RuntimeError('directed scalar arithmetic marker is absent or stale')
    if source.get('source_remainder_binomial_version') != 1:
        raise RuntimeError('closed-binomial source remainder marker is absent or stale')
    if source.get('taylor_product_kernel_version') != 2:
        raise RuntimeError('degree-bucket Taylor product kernel is absent or stale')
    if (D(source.get('source_coefficient_envelope', '-1')) != D('6.038308') or
            source.get('source_tail_first_enveloped_degree') != 39 or
            source.get('source_tail_explicit_degree_cutoff') != 200 or
            not source.get('source_tail_geometric_ratio_below_one', False)):
        raise RuntimeError('analytic source-envelope metadata is absent or stale')
    if (source.get('inverse_lower_bound_count') != 15 or
            D(source.get('minimum_inverse_lower_bound', '0')) <= 0 or
            not source.get('all_inverse_lower_bounds_positive', False)):
        raise RuntimeError('rational LDL inverse-floor certificate is absent or stale')

    remainder = D(source['third_tensor_remainder_bound'])
    ceiling = D(target['sufficient_uniform_third_tensor_l1_ceiling'])
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        excess_factor = remainder / ceiling
    obstructed = remainder >= ceiling
    result = {
        'chart_center': source['taylor_center'],
        'chart_radius': source['taylor_radius'],
        'taylor_degree': source['taylor_degree'],
        'certified_degree_eight_and_higher_C3_remainder': str(remainder),
        'required_uniform_third_tensor_l1_ceiling': str(ceiling),
        'remainder_excess_factor': str(excess_factor),
        'single_chart_continuum_transport_obstructed': obstructed,
        'broken_assumption': (
            'A degree-seven Taylor model on the full radius-.01 box would have '
            'a sufficiently small all-orders C3 remainder.'),
        'scope': 'This falsifies only the one-chart carrier, not the seven-chart cover or rank-six positivity.',
        'directed_decimal_rounding': True,
        'interval_certified': obstructed,
        'rh_proved': False,
    }
    output = ROOT / 'results' / 'central-rank-six-one-chart-obstruction.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
