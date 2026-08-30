fn admitted(q: f64, k: f64, cutoff: f64) -> bool {
    q > 0.0 && k > 0.0 && q <= cutoff && k <= cutoff
}

fn density(q: f64, k: f64) -> f64 {
    1.0 / (4.0 * q * k)
}

fn main() {
    let cutoff = 1.0;
    let mut tested = 0usize;
    for iq in 1..=40 {
        for ik in 1..=40 {
            let q = iq as f64 / 40.0;
            let k = ik as f64 / 40.0;
            assert_eq!(admitted(q, k, cutoff), admitted(k, q, cutoff));
            if admitted(q, k, cutoff) {
                assert!(density(q, k) > 0.0);
                assert_eq!(density(q, k), density(k, q));
                tested += 1;
            }
        }
    }
    println!("{{");
    println!("  \"schema\": \"marici.finite_eft_cut_measure.v1\",");
    println!("  \"domain\": \"theta(Lambda-q) theta(Lambda-k)\",");
    println!("  \"density\": \"d^3q/(2q 2k)\",");
    println!("  \"positive\": true,");
    println!("  \"q_k_invariant\": true,");
    println!("  \"admitted_grid_points\": {tested},");
    println!("  \"one_sided_q_cutoff_admissible\": false");
    println!("}}");
}
