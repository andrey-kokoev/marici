from fractions import Fraction


def schur_numerator(a, d, v, spectral):
    return (a - spectral) * (d - spectral) - v * v


if __name__ == "__main__":
    a = Fraction(2)
    d = Fraction(5)
    v = Fraction(3)

    # D has a pole at spectral=a because its numerator does not vanish there.
    numerator_at_pole = schur_numerator(a, d, v, a)
    assert numerator_at_pole == -v * v
    assert numerator_at_pole != 0

    # The background factor cancels the denominator exactly.
    for spectral in (Fraction(-1), Fraction(0), Fraction(1), Fraction(3), Fraction(7)):
        schur = Fraction(d - spectral) - Fraction(v * v, a - spectral)
        full_from_schur = (a - spectral) * schur
        full_direct = schur_numerator(a, d, v, spectral)
        assert full_from_schur == full_direct

    discriminant = (a - d) * (a - d) + 4 * v * v
    assert discriminant > 0

    print("Schur pole at principal eigenvalue: present")
    print("background determinant cancels pole: exact")
    print("full self-adjoint characteristic roots real: discriminant positive")
    print("result: entire bridge requires full or relative determinant bookkeeping")
