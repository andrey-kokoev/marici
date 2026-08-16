fn gcd(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        let r = a % b;
        a = b;
        b = r;
    }
    a
}

fn main() {
    // Conditional reduced endpoint calculation.  If the intrinsic odd KN
    // counit and the still-missing spatial restriction r_{partial,Q} extend
    // to the pointed mapping fiber, b=+1 and 2a+b=1 force a=0.
    let endpoint_row = [2_i64, 1_i64];
    assert_eq!(gcd(endpoint_row[0], endpoint_row[1]), 1);
    let odd_counit = 1_i64;
    let endpoint_rhs = 1_i64;
    let numerator = endpoint_rhs - odd_counit;
    assert_eq!(numerator % 2, 0);
    let a = numerator / 2;
    assert_eq!(a, 0);
    let p_partial_q = ((a % 2) + 2) % 2;
    assert_eq!(p_partial_q, 0);

    // The polarity connecting map H1(D3;Z_or)=Z/2 -> H2(D3;Z)=Z/2
    // is the identity on the residue representative.
    let polarity_bockstein = p_partial_q;
    assert_eq!(polarity_bockstein, 0);

    // Based generic Q normalization and endpoint augmentation.
    let qsigma_boundary = [1_i64, -1, -1, -1];
    assert_eq!(qsigma_boundary.iter().fold(0_i64, |g, x| gcd(g, *x)), 1);
    assert_eq!(3 - 1 - 1 - 1, 0);

    // D3 action on the three connector roads.
    let rotation = [1_usize, 2, 0];
    let reflection = [0_usize, 2, 1];
    let compose = |a: [usize; 3], b: [usize; 3]| [a[b[0]], a[b[1]], a[b[2]]];
    assert_eq!(compose(rotation, compose(rotation, rotation)), [0, 1, 2]);
    assert_eq!(compose(reflection, reflection), [0, 1, 2]);
    assert_eq!(
        compose(reflection, compose(rotation, reflection)),
        compose(rotation, rotation)
    );

    println!("{{\"status\":\"proved_conditional_reduced_endpoint_Q_consequence\",\"endpoint_row\":[2,1],\"endpoint_smith\":[1],\"normalized_odd_counit\":1,\"conditional_pointed_endpoint_scalar\":{},\"conditional_p_partial_Q\":{},\"H1_D3_Z_or\":\"Z/2\",\"conditional_polarity_bockstein\":{},\"H2_D3_Z\":\"Z/2\",\"qSigma_boundary\":[1,-1,-1,-1],\"qSigma_augmentation\":\"3-1-1-1=0\",\"D3_relations\":true,\"spatial_restriction_r_partial_Q_constructed\":false,\"mapping_fiber_instantiated\":false,\"physical_p_defined\":false,\"D8_tested\":false,\"Jordan_tested\":false}}",a,p_partial_q,polarity_bockstein);
}
