use std::collections::BTreeMap;

type Triple = BTreeMap<(usize, usize, usize), i128>;

fn binomial(n: usize, k: usize) -> i128 {
    let mut out = 1_i128;
    for i in 0..k { out = out * (n - i) as i128 / (i + 1) as i128; }
    out
}

fn add(out: &mut Triple, key: (usize, usize, usize), coefficient: i128) {
    *out.entry(key).or_insert(0) += coefficient;
}

fn theta_terms(n: usize) -> Vec<(usize, usize, i128)> {
    (1..n).map(|k| (k, n - k, -binomial(n, k))).collect()
}

fn main() {
    let mut degree_checks = 0usize;
    let mut tensor_coefficients_checked = 0usize;

    for n in 2_usize..=20 {
        let theta = theta_terms(n);
        let mut left = Triple::new();
        let mut right = Triple::new();

        // (Delta tensor 1)Theta
        for &(a, b, c) in &theta {
            for i in 0..=a { add(&mut left, (i, a - i, b), c * binomial(a, i)); }
        }
        // +(Theta tensor 1)Delta(p) = Theta(p) tensor 1
        for &(a, b, c) in &theta { add(&mut left, (a, b, 0), c); }

        // (1 tensor Delta)Theta
        for &(a, b, c) in &theta {
            for i in 0..=b { add(&mut right, (a, i, b - i), c * binomial(b, i)); }
        }
        // +(1 tensor Theta)Delta(p) = 1 tensor Theta(p)
        for &(a, b, c) in &theta { add(&mut right, (0, a, b), c); }

        left.retain(|_, v| *v != 0);
        right.retain(|_, v| *v != 0);
        assert_eq!(left, right);
        tensor_coefficients_checked += left.len();
        degree_checks += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.coleibniz_defect_cocycle.v1\",");
    println!("  \"interaction_degrees_checked\": {degree_checks},");
    println!("  \"triple_tensor_coefficients_checked\": {tensor_coefficients_checked},");
    println!("  \"coleibniz_defect_is_cohochschild_cocycle\": true,");
    println!("  \"independent_ternary_coherence_required\": false");
    println!("}}");
}
