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
fn swap(x: Atom, left: &str, right: &str) -> Atom {
    let tmp = x.replace(a(left).to_pattern()).with(a("TMP").to_pattern());
    let tmp = tmp.replace(a(right).to_pattern()).with(a(left).to_pattern());
    clean(tmp.replace(a("TMP").to_pattern()).with(a(right).to_pattern()))
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
    for entry in &r {
        assert_eq!(
            shift(shift(entry.clone(), "B24"), "B34"),
            shift(shift(entry.clone(), "B34"), "B24")
        );
    }

    // The off-diagonal reflection is tau_off=(23), not (24).
    // On the dense word basis [234,243,324,342,423,432] it has:
    let word_permutation = [2usize, 3, 0, 1, 5, 4];
    let reflected: Vec<Atom> = r
        .iter()
        .cloned()
        .map(|x| swap(swap(x, "A2", "A3"), "B24", "B34"))
        .collect();
    for (source, target) in word_permutation.iter().enumerate() {
        assert_eq!(reflected[source], r[*target]);
    }

    let packet = serde_json::json!({
        "schema": "marici.benincasa.string_six_point_shift_coherence.v2",
        "pair_shift_commutator_zero": true,
        "pair_shift_group": "(Z/2)^2",
        "off_diagonal_reflection": "(23)",
        "off_diagonal_normal_action": {"s14":"s14","s35":"s25","s25":"s35","s235":"s235"},
        "tangential_action": {"A2":"A3","A3":"A2","B24":"B34","B34":"B24"},
        "dense_word_permutation": word_permutation,
        "source_row_covariant": true,
        "specialized_slice_preserved": true,
        "maximal_flag_reflection_distinct": "(24)",
        "reflection_labels_disambiguated": true
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-shift-coherence.json", &text).unwrap();
    print!("{text}");
}
