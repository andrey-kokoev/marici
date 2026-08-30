// Exact labelled-edge Euler localization for the three contact channels.

fn main() {
    // Edge order: 12,23,31. Each grade-two route omits exactly its retained edge.
    let grade_two_counts = [[0_i128, 1, 1], [1, 0, 1], [1, 1, 0]];
    let grade_three_counts = [1_i128, 1, 1];
    let contacts = [5_i128, 7, 11];

    for channel in 0..3 {
        let a = 8 * contacts[channel];
        let b = -a;
        for edge in 0..3 {
            let response = grade_two_counts[channel][edge] * a
                + grade_three_counts[edge] * b;
            if edge == channel {
                assert_eq!(response, -8 * contacts[channel]);
            } else {
                assert_eq!(response, 0);
            }
        }
    }

    println!(
        "{{\"status\":\"pass\",\"edge_order\":[\"12\",\"23\",\"31\"],\"grade_two_count_rows\":[[0,1,1],[1,0,1],[1,1,0]],\"grade_three_count\":[1,1,1],\"edgewise_response_matrix\":\"diag(-8*C12,-8*C23,-8*C31)\",\"shared_edge_responses_zero\":true,\"last_edge_selector_localized\":true}}"
    );
}
