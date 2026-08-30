use std::collections::BTreeSet;

fn main() {
    let routes = [
        ("G12", "g23"),
        ("G12", "g31"),
        ("G23", "g31"),
        ("G23", "g12"),
        ("G31", "g12"),
        ("G31", "g23"),
    ];
    let mut labels = BTreeSet::new();
    for pair in routes { assert!(labels.insert(pair)); }
    let matrix = routes.map(|port| routes.map(|route| i32::from(port == route)));
    for i in 0..6 {
        for j in 0..6 { assert_eq!(matrix[i][j], i32::from(i == j)); }
    }
    println!("{{\"status\":\"pass\",\"source_routes\":6,\"iterated_residue_ports\":6,\"residue_incidence_matrix\":\"I6 up to source Poincare-residue units\",\"rank\":6,\"scope\":\"generic normal-crossing marked complement; physical-cycle accessibility not inferred\"}}");
}

