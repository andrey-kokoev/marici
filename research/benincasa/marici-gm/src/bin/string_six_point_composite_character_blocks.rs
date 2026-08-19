use serde_json::json;
use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn sine(x: Atom) -> Atom {
    x.clone() - a("1") / x
}
fn cosine_twice(x: Atom) -> Atom {
    x.clone() + a("1") / x
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn permutations() -> Vec<[usize; 3]> {
    vec![
        [2, 3, 4],
        [2, 4, 3],
        [3, 2, 4],
        [3, 4, 2],
        [4, 2, 3],
        [4, 3, 2],
    ]
}
fn pair(i: usize, j: usize) -> Atom {
    match (i.min(j), i.max(j)) {
        (2, 3) => a("X"),
        (2, 4) => a("B24"),
        (3, 4) => a("B34"),
        _ => panic!(),
    }
}
fn pivot(i: usize) -> Atom {
    match i {
        2 => a("A2"),
        3 => a("A3"),
        4 => a("A4"),
        _ => panic!(),
    }
}
fn dense_entry(alpha: [usize; 3], beta: [usize; 3]) -> Atom {
    let mut pos = [0usize; 5];
    for (i, j) in beta.iter().enumerate() {
        pos[*j] = i;
    }
    let mut result = a("1");
    for t in 0..3 {
        let i = alpha[t];
        let mut mon = pivot(i);
        for j in alpha.iter().skip(t + 1) {
            if pos[i] > pos[*j] {
                mon *= pair(i, *j);
            }
        }
        result *= sine(mon);
    }
    clean(result)
}
fn at(x: Atom, name: &str, value: &str) -> Atom {
    clean(x.replace(a(name).to_pattern()).with(a(value).to_pattern()))
}
fn main() {
    let x = a("X");
    let z = a("Z");
    let q = a("Q");
    let y = clean(q / (x.clone() * z.clone()));
    let sx = sine(x.clone());
    let sy = sine(y.clone());
    let sz = sine(z.clone());
    let cx = cosine_twice(x);
    let cy = cosine_twice(y);
    let cz = cosine_twice(z);
    let sparse = [
        [
            clean(a("2") / sx.clone()),
            clean(-(cx.clone() / sx.clone() + cz / sz)),
        ],
        [clean(-(cx / sx.clone() + cy / sy)), clean(a("2") / sx)],
    ];
    let basis = permutations();
    let right = [basis[4], basis[5]];
    let dense: Vec<Vec<Atom>> = right
        .iter()
        .map(|beta| {
            basis
                .iter()
                .map(|alpha| dense_entry(*alpha, *beta))
                .collect()
        })
        .collect();
    let mut transition = vec![vec![a("0"); 6]; 2];
    for i in 0..2 {
        for j in 0..6 {
            transition[i][j] = clean(
                sparse[i][0].clone() * dense[0][j].clone()
                    + sparse[i][1].clone() * dense[1][j].clone(),
            );
        }
    }
    let signed_grade = |sxv: i32| -> Vec<Atom> {
        transition
            .iter()
            .flatten()
            .cloned()
            .map(|entry| {
                let entry = at(at(entry, "X", &sxv.to_string()), "Q", "1");
                at(clean(entry / (a("A4") - a("1"))), "A4", "1")
            })
            .collect()
    };
    let plus = signed_grade(1);
    let minus = signed_grade(-1);
    let blocks = [
        (
            "chi_--",
            vec![0usize, 2],
            clean(plus[0].clone() * minus[2].clone() - plus[2].clone() * minus[0].clone()),
        ),
        ("chi_-+", vec![1usize], clean(plus[1].clone())),
        ("chi_+-", vec![3usize], clean(plus[3].clone())),
        (
            "chi_++",
            vec![4usize, 5],
            clean(plus[4].clone() * minus[5].clone() - plus[5].clone() * minus[4].clone()),
        ),
    ];
    let source_profiles = [
        ("(ZA2)^2-1", [0, 0, 0, 1]),
        ("(ZA2B24)^2-1", [1, 1, 0, 0]),
        ("(A3/Z)^2-1", [0, 0, 0, 1]),
        ("(A3B34/Z)^2-1", [1, 0, 1, 0]),
    ];
    let loaded_profiles = [
        ("(ZA2)^2-1", [1, 0, 0, 0]),
        ("(ZA2B24)^2-1", [1, 1, 0, 0]),
        ("(A3/Z)^2-1", [0, 0, 1, 0]),
        ("(A3B34/Z)^2-1", [0, 0, 0, 2]),
    ];
    let profile_comparison: Vec<_> = source_profiles
        .iter()
        .zip(&loaded_profiles)
        .map(|((factor, source), (_, loaded))| {
            json!({"factor":factor,"source":source,"naive_loaded":loaded,"match":source==loaded})
        })
        .collect();
    assert_eq!(
        profile_comparison
            .iter()
            .filter(|x| x["match"] == true)
            .count(),
        1
    );
    let packet = json!({
        "schema":"marici.benincasa.string_six_point_composite_character_blocks.v1",
        "six_word_basis":["123456","124356","132456","134256","142356","143256"],
        "blocks":blocks.iter().map(|(name,support,minor)|json!({"character":name,"support":support,"source_block_minor":minor.to_string()})).collect::<Vec<_>>(),
        "profile_comparison":profile_comparison,
        "matching_profile_count":1,
        "classification":"determinant agreement does not identify localized character subquotients; the naive occurrence-index-to-six-word-character assignment fails on three of four composite walls"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-composite-character-blocks.json", &text).unwrap();
    print!("{text}");
}
