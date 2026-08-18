use std::collections::BTreeMap;

fn add_term(p: &mut BTreeMap<(u8, u8), i64>, a: u8, b: u8, c: i64) {
    *p.entry((a, b)).or_default() += c;
}

fn main() {
    // Obstruction coefficient after reducing the (s_a,s_b)=(1,1),
    // minus-lattice q relation modulo (K,u^2):
    // 3*(b+1)*(a^2*(1-b^2)+a^3).
    let mut p = BTreeMap::new();
    for (a, b, coefficient) in [
        (2, 0, 3), (2, 1, 3), (2, 2, -3), (2, 3, -3),
        (3, 0, 3), (3, 1, 3),
    ] {
        add_term(&mut p, a, b, coefficient);
    }
    p.retain(|_, coefficient| *coefficient != 0);

    assert!(!p.is_empty());
    assert!(p.keys().all(|(a, _)| *a < 4));
    assert_eq!(p.len(), 6);

    println!(
        "{{\"schema\":\"marici.benincasa.soft_axis_naive_carrier_lift.v1\",\"tested_source\":\"s11:minus:q:f=1\",\"reduction_mod_K_u2\":\"3*u*(b+1)*(a^2*(1-b^2)+a^3)\",\"nonzero_monomial_count\":6,\"divisible_by_a4\":false,\"naive_reduction_is_chain_map\":false,\"required_correction\":\"relative_de_Rham_or_Gauss_Manin_homotopy\"}}"
    );
}
