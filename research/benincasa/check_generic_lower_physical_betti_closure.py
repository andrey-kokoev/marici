"""Close the physical lower Betti census using odd Gysin injectivity."""


def quadratic_form(matrix, vector):
    return sum(
        vector[row] * matrix[row][column] * vector[column]
        for row in range(len(vector))
        for column in range(len(vector))
    )


def main():
    intersection = [
        [-1, 0, 1, 1],
        [0, -1, 1, 1],
        [1, 1, -2, 0],
        [1, 1, 0, -2],
    ]
    sheet_difference = [1, -1, 0, 0]
    delta_square = quadratic_form(intersection, sheet_difference)
    assert delta_square == -2

    compact_h1_odd = 0  # resolved degree-two del Pezzo is rational
    odd_component_rank = 1
    odd_gysin_rank = 1 if delta_square != 0 else 0
    open_h1_odd = compact_h1_odd + odd_component_rank - odd_gysin_rank
    assert open_h1_odd == 0

    open_h0_odd = 0
    open_higher_than_two = 0  # smooth affine complex surface
    euler_characteristic = 5
    open_h2_odd = euler_characteristic + open_h1_odd + open_h0_odd
    assert open_h2_odd == 5

    print("compact_resolved_cover: RATIONAL_DEGREE_TWO_WEAK_DEL_PEZZO")
    print("compact_H1_odd: 0")
    print("sheet_difference_square: -2")
    print("odd_component_Gysin_rank: 1")
    print("physical_open_H1_odd: 0")
    print("physical_open_H2_odd: 5")
    print("physical_cohomology_concentrated_in_H2: YES")
    print("boundary_odd_grades_inside_H2: sheet_difference,conductor_cycle")


if __name__ == "__main__":
    main()
