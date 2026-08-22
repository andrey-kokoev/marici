"""Global first-four Newton-LDL denominator floors from determinant bounds."""
import json
from decimal import Decimal as D
from pathlib import Path

import reduced_source_central_interval_chords as I

ROOT = Path(__file__).parents[1]
r3 = json.loads((ROOT / 'results' / 'central-rank-three-loewner-continuum.json').read_text())
r4 = json.loads((ROOT / 'results' / 'central-rank-four-loewner-continuum.json').read_text())
A = [[(D(a), D(b)) for a, b in row] for row in r3['normalized_divided_difference_matrix']]

q1 = A[0][0]
q2 = I.sub(I.mul(A[0][0], A[1][1]), I.mul(A[0][1], A[0][1]))
q3 = tuple(D(x) for x in r3['Vandermonde_normalized_rank_three_determinant_interval'])
q4_lower = D(r4['continuum_normalized_rank_four_lower_bound'])

# For a positive-semidefinite matrix, each LDL pivot is no larger than its
# original diagonal. Hadamard therefore gives Q_k <= product A_ii.
q2_upper = I.up.multiply(A[0][0][1], A[1][1][1])
q3_upper = I.up.multiply(q2_upper, A[2][2][1])
d1_lower = q1[0]
d2_lower = I.down.divide(q2[0], q1[1])
d3_lower = I.down.divide(q3[0], q2_upper)
d4_lower = I.down.divide(q4_lower, q3_upper)

floors = [d1_lower, d2_lower, d3_lower, d4_lower]
assert all(x > 0 for x in floors)
result = {
    'domain': ['0', '0.01'],
    'normalized_rank_two_determinant_interval': [str(x) for x in q2],
    'rank_two_hadamard_upper_bound': str(q2_upper),
    'rank_three_hadamard_upper_bound': str(q3_upper),
    'global_first_four_pivot_lower_bounds': [str(x) for x in floors],
    'method': 'Q_k/Q_(k-1) with directed determinant lowers and Hadamard uppers',
    'all_four_denominator_floors_strictly_positive': True,
    'directed_decimal_rounding': True,
    'interval_certified': True,
    'rh_proved': False,
}

if __name__ == '__main__':
    output = ROOT / 'results' / 'central-rank-four-global-pivot-denominators.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
