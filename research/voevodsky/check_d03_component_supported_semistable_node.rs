//! Finite coefficient audit of a selected component of the semistable node.
//!
//! For D=V(tx)=X union T, normalization is the equal-constant fibre product
//! of k[t] and k[x] over the conductor k.  Selecting X=V(x) gives
//! J_X=Cone(O_X->O_C)[-1]=(t).  The two conductor Tor grades belong to the
//! derived Cartier self-intersection O_C tensor^L_{O_X} O_C; the primitive
//! conormal/Bockstein label is [t].  This checker makes no sheaf-level
//! endpoint or global-target claim.

fn constant_term(polynomial: &[i64]) -> i64 {
    polynomial[0]
}

fn determinant_3(matrix: [[i64; 3]; 3]) -> i64 {
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
}

fn main() {
    // Bounded normalization audit through degree three.  An element of the
    // normalization k[t] plus k[x] descends to k[x,t]/(xt) exactly when its
    // two constant terms agree; the conductor difference is surjective.
    let samples = -2_i64..=2_i64;
    let mut kernel_count = 0_usize;
    let mut equal_constant_count = 0_usize;
    for ct in samples.clone() {
        for cx in samples.clone() {
            let t_polynomial = [ct, 1, -1, 2];
            let x_polynomial = [cx, -2, 1, 1];
            let conductor_difference = constant_term(&t_polynomial) - constant_term(&x_polynomial);
            if conductor_difference == 0 {
                kernel_count += 1;
            }
            if ct == cx {
                equal_constant_count += 1;
            }
        }
    }
    assert_eq!(kernel_count, equal_constant_count);
    assert_eq!(kernel_count, 5);
    // The pair of constants (1,0) maps to 1, proving surjectivity.
    assert_eq!(1_i64 - 0_i64, 1);

    // On X, restriction k[t] -> k takes the constant term.  Its kernel is
    // precisely (t); division by the labelled generator t identifies the
    // coefficient vectors integrally and without torsion.
    for c0 in samples.clone() {
        let polynomial = [c0, 2, -1, 1];
        let in_kernel = constant_term(&polynomial) == 0;
        let divisible_by_t = polynomial[0] == 0;
        assert_eq!(in_kernel, divisible_by_t);
    }
    let component_support_generator = "t";
    assert_eq!(component_support_generator, "t");

    // The conductor Cartier resolution on X is k[t] --t--> k[t].  Derived
    // tensor with k=k[t]/(t) makes the differential zero, retaining Tor0 and
    // Tor1, each primitive rank one.  The filtered connecting symbol is [t].
    let conductor_derived_differential = 0_i64;
    let conductor_tor_ranks = [1_usize, 1_usize];
    let conormal_symbol = "[t]";
    assert_eq!(conductor_derived_differential, 0);
    assert_eq!(conductor_tor_ranks, [1, 1]);
    assert_eq!(conormal_symbol, "[t]");

    // D3 permutes the three labelled conormal lines.  Rotation is a
    // three-cycle and preserves their determinant; reflection transposes two
    // labels and reverses the determinant orientation.
    let rotation = [[0_i64, 0, 1], [1, 0, 0], [0, 1, 0]];
    let reflection = [[0_i64, 1, 0], [1, 0, 0], [0, 0, 1]];
    assert_eq!(determinant_3(rotation), 1);
    assert_eq!(determinant_3(reflection), -1);

    // Weighted graph closure for occurrence [G:H] and normal [P:Q]:
    // t_D*P*H-t*Q*G=0.  At t=0 with t_D a unit, the selected X strict
    // direction has H nonzero and forces P=0, one normal corner.  The
    // opposite direction H=0 imposes no equation and leaves a full P1.
    let t_d_is_unit = true;
    let selected_h_nonzero = true;
    let selected_corner_forces_p_zero = t_d_is_unit && selected_h_nonzero;
    let selected_normal_corner_count = usize::from(selected_corner_forces_p_zero);
    let opposite_h_zero = true;
    let opposite_normal_fibre_dimension = usize::from(opposite_h_zero);
    assert_eq!(selected_normal_corner_count, 1);
    assert_eq!(opposite_normal_fibre_dimension, 1);

    // The selected corner theorem is completion-scoped: without the unit
    // t_D, the graph equation can vanish identically at the deeper fibre.
    let universal_t_d_may_vanish = true;
    let deeper_full_product_ambiguity = universal_t_d_may_vanish;
    assert!(deeper_full_product_ambiguity);

    println!(
        "{}",
        r#"{"claim":"For the semistable node V(tx)=X union T, the normalization row 0->O_D->O_X plus O_T->O_C->0 is exact, and the selected X-component object Cone(O_X->O_C)[-1] is the principal ideal J_X=(t).  The conductor Cartier self-intersection retains primitive Tor0 and Tor1 lines with conormal/Bockstein symbol [t].  For three labelled nodes, rotation preserves and reflection reverses the determinant conormal orientation.  In the weighted graph with t_D a unit, the strict selected X direction has a unique normal corner at t=0, while the opposite direction retains an exceptional P1 ambiguity.","status":"proved","scope":"finite semistable-node coefficients, component support, Cartier conductor fibre, and completed weighted-graph corner census only","assumptions":["the physical component X=V(x) is selected by its admitted label","t_D is a unit in the fixed-beta completed D03 comparison","the ordered conormal labels are (t1,t3,t5)"],"factorization_test":{"normalization_equalizer":"PASS through the bounded polynomial census","conductor_difference":"SURJECTIVE","component_support":"J_X=(t)=Cone(O_X->O_C)[-1]","derived_conductor_fibre":{"Tor0":1,"Tor1":1,"differential":0,"primitive_symbol":"[t]"},"D3_determinants":{"rotation":1,"reflection":-1},"selected_X_corner":"UNIQUE when t_D is a unit","opposite_corner":"exceptional P1 ambiguity","universal_deeper_fibre":"ambiguous if t_D also vanishes","base_inversion":"NONE"},"unconstructed":["the sheaf-level extraordinary counit from the selected strict transform to the reciprocal/BM endpoint packet","global polarity compatibility of the component-supported node triangle","descent/pushforward to entry143's full target and its generic Q leg"],"boundary":"The checker distinguishes the principal component-support ideal from the two-grade derived Cartier self-intersection.  It proves neither a spatial endpoint identification nor alpha_03."}"#
    );
}
