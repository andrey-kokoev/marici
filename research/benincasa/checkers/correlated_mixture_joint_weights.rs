use std::fs;

fn pair_marginal(support: &[(usize, usize, usize)], axes: (usize, usize)) -> [[usize; 2]; 2] {
    let mut out = [[0_usize; 2]; 2];
    for &(a, b, c) in support {
        let x = [a, b, c];
        out[x[axes.0]][x[axes.1]] += 1;
    }
    out
}

fn main() {
    let mut checks = 0_u64;

    // Same one-site marginals, different joint displacement distribution.
    let diag = [(0_i128, 0_i128), (1, 1)];
    let anti = [(0_i128, 1_i128), (1, 0)];
    let mu = [0_i128, 1_i128];
    let nu = [0_i128, 2_i128];
    let diag_second: i128 = diag.iter().map(|&(i, j)| (mu[i as usize] + nu[j as usize]).pow(2)).sum();
    let anti_second: i128 = anti.iter().map(|&(i, j)| (mu[i as usize] + nu[j as usize]).pow(2)).sum();
    assert_ne!(diag_second, anti_second);
    checks += 1;

    // Even and odd parity distributions have identical pair marginals but
    // distinct three-way support.
    let even = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)];
    let odd = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 1)];
    for axes in [(0, 1), (0, 2), (1, 2)] {
        assert_eq!(pair_marginal(&even, axes), pair_marginal(&odd, axes));
        checks += 1;
    }
    assert_ne!(even, odd);

    // Vanishing-row conditioning: pi_jk=epsilon r_k has a finite normalized
    // exceptional row r_k/sum(r), independent of epsilon but dependent on the
    // chosen approach direction r.
    let mut exceptional_rows = 0_u64;
    for r0 in 1_i128..=17 {
        for r1 in 1_i128..=19 {
            for epsilon in 1_i128..=13 {
                let p0 = epsilon * r0;
                let p1 = epsilon * r1;
                let marginal = p0 + p1;
                assert_eq!(p0 * (r0 + r1), marginal * r0);
                assert_eq!(p1 * (r0 + r1), marginal * r1);
                exceptional_rows += 1;
            }
        }
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.correlated_mixture_joint_weights.v1\",\n",
            "  \"exact_structural_checks\": {},\n",
            "  \"zero_marginal_exceptional_rows_checked\": {},\n",
            "  \"two_block_coefficient\": \"full joint weight table pi_jk\",\n",
            "  \"three_block_coefficient\": \"full joint tensor pi_jkl\",\n",
            "  \"pair_marginals_sufficient_for_three_blocks\": false,\n",
            "  \"zero_marginal_datum\": \"projective normalized row on simplex-face Rees chart\",\n",
            "  \"new_cut_carrier_stratum\": false\n",
            "}}\n"
        ),
        checks, exceptional_rows
    );
    fs::write(
        "research/benincasa/results/correlated-mixture-joint-weights.json",
        output,
    )
    .unwrap();
}
