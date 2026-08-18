"""Test whether naive a,b multiplication descends to the soft exact cokernel."""

from math import comb


P = 2305843009213693951
SECTORS = ((1, 1), (1, 0), (0, 1), (0, 0))


def exact_rows(cutoff):
    monomials = tuple((i, total - i) for total in range(cutoff + 1) for i in range(total + 1))
    position = {monomial: index for index, monomial in enumerate(monomials)}
    rows = []

    def emit(terms):
        terms = {m: coefficient % P for m, coefficient in terms.items() if coefficient % P}
        if not terms or max(sum(m) for m in terms) > cutoff:
            return
        row = [0] * len(monomials)
        for monomial, coefficient in terms.items():
            row[position[monomial]] = coefficient
        rows.append((row, max(sum(m) for m in terms)))

    # Frozen fibre: K=a^4, L1=b+1, L2=a. Divide every exact image by a^4.
    for sa, sb in SECTORS:
        ea = 2 - sa
        eb = 2 - sb
        for total in range(cutoff + 1):
            for i in range(total + 1):
                j = total - i

                p_terms = {}
                if j:
                    for k in range(ea + 1):
                        monomial = (i + eb, j - 1 + k)
                        p_terms[monomial] = p_terms.get(monomial, 0) - j * comb(ea, k)
                if sa:
                    for k in range(ea):
                        monomial = (i + eb, j + k)
                        p_terms[monomial] = p_terms.get(monomial, 0) + comb(ea - 1, k)
                emit(p_terms)

                q_terms = {}
                if i:
                    for k in range(ea + 1):
                        monomial = (i - 1 + eb, j + k)
                        q_terms[monomial] = q_terms.get(monomial, 0) + i * comb(ea, k)
                for k in range(ea + 1):
                    monomial = (i + eb - 1, j + k)
                    q_terms[monomial] = q_terms.get(monomial, 0) - (sb + 6) * comb(ea, k)
                emit(q_terms)

    return monomials, position, rows


def rank(rows):
    basis = {}
    for source in rows:
        row = source[:]
        while True:
            pivot = next((i for i, value in enumerate(row) if value), None)
            if pivot is None:
                break
            if pivot in basis:
                factor = row[pivot]
                row = [(x - factor * y) % P for x, y in zip(row, basis[pivot])]
            else:
                inverse = pow(row[pivot], P - 2, P)
                basis[pivot] = [value * inverse % P for value in row]
                break
    return len(basis)


def multiplied_rows(monomials, position, rows, variable, cutoff):
    answer = []
    for row, degree in rows:
        if degree >= cutoff:
            continue
        product = [0] * len(monomials)
        for index, coefficient in enumerate(row):
            if coefficient:
                a_degree, b_degree = monomials[index]
                target = (a_degree + variable[0], b_degree + variable[1])
                product[position[target]] = coefficient
        answer.append(product)
    return answer


def main():
    results = []
    for cutoff in (12, 16, 20, 24, 28):
        monomials, position, graded_rows = exact_rows(cutoff)
        image = [row for row, _ in graded_rows]
        image_rank = rank(image)
        assert len(monomials) - image_rank == 2

        a_products = multiplied_rows(monomials, position, graded_rows, (1, 0), cutoff)
        b_products = multiplied_rows(monomials, position, graded_rows, (0, 1), cutoff)
        a_defect = rank(image + a_products) - image_rank
        b_defect = rank(image + b_products) - image_rank
        joint_defect = rank(image + a_products + b_products) - image_rank
        results.append((a_defect, b_defect, joint_defect))

    assert all(a_defect == b_defect == 1 for a_defect, b_defect, _ in results)
    assert len({joint for _, _, joint in results}) == 1
    joint = results[0][2]

    print("tested_factored_exact_cokernel_dimension: 2")
    print("tested_cutoffs: 12,16,20,24,28")
    print("naive_a_multiplication_preserves_exact_image: NO")
    print("naive_b_multiplication_preserves_exact_image: NO")
    print("a_multiplication_defect_rank_each_cutoff: 1")
    print("b_multiplication_defect_rank_each_cutoff: 1")
    print(f"joint_multiplication_defect_rank_each_cutoff: {joint}")
    print("length_two_resonance_as_naive_F[a,b]_module: NOT_DEFINED")
    print("required_replacement: CHAIN_LEVEL_HOMOTOPY_CORRECTED_OPERATORS")


if __name__ == "__main__":
    main()
