"""Record the first tagged degree-eight binary-chart transport obstruction."""
import json
from decimal import Decimal as D, localcontext, ROUND_CEILING
from pathlib import Path

from central_rank_six_third_tensor_seven_chart_cover import chart_result

ROOT = Path(__file__).parents[1]


def up_div(numerator, denominator):
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        return numerator / denominator


def main():
    target_source = json.loads((ROOT / 'results' /
        'central-rank-six-continuum-target.json').read_text())
    ceiling = D(target_source['sufficient_uniform_third_tensor_l1_ceiling'])
    row = chart_result(0, ceiling)
    remainder = D(row['post_taylor_degree_C3_remainder'])
    total = D(row['uniform_third_tensor_l1_bound'])
    remainder_obstructs = remainder >= ceiling
    total_obstructs = total >= ceiling
    if not remainder_obstructs or not total_obstructs:
        raise RuntimeError('tagged all-high degree-eight chart is not obstructed')
    result = {
        'source_artifact': (
            'central-rank-six-hessian-taylor-majorant-center-'
            '0p0075_0p0075_0p0075_0p0075_0p0075_0p0075-'
            'radius-0p0025-current-v2.json'),
        'chart_center': row['center'],
        'chart_radius': '0.0025',
        'taylor_degree': row['taylor_degree'],
        'certified_post_degree_eight_C3_remainder': str(remainder),
        'certified_uniform_third_tensor_l1_bound': str(total),
        'required_uniform_third_tensor_l1_ceiling': str(ceiling),
        'remainder_excess_factor': str(up_div(remainder, ceiling)),
        'uniform_bound_excess_factor': str(up_div(total, ceiling)),
        'post_degree_eight_remainder_alone_exceeds_ceiling': remainder_obstructs,
        'all_high_binary_chart_transport_obstructed': total_obstructs,
        'broken_assumption': (
            'The current degree-eight Taylor/analytic-tail majorant on the '
            'all-high radius-.0025 chart would have a post-degree-eight C3 '
            'remainder below the derivative-transport ceiling.'),
        'scope': (
            'This falsifies the adequacy of the present degree-eight '
            'majorant on one required binary chart. It does not falsify '
            'rank-six pivot positivity, and it does not exclude a sharper '
            'tail estimate or a finer chart cover.'),
        'directed_decimal_rounding': True,
        'interval_certified': True,
        'rh_proved': False,
    }
    output = ROOT / 'results' / (
        'central-rank-six-degree-eight-all-high-chart-obstruction.json')
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
