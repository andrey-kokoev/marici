use std::f64::consts::PI;

type Matrix = Vec<Vec<f64>>;

fn permutations() -> Vec<[usize; 3]> {
    vec![
        [2, 3, 4],
        [2, 4, 3],
        [3, 2, 4],
        [3, 4, 2],
        [4, 2, 3],
        [4, 3, 2],
    ]
}

fn dense(s: &[[f64; 7]; 7]) -> Matrix {
    let basis = permutations();
    basis
        .iter()
        .map(|alpha| {
            basis
                .iter()
                .map(|beta| {
                    let mut position = [0usize; 7];
                    for (index, label) in beta.iter().enumerate() {
                        position[*label] = index;
                    }
                    let mut product = 1.0;
                    for t in 0..3 {
                        let i = alpha[t];
                        let mut argument = s[1][i];
                        for j in alpha.iter().skip(t + 1) {
                            if position[i] > position[*j] {
                                argument += s[i][*j];
                            }
                        }
                        product *= (PI * argument).sin();
                    }
                    product
                })
                .collect()
        })
        .collect()
}

fn block(s: &[[f64; 7]; 7], p: [usize; 7]) -> [[f64; 2]; 2] {
    let v = |i: usize, j: usize| s[p[i]][p[j]];
    let (a, x, y, z) = (v(1, 2), v(3, 4), v(3, 5), v(4, 5));
    let csc = |u: f64| 1.0 / (PI * u).sin();
    let cot = |u: f64| (PI * u).cos() / (PI * u).sin();
    let q = x + y + z;
    let d = csc(a) * csc(x) * csc(q);
    [
        [d, -csc(a) * csc(q) * (cot(x) + cot(y))],
        [-csc(a) * csc(q) * (cot(x) + cot(z)), d],
    ]
}

fn block_kernel(s: &[[f64; 7]; 7]) -> Matrix {
    let id = [0, 1, 2, 3, 4, 5, 6];
    let p23 = [0, 1, 3, 2, 4, 5, 6];
    let p24 = [0, 1, 4, 3, 2, 5, 6];
    let b0 = block(s, id);
    let b1 = block(s, p23);
    let raw = block(s, p24);
    let b2 = [[raw[1][1], raw[1][0]], [raw[0][1], raw[0][0]]];
    let blocks = [b0, b1, b2];
    let mut result = vec![vec![0.0; 6]; 6];
    for k in 0..3 {
        for i in 0..2 {
            for j in 0..2 {
                result[2 * k + i][2 * k + j] = blocks[k][i][j];
            }
        }
    }
    result
}

