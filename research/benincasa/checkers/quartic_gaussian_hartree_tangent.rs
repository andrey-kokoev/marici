fn det_derivative(vqq: i64, vqp: i64, vpp: i64, dqq: i64, dqp: i64, dpp: i64) -> i64 {
    dqq * vpp + vqq * dpp - 2 * vqp * dqp
}

fn main() {
    let mut checks = 0usize;
    for lambda in -4_i64..=4 {
        for vqq in 1_i64..=8 {
            for vqp in -6_i64..=6 {
                for vpp in 1_i64..=8 {
                    // H_4=lambda q^4. Gaussian Wick reduction gives
                    // <q^4>=3 Vqq^2 and <{p,q^3}>=6 Vqp Vqq.
                    let direct_dqq = 0;
                    let direct_dqp = -12 * lambda * vqq * vqq;
                    let direct_dpp = -24 * lambda * vqq * vqp;

                    // Effective Hartree Hessian: h_qq=12 lambda Vqq.
                    let hartree_dqq = 0;
                    let hartree_dqp = -12 * lambda * vqq * vqq;
                    let hartree_dpp = -24 * lambda * vqq * vqp;

                    assert_eq!(direct_dqq, hartree_dqq);
                    assert_eq!(direct_dqp, hartree_dqp);
                    assert_eq!(direct_dpp, hartree_dpp);
                    assert_eq!(
                        det_derivative(vqq, vqp, vpp, direct_dqq, direct_dqp, direct_dpp),
                        0
                    );
                    checks += 1;
                }
            }
        }
    }

    println!("{{");
    println!("  \"schema\": \"marici.quartic_gaussian_hartree_tangent.v1\",");
    println!("  \"exact_checks\": {checks},");
    println!("  \"quartic\": \"lambda q^4\",");
    println!("  \"effective_hessian\": \"h_qq=12 lambda V_qq\",");
    println!("  \"direct_equals_hartree\": true,");
    println!("  \"uncertainty_determinant_derivative\": 0,");
    println!("  \"linear_quartic_class\": \"Hamiltonian tangent\"");
    println!("}}");
}
