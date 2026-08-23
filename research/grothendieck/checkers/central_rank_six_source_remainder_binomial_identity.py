"""Exact audit of the closed-binomial rank-six analytic source remainder."""
import json
import math
from decimal import Decimal as D, Context, ROUND_CEILING
from pathlib import Path

ROOT = Path(__file__).parents[1]
UP = Context(prec=90, rounding=ROUND_CEILING)
VARIABLES = 6
CENTER = D('.01')
CHART_RADIUS = D('.0025')
ANCHOR_RADIUS = D('.01')
SOURCE_FIRST = 39
SOURCE_CUTOFF = 200
MAXIMUM_FIXED_ORDER = 2 * (VARIABLES - 1) + 3
TRUNCATION_FIRSTS = (6, 8, 9)
M = D('6.038308')


def falling(p, order):
    return math.factorial(p) // math.factorial(p - order)


identity_checks = 0
for omitted_first in TRUNCATION_FIRSTS:
    for fixed_order in range(MAXIMUM_FIXED_ORDER + 1):
        for p in range(max(SOURCE_FIRST, fixed_order + omitted_first),
                       SOURCE_CUTOFF + 1):
            for degree in range(omitted_first, p - fixed_order + 1):
                left = falling(p, fixed_order + degree) // math.factorial(degree)
                right = falling(p, fixed_order) * math.comb(p - fixed_order, degree)
                assert left == right
                identity_checks += 1

enlarged_center = UP.add(CENTER, UP.multiply(D(VARIABLES), CHART_RADIUS))
ratios = [UP.multiply(enlarged_center, UP.divide(
    D(SOURCE_CUTOFF + 2), D(SOURCE_CUTOFF + 2 - fixed_order)))
    for fixed_order in range(MAXIMUM_FIXED_ORDER + 1)]
maximum_ratio = max(ratios)
assert maximum_ratio < 1
anchor_ratios = [UP.multiply(ANCHOR_RADIUS, UP.divide(
    D(SOURCE_CUTOFF + 2), D(SOURCE_CUTOFF + 2 - fixed_order)))
    for fixed_order in range(MAXIMUM_FIXED_ORDER + 1)]
maximum_anchor_ratio = max(anchor_ratios)
assert maximum_anchor_ratio <= D('.011')

envelope_source = json.loads((ROOT / 'results' /
    'F-prime-unit-disk-theta-coarse-certificate.json').read_text())
rouche_source = json.loads((ROOT / 'results' /
    'xi-centered-unit-disk-rouche-certificate.json').read_text())
certified_f_prime = D(envelope_source['F_prime_unit_disk_upper'])
assert envelope_source['directed_decimal_rounding']
assert envelope_source['target_20_certified']
assert certified_f_prime < M
rouche_margin = D(rouche_source[
    'twice_Xi_half_minus_Xi_three_halves_lower_bound'])
assert rouche_source['centered_q_unit_disk_zero_free_by_theta_Rouche']
assert rouche_source['directed_decimal_rounding']
assert rouche_margin > D(envelope_source['certified_m_lower'])

result = {
    'rank': VARIABLES,
    'source_coefficient_envelope': str(M),
    'certified_F_prime_unit_disk_upper': str(certified_f_prime),
    'certified_Rouche_margin_lower': str(rouche_margin),
    'copied_F_prime_certificate_margin': envelope_source['certified_m_lower'],
    'Rouche_margin_strictly_exceeds_copied_margin': True,
    'centered_unit_disk_zero_free_certified': True,
    'coefficient_implication': '|F_p| <= sup|F_prime|/p <= 6.038308',
    'source_first_enveloped_degree': SOURCE_FIRST,
    'source_explicit_degree_cutoff': SOURCE_CUTOFF,
    'tested_first_omitted_taylor_degrees': list(TRUNCATION_FIRSTS),
    'maximum_fixed_derivative_order': MAXIMUM_FIXED_ORDER,
    'exact_factorial_binomial_identity_checks': identity_checks,
    'all_factorial_binomial_identities_hold': True,
    'binary_chart_coordinate_radius': str(CHART_RADIUS),
    'enlarged_scalar_radius': str(enlarged_center),
    'maximum_source_degree_tail_ratio': str(maximum_ratio),
    'source_degree_tail_ratio_below_one': True,
    'anchor_tail_maximum_source_degree_ratio': str(maximum_anchor_ratio),
    'anchor_tail_ratio_allowance': '0.011',
    'anchor_tail_geometric_divisor': '0.989',
    'anchor_tail_ratio_within_allowance': True,
    'directed_decimal_rounding': True,
    'interval_certified': True,
    'rh_proved': False,
}


if __name__ == '__main__':
    output = ROOT / 'results' / 'central-rank-six-source-remainder-binomial-identity.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
