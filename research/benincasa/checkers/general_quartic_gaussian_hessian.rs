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

fn det_derivative(v: [[i64; 2]; 2], dv: [[i64; 2]; 2]) -> i64 {
    dv[0][0] * v[1][1] + v[0][0] * dv[1][1]
        - dv[0][1] * v[1][0]
        - v[0][1] * dv[1][0]
}

fn main() {
    let j = [[0, 1], [-1, 0]];
    let coefficient_sets = [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [2, -1, 3, 1, -2],
        [-3, 2, 1, -2, 3],
    ];
    let mut checks = 0usize;

    for [a, b, c, d, e] in coefficient_sets {
        for q in 1_i64..=8 {
            for r in -6_i64..=6 {
                for p in 1_i64..=8 {
                    let v = [[q, r], [r, p]];
                    // K=<Hessian H_4> for
                    // H_4=a q^4+b q^3p+c q^2p^2+d qp^3+e p^4.
                    let k = [
                        [12 * a * q + 6 * b * r + 2 * c * p,
                         3 * b * q + 4 * c * r + 3 * d * p],
                        [3 * b * q + 4 * c * r + 3 * d * p,
                         2 * c * q + 6 * d * r + 12 * e * p],
                    ];
                    assert_eq!(k[0][1], k[1][0]);
                    let generator = matmul(j, k);
                    assert_eq!(generator[0][0] + generator[1][1], 0);
                    let dv = add(matmul(generator, v), matmul(v, transpose(generator)));
                    assert_eq!(det_derivative(v, dv), 0);
                    checks += 1;
                }
            }
        }
    }

    println!("{{");
    println!("  \"schema\": \"marici.general_quartic_gaussian_hessian.v1\",");
    println!("  \"exact_checks\": {checks},");
    println!("  \"quartic_basis\": [\"q^4\",\"q^3p\",\"q^2p^2\",\"qp^3\",\"p^4\"],");
    println!("  \"effective_hessian\": \"K=<Hessian H_4>\",");
    println!("  \"generator\": \"A=J K\",");
    println!("  \"generator_trace_zero\": true,");
    println!("  \"uncertainty_determinant_derivative\": 0");
    println!("}}");
}
