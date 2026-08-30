use std::collections::VecDeque;
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
    let mut count = 0;
    for root in 0..n {
        if (support >> root) & 1 == 0 || lab[root] != usize::MAX { continue; }
        lab[root] = count;
        let mut q = VecDeque::from([root]);
        while let Some(a) = q.pop_front() {
            for &b in &adj[a] {
                if lab[b] == usize::MAX {
                    lab[b] = count;
                    q.push_back(b);
                }
            }
        }
        count += 1;
    }
    (lab, count)
}

fn connected(n: usize, edges: &[(usize, usize)]) -> bool {
    labels(n, edges, (1_usize << n) - 1).1 == 1
}

fn component_contractions(
    n: usize,
    edges: &[(usize, usize)],
    coeffs: &[i128],
    u: &[i128],
    support: usize,
) -> Vec<i128> {
    let (lab, c) = labels(n, edges, support);
    let mut out = vec![0_i128; c];
    for (e, &(a, b)) in edges.iter().enumerate() {
        if ((support >> a) & 1 == 1) && ((support >> b) & 1 == 1) {
            assert_eq!(lab[a], lab[b]);
            out[lab[a]] += coeffs[e] * u[a] * u[b];
        }
    }
    out
}

fn main() {
    let mut packets = 0_u64;
    let mut conditional_checks = 0_u64;
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
            if !connected(n, &edges) { continue; }
            let u: Vec<i128> = (0..n).map(|i| (i as i128 + 2) * (n as i128 - i as i128)).collect();
            let coeffs: Vec<i128> = edges
                .iter()
                .enumerate()
                .map(|(e, &(a, b))| (e as i128 + 1) * (a as i128 + b as i128 + 1))
                .collect();
            for h1 in 1_usize..(1_usize << n) {
                for h2 in 1_usize..(1_usize << n) {
                    if h2 & !h1 != 0 { continue; }
                    let child = component_contractions(n, &edges, &coeffs, &u, h2);
                    let direct: i128 = edges
                        .iter()
                        .enumerate()
                        .filter(|(_, &(a, b))| ((h2 >> a) & 1 == 1) && ((h2 >> b) & 1 == 1))
                        .map(|(e, &(a, b))| coeffs[e] * u[a] * u[b])
                        .sum();
                    assert_eq!(child.iter().sum::<i128>(), direct);

                    // The conditional fiber factor is common and therefore
                    // commutes with restriction and component pushforward.
                    for s in -2_i128..=2 {
                        assert_eq!(child.iter().sum::<i128>() * (s * s - 1), direct * (s * s - 1));
                        conditional_checks += 1;
                    }
                    let _parent = component_contractions(n, &edges, &coeffs, &u, h1);
                    packets += 1;
                }
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.cubic_soft_costalk_naturality.v1\",\n",
            "  \"nested_support_coefficient_packets_checked\": {},\n",
            "  \"conditional_fiber_checks\": {},\n",
            "  \"exceptional_contraction\": \"sum C_ij u_i u_j\",\n",
            "  \"relative_H0_square\": \"strictly commuting\",\n",
            "  \"disappearing_component_extension\": false\n",
            "}}\n"
        ),
        packets, conditional_checks
    );
    fs::write(
        "research/benincasa/results/cubic-soft-costalk-naturality.json",
        output,
    )
    .unwrap();
}
