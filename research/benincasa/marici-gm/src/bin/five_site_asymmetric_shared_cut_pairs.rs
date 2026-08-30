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

fn arc_size(label: &str) -> usize {
    label.strip_prefix("g_").unwrap().len()
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
    let selected = source["records"].as_array().unwrap().iter()
        .filter(|record| record["first_gate_class"] == "shared_cut_proper_pair")
        .collect::<Vec<_>>();
    assert_eq!(selected.len(), 105);

    let mut records = Vec::new();
    let mut unit_count = 0_usize;
    let mut nonunit_count = 0_usize;
    for record in selected {
        let labels = record["labels"].as_array().unwrap();
        let left_label = labels[0].as_str().unwrap();
        let right_label = labels[1].as_str().unwrap();
        let m = arc_size(left_label);
        let n = arc_size(right_label);
        let supports = record["cut_supports"].as_array().unwrap();
        let s0 = supports[0].as_array().unwrap().iter()
            .map(|x| x.as_u64().unwrap() as usize - 1).collect::<Vec<_>>();
        let s1 = supports[1].as_array().unwrap().iter()
            .map(|x| x.as_u64().unwrap() as usize - 1).collect::<Vec<_>>();
        let shared = *s0.iter().find(|edge| s1.contains(edge)).unwrap();
        let i = *s0.iter().find(|edge| **edge != shared).unwrap();
        let j = *s1.iter().find(|edge| **edge != shared).unwrap();
        let di = distance_squared(shared, i);
        let dj = distance_squared(shared, j);
        let dij = distance_squared(i, j);
        assert!(di > 0 && dj > 0 && dij > 0);

        let c = format!("(-{m}*t-b)");
        let d = format!("(-{n}*t-b)");
        let p = format!("(b^2+{di}-({c})^2)/2");
        let q = format!("(b^2+{dj}-({d})^2)/2");
        let r = format!("({di}+{dj}-{dij})/2");
        let coplanar = format!(
            "b^2*{di}*{dj}+2*({p})*({q})*({r})-b^2*({r})^2-{di}*({q})^2-{dj}*({p})^2"
        );
        let numerator = format!(
            "2*b*({c})*({d})+({d})*(b^2+({c})^2-{di})+({c})*(b^2+({d})^2-{dj})+b*((({c})^2)+(({d})^2)-{dij})"
        );
        let collinear = format!(
            "({numerator})^2-4*({c})*({d})*((b+({c}))^2-{di})*((b+({d}))^2-{dj})"
        );
        let resultant = resultant_in_b(&coplanar, &collinear);
        let text = resultant.to_string();
        let is_unit = !text.contains('t');
        if is_unit { unit_count += 1; } else { nonunit_count += 1; }
        records.push(json!({
            "labels": record["labels"],
            "arc_sizes": [m, n],
            "focus_edges_zero_based": {"shared": shared, "left": i, "right": j},
            "focus_squared_distances": [di, dj, dij],
            "resultant_in_t": text,
            "resultant_is_nonzero_constant": is_unit
        }));
    }

    let packet = json!({
        "schema": "marici.benincasa.five_site.asymmetric_shared_cut_pairs.v1",
        "source_compatible_pairs": 105,
        "unit_resultants": unit_count,
        "nonunit_resultants": nonunit_count,
        "records": records,
        "typing": "Exact three-focus shared-cut stationarity elimination using Entry 1257 focus distances."
    });
    fs::write(
        "../results/five-site-asymmetric-shared-cut-pairs.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    ).unwrap();
    println!("unit={unit_count} nonunit={nonunit_count}");
}

fn main() {
    std::thread::Builder::new()
        .name("asymmetric-shared-cut-elimination".to_owned())
        .stack_size(128 * 1024 * 1024)
        .spawn(run).unwrap()
        .join().unwrap();
}
