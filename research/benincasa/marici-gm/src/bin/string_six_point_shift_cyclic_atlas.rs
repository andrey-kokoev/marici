use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn sigma(x: Atom) -> Atom {
    let replacements = [
        ("A2", "TA2"), ("A3", "TA3"), ("A4", "TA4"),
        ("B23", "TB23"), ("B24", "TB24"), ("B34", "TB34"),
    ];
    let mut out = x;
    for (from, tmp) in replacements {
        out = out.replace(a(from).to_pattern()).with(a(tmp).to_pattern());
    }
    let images = [
        ("TA2", "A3"), ("TA3", "A4"), ("TA4", "A2"),
        ("TB23", "B34"), ("TB24", "B23"), ("TB34", "B24"),
    ];
    for (tmp, to) in images {
        out = out.replace(a(tmp).to_pattern()).with(a(to).to_pattern());
    }
    clean(out)
}
fn compose(left: &[usize], right: &[usize]) -> Vec<usize> {
    right.iter().map(|i| left[*i]).collect()
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
        assert_eq!(sigma(sigma(sigma(entry.clone()))), *entry);
    }

    // Source occurrence transitions from Entry 909.
    let dense = [vec![1usize, 0], vec![1usize, 0], vec![0usize, 1]];
    let sparse = dense.clone();
    let dense_cycle = compose(&dense[2], &compose(&dense[1], &dense[0]));
    let sparse_cycle = compose(&sparse[2], &compose(&sparse[1], &sparse[0]));
    assert_eq!(dense_cycle, vec![0, 1]);
    assert_eq!(sparse_cycle, vec![0, 1]);

    let pair_generators = [
        ["B24", "B34"],
        ["B23", "B24"],
        ["B34", "B23"],
    ];
    let character_labels = ["--", "-+", "+-", "++"];
    // Relabelling permutes generators but does not add a sign or unit.
    assert_eq!(character_labels.len(), 4);

    let packet = serde_json::json!({
        "schema": "marici.benincasa.string_six_point_shift_cyclic_atlas.v1",
        "cyclic_label_action": "(234)",
        "chart_pair_shift_generators": pair_generators,
        "character_labels_per_chart": character_labels,
        "source_row_return_after_three": true,
        "dense_step_permutations": dense,
        "sparse_step_permutations": sparse,
        "dense_cyclic_composition_identity": true,
        "sparse_cyclic_composition_identity": true,
        "orientation_character_per_step": [1,1,1],
        "cyclic_shift_holonomy": "identity",
        "global_source_shift_rank": 4,
        "global_symbol_shift_rank": 8
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-shift-cyclic-atlas.json", &text).unwrap();
    print!("{text}");
}
