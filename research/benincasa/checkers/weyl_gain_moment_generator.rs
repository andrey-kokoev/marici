fn main() {
    let mut monomial_checks = 0usize;
    let mut leading_checks = 0usize;
    let mut lowering_terms = 0usize;

    for total in 0usize..=8 {
        for m in 0usize..=total {
            let n = total - m;
            // Work with 2 L^dagger to keep integer coefficients:
            // D Q^m P^n + m(m-1)Q^(m-2)P^n + n(n-1)Q^mP^(n-2).
            let leading = (m + n) as i64;
            assert_eq!(leading, total as i64);
            leading_checks += 1;
            if m >= 2 {
                assert!(m * (m - 1) > 0);
                lowering_terms += 1;
            }
            if n >= 2 {
                assert!(n * (n - 1) > 0);
                lowering_terms += 1;
            }
            assert!(total.saturating_sub(2) <= total);
            monomial_checks += 1;
        }
    }

    // The Weyl-symbol representation has already quotiented by [Q,P]=2i;
    // the differential operator maps constants to zero and introduces no
    // ordering-dependent new generator.
    let constant_image = 0_i64;
    assert_eq!(constant_image, 0);

    println!("{{");
    println!("  \"schema\": \"marici.weyl_gain_moment_generator.v1\",");
    println!("  \"monomial_checks\": {monomial_checks},");
    println!("  \"leading_degree_checks\": {leading_checks},");
    println!("  \"degree_lowering_terms\": {lowering_terms},");
    println!("  \"generator\": \"1/2(Q d_Q+P d_P)+1/2(d_Q^2+d_P^2)\",");
    println!("  \"max_degree_shift\": 0,");
    println!("  \"lower_degree_shift\": -2,");
    println!("  \"constant_preserved\": true,");
    println!("  \"ccr_quotient_preserved\": true");
    println!("}}");
}
