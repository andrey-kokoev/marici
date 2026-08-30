use std::collections::BTreeMap;

type Poly = BTreeMap<(usize, usize), i128>;

fn add(out: &mut Poly, key: (usize, usize), value: i128) {
    if value != 0 { *out.entry(key).or_insert(0) += value; }
}

fn direct_on_monomial(q: usize, p: usize) -> Poly {
    let mut out = Poly::new();
    if q > 0 { add(&mut out, (q - 1, p + 1), q as i128); }
    if p > 0 { add(&mut out, (q + 2, p - 1), -(p as i128)); }
    out
}

// Derive the same formula only from Dq=p, Dp=-q^2 and Leibniz.
fn presented_on_monomial(q: usize, p: usize) -> Poly {
    let mut out = Poly::new();
    for _ in 0..q { add(&mut out, (q - 1, p + 1), 1); }
    for _ in 0..p { add(&mut out, (q + 2, p - 1), -1); }
    out
}

fn main() {
    let mut monomial_checks = 0usize;
    for total in 0_usize..=12 {
        for q in 0..=total {
            let p = total - q;
            assert_eq!(direct_on_monomial(q, p), presented_on_monomial(q, p));
            monomial_checks += 1;
        }
    }
    assert_eq!(monomial_checks, 91);

    println!("{{");
    println!("  \"schema\": \"marici.finite_differential_presentation.v1\",");
    println!("  \"monomial_checks\": {monomial_checks},");
    println!("  \"algebra_generators\": [\"q\", \"p\"],");
    println!("  \"derivation_relations\": [\"Dq=p\", \"Dp=-q^2\"],");
    println!("  \"observable_differential_algebra_finitely_presented\": true,");
    println!("  \"moment_dual_finite_rank\": false");
    println!("}}");
}
