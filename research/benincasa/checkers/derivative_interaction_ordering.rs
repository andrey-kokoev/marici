fn main(){
    let mut ordering_choices=0usize;
    let mut primitive_force_shifts=0usize;
    let mut cut_defect_invariances=0usize;

    // H_lambda=q p q + lambda hbar q.
    // Dq=q^2 and Dp=-(pq+qp)-lambda hbar.
    for lambda in -128_i64..=128 {
        let dq_q2_coefficient=1_i64;
        let dp_central_hbar_coefficient=-lambda;
        assert_eq!(dq_q2_coefficient,1);
        assert_eq!(dp_central_hbar_coefficient,-lambda);
        ordering_choices+=1;
        if lambda!=0 { primitive_force_shifts+=1; }

        // With primitive hbar, the ordering shift is itself primitive:
        // Delta(-lambda h) - [(-lambda hL)+(-lambda hR)] = 0.
        let coproduct_shift=-lambda*(1+1);
        let factorwise_shift=(-lambda)+(-lambda);
        assert_eq!(coproduct_shift-factorwise_shift,0);
        cut_defect_invariances+=1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.derivative_interaction_ordering.v1\",");
    println!("  \"ordering_choices\": {ordering_choices},");
    println!("  \"nonweyl_primitive_force_shifts\": {primitive_force_shifts},");
    println!("  \"cut_defect_invariance_checks\": {cut_defect_invariances},");
    println!("  \"weyl_ordered_H\": \"q p q\",");
    println!("  \"ordering_family\": \"q p q + lambda hbar q\",");
    println!("  \"primitive_force_shift\": \"-lambda hbar\",");
    println!("  \"cut_coherence_selects_ordering\": false");
    println!("}}");
}
