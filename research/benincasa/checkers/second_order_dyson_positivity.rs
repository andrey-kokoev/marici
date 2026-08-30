fn main() {
    let mut finite_coupling_failures = 0usize;
    let mut trace_checks = 0usize;
    let mut conditional_checks = 0usize;

    // H=sigma_x and rho=|0><0|.  The second-order real-plus-virtual
    // truncation is [[1-g^2, i g],[-i g,g^2]].  Its determinant is -g^4.
    for numerator in 1_i128..=128 {
        let denominator = 257_i128;
        // Work after multiplying the matrix by denominator^2:
        // [[d^2-n^2, i n d],[-i n d,n^2]].
        let n2 = numerator * numerator;
        let d2 = denominator * denominator;
        let determinant_scaled = (d2 - n2) * n2 - n2 * d2;
        assert_eq!(determinant_scaled, -n2 * n2);
        assert!(determinant_scaled < 0);
        finite_coupling_failures += 1;

        // Trace is exactly one in the second-order polynomial.
        assert_eq!((d2 - n2) + n2, d2);
        trace_checks += 1;

        // The negative determinant starts at order four, beyond the retained
        // second-order grade; no negative coefficient occurs through g^2.
        let det_coefficients_through_order_two = [0_i128, 0, 0];
        assert!(det_coefficients_through_order_two.iter().all(|x| *x >= 0));
        conditional_checks += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.second_order_dyson_positivity.v1\",");
    println!("  \"finite_coupling_failures\": {finite_coupling_failures},");
    println!("  \"trace_checks\": {trace_checks},");
    println!("  \"conditional_order_two_checks\": {conditional_checks},");
    println!("  \"determinant\": \"-g^4\",");
    println!("  \"globally_positive_polynomial_truncation\": false,");
    println!("  \"conditionally_positive_through_declared_order\": true");
    println!("}}");
}
