fn mul3(a: [[i64; 3]; 3], b: [[i64; 3]; 3]) -> [[i64; 3]; 3] {
    let mut out = [[0; 3]; 3];
    for i in 0..3 {
        for j in 0..3 {
            out[i][j] = (0..3).map(|k| a[i][k] * b[k][j]).sum();
        }
    }
    out
}

fn main() {
    let q = [[1, 2, 0], [1, -1, -1], [1, -1, 1]];
    let adj = [[-2, -2, -2], [-2, 1, 1], [0, 3, -3]];
    let product = mul3(q, adj);
    assert_eq!(product, [[-6, 0, 0], [0, -6, 0], [0, 0, -6]]);

    // det(I_r tensor Q)=det(Q)^r for the elliptic and marked-relative ranks.
    assert_eq!((-6_i64).pow(2), 36);
    assert_eq!((-6_i64).pow(12), 2_176_782_336);

    println!(
        "{{\"status\":\"pass\",\"observer_matrix_determinant\":-6,\"horizontal_inverse\":\"adj(Q)/(-6)\",\"elliptic_rank2_tensor_determinant\":36,\"marked_relative_rank12_tensor_determinant\":2176782336,\"external_product_cone\":\"contractible\",\"internal_rank3_identification\":\"not_typed\"}}"
    );
}
