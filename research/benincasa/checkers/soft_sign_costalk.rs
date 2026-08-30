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

fn gf2_rank(mut cols: Vec<u64>) -> usize {
    let mut rank = 0;
    for bit in (0..64).rev() {
        if let Some(pivot) = (rank..cols.len()).find(|&i| ((cols[i] >> bit) & 1) == 1) {
            cols.swap(rank, pivot);
            for i in 0..cols.len() {
                if i != rank && ((cols[i] >> bit) & 1) == 1 {
                    cols[i] ^= cols[rank];
                }
            }
            rank += 1;
        }
    }
    rank
}

fn main() {
    let mut packets = 0_u64;
    let mut nonzero_costalks = 0_u64;
    let mut total_costalk_rank = 0_u64;
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
                let c = components(n, &edges, support);
                let incidence_cols: Vec<u64> = edges
                    .iter()
                    .filter_map(|&(a, b)| {
                        if ((support >> a) & 1 == 1) && ((support >> b) & 1 == 1) {
                            Some((1_u64 << a) | (1_u64 << b))
                        } else {
                            None
                        }
                    })
                    .collect();
                let incidence_rank = gf2_rank(incidence_cols);
                assert_eq!(incidence_rank, vertices - c);
                let h0_dim = vertices - incidence_rank;
                assert_eq!(h0_dim, c);
                let reduced_h0_dim = h0_dim - 1;
                assert_eq!(reduced_h0_dim, c - 1);
                packets += 1;
                total_costalk_rank += reduced_h0_dim as u64;
                if reduced_h0_dim > 0 {
                    nonzero_costalks += 1;
                }
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.soft_sign_costalk.v1\",\n",
            "  \"support_incidence_packets_checked\": {},\n",
            "  \"nonzero_costalk_packets\": {},\n",
            "  \"aggregate_reduced_h0_rank\": {},\n",
            "  \"costalk\": \"reduced H0(H,Z2) of rank c(H)-1\",\n",
            "  \"source\": \"existing labelled Cut incidence boundary\",\n",
            "  \"new_carrier_stratum\": false\n",
            "}}\n"
        ),
        packets, nonzero_costalks, total_costalk_rank
    );
    fs::write(
        "research/benincasa/results/soft-sign-costalk.json",
        output,
    )
    .unwrap();
}
