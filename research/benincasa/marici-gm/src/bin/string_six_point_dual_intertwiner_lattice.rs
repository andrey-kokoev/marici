use serde_json::{json, Value};
use std::fs;

fn read(path: &str) -> Value {
    serde_json::from_str(&fs::read_to_string(path).expect("read packet")).expect("parse packet")
}

fn main() {
    let dual = read("../string-six-point-diagonal-dual-intertwiner.json");
    let occurrence = read("../string-six-point-global-support-permutation.json");
    assert_eq!(dual["diagonal_solution_dimension"], 1);
    assert_eq!(occurrence["determinant"], 1);

    let expected_vertex = [
        "1",
        "A3^2/Z^2",
        "A3^2*A2^2",
        "A3^2*A2^2/X^2",
        "Z^2*A2^2/X^2",
        "1/X^2",
    ];
    let expected_edge = [
        "A3^2/Z^2",
        "A3^2*A2^2",
        "A3^2*A2^2/X^2",
        "Z^2*A2^2/X^2",
        "1/X^2",
        "1",
    ];
    for sheet in dual["sheets"].as_array().unwrap() {
        let vertex: Vec<_> = sheet["vertex_frame"].as_array().unwrap().iter().map(|x| x.as_str().unwrap()).collect();
        let edge: Vec<_> = sheet["edge_frame"].as_array().unwrap().iter().map(|x| x.as_str().unwrap()).collect();
        assert_eq!(vertex, expected_vertex);
        assert_eq!(edge, expected_edge);
    }

    // Exponent order (A2,A3,Z,X); sums for either diagonal frame.
    let determinant_exponents = [6_i32, 6, 0, -6];
    let packet = json!({
        "schema":"marici.benincasa.string_six_point_dual_intertwiner_lattice.v1",
        "coefficient_ring":"Z[A2^+-1,A3^+-1,Z^+-1,X^+-1]",
        "vertex_determinant":"A2^6*A3^6/X^6",
        "edge_determinant":"A2^6*A3^6/X^6",
        "determinant_exponents_A2_A3_Z_X":determinant_exponents,
        "determinants_are_laurent_units":true,
        "occurrence_permutation_determinant":1,
        "occurrence_transport_preserves_unimodularity":true,
        "finite_lattice_index":1,
        "source_intersection_normalization_matched":false,
        "conclusion":"The diagonal dual cellular intertwiner is unimodular over the frozen Laurent ring, before and after the orientation-preserving occurrence permutation. No finite cellular lattice index remains."
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    fs::write("../string-six-point-dual-intertwiner-lattice.json",&text).unwrap();
    print!("{text}");
}
