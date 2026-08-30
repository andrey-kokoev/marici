fn main() {
    let mut admissible_covariances = 0usize;
    let mut naive_failures = 0usize;
    let mut conditional_matches = 0usize;
    let mut reverse_order_matches = 0usize;

    for nu3 in 1_i128..=32 {
        for nu4 in 1_i128..=32 {
            for kappa in -16_i128..=16 {
                if kappa * kappa >= nu3 * nu4 { continue; }
                admissible_covariances += 1;

                // Joint centered Gaussian Wick theorem.
                let joint_fourth = nu3 * nu4 + 2 * kappa * kappa;
                let naive_marginal_product = nu3 * nu4;
                if kappa != 0 {
                    assert_ne!(joint_fourth, naive_marginal_product);
                    assert_eq!(joint_fourth - naive_marginal_product, 2 * kappa * kappa);
                    naive_failures += 1;
                }

                // Condition q4 on q3:
                // Var(q4|q3)=nu4-kappa^2/nu3,
                // E(q4|q3)=kappa q3/nu3.
                // Multiply by nu3 to keep the calculation integral.
                let conditional_numerator =
                    (nu3 * nu4 - kappa * kappa) * nu3
                    + 3 * kappa * kappa * nu3;
                assert_eq!(conditional_numerator, nu3 * joint_fourth);
                conditional_matches += 1;

                // Reverse conditioning gives the same joint moment.
                let reverse_numerator =
                    (nu4 * nu3 - kappa * kappa) * nu4
                    + 3 * kappa * kappa * nu4;
                assert_eq!(reverse_numerator, nu4 * joint_fourth);
                reverse_order_matches += 1;
            }
        }
    }

    println!("{{");
    println!("  \"schema\": \"marici.correlated_nested_cut_conditioning.v1\",");
    println!("  \"admissible_covariances\": {admissible_covariances},");
    println!("  \"nonzero_correlation_naive_failures\": {naive_failures},");
    println!("  \"conditional_matches\": {conditional_matches},");
    println!("  \"reverse_order_matches\": {reverse_order_matches},");
    println!("  \"naive_missing_term\": \"2 kappa^2\",");
    println!("  \"conditional_nested_pushforward_matches_joint\": true");
    println!("}}");
}
