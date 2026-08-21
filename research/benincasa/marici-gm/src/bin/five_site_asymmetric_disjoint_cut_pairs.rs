use serde_json::{json, Value};
use std::{fs, sync::Arc};
use symbolica::prelude::*;

const P: [[i64; 3]; 5] = [
    [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 2, 3], [-2, -3, -4],
];

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn focus(edge: usize) -> [i64; 3] {
    let mut q = [0_i64; 3];
    if edge > 0 {
        for p in P.iter().take(edge) {
            for k in 0..3 { q[k] += p[k]; }
        }
    }
    q
}

fn dist(left: usize, right: usize) -> Atom {
    let a = focus(left);
    let b = focus(right);
    atom(&(0..3).map(|k| (a[k] - b[k]).pow(2)).sum::<i64>().to_string())
}

fn det3(h: &[[Atom; 3]; 3]) -> Atom {
    (&h[0][0] * (&h[1][1] * &h[2][2] - &h[1][2] * &h[2][1])
        - &h[0][1] * (&h[1][0] * &h[2][2] - &h[1][2] * &h[2][0])
        + &h[0][2] * (&h[1][0] * &h[2][1] - &h[1][1] * &h[2][0])).expand()
}

fn adj3(h: &[[Atom; 3]; 3]) -> [[Atom; 3]; 3] {
    [
        [(&h[1][1]*&h[2][2]-&h[1][2]*&h[2][1]).expand(), (&h[0][2]*&h[2][1]-&h[0][1]*&h[2][2]).expand(), (&h[0][1]*&h[1][2]-&h[0][2]*&h[1][1]).expand()],
        [(&h[1][2]*&h[2][0]-&h[1][0]*&h[2][2]).expand(), (&h[0][0]*&h[2][2]-&h[0][2]*&h[2][0]).expand(), (&h[0][2]*&h[1][0]-&h[0][0]*&h[1][2]).expand()],
        [(&h[1][0]*&h[2][1]-&h[1][1]*&h[2][0]).expand(), (&h[0][1]*&h[2][0]-&h[0][0]*&h[2][1]).expand(), (&h[0][0]*&h[1][1]-&h[0][1]*&h[1][0]).expand()],
    ]
}

fn resultant_var(
    mut left: MultivariatePolynomial<Q, u16>,
    mut right: MultivariatePolynomial<Q, u16>,
    variable: Symbol,
) -> MultivariatePolynomial<Q, u16> {
    left.unify_variables(&mut right);
    let index = left.get_vars_ref().iter()
        .position(|x| *x == PolyVariable::Symbol(variable)).unwrap();
    left.to_univariate(index).resultant_prs(&right.to_univariate(index))
}

