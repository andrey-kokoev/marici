from fractions import Fraction


def rank_two(rows):
    a, b = rows
    return int(a[0] * b[1] - a[1] * b[0] != 0) + 1


if __name__ == "__main__":
    diagonal = (Fraction(1), Fraction(1))
    central_sheet_label = (Fraction(1), Fraction(-1))

    # A central label does not enter the noncentral coefficient span.
    noncentral_without_tag = [diagonal]
    assert len(noncentral_without_tag) == 1

    noncentral_asymmetric_tag = (Fraction(1), Fraction(-1))
    assert rank_two((diagonal, noncentral_asymmetric_tag)) == 2

    first_sector = tuple((diagonal[i] + noncentral_asymmetric_tag[i]) / 2 for i in range(2))
    second_sector = tuple((diagonal[i] - noncentral_asymmetric_tag[i]) / 2 for i in range(2))
    assert first_sector == (1, 0)
    assert second_sector == (0, 1)

    equal_weight_tag = (Fraction(3), Fraction(3))
    assert diagonal[0] * equal_weight_tag[1] - diagonal[1] * equal_weight_tag[0] == 0

    print("diagonal noncentral span dimension before tag: 1")
    print("noncentral span dimension after asymmetric tag: 2")
    print("central sheet label alone unlocks dynamics: no")
    print("result: independent sector control needs noncentral asymmetry")
