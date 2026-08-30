fn main() {
    // Simultaneous hard scaling q ~ k ~ Q at fixed nonzero conformal times.
    let radial_measure_degree = 2_i32;
    let source_vertex_degree = 4_i32; // (p^2+q^2+k^2)^2
    let wightman_q_degree = -1_i32;
    let wightman_k_degree = -1_i32;
    let raw_loop_degree = radial_measure_degree
        + source_vertex_degree
        + wightman_q_degree
        + wightman_k_degree;
    assert_eq!(raw_loop_degree, 4);

    // Hadamard input: beta_Q=o(Q^-2).  Record the strict bound rather than
    // replacing it by an equality.
    let beta_upper_degree = -2_i32;
    let middle_state_dependent_upper_degree = raw_loop_degree + beta_upper_degree;
    assert_eq!(middle_state_dependent_upper_degree, 2);

    let internal_statistical_occurrences = ["q", "k=|p-q|"];
    assert_eq!(internal_statistical_occurrences.len(), 2);

    println!(
        "{{\"schema\":\"marici.benincasa.keldysh_uv_responsibility_split.v1\",\"raw_radial_integrand_degree\":{},\"hadamard_middle_degree_bound\":\"strictly_less_than_{}\",\"external_placement_loop_type\":\"bunch_davies_vacuum_self_energy\",\"internal_statistical_occurrences\":[\"{}\",\"{}\"],\"convergence_claim\":false,\"status\":\"verified\"}}",
        raw_loop_degree,
        middle_state_dependent_upper_degree,
        internal_statistical_occurrences[0],
        internal_statistical_occurrences[1]
    );
}

