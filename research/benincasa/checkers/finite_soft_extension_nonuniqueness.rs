fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn matrix_b(q: i64) -> [[i64; 3]; 3] {
    let f = 1 - q * q;
    [[2, 2 * f, 0], [2, -f, -f], [2, -f, f]]
}

fn main() {
    let t0 = [[2, 2, 0], [2, -1, -1], [2, -1, 1]];
    assert_eq!(matrix_b(0), t0);
    assert_eq!(det3(t0), -12);
    assert_eq!(det3(matrix_b(1)), 0);

    // det(T_B(q)) = -12(1-q^2)^2.  The value and first q derivative at
    // q=0 agree with the constant extension, but finite-q rank does not.
    for q in [-3_i64, -2, 0, 2, 3] {
        let f = 1 - q * q;
        assert_eq!(det3(matrix_b(q)), -12 * f * f);
    }

    println!(
        "{{\"status\":\"pass\",\"extension_A_determinant\":\"-12\",\"extension_B_determinant\":\"-12(1-q^2)^2\",\"same_soft_value\":true,\"same_first_soft_jet\":true,\"B_rank_loss\":[\"q=1\",\"q=-1\"],\"conclusion\":\"leading Ward data do not determine finite-q support\"}}"
    );
}
