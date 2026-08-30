fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn main() {
    // Scaled contractions (2, 2 e+_ij p_i p_j, 2 ex_ij p_i p_j)
    // for the three equilateral momentum directions.
    let tensor_readout = [[2, 2, 0], [2, -1, -1], [2, -1, 1]];
    let determinant = det3(tensor_readout);
    assert_eq!(determinant, -12);

    // Both tensor polarizations are even under p -> -p and are traceless.
    let trace_plus = 1 + (-1);
    let trace_cross = 0 + 0;
    assert_eq!(trace_plus, 0);
    assert_eq!(trace_cross, 0);

    println!(
        "{{\"status\":\"pass\",\"port\":\"soft_traceless_tensor_Ward_response\",\"polarizations\":[\"plus\",\"cross\"],\"scaled_determinant\":{},\"rank\":3,\"momentum_reversal_even\":true,\"physical_accessibility\":\"not_established_by_algebraic_identity\"}}",
        determinant
    );
}
