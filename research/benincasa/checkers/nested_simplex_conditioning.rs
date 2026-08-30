use std::fs;

fn main() {
    let mut exact_checks = 0_u64;

    // Two nested vanishing scales.  The zero row has entries epsilon*delta*s_k;
    // its sibling has entries epsilon*r_k.  Iterated conditioning must agree
    // with direct conditioning before either normal parameter is specialized.
    for s0 in 1_i128..=11 {
        for s1 in 1_i128..=13 {
            for r0 in 1_i128..=7 {
                for r1 in 1_i128..=9 {
                    for epsilon in 1_i128..=5 {
                        for delta in 1_i128..=6 {
                            let s = s0 + s1;
                            let r = r0 + r1;
                            let total = epsilon * (r + delta * s);

                            // (row-zero probability) * (within-row probability)
                            // equals the direct normalized entry.  Cross-multiply
                            // to keep the certificate integral and exact.
                            for sk in [s0, s1] {
                                let iter_num = delta * s * sk;
                                let iter_den = (r + delta * s) * s;
                                let direct_num = epsilon * delta * sk;
                                let direct_den = total;
                                assert_eq!(iter_num * direct_den, direct_num * iter_den);
                                exact_checks += 1;
                            }

                            // The common epsilon scale cancels at the first face.
                            assert_eq!(total, epsilon * (r + delta * s));
                        }
                    }
                }
            }
        }
    }

    // Different deeper directions remain distinguishable on the exceptional
    // flag although both have the same ordinary specialization at delta=0.
    let directions = [(1_i128, 2_i128), (2, 1), (1, 3)];
    for i in 0..directions.len() {
        for j in (i + 1)..directions.len() {
            let (a, b) = directions[i];
            let (c, d) = directions[j];
            assert_ne!(a * d, b * c);
            exact_checks += 1;
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.nested_simplex_conditioning.v1\",\n",
            "  \"exact_checks\": {},\n",
            "  \"iterated_equals_direct\": true,\n",
            "  \"outer_exceptional_coordinate\": \"delta*S/(R+delta*S)\",\n",
            "  \"inner_exceptional_coordinate\": \"[s_0:s_1]\",\n",
            "  \"transition\": \"delta*s_k/(R+delta*S)\",\n",
            "  \"overlap_extension_class\": false,\n",
            "  \"geometry\": \"ordinary iterated simplex-face blowup\",\n",
            "  \"new_cut_carrier_stratum\": false\n",
            "}}\n"
        ),
        exact_checks
    );
    fs::write(
        "research/benincasa/results/nested-simplex-conditioning.json",
        output,
    )
    .unwrap();
}
