from fractions import Fraction


def hostile_factor(real, imag):
    value = complex(float(real), float(imag))
    return value * value + 1


if __name__ == "__main__":
    seam_points = [Fraction(-3), Fraction(-1), Fraction(0), Fraction(2), Fraction(5)]
    for point in seam_points:
        h = point * point + 1
        original_transition = Fraction(1, 1)
        modified_transition = h / h
        assert modified_transition == original_transition
        assert h > 0

    assert abs(hostile_factor(0, 1)) == 0
    assert abs(hostile_factor(0, -1)) == 0

    print("original transition: 1")
    print("modified transition after common factor: 1")
    print("inserted off-seam zeros: +i and -i")
    print("result: descent transition does not determine section divisor")
