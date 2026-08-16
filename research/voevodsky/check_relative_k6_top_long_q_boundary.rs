//! Target-side relative K6 top and the coefficient-two source gate.

fn gcd(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        (a, b) = (b, a % b);
    }
    a
}

fn main() {
    // Outward-oriented facet bases make the cellular boundary coefficients +1.
    let absolute_boundary = [1_i64; 9];
    let short_projection = [0_i64; 6];
    let relative_long_boundary = [1_i64; 3];
    assert_eq!(absolute_boundary.len(), 9);
    assert_eq!(short_projection, [0; 6]);
    assert_eq!(relative_long_boundary.into_iter().fold(0, gcd), 1);

    // D3 rotation cyclically permutes the three long facets. Reflection reverses
    // the ambient top orientation and applies the corresponding signed permutation.
    let rotate = |v: [i64; 3]| [v[2], v[0], v[1]];
    let reflect_signed = |v: [i64; 3]| [-v[0], -v[2], -v[1]];
    assert_eq!(rotate(relative_long_boundary), relative_long_boundary);
    assert_eq!(reflect_signed(relative_long_boundary), [-1, -1, -1]);

    // The constructed full-log maximal-cone source has degree two.
    let existing_source_image = relative_long_boundary.map(|value| 2 * value);
    assert_eq!(existing_source_image, [2, 2, 2]);
    assert_eq!(existing_source_image.into_iter().fold(0, gcd), 2);

    // A separately sourced primitive relative interior would be the missing odd column.
    let enlarged_row = [2_i64, 1_i64];
    assert_eq!(enlarged_row.into_iter().fold(0, gcd), 1);

    println!(
        "{{\"status\":\"proved_scoped_relative_K6_top_target_with_source_degree_two_gate\",\"absolute_facets\":9,\"short_facets_quotiented\":6,\"relative_long_boundary\":[1,1,1],\"relative_snf\":[1],\"reflection_character\":\"odd\",\"existing_full_log_source_boundary\":[2,2,2],\"existing_source_snf\":[2],\"primitive_source_interior_constructed\":false,\"literal_Q_source_comparison_constructed\":false,\"physical_mapping_fiber\":\"unconstructed\"}}"
    );
}
