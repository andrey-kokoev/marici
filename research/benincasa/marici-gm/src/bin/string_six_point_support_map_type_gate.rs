use serde_json::json;

fn main(){
    let dense=["A2","A3","A4","X","B24","B34"];
    let sparse=["X","Y","Z","Q"];
    let overlap=["X"];
    let declared_relation="Q=X*Y*Z";
    let unresolved=["Z","Q"];
    assert_eq!(dense.len(),6);
    assert_eq!(sparse.len(),4);
    assert_eq!(overlap.len(),1);
    let packet=json!({
      "schema":"marici.benincasa.string_six_point_support_map_type_gate.v1",
      "dense_kernel_generators":dense,
      "sparse_block_generators":sparse,
      "explicit_overlap":overlap,
      "declared_sparse_relation":declared_relation,
      "unresolved_branch_generators":unresolved,
      "source_relation_expressing_Z_in_dense_ring":false,
      "source_relation_expressing_Q_in_dense_ring":false,
      "branch_to_dense_occurrence_map":"undefined",
      "factor_matching_without_map":"prohibited",
      "required_missing_datum":"physical six-point Mandelstam/conservation dictionary for the sparse block inside the dense kernel ring"
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-support-map-type-gate.json",&text).unwrap();print!("{text}");
}
