fn det2(m: [[i64; 2]; 2]) -> i64 {
    m[0][0] * m[1][1] - m[0][1] * m[1][0]
}

fn matmul(a: [[i64; 2]; 2], b: [[i64; 2]; 2]) -> [[i64; 2]; 2] {
    let mut c = [[0; 2]; 2];
    for i in 0..2 {
        for j in 0..2 {
            for k in 0..2 {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    c
}

fn transpose(a: [[i64; 2]; 2]) -> [[i64; 2]; 2] {
    [[a[0][0], a[1][0]], [a[0][1], a[1][1]]]
}

fn add(a: [[i64; 2]; 2], b: [[i64; 2]; 2]) -> [[i64; 2]; 2] {
    [
        [a[0][0] + b[0][0], a[0][1] + b[0][1]],
        [a[1][0] + b[1][0], a[1][1] + b[1][1]],
    ]
}

fn determinant_derivative(v: [[i64; 2]; 2], dv: [[i64; 2]; 2]) -> i64 {
    dv[0][0] * v[1][1] + v[0][0] * dv[1][1]
        - dv[0][1] * v[1][0]
        - v[0][1] * dv[1][0]
}

fn main() {
    let j = [[0, 1], [-1, 0]];
    let mut hamiltonian_checks = 0usize;
    let mut cut_checks = 0usize;

    for a in -3..=3 {
        for b in -3..=3 {
            for c in -3..=3 {
                let h = [[a, b], [b, c]];
                let generator = matmul(j, h);
                assert_eq!(generator[0][0] + generator[1][1], 0);

                for r in 1..=4 {
                    for s in -3..=3 {
                        for t in 1..=4 {
                            let v = [[r, s], [s, t]];
                            let dv_h = add(matmul(generator, v), matmul(v, transpose(generator)));
                            assert_eq!(determinant_derivative(v, dv_h), 0);
                            hamiltonian_checks += 1;

                            if det2(v) >= 0 {
                                for x in -2..=2 {
                                    for y in -2..=2 {
                                        let noise = [[x * x, x * y], [x * y, y * y]];
                                        assert!(determinant_derivative(v, noise) >= 0);
                                        cut_checks += 1;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    println!("{{");
    println!("  \"schema\": \"marici.gaussian_counterterm_cut_uncertainty.v1\",");
    println!("  \"hamiltonian_counterterm_checks\": {hamiltonian_checks},");
    println!("  \"hamiltonian_uncertainty_derivative\": 0,");
    println!("  \"rank_one_cut_checks\": {cut_checks},");
    println!("  \"rank_one_cut_uncertainty_derivative_nonnegative\": true,");
    println!("  \"counterterm_class\": \"frozen Hermitian local quadratic\",");
    println!("  \"cut_class\": \"positive labelled outer product\"");
    println!("}}");
}
