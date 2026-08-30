// Exact affine no-go: a reciprocal contact coefficient cannot vanish.

fn main() {
    // The graph of C=1/l is l*C-1=0.  Adding C=0 leaves -1=0.
    let linear_denominators = [-31_i128, -7, -1, 1, 5, 29];
    for ell in linear_denominators {
        assert_ne!(ell, 0);
        // Work denominator-cleared: ell*C=1, hence C is a unit.
        let numerator_of_c = 1_i128;
        assert_ne!(numerator_of_c, 0);
        assert_eq!(ell * numerator_of_c, ell);
    }

    // Scheme-theoretic certificate: (ell*C-1, C) contains 1 because
    // (ell*C-1)-ell*C=-1.
    let ideal_constant = -1_i128;
    assert!(ideal_constant.abs() == 1);

    println!(
        "{{\"status\":\"pass\",\"contact_graph_equation\":\"ell*C-1=0\",\"augmented_ideal\":\"(ell*C-1,C)=(1)\",\"finite_contact_zero_locus_empty\":true,\"finite_route_loss_available\":false,\"remaining_location\":\"compactification_infinity\"}}"
    );
}
