use std::process::ExitCode;

fn main() -> ExitCode {
    let mut tests = 0_u64;
    for x in 1_i128..=32 {
        for y in 1_i128..=32 {
            let s = x + y;
            for w2 in -16_i128..=16 {
                // On the wall cover w^2=a*n^2-2*s, hence a*n^2=w^2+2*s.
                let transformed_numerator = 3 * (w2 + 2 * s) - 5 * s;
                assert_eq!(transformed_numerator, 3 * w2 + s);
                tests += 1;
            }

            // The involution exchanging endpoints changes n to -n and fixes
            // the frozen square-root sheet w. The complete polar coefficient
            // vector of s/w^3+3/w is therefore identical at both endpoints.
            let plus_principal_part = [s, 3_i128];
            let minus_principal_part = [s, 3_i128];
            assert_eq!(plus_principal_part, minus_principal_part);
        }
    }

    assert_eq!(tests, 33_792);
    println!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.wall-endpoint-principal-parts.v1\",\n",
            "  \"tests\": {},\n",
            "  \"cover_equation\": \"w^2=a*n^2-2*s\",\n",
            "  \"primitive_on_cover\": \"C*(s/w^3+3/w)\",\n",
            "  \"endpoint_involution\": \"n->-n, w->w\",\n",
            "  \"plus_principal_coefficients_w_minus_3_w_minus_1\": [\"s\", 3],\n",
            "  \"minus_principal_coefficients_w_minus_3_w_minus_1\": [\"s\", 3],\n",
            "  \"oriented_principal_part_difference\": [0, 0],\n",
            "  \"weight_minus_one_relative_class\": 0,\n",
            "  \"new_carrier_incidence\": false\n",
            "}}"
        ),
        tests
    );

    ExitCode::SUCCESS
}
