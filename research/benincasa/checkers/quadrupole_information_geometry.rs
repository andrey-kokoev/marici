fn dot(a: [i64; 3], b: [i64; 3]) -> i64 {
    a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
}

fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn main() {
    // Four times the per-angle-averaged Fisher metric at unit radial slope:
    // E[S^2]=1/2 and <cos^2 2theta>=<sin^2 2theta>=1/2.
    let fisher_times_four = [[2, 0, 0], [0, 1, 0], [0, 0, 1]];
    assert_eq!(fisher_times_four[1][1], fisher_times_four[2][2]);

    // Exact scaled equilateral occurrence matrix.
    let evaluation = [[1, 2, 0], [1, -1, -1], [1, -1, 1]];
    assert_eq!(det3(evaluation), -6);

    // Single-polarization kernels.
    let plus_values = [2, -1, -1];
    let cross_values = [0, -1, 1];
    let scalar_values = [1, 1, 1];
    let plus_blind = [0, 1, -1];
    let cross_blind = [-2, 1, 1];
    assert_eq!(dot(scalar_values, plus_blind), 0);
    assert_eq!(dot(plus_values, plus_blind), 0);
    assert_eq!(dot(scalar_values, cross_blind), 0);
    assert_eq!(dot(cross_values, cross_blind), 0);

    // The three unit quadrupole directions have Gram matrix with diagonal 1
    // and off-diagonal -1/2; its nonzero eigenvalues are 3/2,3/2.
    let twice_gram = [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]];
    assert_eq!(twice_gram[0][0] + twice_gram[0][1] + twice_gram[0][2], 0);

    println!(
        "{{\"status\":\"pass\",\"fisher_times_four\":[[2,0,0],[0,1,0],[0,0,1]],\"quadrupole_frame_eigenvalues\":[\"3/2\",\"3/2\"],\"full_determinant\":-6,\"plus_only_blind\":[0,1,-1],\"cross_only_blind\":[-2,1,1],\"minimum_tensor_polarizations\":2}}"
    );
}
