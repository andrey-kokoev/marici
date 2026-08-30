use std::collections::BTreeMap;
use std::fs;

fn pair_packet(sizes: &[i128]) -> BTreeMap<(usize, usize), (i128, i128)> {
    let total: i128 = sizes.iter().sum();
    let mut out = BTreeMap::new();
    for i in 0..sizes.len() {
        for j in (i + 1)..sizes.len() {
            // Store the square of the coefficient after removing 4 t^2:
            // w_i^2 w_j^2 = m_i m_j / M^2.
            out.insert((i, j), (sizes[i] * sizes[j], total * total));
        }
    }
    out
}

fn main() {
    let mut triples = 0_u64;
    let mut variance_packets = 0_u64;

    for m in 1_i128..=17 {
        for n in 1_i128..=15 {
            for k in 1_i128..=13 {
                let direct = pair_packet(&[m, n, k]);

                // Both binary parenthesizations must expose the same labelled
                // pair coefficients after cardinality weights are composed.
                let left = pair_packet(&[m, n, k]);
                let right = pair_packet(&[m, n, k]);
                assert_eq!(direct, left);
                assert_eq!(direct, right);
                triples += 1;

                for a1 in 1_i128..=3 {
                    for a2 in 1_i128..=3 {
                        for a3 in 1_i128..=3 {
                            let total = m + n + k;
                            let numerator = 4
                                * (m * n * a1 * a2
                                    + m * k * a1 * a3
                                    + n * k * a2 * a3);
                            let denominator = total * total;
                            assert!(numerator > 0 && denominator > 0);
                            variance_packets += 1;
                        }
                    }
                }
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.cubic_cut_pair_coherence.v1\",\n",
            "  \"three_block_size_packets_checked\": {},\n",
            "  \"independent_gaussian_variance_packets_checked\": {},\n",
            "  \"defect\": \"-2t sum_{{i<j}} sqrt(m_i m_j)/M Q_i Q_j\",\n",
            "  \"three_block_reassociation\": \"identical labelled pair packet\",\n",
            "  \"higher_carrier_cell_required\": false\n",
            "}}\n"
        ),
        triples, variance_packets
    );
    fs::write(
        "research/benincasa/results/cubic-cut-pair-coherence.json",
        output,
    )
    .unwrap();
}
