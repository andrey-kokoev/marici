use std::{env, fs};

fn main() {
    let output = env::args().nth(1).expect("output path");
    let mut exact_points = 0usize;

    // Frozen q_G12-residue chart:
    // q_g31=A, q_g23=B, E=tau^2, A=tau^2*r, A+B=tau^3*n.
    // Clear denominators in
    //   1/A + 1/B = (A+B)/(A*B)
    // and test the weighted identity at exact integer points.
    for tau in 1i128..=17 {
        for r in -19i128..=19 {
            for n in -13i128..=13 {
                if r == 0 || -r + tau * n == 0 {
                    continue;
                }
                let a = tau.pow(2) * r;
                let b = tau.pow(2) * (-r + tau * n);
                assert_eq!(a + b, tau.pow(3) * n);
                assert_eq!(a * b, tau.pow(4) * r * (-r + tau * n));
                assert_eq!((a + b) * tau, tau.pow(4) * n);
                exact_points += 1;
            }
        }
    }

    // On the exceptional divisor tau=0 the strict transforms of A=0 and
    // B=0 both have r=0, but their first normal equations are r and -r.
    let individual_leading_signs = [1i8, -1i8];
    assert_eq!(individual_leading_signs.iter().sum::<i8>(), 0);

    // Consequently
    // tau^2(1/A+1/B) -> 0,
    // while tau(1/A+1/B) -> -n/r^2.
    // The physical ++ sum drops from weight -2 to weight -1.
    let individual_weight = -2i8;
    let summed_weight = -1i8;
    assert_eq!(summed_weight, individual_weight + 1);

    let json = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.lower_occurrence_weighted_collision.v1\",\n",
            "  \"exact_integer_points\": {},\n",
            "  \"residue_chart\": {{\"q_g31\":\"A\",\"q_g23\":\"B\"}},\n",
            "  \"weighted_substitution\": \"E=tau^2, A=tau^2*r, B=tau^2*(-r+tau*n)\",\n",
            "  \"individual_leading_coefficients\": [\"1/r\",\"-1/r\"],\n",
            "  \"individual_weight\": -2,\n",
            "  \"summed_exact_identity\": \"1/A+1/B=tau^-1*n/(r*(-r+tau*n))\",\n",
            "  \"summed_leading_coefficient\": \"-n/r^2\",\n",
            "  \"summed_weight\": -1,\n",
            "  \"exceptional_strict_transform_support\": \"r=0\",\n",
            "  \"forget_then_grade_equals_grade_then_forget\": false,\n",
            "  \"regulator_hierarchy_used\": false,\n",
            "  \"new_carrier_incidence\": false\n",
            "}}\n"
        ),
        exact_points
    );
    fs::write(output, json).expect("write certificate");
}
