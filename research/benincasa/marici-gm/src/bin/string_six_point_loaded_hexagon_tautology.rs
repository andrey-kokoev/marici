use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn mul(x: &[Vec<Atom>], y: &[Vec<Atom>]) -> Vec<Vec<Atom>> {
    let inner = y.len();
    let cols = y[0].len();
    (0..x.len())
        .map(|i| {
            (0..cols)
                .map(|j| clean((0..inner).map(|k| x[i][k].clone() * y[k][j].clone()).sum()))
                .collect()
        })
        .collect()
}
fn zero(m: &[Vec<Atom>]) -> bool {
    m.iter().flatten().all(|x| clean(x.clone()) == a("0"))
}
fn equal(x: &[Vec<Atom>], y: &[Vec<Atom>]) -> bool {
    x.iter().zip(y).all(|(xr, yr)| xr.iter().zip(yr).all(|(u, v)| clean(u.clone()-v.clone())==a("0")))
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
    let q: Vec<Atom> = (1..=6).map(|i| a(&format!("q{i}"))).collect();
    let c: Vec<Vec<Atom>> = (0..6)
        .map(|i| (0..6).map(|j| a(&s[i][j].to_string()) * q[j].clone()).collect())
        .collect();
    let h: Vec<Vec<Atom>> = (0..6)
        .map(|i| (0..6).map(|j| clean(a(&sinv[i][j].to_string()) / q[i].clone())).collect())
        .collect();

    // Ordinary oriented hexagon boundary: edge j runs from vertex j to j+1.
    let mut d1 = vec![vec![a("0"); 6]; 6];
    for j in 0..6 {
        d1[j][j] = a("-1");
        d1[(j + 1) % 6][j] = a("1");
    }
    let d2 = vec![vec![a("1")]; 6];
    assert!(zero(&mul(&d1, &d2)));

    // Keep the vertex comparison arbitrary to expose the fitted family.
    let j0: Vec<Vec<Atom>> = (0..6)
        .map(|i| (0..6).map(|j| if i == j { a(&format!("x{}", i+1)) } else { a("0") }).collect())
        .collect();
    let j1 = mul(&mul(&h, &j0), &d1);
    assert!(equal(&mul(&c, &j1), &mul(&j0, &d1)));
    assert!(zero(&mul(&j1, &d2)));

    let packet = serde_json::json!({
        "schema": "marici.benincasa.string.loaded_hexagon_tautology.v1",
        "entry": 1034,
        "source_entries": [1024, 1027, 1033],
        "hexagon_chain_identity": "d1*d2=0",
        "arbitrary_vertex_map": "J0=diag(x1,...,x6)",
        "fitted_edge_map": "J1=h*J0*d1",
        "degree_one_chain_identity": "C*J1=J0*d1",
        "two_cell_identity": "J1*d2=0",
        "two_cell_obstruction_after_localization": false,
        "source_derived_comparison_constructed": false,
        "classification": "the localized extension exists tautologically for every J0 and therefore is not evidence for a geometric regularization map"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-loaded-hexagon-tautology.json", &text).unwrap();
    print!("{text}");
}
