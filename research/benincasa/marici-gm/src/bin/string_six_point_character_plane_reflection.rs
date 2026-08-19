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
fn restrict(v: &[Atom], value: &str) -> Vec<Atom> {
    v.iter()
        .cloned()
        .map(|x| clean(x.replace(a("Z").to_pattern()).with(a(value).to_pattern())))
        .collect()
}
fn restrict_many(v: &[Atom], substitutions: &[(&str, String)]) -> Vec<Atom> {
    v.iter()
        .cloned()
        .map(|mut x| {
            for (name, value) in substitutions {
                x = x.replace(a(name).to_pattern()).with(a(value).to_pattern());
            }
            clean(x)
        })
        .collect()
}
fn projective_rank(x: &[Atom], y: &[Atom]) -> usize {
    if x.iter().all(|z| *z == a("0")) && y.iter().all(|z| *z == a("0")) {
        return 0;
    }
    for i in 0..x.len() {
        for j in i + 1..x.len() {
            if clean(x[i].clone() * y[j].clone() - x[j].clone() * y[i].clone()) != a("0") {
                return 2;
            }
        }
    }
    1
}
fn proportional_scalar(x: &[Atom], y: &[Atom]) -> Option<String> {
    let i = (0..x.len()).find(|i| x[*i] != a("0"))?;
    let q = clean(y[i].clone() / x[i].clone());
    if (0..x.len()).all(|j| clean(y[j].clone() - q.clone() * x[j].clone()) == a("0")) {
        Some(q.to_string())
    } else {
        None
    }
}
fn derivative_at(v: &[Atom], variable: &str, point: i32) -> Vec<Atom> {
    v.iter()
        .cloned()
        .map(|x| {
            let shifted = clean(
                x.clone()
                    .replace(a(variable).to_pattern())
                    .with((a(&point.to_string()) + a("H")).to_pattern()),
            );
            let base = clean(
                x.replace(a(variable).to_pattern())
                    .with(a(&point.to_string()).to_pattern()),
            );
            clean(
                ((shifted - base) / a("H"))
                    .replace(a("H").to_pattern())
                    .with(a("0").to_pattern()),
            )
        })
        .collect()
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
        let corrected = (0..6)
            .map(|i| {
                clean(
                    b0[i].clone()
                        - (a("1") + a("Z") * a("Z")) / (a("Z") * a("Z") - a("1")) * b1[i].clone(),
                )
            })
            .collect::<Vec<_>>();
        let walls = [
            ("ZA2", "1/A2"),
            ("ZA2", "-1/A2"),
            ("ZA2B24", "1/(A2*B24)"),
            ("ZA2B24", "-1/(A2*B24)"),
            ("A3/Z", "A3"),
            ("A3/Z", "-A3"),
            ("A3B34/Z", "A3*B34"),
            ("A3B34/Z", "-A3*B34"),
        ];
        let boundary = walls.iter().map(|(wall,value)| {
            let rank=projective_rank(&restrict(&b1,value),&restrict(&corrected,value));
            json!({"wall":wall,"root":value,"specialized_rank":rank,"splitting_survives":rank==2})
        }).collect::<Vec<_>>();
        assert!(boundary.iter().all(|x| x["splitting_survives"] == true));
        let mut pairwise = Vec::new();
        for s in [-1, 1] {
            for t in [-1, 1] {
                let specs = [
                    (
                        "ZA2 & ZA2B24",
                        vec![("Z", format!("{s}/A2")), ("B24", format!("{t}/{s}"))],
                    ),
                    (
                        "A3/Z & A3B34/Z",
                        vec![("Z", format!("{s}*A3")), ("B34", format!("{t}/{s}"))],
                    ),
                    (
                        "ZA2 & A3/Z",
                        vec![("Z", format!("{s}/A2")), ("A3", format!("{s}*{t}/A2"))],
                    ),
                    (
                        "ZA2 & A3B34/Z",
                        vec![
                            ("Z", format!("{s}/A2")),
                            ("B34", format!("{s}*{t}/(A2*A3)")),
                        ],
                    ),
                    (
                        "ZA2B24 & A3/Z",
                        vec![
                            ("Z", format!("{s}/(A2*B24)")),
                            ("A3", format!("{s}*{t}/(A2*B24)")),
                        ],
                    ),
                    (
                        "ZA2B24 & A3B34/Z",
                        vec![
                            ("Z", format!("{s}/(A2*B24)")),
                            ("B34", format!("{s}*{t}/(A2*A3*B24)")),
                        ],
                    ),
                ];
                for (intersection, substitutions) in specs {
                    let rank = projective_rank(
                        &restrict_many(&b1, &substitutions),
                        &restrict_many(&corrected, &substitutions),
                    );
                    let normal_r = restrict_many(&b1, &substitutions);
                    let corrected_r = restrict_many(&corrected, &substitutions);
                    let scalar = if rank == 1 {
                        proportional_scalar(&normal_r, &corrected_r)
                    } else {
                        None
                    };
                    pairwise.push(json!({"intersection":intersection,"signs":[s,t],"specialized_rank":rank,"splitting_survives":rank==2,"collapse_scalar_corrected_over_normal":scalar}));
                }
            }
        }
        let (parametrized, q) = if label == "++" {
            (
                restrict_many(&corrected, &[("Z", "U/A2".into()), ("A3", "U*V/A2".into())]),
                a("(1+A2^2)/(A2^2-1)"),
            )
        } else {
            (
                restrict_many(
                    &corrected,
                    &[
                        ("Z", "U/(A2*B24)".into()),
                        ("B34", "U*V/(A2*A3*B24)".into()),
                    ],
                ),
                a("(1+A2^2*B24^2)/(A2^2*B24^2-1)"),
            )
        };
        let normal_param = if label == "++" {
            restrict_many(&b1, &[("Z", "U/A2".into()), ("A3", "U*V/A2".into())])
        } else {
            restrict_many(
                &b1,
                &[
                    ("Z", "U/(A2*B24)".into()),
                    ("B34", "U*V/(A2*A3*B24)".into()),
                ],
            )
        };
        let kernel = (0..6)
            .map(|i| clean(parametrized[i].clone() - q.clone() * normal_param[i].clone()))
            .collect::<Vec<_>>();
        let mut conormal = Vec::new();
        for s in [-1, 1] {
            for t in [-1, 1] {
                let du = restrict_many(&derivative_at(&kernel, "U", s), &[("V", t.to_string())]);
                let dv = restrict_many(&derivative_at(&kernel, "V", t), &[("U", s.to_string())]);
                let rank = projective_rank(&du, &dv);
                conormal.push(json!({"signs":[s,t],"conormal_rank":rank}));
            }
        }
        records.push(json!({
            "character": label,
            "ordered_basis": ["loaded_occurrence_projector", "normal_symbol_projector"],
            "reflection_matrix_columns": [[a00.to_string(), a10.to_string()], [a01.to_string(), a11.to_string()]],
            "coordinate_pivots": [pivot0, pivot1],
            "directions_separated": diagonal,
            "involution_verified_on_basis": true,
            "generic_boundary_specializations": boundary,
            "generic_pairwise_intersections": pairwise,
            "recombination_kernel_conormal": conormal
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
