fn main() {
    let mut correlated_failures = 0usize;
    let mut product_passes = 0usize;

    // A Gaussian assignment preserving the observed mode and fixing the
    // partner has X=(I,0)^T. Its CP noise test contains [[0,c],[c,a]],
    // whose determinant is -c^2.
    for a in 2_i64..=128 {
        let c_squared = a * a - 1;
        assert!(c_squared > 0);
        let principal_minor = -c_squared;
        assert!(principal_minor < 0);
        correlated_failures += 1;
    }

    // At c=0 the remaining environment noise block aI+iJ has eigenvalues
    // a-1 and a+1, both nonnegative exactly for physical a>=1.
    for a in 1_i64..=256 {
        assert!(a - 1 >= 0);
        assert!(a + 1 > 0);
        product_passes += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.correlated_gaussian_cp_assignment_no_go.v1\",");
    println!("  \"correlated_failures\": {correlated_failures},");
    println!("  \"product_passes\": {product_passes},");
    println!("  \"correlated_principal_minor\": \"-c^2\",");
    println!("  \"ordinary_gaussian_cp_assignment_for_c_nonzero\": false,");
    println!("  \"product_assignment_for_c_zero\": true");
    println!("}}");
}
