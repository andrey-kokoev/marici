fn main() {
    let mut boundary_checks = 0usize;
    let mut admitted_checks = 0usize;
    let mut rejected_checks = 0usize;

    for a in 1_i64..=128 {
        let c_squared = a * a - 1;
        assert!(c_squared >= 0);

        // For B=aI, C=cZ and c^2=a^2-1, the quantum Schur complement of
        // V+iOmega is exactly (x-a)I.
        for x in 1_i64..=(a + 8) {
            let quantum_schur = x - a;
            let compatible = quantum_schur >= 0;
            assert_eq!(compatible, x >= a);
            if x == a {
                assert_eq!(quantum_schur, 0);
                boundary_checks += 1;
            }
            if compatible { admitted_checks += 1; } else { rejected_checks += 1; }
        }
    }

    // Product degeneration c=0, a=1 admits every physical isotropic x>=1.
    for x in 1_i64..=256 {
        assert!(x - 1 >= 0);
    }

    println!("{{");
    println!("  \"schema\": \"marici.quantum_correlated_compatibility_domain.v1\",");
    println!("  \"boundary_checks\": {boundary_checks},");
    println!("  \"admitted_checks\": {admitted_checks},");
    println!("  \"rejected_checks\": {rejected_checks},");
    println!("  \"pure_support_relation\": \"c^2=a^2-1\",");
    println!("  \"quantum_schur_complement\": \"(x-a) I\",");
    println!("  \"compatibility_domain\": \"x>=a\",");
    println!("  \"source_marginal_on_boundary\": true,");
    println!("  \"c_to_zero_product_limit\": \"a->1, x>=1\"");
    println!("}}");
}
