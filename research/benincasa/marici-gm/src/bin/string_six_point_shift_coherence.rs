use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn shift(x: Atom, name: &str) -> Atom {
    clean(
        x.replace(a(name).to_pattern())
            .with((-a(name)).to_pattern()),
    )
}

fn main() {
    let r = vec![
        a("-2*(-1+A2*B24)*(-1+A3*B34)*(1+A2*B24)*(1+A3*B34)/(A2*B24*A3*B34)"),
        a("-2*(-1+A3)*(-1+A2*B24)*(1+A3)*(1+A2*B24)/(A2*B24*A3)"),
        a("-2*(-1+A2*B24)*(-1+A3*B34)*(1+A2*B24)*(1+A3*B34)/(A2*B24*A3*B34)"),
        a("-2*(-1+A2)*(-1+A3*B34)*(1+A2)*(1+A3*B34)/(A2*A3*B34)"),
        a("-2*(-1+A2)*(-1+A3)*(1+A2)*(1+A3)/(A2*A3)"),
        a("-2*(-1+A2)*(-1+A3)*(1+A2)*(1+A3)/(A2*A3)"),
    ];
    for entry in r {
        assert_eq!(
            shift(shift(entry.clone(), "B24"), "B34"),
            shift(shift(entry, "B34"), "B24")
        );
    }

    // Label reflection tau=(24) acts before the maximal-flag specialization.
    let reflection = [
        ("A2", "A4"),
        ("A3", "A3"),
        ("A4", "A2"),
        ("B23", "B34"),
        ("B24", "B24"),
        ("B34", "B23"),
    ];
    let tangential = ["A2", "A3", "B24", "B34"];
    let image = ["A4", "A3", "B24", "B23"];
    let retained = image.iter().filter(|x| tangential.contains(x)).count();
    assert_eq!(retained, 2);

    let packet = serde_json::json!({
        "schema": "marici.benincasa.string_six_point_shift_coherence.v1",
        "pair_shift_commutator_zero": true,
        "pair_shift_group": "(Z/2)^2",
        "reflection": "(24)",
        "ambient_label_action": reflection.iter().map(|(x,y)| serde_json::json!([x,y])).collect::<Vec<_>>(),
        "current_tangential_slice": tangential,
        "reflected_slice": image,
        "retained_tangential_coordinates": retained,
        "reflection_internal_to_current_slice": false,
        "required_next_object": "unspecialized six-point shift atlas before maximal-flag specialization"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-shift-coherence.json", &text).unwrap();
    print!("{text}");
}