fn multiply(a: &Matrix, b: &Matrix) -> Matrix {
    let mut r = vec![vec![0.0; b[0].len()]; a.len()];
    for i in 0..a.len() {
        for k in 0..b.len() {
            for j in 0..b[0].len() {
                r[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    r
}
fn transpose(a: &Matrix) -> Matrix {
    let mut r = vec![vec![0.0; a.len()]; a[0].len()];
    for i in 0..a.len() {
        for j in 0..a[0].len() {
            r[j][i] = a[i][j];
        }
    }
    r
}
fn scale(mut a: Matrix, q: f64) -> Matrix {
    for row in &mut a {
        for x in row {
            *x *= q;
        }
    }
    a
}
fn combine(a: &Matrix, qa: f64, b: &Matrix, qb: f64) -> Matrix {
    let mut r = vec![vec![0.0; a[0].len()]; a.len()];
    for i in 0..a.len() {
        for j in 0..a[0].len() {
            r[i][j] = qa * a[i][j] + qb * b[i][j];
        }
    }
    r
}
fn max_diff(a: &Matrix, b: &Matrix) -> f64 {
    let mut r: f64 = 0.0;
    for i in 0..a.len() {
        for j in 0..a[0].len() {
            r = r.max((a[i][j] - b[i][j]).abs());
        }
    }
    r
}
fn norm(a: &Matrix) -> f64 {
    a.iter().flatten().map(|x| x * x).sum::<f64>().sqrt()
}
fn row_gram_determinant(a: &Matrix) -> f64 {
    let g00: f64 = a[0].iter().map(|x| x * x).sum();
    let g11: f64 = a[1].iter().map(|x| x * x).sum();
    let g01: f64 = a[0].iter().zip(&a[1]).map(|(x, y)| x * y).sum();
    g00 * g11 - g01 * g01
}

fn kinematics_mode(epsilon: f64, delta: f64, third: f64, seed: f64, mode: &str) -> [[f64; 7]; 7] {
    let mut s = [[0.0; 7]; 7];
    let z_generic = 0.197 - 0.009 * seed;
    let x_generic = 0.181 + 0.019 * seed;
    let (x, y, z) = match mode {
        "x" => (epsilon, delta - epsilon - z_generic, z_generic),
        "y" => (delta - epsilon - z_generic, epsilon, z_generic),
        "z" => (x_generic, delta - x_generic - epsilon, epsilon),
        _ => panic!("unknown subchannel mode"),
    };
    let values = [
        ((1, 2), 0.173 + 0.013 * seed),
        ((1, 3), -0.219 + 0.011 * seed),
        ((1, 4), third),
        ((2, 3), x),
        ((2, 4), -0.131 + 0.007 * seed),
        ((2, 5), z),
        ((3, 4), 0.241 + 0.019 * seed),
        ((3, 5), y),
        ((4, 5), -0.163 - 0.005 * seed),
    ];
    for ((i, j), x) in values {
        s[i][j] = x;
        s[j][i] = x;
    }
    s
}
fn kinematics(epsilon: f64, delta: f64, seed: f64) -> [[f64; 7]; 7] {
    kinematics_mode(epsilon, delta, 0.287 - 0.017 * seed, seed, "x")
}
fn normalized_transition(epsilon: f64, delta: f64, seed: f64) -> Matrix {
    let s = kinematics(epsilon, delta, seed);
    let t = multiply(&block_kernel(&s), &transpose(&dense(&s)));
    scale(t, (PI * delta).sin())
}

fn normalized_three_normal(epsilon: f64, delta: f64, third: f64, seed: f64, mode: &str) -> Matrix {
    let s = kinematics_mode(epsilon, delta, third, seed, mode);
    let t = multiply(&block_kernel(&s), &transpose(&dense(&s)));
    scale(t, (PI * delta).sin() * (PI * third).sin())
}

fn main() {
    let hs = [1e-2, 5e-3, 2.5e-3, 1.25e-3, 6.25e-4];
    let mut certificates = Vec::new();
    for seed in [0.0, 1.0, 2.0] {
        let mut route_a = Vec::new();
        let mut route_b = Vec::new();
        for h in hs {
            route_a.push(normalized_transition(h, h * h, seed));
            route_b.push(normalized_transition(h * h, h, seed));
        }
        let a_errors: Vec<_> = (1..route_a.len())
            .map(|i| max_diff(&route_a[i], &route_a[i - 1]))
            .collect();
        let b_errors: Vec<_> = (1..route_b.len())
            .map(|i| max_diff(&route_b[i], &route_b[i - 1]))
            .collect();
        let commutator = max_diff(route_a.last().unwrap(), route_b.last().unwrap());
        let n = route_a.len();
        let extrap_a = combine(&route_a[n - 1], 2.0, &route_a[n - 2], -1.0);
        let extrap_b = combine(&route_b[n - 1], 2.0, &route_b[n - 2], -1.0);
        let extrapolated_commutator = max_diff(&extrap_a, &extrap_b);
        let scale_norm = norm(route_a.last().unwrap()).max(norm(route_b.last().unwrap()));
        certificates.push(serde_json::json!({"seed":seed,"route_a_errors":a_errors,"route_b_errors":b_errors,"final_commutator":commutator,"relative_commutator":commutator/scale_norm,"richardson_commutator":extrapolated_commutator,"norm":scale_norm}));
    }
    let mut maximal_flag_scan = Vec::new();
    for mode in ["x", "y", "z"] {
        let matrices: Vec<Matrix> = hs
            .iter()
            .map(|h| normalized_three_normal(*h, *h, *h, 0.0, mode))
            .collect();
        let norms: Vec<f64> = matrices.iter().map(norm).collect();
        let gram_determinants: Vec<f64> = matrices.iter().map(row_gram_determinant).collect();
        maximal_flag_scan.push(serde_json::json!({"subchannel":mode,"diagonal_norms":norms,"row_gram_determinants":gram_determinants}));
    }
    println!("{}",serde_json::to_string(&serde_json::json!({"schema":"marici.benincasa.string_six_point_mixed_corner.v2","corner":["s23","s235"],"normalization":"sin(pi*s235) T","certificates":certificates,"maximal_flag_discovery":{"normalization":"sin(pi*q) sin(pi*a) T","scan":maximal_flag_scan}})).unwrap());
}
