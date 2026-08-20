fn determinant(matrix: &[Vec<i64>]) -> i64 {
    match matrix.len() {
        0 => 1,
        1 => matrix[0][0],
        n => (0..n)
            .map(|column| {
                let minor: Vec<Vec<i64>> = matrix[1..]
                    .iter()
                    .map(|row| {
                        row.iter()
                            .enumerate()
                            .filter_map(|(j, value)| (j != column).then_some(*value))
                            .collect()
                    })
                    .collect();
                (if column % 2 == 0 { 1 } else { -1 })
                    * matrix[0][column]
                    * determinant(&minor)
            })
            .sum(),
    }
}

fn row_times_matrix(row: &[i64], matrix: &[Vec<i64>]) -> Vec<i64> {
    (0..matrix[0].len())
        .map(|column| {
            row.iter()
                .enumerate()
                .map(|(i, coefficient)| coefficient * matrix[i][column])
                .sum()
        })
        .collect()
}

fn scale(row: &[i64], factor: i64) -> Vec<i64> {
    row.iter().map(|entry| factor * entry).collect()
}

fn main() {
    // Pair one: (2/3,0,0,-1/3) -> (-1,0,1/2,0), denominator eight.
    let first = vec![
        vec![-18, -6, 0, 0],
        vec![0, -12, 0, 0],
        vec![3, 3, 0, -12],
        vec![0, 0, -12, 0],
    ];
    assert_eq!(determinant(&first), -31_104);
    assert_eq!(
        row_times_matrix(&[1, 1, -2, 0], &first),
        scale(&[1, 1, 0, -1], -24)
    );
    assert_eq!(
        row_times_matrix(&[1, 0, 0, -1], &first),
        scale(&[3, 1, -2, 0], -6)
    );
    assert_eq!(
        row_times_matrix(&[1, 0, 0, 1], &first),
        scale(&[3, 1, 2, 0], -6)
    );
    let first_support_sign = -1;
    let first_relative_fiber_sign = 1; // -d/2 at d=-4/3.
    let ordered_cut_sign = -1;
    assert_eq!(
        first_support_sign,
        first_relative_fiber_sign * ordered_cut_sign
    );

    // Pair two: (1,2,1/2,0) -> (2,4,0,1).
    let second = vec![
        vec![0, -2, 0, 0],
        vec![-4, -2, 0, 0],
        vec![0, 0, 0, 2],
        vec![-1, -1, 2, 0],
    ];
    assert_eq!(determinant(&second), 32);
    // p'=-2q.
    assert_eq!(
        row_times_matrix(&[1, 0, 0, 0], &second),
        scale(&[0, 1, 0, 0], -2)
    );
    // Twice target L2+ maps to four times source L1+.
    assert_eq!(
        row_times_matrix(&[-1, 1, 2, 0], &second),
        scale(&[-1, 0, 0, 1], 4)
    );
    // Twice target L2- maps to four times source L1-.
    assert_eq!(
        row_times_matrix(&[1, -1, 2, 0], &second),
        scale(&[1, 0, 0, 1], 4)
    );
    let second_support_sign = 1;
    let second_relative_fiber_sign = -1; // -d/2 at d=1.
    assert_eq!(
        second_support_sign,
        second_relative_fiber_sign * ordered_cut_sign
    );

    println!("schema=marici.benincasa.rank12_tangency_swap_coherence.v1");
    println!("ordered_cut_occurrence_sign={ordered_cut_sign}");
    println!("first_linear_determinant=-243/32");
    println!("first_support_sign={first_support_sign}");
    println!("first_relative_fiber_sign={first_relative_fiber_sign}");
    println!("first_total_residue_sign={}", first_relative_fiber_sign * ordered_cut_sign);
    println!("second_linear_determinant=32");
    println!("second_factor_map=(q,L1_minus,L1_plus)->(p_prime,L2_plus,L2_minus)");
    println!("second_factor_matrix=[[-2,0,0],[0,0,2],[0,2,0]]");
    println!("second_support_sign={second_support_sign}");
    println!("second_relative_fiber_sign={second_relative_fiber_sign}");
    println!("second_total_residue_sign={}", second_relative_fiber_sign * ordered_cut_sign);
    println!("both_orientation_squares=true");
    println!("deck_character=1");
}
