fn gcd(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        let remainder = a % b;
        a = b;
        b = remainder;
    }
    a
}

fn main() {
    // Entry266 supplies the oriented degree-two full-log carrier. Entry176
    // supplies the independently normalized central exceptional coefficient.
    let carrier_degree = 2_i64;
    let central_coefficient = 1_i64;
    assert_eq!(gcd(carrier_degree, central_coefficient), 1);

    // The augmented top/framing row [2,1] is saturated.
    let smith_factor = gcd(carrier_degree, central_coefficient);
    assert_eq!(smith_factor, 1);
    let cokernel_order = smith_factor;
    assert_eq!(cokernel_order, 1);

    // With the certified positive central normalization k=+1, the primitive
    // target top equation 2a+k=1 has the unique carrier coordinate a=0.
    let k = 1_i64;
    let numerator = 1 - k;
    assert_eq!(numerator % carrier_degree, 0);
    let carrier_coordinate = numerator / carrier_degree;
    assert_eq!(carrier_coordinate, 0);
    let local_parity = carrier_coordinate.rem_euclid(2);
    assert_eq!(local_parity, 0);

    println!(
        "{{\"status\":\"proved_scoped_degree_two_central_exceptional_repair\",\"carrier_degree\":2,\"central_coefficient\":1,\"augmented_row\":[2,1],\"smith_factors\":[1],\"cokernel\":0,\"normalized_central_k\":1,\"carrier_coordinate\":0,\"local_top_parity\":0,\"spatial_central_to_entry143_top_map_constructed\":false,\"physical_p_defined\":false}}"
    );
}
