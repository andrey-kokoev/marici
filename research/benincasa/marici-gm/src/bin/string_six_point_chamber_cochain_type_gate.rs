use serde_json::{json, Value};

fn read(path: &str) -> Value {
    serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap()
}

fn main() {
    let cochain = read("../string-six-point-circuit-exceptional-cochain.json");
    let chamber = read("../string-six-point-loaded-transition-gate.json");
    let occurrence = read("../string-six-point-mixed-corner-occurrence.json");
    let loaded = read("../string-six-point-loaded-corner-comparison.json");

    assert_eq!(cochain["cochain"].as_array().unwrap().len(), 6);
    assert_eq!(loaded["matrix"].as_array().unwrap().len(), 6);
    assert_eq!(chamber["edge_loadings"].as_array().unwrap().len(), 6);
    assert!(chamber["edge_loadings"]
        .as_array()
        .unwrap()
        .iter()
        .all(|e| e.get("matrix").is_none() && e.get("cochain_map").is_none()));

    let dense_steps = occurrence["dense_permutations"].as_array().unwrap();
    let sparse_steps = occurrence["sparse_permutations"].as_array().unwrap();
    assert_eq!(dense_steps.len(), 3);
    assert_eq!(sparse_steps.len(), 3);
    assert!(dense_steps
        .iter()
        .all(|p| p.as_array().unwrap().len() == 2));
    assert!(sparse_steps
        .iter()
        .all(|p| p.as_array().unwrap().len() == 2));

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_chamber_cochain_type_gate.v1",
        "local_cochain_rank":6,
        "loaded_matrix_shape":[6,6],
        "chamber_edge_count":6,
        "chamber_edge_data":["edge label","half-monodromy label","boundary factor","branch activity"],
        "chamber_edges_with_rational_cochain_map":0,
        "occurrence_chart_count":3,
        "occurrence_transition_shape":[2,2],
        "occurrence_transition_scope":"rank-one mixed-corner source and target blocks",
        "six_edge_target_cochain_transport_present":false,
        "two_cell_homotopy_on_target_cochains_present":false,
        "delta_lambda_typed":false,
        "classification":"the repository fixes one local rank-six cochain, six chamber adjacencies, and a separate rank-two C3 occurrence transport, but no six-edge rational action on the cochain or compatible two-cell homotopy",
        "required_next_datum":"derive target-chamber pullback maps from the same loaded Pochhammer paths, including their action on rational pivot coordinates and circuit homotopies"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-chamber-cochain-type-gate.json", &text).unwrap();
    print!("{text}");
}
