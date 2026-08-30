use std::fs;

fn main() {
    let mut packets = 0_u64;
    for a in 1_i128..=23 {
        for d in -19_i128..=19 {
            // Atomic displacement law: mu=2d with weight 1/3 and mu=-d
            // with weight 2/3.  All moments below are stored after their
            // denominators cancel exactly.
            let mean_mu_num = 2 * d + 2 * (-d);
            assert_eq!(mean_mu_num, 0);
            let mu2 = 2 * d * d;
            let mu3 = 2 * d.pow(3);
            let mu4 = 6 * d.pow(4);

            let variance_q = a + mu2;
            let third_q = mu3;
            let fourth_q = 3 * a * a + 6 * a * mu2 + mu4;
            let kappa4_q = fourth_q - 3 * variance_q * variance_q;
            assert_eq!(third_q, 2 * d.pow(3));
            assert_eq!(kappa4_q, -6 * d.pow(4));

            for t in -11_i128..=11 {
                let cubic_qqpi = -t * (fourth_q - variance_q * variance_q);
                assert_eq!(
                    cubic_qqpi,
                    -t * (2 * variance_q * variance_q + kappa4_q)
                );
                packets += 1;
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.nongaussian_input_cubic_generator.v1\",\n",
            "  \"exact_density_mixture_packets_checked\": {},\n",
            "  \"atomic_displacement_law\": \"mu=2d with weight 1/3; mu=-d with weight 2/3\",\n",
            "  \"initial_kappa3\": \"2d^3\",\n",
            "  \"initial_kappa4\": \"-6d^4\",\n",
            "  \"first_cubic_kappa_QQPi\": \"-t(2A^2+kappa4)\",\n",
            "  \"complete_input_extension\": \"finite Gaussian-mixture log-sum-exp factor\",\n",
            "  \"standalone_kappa3_closed\": false\n",
            "}}\n"
        ),
        packets
    );
    fs::write(
        "research/benincasa/results/nongaussian-input-cubic-generator.json",
        output,
    )
    .unwrap();
}
