use serde_json::json;

fn main(){
    let dense=["A2","A3","A4","X","B24","B34"];
    let sparse=["X","Y","Z","Q"];
    let overlap=["X"];
    let declared_relation="Q=X*Y*Z";
    let common_ambient=["s12","s13","s14","s23","s24","s34","s25","s35","s45"];
    assert_eq!(dense.len(),6);
    assert_eq!(sparse.len(),4);
    assert_eq!(overlap.len(),1);
    let packet=json!({
      "schema":"marici.benincasa.string_six_point_support_map_type_gate.v2",
      "dense_kernel_generators":dense,
      "sparse_block_generators":sparse,
      "explicit_overlap":overlap,
      "declared_sparse_relation":declared_relation,
      "common_conserved_kinematic_generators":common_ambient,
      "branch_dictionary":{"X":"exp(i*pi*s23)","Y":"exp(i*pi*s25)","Z":"exp(i*pi*s35)","Q":"exp(i*pi*s235)"},
      "additive_relation":"s235=s23+s25+s35",
      "source_relation_expressing_Z_in_dense_six_generator_subring":false,
      "direct_branch_to_dense_six_generator_map":"absent and unnecessary",
      "comparison_via_common_ambient_ring":"typed",
      "canonical_transition":"T=M_block*K_dense",
      "source":"Ledger Entry 905 and string-six-point-basis-transition-divisor.json",
      "entry_951_original_gate":"superseded"
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-support-map-type-gate.json",&text).unwrap();print!("{text}");
}
