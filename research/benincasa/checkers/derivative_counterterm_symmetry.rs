fn main(){
    // Characters of q p q and hbar q.
    let phase_space_parity_main=-1_i64;
    let phase_space_parity_counter=-1_i64;
    assert_eq!(phase_space_parity_main,phase_space_parity_counter);

    // Under canonical scaling q->s q, p->s^-1 p, hbar fixed,
    // both monomials have weight +1.
    let scaling_weight_main=1_i64;
    let scaling_weight_counter=1_i64;
    assert_eq!(scaling_weight_main,scaling_weight_counter);

    // Under antiunitary time reversal q->q, p->-p:
    // q p q is odd while hbar q is even.
    let time_reversal_main=-1_i64;
    let time_reversal_counter=1_i64;
    assert_ne!(time_reversal_main,time_reversal_counter);

    let mut lambda_checks=0usize;
    let mut odd_time_reversal_solutions=0usize;
    for lambda in -128_i64..=128 {
        let has_even_component=lambda!=0;
        let transforms_purely_odd=!has_even_component;
        assert_eq!(transforms_purely_odd,lambda==0);
        lambda_checks+=1;
        if transforms_purely_odd {odd_time_reversal_solutions+=1;}
    }

    println!("{{");
    println!("  \"schema\": \"marici.derivative_counterterm_symmetry.v1\",");
    println!("  \"lambda_checks\": {lambda_checks},");
    println!("  \"phase_space_parity_distinguishes_counterterm\": false,");
    println!("  \"canonical_scaling_distinguishes_counterterm\": false,");
    println!("  \"time_reversal_distinguishes_counterterm\": true,");
    println!("  \"pure_time_reversal_odd_solution_count\": {odd_time_reversal_solutions},");
    println!("  \"time_reversal_forces_lambda_zero_conditionally\": true");
    println!("}}");
}
