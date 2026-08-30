use std::fs;

fn main() {
    let mut packets = 0_u64;
    let mut boundary_packets = 0_u64;
    for c in -17_i128..=17 {
        for residual in 0_i128..=13 {
            let b = c * c + residual * residual;
            assert!(b - c * c >= 0);
            for t in -7_i128..=7 {
                for x in -5_i128..=5 {
                    for y in -5_i128..=5 {
                        // Coefficients of 2K through epsilon^2.
                        let k0 = b * y * y;
                        let k1 = 2 * c * x * y;
                        let k2 = x * x - 2 * t * c * c * y.pow(3);
                        let d2 = 2 * t * y;

                        // Multiplying by D=1+d2 epsilon^2 must recover the
                        // exact rational numerator through the same grade.
                        let numerator0 = b * y * y;
                        let numerator1 = 2 * c * x * y;
                        let numerator2 = x * x + 2 * t * (b - c * c) * y.pow(3);
                        assert_eq!(k0, numerator0);
                        assert_eq!(k1, numerator1);
                        assert_eq!(k2 + d2 * k0, numerator2);
                        packets += 1;
                    }
                }
            }
            if residual == 0 { boundary_packets += 1; }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.correlated_generator_a0_rees.v1\",\n",
            "  \"exact_strict_transform_packets_checked\": {},\n",
            "  \"rank_one_boundary_packets_checked\": {},\n",
            "  \"weighted_coordinates\": \"A=epsilon^2; C=epsilon c\",\n",
            "  \"grade_zero\": \"B y^2/2\",\n",
            "  \"grade_one\": \"c x y\",\n",
            "  \"grade_two\": \"x^2/2-c^2 t y^3\",\n",
            "  \"new_coefficient_chart_required\": false\n",
            "}}\n"
        ),
        packets, boundary_packets
    );
    fs::write(
        "research/benincasa/results/correlated-generator-a0-rees.json",
        output,
    )
    .unwrap();
}
