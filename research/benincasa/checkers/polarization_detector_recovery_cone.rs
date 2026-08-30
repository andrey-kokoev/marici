fn dot(a: [i64; 3], b: [i64; 3]) -> i64 {
    a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
}

fn main() {
    let scalar = [1, 1, 1];
    let plus = [2, -1, -1];
    let cross = [0, -1, 1];

    let kernel_plus = [0, 1, -1];
    let kernel_cross = [-2, 1, 1];

    assert_eq!(dot(scalar, kernel_plus), 0);
    assert_eq!(dot(plus, kernel_plus), 0);
    assert_eq!(dot(cross, kernel_plus), -2);

    assert_eq!(dot(scalar, kernel_cross), 0);
    assert_eq!(dot(cross, kernel_cross), 0);
    assert_eq!(dot(plus, kernel_cross), -6);

    println!(
        "{{\"status\":\"pass\",\"plus_detector_kernel\":[0,1,-1],\"cross_recovery_coefficient\":-2,\"cross_detector_kernel\":[-2,1,1],\"plus_recovery_coefficient\":-6,\"supported_cone_homology_after_complementary_port\":0}}"
    );
}
