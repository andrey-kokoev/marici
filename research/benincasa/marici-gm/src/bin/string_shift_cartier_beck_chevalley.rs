use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn shift(x: Atom, name: &str) -> Atom {
    clean(x.replace(a(name).to_pattern()).with((-a(name)).to_pattern()))
}
fn specialize(x: Atom, name: &str, value: &str) -> Atom {
    clean(x.replace(a(name).to_pattern()).with(a(value).to_pattern()))
}

fn main() {
    let n = a("N");
    let i_plus = n.clone() - a("1");
    let i_minus = n.clone() + a("1");
    assert_eq!(shift(i_plus.clone(), "N"), -i_minus.clone());
    assert_eq!(shift(i_minus.clone(), "N"), -i_plus.clone());

    // A normal unit shift does not preserve the + Cartier ideal.
    assert_eq!(specialize(shift(i_plus.clone(), "N"), "N", "1"), a("-2"));
    // It does preserve the two-sheet union (N-1)(N+1).
    let union = clean(i_plus.clone() * i_minus.clone());
    assert_eq!(shift(union.clone(), "N"), union);

    // Tangential shifts commute strictly with specialization in a distinct
    // normal coordinate.
    let test = a("(1+C*N+C^2*N^2)/(C*N)");
    assert_eq!(
        specialize(shift(test.clone(), "C"), "N", "1"),
        shift(specialize(test, "N", "1"), "C")
    );

    let packet = serde_json::json!({
        "schema": "marici.benincasa.string_shift_cartier_beck_chevalley.v1",
        "normal_cartier_ideal_plus": "(N-1)",
        "normal_cartier_ideal_minus": "(N+1)",
        "unit_normal_shift": {
            "I_plus_image": "-I_minus",
            "I_minus_image": "-I_plus",
            "preserves_single_sheet": false,
            "preserves_two_sheet_union": true
        },
        "even_normal_shift_preserves_sheet": true,
        "tangential_shift_specialization_commutator_zero": true,
        "typed_structure": "two-sheet Cartier atlas with unit normal shifts exchanging sheets",
        "one_sheet_stabilizer": "arbitrary tangential shifts and even normal shifts"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-shift-cartier-beck-chevalley.json", &text).unwrap();
    print!("{text}");
}
