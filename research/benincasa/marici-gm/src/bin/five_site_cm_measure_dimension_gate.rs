use serde_json::json;
use std::fs;

fn exponent_numerator(d: i32, edges: i32) -> i32 { d - edges - 1 }

fn main() {
    let edges = 5;
    let generic_double_cover_dimension = 5;
    let physical_dimension = 3;
    assert_eq!(exponent_numerator(generic_double_cover_dimension, edges), -1);
    assert_eq!(exponent_numerator(physical_dimension, edges), -3);
    assert!(physical_dimension < edges);
    let packet = json!({
        "schema":"marici.benincasa.five_site.cm_measure_dimension_gate.v1",
        "primary_source":"Benincasa-Vazao arXiv:2402.06558v3, equations (3.6)-(3.10)",
        "one_loop_edge_count":edges,
        "cm_measure_exponent":"(d-n_e-1)/2=(d-6)/2",
        "d5_exponent":"-1/2",
        "d5_coefficient_model":"square-root/double-cover model used in Entries 1210-1212",
        "d3_exponent":"-3/2",
        "d3_independent_loop_variables":physical_dimension,
        "d3_constraint":"d<n_e, so the source states not all five edge weights are independent and the loop integral is d-fold",
        "generic_branch_geometry_entries_1207_1210":"retained",
        "physical_interpretation_entries_1211_1212":"restricted to the d=5 analytically continued coefficient sector",
        "required_next_object":"source-derived d=3 rank-constrained five-site CM current",
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-cm-measure-dimension-gate.json",
              serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
