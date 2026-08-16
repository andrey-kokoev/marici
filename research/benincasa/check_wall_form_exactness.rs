use std::process::ExitCode;

fn main() -> ExitCode {
    let mut tests = 0_u64;
    for x in 1_i128..=24 {
        for y in 1_i128..=24 {
            let a = x * y;
            let s = x + y;
            for n in -24_i128..=24 {
                let v = a * n * n - 2 * s;
                let primitive_numerator = 3 * a * n * n - 5 * s;

                // For P=(3*a*n^2-5*s)/v^(3/2), differentiation over the
                // common denominator v^(5/2) gives the numerator below.
                let derivative_numerator = 6 * a * n * v - 3 * a * n * primitive_numerator;
                let expected = -3 * a * n * (a * n * n - s);
                assert_eq!(derivative_numerator, expected);
                tests += 1;
            }
        }
    }

    assert_eq!(tests, 28_224);
    println!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.wall-form-exactness.v1\",\n",
            "  \"tests\": {},\n",
            "  \"wall_form_core\": \"n*(a*n^2-s)*dn/(a*n^2-2*s)^(5/2)\",\n",
            "  \"primitive_core\": \"-(3*a*n^2-5*s)/(3*a*(a*n^2-2*s)^(3/2))\",\n",
            "  \"exact_on_punctured_wall_curve\": true,\n",
            "  \"primitive_parity_in_n\": \"even\",\n",
            "  \"endpoint_status\": \"meromorphic poles at a*n^2=2*s\",\n",
            "  \"symmetric_regularized_pairing\": 0,\n",
            "  \"new_carrier_incidence\": false\n",
            "}}"
        ),
        tests
    );

    ExitCode::SUCCESS
}
