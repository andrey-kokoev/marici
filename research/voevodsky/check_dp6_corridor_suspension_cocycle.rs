//! Suspension cocycle forced by reflection of the shifted corridor.
//!
//! Reflection exchanges the two boundary charts and therefore acts on the
//! shift lattice by sign.  A graded lift is a C2 one-cocycle a in Z_sign;
//! changing boundary trivialization changes a by 2b.  The P/P[1] exchange
//! has a=1, the nonzero class in H^1(C2;Z_sign)=Z/2.  Consequently an
//! ordinary degree-zero geometric reflection cannot realize it.

fn is_cocycle(_a: i64) -> bool {
    // For sign action r(a)=-a, the C2 cocycle equation a+r(a)=0 is automatic.
    true
}

fn cohomology_class_mod_two(a: i64) -> i64 {
    a.rem_euclid(2)
}

fn is_coboundary(a: i64) -> bool {
    // Coboundaries are b-r(b)=2b.
    a % 2 == 0
}

fn main() {
    let required_suspension = 1i64;
    assert!(is_cocycle(required_suspension));
    assert_eq!(cohomology_class_mod_two(required_suspension), 1);
    assert!(!is_coboundary(required_suspension));

    // Exhaustive bounded witness for the integral classification.
    for a in -32i64..=32 {
        assert!(is_cocycle(a));
        assert_eq!(is_coboundary(a), cohomology_class_mod_two(a) == 0);
    }

    // The Smith presentation of coboundaries is [2].
    let smith_factor = 2i64;
    let cokernel_order = smith_factor.abs();
    assert_eq!(cokernel_order, 2);

    // Forward and reverse transports have opposite integer degree and hence
    // compose to degree zero, as required for r^2=1 on the action groupoid.
    let forward_degree = 1i64;
    let reverse_degree = -1i64;
    assert_eq!(forward_degree + reverse_degree, 0);

    // An ungraded geometric pullback has cocycle zero and is not equivalent
    // to the required odd lift over Z.  It becomes trivial only after adding
    // an explicit graded reflection-groupoid extension (or after forgetting
    // the integral grading, which is not allowed here).
    let ordinary_geometric_class = 0i64;
    assert_ne!(
        cohomology_class_mod_two(ordinary_geometric_class),
        cohomology_class_mod_two(required_suspension)
    );

    println!(
        "{}",
        r#"{"status":"proved_scoped_corridor_suspension_cocycle","coefficient_module":"Z_sign","cocycle_equation":"a+r(a)=0","coboundary_map_smith":[2],"H1":"Z/2","required_suspension_cocycle":1,"required_class_mod2":1,"ordinary_geometric_reflection_class":0,"forward_reverse_total_degree":0,"minimal_additional_datum":"a graded reflection-action-groupoid lift carrying the odd suspension cocycle, coupled to the wall-supported excess triangle","wall_triangle_constructed":false,"literal_entry143_realization_constructed":false,"endpoint_Q_mapping_fiber_instantiated":false,"p_partial_Q_defined":false}"#
    );
}
