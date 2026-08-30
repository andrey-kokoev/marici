fn main() {
    let probes = [(0_i64, 1_i64), (1, 1), (1, -1), (2, 1)];
    let mut assignments = 0usize;
    let mut markov_cases = 0usize;
    let mut detected_memory_cases = 0usize;

    // In one quadrature, the second-step observed covariance discrepancy is
    // delta = y^2 (B'-B0) + 2 x y C'.  Equality for all second-step blocks
    // (x,y) is equivalent to B'=B0 and C'=0.
    for b_delta in -8_i64..=8 {
        for cross in -8_i64..=8 {
            let invisible_to_all = probes.iter().all(|(x, y)| {
                y * y * b_delta + 2 * x * y * cross == 0
            });
            assert_eq!(invisible_to_all, b_delta == 0 && cross == 0);
            assignments += 1;
            if invisible_to_all { markov_cases += 1; } else { detected_memory_cases += 1; }
        }
    }

    println!("{{");
    println!("  \"schema\": \"marici.gaussian_markov_factorization_criterion.v1\",");
    println!("  \"assignments_checked\": {assignments},");
    println!("  \"markov_cases\": {markov_cases},");
    println!("  \"detected_memory_cases\": {detected_memory_cases},");
    println!("  \"universal_early_pushforward_criterion\": \"B'=B0 and C'=0\"");
    println!("}}");
}
