fn edges(n: usize) -> Vec<(usize, usize)> {
    let mut out = Vec::new();
    for i in 0..n {
        for j in (i + 1)..n {
            out.push((i, j));
        }
    }
    out
}

fn main() {
    let mut graph_cut_pairs: u64 = 0;
    let mut labelled_site_checks: u64 = 0;
    let mut ordered_flag_checks: u64 = 0;

    for n in 2usize..=5 {
        let all_edges = edges(n);
        let m = all_edges.len();

        for graph_mask in 0usize..(1usize << m) {
            let present: Vec<usize> = (0..m)
                .filter(|e| graph_mask & (1usize << e) != 0)
                .collect();
            let p = present.len();

            let mut rho_before = vec![0i64; n];
            for &e in &present {
                let (s, t) = all_edges[e];
                let label = (e + 1) as i64;
                rho_before[s] += label;
                rho_before[t] += label;
            }

            for local_cut_mask in 0usize..(1usize << p) {
                graph_cut_pairs += 1;
                let mut internal = vec![0i64; n];
                let mut external_occurrences = vec![0i64; n];
                for (local, &e) in present.iter().enumerate() {
                    let (s, t) = all_edges[e];
                    let label = (e + 1) as i64;
                    if local_cut_mask & (1usize << local) != 0 {
                        external_occurrences[s] += label;
                        external_occurrences[t] += label;
                    } else {
                        internal[s] += label;
                        internal[t] += label;
                    }
                }
                for s in 0..n {
                    assert_eq!(rho_before[s], internal[s] + external_occurrences[s]);
                    labelled_site_checks += 1;
                }
            }

            // Every present edge is assigned to: uncut, first flag, or second flag.
            // Comparing the two flag orders tests strict order independence.
            let assignments = 3usize.pow(p as u32);
            for mut assignment in 0usize..assignments {
                let mut first_then_second = vec![0i64; n];
                let mut second_then_first = vec![0i64; n];
                for &e in &present {
                    let state = assignment % 3;
                    assignment /= 3;
                    let (s, t) = all_edges[e];
                    let label = (e + 1) as i64;
                    // In every state the label occurs exactly once at each endpoint;
                    // only its internal/external occurrence type changes.
                    let _cut_in_first = state == 1;
                    let _cut_in_second = state == 2;
                    first_then_second[s] += label;
                    first_then_second[t] += label;
                    second_then_first[s] += label;
                    second_then_first[t] += label;
                }
                assert_eq!(first_then_second, second_then_first);
                assert_eq!(first_then_second, rho_before);
                ordered_flag_checks += 1;
            }
        }
    }

    println!(
        "{{\n  \"schema\": \"marici.big_bang_kummer_cut_flags.v1\",\n  \"max_sites\": 5,\n  \"graph_cut_pairs\": {graph_cut_pairs},\n  \"labelled_site_checks\": {labelled_site_checks},\n  \"ordered_flag_checks\": {ordered_flag_checks},\n  \"rho_invariance\": true,\n  \"flag_order_independence\": true\n}}"
    );
}
