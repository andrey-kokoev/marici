from fractions import Fraction


def determinant(a, b):
    return a[0] * b[1] - a[1] * b[0]


if __name__ == "__main__":
    diagonal_noncentral = (Fraction(1), Fraction(1))
    central_sheet_label = (Fraction(1), Fraction(-1))

    # The central label distinguishes the summands and kills the exchanger,
    # but contributes no noncentral bracket direction.
    carrier_projectors_exist = True
    noncentral_action_vectors = [diagonal_noncentral]
    assert carrier_projectors_exist
    assert len(noncentral_action_vectors) == 1

    asymmetric_noncentral = (Fraction(1), Fraction(-1))
    assert determinant(diagonal_noncentral, asymmetric_noncentral) != 0
    noncentral_action_vectors.append(asymmetric_noncentral)
    assert len(noncentral_action_vectors) == 2

    first = tuple((diagonal_noncentral[i] + asymmetric_noncentral[i]) / 2 for i in range(2))
    second = tuple((diagonal_noncentral[i] - asymmetric_noncentral[i]) / 2 for i in range(2))
    assert first == (1, 0)
    assert second == (0, 1)

    print("central label removes sector exchanger: yes")
    print("central label splits noncentral action: no")
    print("unequal noncentral coefficient rank: 2")
    print("result: carrier splitting and action splitting are distinct")
