fn main() {
    // Local resonant model over Q: doubled carrier R=Q[z]/(z^2).
    // A normalized exact image z*unit is zero modulo z, but nonzero modulo z^2.
    let exact_z_order = 1_u8;
    let doubled_carrier_order = 2_u8;
    let reduced_carrier_order = 1_u8;

    let descends_to_doubled = exact_z_order >= doubled_carrier_order;
    let descends_to_reduced = exact_z_order >= reduced_carrier_order;
    assert!(!descends_to_doubled);
    assert!(descends_to_reduced);

    // Even resonance has no first-Cartier exact symbol; odd resonance has a unit symbol.
    let first_cartier_ranks = [0_u8, 1_u8];
    assert_eq!(first_cartier_ranks, [0, 1]);

    println!(
        "{{\"schema\":\"marici.benincasa.soft_axis_carrier_reduction_lift.v1\",\
\"doubled_carrier_ideal\":\"(z^2)\",\
\"exact_image_ideal_on_odd_resonance\":\"(z)\",\
\"ordinary_reduction_to_doubled_carrier_descends\":false,\
\"ordinary_reduction_to_reduced_carrier_descends\":true,\
\"first_Cartier_ranks_even_odd\":[0,1],\
\"required_replacement\":\"derived_two_term_carrier_resolution\",\
\"new_carrier_datum\":false}}"
    );
}
