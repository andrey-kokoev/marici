"""Audit separation of Cartier filtration from the PC face-circle grading."""

from math import comb


def main():
    face_counts_after_endpoints = [1, 9, 21, 12]
    target = [[0 for _ in range(4)] for _ in range(4)]
    for face_size, count in enumerate(face_counts_after_endpoints):
        for circle_size in range(face_size + 1):
            degree = 3 - face_size + circle_size
            target[degree][circle_size] += count * comb(face_size, circle_size)
    assert target == [
        [12, 0, 0, 0],
        [21, 36, 0, 0],
        [9, 42, 36, 0],
        [1, 9, 21, 12],
    ]
    assert [sum(row) for row in target] == [12, 57, 87, 43]

    carrier = [1, 3, 3, 1]
    cartier = [1, 3, 3, 1]
    source = [[carrier[degree] * rank for rank in cartier] for degree in range(4)]
    assert source == [
        [1, 3, 3, 1],
        [3, 9, 9, 3],
        [3, 9, 9, 3],
        [1, 3, 3, 1],
    ]

    failed_bidegrees = [
        (degree, filtration)
        for degree in range(4)
        for filtration in range(4)
        if source[degree][filtration] > target[degree][filtration]
    ]
    assert failed_bidegrees == [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3),
    ]

    # An independent coefficient packet supplies all four Cartier levels over
    # every target generator without changing cellular degree.
    coefficientwise_target = [
        [sum(target[degree]) * rank for rank in cartier]
        for degree in range(4)
    ]
    assert all(
        source[degree][filtration] <= coefficientwise_target[degree][filtration]
        for degree in range(4)
        for filtration in range(4)
    )

    print("face_circle_bidegrees:")
    for degree, row in enumerate(target):
        print(f"  degree_{degree}: {','.join(map(str, row))}")
    print("failed_literal_identifications: (0,1),(0,2),(0,3),(1,2),(1,3),(2,3)")
    print("Cartier_equals_face_circle: FALSE")
    print("coefficientwise_Rees_packet_capacity: PASS")
    print("required_target_type: PC_Cech_OBJECT_WITH_EXTERNAL_CARTIER_COEFFICIENTS")
    print("graph_Cartier_comparison: STILL_REQUIRED")


if __name__ == "__main__":
    main()
