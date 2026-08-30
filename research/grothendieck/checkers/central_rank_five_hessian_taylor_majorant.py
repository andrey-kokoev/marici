"""All-orders C3 remainder majorant for the endpoint final pivot."""
import json, math, os
from decimal import Decimal as D
from pathlib import Path

import central_rank_five_hessian_taylor_deep as T

P = T.P
I = T.I
R = D(os.environ.get('MARICI_TAYLOR_RADIUS', '.0005'))
ZERO_NORM = (D(0), D(0), D(0), D(0))
DIRECTED_SCALAR_ARITHMETIC_VERSION = 2
SOURCE_REMAINDER_BINOMIAL_VERSION = 1
TAYLOR_PRODUCT_KERNEL_VERSION = 2
SOURCE_EXACT_COEFFICIENT_DEGREE = len(T.f) - 1
FIRST_ENVELOPED_DEGREE = len(T.f)


def up_pow(base, exponent):
    return I.up.power(base, D(exponent))


def nadd(a, b):
    return tuple(I.up.add(a[i], b[i]) for i in range(4))


def nmul(a, b):
    return (I.up.multiply(a[0], b[0]),
            I.up.add(I.up.multiply(a[1], b[0]), I.up.multiply(a[0], b[1])),
            I.up.add(I.up.add(I.up.multiply(a[2], b[0]),
                              I.up.multiply(D(2), I.up.multiply(a[1], b[1]))),
                     I.up.multiply(a[0], b[2])),
            I.up.add(I.up.add(I.up.multiply(a[3], b[0]),
                              I.up.multiply(D(3), I.up.multiply(a[2], b[1]))),
                     I.up.add(I.up.multiply(D(3), I.up.multiply(a[1], b[2])),
                              I.up.multiply(a[0], b[3]))))


def degree_monomial_norm(degree, size):
    value = I.up.multiply(size, up_pow(R, degree))
    gradient = D(0) if degree == 0 else I.up.multiply(
        I.up.multiply(size, D(degree)), up_pow(R, degree - 1))
    hessian = D(0) if degree < 2 else I.up.multiply(
        I.up.multiply(size, D(degree * (degree - 1))),
        up_pow(R, degree - 2))
    third = D(0) if degree < 3 else I.up.multiply(
        I.up.multiply(size, D(degree * (degree - 1) * (degree - 2))),
        up_pow(R, degree - 3))
    return value, gradient, hessian, third


def monomial_norm(key, coefficient):
    return degree_monomial_norm(
        sum(key), max(abs(coefficient[0]), abs(coefficient[1])))


def polynomial_norm(jet):
    out = ZERO_NORM
    for key, coefficient in jet.items():
        out = nadd(out, monomial_norm(key, coefficient))
    return out


def high_product_norm(left, right):
    out = ZERO_NORM
    left_buckets = P.degree_buckets(left)
    right_buckets = P.degree_buckets(right)
    left_norms = {degree: polynomial_coefficient_norm(items)
                  for degree, items in left_buckets.items()}
    right_norms = {degree: polynomial_coefficient_norm(items)
                   for degree, items in right_buckets.items()}
    for left_degree, left_size in left_norms.items():
        for right_degree, right_size in right_norms.items():
            if left_degree + right_degree <= P.ORDER:
                continue
            product_size = I.up.multiply(left_size, right_size)
            out = nadd(out, degree_monomial_norm(
                left_degree + right_degree, product_size))
    return out


def polynomial_coefficient_norm(items):
    total = D(0)
    for _, coefficient in items:
        total = I.up.add(
            total, max(abs(coefficient[0]), abs(coefficient[1])))
    return total


def tm_add(a, b):
    return P.add(a[0], b[0]), nadd(a[1], b[1])


def tm_neg(a):
    return P.neg(a[0]), a[1]


def tm_sub(a, b):
    return tm_add(a, tm_neg(b))


def tm_mul(a, b):
    polynomial = P.mul(a[0], b[0])
    error = high_product_norm(a[0], b[0])
    error = nadd(error, nmul(polynomial_norm(a[0]), b[1]))
    error = nadd(error, nmul(a[1], polynomial_norm(b[0])))
    error = nadd(error, nmul(a[1], b[1]))
    return polynomial, error


inverse_norm_call_index = 0
inverse_lower_bounds = []
inverse_diagnostics = []


