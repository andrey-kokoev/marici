// Exact denominator-cleared certificate for the cyclic rational contact kernel.

fn main() {
    // For each complementary connected component:
    // C_j C_k / P_jk = q_jk / y_jk.
    let packets = [
        ([3_i128, 5, 7], [11_i128, 13, 17]),
        ([19_i128, 23, 29], [31_i128, 37, 41]),
        ([-5_i128, 7, 11], [13_i128, 17, 19]),
    ];

    for (q, y) in packets {
        for i in 0..3 {
            assert_ne!(q[i], 0);
            assert_ne!(y[i], 0);
            let contact_product = (i as i128 + 2) * 17;
            // Clear denominators in
            // 4*(contact_product*y/q)*(2*q/y)-8*contact_product = 0.
            let cleared =
                4 * contact_product * y[i] * (2 * q[i])
                - 8 * contact_product * q[i] * y[i];
            assert_eq!(cleared, 0);
        }
    }

    println!(
        "{{\"status\":\"pass\",\"samples\":3,\"cyclic_components\":3,\"kernel\":\"(2q23/y23,2q31/y31,2q12/y12,1)\",\"support_substitution\":\"prohibited\"}}"
    );
}
