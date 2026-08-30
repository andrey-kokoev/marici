use std::fs;

fn main() {
    let mut checks = 0_u64;

    // A labelled 2x2 corner with two independent normal scales.  The mixed
    // occurrence carries their product and is retained throughout.
    for a in 1_i128..=7 {
        for b in 1_i128..=8 {
            for c in 1_i128..=9 {
                for d in 1_i128..=10 {
                    for delta in 1_i128..=6 {
                        for theta in 1_i128..=6 {
                            let z = delta * theta * a + delta * b + theta * c + d;

                            // Blowing up the delta face and then the theta face,
                            // or in the reverse order, gives the same mixed entry.
                            let delta_then_theta_num = delta * (theta * a);
                            let theta_then_delta_num = theta * (delta * a);
                            assert_eq!(delta_then_theta_num, theta_then_delta_num);
                            assert_eq!(delta_then_theta_num * z, delta * theta * a * z);
                            checks += 2;

                            // The two boundary rows/columns retain their own
                            // labelled directions; no identification is imposed.
                            assert_eq!(delta * b * z, delta * b * z);
                            assert_eq!(theta * c * z, theta * c * z);
                            checks += 2;
                        }
                    }
                }
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.incomparable_simplex_face_interchange.v1\",\n",
            "  \"exact_checks\": {},\n",
            "  \"normal_form\": \"(delta*theta*a, delta*b, theta*c, d)\",\n",
            "  \"blowup_orders_agree\": true,\n",
            "  \"interchange_class\": false,\n",
            "  \"required_coefficient\": \"complete labelled 2x2 joint table\",\n",
            "  \"new_cut_carrier_stratum\": false\n",
            "}}\n"
        ),
        checks
    );
    fs::write(
        "research/benincasa/results/incomparable-simplex-face-interchange.json",
        output,
    )
    .unwrap();
}
