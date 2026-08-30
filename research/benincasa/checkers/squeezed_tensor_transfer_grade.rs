fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn main() {
    // The leading squeezed tensor Ward operator on radial P(k) is
    // -(d log P / d log k) e^s_ij khat_i khat_j.
    let angular = [[2, 2, 0], [2, -1, -1], [2, -1, 1]];
    let det = det3(angular);
    assert_eq!(det, -12);

    // Representative nonzero spectral slopes, including scale-invariant
    // three-dimensional P(k) proportional to k^-3.
    let slopes = [-3_i64, -2, 1];
    assert!(slopes.iter().all(|n| *n != 0));

    println!(
        "{{\"status\":\"pass\",\"grade\":\"leading_squeezed_tensor_Ward\",\"transfer_coefficient\":\"-d_log_P/d_log_k\",\"scaled_angular_determinant\":{},\"rank_when_slope_nonzero\":3,\"failure_locus\":\"d_log_P/d_log_k=0\",\"finite_q_transfer\":\"not_tested\"}}",
        det
    );
}
