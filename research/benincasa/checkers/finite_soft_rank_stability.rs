fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn main() {
    let t0 = [[2, 2, 0], [2, -1, -1], [2, -1, 1]];
    assert_eq!(det3(t0), -12);

    // adj(T0); T0^{-1}=adj(T0)/det(T0).
    let adj = [[-2_i64, -2, -2], [-4, 2, 2], [0, 6, -6]];
    let max_row_sum = adj
        .iter()
        .map(|row| row.iter().map(|x| x.abs()).sum::<i64>())
        .max()
        .unwrap();
    assert_eq!(max_row_sum, 12);
    assert_eq!(max_row_sum, det3(t0).abs());

    println!(
        "{{\"status\":\"pass\",\"det_T0\":-12,\"inverse_infinity_norm\":1,\"sufficient_stability_condition\":\"norm_infinity(Delta)<1 after source normalization\",\"conclusion\":\"open finite-soft rank-three neighborhood\",\"assumption\":\"analytic_or_continuous_source_transfer\"}}"
    );
}
