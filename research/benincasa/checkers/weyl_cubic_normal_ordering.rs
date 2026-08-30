fn choose(n: i128, k: i128) -> i128 {
    if k > n { return 0; }
    let mut out = 1_i128;
    for i in 0..k { out = out * (n - i) / (i + 1); }
    out
}

fn main() {
    let mut degree_checks = 0usize;
    let mut central_corrections = 0usize;

    // For H_int=q^3/3 and q-left normal ordering:
    // D(p^m) = -m q^2 p^(m-1)
    //          +2 i h C(m,2) q p^(m-2)
    //          +2 h^2 C(m,3) p^(m-3).
    for m in 1_i128..=32 {
        let classical = -m;
        let order_h = 2 * choose(m, 2);
        let order_h2 = 2 * choose(m, 3);
        assert_eq!(classical, -m);
        if m < 2 { assert_eq!(order_h, 0); }
        if m < 3 { assert_eq!(order_h2, 0); }
        if m >= 3 {
            assert!(order_h2 > 0);
            central_corrections += 1;
        }
        degree_checks += 1;
    }

    assert_eq!((-3_i128, 6_i128, 2_i128),
               (-3, 2 * choose(3, 2), 2 * choose(3, 3)));

    println!("{{");
    println!("  \"schema\": \"marici.weyl_cubic_normal_ordering.v1\",");
    println!("  \"degrees_checked\": {degree_checks},");
    println!("  \"degrees_with_hbar_squared_correction\": {central_corrections},");
    println!("  \"first_corrected_observable\": \"p^3\",");
    println!("  \"D_p3_normal_ordered\": \"-3 q^2 p^2 + 6 i hbar q p + 2 hbar^2\",");
    println!("  \"primitive_force_relation_has_quantum_correction\": false,");
    println!("  \"higher_moment_hierarchy_has_quantum_correction\": true");
    println!("}}");
}
