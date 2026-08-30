fn main() {
    let mut checked_ranks = 0usize;
    for rank in 1_i64..=4096 {
        // For finite matrices, tr(QP-PQ)=0. Exact [Q,P]=2i I would require
        // imaginary trace coefficient 2*rank, which is nonzero.
        let commutator_trace_imaginary_coefficient = 0_i64;
        let ccr_trace_imaginary_coefficient = 2 * rank;
        assert_ne!(commutator_trace_imaginary_coefficient, ccr_trace_imaginary_coefficient);
        checked_ranks += 1;
    }

    println!("{{");
    println!("  \"schema\": \"marici.ccr_flat_extension_trace_obstruction.v1\",");
    println!("  \"checked_positive_ranks\": {checked_ranks},");
    println!("  \"finite_matrix_commutator_trace\": 0,");
    println!("  \"exact_ccr_trace\": \"2 i rank\",");
    println!("  \"rank_preserving_flat_extension_possible\": false,");
    println!("  \"required_gns_dimension\": \"infinite\"");
    println!("}}");
}