def exact_inverse_norm(a):
    global inverse_norm_call_index
    inverse_norm_call_index += 1
    full = nadd(polynomial_norm(a[0]), a[1])
    constant_interval = a[0][P.zero]
    if constant_interval[0] > 0:
        constant_lower = constant_interval[0]
        constant_sign = 'positive'
    elif constant_interval[1] < 0:
        constant_lower = constant_interval[1].copy_negate()
        constant_sign = 'negative'
    else:
        constant_lower = D(0)
        constant_sign = 'contains-zero'
    variation = I.up.add(polynomial_norm({k:v for k,v in a[0].items() if k != P.zero})[0], a[1][0])
    lower = I.down.subtract(constant_lower, variation)
    if lower <= 0:
        raise ArithmeticError(
            'inverse lower-bound obstruction: '
            f'call={inverse_norm_call_index}, variables={P.VARIABLES}, '
            f'order={P.ORDER}, center={[str(x) for x in T.CHART_CENTER]}, '
            f'radius={R}, constant_interval={constant_interval}, '
            f'constant_sign={constant_sign}, constant_lower={constant_lower}, '
            f'variation_upper={variation}, lower={lower}'
        )
    inverse_lower_bounds.append(lower)
    inverse_diagnostics.append({
        'call_index': inverse_norm_call_index,
        'constant_sign': constant_sign,
        'constant_lower_bound': str(constant_lower),
        'variation_upper_bound': str(variation),
        'denominator_floor': str(lower),
        'incoming_value_C3_norm': [str(value) for value in full],
    })
    inverse0 = I.up.divide(D(1), lower)
    lower2, lower3, lower4 = (up_pow(lower, degree) for degree in (2, 3, 4))
    inverse1 = I.up.divide(full[1], lower2)
    inverse2 = I.up.add(I.up.divide(full[2], lower2),
                        I.up.divide(I.up.multiply(D(2),
                            I.up.multiply(full[1], full[1])), lower3))
    inverse3 = I.up.add(
        I.up.add(I.up.divide(full[3], lower2),
                 I.up.divide(I.up.multiply(D(6),
                     I.up.multiply(full[1], full[2])), lower3)),
        I.up.divide(I.up.multiply(D(6),
            I.up.multiply(full[1], I.up.multiply(full[1], full[1]))), lower4))
    return (inverse0, inverse1, inverse2, inverse3), lower


def tm_inv(a):
    inverse_norm, _ = exact_inverse_norm(a)
    polynomial = P.inv(a[0])
    product = tm_mul(a, (polynomial, ZERO_NORM))
    residual = tm_sub((P.constant(1), ZERO_NORM), product)
    error = nmul(inverse_norm, nadd(polynomial_norm(residual[0]), residual[1]))
    return polynomial, error


def tm_div(a, b):
    return tm_mul(a, tm_inv(b))


def source_remainder(i, j):
    out = [D(0), D(0), D(0), D(0)]
    omitted_degree = P.ORDER + 1
    coordinate_radius = I.up.multiply(D(P.VARIABLES), R)
    enlarged_center = I.up.add(P.CENTER, coordinate_radius)
    denominator = D(math.factorial(i) * math.factorial(j))
    for derivative in range(4):
        fixed_order = i + j + derivative
        coordinate_derivatives = up_pow(D(P.VARIABLES), derivative)
        total = D(0)
        # For a source monomial x^p, first take the fixed derivatives and
        # then sum the omitted Taylor degrees by the binomial identity.
        for p in range(max(FIRST_ENVELOPED_DEGREE,
                           fixed_order + omitted_degree), 201):
            fixed_falling = math.factorial(p) // math.factorial(p - fixed_order)
            common = I.up.divide(I.up.multiply(P.M, I.up.multiply(
                coordinate_derivatives, D(fixed_falling))), denominator)
            for degree in range(omitted_degree, p - fixed_order + 1):
                term = I.up.multiply(common, D(math.comb(p - fixed_order, degree)))
                term = I.up.multiply(term, up_pow(
                    P.CENTER, p - fixed_order - degree))
                term = I.up.multiply(term, up_pow(coordinate_radius, degree))
                total = I.up.add(total, term)

        # For p >= 201, including every Taylor degree only enlarges the tail.
        # The consecutive full-binomial terms have ratio at most
        # (CENTER+nR) * 202/(202-fixed_order), which is below one.
        p0 = 201
        fixed_falling = math.factorial(p0) // math.factorial(p0 - fixed_order)
        first = I.up.divide(I.up.multiply(P.M, I.up.multiply(
            coordinate_derivatives, I.up.multiply(
                D(fixed_falling), up_pow(enlarged_center, p0 - fixed_order)))),
            denominator)
        ratio = I.up.multiply(enlarged_center, I.up.divide(
            D(p0 + 1), D(p0 + 1 - fixed_order)))
        if ratio >= 1:
            raise ArithmeticError('source p-tail geometric ratio is not below one')
        geometric_tail = I.up.divide(first, I.down.subtract(D(1), ratio))
        out[derivative] = I.up.add(total, geometric_tail)
    return tuple(out)


