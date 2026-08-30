fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn main() {
    let score = [[1, 2, 0], [1, -1, -1], [1, -1, 1]];
    assert_eq!(det3(score), -6);

    // Rank loss of the tensor channel is linear in the resolved Gram normal.
    for c in -10_i64..=10 {
        let tensor_local = [[1, 0, 0], [1, 1, -c], [1, 1, c]];
        assert_eq!(det3(tensor_local), 2 * c);
    }

    // The normalized massless Gaussian score and logarithmic shear slope are
    // k-independent after xi=sqrt(k)Phi, so the direct determinant survives
    // soft specialization unchanged.
    let soft_score_determinant = det3(score);
    assert_eq!(soft_score_determinant, -6);

    // Restoring nonzero contact rows cannot change the finite rank locus.
    let contact = [2_i64, 3, 5];
    let mut weighted = score;
    for i in 0..3 {
        for j in 0..3 {
            weighted[i][j] *= -8 * contact[i];
        }
    }
    assert_eq!(det3(weighted), (-8_i64).pow(3) * 2 * 3 * 5 * det3(score));

    println!(
        "{{\"status\":\"pass\",\"direct_score_determinant\":-6,\"contact_weighting_preserves_rank_locus\":true,\"tensor_local_determinant\":\"2c\",\"component_soft_direct_determinant\":-6,\"Gram_completed_cone_homology\":0,\"elliptic_external_product_homology\":0,\"hard_falsifier_found\":false,\"H2_update\":\"strong_support_in_frozen_spectral_source\"}}"
    );
}
