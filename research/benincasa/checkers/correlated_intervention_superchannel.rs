type M2 = [[i64; 2]; 2];

fn kron_apply(k: M2, v: [i64; 4]) -> [i64; 4] {
    let mut out = [0_i64; 4];
    for ao in 0..2 {
        for e in 0..2 {
            for ai in 0..2 {
                out[2 * ao + e] += k[ao][ai] * v[2 * ai + e];
            }
        }
    }
    out
}

fn evolve(v: [i64; 4], permutation: [usize; 4], signs: [i64; 4]) -> [i64; 4] {
    let mut out = [0_i64; 4];
    for i in 0..4 { out[i] = signs[i] * v[permutation[i]]; }
    out
}

fn reduced_output(vectors: &[[i64; 4]]) -> M2 {
    let mut rho = [[0_i64; 2]; 2];
    for v in vectors {
        for a in 0..2 {
            for ap in 0..2 {
                for e in 0..2 { rho[a][ap] += v[2 * a + e] * v[2 * ap + e]; }
            }
        }
    }
    rho
}

fn is_psd_2(r: M2) -> bool {
    r[0][0] >= 0 && r[1][1] >= 0 && r[0][0] * r[1][1] - r[0][1] * r[1][0] >= 0
}

fn main() {
    let states = [
        [1, 0, 0, 1], [2, 1, 1, 3], [1, -2, 3, 1], [3, 0, 2, -1],
    ];
    let instruments: [[M2; 2]; 4] = [
        [[[1, 0], [0, 1]], [[0, 0], [0, 0]]],
        [[[1, 1], [0, 1]], [[0, 0], [1, -1]]],
        [[[2, 0], [1, 1]], [[1, -1], [0, 2]]],
        [[[0, 1], [1, 0]], [[1, 0], [0, -1]]],
    ];
    let evolutions = [
        ([0, 1, 2, 3], [1, 1, 1, 1]),
        ([0, 3, 2, 1], [1, 1, 1, 1]),
        ([3, 2, 1, 0], [1, -1, 1, -1]),
        ([1, 0, 3, 2], [-1, 1, 1, 1]),
    ];

    let mut positivity_checks = 0usize;
    for state in states {
        for instrument in instruments {
            for (perm, signs) in evolutions {
                let branches = instrument.map(|k| evolve(kron_apply(k, state), perm, signs));
                let out = reduced_output(&branches);
                assert!(is_psd_2(out));
                positivity_checks += 1;
            }
        }
    }

    // Product state p tensor e: the correlated superchannel expression is
    // exactly the ordinary product-channel expression, branch by branch.
    let mut product_checks = 0usize;
    for p in [[1, 0], [1, 2], [-2, 3]] {
        for e in [[1, 0], [1, -1], [2, 1]] {
            let product = [p[0] * e[0], p[0] * e[1], p[1] * e[0], p[1] * e[1]];
            for instrument in instruments {
                for k in instrument {
                    let lhs = kron_apply(k, product);
                    let kp = [
                        k[0][0] * p[0] + k[0][1] * p[1],
                        k[1][0] * p[0] + k[1][1] * p[1],
                    ];
                    let rhs = [kp[0] * e[0], kp[0] * e[1], kp[1] * e[0], kp[1] * e[1]];
                    assert_eq!(lhs, rhs);
                    product_checks += 1;
                }
            }
        }
    }

    println!("{{");
    println!("  \"schema\": \"marici.correlated_intervention_superchannel.v1\",");
    println!("  \"positivity_checks\": {positivity_checks},");
    println!("  \"product_degeneracy_checks\": {product_checks},");
    println!("  \"positive_on_local_cp_interventions\": true,");
    println!("  \"product_limit_equals_ordinary_channel\": true");
    println!("}}");
}
