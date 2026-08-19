use std::collections::BTreeSet;

fn set(values: &[u8]) -> BTreeSet<u8> {
    values.iter().copied().collect()
}

fn compatible(left: &BTreeSet<u8>, right: &BTreeSet<u8>) -> bool {
    left.is_disjoint(right) || left.is_subset(right) || right.is_subset(left)
}

fn pairwise_compatible(flag: &[BTreeSet<u8>]) -> bool {
    flag.iter().enumerate().all(|(i, left)| {
        flag.iter()
            .skip(i + 1)
            .all(|right| compatible(left, right))
    })
}

fn main() {
    let a = set(&[1, 4]);
    let x = set(&[2, 3]);
    let y = set(&[3, 5]);
    let q = set(&[2, 3, 5]);

    let diagonal = vec![a.clone(), x.clone(), q.clone()];
    let off_diagonal = vec![a.clone(), y.clone(), q.clone()];
    let union = vec![a, x.clone(), y.clone(), q];

    assert!(pairwise_compatible(&diagonal));
    assert!(pairwise_compatible(&off_diagonal));
    assert!(!compatible(&x, &y));
    assert!(!pairwise_compatible(&union));

    // Both source objects are maximal length-three flags. A cellular/nested-set
    // incidence differential changes flag length by one and cannot directly
    // connect two distinct generators of the same degree.
    let diagonal_degree = diagonal.len();
    let off_diagonal_degree = off_diagonal.len();
    assert_eq!(diagonal_degree, off_diagonal_degree);
    let direct_incidence_degree = off_diagonal_degree as isize - diagonal_degree as isize;
    assert_eq!(direct_incidence_degree, 0);

    // Deleting the incompatible middle cut from either ordered flag gives
    // the same length-two coarsening (a,q), with the same simplicial sign.
    let common_coarsening = vec![diagonal[0].clone(), diagonal[2].clone()];
    assert_eq!(common_coarsening, vec![off_diagonal[0].clone(), off_diagonal[2].clone()]);
    assert!(pairwise_compatible(&common_coarsening));
    let deleted_index = 1usize;
    let diagonal_incidence_sign = if deleted_index % 2 == 0 { 1 } else { -1 };
    let off_diagonal_incidence_sign = if deleted_index % 2 == 0 { 1 } else { -1 };
    assert_eq!(diagonal_incidence_sign, off_diagonal_incidence_sign);

    println!(
        "{{\"schema\":\"marici.benincasa.string_six_point_flag_compatibility.v2\",\"diagonal_flag\":[\"s14\",\"s23\",\"s235\"],\"off_diagonal_flag\":[\"s14\",\"s35\",\"s235\"],\"diagonal_flag_compatible\":true,\"off_diagonal_flag_compatible\":true,\"differing_cuts\":[\"s23\",\"s35\"],\"cut_intersection\":[3],\"left_subset_right\":false,\"right_subset_left\":false,\"cuts_disjoint\":false,\"union_nested_set\":false,\"carrier_common_stratum\":false,\"diagonal_degree\":{},\"off_diagonal_degree\":{},\"direct_incidence_degree\":{},\"cellular_boundary_can_connect_directly\":false,\"common_coarsening\":[\"s14\",\"s235\"],\"deleted_slot\":1,\"diagonal_incidence_sign\":{},\"off_diagonal_incidence_sign\":{},\"signs_equal\":true}}",
        diagonal_degree,
        off_diagonal_degree,
        direct_incidence_degree,
        diagonal_incidence_sign,
        off_diagonal_incidence_sign
    );
}
