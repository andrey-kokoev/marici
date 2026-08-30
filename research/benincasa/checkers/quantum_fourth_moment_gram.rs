fn determinant_formula(q: i64, r: i64, u: i64, z: i64, w: i64) -> i64 {
    (u - q * q) * (w - r * r) - (z - q * r) * (z - q * r) - 4 * q * q
}

fn main() {
    let mut admitted_checks = 0usize;
    for q in 1_i64..=6 {
        for r in -4_i64..=4 {
            for u in (q * q + 1)..=(q * q + 5) {
                for z in -10_i64..=10 {
                    // Choose W above the exact Schur/Robertson lower bound.
                    let variance_q2 = u - q * q;
                    let centered = z - q * r;
                    let numerator = centered * centered + 4 * q * q;
                    let w = r * r + (numerator + variance_q2 - 1) / variance_q2;
                    let det = determinant_formula(q, r, u, z, w);
                    assert!(u - q * q > 0);
                    assert!(det >= 0);
                    admitted_checks += 1;
                }
            }
        }
    }

    // At fixed Q=1, R=0, U=2, arbitrary Z is admitted by W=Z^2+4.
    let mut unbounded_witnesses = 0usize;
    for z in -100_i64..=100 {
        let w = z * z + 4;
        assert_eq!(determinant_formula(1, 0, 2, z, w), 0);
        unbounded_witnesses += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.quantum_fourth_moment_gram.v1\",");
    println!("  \"commutator\": \"[Q,P]=2i\",");
    println!("  \"operator_basis\": [\"1\",\"Q^2\",\"S=(QP+PQ)/2\"],");
    println!("  \"forced_imaginary_entry\": \"Im <Q^2 S>=2<Q^2>\",");
    println!("  \"psd_checks\": {admitted_checks},");
    println!("  \"unbounded_mixed_witnesses\": {unbounded_witnesses},");
    println!("  \"determinant_inequality\": \"Var(Q^2) Var(S) >= Cov(Q^2,S)^2 + 4<Q^2>^2\",");
    println!("  \"mixed_fourth_moment_bounded_without_S2\": false");
    println!("}}");
}
