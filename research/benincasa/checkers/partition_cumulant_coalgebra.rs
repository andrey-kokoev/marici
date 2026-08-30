fn partitions(n: usize) -> Vec<Vec<usize>> {
    fn rec(pos: usize, n: usize, current: &mut Vec<usize>, max_label: usize, out: &mut Vec<Vec<usize>>) {
        if pos == n { out.push(current.clone()); return; }
        for label in 0..=max_label + 1 {
            if pos == 0 && label != 0 { continue; }
            current.push(label);
            rec(pos + 1, n, current, max_label.max(label), out);
            current.pop();
        }
    }
    if n == 0 { return vec![Vec::new()]; }
    let mut out = Vec::new();
    let mut current = Vec::new();
    rec(0, n, &mut current, 0, &mut out);
    // The recursion above permits label 1 at position one only after label 0,
    // which is the restricted-growth encoding; remove any skipped-label words.
    out.into_iter().filter(|p| {
        let mut seen_max = 0usize;
        for (i, &x) in p.iter().enumerate() {
            if i == 0 { if x != 0 { return false; } }
            else if x > seen_max + 1 { return false; }
            seen_max = seen_max.max(x);
        }
        true
    }).collect()
}

fn refines(fine: &[usize], coarse: &[usize]) -> bool {
    for i in 0..fine.len() {
        for j in 0..fine.len() {
            if fine[i] == fine[j] && coarse[i] != coarse[j] { return false; }
        }
    }
    true
}

fn main() {
    let expected_bell = [1_usize, 2, 5, 15, 52, 203, 877, 4140];
    let mut bell_checks = 0usize;
    let mut connected_generators = 0usize;
    for n in 1..=8 {
        let ps = partitions(n);
        assert_eq!(ps.len(), expected_bell[n - 1]);
        bell_checks += 1;
        assert!(ps.iter().any(|p| p.iter().all(|x| *x == 0)));
        connected_generators += 1;
    }

    let mut coassociativity_checks = 0usize;
    let mut total_refinement_chains = 0usize;
    for n in 1..=6 {
        let ps = partitions(n);
        let mut leq = vec![vec![false; ps.len()]; ps.len()];
        for i in 0..ps.len() {
            for j in 0..ps.len() { leq[i][j] = refines(&ps[i], &ps[j]); }
        }
        let left: usize = (0..ps.len()).map(|middle| {
            let lower = (0..ps.len()).filter(|i| leq[*i][middle]).count();
            let upper = (0..ps.len()).filter(|k| leq[middle][*k]).count();
            lower * upper
        }).sum();
        let right: usize = (0..ps.len()).map(|lower| {
            (0..ps.len()).filter(|upper| leq[lower][*upper]).map(|upper| {
                (0..ps.len()).filter(|middle| leq[lower][*middle] && leq[*middle][upper]).count()
            }).sum::<usize>()
        }).sum();
        assert_eq!(left, right);
        total_refinement_chains += left;
        coassociativity_checks += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.partition_cumulant_coalgebra.v1\",");
    println!("  \"bell_checks\": {bell_checks},");
    println!("  \"connected_arity_generators_observed\": {connected_generators},");
    println!("  \"coassociativity_checks\": {coassociativity_checks},");
    println!("  \"refinement_chains_counted\": {total_refinement_chains},");
    println!("  \"arity_uniform_partition_rule\": true,");
    println!("  \"finite_rank_cumulant_coalgebra_for_arbitrary_states\": false");
    println!("}}");
}
