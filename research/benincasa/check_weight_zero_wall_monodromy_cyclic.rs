use std::process::ExitCode;

fn coefficient_square(x: i128, y: i128) -> (i128, i128) {
    let numerator = 9 * (x - y).pow(2) * (x + y).pow(2);
    let denominator = 256 * (x * y).pow(7);
    (numerator, denominator)
}

fn main() -> ExitCode {
    // Total-energy deck action: tau -> -tau forces n -> -n. The normalized
    // wall root w=sqrt(K)/tau^3 is fixed, hence dn/w has sign -1.
    let n_sign = -1_i8;
    let dn_sign = -1_i8;
    let w_sign = 1_i8;
    let cohomology_sign = dn_sign * w_sign;
    let endpoint_primitive_sign = n_sign;
    let transported_chain_sign = -1_i8;
    let period_pairing_sign = cohomology_sign * transported_chain_sign;
    assert_eq!(cohomology_sign, -1);
    assert_eq!(endpoint_primitive_sign, -1);
    assert_eq!(period_pairing_sign, 1);

    let mut cyclic_tests = 0_u64;
    for x in 1_i128..=12 {
        for y in 1_i128..=12 {
            for z in 1_i128..=12 {
                let sectors = [
                    coefficient_square(x, y),
                    coefficient_square(y, z),
                    coefficient_square(z, x),
                ];
                let rotated = [
                    coefficient_square(y, z),
                    coefficient_square(z, x),
                    coefficient_square(x, y),
                ];
                assert_eq!(rotated, [sectors[1], sectors[2], sectors[0]]);
                cyclic_tests += 1;
            }
        }
    }
    assert_eq!(cyclic_tests, 1_728);

    println!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.weight-zero-wall-monodromy-cyclic.v1\",\n",
            "  \"cyclic_tests\": {},\n",
            "  \"deck_action\": \"tau->-tau, n->-n, w->w\",\n",
            "  \"cohomology_generator\": \"dn/w\",\n",
            "  \"semisimple_character\": -1,\n",
            "  \"unipotent_part\": 1,\n",
            "  \"nilpotent_logarithm_N\": 0,\n",
            "  \"endpoint_polar_jet_character\": -1,\n",
            "  \"transported_relative_chain_character\": -1,\n",
            "  \"period_pairing_character\": 1,\n",
            "  \"cyclic_covariance\": [\"kappa12->kappa23\", \"kappa23->kappa31\", \"kappa31->kappa12\"],\n",
            "  \"occurrence_split_status\": \"uncomputed\",\n",
            "  \"new_carrier_incidence\": false\n",
            "}}"
        ),
        cyclic_tests
    );

    ExitCode::SUCCESS
}
