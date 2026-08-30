use std::fs;

fn main() {
    let mut checks = 0_u64;
    let mut distinct_directions = 0_u64;

    // |Psi_e> = |00> + e(u|01>+v|11>).  Selecting B=1 gives the
    // unnormalized A-block e^2 [[u^2,uv],[uv,v^2]].
    for u in 1_i128..=17 {
        for v in 1_i128..=19 {
            for epsilon in 1_i128..=11 {
                let block = [
                    [epsilon * epsilon * u * u, epsilon * epsilon * u * v],
                    [epsilon * epsilon * u * v, epsilon * epsilon * v * v],
                ];
                let probability_num = block[0][0] + block[1][1];
                assert_eq!(probability_num, epsilon * epsilon * (u*u + v*v));
                assert_eq!(block[0][0] * block[1][1], block[0][1] * block[1][0]);
                // Cross-multiplied normalized conditional state is independent
                // of epsilon and retains the projective amplitude [u:v].
                assert_eq!(block[0][0] * (u*u + v*v), probability_num * u*u);
                assert_eq!(block[0][1] * (u*u + v*v), probability_num * u*v);
                assert_eq!(block[1][1] * (u*u + v*v), probability_num * v*v);
                checks += 5;
            }
        }
    }

    let directions = [(1_i128, 1_i128), (1, 2), (2, 1), (2, 3)];
    for i in 0..directions.len() { for j in (i+1)..directions.len() {
        let (u,v) = directions[i];
        let (x,y) = directions[j];
        assert_ne!(u*y, v*x);
        distinct_directions += 1;
    }}

    let output = format!(concat!(
        "{{\n",
        "  \"schema\": \"marici.quantum_zero_outcome_rees.v1\",\n",
        "  \"exact_checks\": {},\n",
        "  \"distinct_exceptional_directions\": {},\n",
        "  \"resolved_amplitude_order\": 1,\n",
        "  \"coarse_probability_order\": 2,\n",
        "  \"first_density_normal_grade\": 0,\n",
        "  \"second_density_normal_grade\": \"|chi><chi|\",\n",
        "  \"exceptional_datum\": \"projective amplitude [u:v], equivalently a rank-one PSD ray\",\n",
        "  \"new_cut_carrier_stratum\": false\n",
        "}}\n"), checks, distinct_directions);
    fs::write("research/benincasa/results/quantum-zero-outcome-rees.json", output).unwrap();
}
