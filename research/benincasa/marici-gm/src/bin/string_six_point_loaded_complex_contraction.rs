use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn multiply(x: &[Vec<Atom>], y: &[Vec<Atom>]) -> Vec<Vec<Atom>> {
    (0..6)
        .map(|i| {
            (0..6)
                .map(|j| clean((0..6).map(|k| x[i][k].clone() * y[k][j].clone()).sum()))
                .collect()
        })
        .collect()
}
fn identity(m: &[Vec<Atom>]) -> bool {
    (0..6).all(|i| (0..6).all(|j| {
        let expected = if i == j { a("1") } else { a("0") };
        clean(m[i][j].clone() - expected) == a("0")
    }))
}

fn main() {
    let s = [
        [0, 0, 0, 0, -1, 0],
        [1, 0, 0, 0, 1, 0],
        [0, -1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
    ];
    let sinv = [
        [1, 1, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 0],
        [-1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
    ];
    let aa = |m: &[[i32; 6]; 6]| {
        m.iter()
            .map(|r| r.iter().map(|x| a(&x.to_string())).collect::<Vec<_>>())
            .collect::<Vec<_>>()
    };
    assert!(identity(&multiply(&aa(&s), &aa(&sinv))));
    assert!(identity(&multiply(&aa(&sinv), &aa(&s))));

    let q: Vec<Atom> = (1..=6).map(|i| a(&format!("q{i}"))).collect();
    let c: Vec<Vec<Atom>> = (0..6)
        .map(|i| (0..6).map(|j| a(&s[i][j].to_string()) * q[j].clone()).collect())
        .collect();
    let h: Vec<Vec<Atom>> = (0..6)
        .map(|i| (0..6).map(|j| clean(a(&sinv[i][j].to_string()) / q[i].clone())).collect())
        .collect();

    assert!(identity(&multiply(&c, &h)));
    assert!(identity(&multiply(&h, &c)));

    let packet = serde_json::json!({
        "schema": "marici.benincasa.string.loaded_complex_contraction.v1",
        "entry": 1033,
        "source_entries": [969, 1028, 1032],
        "differential": "C=S*diag(q_i)",
        "contracting_homotopy": "h=diag(q_i^-1)*S^-1",
        "C_h": "identity_degree_0",
        "h_C": "identity_degree_1",
        "pole_support": ["q1","q2","q3","q4","q5","q6"],
        "extra_pole_support": [],
        "internal_localized_cech_obstruction": false,
        "qualification": "uniqueness is internal to the frozen two-term loaded complex; a geometric higher-cell lift is additional data"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-loaded-complex-contraction.json", &text).unwrap();
    print!("{text}");
}
