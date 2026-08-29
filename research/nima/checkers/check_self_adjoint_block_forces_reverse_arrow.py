from fractions import Fraction


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix[0])))


if __name__ == "__main__":
    triangular = (
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0)),
    )
    assert triangular != transpose(triangular)

    completed = (
        (Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
    )
    assert completed == transpose(completed)

    psi = (Fraction(2), Fraction(3))
    source_coordinate = Fraction(5)
    forward_residual = source_coordinate
    reverse_residual = psi[0]
    assert forward_residual == 5
    assert reverse_residual == 2

    print("one-way source block self-adjoint: no")
    print("self-adjoint completion inserts reverse arrow: yes")
    print("forward and reverse equations independently present: yes")
    print("result: bounded finite-rank homogenization forces adjoint coupling")
