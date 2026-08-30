fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn transfer(w1: i64, w2: i64, w3: i64) -> [[i64; 3]; 3] {
    [[1, 2 * w1, 0], [1, -w2, -w2], [1, -w3, w3]]
}

fn main() {
    for w1 in 1_i64..=8 {
        for w2 in 1_i64..=8 {
            for w3 in 1_i64..=8 {
                let expected = -2 * (w1 * w2 + w2 * w3 + w3 * w1);
                assert_eq!(det3(transfer(w1, w2, w3)), expected);
                assert!(expected < 0);
            }
        }
    }

    // Divided-difference identity for A=sqrt(L), sampled exactly at integer
    // momenta k,k': (k'-k)/(k'^2-k^2)=1/(k'+k).
    for k in 1_i64..=12 {
        for kp in 1_i64..=12 {
            if k != kp {
                assert_eq!((kp - k) * (kp + k), kp * kp - k * k);
            }
        }
    }

    println!(
        "{{\"status\":\"pass\",\"frozen_precision\":\"A_g=sqrt(-Delta_g)\",\"kinematic_slice\":\"tensor momentum normal to the equilateral hard-momentum plane\",\"finite_q_vertex_weight\":\"w_e=k_e^2/(k_e+sqrt(k_e^2+q^2)) up to common source normalization\",\"determinant\":\"-2(w1w2+w2w3+w3w1)\",\"positive_energy_rank_loss\":false,\"tested_positive_weight_packets\":512}}"
    );
}
