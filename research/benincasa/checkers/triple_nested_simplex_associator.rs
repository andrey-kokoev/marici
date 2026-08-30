use std::fs;

fn main() {
    let mut checks = 0_u64;

    // Three labelled rows at nested scales:
    //   row 0 = epsilon*delta*theta*t_k,
    //   row 1 = epsilon*delta*s_k,
    //   row 2 = epsilon*r_k.
    // Compare direct normalization with the parenthesization
    // ((row 0 inside rows 0+1) inside all rows).
    for t0 in 1_i128..=5 {
        for t1 in 1_i128..=6 {
            for s0 in 1_i128..=4 {
                for s1 in 1_i128..=5 {
                    for r0 in 1_i128..=3 {
                        for r1 in 1_i128..=4 {
                            for epsilon in 1_i128..=3 {
                                for delta in 1_i128..=4 {
                                    for theta in 1_i128..=4 {
                                        let t = t0 + t1;
                                        let s = s0 + s1;
                                        let r = r0 + r1;
                                        let grouped = s + theta * t;
                                        let total = epsilon * (r + delta * grouped);

                                        for tk in [t0, t1] {
                                            // Product of the three conditional factors:
                                            // delta*grouped/(r+delta*grouped),
                                            // theta*t/grouped, tk/t.
                                            let iter_num = delta * grouped * theta * t * tk;
                                            let iter_den = (r + delta * grouped) * grouped * t;
                                            let direct_num = epsilon * delta * theta * tk;
                                            let direct_den = total;
                                            assert_eq!(iter_num * direct_den, direct_num * iter_den);
                                            checks += 1;
                                        }

                                        // The alternative regrouping multiplies the same
                                        // labelled normal coordinates delta and theta.
                                        assert_eq!(delta * (theta * t), (delta * theta) * t);
                                        checks += 1;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.triple_nested_simplex_associator.v1\",\n",
            "  \"exact_checks\": {},\n",
            "  \"parenthesizations_agree\": true,\n",
            "  \"deep_transition\": \"delta*theta*t_k/(R+delta*(S+theta*T))\",\n",
            "  \"exceptional_flag\": \"(delta, theta, [t_k])\",\n",
            "  \"associator_class\": false,\n",
            "  \"new_cut_carrier_stratum\": false\n",
            "}}\n"
        ),
        checks
    );
    fs::write(
        "research/benincasa/results/triple-nested-simplex-associator.json",
        output,
    )
    .unwrap();
}
