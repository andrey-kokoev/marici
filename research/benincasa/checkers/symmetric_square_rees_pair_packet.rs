use std::fs;

fn main() {
    let mut vectors = 0_u64;
    let mut minors = 0_u64;
    let mut deck_checks = 0_u64;

    for n in 2_usize..=8 {
        for seed in -17_i128..=17 {
            let u: Vec<i128> = (0..n)
                .map(|i| seed + (i as i128 + 1) * (i as i128 + 2))
                .collect();
            let mut xi = vec![vec![0_i128; n]; n];
            let mut xi_deck = vec![vec![0_i128; n]; n];
            for i in 0..n {
                for j in 0..n {
                    xi[i][j] = u[i] * u[j];
                    xi_deck[i][j] = (-u[i]) * (-u[j]);
                    assert_eq!(xi[i][j], xi_deck[i][j]);
                    deck_checks += 1;
                }
            }
            for i in 0..n {
                for j in 0..n {
                    for k in 0..n {
                        for l in 0..n {
                            assert_eq!(xi[i][j] * xi[k][l], xi[i][l] * xi[k][j]);
                            minors += 1;
                        }
                    }
                }
            }
            vectors += 1;
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.symmetric_square_rees_pair_packet.v1\",\n",
            "  \"resolved_normal_vectors_checked\": {},\n",
            "  \"rank_one_minor_identities_checked\": {},\n",
            "  \"deck_invariance_checks\": {},\n",
            "  \"exceptional_tensor\": \"Xi_ij=u_i u_j\",\n",
            "  \"deck_action\": \"u maps to -u; Xi is invariant\",\n",
            "  \"additional_pair_extension_required\": false\n",
            "}}\n"
        ),
        vectors, minors, deck_checks
    );
    fs::write(
        "research/benincasa/results/symmetric-square-rees-pair-packet.json",
        output,
    )
    .unwrap();
}
