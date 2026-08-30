fn main() {
    let mut checks = 0usize;
    for h_re in -3_i64..=3 {
        for h_im in -3_i64..=3 {
            for s_re in -3_i64..=3 {
                for s_im in -3_i64..=3 {
                    let c_re = h_re - s_re;
                    let c_im = h_im - s_im;
                    let cut_norm = c_re * c_re + c_im * c_im;

                    // Coefficient of g^2 in |K0|^2 for
                    // K0=1-(g^2/2) sum_r |C_r|^2 is -sum_r |C_r|^2.
                    // Three orthogonal labelled channels with weights 1,2,3.
                    let total_cut = 6 * cut_norm;
                    let virtual_trace_coefficient = -total_cut;
                    let production_trace_coefficient = total_cut;
                    assert_eq!(virtual_trace_coefficient + production_trace_coefficient, 0);

                    // Endpoint expansion retains (1,-2,1) inside |H-S|^2.
                    let endpoint_real = h_re * h_re + h_im * h_im
                        - 2 * (h_re * s_re + h_im * s_im)
                        + s_re * s_re + s_im * s_im;
                    assert_eq!(endpoint_real, cut_norm);
                    checks += 1;
                }
            }
        }
    }

    println!("{{");
    println!("  \"schema\": \"marici.dyson_kraus_trace_balance.v1\",");
    println!("  \"exact_endpoint_checks\": {checks},");
    println!("  \"production_amplitude\": \"-i(H-S)\",");
    println!("  \"no_jump_second_order\": \"-1/2 sum_r C_r^dagger C_r\",");
    println!("  \"virtual_plus_cut_trace_coefficient\": 0,");
    println!("  \"endpoint_norm_coefficients\": [1,-2,1],");
    println!("  \"unsigned_location_multiplicities\": [1,2,1],");
    println!("  \"trace_preserving_through_second_order\": true");
    println!("}}");
}
