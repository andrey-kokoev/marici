"""Isolate the analytic source-tail share of the rank-six C3 obstruction."""
import json
import math
import os
from decimal import Decimal as D, localcontext, ROUND_CEILING
from pathlib import Path

import reduced_source_central_interval_chords as I

ROOT = Path(__file__).parents[1]
RANK = 6
ORDER = 8
RADIUS = D('.0025')
CENTER_BOUND = D('.01')
ENVELOPE = D('6.038308')
FIRST_ENVELOPED_DEGREE = int(os.environ.get(
    'MARICI_FIRST_ENVELOPED_DEGREE', '39'))


def up_pow(base, exponent):
    return I.up.power(base, D(exponent))


def source_remainder(i, j):
    out = []
    omitted_degree = ORDER + 1
    coordinate_radius = I.up.multiply(D(RANK), RADIUS)
    enlarged_center = I.up.add(CENTER_BOUND, coordinate_radius)
    denominator = D(math.factorial(i) * math.factorial(j))
    for derivative in range(4):
        fixed_order = i + j + derivative
        coordinate_derivatives = up_pow(D(RANK), derivative)
        total = D(0)
        for p in range(max(FIRST_ENVELOPED_DEGREE,
                           fixed_order + omitted_degree), 201):
            fixed_falling = math.factorial(p) // math.factorial(p - fixed_order)
            common = I.up.divide(I.up.multiply(ENVELOPE, I.up.multiply(
                coordinate_derivatives, D(fixed_falling))), denominator)
            for degree in range(omitted_degree, p - fixed_order + 1):
                term = I.up.multiply(
                    common, D(math.comb(p - fixed_order, degree)))
                term = I.up.multiply(term, up_pow(
                    CENTER_BOUND, p - fixed_order - degree))
                term = I.up.multiply(term, up_pow(coordinate_radius, degree))
                total = I.up.add(total, term)
        p0 = 201
        fixed_falling = math.factorial(p0) // math.factorial(p0 - fixed_order)
        first = I.up.divide(I.up.multiply(ENVELOPE, I.up.multiply(
            coordinate_derivatives, I.up.multiply(
                D(fixed_falling), up_pow(enlarged_center, p0 - fixed_order)))),
            denominator)
        ratio = I.up.multiply(enlarged_center, I.up.divide(
            D(p0 + 1), D(p0 + 1 - fixed_order)))
        if ratio >= 1:
            raise ArithmeticError('source p-tail ratio is not below one')
        total = I.up.add(total, I.up.divide(
            first, I.down.subtract(D(1), ratio)))
        out.append(total)
    return tuple(out)


def up_div(numerator, denominator):
    with localcontext() as context:
        context.prec = 50
        context.rounding = ROUND_CEILING
        return numerator / denominator


def main():
    target = json.loads((ROOT / 'results' /
        'central-rank-six-continuum-target.json').read_text())
    chart = json.loads((ROOT / 'results' / (
        'central-rank-six-hessian-taylor-majorant-center-'
        '0p0075_0p0075_0p0075_0p0075_0p0075_0p0075-'
        'radius-0p0025-current-v2.json')).read_text())
    components = [[source_remainder(i, j) for j in range(RANK)]
                  for i in range(RANK)]
    maxima = [max(value[q] for row in components for value in row)
              for q in range(4)]
    combined = [D(value) for value in chart['maximum_matrix_entry_C3_remainder']]
    if (FIRST_ENVELOPED_DEGREE == 39 and
            any(maxima[q] > combined[q] for q in range(4))):
        raise RuntimeError('isolated source bound exceeds combined entry bound')
    ceiling = D(target['sufficient_uniform_third_tensor_l1_ceiling'])
    source_alone_obstructs = maxima[3] >= ceiling
    result = {
        'rank': RANK,
        'taylor_degree': ORDER,
        'chart_radius': str(RADIUS),
        'source_tail_first_enveloped_degree': FIRST_ENVELOPED_DEGREE,
        'source_coefficient_envelope': str(ENVELOPE),
        'source_tail_coordinate_multiplicity': RANK,
        'maximum_matrix_entry_source_C3_remainder': [str(x) for x in maxima],
        'maximum_matrix_entry_combined_C3_remainder': [str(x) for x in combined],
        'required_uniform_third_tensor_l1_ceiling': str(ceiling),
        'source_C3_excess_factor': str(up_div(maxima[3], ceiling)),
        'source_majorant_alone_exceeds_transport_ceiling': source_alone_obstructs,
        'isolated_source_bounds_no_greater_than_combined_bounds': (
            True if FIRST_ENVELOPED_DEGREE == 39 else None),
        'interpretation': (
            'This isolates the analytic coefficient-envelope contribution '
            'before LDL propagation. It is a bound diagnosis, not a lower '
            'bound on the true Taylor remainder.'),
        'directed_decimal_rounding': True,
        'interval_certified': True,
        'rh_proved': False,
    }
    suffix = '' if FIRST_ENVELOPED_DEGREE == 39 else (
        '-from-degree-' + str(FIRST_ENVELOPED_DEGREE))
    output = ROOT / 'results' / (
        'central-rank-six-source-C3-component' + suffix + '.json')
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
