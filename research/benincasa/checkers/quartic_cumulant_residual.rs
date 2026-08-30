fn main() {
    let mut checks = 0usize;
    let mut positive = 0usize;
    let mut negative = 0usize;
    let mut zero = 0usize;

    for lambda in -3_i64..=3 {
        for q in 1_i64..=6 {
            for r in -5_i64..=5 {
                for kqqqq in -4_i64..=4 {
                    for kpqqq in -4_i64..=4 {
                        let residual_dqp = -4 * lambda * kqqqq;
                        let residual_dpp = -8 * lambda * kpqqq;
                        let determinant_derivative = q * residual_dpp - 2 * r * residual_dqp;
                        let formula = 8 * lambda * (r * kqqqq - q * kpqqq);
                        assert_eq!(determinant_derivative, formula);
                        match formula.cmp(&0) {
                            std::cmp::Ordering::Greater => positive += 1,
                            std::cmp::Ordering::Less => negative += 1,
                            std::cmp::Ordering::Equal => zero += 1,
                        }
                        checks += 1;
                    }
                }
            }
        }
    }

    assert!(positive > 0 && negative > 0 && zero > 0);
    println!("{{");
    println!("  \"schema\": \"marici.quartic_cumulant_residual.v1\",");
    println!("  \"exact_checks\": {checks},");
    println!("  \"positive_cases\": {positive},");
    println!("  \"negative_cases\": {negative},");
    println!("  \"zero_cases\": {zero},");
    println!("  \"residual_dV_qp\": \"-4 lambda kappa_qqqq\",");
    println!("  \"residual_dV_pp\": \"-8 lambda kappa_pqqq\",");
    println!("  \"uncertainty_derivative\": \"8 lambda (V_qp kappa_qqqq - V_qq kappa_pqqq)\",");
    println!("  \"sign_definite\": false");
    println!("}}");
}
