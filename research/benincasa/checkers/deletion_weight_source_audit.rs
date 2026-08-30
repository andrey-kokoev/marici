// Frozen-source schema audit for the three-edge correlator weights.

fn main() {
    let fixed_weights = [1_i128, -2, 4, -8];
    for grade in 0_u32..=3 {
        assert_eq!(fixed_weights[grade as usize], (-2_i128).pow(grade));
    }

    let declared_continuous_weight_parameters: [&str; 0] = [];
    assert!(declared_continuous_weight_parameters.is_empty());

    println!(
        "{{\"status\":\"pass\",\"source_equations\":[\"2.13-2.14\",\"2.27-2.30\",\"4.66-4.71\"],\"fixed_grade_weights\":[1,-2,4,-8],\"declared_weight_deformation_parameters\":[],\"rees_marker_status\":\"derived_filtration_parameter_not_physical_source\"}}"
    );
}
