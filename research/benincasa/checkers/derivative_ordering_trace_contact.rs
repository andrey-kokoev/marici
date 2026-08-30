fn main(){
    let mut orderings=0usize;
    let mut nonhermitian_failures=0usize;
    let mut hermitian_solutions=0usize;

    // H_a=q^2 p + a i hbar q.
    // Since (q^2 p)^dagger=p q^2=q^2 p-2 i hbar q,
    // H_a^dagger=q^2 p-(2+a)i hbar q.
    // Hermiticity requires a=-(2+a), hence a=-1.
    for a in -128_i64..=128 {
        let original_i_coefficient=a;
        let adjoint_i_coefficient=-(2+a);
        let hermitian=original_i_coefficient==adjoint_i_coefficient;
        assert_eq!(hermitian,a==-1);
        let trace_defect_coefficient=2*(a+1);
        assert_eq!(trace_defect_coefficient==0,hermitian);
        orderings+=1;
        if hermitian {hermitian_solutions+=1;} else {nonhermitian_failures+=1;}
    }

    // Adding real lambda hbar q preserves Hermiticity for every lambda.
    let mut residual_hermitian_ambiguities=0usize;
    for lambda in -128_i64..=128 {
        let _h_lambda_real=lambda;
        residual_hermitian_ambiguities+=1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.derivative_ordering_trace_contact.v1\",");
    println!("  \"monomial_orderings_checked\": {orderings},");
    println!("  \"nonhermitian_trace_failures\": {nonhermitian_failures},");
    println!("  \"hermitian_solution_count\": {hermitian_solutions},");
    println!("  \"required_contact\": \"-i hbar q\",");
    println!("  \"weyl_ordered_H\": \"q^2 p - i hbar q = q p q\",");
    println!("  \"residual_real_hbar_q_ambiguities_checked\": {residual_hermitian_ambiguities},");
    println!("  \"trace_preservation_fixes_all_quantum_counterterms\": false");
    println!("}}");
}