def padd(a, b):
    return [I.up.add(a[k] if k < len(a) else D(0), b[k] if k < len(b) else D(0))
            for k in range(max(len(a), len(b)))]


def pmul(a, b):
    out = [D(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = I.up.add(out[i+j], I.up.multiply(x, y))
    return out[:len(T.f)]


def ppow(a, n):
    out = [D(1)]
    for _ in range(n): out = pmul(out, a)
    return out


node = [P.CENTER, R]
homogeneous = []
h = [[D(1)]] + [[D(0)] for _ in range(len(T.f) - 1)]
powers = [ppow(node, q) for q in range(len(T.f))]
for _ in range(P.VARIABLES):
    h = [__import__('functools').reduce(padd,
         (pmul(h[d-q], powers[q]) for q in range(d+1)), [D(0)])
         for d in range(len(T.f))]
    homogeneous.append(h)


def known_remainder(i, j):
    value = [D(0)]
    for n in range(1, len(T.f)):
        coefficient = max(abs(T.f[n][0]), abs(T.f[n][1]))
        for k in range(i, n):
            ell = n - 1 - k
            if ell >= j:
                value = padd(value, [I.up.multiply(coefficient, x)
                                     for x in pmul(homogeneous[i][k-i], homogeneous[j][ell-j])])
    out = [D(0), D(0), D(0), D(0)]
    for degree in range(P.ORDER + 1, len(value)):
        out[0] = I.up.add(out[0], value[degree])
        out[1] = I.up.add(out[1], I.up.divide(
            I.up.multiply(D(degree), value[degree]), R))
        out[2] = I.up.add(out[2], I.up.divide(
            I.up.multiply(D(degree * (degree - 1)), value[degree]),
            up_pow(R, 2)))
        out[3] = I.up.add(out[3], I.up.divide(
            I.up.multiply(D(degree * (degree - 1) * (degree - 2)),
                          value[degree]), up_pow(R, 3)))
    return tuple(out)


source_errors = [[source_remainder(i, j) for j in range(P.VARIABLES)]
                 for i in range(P.VARIABLES)]
known_errors = [[known_remainder(i, j) for j in range(P.VARIABLES)]
                for i in range(P.VARIABLES)]
entry_errors = [[nadd(source_errors[i][j], known_errors[i][j])
                 for j in range(P.VARIABLES)] for i in range(P.VARIABLES)]
matrix = [[(T.matrix[i][j], entry_errors[i][j]) for j in range(P.VARIABLES)]
          for i in range(P.VARIABLES)]
lower = [[(P.constant(0), ZERO_NORM) for _ in range(P.VARIABLES)] for _ in range(P.VARIABLES)]
diagonal = []
for k in range(P.VARIABLES):
    pivot = matrix[k][k]
    for j in range(k): pivot = tm_sub(pivot, tm_mul(tm_mul(lower[k][j], lower[k][j]), diagonal[j]))
    diagonal.append(pivot); lower[k][k] = (P.constant(1), ZERO_NORM)
    for row in range(k + 1, P.VARIABLES):
        value = matrix[row][k]
        for j in range(k): value = tm_sub(value, tm_mul(tm_mul(lower[row][j], lower[k][j]), diagonal[j]))
        lower[row][k] = tm_div(value, pivot)

fifth = diagonal[-1]
source_tail_enlarged_center = I.up.add(
    P.CENTER, I.up.multiply(D(P.VARIABLES), R))
source_tail_maximum_fixed_order = 2 * (P.VARIABLES - 1) + 3
source_tail_ratio_ceiling = I.up.multiply(
    source_tail_enlarged_center,
    I.up.divide(D(202), D(202 - source_tail_maximum_fixed_order)))
result = {
    'rank': P.VARIABLES,
    'taylor_degree': P.ORDER,
    'taylor_center': [str(x) for x in T.CHART_CENTER],
    'taylor_radius': str(R),
    'maximum_matrix_entry_C2_remainder': [str(max(x[q] for row in entry_errors for x in row)) for q in range(3)],
    'maximum_matrix_entry_C3_remainder': [str(max(x[q] for row in entry_errors for x in row)) for q in range(4)],
    'maximum_matrix_entry_source_C3_remainder': [str(max(x[q] for row in source_errors for x in row)) for q in range(4)],
    'maximum_matrix_entry_known_polynomial_C3_remainder': [str(max(x[q] for row in known_errors for x in row)) for q in range(4)],
    'final_pivot_remainder_C2_norm': [str(x) for x in fifth[1][:3]],
    'final_pivot_remainder_C3_norm': [str(x) for x in fifth[1]],
    'all_pivot_remainder_C3_norms': [
        [str(value) for value in pivot[1]] for pivot in diagonal],
    'fifth_pivot_remainder_C2_norm': [str(x) for x in fifth[1][:3]] if P.VARIABLES == 5 else None,
    'fifth_pivot_remainder_C3_norm': [str(x) for x in fifth[1]] if P.VARIABLES == 5 else None,
    'hessian_remainder_bound': str(fifth[1][2]),
    'third_tensor_remainder_bound': str(fifth[1][3]),
    'finite_jet_budget_radius': T.result['budget_radius'],
    'finite_jet_hessian_row_budgets_by_degree': T.result['hessian_row_variation_budgets_by_degree'],
    'all_inverse_lower_bounds_positive': True,
    'inverse_lower_bound_count': len(inverse_lower_bounds),
    'minimum_inverse_lower_bound': str(min(inverse_lower_bounds)),
    'inverse_gate_diagnostics': inverse_diagnostics,
    'source_and_rational_remainders_included': True,
    'source_tail_coordinate_multiplicity': P.VARIABLES,
    'directed_scalar_arithmetic_version': DIRECTED_SCALAR_ARITHMETIC_VERSION,
    'source_remainder_binomial_version': SOURCE_REMAINDER_BINOMIAL_VERSION,
    'taylor_product_kernel_version': TAYLOR_PRODUCT_KERNEL_VERSION,
    'source_coefficient_envelope': str(P.M),
    'source_coefficient_envelope_basis': (
        'Cauchy from certified sup_|t|<=1 |F_prime(t)| < 6.038308; '
        '|F_p| <= M/p <= M'),
    'source_coefficient_envelope_result': (
        'F-prime-unit-disk-theta-coarse-certificate.json'),
    'source_exact_coefficient_degree': SOURCE_EXACT_COEFFICIENT_DEGREE,
    'source_tail_first_enveloped_degree': FIRST_ENVELOPED_DEGREE,
    'source_tail_explicit_degree_cutoff': 200,
    'source_tail_enlarged_center': str(source_tail_enlarged_center),
    'source_tail_geometric_ratio_ceiling': str(source_tail_ratio_ceiling),
    'source_tail_geometric_ratio_below_one': source_tail_ratio_ceiling < 1,
    'interval_certified': True,
    'rh_proved': False,
}

if __name__ == '__main__':
    default_center = T.CHART_CENTER == (D('.01'),) * P.VARIABLES
    rank_prefix = 'central-rank-' + ('five' if P.VARIABLES == 5 else 'six')
    if R == D('.0005') and default_center:
        name = rank_prefix + '-hessian-taylor-majorant.json'
    elif default_center:
        name = rank_prefix + '-hessian-taylor-majorant-radius-' + str(R).replace('.', 'p') + '.json'
    else:
        center_tag = '_'.join(str(x).replace('.', 'p') for x in T.CHART_CENTER)
        name = (rank_prefix + '-hessian-taylor-majorant-center-' + center_tag +
                '-radius-' + str(R).replace('.', 'p') + '.json')
    output_tag = os.environ.get('MARICI_TAYLOR_OUTPUT_TAG', '')
    if output_tag:
        if not output_tag.replace('-', '').replace('_', '').isalnum():
            raise ValueError('MARICI_TAYLOR_OUTPUT_TAG must be alphanumeric, hyphen, or underscore')
        name = name[:-5] + '-' + output_tag + '.json'
    output = Path(__file__).parents[1] / 'results' / name
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
