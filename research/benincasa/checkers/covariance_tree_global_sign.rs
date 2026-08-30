use std::collections::VecDeque;
use std::fs;

fn decode_prufer(n: usize, code: &[usize]) -> Vec<(usize, usize)> {
    let mut degree = vec![1_usize; n];
    for &v in code {
        degree[v] += 1;
    }
    let mut edges = Vec::with_capacity(n - 1);
    for &v in code {
        let leaf = (0..n).find(|&i| degree[i] == 1).unwrap();
        edges.push((leaf, v));
        degree[leaf] -= 1;
        degree[v] -= 1;
    }
    let rest: Vec<usize> = (0..n).filter(|&i| degree[i] == 1).collect();
    edges.push((rest[0], rest[1]));
    edges
}

fn codes(n: usize) -> Vec<Vec<usize>> {
    let len = n - 2;
    let count = n.pow(len as u32);
    let mut out = Vec::with_capacity(count);
    for mut value in 0..count {
        let mut code = vec![0_usize; len];
        for digit in &mut code {
            *digit = value % n;
            value /= n;
        }
        out.push(code);
    }
    out
}

fn reconstruct(n: usize, edges: &[(usize, usize)], products: &[i8], root_sign: i8) -> Vec<i8> {
    let mut adj = vec![Vec::<(usize, i8)>::new(); n];
    for (&(a, b), &p) in edges.iter().zip(products) {
        adj[a].push((b, p));
        adj[b].push((a, p));
    }
    let mut signs = vec![0_i8; n];
    signs[0] = root_sign;
    let mut queue = VecDeque::from([0_usize]);
    while let Some(a) = queue.pop_front() {
        for &(b, p) in &adj[a] {
            if signs[b] == 0 {
                signs[b] = p * signs[a];
                queue.push_back(b);
            }
        }
    }
    signs
}

fn main() {
    let mut trees = 0_u64;
    let mut sign_packets = 0_u64;
    for n in 2_usize..=7 {
        for code in codes(n) {
            let edges = decode_prufer(n, &code);
            trees += 1;
            for mask in 0_usize..(1_usize << n) {
                let source: Vec<i8> = (0..n)
                    .map(|i| if (mask >> i) & 1 == 0 { 1 } else { -1 })
                    .collect();
                let products: Vec<i8> = edges.iter().map(|&(a, b)| source[a] * source[b]).collect();
                let plus = reconstruct(n, &edges, &products, 1);
                let minus = reconstruct(n, &edges, &products, -1);
                assert!(plus == source || plus.iter().zip(&source).all(|(a, b)| *a == -*b));
                assert!(minus.iter().zip(&plus).all(|(a, b)| *a == -*b));
                sign_packets += 1;
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.covariance_tree_global_sign.v1\",\n",
            "  \"labelled_trees_checked\": {},\n",
            "  \"nonsoft_sign_packets_checked\": {},\n",
            "  \"generic_deck_group\": \"Z2 global sign\",\n",
            "  \"soft_zero_effect\": \"sign propagation splits by connected component\",\n",
            "  \"identified_with_cosmological_time_root\": false\n",
            "}}\n"
        ),
        trees, sign_packets
    );
    fs::write(
        "research/benincasa/results/covariance-tree-global-sign.json",
        output,
    )
    .unwrap();
}
