use serde_json::{json, Value};

fn read(path: &str) -> Value {
    serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap()
}

fn advertises_support_changing_map(v: &Value) -> bool {
    [
        "costalk_to_edge_map",
        "cousin_boundary",
        "normal_gysin_to_edge",
        "edge_restriction",
        "chain_cochain_pairing",
    ]
    .iter()
    .any(|key| v.get(*key).is_some())
}

fn main() {
    let modification = read("../string-six-point-rank-one-modification-descent.json");
    let edge = read("../string-six-point-pochhammer-cochain-closure.json");
    let prior_gate = read("../string-six-point-edge-vertex-type-gate.json");

    assert_eq!(modification["cyclic_holonomy"], 1);
    assert_eq!(edge["twisted_defects"].as_array().unwrap().len(), 6);
    assert_eq!(edge["weighted_two_cell_boundary"], "0");
    assert_eq!(prior_gate["direct_comparison_typed"], false);
    assert!(!advertises_support_changing_map(&modification));
    assert!(!advertises_support_changing_map(&edge));
    assert!(!advertises_support_changing_map(&prior_gate));

    let packet = json!({
        "schema": "marici.benincasa.string_six_point_normal_gysin_edge_support_gate.v1",
        "left_object": {
            "source": "Entry 997",
            "cohomological_degree_after_normal_gysin": 1,
            "support": "codimension-two signed source-wall intersection",
            "variance": "normal elementary-modification costalk",
            "generic_rank_per_character": 1
        },
        "right_object": {
            "source": "Entry 979",
            "cohomological_degree": 1,
            "support": "six oriented codimension-one chamber edges",
            "variance": "twisted chamber edge cochain",
            "edge_count": 6,
            "two_cell_boundary": 0
        },
        "audited_packets": [
            "string-six-point-rank-one-modification-descent",
            "string-six-point-pochhammer-cochain-closure",
            "string-six-point-edge-vertex-type-gate"
        ],
        "degree_match_after_gysin": true,
        "support_and_variance_match": false,
        "source_costalk_to_edge_map_present": false,
        "comparison_typed": false,
        "classification": "the normal Gysin shift aligns cohomological degree but does not supply the missing codimension-two-costalk to chamber-edge support morphism",
        "prohibited_inference": "rank, character, and degree agreement do not identify the modification line with the chamber-edge class",
        "required_next_datum": "derive the Cousin boundary/restriction from each labelled signed wall intersection to its incident oriented chamber edges, including units and orientations, or retain the objects as separate terms of a total complex"
    });

    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-normal-gysin-edge-support-gate.json", &text).unwrap();
    print!("{text}");
}
