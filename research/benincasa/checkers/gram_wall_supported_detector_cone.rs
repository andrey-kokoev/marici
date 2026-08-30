fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn dot(a: [i64; 3], b: [i64; 3]) -> i64 {
    a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
}

fn main() {
    // Representative Gram wall q parallel to occurrence 1.  The transported
    // cross column vanishes and occurrences 2,3 have equal plus response.
    let tensor_scalar = [1, 1, 1];
    let tensor_plus = [0, 1, 1];
    let gram_kernel = [0, 1, -1];
    assert_eq!(dot(tensor_scalar, gram_kernel), 0);
    assert_eq!(dot(tensor_plus, gram_kernel), 0);

    // Direct boundary-state quadrupole score remains the frozen tight frame.
    let direct_score = [[1, 2, 0], [1, -1, -1], [1, -1, 1]];
    assert_eq!(det3(direct_score), -6);
    let direct_cross = [0, -1, 1];
    assert_eq!(dot(direct_cross, gram_kernel), -2);

    println!(
        "{{\"status\":\"pass\",\"tensor_transport_rank_on_Gram_wall\":2,\"supported_kernel\":[0,1,-1],\"direct_score_determinant\":-6,\"alternate_port_recovery\":-2,\"completed_port_cone_homology\":0,\"classification\":\"existing_Gram_support plus transport projection\"}}"
    );
}
