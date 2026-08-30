// Exact tensor-factor no-go for branch-only activation of route interference.

fn main() {
    let route_packet = [1_i128, -1];
    let route_sum = [1_i128, 1];
    let branch_vectors = [[1_i128, 0], [0, 1], [3, -5], [-7, 11]];
    let branch_ops = [
        [[1_i128, 0], [0, 1]],
        [[0, 1], [1, 0]],
        [[2, -3], [5, 7]],
    ];
    let branch_covectors = [[1_i128, 1], [1, -1], [13, -17]];

    let route_pairing = route_sum[0] * route_packet[0] + route_sum[1] * route_packet[1];
    assert_eq!(route_pairing, 0);

    for b in branch_vectors {
        for d in branch_ops {
            let db = [
                d[0][0] * b[0] + d[0][1] * b[1],
                d[1][0] * b[0] + d[1][1] * b[1],
            ];
            for lambda in branch_covectors {
                let branch_pairing = lambda[0] * db[0] + lambda[1] * db[1];
                assert_eq!(route_pairing * branch_pairing, 0);
            }
        }
    }

    println!(
        "{{\"status\":\"pass\",\"route_packet\":[1,-1],\"route_readout\":[1,1],\"branch_vectors\":4,\"branch_operators\":3,\"branch_covectors\":3,\"all_tensor_pairings_zero\":true,\"required_activation\":\"mixed_route_branch_operator_or_route_resolving_covector\"}}"
    );
}
