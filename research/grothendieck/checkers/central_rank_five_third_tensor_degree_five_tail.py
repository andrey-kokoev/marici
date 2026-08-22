"""Certify the degree-five-and-higher third-tensor Taylor tail.

For a homogeneous polynomial of degree d at radius R, its total ordered
third-derivative l1 budget is exactly (d-2)/R times its total ordered
Hessian l1 budget.  This converts the already-certified degree 5--7
Hessian row budgets without re-evaluating the symbolic jet.  The separate
all-orders C3 majorant supplies degrees 8 and higher.
"""
import json
from decimal import Decimal as D, localcontext, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).parents[1]
# The imported degree budgets were evaluated on the endpoint cell of
# half-width .0005; use that same radius in the homogeneous identity.
R = D('.0005')


def upward_sum(values):
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        return sum(values, D(0))


def main():
    deep = json.loads((ROOT / 'results' / 'central-rank-five-hessian-taylor-deep.json').read_text())
    majorant = json.loads((ROOT / 'results' / 'central-rank-five-hessian-taylor-majorant.json').read_text())
    if 'third_tensor_remainder_bound' not in majorant:
        raise RuntimeError('C3 all-orders majorant has not completed')

    by_degree = {}
    for degree in range(5, 8):
        rows = [D(x) for x in deep['hessian_row_variation_budgets_by_degree'][str(degree)]]
        with localcontext() as context:
            context.prec = 50
            context.rounding = ROUND_CEILING
            by_degree[str(degree)] = upward_sum(rows) * D(degree - 2) / R

    finite = upward_sum(by_degree.values())
    infinite = D(majorant['third_tensor_remainder_bound'])
    total = upward_sum([finite, infinite])
    result = {
        'radius': str(R),
        'degree_five_through_seven_third_tensor_variation_by_degree': {
            degree: str(value) for degree, value in by_degree.items()
        },
        'degree_five_through_seven_total': str(finite),
        'degree_eight_and_higher_C3_remainder': str(infinite),
        'degree_five_and_higher_third_tensor_tail': str(total),
        'conversion_identity': 'T3_l1(d) = (d-2)/R * Hessian_l1(d)',
        'directed_decimal_rounding': True,
        'interval_certified': True,
        'rh_proved': False,
    }
    output = ROOT / 'results' / 'central-rank-five-third-tensor-degree-five-tail.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
