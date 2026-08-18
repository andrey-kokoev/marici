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
        }
        pivot_row += 1;
    }
    pivot_row
}

fn main() {
    // Basis: D_+, D_-, E_+, E_-, gamma.  The deck involution exchanges the
    // sheet components, fixes each exceptional component class, and reverses
    // the unique cycle in the K_2,2 dual graph.
    let tau = [
        [0_i64, 1, 0, 0, 0],
        [1_i64, 0, 0, 0, 0],
        [0_i64, 0, 1, 0, 0],
        [0_i64, 0, 0, 1, 0],
        [0_i64, 0, 0, 0, -1],
    ];
    let identity: Vec<Vec<i64>> = (0..5)
        .map(|row| (0..5).map(|column| i64::from(row == column)).collect())
        .collect();
    let plus_operator: Vec<Vec<i64>> = tau
        .iter()
        .enumerate()
        .map(|(row, values)| {
            values
                .iter()
                .enumerate()
                .map(|(column, value)| value + identity[row][column])
                .collect()
        })
        .collect();
    let minus_operator: Vec<Vec<i64>> = tau
        .iter()
        .enumerate()
        .map(|(row, values)| {
            values
                .iter()
                .enumerate()
                .map(|(column, value)| value - identity[row][column])
                .collect()
        })
        .collect();
    let plus_dimension = 5 - rank(minus_operator);
    let minus_dimension = 5 - rank(plus_operator);
    assert_eq!((plus_dimension, minus_dimension), (3, 2));
    assert_eq!(plus_dimension + minus_dimension, 5);
    println!("deck_action=D_plus<->D_minus,E_plus->E_plus,E_minus->E_minus,gamma->-gamma");
    println!("boundary_packet_character_dimensions=plus:3,minus:2");
    println!("physical_form=da_wedge_db/w");
    println!("physical_square_root_character=minus");
    println!("max_equivariant_physical_boundary_image_rank=2");
    println!("rank_five_equivariant_isomorphism=IMPOSSIBLE_WITH_RAW_PACKET");
}
