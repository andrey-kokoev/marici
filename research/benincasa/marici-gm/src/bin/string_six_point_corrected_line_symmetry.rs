use serde_json::{json, Value};
use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn mul(x: &[Vec<Atom>], y: &[Vec<Atom>]) -> Vec<Vec<Atom>> {
    (0..2)
        .map(|i| {
            (0..2)
                .map(|j| clean((0..2).fold(a("0"), |s, k| s + x[i][k].clone() * y[k][j].clone())))
                .collect()
        })
        .collect()
}

fn main() {
    let prior: Value = serde_json::from_str(
        &std::fs::read_to_string("../string-six-point-character-plane-reflection.json").unwrap(),
    )
    .unwrap();
    let mut records = Vec::new();
    for rec in prior["rank_two_character_planes"].as_array().unwrap() {
        let label = rec["character"].as_str().unwrap();
        let cols = rec["reflection_matrix_columns"].as_array().unwrap();
        let r = vec![
            vec![
                a(cols[0][0].as_str().unwrap()),
                a(cols[1][0].as_str().unwrap()),
            ],
            vec![
                a(cols[0][1].as_str().unwrap()),
                a(cols[1][1].as_str().unwrap()),
            ],
        ];
        let sign = if label == "++" { 1 } else { -1 };
        let t = vec![
            vec![a(&sign.to_string()), a("0")],
            vec![a("0"), a(&sign.to_string())],
        ];
        let id = vec![vec![a("1"), a("0")], vec![a("0"), a("1")]];
        assert_eq!(mul(&r, &r), id);
        assert_eq!(mul(&r, &mul(&t, &r)), t);
        let c = r[1][0].clone();
        let eigen_plus = vec![a("0"), a("1")];
        let eigen_minus = vec![a("1"), clean(-c / a("2"))];
        let act = |m: &[Vec<Atom>], v: &[Atom]| -> Vec<Atom> {
            (0..2)
                .map(|i| clean(m[i][0].clone() * v[0].clone() + m[i][1].clone() * v[1].clone()))
                .collect()
        };
        assert_eq!(act(&r, &eigen_plus), eigen_plus);
        assert_eq!(
            act(&r, &eigen_minus),
            eigen_minus
                .iter()
                .cloned()
                .map(|x| clean(-x))
                .collect::<Vec<_>>()
        );
        for v in [&eigen_plus, &eigen_minus] {
            assert_eq!(
                act(&t, v),
                v.iter()
                    .cloned()
                    .map(|x| clean(a(&sign.to_string()) * x))
                    .collect::<Vec<_>>()
            );
        }
        records.push(json!({
            "character": label,
            "pair_shift_matrices": {"T24": [[sign,0],[0,sign]], "T34": [[sign,0],[0,sign]]},
            "reflection_eigenlines": {
                "+1": ["0", "1"],
                "-1": eigen_minus.iter().map(ToString::to_string).collect::<Vec<_>>()
            },
            "semidirect_relations_verified": true,
            "both_eigenlines_invariant": true
        }));
    }
    let packet = json!({
        "schema": "marici.benincasa.string_six_point_corrected_line_symmetry.v1",
        "local_group": "(Z/2)^2 semidirect <tau_off>",
        "planes": records,
        "classification": "the reflection eigensplitting is invariant under the complete frozen local occurrence symmetry in both repeated characters",
        "scope": "local maximal-flag chart only; cyclic descent across three occurrence charts is not asserted"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-corrected-line-symmetry.json", &text).unwrap();
    print!("{text}");
}
