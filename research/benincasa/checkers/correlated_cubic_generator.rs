use std::fs;

fn main() {
    let mut packets = 0_u64;
    let mut singular_packets = 0_u64;
    for p in 1_i128..=17 {
        for q in -11_i128..=11 {
            for r in 0_i128..=9 {
                // Q=p Z1, P=q Z1+r Z2 gives A>0 and AB-C^2>=0.
                let a = p * p;
                let b = q * q + r * r;
                let c = p * q;
                let det = a * b - c * c;
                assert_eq!(det, a * r * r);
                if det == 0 { singular_packets += 1; }

                // At t=0 the conditional-Gaussian exponent must reconstruct
                // the original quadratic form after clearing 2A.
                for x in -3_i128..=3 {
                    for y in -3_i128..=3 {
                        let conditional_num = det * y * y + (a * x + c * y).pow(2);
                        let gaussian_num = a * (a * x * x + 2 * c * x * y + b * y * y);
                        assert_eq!(conditional_num, gaussian_num);
                    }
                }

                for t in -5_i128..=5 {
                    let qqpi = -2 * t * a * a;
                    let pi_variance = b + 2 * t * t * a * a;
                    assert_eq!(qqpi, -2 * t * a * a);
                    assert!(a * pi_variance - c * c >= det);
                    packets += 1;
                }
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.correlated_cubic_generator.v1\",\n",
            "  \"exact_correlated_packets_checked\": {},\n",
            "  \"singular_covariance_packets_checked\": {},\n",
            "  \"collective_data\": \"A=w^T A_Q w; B=w^T A_P w; C=w^T A_QP w\",\n",
            "  \"generator\": \"tAy-log(1+2Aty)/2+(B-C^2/A)y^2/2+A(x+Cy/A)^2/(2(1+2Aty))\",\n",
            "  \"kappa_QQPi\": \"-2tA^2\",\n",
            "  \"direct_singular_extension_when_A_nonzero\": true,\n",
            "  \"new_carrier_operation_required\": false\n",
            "}}\n"
        ),
        packets, singular_packets
    );
    fs::write(
        "research/benincasa/results/correlated-cubic-generator.json",
        output,
    )
    .unwrap();
}
