use std::collections::BTreeMap;

type Poly = BTreeMap<(usize, usize), i128>; // (q degree, p degree)

fn add_term(out: &mut Poly, key: (usize, usize), value: i128) {
    if value == 0 { return; }
    *out.entry(key).or_insert(0) += value;
    if out.get(&key) == Some(&0) { out.remove(&key); }
}

// Hamiltonian derivation D f = {f, p^2/2 + q^3/3}
// = p d_q f - q^2 d_p f.
fn derivation(f: &Poly) -> Poly {
    let mut out = Poly::new();
    for (&(q, p), &coefficient) in f {
        if q > 0 { add_term(&mut out, (q - 1, p + 1), coefficient * q as i128); }
        if p > 0 { add_term(&mut out, (q + 2, p - 1), -coefficient * p as i128); }
    }
    out
}

fn max_degree(f: &Poly) -> usize {
    f.keys().map(|(q, p)| q + p).max().unwrap_or(0)
}

fn main() {
    let mut f = Poly::from([((1_usize, 0_usize), 1_i128)]); // q
    let mut degrees = Vec::new();
    let mut strict_degree_increases = 0usize;
    let mut previous = max_degree(&f);
    degrees.push(previous);

    for _ in 0..24 {
        f = derivation(&f);
        assert!(!f.is_empty());
        let degree = max_degree(&f);
        if degree > previous { strict_degree_increases += 1; }
        previous = degree;
        degrees.push(degree);
    }

    assert!(degrees.last().copied().unwrap() >= 9);
    assert!(strict_degree_increases >= 8);

    let rendered = degrees.iter().map(|d| d.to_string()).collect::<Vec<_>>().join(",");
    println!("{{");
    println!("  \"schema\": \"marici.free_cubic_moment_hierarchy.v1\",");
    println!("  \"iterations\": 24,");
    println!("  \"degree_sequence\": \"{rendered}\",");
    println!("  \"strict_degree_increases\": {strict_degree_increases},");
    println!("  \"final_max_degree\": {},", degrees.last().unwrap());
    println!("  \"finite_degree_moment_closure\": false");
    println!("}}");
}
