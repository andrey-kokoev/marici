use std::collections::VecDeque;
use std::fs;

fn connected(n: usize, edges: &[(usize, usize)]) -> bool {
    let mut adj = vec![Vec::new(); n];
    for &(a, b) in edges {
        adj[a].push(b);
        adj[b].push(a);
    }
    let mut seen = vec![false; n];
    seen[0] = true;
    let mut q = VecDeque::from([0_usize]);
    while let Some(a) = q.pop_front() {
        for &b in &adj[a] {
            if !seen[b] {
                seen[b] = true;
                q.push_back(b);
            }
        }
    }
    seen.into_iter().all(|x| x)
}

fn main() {
    let mut connected_graphs = 0_u64;
    let mut source_packets = 0_u64;
    let mut loop_rank_sum = 0_u64;

    for n in 2_usize..=6 {
        let all_edges: Vec<(usize, usize)> = (0..n)
            .flat_map(|i| ((i + 1)..n).map(move |j| (i, j)))
            .collect();
        for mask in 0_usize..(1_usize << all_edges.len()) {
            let edges: Vec<(usize, usize)> = all_edges
                .iter()
                .enumerate()
                .filter_map(|(i, &e)| if (mask >> i) & 1 == 1 { Some(e) } else { None })
                .collect();
            if !connected(n, &edges) {
                continue;
            }
            connected_graphs += 1;
            let b1 = edges.len() + 1 - n;
            loop_rank_sum += b1 as u64;

            // Source-derived edge signs are coboundaries s_i s_j.  There are
            // exactly 2^(n-1) distinct packets because s and -s agree.
            let mut packets = std::collections::BTreeSet::new();
            for signs in 0_usize..(1_usize << n) {
                let packet: Vec<bool> = edges
                    .iter()
                    .map(|&(a, b)| ((signs >> a) & 1) == ((signs >> b) & 1))
                    .collect();
                packets.insert(packet);
            }
            assert_eq!(packets.len(), 1_usize << (n - 1));
            // All edge packets number 2^m, leaving 2^b1 holonomy classes.
            assert_eq!(1_usize << edges.len(), packets.len() * (1_usize << b1));
            source_packets += packets.len() as u64;
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.covariance_loop_holonomy.v1\",\n",
            "  \"connected_labelled_graphs_checked\": {},\n",
            "  \"source_derived_edge_packets_checked\": {},\n",
            "  \"aggregate_cycle_rank\": {},\n",
            "  \"source_holonomy\": \"trivial\",\n",
            "  \"arbitrary_edge_obstruction\": \"H1(G,Z2)\",\n",
            "  \"new_generic_loop_coefficient\": false\n",
            "}}\n"
        ),
        connected_graphs, source_packets, loop_rank_sum
    );
    fs::write(
        "research/benincasa/results/covariance-loop-holonomy.json",
        output,
    )
    .unwrap();
}
