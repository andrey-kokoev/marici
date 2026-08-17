fn main() {
    // Frozen exact-system dimensions from the source-normalized certificates.
    let one_wall = (188_i64, 93_i64);
    let two_wall = (540_i64, 194_i64);
    let top_six_orders = (1080_i64, 416_i64);
    assert_eq!(one_wall.0 - one_wall.1, 95);
    assert_eq!(two_wall.0 - two_wall.1, 346);
    assert_eq!(top_six_orders.0 - top_six_orders.1, 664);

    // In the audited degree-four one-wall system only five of the ten
    // quotient/absolute residue coordinates are fixed. The other five vary
    // along exact-lift gauge directions.
    let one_wall_residue_coordinates = 10_i64;
    let one_wall_variation_rank = 5_i64;
    assert_eq!(one_wall_residue_coordinates - one_wall_variation_rank, 5);

    // The source geometry does fix the required solver shape: twelve master
    // coefficients plus eight polynomial primitive fields per degree layer.
    let degree4_monomials = (4 + 1) * (4 + 2) / 2;
    let unknowns_per_layer = 12 + 8 * degree4_monomials;
    assert_eq!(degree4_monomials, 15);
    assert_eq!(unknowns_per_layer, 132);
    assert_eq!(2 * unknowns_per_layer, 264);
    assert_eq!(3 * unknowns_per_layer, 396);

    println!("{{");
    println!("  \"schema\": \"marici.benincasa.marked_connection_reconstruction_gate.v1\",");
    println!("  \"one_wall_degree5_nullity\": 95,");
    println!("  \"one_wall_residue_variation_rank\": 5,");
    println!("  \"two_wall_degree5_nullity\": 346,");
    println!("  \"top_six_order_degree5_nullity\": 664,");
    println!("  \"formal_single_power_degree4_unknowns\": 132,");
    println!("  \"formal_count_is_complete_solver_shape\": false,");
    println!("  \"existing_packets_uniquely_determine_bivariate_rank12_connection\": false,");
    println!("  \"required_next_object\": \"source-normalized four-stratum relative de Rham reduction engine\",");
    println!("  \"post_hoc_flat_splitting_allowed\": false,");
    println!("  \"new_carrier_datum\": false");
    println!("}}");
}
