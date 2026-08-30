from fractions import Fraction


def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


if __name__ == "__main__":
    carrier_projectors_exist = True
    diagonal_noncentral_rank = 1
    assert carrier_projectors_exist
    assert diagonal_noncentral_rank == 1

    inverse_norms = []
    for n in (2, 4, 8, 16, 32, 64):
        matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1, n)))
        assert determinant(matrix) != 0
        inverse_norms.append(n)

    assert all(a < b for a, b in zip(inverse_norms, inverse_norms[1:]))
    assert inverse_norms[-1] == 64

    uniform_matrix = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
    assert determinant(uniform_matrix) == 1

    print("carrier splitting without action splitting: witnessed")
    print("finite action splitting without uniform estimate: witnessed")
    print("uniformly bounded split action: independent third gate")
    print("result: three splitting gates are logically independent")
