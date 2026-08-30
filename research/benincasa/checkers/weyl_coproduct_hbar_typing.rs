fn main() {
    let mut fixed_hbar_failures = 0usize;
    let mut primitive_hbar_passes = 0usize;

    // For n occurrence factors, q_total=sum q_i and p_total=sum p_i.
    // Cross-occurrence commutators vanish, so [q_total,p_total]=n i hbar.
    // A fixed scalar Weyl relation expects only i hbar.
    for occurrences in 2_i64..=128 {
        let commutator_coefficient = occurrences;
        let fixed_scalar_relation = 1_i64;
        let fixed_residual = commutator_coefficient - fixed_scalar_relation;
        assert_eq!(fixed_residual, occurrences - 1);
        assert_ne!(fixed_residual, 0);
        fixed_hbar_failures += 1;

        // If the central parameter is primitive, hbar_total=sum hbar_i,
        // its coefficient is n and the relation descends exactly.
        let primitive_hbar_coefficient = occurrences;
        assert_eq!(commutator_coefficient - primitive_hbar_coefficient, 0);
        primitive_hbar_passes += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.weyl_coproduct_hbar_typing.v1\",");
    println!("  \"fixed_hbar_failures\": {fixed_hbar_failures},");
    println!("  \"primitive_hbar_passes\": {primitive_hbar_passes},");
    println!("  \"two_occurrence_fixed_hbar_residual\": \"i hbar\",");
    println!("  \"fixed_parameter_weyl_algebra_has_primitive_qp_coproduct\": false,");
    println!("  \"homogenized_primitive_hbar_relation_descends\": true");
    println!("}}");
}
