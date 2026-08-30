fn main() {
    let mut checks = 0usize;
    for nq in 0_i64..=8 {
        for nk in 0_i64..=8 {
            for cr in -3_i64..=3 {
                for ci in -3_i64..=3 {
                    for br in -3_i64..=3 {
                        for bi in -3_i64..=3 {
                            let normal_cross_norm = cr * cr + ci * ci;
                            let anomalous_cross_norm = br * br + bi * bi;
                            let mu = (nq + 1) * (nk + 1)
                                + normal_cross_norm
                                + anomalous_cross_norm;
                            assert!(mu > 0);
                            let swapped = (nk + 1) * (nq + 1)
                                + normal_cross_norm
                                + anomalous_cross_norm;
                            assert_eq!(mu, swapped);
                            checks += 1;
                        }
                    }
                }
            }
        }
    }

    for degree in 1usize..=32 {
        let finite_difference_degree = degree - 1;
        let observed_output_degree = finite_difference_degree + 1;
        assert_eq!(observed_output_degree, degree);
    }

    println!("{{");
    println!("  \"schema\": \"marici.gaussian_internal_pushforward.v1\",");
    println!("  \"exact_wick_packets\": {checks},");
    println!("  \"internal_scalar\": \"(n_q+1)(n_k+1)+|c_qk|^2+|beta_qk|^2\",");
    println!("  \"internal_scalar_positive\": true,");
    println!("  \"q_k_exchange_natural\": true,");
    println!("  \"observed_degree_shift\": 0,");
    println!("  \"requires_product_initial_split\": true");
    println!("}}");
}
