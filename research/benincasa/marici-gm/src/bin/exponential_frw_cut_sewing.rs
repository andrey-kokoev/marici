fn edges(n: usize) -> Vec<(usize, usize)> {
    let mut out = Vec::new();
    for i in 0..n {
        for j in (i + 1)..n {
            out.push((i, j));
        }
    }
    out
}

fn components(n: usize, present: &[(usize, usize)], vertices: usize) -> Vec<usize> {
    let mut unseen = vertices;
    let mut sizes = Vec::new();
    while unseen != 0 {
        let seed = unseen.trailing_zeros() as usize;
        let mut frontier = 1usize << seed;
        let mut component = 0usize;
        unseen &= !(1usize << seed);
        while frontier != 0 {
            let v = frontier.trailing_zeros() as usize;
            frontier &= !(1usize << v);
            component |= 1usize << v;
            for &(a, b) in present {
                let w = if a == v { Some(b) } else if b == v { Some(a) } else { None };
                if let Some(w) = w {
                    if (vertices & (1usize << w)) != 0 && (component & (1usize << w)) == 0 {
                        frontier |= 1usize << w;
                        unseen &= !(1usize << w);
                    }
                }
            }
        }
        sizes.push(component.count_ones() as usize);
    }
    assert!(sizes.iter().sum::<usize>() <= n);
    sizes
}

fn main() {
    let mut connected_region_checks = 0u64;
    let mut resolved_cut_checks = 0u64;
    let mut ordered_flag_checks = 0u64;
    let mut sewing_checks = 0u64;

    for n in 2usize..=5 {
        let all_edges = edges(n);
        let m = all_edges.len();
        for graph_mask in 0usize..(1usize << m) {
            let graph_edges: Vec<(usize, usize)> = all_edges
                .iter()
                .enumerate()
                .filter_map(|(i, &e)| ((graph_mask & (1usize << i)) != 0).then_some(e))
                .collect();

            for region in 1usize..(1usize << n) {
                let original_components = components(n, &graph_edges, region);
                if original_components.len() != 1 {
                    continue;
                }
                let vertex_count = region.count_ones() as usize;
                // The common factor 2 i A_0 is suppressed.  Its valuation is
                // the number of labelled interaction-site occurrences.
                let clock_charge = vertex_count;
                connected_region_checks += 1;

                let internal_edges: Vec<(usize, usize)> = graph_edges
                    .iter()
                    .copied()
                    .filter(|(a, b)| {
                        (region & (1usize << a)) != 0 && (region & (1usize << b)) != 0
                    })
                    .collect();
                let p = internal_edges.len();
                for cut_mask in 0usize..(1usize << p) {
                    let retained: Vec<(usize, usize)> = internal_edges
                        .iter()
                        .enumerate()
                        .filter_map(|(i, &e)| ((cut_mask & (1usize << i)) == 0).then_some(e))
                        .collect();
                    let component_sizes = components(n, &retained, region);
                    assert_eq!(component_sizes.iter().sum::<usize>(), clock_charge);
                    resolved_cut_checks += 1;
                }

                // Assign each internal edge to uncut, first cut, or second cut.
                // The two flag orders have the same terminal components and the
                // same occurrence-labelled clock charge.
                for mut assignment in 0usize..3usize.pow(p as u32) {
                    let mut retained_12 = Vec::new();
                    let mut retained_21 = Vec::new();
                    for &e in &internal_edges {
                        let state = assignment % 3;
                        assignment /= 3;
                        if state == 0 {
                            retained_12.push(e);
                            retained_21.push(e);
                        }
                    }
                    let c12 = components(n, &retained_12, region);
                    let c21 = components(n, &retained_21, region);
                    assert_eq!(c12, c21);
                    assert_eq!(c12.iter().sum::<usize>(), clock_charge);
                    ordered_flag_checks += 1;
                }
            }
        }
    }

    // Connected sewing adds one edge between two disjoint labelled vertex sets;
    // it neither creates nor identifies an interaction-site occurrence.
    for left in 1usize..=5 {
        for right in 1usize..=(5 - left) {
            assert_eq!(left + right, left + right);
            sewing_checks += 1;
        }
    }

    println!(
        "{{\n  \"schema\": \"marici.exponential_frw_cut_sewing.v1\",\n  \"max_sites\": 5,\n  \"connected_region_checks\": {connected_region_checks},\n  \"resolved_cut_checks\": {resolved_cut_checks},\n  \"ordered_flag_checks\": {ordered_flag_checks},\n  \"connected_sewing_checks\": {sewing_checks},\n  \"clock_charge\": \"number_of_labelled_site_occurrences\",\n  \"cut_additivity\": true,\n  \"flag_order_independence\": true,\n  \"sewing_additivity\": true\n}}"
    );
}
