fn coefficients(delta_mass: i64) -> (i64, i64, i64) {
    // Coefficients of (V^2, V*S, S^2), multiplied by eight, in
    // -1/2 * (V - delta_mass*S/2)^2.
    (-4, 4 * delta_mass, -delta_mass * delta_mass)
}

fn main() {
    let desired = (-4, 8, -4); // eight times -1/2*(V-S)^2
    assert_eq!(coefficients(2), desired);
    assert_ne!(coefficients(1), desired);

    println!("{{");
    println!("  \"schema\": \"marici.boundary_delta_insertion_contract.v1\",");
    println!("  \"desired_coefficients_times_8\": [-4, 8, -4],");
    println!("  \"printed_H0_coefficient\": \"-1/2\",");
    println!("  \"forced_endpoint_delta_mass\": 2,");
    println!("  \"forced_integrated_H0\": \"-S0^(3)\",");
    println!("  \"ordinary_full_weight_delta_passes\": false,");
    println!("  \"effective_insertion_passes\": true");
    println!("}}");
}

