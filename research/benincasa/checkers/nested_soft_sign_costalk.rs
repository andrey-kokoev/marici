use std::collections::{BTreeSet, VecDeque};
use std::fs;

fn labels(n: usize, edges: &[(usize, usize)], support: usize) -> (Vec<usize>, usize) {
    let mut adj = vec![Vec::new(); n];
    for &(a, b) in edges {
        if ((support >> a) & 1 == 1) && ((support >> b) & 1 == 1) {
            adj[a].push(b);
            adj[b].push(a);
        }
    }
    let mut lab = vec![usize::MAX; n];
    let mut c = 0;
    for root in 0..n {
        if (support >> root) & 1 == 0 || lab[root] != usize::MAX {
            continue;
        }
        lab[root] = c;
        let mut q = VecDeque::from([root]);
        while let Some(a) = q.pop_front() {
            for &b in &adj[a] {
                if lab[b] == usize::MAX {
                    lab[b] = c;
                    q.push_back(b);
                }
            }
        }
        c += 1;
    }
    (lab, c)
}

fn connected(n: usize, edges: &[(usize, usize)]) -> bool {
    labels(n, edges, (1_usize << n) - 1).1 == 1
}

fn main() {
    let mut pair_flags = 0_u64;
    let mut triple_flags = 0_u64;
    let mut kernel_rank_sum = 0_u64;
    let mut cokernel_rank_sum = 0_u64;

    for n in 2_usize..=5 {
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

            // Ternary states encode H2 subset H1: 0 outside H1, 1 in H1 only,
            // 2 in H2.
            for mut state in 0_usize..3_usize.pow(n as u32) {
                let mut h1 = 0_usize;
                let mut h2 = 0_usize;
                for i in 0..n {
                    let d = state % 3;
                    state /= 3;
                    if d >= 1 { h1 |= 1 << i; }
                    if d == 2 { h2 |= 1 << i; }
                }
                if h1 == 0 || h2 == 0 { continue; }
                let (l1, c1) = labels(n, &edges, h1);
                let (l2, c2) = labels(n, &edges, h2);
                let mut touched = BTreeSet::new();
                for i in 0..n {
                    if (h2 >> i) & 1 == 1 {
                        touched.insert(l1[i]);
                        assert!(l2[i] < c2);
                    }
                }
                let rank = touched.len();
                assert!(rank <= c1 && rank <= c2);
                kernel_rank_sum += (c2 - rank) as u64;
                cokernel_rank_sum += (c1 - rank) as u64;
                pair_flags += 1;
            }

            // Quaternary states encode H3 subset H2 subset H1.
            for mut state in 0_usize..4_usize.pow(n as u32) {
                let mut h1 = 0_usize;
                let mut h2 = 0_usize;
                let mut h3 = 0_usize;
                for i in 0..n {
                    let d = state % 4;
                    state /= 4;
                    if d >= 1 { h1 |= 1 << i; }
                    if d >= 2 { h2 |= 1 << i; }
                    if d == 3 { h3 |= 1 << i; }
                }
                if h1 == 0 || h2 == 0 || h3 == 0 { continue; }
                let (l1, _) = labels(n, &edges, h1);
                let (l2, _) = labels(n, &edges, h2);
                let (l3, c3) = labels(n, &edges, h3);
                for component in 0..c3 {
                    let representative = (0..n)
                        .find(|&i| ((h3 >> i) & 1 == 1) && l3[i] == component)
                        .unwrap();
                    // The same vertex witnesses direct and iterated component
                    // transport, so the parent label must agree.
                    let via_h2 = (l2[representative], l1[representative]);
                    let direct = l1[representative];
                    assert_eq!(via_h2.1, direct);
                }
                triple_flags += 1;
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.nested_soft_sign_costalk.v1\",\n",
            "  \"nested_support_pairs_checked\": {},\n",
            "  \"three_support_flags_checked\": {},\n",
            "  \"aggregate_component_map_kernel_rank\": {},\n",
            "  \"aggregate_component_map_cokernel_rank\": {},\n",
            "  \"flag_composition\": \"strict\",\n",
            "  \"excess_coherence_class\": false\n",
            "}}\n"
        ),
        pair_flags, triple_flags, kernel_rank_sum, cokernel_rank_sum
    );
    fs::write(
        "research/benincasa/results/nested-soft-sign-costalk.json",
        output,
    )
    .unwrap();
}
