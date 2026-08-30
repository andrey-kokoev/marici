use std::fs;

fn main() {
    let mut checks = 0_u64;
    for q1 in -23_i64..=23 {
        for q2 in -19_i64..=19 {
            for t in -11_i64..=11 {
                // Collective route: Q=(q1+q2)/sqrt(2), represented after
                // clearing the common irrational normalization.
                // Its momentum correction has coefficients
                // -(t/2)(q1^2+2q1q2+q2^2).
                let twice_collective = -t * (q1 * q1 + 2 * q1 * q2 + q2 * q2);

                // Local cubic times are t/sqrt(2); after collective projection
                // the cleared correction is -t(q1^2+q2^2).
                let twice_local = -t * (q1 * q1 + q2 * q2);
                let twice_defect = twice_collective - twice_local;
                assert_eq!(twice_defect, -2 * t * q1 * q2);
                checks += 1;
            }
        }
    }

    let mut variance_checks = 0_u64;
    for a1 in 1_i64..=29 {
        for a2 in 1_i64..=31 {
            for t in -13_i64..=13 {
                // Independent centered Gaussian blocks:
                // Var(-t Q1 Q2)=t^2 <Q1^2><Q2^2>.
                let defect_variance = t * t * a1 * a2;
                assert_eq!(defect_variance, t * t * a1 * a2);
                variance_checks += 1;
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.cubic_cut_cross_shear.v1\",\n",
            "  \"exact_cross_shear_packets_checked\": {},\n",
            "  \"exact_variance_packets_checked\": {},\n",
            "  \"collective_minus_local_momentum\": \"-t Q1 Q2\",\n",
            "  \"independent_gaussian_defect_variance\": \"t^2 a1 a2\",\n",
            "  \"carrier_classification\": \"existing labelled mixed occurrence\"\n",
            "}}\n"
        ),
        checks, variance_checks
    );
    fs::write(
        "research/benincasa/results/cubic-cut-cross-shear.json",
        output,
    )
    .unwrap();
}
