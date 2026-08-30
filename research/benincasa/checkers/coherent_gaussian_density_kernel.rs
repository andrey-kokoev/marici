use std::fs;

fn main() {
    let mut checks = 0_u64;
    let mut phase_sensitive_cases = 0_u64;

    // Algebraic audit of two normalized displaced packets with overlap S.
    // Diagonal q^2 matrix elements are a+d^2; the off-diagonal element is aS.
    for a in 1_i128..=17 {
        for d2 in 1_i128..=19 {
            for sn in 1_i128..=9 {
                let sd = 10_i128;
                // q2_+ = ((a+d2)+a*S)/(1+S)
                // q2_- = ((a+d2)-a*S)/(1-S)
                let plus_num = (a + d2) * sd + a * sn;
                let plus_den = sd + sn;
                let minus_num = (a + d2) * sd - a * sn;
                let minus_den = sd - sn;

                // Difference is nonzero whenever d != 0 and 0<S<1.
                let diff_num = plus_num * minus_den - minus_num * plus_den;
                assert_eq!(diff_num, -2 * d2 * sn * sd);
                assert_ne!(diff_num, 0);
                checks += 2;
                phase_sensitive_cases += 1;

                // Both cats have identical diagonal component weights 1/2,1/2;
                // deleting the off-diagonal kernel would give the same mixture
                // moment a+d^2 for both and therefore loses the exact result.
                assert_ne!(plus_num, (a + d2) * plus_den);
                assert_ne!(minus_num, (a + d2) * minus_den);
                checks += 2;
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.coherent_gaussian_density_kernel.v1\",\n",
            "  \"exact_checks\": {},\n",
            "  \"phase_sensitive_cases\": {},\n",
            "  \"packet_overlap\": \"S=exp(-d^2/(2a))\",\n",
            "  \"even_q2\": \"((a+d^2)+aS)/(1+S)\",\n",
            "  \"odd_q2\": \"((a+d^2)-aS)/(1-S)\",\n",
            "  \"same_diagonal_weights_sufficient\": false,\n",
            "  \"minimal_coefficient\": \"Hermitian component density kernel rho_jk with transition generating kernels\",\n",
            "  \"new_cut_carrier_stratum\": false\n",
            "}}\n"
        ), checks, phase_sensitive_cases
    );
    fs::write("research/benincasa/results/coherent-gaussian-density-kernel.json", output).unwrap();
}
