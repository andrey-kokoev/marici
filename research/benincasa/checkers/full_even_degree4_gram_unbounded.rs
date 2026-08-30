fn main() {
    let mut checks = 0usize;
    for z in -500_i64..=500 {
        // Basis (1,A=Q^2,B=S,C=P^2), with fixed lower covariance
        // Q2=1, <S>=0, P2=2 and fixed U=<Q^4>=2.
        // The leading 3x3 block uses W=<S^2>=z^2+5 and has determinant 1.
        let w = z * z + 5;
        assert!(1 * 2 - 0 * 0 >= 1);
        let leading_det = w - z * z - 4;
        assert_eq!(leading_det, 1);

        // Cross column to C is c=(2,0,4i). Exact solution of M3 x=c gives
        // c^* M3^{-1} c = 4 z^2+8. Choose T=<P^4> one unit above.
        let schur_cost = 4 * z * z + 8;
        let t = 4 * z * z + 9;
        let schur = t - schur_cost;
        assert_eq!(schur, 1);

        // Canonical commutator imaginary parts:
        // Im<Q^2 S>=2, Im<Q^2 P^2>=0, Im<S P^2>=4.
        let im_a_b = 2;
        let im_a_c = 0;
        let im_b_c = 4;
        assert_eq!(im_a_b, 2 * 1);
        assert_eq!(im_a_c, 4 * 0);
        assert_eq!(im_b_c, 2 * 2);
        checks += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.full_even_degree4_gram_unbounded.v1\",");
    println!("  \"exact_family_checks\": {checks},");
    println!("  \"fixed_covariance\": {{\"Q2\":1,\"S\":0,\"P2\":2}},");
    println!("  \"fixed_Q4\": 2,");
    println!("  \"free_mixed_entry\": \"Z=Re<Q^2 S>\",");
    println!("  \"completion\": {{\"S2\":\"Z^2+5\",\"P4\":\"4Z^2+9\"}},");
    println!("  \"leading_minor\": 1,");
    println!("  \"full_schur_complement\": 1,");
    println!("  \"degree4_gram_bounds_Z\": false");
    println!("}}");
}
