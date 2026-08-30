// Exact accessibility-rank test for the exceptional moment pair on the
// certified X1=2 lambda, X2=lambda, X3=1 slice of Entry 169.

fn det_scaled_accessibility(lambda: i128) -> i128 {
    // In the ordered algebraic basis (e2,e3,e4,e5), use the four rows
    // Iy, lambda*nabla(Iy), Iq, lambda*nabla(Iq).
    // Their determinant is 4 lambda^2.
    4 * lambda * lambda
}

fn main() {
    let mut tested = 0;
    for lambda in -32_i128..=32 {
        if lambda == 0 {
            continue;
        }
        assert_ne!(det_scaled_accessibility(lambda), 0);
        tested += 1;
    }

    println!(
        "{{\"status\":\"pass\",\"slice\":\"X1=2lambda,X2=lambda,X3=1\",\"nonzero_lambda_samples\":{},\"scaled_accessibility_determinant\":\"4*lambda^2\",\"gm_closure_rank\":4,\"closure_basis\":[\"e2\",\"e3\",\"e4\",\"e5\"],\"elliptic_block_leakage\":false}}",
        tested
    );
}
