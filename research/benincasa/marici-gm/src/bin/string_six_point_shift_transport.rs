use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn shift(row: &[Atom], name: &str) -> Vec<Atom> {
    row.iter()
        .cloned()
        .map(|x| {
            clean(
                x.replace(a(name).to_pattern())
                    .with((-a(name)).to_pattern()),
            )
        })
        .collect()
}
fn projective_minors(row: &[Atom], shifted: &[Atom]) -> Vec<Atom> {
    (1..row.len())
        .map(|j| clean(row[0].clone() * shifted[j].clone() - row[j].clone() * shifted[0].clone()))
        .collect()
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
    let names = ["A2", "A3", "B24", "B34"];
    let mut audits = Vec::new();
    for name in names {
        let shifted = shift(&r, name);
        let minors = projective_minors(&r, &shifted);
        let nonzero = minors.iter().filter(|x| **x != a("0")).count();
        audits.push(serde_json::json!({
            "shift": format!("{name}->-{name}"),
            "nonzero_projective_minors": nonzero,
            "preserves_source_line": nonzero == 0
        }));
    }
    let shifted_all = names.iter().fold(r.clone(), |row, name| shift(&row, name));
    let all_minors = projective_minors(&r, &shifted_all);
    let all_nonzero = all_minors.iter().filter(|x| **x != a("0")).count();

    // The two pair-coordinate shifts act diagonally on four disjoint supports.
    // These are the four characters of (Z/2)^2 and are all nonzero generically.
    let character_supports = [
        ("--", vec![0, 2]),
        ("-+", vec![1]),
        ("+-", vec![3]),
        ("++", vec![4, 5]),
    ];
    let covered: Vec<usize> = character_supports
        .iter()
        .flat_map(|(_, support)| support.iter().copied())
        .collect();
    assert_eq!(covered.len(), 6);
    assert!((0..6).all(|index| covered.contains(&index)));
    let source_shift_closure_rank = character_supports.len();
    let symbol_shift_closure_rank = 2 * source_shift_closure_rank;

    let packet = serde_json::json!({
        "schema": "marici.benincasa.string_six_point_shift_transport.v1",
        "coordinate_rule": "s_c->s_c+1 implies A_c->-A_c",
        "individual_shifts": audits,
        "simultaneous_four_shift": {
            "nonzero_projective_minors": all_nonzero,
            "preserves_source_line": all_nonzero == 0
        },
        "pivot_shift_character": -1,
        "pair_shift_character_supports": character_supports.iter().map(|(character, support)| {
            serde_json::json!({"character": character, "word_indices": support})
        }).collect::<Vec<_>>(),
        "source_shift_closure_rank": source_shift_closure_rank,
        "target_rank": 2,
        "symbol_shift_closure_rank": symbol_shift_closure_rank
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-shift-transport.json", &text).unwrap();
    print!("{text}");
}
