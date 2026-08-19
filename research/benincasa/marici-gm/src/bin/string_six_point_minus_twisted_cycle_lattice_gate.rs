use serde_json::{json,Value};

fn read(path:&str)->Value{serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap()}

fn main(){
    let arc=read("../string-six-point-minus-recombination-edge-restriction.json");
    let boundary=read("../string-six-point-twisted-boundary-support.json");
    let permutation=read("../string-six-point-global-support-permutation.json");
    for sheet in arc["sheet_restrictions"].as_array().unwrap(){
        assert_eq!(sheet["primitive_nonzero_indices"],json!([4,5]));
        assert_eq!(sheet["edge_class_in_image_of_delta"],true);
    }
    let occurrence_to_dense:Vec<usize>=permutation["occurrence_to_dense_indices"].as_array().unwrap().iter().map(|x|x.as_u64().unwrap() as usize).collect();
    let dense_to_occurrence:Vec<usize>=(0..6).map(|d|occurrence_to_dense.iter().position(|x|*x==d).unwrap()).collect();
    assert_eq!(dense_to_occurrence[4],0);
    assert_eq!(dense_to_occurrence[5],3);
    let factors:Vec<&Value>=["Z*A2","A3/Z"].iter().map(|name|boundary["fitting_factors"].as_array().unwrap().iter().find(|x|x["monodromy_square_root"]==*name).unwrap()).collect();
    assert!(factors.iter().all(|x|x["fitting_valuation"]==1));
    assert_eq!(boundary["closure_coefficient"],"1/(M-1)");
    let packet=json!({
      "schema":"marici.benincasa.string_six_point_minus_twisted_cycle_lattice_gate.v2",
      "relative_primitive_dense_support":[4,5],
      "dense_to_occurrence":dense_to_occurrence,
      "primitive_source_occurrences":[0,3],
      "primitive_support_walls":["(Z*A2)^2-1","(A3/Z)^2-1"],
      "fitting_valuations":[1,1],
      "relative_cellular_class":"exact",
      "minus_recombination_walls":["(Z*A2*B24)^2-1","(A3*B34/Z)^2-1"],
      "primitive_walls_vanish_generically_on_minus_recombination":false,
      "closed_twisted_cycle_regularization":"regular at a generic minus recombination point",
      "supported_nearby_class_determined":"zero generically: the relative primitive remains admissible",
      "classification":"Entry 1004 mixed dense chamber indices with sparse occurrence indices; after the frozen permutation, the primitive lies on the two singleton walls and remains regular at generic minus recombination",
      "entry_1004_status":"retracted",
      "new_carrier_divisor_required":false
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-minus-twisted-cycle-lattice-gate.json",&text).unwrap();
    print!("{text}");
}
