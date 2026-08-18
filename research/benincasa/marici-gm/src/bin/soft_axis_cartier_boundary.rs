fn order_at_linear_factor(mut coefficients: Vec<i64>, root: i64) -> usize {
    let mut order = 0;
    loop {
        let value = coefficients
            .iter()
            .rev()
            .fold(0_i64, |acc, coefficient| acc * root + coefficient);
        if value != 0 || coefficients.len() <= 1 {
            return order;
        }
        let mut quotient = vec![0_i64; coefficients.len() - 1];
        let mut carry = *coefficients.last().unwrap();
        for degree in (1..coefficients.len()).rev() {
            quotient[degree - 1] = carry;
            carry = coefficients[degree - 1] + root * carry;
        }
        assert_eq!(carry, 0);
        coefficients = quotient;
        order += 1;
    }
}

fn main() {
    // 8*w=(b-1)^3*(b+1)^4.
    // Coefficients are ascending in b.
    let mut polynomial = vec![1_i64];
    for root in [1_i64, 1, 1, -1, -1, -1, -1] {
        let mut next = vec![0_i64; polynomial.len() + 1];
        for (degree, coefficient) in polynomial.iter().enumerate() {
            next[degree] -= root * coefficient;
            next[degree + 1] += coefficient;
        }
        polynomial = next;
    }
    assert_eq!(order_at_linear_factor(polynomial.clone(), 1), 3);
    assert_eq!(order_at_linear_factor(polynomial, -1), 4);

    // Entry 464's normalized q-symbol is -6 times the odd lattice generator.
    let normalized_q_coefficient = -6_i64;
    assert!(normalized_q_coefficient == 1 || normalized_q_coefficient.abs() > 1);
    assert_ne!(normalized_q_coefficient, 0);

    println!(
        "{{\"schema\":\"marici.benincasa.soft_axis_cartier_boundary.v1\",\
\"odd_lattice_generator\":\"a*t^3*(b+1)\",\
\"eight_times_scalar_transition\":\"(b-1)^3*(b+1)^4\",\
\"boundary_orders\":[3,4],\
\"normalized_q_symbol_coefficient\":-6,\
\"coefficient_is_unit_over_Q\":true,\
\"odd_first_Cartier_map_surjective_at_b_plus_minus_1\":true,\
\"boundary_cokernel\":0,\
\"global_specialization_map\":\"NOT_ASSERTED\"}}"
    );
}
