use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}

fn main() {
    let loaded = [a("M1"), a("M2"), a("M2"), a("M3"), a("M4"), a("M4")];
    let loaded_holonomy = loaded.iter().cloned().fold(a("1"), |p, x| clean(p * x));
    assert_eq!(loaded_holonomy, a("M1*M2^2*M3*M4^2"));
    assert_ne!(loaded_holonomy, a("1"));

    let hex = [a("B34"), a("B24"), a("X"), a("1/B34"), a("1/B24"), a("1/X")];
    let hex_holonomy = hex.iter().cloned().fold(a("1"), |p, x| clean(p * x));
    assert_eq!(hex_holonomy, a("1"));
    assert!((0..3).all(|i| clean(hex[i].clone() * hex[i+3].clone()) == a("1")));

    // The loaded multiset contains no inverse of any of its four independent
    // monodromies, so no relabelling can turn it into three inverse pairs.
    let inverse_pairs = loaded.iter().enumerate().flat_map(|(i, x)| {
        loaded.iter().enumerate().filter_map(move |(j, y)| {
            if i < j && clean(x.clone() * y.clone()) == a("1") { Some((i,j)) } else { None }
        })
    }).count();
    assert_eq!(inverse_pairs, 0);

    let packet = serde_json::json!({
        "schema": "marici.benincasa.string.loaded_monodromy_type_gate.v1",
        "entry": 1036,
        "source_entries": [967, 969, 979, 1025, 1034],
        "loaded_occurrence_monodromies": ["M1","M2","M2","M3","M4","M4"],
        "loaded_total_holonomy": "M1*M2^2*M3*M4^2",
        "loaded_total_holonomy_is_one": false,
        "loaded_inverse_pair_count": 0,
        "hexagon_facet_monodromies": ["B34","B24","X","B34^-1","B24^-1","X^-1"],
        "hexagon_total_holonomy": "1",
        "hexagon_inverse_pair_count": 3,
        "single_associahedron_regularization_typed": false,
        "classification": "the six loaded factors are occurrence-labelled tubular boundaries on four source walls, not the facet local system of one hexagon"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-loaded-monodromy-type-gate.json", &text).unwrap();
    print!("{text}");
}
