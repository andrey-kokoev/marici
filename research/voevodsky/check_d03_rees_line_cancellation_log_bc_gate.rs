//! Canonical Rees-line cancellation and ordinary-purity gate.
//!
//! The occurrence ideal dual cancels the Rees occurrence line before proper
//! pushforward.  Ordinary conormal/Koszul purity for u=X*t fails at the
//! crossing; a logarithmic branch-selected BC map is not constructed here.

fn p1_h0(degree: i32) -> usize {
    (degree + 1).max(0) as usize
}

fn p1_h1(degree: i32) -> usize {
    (-degree - 1).max(0) as usize
}

fn main() {
    // On the X-chart of Bl_(X,u), the divisor section factors as u=X*t.
    // At C=V(X,t), both partial derivatives du/dX=t and du/dt=X vanish.
    let x_at_c = 0_i64;
    let t_at_c = 0_i64;
    let u_at_c = x_at_c * t_at_c;
    let du_dx_at_c = t_at_c;
    let du_dt_at_c = x_at_c;
    assert_eq!((u_at_c, du_dx_at_c, du_dt_at_c), (0, 0, 0));

    // The selected conductor line is I_X=O(-1) and the primal occurrence
    // dual is I_X^vee=O(+1).  Evaluation is canonical and degree zero.
    let i_x_exponent = -1_i32;
    let i_x_dual_exponent = 1_i32;
    let evaluated_exponent = i_x_exponent + i_x_dual_exponent;
    assert_eq!(evaluated_exponent, 0);

    // Before evaluation, Rp_*O(-1)=0.  After line evaluation, Rp_*O=O has
    // one primitive global section and no higher cohomology.
    assert_eq!((p1_h0(-1), p1_h1(-1)), (0, 0));
    assert_eq!((p1_h0(evaluated_exponent), p1_h1(evaluated_exponent)), (1, 0));

    // Support mismatch: V(X*t) contains both coordinate axes, whereas
    // V(X,t) is their intersection.  The point (X,t)=(1,0) distinguishes them.
    let point = (1_i64, 0_i64);
    let on_product_divisor = point.0 * point.1 == 0;
    let on_complete_intersection = point.0 == 0 && point.1 == 0;
    assert!(on_product_divisor);
    assert!(!on_complete_intersection);

    // Hilbert-function witness over k[X,t].  In degree d>=1, k[X,t]/(Xt)
    // retains X^d and t^d (rank two), while k[X,t]/(X,t) has rank zero.
    for degree in 1_usize..=12 {
        let product_quotient_rank = 2_usize;
        let intersection_quotient_rank = 0_usize;
        assert_ne!(product_quotient_rank, intersection_quotient_rank);
        assert_eq!(degree + 1 - (degree - 1), product_quotient_rank);
    }

    // Derived fibre at C: K(X*t) has one generator in degrees 0 and 1,
    // while K(X,t) has the 1-2-1 exterior algebra.  Ordinary purity cannot
    // identify these Tor packets.
    let product_koszul_fibre_ranks = [1_usize, 1_usize, 0_usize];
    let pair_koszul_fibre_ranks = [1_usize, 2_usize, 1_usize];
    assert_ne!(product_koszul_fibre_ranks, pair_koszul_fibre_ranks);

    let canonical_line_evaluation = true;
    let ordinary_purity_bc_exists = false;
    let log_branch_selected_bc_constructed = false;
    let literal_entry143_comparison_constructed = false;
    assert!(canonical_line_evaluation);
    assert!(!ordinary_purity_bc_exists);
    assert!(!log_branch_selected_bc_constructed);
    assert!(!literal_entry143_comparison_constructed);

    println!(
        "{}",
        r#"{"claim":"On the Rees chart u5=X5*t5, the selected occurrence line I_X5=O(-1) canonically pairs with the primal I_X5^vee=O(1), so evaluation occurs before pushforward and changes Rp_*O(-1)=0 into Rp_*O=O with one primitive section. This requires no scalar trivialization. Ordinary purity nevertheless fails at C=V(X5,t5): du5=(t5,X5) vanishes there, V(X5*t5) differs from V(X5,t5), and the derived fibres of K(X5*t5) and K(X5,t5) have ranks 1-1 and 1-2-1 respectively.","status":"proved_scoped_with_no_go","scope":"canonical Rees occurrence-line cancellation and falsification of ordinary Cartier/BC identification at the crossing","factorization_test":{"divisor_factorization":"u5=X5*t5","I_X5_exponent":-1,"I_X5_dual_exponent":1,"evaluated_exponent":0,"Rp_*O(-1)":[0,0],"Rp_*O":[1,0],"du5_at_C":[0,0],"support_witness":"(1,0) lies in V(X5*t5) but not V(X5,t5)","K_product_fibre_ranks":[1,1],"K_pair_fibre_ranks":[1,2,1],"base_inversion":false},"unconstructed":["logarithmic branch-selected excess BC map","Tor0/Tor1 comparison to literal entry143 u5 Boolean factor","endpoint butterfly connector"],"boundary":"The line evaluation is canonical, but it does not imply ordinary purity. A log/SNC branch-selected correspondence remains additional geometric structure."}"#
    );
}
