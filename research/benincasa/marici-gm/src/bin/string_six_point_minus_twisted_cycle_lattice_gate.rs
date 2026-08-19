use serde_json::{json,Value};

fn read(path:&str)->Value{serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap()}

fn main(){
    let arc=read("../string-six-point-minus-recombination-edge-restriction.json");
    let boundary=read("../string-six-point-twisted-boundary-support.json");
    let incidence=read("../string-six-point-recombination-hexagon-incidence.json");
    for sheet in arc["sheet_restrictions"].as_array().unwrap(){
        assert_eq!(sheet["primitive_nonzero_indices"],json!([4,5]));
        assert_eq!(sheet["edge_class_in_image_of_delta"],true);
    }
    let factor=boundary["fitting_factors"].as_array().unwrap().iter().find(|x|x["monodromy_square_root"]=="A3*B34/Z").unwrap();
    assert_eq!(factor["fitting_valuation"],2);
    assert_eq!(factor["twisted_boundary_factor"],"(A3*B34/Z)^2-1");
    assert_eq!(boundary["closure_coefficient"],"1/(M-1)");
    assert_eq!(incidence["wall_occurrence_blocks"]["A3B34_over_Z"],json!([4,5]));
    let packet=json!({
      "schema":"marici.benincasa.string_six_point_minus_twisted_cycle_lattice_gate.v1",
      "relative_primitive_support":[4,5],
      "support_wall":"(A3*B34/Z)^2-1",
      "support_wall_occurrence_multiplicity":2,
      "fitting_valuation":2,
      "relative_cellular_class":"exact",
      "closed_twisted_cycle_regularization":"requires 1/(M-1)",
      "regular_at_resonance":false,
      "supported_nearby_class_determined":false,
      "classification":"relative cellular exactness does not imply exactness in the unlocalized closed twisted-cycle lattice at M=1",
      "required_next_datum":"the source-normalized two-occurrence regularization block and its first Laurent residue at (A3*B34/Z)^2=1",
      "new_carrier_divisor_required":false
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-minus-twisted-cycle-lattice-gate.json",&text).unwrap();
    print!("{text}");
}
