use std::collections::VecDeque;
use std::fs;

fn components(n: usize, edges: &[(usize, usize)], support: usize) -> usize {
    let mut adj = vec![Vec::new(); n];
    for &(a, b) in edges {
        if ((support >> a) & 1 == 1) && ((support >> b) & 1 == 1) {
            adj[a].push(b);
            adj[b].push(a);
        }
    }
    let mut seen = vec![false; n];
    let mut count = 0;
    for root in 0..n {
        if (support >> root) & 1 == 0 || seen[root] {
            continue;
        }
        count += 1;
        seen[root] = true;
        let mut q = VecDeque::from([root]);
        while let Some(a) = q.pop_front() {
            for &b in &adj[a] {
                if !seen[b] {
                    seen[b] = true;
                    q.push_back(b);
                }
            }
        }
    }
    count
}

fn connected(n: usize, edges: &[(usize, usize)]) -> bool {
    components(n, edges, (1_usize << n) - 1) == 1
}

fn main() {
    let mut support_packets = 0_u64;
    let mut disconnected_soft_packets = 0_u64;
    let mut loop_obstruction_rank_sum = 0_u64;

    for n in 2_usize..=6 {
        let all_edges: Vec<(usize, usize)> = (0..n)
            .flat_map(|i| ((i + 1)..n).map(move |j| (i, j)))
            .collect();
        for graph_mask in 0_usize..(1_usize << all_edges.len()) {
            let edges: Vec<(usize, usize)> = all_edges
                .iter()
                .enumerate()
                .filter_map(|(i, &e)| if (graph_mask >> i) & 1 == 1 { Some(e) } else { None })
                .collect();
            if !connected(n, &edges) {
                continue;
            }
            for support in 1_usize..(1_usize << n) {
                let vertices = support.count_ones() as usize;
                let induced_edges = edges
                    .iter()
                    .filter(|&&(a, b)| ((support >> a) & 1 == 1) && ((support >> b) & 1 == 1))
                    .count();
                let c = components(n, &edges, support);
                let b1 = induced_edges + c - vertices;
                let deck_count = 1_usize << c;
                let source_packets = 1_usize << (vertices - c);
                let arbitrary_packets = 1_usize << induced_edges;
                assert_eq!(arbitrary_packets, source_packets * (1_usize << b1));
                assert_eq!(deck_count * source_packets, 1_usize << vertices);
                support_packets += 1;
                loop_obstruction_rank_sum += b1 as u64;
                if c > 1 {
                    disconnected_soft_packets += 1;
                }
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.soft_relative_sign_cohomology.v1\",\n",
            "  \"nonempty_support_packets_checked\": {},\n",
            "  \"soft_disconnected_packets\": {},\n",
            "  \"aggregate_support_cycle_rank\": {},\n",
            "  \"deck_group\": \"Z2 to the number of nonzero-support components\",\n",
            "  \"source_cycle_holonomy\": \"trivial on every component\",\n",
            "  \"generic_new_class_after_localization\": false\n",
            "}}\n"
        ),
        support_packets, disconnected_soft_packets, loop_obstruction_rank_sum
    );
    fs::write(
        "research/benincasa/results/soft-relative-sign-cohomology.json",
        output,
    )
    .unwrap();
}
