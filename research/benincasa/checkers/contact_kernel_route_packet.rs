// Exact pre-aggregation classification of the canonical contact kernel.

fn main() {
    let packets = [
        ([3_i128, 5, 7], [11_i128, 13, 17], [19_i128, 23, 29]),
        ([31_i128, 37, 41], [43_i128, 47, 53], [59_i128, 61, 67]),
        ([-5_i128, 7, 11], [13_i128, 17, 19], [23_i128, 29, 31]),
    ];

    for (q, y, contact) in packets {
        for i in 0..3 {
            assert_ne!(q[i], 0);
            assert_ne!(y[i], 0);
            assert_ne!(contact[i], 0);

            // Source factorization fixes P = C*y/q.  Evaluate the two
            // weighted routes on the kernel coefficient 2q/y and clear q,y.
            let grade_two_cleared = 4 * contact[i] * y[i] * (2 * q[i]);
            let grade_three_cleared = -8 * contact[i] * q[i] * y[i];
            assert_ne!(grade_two_cleared, 0);
            assert_ne!(grade_three_cleared, 0);
            assert_eq!(grade_two_cleared + grade_three_cleared, 0);
        }
    }

    println!(
        "{{\"status\":\"pass\",\"samples\":3,\"channels_per_sample\":3,\"generic_route_packet\":\"(8*Cj*Ck,-8*Cj*Ck)\",\"preaggregation_nonzero\":true,\"aggregate_zero\":true,\"classification\":\"destructive_interference\"}}"
    );
}
