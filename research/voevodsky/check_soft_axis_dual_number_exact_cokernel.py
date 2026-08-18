"""Compute the first soft deformation of the full exact-form cokernel."""

from math import comb


P = 2305843009213693951
INV2 = pow(2, P - 2, P)
SECTORS = ((1, 1), (1, 0), (0, 1), (0, 0))


def add(first, second):
    result = dict(first)
    for monomial, coefficient in second.items():
        result[monomial] = (result.get(monomial, 0) + coefficient) % P
    return {m: c for m, c in result.items() if c}


def scale(polynomial, coefficient):
    return {m: coefficient * c % P for m, c in polynomial.items() if coefficient * c % P}


def multiply(first, second):
    result = {}
    for (a1, b1), x in first.items():
        for (a2, b2), y in second.items():
            monomial = (a1 + a2, b1 + b2)
            result[monomial] = (result.get(monomial, 0) + x * y) % P
    return {m: c for m, c in result.items() if c}


def derivative(polynomial, variable):
    result = {}
    for (a_degree, b_degree), coefficient in polynomial.items():
        degree = (a_degree, b_degree)[variable]
        if degree:
            monomial = (a_degree - (variable == 0), b_degree - (variable == 1))
            result[monomial] = coefficient * degree % P
    return result


def dual_add(first, second):
    return add(first[0], second[0]), add(first[1], second[1])


def dual_scale(pair, coefficient):
    return scale(pair[0], coefficient), scale(pair[1], coefficient)


def dual_multiply(first, second):
    return multiply(first[0], second[0]), add(multiply(first[0], second[1]), multiply(first[1], second[0]))


def dual_power(pair, exponent):
    result = ({(0, 0): 1}, {})
    for _ in range(exponent):
        result = dual_multiply(result, pair)
    return result


def exact_pair(sa, sb, monomial, is_q):
    f = ({monomial: 1}, {})
    ea, eb = 2 - sa, 2 - sb
    l1 = ({(0, 1): 1, (0, 0): 1}, {(0, 0): -1 % P})
    l2 = ({(1, 0): 1}, {(0, 0): -INV2 % P})
    k = ({(4, 0): 1}, {(2, 0): 1, (2, 2): -1 % P})
    base = dual_multiply(dual_power(l1, ea), dual_power(l2, eb))

    if not is_q:
        answer = dual_scale(dual_multiply(dual_multiply((derivative(f[0], 1), {}), base), k), -1)
        if sa:
            term = dual_multiply(dual_multiply(f, dual_power(l1, ea - 1)), dual_power(l2, eb))
            answer = dual_add(answer, dual_scale(dual_multiply(term, k), sa))
        k_b = (derivative(k[0], 1), derivative(k[1], 1))
        answer = dual_add(answer, dual_scale(dual_multiply(dual_multiply(f, base), k_b), 3 * INV2 % P))
        return answer

    answer = dual_multiply(dual_multiply((derivative(f[0], 0), {}), base), k)
    if sb:
        term = dual_multiply(dual_multiply(f, dual_power(l1, ea)), dual_power(l2, eb - 1))
        answer = dual_add(answer, dual_scale(dual_multiply(term, k), -sb))
    k_a = (derivative(k[0], 0), derivative(k[1], 0))
    return dual_add(answer, dual_scale(dual_multiply(dual_multiply(f, base), k_a), -3 * INV2 % P))


def rank(columns, row_count):
    basis = {}
    for sparse in columns:
        vector = dict(sparse)
        while vector:
            pivot = min(vector)
            if pivot in basis:
                factor = vector[pivot]
                for index, value in basis[pivot].items():
                    vector[index] = (vector.get(index, 0) - factor * value) % P
                    if not vector[index]:
                        vector.pop(index, None)
            else:
                inverse = pow(vector[pivot], P - 2, P)
                basis[pivot] = {index: value * inverse % P for index, value in vector.items()}
                break
    assert all(index < row_count for column in columns for index in column)
    return len(basis)


def main():
    results = []
    for cutoff in (12, 16, 20, 24, 28):
        monomials = tuple((i, total - i) for total in range(cutoff + 1) for i in range(total + 1))
        position = {monomial: index for index, monomial in enumerate(monomials)}
        n = len(monomials)
        pairs = []
        for sa, sb in SECTORS:
            for total in range(cutoff + 1):
                for i in range(total + 1):
                    for is_q in (False, True):
                        pair = exact_pair(sa, sb, (i, total - i), is_q)
                        support = set(pair[0]) | set(pair[1])
                        if support and max(map(sum, support)) <= cutoff:
                            pairs.append(pair)

        base_columns = [
            {position[monomial]: coefficient for monomial, coefficient in zero.items()}
            for zero, _ in pairs
        ]
        base_rank = rank(base_columns, n)
        special_cokernel = n - base_rank

        dual_columns = []
        for zero, first in pairs:
            dual_columns.append(
                add_sparse(
                    {position[m]: c for m, c in zero.items()},
                    {n + position[m]: c for m, c in first.items()},
                )
            )
            dual_columns.append({n + position[m]: c for m, c in zero.items()})
        dual_rank = rank(dual_columns, 2 * n)
        dual_cokernel = 2 * n - dual_rank
        flatness_defect = 2 * special_cokernel - dual_cokernel
        results.append((cutoff, special_cokernel, dual_cokernel, flatness_defect))

    print("dual_number_data: K=a4+u*a2*(1-b2),L1=b+1-u,L2=a-u/2")
    for cutoff, special, dual, defect in results:
        print(f"cutoff_{cutoff}: special_coker={special},dual_coker={dual},flatness_defect={defect}")
    assert all(special == 4 * cutoff for cutoff, special, _, _ in results)
    assert all(dual == 7 * cutoff + 6 for cutoff, _, dual, _ in results)
    assert all(defect == cutoff - 6 for cutoff, _, _, defect in results)
    print("special_cokernel_dimension_formula: 4D")
    print("dual_number_cokernel_dimension_formula_tested: 7D+6")
    print("dual_number_flatness_defect_formula_tested: D-6")
    print("Euler_plane_independent_flat_lift: REFUTED_IN_TESTED_FILTRATION")
    print("first_soft_deformation: MIXES_FINITE_RESONANCE_WITH_QUARTIC_TAIL")
    print("next_gate: LOG_BLOWUP_TOTAL_COMPLEX_WITH_FILTRATION_SHIFTS")


def add_sparse(first, second):
    result = dict(first)
    for index, coefficient in second.items():
        result[index] = (result.get(index, 0) + coefficient) % P
        if not result[index]:
            result.pop(index)
    return result


if __name__ == "__main__":
    main()