fn run() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-asymmetric-compatible-pairs.json").unwrap()
    ).unwrap();
    let selected = source["records"].as_array().unwrap().iter()
        .filter(|record| record["first_gate_class"] == "disjoint_cut_proper_pair")
        .collect::<Vec<_>>();
    assert_eq!(selected.len(), 35);
    let order = Arc::new(vec![
        PolyVariable::Symbol(symbol!("b")),
        PolyVariable::Symbol(symbol!("c")),
        PolyVariable::Symbol(symbol!("t")),
    ]);
    let parse = |value: &Atom| -> MultivariatePolynomial<Q, u16> {
        value.to_polynomial(&Q, Some(order.clone()))
    };

    let mut records = Vec::new();
    let mut excluded = 0_usize;
    let mut unresolved = 0_usize;
    for record in selected {
        let labels = record["labels"].as_array().unwrap();
        let m = labels[0].as_str().unwrap().strip_prefix("g_").unwrap().len();
        let n = labels[1].as_str().unwrap().strip_prefix("g_").unwrap().len();
        let supports = record["cut_supports"].as_array().unwrap();
        let left = supports[0].as_array().unwrap().iter()
            .map(|x| x.as_u64().unwrap() as usize - 1).collect::<Vec<_>>();
        let right = supports[1].as_array().unwrap().iter()
            .map(|x| x.as_u64().unwrap() as usize - 1).collect::<Vec<_>>();
        let f = [left[0], left[1], right[0], right[1]];
        assert_eq!(f.iter().copied().collect::<std::collections::BTreeSet<_>>().len(), 4);
        let y = [atom("b"), atom(&format!("-{m}*t-b")), atom("c"), atom(&format!("-{n}*t-c"))];
        let h: [[Atom; 3]; 3] = std::array::from_fn(|i| std::array::from_fn(|j|
            ((dist(f[0], f[i+1]) + dist(f[0], f[j+1]) - dist(f[i+1], f[j+1])) / atom("2")).expand()
        ));
        let determinant = det3(&h);
        assert_ne!(determinant, atom("0"));
        let adj = adj3(&h);
        let p: [Atom; 3] = std::array::from_fn(|i|
            ((&y[0]*&y[0] + dist(f[0], f[i+1]) - &y[i+1]*&y[i+1]) / atom("2")).expand()
        );
        let xnum: [Atom; 3] = std::array::from_fn(|i|
            (0..3).fold(Atom::new(), |sum, j| sum + &adj[i][j] * &p[j]).expand()
        );
        let existence = (&determinant*&y[0]*&y[0]
            - (0..3).fold(Atom::new(), |sum, i| sum + &p[i]*&xnum[i])).expand();
        let u: [Atom; 3] = std::array::from_fn(|i|
            ((&y[0]+&y[1])*&xnum[i] - if i==0 {&determinant*&y[0]} else {Atom::new()}).expand()
        );
        let v: [Atom; 3] = std::array::from_fn(|i|
            ((&y[2]+&y[3])*&xnum[i] - if i==1 {&determinant*&y[3]} else if i==2 {&determinant*&y[2]} else {Atom::new()}).expand()
        );
        let minors = [
            (&u[0]*&v[1]-&u[1]*&v[0]).expand(),
            (&u[0]*&v[2]-&u[2]*&v[0]).expand(),
            (&u[1]*&v[2]-&u[2]*&v[1]).expand(),
        ];
        let first = minors.iter().map(|minor|
            resultant_var(parse(&existence), parse(minor), symbol!("b"))
        ).collect::<Vec<_>>();
        let second = [(0_usize,1_usize),(0,2),(1,2)].into_iter().map(|(i,j)|
            resultant_var(first[i].clone(), first[j].clone(), symbol!("c"))
        ).collect::<Vec<_>>();
        let certificate = second.iter().find(|candidate| candidate.to_string() == "1")
            .map(|_| "unit_staged_resultant");
        if certificate.is_some() { excluded += 1; } else { unresolved += 1; }
        records.push(json!({
            "labels": record["labels"],
            "arc_sizes": [m,n],
            "ordered_focus_edges_zero_based": f,
            "routing_gram_determinant": determinant.to_string(),
            "second_stage_resultants": second.iter().map(ToString::to_string).collect::<Vec<_>>(),
            "classification": certificate.unwrap_or("requires_stronger_elimination")
        }));
    }
    let packet = json!({
        "schema": "marici.benincasa.five_site.asymmetric_disjoint_cut_pairs.v1",
        "source_compatible_pairs": 35,
        "excluded_by_unit_staged_resultant": excluded,
        "requires_stronger_elimination": unresolved,
        "records": records,
        "scope": "Exact staged necessary-condition elimination; a unit second-stage resultant excludes a Landau solution."
    });
    fs::write(
        "../results/five-site-asymmetric-disjoint-cut-pairs.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    ).unwrap();
    println!("excluded={excluded} unresolved={unresolved}");
}

fn main() {
    std::thread::Builder::new().stack_size(256 * 1024 * 1024)
        .spawn(run).unwrap().join().unwrap();
}
