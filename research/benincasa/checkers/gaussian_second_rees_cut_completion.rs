fn main() {
    // First-order state: |00> + eps*a|20> + eps*b|11>.
    // For the observed first mode, beta_1=<aa>/eps=sqrt(2)*a and
    // n_2=<a^dagger a>/eps^2=2a^2+b^2.
    let samples = [(3_i64, 4_i64), (5, 12), (8, 15), (7, 0)];
    for (a, b) in samples {
        let beta_norm_squared = 2 * a * a;
        let occupation_second_grade = 2 * a * a + b * b;
        let uncertainty_second_grade = occupation_second_grade - beta_norm_squared;
        assert_eq!(uncertainty_second_grade, b * b);
        assert!(uncertainty_second_grade >= 0);
    }
    println!("{{");
    println!("  \"schema\": \"marici.gaussian_second_rees_cut_completion.v1\",");
    println!("  \"first_order_state\": \"|00>+eps*a|20>+eps*b|11>\",");
    println!("  \"bogoliubov_norm_squared\": \"2a^2\",");
    println!("  \"occupation_second_grade\": \"2a^2+b^2\",");
    println!("  \"uncertainty_second_grade\": \"b^2\",");
    println!("  \"cut_completion_nonnegative\": true");
    println!("}}");
}
