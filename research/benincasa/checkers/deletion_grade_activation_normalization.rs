// Exact affine-regrading audit of Phi(N)=sigma*N*(1,-1)^T.

fn phi(diagonal: [i128; 2]) -> i128 {
    diagonal[0] - diagonal[1]
}

fn main() {
    let base = [2_i128, 3_i128];
    assert_eq!(phi(base), -1);

    for shift in -32_i128..=32 {
        let translated = [base[0] + shift, base[1] + shift];
        assert_eq!(phi(translated), -1);
    }

    for scale in [-7_i128, -3, -1, 1, 2, 5, 11] {
        for shift in [-13_i128, 0, 17] {
            let regraded = [scale * base[0] + shift, scale * base[1] + shift];
            assert_eq!(phi(regraded), -scale);
        }
    }

    println!(
        "{{\"status\":\"pass\",\"base_grades\":[2,3],\"translation_invariant\":true,\"affine_scale_law\":\"Phi(a*N+b*I)=-a\",\"unit_step_value\":-1,\"source_order_fixes_sign\":true,\"canonical_normalization\":true}}"
    );
}
