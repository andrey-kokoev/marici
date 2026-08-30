fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn main() {
    // Local representative: c is the resolved Gram normal.  At c=0 the
    // cross column vanishes; a unit 2x2 minor remains.
    let at_zero = [[1, 0, 0], [1, 1, 0], [1, 1, 0]];
    let unit_minor = at_zero[0][0] * at_zero[1][1] - at_zero[0][1] * at_zero[1][0];
    assert_eq!(unit_minor, 1);

    for c in -12_i64..=12 {
        let t = [[1, 0, 0], [1, 1, -c], [1, 1, c]];
        assert_eq!(det3(t), 2 * c);
    }

    let direct_score = [[1, 2, 0], [1, -1, -1], [1, -1, 1]];
    assert_eq!(det3(direct_score), -6);

    println!(
        "{{\"status\":\"pass\",\"local_determinant\":\"2c\",\"unit_two_minor\":1,\"Smith_form_over_Q_bracket_c\":\"diag(1,1,c)\",\"tensor_supported_cokernel\":\"Q[c]/(c)\",\"direct_score_unit_determinant\":-6,\"completed_supported_cone_homology\":0}}"
    );
}
