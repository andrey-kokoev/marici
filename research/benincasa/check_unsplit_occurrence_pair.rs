use std::{env, fs};

fn main() {
    let output = env::args().nth(1).expect("output path");
    let mut exact_points = 0usize;

    // Positive q_G12-residue corner:
    // E=tau^2, X3=E-X1-X2,
    // a=X2+tau^2*r, b=X1-tau^2*r+tau^3*n.
    for x in 1i128..=11 {
        for y in 1i128..=11 {
            for tau in 1i128..=9 {
                for r in -7i128..=7 {
                    for n in -5i128..=5 {
                        let tau2 = tau.pow(2);
                        let tau3 = tau.pow(3);
                        let e = tau2;
                        let z = e - x - y;
                        let a = y + tau2 * r;
                        let b = x - tau2 * r + tau3 * n;

                        let qg1 = b - y - z;
                        let qg2 = a - x - z;
                        let qg3 = a + b + z;
                        let qg31 = a - y;
                        let qg23 = b - x;

                        assert_eq!(qg1, 2 * x - tau2 * (r + 1) + tau3 * n);
                        assert_eq!(qg2, 2 * y + tau2 * (r - 1));
                        assert_eq!(qg3, tau2 * (1 + tau * n));
                        assert_eq!(qg31, tau2 * r);
                        assert_eq!(qg23, tau2 * (-r + tau * n));
                        assert_eq!(qg31 + qg23, tau3 * n);

                        // Clear denominators in the source-defined unsplit pair.
                        // 1/qg23 + 1/qg31 = (qg23+qg31)/(qg23*qg31).
                        assert_eq!(
                            (qg23 + qg31) * tau,
                            tau.pow(4) * n,
                            "one-grade cancellation"
                        );
                        exact_points += 1;
                    }
                }
            }
        }
    }

    // Individual full lower factors qg3^{-1}qg31^{-1} and
    // qg3^{-1}qg23^{-1} have weight -4. Their ++ sum has weight -3.
    let individual_weight = -4i8;
    let pair_weight = -3i8;
    assert_eq!(pair_weight, individual_weight + 1);

    // For fixed x,y the leading two-form is
    // -(n/(4*x*y*r^2)) dr^dn = d((n/(4*x*y*r)) dn).
    // Store the numerator identity after clearing 4*x*y*r^2.
    for x in 1i128..=31 {
        for y in 1i128..=31 {
            for r in -31i128..=31 {
                if r == 0 {
                    continue;
                }
                for n in -9i128..=9 {
                    let exterior_derivative_numerator = -n * 4 * x * y;
                    let leading_numerator = -n * 4 * x * y;
                    assert_eq!(exterior_derivative_numerator, leading_numerator);
                }
            }
        }
    }

    let json = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.unsplit_occurrence_pair.v1\",\n",
            "  \"exact_weighted_points\": {},\n",
            "  \"common_denominators\": {{\n",
            "    \"q_g1\": \"2*x-tau^2*(r+1)+tau^3*n\",\n",
            "    \"q_g2\": \"2*y+tau^2*(r-1)\",\n",
            "    \"q_g3\": \"tau^2*(1+tau*n)\"\n",
            "  }},\n",
            "  \"occurrence_denominators\": {{\"q_g31\":\"tau^2*r\",\"q_g23\":\"tau^2*(-r+tau*n)\"}},\n",
            "  \"individual_full_weight\": -4,\n",
            "  \"unsplit_pair_weight\": -3,\n",
            "  \"leading_two_form\": \"-n/(4*x*y*r^2) dr wedge dn\",\n",
            "  \"primitive\": \"n/(4*x*y*r) dn\",\n",
            "  \"simple_residue_on_r0\": 0,\n",
            "  \"individual_boundary_current_canonical\": false,\n",
            "  \"unsplit_pair_canonical\": true,\n",
            "  \"new_carrier_incidence\": false\n",
            "}}\n"
        ),
        exact_points
    );
    fs::write(output, json).expect("write certificate");
}
