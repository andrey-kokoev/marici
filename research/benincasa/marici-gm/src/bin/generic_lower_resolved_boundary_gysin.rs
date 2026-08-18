const INTERSECTION: [[i64; 4]; 4] = [
    [-1, 0, 1, 1],
    [0, -1, 1, 1],
    [1, 1, -2, 0],
    [1, 1, 0, -2],
];

fn rank(mut matrix: Vec<Vec<i64>>) -> usize {
    let rows = matrix.len();
    let columns = matrix[0].len();
    let mut pivot_row = 0;
    for column in 0..columns {
        let Some(pivot) = (pivot_row..rows).find(|&row| matrix[row][column] != 0) else {
            continue;
        };
        matrix.swap(pivot_row, pivot);
        for row in 0..rows {
            if row == pivot_row || matrix[row][column] == 0 {
                continue;
            }
            let left = matrix[pivot_row][column];
            let right = matrix[row][column];
            for col in column..columns {
                matrix[row][col] = left * matrix[row][col] - right * matrix[pivot_row][col];
            }
            let gcd = matrix[row].iter().fold(0_i64, |g, value| gcd_i64(g, *value));
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

fn gcd_i64(mut left: i64, mut right: i64) -> i64 {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        (left, right) = (right, left % right);
    }
    left
}

fn main() {
    // Ordered boundary components: D_+, D_-, E_+, E_-.
    // D_\pm are strict transforms of the two sheets at infinity.  E_\pm are
    // the exceptional (-2)-curves over t=+1 and t=-1 respectively.
    assert_eq!(rank(INTERSECTION.iter().map(|row| row.to_vec()).collect()), 4);

    let vertices = 4_usize;
    let edges = 4_usize;
    let connected_components = 1_usize;
    let graph_h1 = edges - vertices + connected_components;
    assert_eq!(graph_h1, 1);
    let weight_packet_rank = vertices + graph_h1;
    assert_eq!(weight_packet_rank, 5);

    // On q_g1=0, the remaining finite walls have leading directions
    // q_g2: a-b=0 and q_g3: a+b=0.  Their closures therefore hit the two
    // nodes t=+1 and t=-1 and, after resolution, select E_+ and E_-.
    let pair_residue = [[0_i64, 0, 1, 0, 0], [0_i64, 0, 0, 1, 0]];
    assert_eq!(rank(pair_residue.iter().map(|row| row.to_vec()).collect()), 2);

    println!("boundary_basis=D_plus,D_minus,E_plus,E_minus,gamma");
    println!("boundary_dual_graph=K_2_2=CYCLE_4");
    println!("intersection_matrix_rank=4");
    println!("intersection_matrix_kernel=ZERO");
    println!("dual_graph_H1_rank=1");
    println!("resolved_weight_packet_rank=5");
    println!("q_g1_q_g2_pair_direction=t_plus_1");
    println!("q_g1_q_g3_pair_direction=t_minus_1");
    println!("pair_residue_matrix=[[0,0,1,0,0],[0,0,0,1,0]]");
    println!("rank_five_identification_with_twisted_de_Rham=REQUIRES_COMPARISON_MAP");
}
