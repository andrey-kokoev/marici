use serde_json::{json, Value};

fn read(path:&str)->Value{serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap()}
fn has_map(v:&Value)->bool{
    ["edge_to_vertex_map","contraction","chain_homotopy","intersection_pairing","codifferential"]
        .iter().any(|k|v.get(*k).is_some())
}
fn main(){
 let edge=read("../string-six-point-pochhammer-cochain-closure.json");
 let vertex=read("../string-six-point-normal-symbol-comparison.json");
 let local=read("../string-five-point-twisted-boundary.json");
 assert_eq!(edge["twisted_defects"].as_array().unwrap().len(),6);
 assert_eq!(vertex["rank_two_character_count"],2);
 assert!(!has_map(&edge));
 assert!(!has_map(&vertex));
 assert!(!has_map(&local));
 let packet=json!({
  "schema":"marici.benincasa.string_six_point_edge_vertex_type_gate.v1",
  "edge_object":{"degree":1,"rank":6,"variance":"twisted chamber edge cochain","source":"Entry 979"},
  "vertex_objects":{"degree":0,"rank_two_characters":["++","--"],"variance":"dense six-word vertex coefficient planes","source":"Entry 982"},
  "frozen_packets_audited":["string-six-point-pochhammer-cochain-closure","string-six-point-normal-symbol-comparison","string-five-point-twisted-boundary"],
  "edge_to_vertex_map_present":false,
  "intersection_pairing_present":false,
  "codifferential_present":false,
  "direct_comparison_typed":false,
  "classification":"the twisted edge coboundary cannot supply a degree-zero coefficient direction without a separately derived contraction, pairing, or Gysin map",
  "required_next_datum":"construct a source-normalized chamber chain/cochain pairing or retain the edge defect and vertex planes in a total complex without collapsing degrees"
 });
 let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";std::fs::write("../string-six-point-edge-vertex-type-gate.json",&text).unwrap();print!("{text}");
}
