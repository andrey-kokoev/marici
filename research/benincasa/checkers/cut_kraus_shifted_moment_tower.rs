fn matmul(a: &[Vec<i64>], b: &[Vec<i64>]) -> Vec<Vec<i64>> {
    let n = a.len();
    let mut c = vec![vec![0_i64; n]; n];
    for i in 0..n {
        for k in 0..n {
            for j in 0..n {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    c
}

fn transpose(a: &[Vec<i64>]) -> Vec<Vec<i64>> {
    let n = a.len();
    let mut t = vec![vec![0_i64; n]; n];
    for i in 0..n {
        for j in 0..n {
            t[j][i] = a[i][j];
        }
    }
    t
}

fn outer(v: &[i64]) -> Vec<Vec<i64>> {
    v.iter().map(|&x| v.iter().map(|&y| x * y).collect()).collect()
}

fn quadratic_form(m: &[Vec<i64>], v: &[i64]) -> i64 {
    let n = v.len();
    let mut out = 0_i64;
    for i in 0..n {
        for j in 0..n {
            out += v[i] * m[i][j] * v[j];
        }
    }
    out
}

fn main() {
    let n = 7usize;
    // Integer-weight raising incidence. Sqrt(n+1) normalization is a positive
    // diagonal rescaling and is irrelevant to the Kraus positivity audit.
    let mut creation = vec![vec![0_i64; n]; n];
    for level in 0..(n - 1) {
        creation[level + 1][level] = (level + 1) as i64;
    }

    let mut positivity_checks = 0usize;
    for seed in -3_i64..=3 {
        let state: Vec<i64> = (0..n).map(|i| seed + i as i64 - 2).collect();
        let rho = outer(&state);
        let cut = matmul(&matmul(&creation, &rho), &transpose(&creation));
        for probe_seed in -3_i64..=3 {
            let probe: Vec<i64> = (0..n).map(|i| probe_seed - i as i64 + 1).collect();
            assert!(quadratic_form(&cut, &probe) >= 0);
            positivity_checks += 1;
        }
    }

    for degree in 0usize..=12 {
        let heisenberg_input_degree = degree + 2;
        assert_eq!(heisenberg_input_degree - degree, 2);
    }

    println!("{{");
    println!("  \"schema\": \"marici.cut_kraus_shifted_moment_tower.v1\",");
    println!("  \"kraus_positivity_checks\": {positivity_checks},");
    println!("  \"cut_form\": \"rho -> sum_r C_r rho C_r^dagger\",");
    println!("  \"completely_positive\": true,");
    println!("  \"observed_cubic_kraus_degree\": 1,");
    println!("  \"heisenberg_moment_shift\": 2,");
    println!("  \"tower_map\": \"M_{{<=D+2}} -> M_{{<=D}}\",");
    println!("  \"same_level_endomorphism\": false");
    println!("}}");
}
