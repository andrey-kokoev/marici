fn gcd(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        let remainder = a % b;
        a = b;
        b = remainder;
    }
    a
}

fn main() {
    // Entry266 computes the full-log carrier degree in the primitive Q-top
    // line. Existing central/road corrections lie in F_B and therefore have
    // zero image under the literal quotient E -> Q.
    let carrier_q_coefficient = 2_i64;
    let existing_central_q_coefficient = 0_i64;
    let current_smith_factor = gcd(carrier_q_coefficient, existing_central_q_coefficient);
    assert_eq!(current_smith_factor, 2);
    let current_cokernel_order = current_smith_factor;
    assert_eq!(current_cokernel_order, 2);

    // No integral carrier coordinate reaches the primitive target value one.
    assert!((-32_i64..=32).all(|coordinate| carrier_q_coefficient * coordinate != 1));

    // An added boundary-crossing connector with coefficient m repairs the
    // row exactly when m is odd. The primitive possibilities are +/-1.
    let repairs = (-8_i64..=8)
        .map(|m| (m, gcd(carrier_q_coefficient, m)))
        .collect::<Vec<_>>();
    assert!(repairs
        .iter()
        .all(|(m, smith)| (*smith == 1) == (m.rem_euclid(2) == 1)));
    let primitive_repairs = repairs
        .iter()
        .filter(|(m, smith)| *smith == 1 && m.abs() == 1)
        .map(|(m, _)| *m)
        .collect::<Vec<_>>();
    assert_eq!(primitive_repairs, vec![-1, 1]);

    // The abstract local exceptional coefficient is +1, but without its
    // support map to Q its effective column remains zero. Equating these is
    // precisely the missing, non-circular geometric datum.
    let abstract_local_exceptional_coefficient = 1_i64;
    assert_eq!(abstract_local_exceptional_coefficient, 1);
    assert_ne!(
        abstract_local_exceptional_coefficient,
        existing_central_q_coefficient
    );

    println!(
        "{{\"status\":\"falsified_scoped_literal_support_preserving_primitive_Q_map\",\"carrier_Q_coefficient\":2,\"existing_central_Q_coefficient\":0,\"current_row\":[2,0],\"current_smith_factors\":[2],\"current_cokernel\":\"Z/2\",\"primitive_qSigma_reachable\":false,\"abstract_local_exceptional_coefficient\":1,\"abstract_coefficient_has_literal_Q_support_map\":false,\"repair_row\":\"[2,m]\",\"repair_iff_m_odd\":true,\"minimal_primitive_connector_coefficients\":[-1,1],\"mapping_fiber_instantiated\":false,\"physical_p_defined\":false}}"
    );
}
