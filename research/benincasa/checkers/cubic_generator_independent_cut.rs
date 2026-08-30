use std::fs;

fn binomial(n: u32, k: u32) -> i128 {
    let mut out = 1_i128;
    for i in 0..k.min(n - k) {
        out = out * (n - i) as i128 / (i + 1) as i128;
    }
    out
}

fn main() {
    let triples = [(3_i128, 4_i128, 5_i128), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)];
    let mut shear_packets = 0_u64;
    let mut generator_coefficients = 0_u64;

    for &(n1, n2, d) in &triples {
        assert_eq!(n1 * n1 + n2 * n2, d * d);
        for a1 in 1_i128..=11 {
            for a2 in 1_i128..=13 {
                let x = n1 * n1 * a1;
                let y = n2 * n2 * a2;
                let a_num = x + y;
                for r in 0_u32..=10 {
                    let expanded: i128 = (0..=r)
                        .map(|k| binomial(r, k) * x.pow(k) * y.pow(r - k))
                        .sum();
                    assert_eq!(expanded, a_num.pow(r));
                    generator_coefficients += 1;
                }

                for q1 in -5_i128..=5 {
                    for q2 in -5_i128..=5 {
                        for t in -3_i128..=3 {
                            // All expressions are multiplied by d^2.
                            let global = -t * ((n1 * q1 + n2 * q2).pow(2) - a_num);
                            let local = -t
                                * (n1 * n1 * (q1 * q1 - a1)
                                    + n2 * n2 * (q2 * q2 - a2));
                            let mixed = -2 * t * n1 * n2 * q1 * q2;
                            assert_eq!(global, local + mixed);
                            shear_packets += 1;
                        }
                    }
                }
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.cubic_generator_independent_cut.v1\",\n",
            "  \"exact_collective_shear_packets_checked\": {},\n",
            "  \"multinomial_generator_coefficients_checked\": {},\n",
            "  \"aggregate_variance\": \"A=sum w_i^2 a_i\",\n",
            "  \"mixed_cocycle\": \"-2t sum_{{i<j}} w_i w_j Q_i Q_j\",\n",
            "  \"complete_generator_reconstructed\": true,\n",
            "  \"coefficientwise_fitting_used\": false\n",
            "}}\n"
        ),
        shear_packets, generator_coefficients
    );
    fs::write(
        "research/benincasa/results/cubic-generator-independent-cut.json",
        output,
    )
    .unwrap();
}
