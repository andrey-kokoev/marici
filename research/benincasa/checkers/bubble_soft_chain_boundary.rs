// Radial soft-boundary audit for the last-edge deletion insertion 1/y_b.

fn post_deletion_radial_exponent(spatial_dimension: i32) -> i32 {
    // d^d ell ~ r^(d-1) dr dOmega; deletion contributes r^(-1).
    spatial_dimension - 2
}

fn primitive_exponent(spatial_dimension: i32) -> i32 {
    post_deletion_radial_exponent(spatial_dimension) + 1
}

fn main() {
    let d = 3_i32;
    assert_eq!(post_deletion_radial_exponent(d), 1);
    assert_eq!(primitive_exponent(d), 2);
    let boundary_current = primitive_exponent(d) <= 0;
    assert!(!boundary_current);

    // The first marginal logarithmic case is d=1.
    assert_eq!(post_deletion_radial_exponent(1), -1);
    assert_eq!(primitive_exponent(1), 0);

    println!(
        "{{\"status\":\"pass\",\"spatial_dimension\":3,\"post_deletion_radial_exponent\":1,\"primitive_exponent\":2,\"soft_boundary_current\":false,\"first_marginal_dimension\":1}}"
    );
}
