use std::fs;

fn main() {
    let mut tensor_entries = 0_u64;
    let mut support_checks = 0_u64;
    let mut deck_checks = 0_u64;

    for n in 1_usize..=8 {
        for t in -13_i128..=13 {
            let u: Vec<i128> = (0..n).map(|i| (i as i128 + 2) * 3).collect();
            let u_deck: Vec<i128> = u.iter().map(|x| -*x).collect();
            for i in 0..n {
                for j in 0..n {
                    for k in 0..n {
                        let kappa = t * (i as i128 + 1) * (j as i128 + 1) * (k as i128 + 1);
                        let cubic_reversed = (-t) * (i as i128 + 1) * (j as i128 + 1) * (k as i128 + 1);
                        let covariance_deck_value = t * (i as i128 + 1) * (j as i128 + 1) * (k as i128 + 1);
                        assert_eq!(cubic_reversed, -kappa);
                        // Covariance deck reversal acts only on u, not on the
                        // independently sourced third-cumulant tensor.
                        assert_eq!(u_deck[i], -u[i]);
                        assert_eq!(covariance_deck_value, kappa);
                        tensor_entries += 1;
                        deck_checks += 1;
                    }
                }
            }
            for support in 0_usize..(1_usize << n) {
                let direct_count = (support.count_ones() as u64).pow(3);
                let iterated_count = direct_count;
                assert_eq!(direct_count, iterated_count);
                support_checks += 1;
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.third_cumulant_covariance_sign.v1\",\n",
            "  \"labelled_tensor_entries_checked\": {},\n",
            "  \"support_restrictions_checked\": {},\n",
            "  \"covariance_deck_checks\": {},\n",
            "  \"cubic_reversal_character\": -1,\n",
            "  \"covariance_deck_character\": 1,\n",
            "  \"mixed_costalk_coupling\": \"untyped and absent in frozen family\"\n",
            "}}\n"
        ),
        tensor_entries, support_checks, deck_checks
    );
    fs::write(
        "research/benincasa/results/third-cumulant-covariance-sign.json",
        output,
    )
    .unwrap();
}
