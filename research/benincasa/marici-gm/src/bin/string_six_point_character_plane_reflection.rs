use serde_json::{json, Value};
use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn shift(v: &[Atom], name: &str) -> Vec<Atom> {
    v.iter()
        .cloned()
        .map(|x| {
            clean(
                x.replace(a(name).to_pattern())
                    .with((-a(name)).to_pattern()),
            )
        })
        .collect()
}
fn project(v: &[Atom], ex: i32, ey: i32) -> Vec<Atom> {
    let x = shift(v, "B24");
    let y = shift(v, "B34");
    let xy = shift(&x, "B34");
    (0..v.len())
        .map(|i| {
            clean(
                v[i].clone()
                    + a(&ex.to_string()) * x[i].clone()
                    + a(&ey.to_string()) * y[i].clone()
                    + a(&(ex * ey).to_string()) * xy[i].clone(),
            )
        })
        .collect()
}
fn eval(v: &[Atom], m: &[Vec<Atom>]) -> Vec<Atom> {
    (0..m[0].len())
        .map(|j| clean((0..v.len()).fold(a("0"), |s, i| s + v[i].clone() * m[i][j].clone())))
        .collect()
}
fn tau_atom(mut x: Atom) -> Atom {
    for (from, to) in [
        ("A2", "TA2"),
        ("A3", "TA3"),
        ("B24", "TB24"),
        ("B34", "TB34"),
    ] {
        x = x.replace(a(from).to_pattern()).with(a(to).to_pattern());
    }
    for (from, to) in [
        ("TA2", "A3"),
        ("TA3", "A2"),
        ("TB24", "B34"),
        ("TB34", "B24"),
    ] {
        x = x.replace(a(from).to_pattern()).with(a(to).to_pattern());
    }
    clean(x)
}
fn reflection(v: &[Atom]) -> Vec<Atom> {
    let pi = [2usize, 3, 0, 1, 5, 4];
    let tv: Vec<_> = v.iter().cloned().map(tau_atom).collect();
    pi.iter().map(|&i| tv[i].clone()).collect()
}
fn coordinates(b0: &[Atom], b1: &[Atom], target: &[Atom]) -> (Atom, Atom, [usize; 2]) {
    for i in 0..b0.len() {
        for j in i + 1..b0.len() {
            let det = clean(b0[i].clone() * b1[j].clone() - b0[j].clone() * b1[i].clone());
            if det == a("0") {
                continue;
            }
            let alpha = clean(
                (target[i].clone() * b1[j].clone() - target[j].clone() * b1[i].clone())
                    / det.clone(),
            );
            let beta = clean(
                (b0[i].clone() * target[j].clone() - b0[j].clone() * target[i].clone()) / det,
            );
            assert!((0..b0.len()).all(|k| clean(
                target[k].clone() - alpha.clone() * b0[k].clone() - beta.clone() * b1[k].clone()
            ) == a("0")));
            return (alpha, beta, [i, j]);
        }
    }
    panic!("basis has rank less than two")
}

fn main() {
    let lp: Value = serde_json::from_str(
        &std::fs::read_to_string("../string-six-point-circuit-exceptional-cochain.json").unwrap(),
    )
    .unwrap();
    let cp: Value = serde_json::from_str(
        &std::fs::read_to_string("../string-six-point-loaded-corner-comparison.json").unwrap(),
    )
    .unwrap();
    let l: Vec<Atom> = lp["cochain"]
        .as_array()
        .unwrap()
        .iter()
        .map(|x| a(x.as_str().unwrap()))
        .collect();
    let c: Vec<Vec<Atom>> = cp["matrix"]
        .as_array()
        .unwrap()
        .iter()
        .map(|r| {
            r.as_array()
                .unwrap()
                .iter()
                .map(|x| a(x.as_str().unwrap()))
                .collect()
        })
        .collect();
    let occurrence = eval(&l, &c);
    let p = [4usize, 1, 0, 5, 3, 2];
    let mut loaded = vec![a("0"); 6];
    for i in 0..6 {
        loaded[p[i]] = occurrence[i].clone();
    }
    let normal = vec![
        a("-2*(-1+A2*B24)*(-1+A3*B34)*(1+A2*B24)*(1+A3*B34)/(A2*B24*A3*B34)"),
        a("-2*(-1+A3)*(-1+A2*B24)*(1+A3)*(1+A2*B24)/(A2*B24*A3)"),
        a("-2*(-1+A2*B24)*(-1+A3*B34)*(1+A2*B24)*(1+A3*B34)/(A2*B24*A3*B34)"),
        a("-2*(-1+A2)*(-1+A3*B34)*(1+A2)*(1+A3*B34)/(A2*A3*B34)"),
        a("-2*(-1+A2)*(-1+A3)*(1+A2)*(1+A3)/(A2*A3)"),
        a("-2*(-1+A2)*(-1+A3)*(1+A2)*(1+A3)/(A2*A3)"),
    ];
    assert_eq!(reflection(&normal), normal);

    let mut records = Vec::new();
    for (label, ex, ey) in [("++", 1, 1), ("--", -1, -1)] {
        let b0 = project(&loaded, ex, ey);
        let b1 = project(&normal, ex, ey);
        let r0 = reflection(&b0);
        let r1 = reflection(&b1);
        assert_eq!(reflection(&r0), b0);
        assert_eq!(reflection(&r1), b1);
        let (a00, a10, pivot0) = coordinates(&b0, &b1, &r0);
        let (a01, a11, pivot1) = coordinates(&b0, &b1, &r1);
        let diagonal = a10 == a("0") && a01 == a("0");
        records.push(json!({
            "character": label,
            "ordered_basis": ["loaded_occurrence_projector", "normal_symbol_projector"],
            "reflection_matrix_columns": [[a00.to_string(), a10.to_string()], [a01.to_string(), a11.to_string()]],
            "coordinate_pivots": [pivot0, pivot1],
            "directions_separated": diagonal,
            "involution_verified_on_basis": true
        }));
    }
    let separates = records.iter().all(|r| r["directions_separated"] == true);
    let packet = json!({
        "schema": "marici.benincasa.string_six_point_character_plane_reflection.v1",
        "reflection": {
            "label_action": "A2<->A3, B24<->B34",
            "dense_word_permutation": [2,3,0,1,5,4],
            "fixed_frame_action": "pi^{-1} tau",
            "normal_symbol_row_fixed": true
        },
        "rank_two_character_planes": records,
        "reflection_separates_loaded_and_normal_directions": separates,
        "classification": if separates {"the source reflection preserves the two candidate lines separately"} else {"the source reflection mixes at least one loaded/normal rank-two plane and therefore does not separate the modules into invariant lines"},
        "scope": "degree-zero semilinear reflection in the common dense six-word basis; no degree-changing map is introduced"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-character-plane-reflection.json", &text).unwrap();
    print!("{text}");
}
