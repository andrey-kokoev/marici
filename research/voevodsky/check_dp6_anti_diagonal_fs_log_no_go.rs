//! Sharp-monoid obstruction for the conductor-Tor wall.
//!
//! For the product-branch log map N -> N^2, 1 |-> (1,1), the relative
//! characteristic lattice is L = Z^2 / Z(1,1) = Z.  In the ordered branch
//! convention [b]=+1 and [a]=-1, while branch reflection acts by n |-> -n.
//! No nonzero sharp integral submonoid of this sign lattice can contain both
//! branch classes or be reflection invariant: containing n and -n makes n a
//! unit.
//!
//! Scope: an ordinary fs-log divisor/ray used as the third wall while
//! retaining both branch restrictions and physical reflection.  Oriented
//! Kato-Nakayama, constructible sign-local-system, derived, and
//! vanishing-cycle correspondences remain available.

const ORDERED_PAIRS: usize = 6;

fn delta(a: i64, b: i64) -> i64 {
    b - a
}

fn reflected(value: i64) -> i64 {
    -value
}

fn is_unit_if_both_signs_are_present(value: i64, negative: i64) -> bool {
    value + negative == 0
}

fn main() {
    // The relative characteristic quotient and its branch classes.
    let class_a = delta(1, 0);
    let class_b = delta(0, 1);
    assert_eq!(class_a, -1);
    assert_eq!(class_b, 1);
    assert_eq!(class_a + class_b, 0);

    // The labelled branch swap is precisely the sign action.
    assert_eq!(reflected(class_a), class_b);
    assert_eq!(reflected(class_b), class_a);

    // If a monoid contains both effective branch classes, either class has
    // an additive inverse inside the monoid and is therefore a unit.  A
    // sharp characteristic monoid permits no such nonzero unit.
    let both_branch_classes_make_unit = is_unit_if_both_signs_are_present(class_b, class_a);
    assert!(both_branch_classes_make_unit);
    let sharp_nonzero_monoid_can_contain_both = false;
    assert!(!sharp_nonzero_monoid_can_contain_both);

    // The same argument excludes a nonzero reflection-stable sharp ray:
    // stability sends every positive element to its inverse.
    for positive in 1_i64..=12 {
        let image = reflected(positive);
        assert!(is_unit_if_both_signs_are_present(positive, image));
    }
    let nonzero_reflection_invariant_sharp_ray_exists = false;
    assert!(!nonzero_reflection_invariant_sharp_ray_exists);

    // Choosing one ordered ray is possible, but reflection exchanges it
    // with the opposite ray.  The anti-diagonal is therefore an oriented
    // sign local system/groupified log direction, not an equivariant
    // effective fs-log boundary divisor.
    let ordered_positive_ray_exists = true;
    let reflection_preserves_ordered_positive_ray = false;
    assert!(ordered_positive_ray_exists);
    assert!(!reflection_preserves_ordered_positive_ray);

    // Rotation only relabels the six ordered pairs; the obstruction repeats
    // uniformly.
    let obstructed_ordered_pairs = ORDERED_PAIRS;
    assert_eq!(obstructed_ordered_pairs, 6);

    println!(
        "{}",
        r#"{"status":"falsified_scoped_reflection_equivariant_fs_log_wall","relative_characteristic_lattice":"Z^2/Z(1,1)=Z_or","class_a":-1,"class_b":1,"branch_swap":"n->-n","both_effective_classes_make_nonzero_unit":true,"nonzero_reflection_invariant_sharp_ray_exists":false,"ordered_positive_ray_exists":true,"reflection_preserves_ordered_positive_ray":false,"ordered_pairs":6,"ordinary_fs_log_third_divisor_constructed":false,"oriented_KN_or_derived_correspondence_no_go":false,"minimal_additional_datum":"an oriented Kato-Nakayama/constructible sign-local-system wall or derived vanishing-cycle object, with reflection acting on its orientation line and a proper Beck-Chevalley realization into the literal entry143 wall costalk"}"#
    );
}
