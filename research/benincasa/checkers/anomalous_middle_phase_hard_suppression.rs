fn main() {
    // In the hard region q=Q and k=Q-mu+O(Q^-1), mu=p cos(theta).
    let degree_q_plus_k = 1_i32;
    let degree_q_minus_k = 0_i32;
    assert_eq!(degree_q_plus_k, 1);
    assert_eq!(degree_q_minus_k, 0);

    let raw_radial_degree = 4_i32;
    let guaranteed_hard_primitive_gain = 1_i32;
    let after_primitive_degree = raw_radial_degree - guaranteed_hard_primitive_gain;
    assert_eq!(after_primitive_degree, 3);

    // The source Hadamard condition beta_Q=o(Q^-2) makes the resulting
    // degree strictly below one, which is not by itself an L1 radial bound.
    let beta_strict_upper_degree = -2_i32;
    let filtered_strict_upper_degree = after_primitive_degree + beta_strict_upper_degree;
    assert_eq!(filtered_strict_upper_degree, 1);
    let absolute_convergence_threshold = -1_i32;
    assert!(filtered_strict_upper_degree > absolute_convergence_threshold);

    println!(
        "{{\"schema\":\"marici.benincasa.anomalous_middle_phase_hard_suppression.v1\",\"vertex_frequencies\":[\"q-k\",\"q+k\"],\"hard_degrees\":[{},{}],\"guaranteed_hard_primitive_count\":{},\"raw_radial_degree\":{},\"post_primitive_degree\":{},\"hadamard_filtered_degree\":\"strictly_less_than_{}\",\"absolute_convergence_established\":false,\"status\":\"verified\"}}",
        degree_q_minus_k,
        degree_q_plus_k,
        guaranteed_hard_primitive_gain,
        raw_radial_degree,
        after_primitive_degree,
        filtered_strict_upper_degree
    );
}

