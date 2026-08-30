#[derive(Clone, Copy)]
struct SupportInterval { lo: f64, hi: f64 }

fn external_support(q: SupportInterval, k: SupportInterval) -> SupportInterval {
    // Union of |q-k| <= p <= q+k over nonnegative radial supports.
    let lo = if q.hi < k.lo { k.lo - q.hi }
        else if k.hi < q.lo { q.lo - k.hi }
        else { 0.0 };
    SupportInterval { lo, hi: q.hi + k.hi }
}

fn main() {
    let cutoff = 1.0;
    let excited_q = SupportInterval { lo: 0.0, hi: cutoff };
    let vacuum_k = SupportInterval { lo: 0.0, hi: cutoff };
    let output = external_support(excited_q, vacuum_k);
    assert_eq!(output.lo, 0.0);
    assert_eq!(output.hi, 2.0 * cutoff);

    // Every momentum in the EFT observation domain receives a permitted
    // middle-placement contribution, including momenta where beta_p itself
    // can be zero.  Explicit witnesses avoid an inference from dimensions.
    for p in [0.1, 0.5, 0.9, 1.0] {
        let q = 0.5 * p;
        let k = 0.5 * p;
        assert!(q <= cutoff && k <= cutoff);
        assert!((p - (q + k)).abs() < 1e-14);
    }

    println!("{{");
    println!("  \"schema\": \"marici.gaussian_dyson_support_spread.v1\",");
    println!("  \"input_excited_support\": \"0<=q<=Lambda\",");
    println!("  \"vacuum_partner_support\": \"0<=k<=Lambda\",");
    println!("  \"convolution_external_support\": \"0<=p<=2Lambda\",");
    println!("  \"covers_entire_eft_observation_domain\": true,");
    println!("  \"pointwise_beta_support_is_dyson_invariant\": false");
    println!("}}");
}
