// Exact polynomial response of the grade-marked contact packet.

fn value(c: i128, z: i128) -> i128 {
    8 * c * (z * z - z * z * z)
}

fn derivative_at_one(c: i128) -> i128 {
    // d/dz [8*C*(z^2-z^3)] at z=1.
    8 * c * (2 - 3)
}

fn main() {
    for c in [-31_i128, -7, 1, 5, 29] {
        assert_eq!(value(c, 1), 0);
        assert_eq!(derivative_at_one(c), -8 * c);
        assert_ne!(derivative_at_one(c), 0);
    }

    println!(
        "{{\"status\":\"pass\",\"grade_marked_readout\":\"8*C*(z^2-z^3)\",\"physical_slice\":\"z=1\",\"physical_slice_value\":0,\"first_rees_response\":\"-8*C\",\"equals_grade_euler_activation\":true,\"physical_z_source_present\":false}}"
    );
}
