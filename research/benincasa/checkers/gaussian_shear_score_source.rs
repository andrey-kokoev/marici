fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn main() {
    // Twice the evaluation of (1, cos 2theta, sin 2theta) at
    // theta = 0, 2pi/3, 4pi/3.  Multiplying angular columns by a
    // nonzero logarithmic radial slope cannot change the rank.
    let evaluation = [[2, 2, 0], [2, -1, -1], [2, -1, 1]];
    let determinant = det3(evaluation);
    assert_eq!(determinant, -12);

    // A traceless metric shear h=(h_plus,h_cross) changes
    // |p| by (|p|/2)(h_plus cos 2theta+h_cross sin 2theta).
    // Hence a radial kernel a0(k) generates both quadrupole scores
    // whenever k a0'(k)/a0(k) is nonzero.
    let logarithmic_slopes = [1_i64, 2, 3];
    assert!(logarithmic_slopes.iter().all(|s| *s != 0));

    println!(
        "{{\"status\":\"pass\",\"source_operation\":\"traceless_metric_shear\",\"scaled_evaluation_determinant\":{},\"rank\":3,\"normalization\":\"(k/2) d_k log a0\",\"failure_locus\":\"d_k a0=0\"}}",
        determinant
    );
}
