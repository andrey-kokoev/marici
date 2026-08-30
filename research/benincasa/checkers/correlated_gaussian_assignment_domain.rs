fn main() {
    let mut source_checks = 0usize;
    let mut vacuum_failures = 0usize;
    let mut compatibility_checks = 0usize;

    for a in 2_i64..=64 {
        // Standard pure two-mode-squeezed covariance has local variance a and
        // c^2=a^2-1. Ordinary positivity already requires x*a-c^2 >= 0
        // when replacing the observed block by x I while retaining c.
        let c_squared = a * a - 1;

        let source_schur_numerator = a * a - c_squared;
        assert_eq!(source_schur_numerator, 1);
        source_checks += 1;

        let vacuum_x = 1_i64;
        let vacuum_schur_numerator = vacuum_x * a - c_squared;
        assert!(vacuum_schur_numerator < 0);
        vacuum_failures += 1;

        // Integer x is compatible exactly when x*a >= c^2 at this ordinary
        // positivity gate.
        for x in 1_i64..=(a + 2) {
            let compatible = x * a >= c_squared;
            if compatible {
                assert!(x >= 2);
            }
            compatibility_checks += 1;
        }
    }

    println!("{{");
    println!("  \"schema\": \"marici.correlated_gaussian_assignment_domain.v1\",");
    println!("  \"source_covariance_checks\": {source_checks},");
    println!("  \"vacuum_assignment_failures\": {vacuum_failures},");
    println!("  \"compatibility_checks\": {compatibility_checks},");
    println!("  \"source_family\": \"a>=2, c^2=a^2-1\",");
    println!("  \"ordinary_compatibility_condition\": \"x a >= c^2\",");
    println!("  \"positive_assignment_on_all_observed_states\": false,");
    println!("  \"replacement\": \"compatibility-domain assignment/process tensor\"");
    println!("}}");
}
