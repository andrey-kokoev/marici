fn rank(mut matrix: Vec<Vec<i64>>) -> usize {
    let mut pivot_row = 0;
    for column in 0..matrix[0].len() {
        let Some(pivot) = (pivot_row..matrix.len()).find(|&row| matrix[row][column] != 0) else {
            continue;
        };
        matrix.swap(pivot_row, pivot);
        for row in 0..matrix.len() {
            if row == pivot_row || matrix[row][column] == 0 {
                continue;
            }
            let a = matrix[pivot_row][column];
            let b = matrix[row][column];
            for col in column..matrix[row].len() {
                matrix[row][col] = a * matrix[row][col] - b * matrix[pivot_row][col];
            }
            let gcd = matrix[row].iter().fold(0_i64, |g, x| gcd_i64(g, *x));
            if gcd > 1 {
                for value in &mut matrix[row] {
                    *value /= gcd;
                }
            }
        }
        pivot_row += 1;
    }
    pivot_row
}

fn gcd_i64(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn main() {
    // Columns: D_+, D_-, E_+, E_-, gamma.
    let valuation_and_pair = vec![
        vec![-4, -4, -2, -2, 0],
        vec![-1, -1, 0, -1, 0],
        vec![-1, -1, -1, 0, 0],
        vec![0, 0, 1, 0, 0],
        vec![0, 0, 0, 1, 0],
    ];
    assert_eq!(rank(valuation_and_pair.clone()), 3);

    // The normalization Čech boundary compares the two deck sheets.
    let normalization_transition = vec![1, -1, 0, 0, 0];
    // The conductor trace evaluates the unique oriented graph cycle.
    let conductor_trace = vec![0, 0, 0, 0, 1];

    let mut with_normalization = valuation_and_pair.clone();
    with_normalization.push(normalization_transition.clone());
    assert_eq!(rank(with_normalization.clone()), 4);
    let mut completed = with_normalization;
    completed.push(conductor_trace.clone());
    assert_eq!(rank(completed), 5);

    println!("valuation_and_pair_rank=3");
    println!("normalization_transition_row=[1,-1,0,0,0]");
    println!("rank_after_normalization=4");
    println!("conductor_trace_row=[0,0,0,0,1]");
    println!("rank_after_conductor=5");
    println!("boundary_coordinate_detection=COMPLETE");
    println!("source_to_boundary_chain_map=NOT_YET_CONSTRUCTED");
}
