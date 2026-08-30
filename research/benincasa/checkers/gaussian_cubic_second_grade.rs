use std::fs;

fn main() {
    let mut checks = 0_u64;

    for a in 1_i128..=23 {
        for b in 1_i128..=17 {
            for t in -11_i128..=11 {
                let x2 = 2 * a * a;
                let q2_pi2 = a * b + 10 * t * t * a * a * a;
                let pi2 = b + t * t * x2;
                let k_qqpp = q2_pi2 - a * pi2;
                assert_eq!(k_qqpp, 8 * t * t * a * a * a);

                // X=Q^2-a has fourth centered moment 60 a^4.
                let x4 = 60 * a.pow(4);
                let pi4 = 3 * b * b
                    + 12 * t * t * b * a * a
                    + t.pow(4) * x4;
                let k_pppp = pi4 - 3 * pi2 * pi2;
                assert_eq!(k_pppp, 48 * t.pow(4) * a.pow(4));

                checks += 1;
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.gaussian_cubic_second_grade.v1\",\n",
            "  \"exact_parameter_packets_checked\": {},\n",
            "  \"mixed_fourth_cumulant\": \"kappa_QQPiPi=8 t^2 a^3\",\n",
            "  \"momentum_fourth_cumulant\": \"kappa_PiPiPiPi=48 t^4 a^4\",\n",
            "  \"first_connected_fourth_normal_order\": 2,\n",
            "  \"degree_six_completion\": \"fixed by the exact unitary orbit\"\n",
            "}}\n"
        ),
        checks
    );

    fs::write(
        "research/benincasa/results/gaussian-cubic-second-grade.json",
        output,
    )
    .unwrap();
}
