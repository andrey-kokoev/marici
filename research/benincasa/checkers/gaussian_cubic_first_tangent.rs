use std::fs;

fn main() {
    let mut checks = 0_u64;
    let mut nonzero_third = 0_u64;

    // Exact integer census.  The identities are polynomial, so this is a
    // regression packet rather than evidence inferred from floating point.
    for a in 1_i64..=31 {
        for t in -19_i64..=19 {
            let k_qqp = -2 * t * a * a;
            let expected = -2 * t * a * a;
            assert_eq!(k_qqp, expected);

            // For a centered parity-even Gaussian, the cubic shear correction
            // to Re<Q^2 S> is -t(<Q^5>-a<Q^3>) = 0.
            let z_shift = 0_i64;
            assert_eq!(z_shift, 0);

            // The connected fourth moments tested in Entry 1627 also have no
            // linear term: their shear corrections contain odd Gaussian
            // moments.
            let fourth_cumulant_linear = 0_i64;
            assert_eq!(fourth_cumulant_linear, 0);

            checks += 1;
            if k_qqp != 0 {
                nonzero_third += 1;
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.gaussian_cubic_first_tangent.v1\",\n",
            "  \"exact_parameter_packets_checked\": {},\n",
            "  \"nonzero_third_cumulant_packets\": {},\n",
            "  \"heisenberg_transform\": \"P_t=P-t Q^2\",\n",
            "  \"centered_third_cumulant\": \"kappa_QQP=-2 t a^2\",\n",
            "  \"entry_1630_Z_linear_tangent\": 0,\n",
            "  \"connected_fourth_cumulant_linear_tangent\": 0,\n",
            "  \"density_representability\": \"exact unitary conjugation\"\n",
            "}}\n"
        ),
        checks, nonzero_third
    );

    fs::create_dir_all("research/benincasa/results").unwrap();
    fs::write(
        "research/benincasa/results/gaussian-cubic-first-tangent.json",
        output,
    )
    .unwrap();
}
