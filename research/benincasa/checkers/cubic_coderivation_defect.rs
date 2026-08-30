fn binomial(n: usize, k: usize) -> i128 {
    let mut out = 1_i128;
    for i in 0..k { out = out * (n - i) as i128 / (i + 1) as i128; }
    out
}

fn main() {
    // Primitive coproduct Delta(q)=qL+qR. For force Dp=-q^n,
    // strict coderivation omits every mixed binomial term.
    let mut degree_checks = 0usize;
    let mut mixed_terms_checked = 0usize;
    for n in 2_usize..=20 {
        let mut full_sum = 0_i128;
        let mut endpoint_sum = 0_i128;
        let mut mixed_sum = 0_i128;
        for k in 0..=n {
            let coefficient = binomial(n, k);
            full_sum += coefficient;
            if k == 0 || k == n { endpoint_sum += coefficient; }
            else {
                mixed_sum += coefficient;
                mixed_terms_checked += 1;
            }
        }
        assert_eq!(full_sum, 1_i128 << n);
        assert_eq!(full_sum - endpoint_sum, mixed_sum);
        assert!(mixed_sum > 0);
        degree_checks += 1;
    }

    // Cubic potential gives quadratic force: the unique mixed term is
    // -2 qL qR.
    assert_eq!(binomial(2, 1), 2);

    println!("{{");
    println!("  \"schema\": \"marici.cubic_coderivation_defect.v1\",");
    println!("  \"nonlinear_force_degrees_checked\": {degree_checks},");
    println!("  \"mixed_terms_checked\": {mixed_terms_checked},");
    println!("  \"cubic_potential_defect\": \"-2 q_left tensor q_right\",");
    println!("  \"free_linear_derivation_is_coderivation\": true,");
    println!("  \"nonlinear_derivation_is_strict_coderivation\": false");
    println!("}}");
}
