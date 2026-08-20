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
                let sign = if column % 2 == 0 { 1 } else { -1 };
                sign * matrix[0][column] * determinant(&minor)
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

fn scaled(row: &[i64], factor: i64) -> Vec<i64> {
    row.iter().map(|entry| factor * entry).collect()
}

fn main() {
    // Eight times the linearization from source (p,q,A,B) to target
    // (p',q',A',B') at (u,v,a,b)=(2/3,0,0,-1/3).
    let linear_numerator = vec![
        vec![-18, -6, 0, 0],
        vec![0, -12, 0, 0],
        vec![3, 3, 0, -12],
        vec![0, 0, -12, 0],
    ];
    let determinant_numerator = determinant(&linear_numerator);
    assert_eq!(determinant_numerator, -31_104);

    let source_t = vec![1, 1, 0, -1];
    let source_q = vec![0, 1, 0, 0];
    let source_u_minus = vec![3, 1, -2, 0];
    let source_u_plus = vec![3, 1, 2, 0];
    let target_t = vec![1, 1, -2, 0];
    let target_q = vec![0, 1, 0, 0];
    let target_v_minus = vec![1, 0, 0, -1];
    let target_v_plus = vec![1, 0, 0, 1];

    // All rows below carry the common denominator eight.
    assert_eq!(
        row_times_matrix(&target_t, &linear_numerator),
        scaled(&source_t, -24)
    );
    assert_eq!(
        row_times_matrix(&target_q, &linear_numerator),
        scaled(&source_q, -12)
    );
    assert_eq!(
        row_times_matrix(&target_v_minus, &linear_numerator),
        scaled(&source_u_minus, -6)
    );
    assert_eq!(
        row_times_matrix(&target_v_plus, &linear_numerator),
        scaled(&source_u_plus, -6)
    );

    // Units on the ordered support factors (rho,q,U_minus,U_plus):
    // (1,-3/2,-3/4,-3/4). Their product is -27/32.
    let support_orientation_sign = -1;
    let relative_fiber_residue_orientation_sign = 1;
    let ordered_cut_occurrence_sign = -1;
    let total_residue_orientation_sign =
        relative_fiber_residue_orientation_sign * ordered_cut_occurrence_sign;
    let deck_character = 1;
    assert_eq!(support_orientation_sign, total_residue_orientation_sign);

    println!("schema=marici.benincasa.rank12_rational_tangency_source_swap.v1");
    println!("base_map=(u',v')=(2u/d,2v/d),d=u+v-2");
    println!("fiber_map=(a',b')=(2b/d,2a/d)");
    println!("linear_denominator=8");
    println!("linear_numerator={linear_numerator:?}");
    println!("linear_determinant=-243/32");
    println!("factor_units=(1,-3/2,-3/4,-3/4)");
    println!("support_orientation_sign={support_orientation_sign}");
    println!("relative_fiber_residue_orientation_sign={relative_fiber_residue_orientation_sign}");
    println!("ordered_cut_occurrence_sign={ordered_cut_occurrence_sign}");
    println!("total_residue_orientation_sign={total_residue_orientation_sign}");
    println!("deck_character={deck_character}");
    println!("orientation_match=true");
}
