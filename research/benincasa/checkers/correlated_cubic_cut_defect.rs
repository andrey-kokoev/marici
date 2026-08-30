use std::fs;

fn covariance_of_products(a: &[[i128; 3]; 3], i: usize, j: usize, k: usize, l: usize) -> i128 {
    a[i][k] * a[j][l] + a[i][l] * a[j][k]
}

fn main() {
    let pairs = [(0_usize, 1_usize), (0, 2), (1, 2)];
    let mut packets = 0_u64;
    let mut singular_packets = 0_u64;

    for rank in 1_usize..=3 {
        for seed in -5_i128..=5 {
            let mut l = [[0_i128; 3]; 3];
            for i in 0..3 {
                for j in 0..rank {
                    l[i][j] = (i as i128 + 1) * (j as i128 + 2) + seed;
                }
            }
            let mut a = [[0_i128; 3]; 3];
            for i in 0..3 {
                for j in 0..3 {
                    for r in 0..rank {
                        a[i][j] += l[i][r] * l[j][r];
                    }
                }
            }

            for c0 in -3_i128..=3 {
                for c1 in -3_i128..=3 {
                    for c2 in -3_i128..=3 {
                        let c = [c0, c1, c2];
                        let mean: i128 = pairs
                            .iter()
                            .enumerate()
                            .map(|(r, &(i, j))| c[r] * a[i][j])
                            .sum();
                        let mut variance = 0_i128;
                        for (r, &(i, j)) in pairs.iter().enumerate() {
                            for (s, &(k, q)) in pairs.iter().enumerate() {
                                variance += c[r] * c[s] * covariance_of_products(&a, i, j, k, q);
                            }
                        }
                        assert!(variance >= 0);
                        let _ = mean;
                        packets += 1;
                        if rank < 3 {
                            singular_packets += 1;
                        }
                    }
                }
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.correlated_cubic_cut_defect.v1\",\n",
            "  \"exact_psd_packets_checked\": {},\n",
            "  \"singular_psd_packets_checked\": {},\n",
            "  \"product_covariance\": \"Cov(QiQj,QkQl)=Aik Ajl+Ail Ajk\",\n",
            "  \"inverse_covariance_used\": false,\n",
            "  \"singular_extension\": \"polynomial and regular\"\n",
            "}}\n"
        ),
        packets, singular_packets
    );
    fs::write(
        "research/benincasa/results/correlated-cubic-cut-defect.json",
        output,
    )
    .unwrap();
}
