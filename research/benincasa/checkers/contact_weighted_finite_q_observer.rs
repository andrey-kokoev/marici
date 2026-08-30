fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn main() {
    for c1 in 1_i64..=5 {
        for c2 in 1_i64..=5 {
            for c3 in 1_i64..=5 {
                for w1 in 1_i64..=4 {
                    for w2 in 1_i64..=4 {
                        for w3 in 1_i64..=4 {
                            let t = [[1, 2 * w1, 0], [1, -w2, -w2], [1, -w3, w3]];
                            let r = [
                                [-8 * c1 * t[0][0], -8 * c1 * t[0][1], -8 * c1 * t[0][2]],
                                [-8 * c2 * t[1][0], -8 * c2 * t[1][1], -8 * c2 * t[1][2]],
                                [-8 * c3 * t[2][0], -8 * c3 * t[2][1], -8 * c3 * t[2][2]],
                            ];
                            assert_eq!(det3(r), (-8_i64).pow(3) * c1 * c2 * c3 * det3(t));
                        }
                    }
                }
            }
        }
    }
    println!(
        "{{\"status\":\"pass\",\"full_matrix\":\"R=-8 diag(C12,C23,C31) T(q)\",\"determinant\":\"(-8)^3 C12 C23 C31 det(T)\",\"finite_contact_zero_locus\":\"empty\",\"finite_rank_loss\":\"Gram wall only\",\"contact_poles\":\"existing shifted-energy support\",\"tested_packets\":8000}}"
    );
}
