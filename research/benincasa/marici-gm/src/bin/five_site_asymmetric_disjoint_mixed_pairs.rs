use serde_json::{json, Value};
use std::{fs, sync::Arc};
use symbolica::prelude::*;

const P: [[i64; 3]; 5] = [
    [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 2, 3], [-2, -3, -4],
];

fn focus(edge: usize) -> [i64; 3] {
    let mut q = [0_i64; 3];
    if edge > 0 {
        for p in P.iter().take(edge) {
            for k in 0..3 { q[k] += p[k]; }
        }
    }
    q
}

fn distance_squared(left: usize, right: usize) -> i64 {
    let a = focus(left);
    let b = focus(right);
    (0..3).map(|k| (a[k] - b[k]).pow(2)).sum()
}

fn resultant_in_b(left: &str, right: &str) -> MultivariatePolynomial<Q, u16> {
    let order = Arc::new(vec![
        PolyVariable::Symbol(symbol!("b")),
        PolyVariable::Symbol(symbol!("t")),
    ]);
    let p: MultivariatePolynomial<_, u16> =
        Atom::parse(left, "marici", Default::default()).unwrap()
            .expand().to_polynomial(&Q, Some(order.clone()));
    let q: MultivariatePolynomial<_, u16> =
        Atom::parse(right, "marici", Default::default()).unwrap()
            .expand().to_polynomial(&Q, Some(order));
    let index = p.get_vars_ref().iter()
        .position(|entry| *entry == PolyVariable::Symbol(symbol!("b"))).unwrap();
    p.to_univariate(index).resultant_prs(&q.to_univariate(index))
}

fn run() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-asymmetric-compatible-pairs.json").unwrap()
    ).unwrap();
    let selected = source["records"].as_array().unwrap().iter().filter(|record| {
        if record["first_gate_class"] != "contains_one_cut_total" { return false; }
        let supports = record["cut_supports"].as_array().unwrap();
        let a = supports[0].as_array().unwrap();
        let b = supports[1].as_array().unwrap();
        !a.iter().any(|edge| b.contains(edge))
    }).collect::<Vec<_>>();
    assert_eq!(selected.len(), 30);

    let mut records = Vec::new();
    let mut unit_count = 0_usize;
    for record in selected {
        let labels = record["labels"].as_array().unwrap();
        let proper_label = labels.iter().map(|x| x.as_str().unwrap())
            .find(|label| label.starts_with("g_")).unwrap();
        let m = proper_label.strip_prefix("g_").unwrap().len();
        let supports = record["cut_supports"].as_array().unwrap();
        let one_cut_position = labels.iter().position(|label|
            label.as_str().unwrap().starts_with("G_minus_e")).unwrap();
        let proper_position = 1 - one_cut_position;
        let e = supports[one_cut_position].as_array().unwrap()[0].as_u64().unwrap() as usize - 1;
        let proper_cuts = supports[proper_position].as_array().unwrap().iter()
            .map(|x| x.as_u64().unwrap() as usize - 1).collect::<Vec<_>>();
        let i = proper_cuts[0];
        let j = proper_cuts[1];
        assert!(e != i && e != j && i != j);
        let di = distance_squared(e, i);
        let dj = distance_squared(e, j);
        let dij = distance_squared(i, j);

        let a = "(-5*t/2)";
        let c = format!("(-{m}*t-b)");
        let aa = format!("({a})^2");
        let p = format!("(({aa})+{di}-b^2)/2");
        let q = format!("(({aa})+{dj}-({c})^2)/2");
        let r = format!("({di}+{dj}-{dij})/2");
        let coplanar = format!(
            "({aa})*{di}*{dj}+2*({p})*({q})*({r})-({aa})*({r})^2-{di}*({q})^2-{dj}*({p})^2"
        );
        let collinear = format!(
            "((({c})*(({aa})+b^2-{di})+b*(({aa})+({c})^2-{dj}))^2-4*({aa})*b*({c})*((b+({c}))^2-{dij}))"
        );
        let resultant = resultant_in_b(&coplanar, &collinear);
        let text = resultant.to_string();
        assert_ne!(text, "0");
        let is_unit = text == "1";
        if is_unit { unit_count += 1; }
        records.push(json!({
            "labels": record["labels"],
            "region_size": m,
            "focus_edges_zero_based": [e,i,j],
            "focus_squared_distances": [di,dj,dij],
            "resultant_in_t": text,
            "resultant_is_one": is_unit
        }));
    }
    let packet = json!({
        "schema": "marici.benincasa.five_site.asymmetric_disjoint_mixed_pairs.v1",
        "source_compatible_pairs": 30,
        "unit_resultants": unit_count,
        "records": records,
        "root_substitution": ["y_e=-5t/2", "y_i=b", "y_j=-mt-b"],
        "equations": ["three-focus Cayley-Menger coplanarity", "collinearity of n_i+n_j with n_e"],
        "scope": "Exact pair-stationarity elimination for every disjoint-incidence one-cut-total plus proper pair."
    });
    fs::write(
        "../results/five-site-asymmetric-disjoint-mixed-pairs.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    ).unwrap();
    println!("unit={unit_count} nonunit={}", 30-unit_count);
}

fn main() {
    std::thread::Builder::new().stack_size(128 * 1024 * 1024)
        .spawn(run).unwrap().join().unwrap();
}
