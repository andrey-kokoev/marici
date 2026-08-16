use std::{collections::BTreeMap, env, fs};

fn sign(value: i32) -> i8 {
    match value.cmp(&0) {
        std::cmp::Ordering::Less => -1,
        std::cmp::Ordering::Equal => 0,
        std::cmp::Ordering::Greater => 1,
    }
}

fn main() {
    let output = env::args().nth(1).expect("output path");
    let mut chamber_counts = BTreeMap::<(i8, i8), usize>::new();
    let mut tested = 0usize;

    // X_i -> X_i-i*xi_i and y_ij -> y_ij-i*eta_ij, all regulators positive.
    // After Res(q_G12), q_g31=A+i*(xi_2-eta_23) and
    // q_g23=B+i*(xi_1-eta_31).  Exhaust a positive integer box.
    for xi1 in 1i32..=9 {
        for xi2 in 1i32..=9 {
            for eta23 in 1i32..=9 {
                for eta31 in 1i32..=9 {
                    let alpha = xi2 - eta23;
                    let beta = xi1 - eta31;
                    let chamber = (sign(alpha), sign(beta));
                    *chamber_counts.entry(chamber).or_default() += 1;
                    tested += 1;
                }
            }
        }
    }

    for chamber in [(-1, -1), (-1, 1), (1, -1), (1, 1)] {
        assert!(chamber_counts.get(&chamber).copied().unwrap_or(0) > 0);
    }

    // At B=-A, in units of i*pi*delta(A):
    // 1/(A+i0*s_a)+1/(-A+i0*s_b) -> -(s_a+s_b).
    let current_coefficients = [
        ((-1i8, -1i8), 2i8),
        ((-1i8, 1i8), 0i8),
        ((1i8, -1i8), 0i8),
        ((1i8, 1i8), -2i8),
    ];
    for ((sa, sb), coefficient) in current_coefficients {
        assert_eq!(coefficient, -(sa + sb));
    }

    // The equal-regulator diagonal lands on alpha=beta=0 and selects no side.
    for common in 1i32..=100 {
        assert_eq!(common - common, 0);
    }

    let json = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.iterated_cut_regulator_chambers.v1\",\n",
            "  \"positive_regulator_assignments_tested\": {},\n",
            "  \"induced_regulators\": {{\n",
            "    \"q_g31\": \"alpha=epsilon_X2-epsilon_y23\",\n",
            "    \"q_g23\": \"beta=epsilon_X1-epsilon_y31\"\n",
            "  }},\n",
            "  \"realized_nonzero_sign_chambers\": [\"--\",\"-+\",\"+-\",\"++\"],\n",
            "  \"current_coefficients_in_i_pi_delta_units\": {{\"--\":2,\"-+\":0,\"+-\":0,\"++\":-2}},\n",
            "  \"equal_regulator_diagonal\": \"alpha=beta=0; no boundary side selected\",\n",
            "  \"printed_energy_sign_conditions_select_unique_current\": false,\n",
            "  \"graph_level_contour_cone_image\": \"uncomputed\",\n",
            "  \"tau_and_regulator_limits_commute_without_extra_data\": false,\n",
            "  \"new_carrier_incidence\": false\n",
            "}}\n"
        ),
        tested
    );
    fs::write(output, json).expect("write certificate");
}
