use serde_json::{json, Value};
use std::{fs, path::Path};

fn read(path: &str) -> Value {
    serde_json::from_str(&fs::read_to_string(path).expect("read packet")).expect("parse packet")
}

fn main() {
    let dense = read("../string-six-point-dense-momentum-kernel.json");
    let boundary = read("../string-six-point-twisted-boundary-support.json");

    assert_eq!(dense["schema"], "marici.benincasa.string_six_point_dense_kernel_certificate.v1");
    assert_eq!(dense["checks"]["total_valuation"], 18);
    assert_eq!(boundary["schema"], "marici.benincasa.string_six_point_twisted_boundary_support.v1");
    assert_eq!(boundary["total_fitting_zero_valuation"], 12);
    assert_eq!(boundary["unlocalized_chamber_lattice_equals_betti_lattice"], false);

    let out = json!({
        "schema": "marici.benincasa.string_six_point_dual_regularization_type_gate.v1",
        "available_maps": {
            "source_intersection": "M_block : sparse_right_cycles x common_left_cycles",
            "dense_klt_contraction": "S^T : common_left_cycles x dense_right_cycles",
            "composite": "M_block S^T : sparse_right_cycles x dense_right_cycles",
            "twisted_boundary": "partial(gamma)=(M-1)e on chains"
        },
        "required_map": "Reg^vee : chamber_vertex_cochains -> dual_regularized_Betti_object",
        "variance_checks": {
            "composite_is_cycle_basis_transition": true,
            "twisted_boundary_is_chain_variance": true,
            "required_map_is_cochain_to_dual_betti_variance": true,
            "transpose_requires_unprovided_pairing": true
        },
        "conclusion": "The frozen six-point packets do not type the dual regularization map; neither M_block S^T nor its bare transpose may be applied to the chamber cochain primitive.",
        "next_falsifier": "Derive the source-normalized twisted cycle/cochain intersection pairing, including orientations and dual local-system convention, then compute the adjoint regularization map."
    });

    let output = Path::new("../string-six-point-dual-regularization-type-gate.json");
    fs::write(output, serde_json::to_string_pretty(&out).unwrap() + "\n").expect("write packet");
    println!("{}", serde_json::to_string(&out).unwrap());
}
