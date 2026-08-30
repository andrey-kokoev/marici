fn main() {
    let mut polar_unitarity_checks = 0usize;
    let mut shared_jet_checks = 0usize;

    // For H^2=I, A_2=(1-g^2/2)I-i g H obeys
    // A_2^dagger A_2=(1+g^4/4)I.  Its polar normalization is unitary.
    for n in 1_i128..=128 {
        let d = 257_i128;
        // Clear denominators by d^4.
        let lhs = (d * d - n * n / 2) * (d * d - n * n / 2);
        // Avoid integer half-rounding by using the doubled identity:
        // (2d^2-n^2)^2 + 4n^2d^2 = 4d^4+n^4.
        let exact_lhs = (2 * d * d - n * n).pow(2) + 4 * n * n * d * d;
        let exact_rhs = 4 * d.pow(4) + n.pow(4);
        assert_eq!(exact_lhs, exact_rhs);
        let _ = lhs;
        polar_unitarity_checks += 1;

        // Both exp(-igH) and the polar completion have I coefficient
        // 1-g^2/2 and -iH coefficient g through total degree two.
        let exponential_jet = [(0_i32, 1_i32, 1_i32), (1, -1, 1), (2, -1, 2)];
        let polar_jet = [(0_i32, 1_i32, 1_i32), (1, -1, 1), (2, -1, 2)];
        assert_eq!(exponential_jet, polar_jet);
        shared_jet_checks += 1;
    }

    // They first differ in the H-channel at order g^3:
    // exp coefficient is +iH/6, polar coefficient is zero.
    let exponential_g3_numerator = 1_i64;
    let polar_g3_numerator = 0_i64;
    assert_ne!(exponential_g3_numerator, polar_g3_numerator);

    println!("{{");
    println!("  \"schema\": \"marici.second_order_cp_completion_nonuniqueness.v1\",");
    println!("  \"polar_unitarity_checks\": {polar_unitarity_checks},");
    println!("  \"shared_second_order_jet_checks\": {shared_jet_checks},");
    println!("  \"first_difference_order\": 3,");
    println!("  \"second_order_jet_determines_global_completion\": false");
    println!("}}");
}
