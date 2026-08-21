use serde_json::{json, Value};
use std::{collections::BTreeSet, fs, sync::Arc};
use symbolica::prelude::*;

fn sym(name: &str) -> Symbol {
    Symbol::parse(name, "marici").unwrap()
}

fn cut_support(label: &str) -> Vec<usize> {
    let sites = label.strip_prefix("g_").unwrap().chars()
        .map(|digit| digit.to_digit(10).unwrap() as usize - 1)
        .collect::<BTreeSet<_>>();
    (0..5).filter(|edge|
        sites.contains(edge) != sites.contains(&((edge + 1) % 5))
    ).collect()
}

fn denominator(label: &str) -> String {
    if label == "G" { return "5*t".to_owned(); }
    if let Some(edge) = label.strip_prefix("G_minus_e") {
        let index = edge.chars().next().unwrap().to_digit(10).unwrap() as usize - 1;
        return format!("5*t+2*y{}", index + 1);
    }
    let size = label.strip_prefix("g_").unwrap().len();
    let cuts = cut_support(label);
    assert_eq!(cuts.len(), 2);
    format!("{size}*t+y{}+y{}", cuts[0] + 1, cuts[1] + 1)
}

fn degree_range(polynomial: &MultivariatePolynomial<Q, u16>) -> (usize, usize) {
    let degrees = (0..polynomial.nterms()).map(|term|
        polynomial.exponents(term).iter().map(|entry| *entry as usize).sum::<usize>()
    ).collect::<Vec<_>>();
    (
        degrees.iter().min().copied().unwrap_or(0),
        degrees.iter().max().copied().unwrap_or(0),
    )
}

fn run() {
    let canonical: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-asymmetric-canonical-sum.json").unwrap()
    ).unwrap();
    let characters: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-asymmetric-kummer-character-reduction-homogeneous.json").unwrap()
    ).unwrap();
    let current: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-d3-physical-current.json").unwrap()
    ).unwrap();

    assert_eq!(canonical["combined_numerator_total_degree"], 16);
    assert_eq!(canonical["full_denominator_degree"], 26);
    assert_eq!(characters["all_homogeneous_degree_rules_pass"], true);
    assert_eq!(current["source_measure"], "d^3 ell on physical loop momentum space");

    let order = Arc::new(vec![
        PolyVariable::Symbol(sym("t")),
        PolyVariable::Symbol(sym("y1")),
        PolyVariable::Symbol(sym("y2")),
        PolyVariable::Symbol(sym("y3")),
        PolyVariable::Symbol(sym("y4")),
        PolyVariable::Symbol(sym("y5")),
        PolyVariable::Symbol(sym("u1")),
        PolyVariable::Symbol(sym("u2")),
        PolyVariable::Symbol(sym("u3")),
        PolyVariable::Symbol(sym("rho")),
    ]);
    let polynomial = |text: &str| -> MultivariatePolynomial<Q, u16> {
        Atom::parse(text, "marici", Default::default()).unwrap()
            .expand().to_polynomial(&Q, Some(order.clone()))
    };

    let f = [
        "2*u1^2+2*u2^2+u3^2-2*u1*u2-2*u2*u3".to_owned(),
        "2*u1^2+2*u2^2+u3^2-2*u1*u2-2*u2*u3-2*rho*u1+rho^2".to_owned(),
        "2*u1^2+2*u2^2+u3^2-2*u1*u2-2*u2*u3-2*rho*u2+2*rho^2".to_owned(),
        "2*u1^2+2*u2^2+u3^2-2*u1*u2-2*u2*u3-2*rho*u3+3*rho^2".to_owned(),
        "2*u1^2+2*u2^2+u3^2-2*u1*u2-2*u2*u3+2*rho*u1+2*rho*u2-8*rho*u3+29*rho^2".to_owned(),
    ];
    let relation_rows = (0..5).map(|edge| {
        let relation = polynomial(&format!("y{}^2-({})", edge + 1, f[edge]));
        let range = degree_range(&relation);
        json!({
            "edge": edge + 1,
            "relation": format!("y{}^2=F{}", edge + 1, edge + 1),
            "minimum_degree": range.0,
            "maximum_degree": range.1,
            "homogeneous_degree_two": range == (2, 2)
        })
    }).collect::<Vec<_>>();

    let labels = canonical["denominator_labels"].as_array().unwrap();
    assert_eq!(labels.len(), 26);
    let wall_rows = labels.iter().map(|entry| {
        let label = entry.as_str().unwrap();
        let equation = denominator(label);
        let range = degree_range(&polynomial(&equation));
        json!({
            "label": label,
            "equation": equation,
            "minimum_degree": range.0,
            "maximum_degree": range.1,
            "homogeneous_degree_one": range == (1, 1)
        })
    }).collect::<Vec<_>>();

    let relations_pass = relation_rows.iter().all(|row| row["homogeneous_degree_two"] == true);
    let walls_pass = wall_rows.iter().all(|row| row["homogeneous_degree_one"] == true);
    assert!(relations_pass && walls_pass);

    let packet = json!({
        "schema": "marici.benincasa.five_site.asymmetric_graded_localization.v1",
        "grading": "deg(t)=deg(y_i)=deg(u_i)=deg(rho)=1; deg(dz)=deg(z)",
        "kummer_relations": relation_rows,
        "all_kummer_relations_homogeneous_degree_two": relations_pass,
        "walls": wall_rows,
        "all_26_walls_homogeneous_degree_one": walls_pass,
        "numerator_degree": 16,
        "denominator_degree": 26,
        "canonical_rational_degree": -10,
        "de_rham_differential_degree": 0,
        "physical_current_scaling_degree": 3,
        "physical_period_scaling_degree": -7,
        "physical_scaling_identity": "Pi(lambda*t,lambda*P)=lambda^(-7) Pi(t,P)",
        "physical_euler_equation": "(t*d_t+rho*d_rho+7)Pi=0",
        "projective_reduction": "Pi(t,rho)=rho^(-7) Pi(t/rho,1)",
        "momentum_reversal": "Pi(t,-rho)=Pi(t,rho), induced by (ell,P)->(-ell,-P)",
        "projective_parity": "Pi(-z)=-Pi(z)",
        "infinity_series_coordinate": "x=1/z^2 with z^7 Pi(z) regular/formal in x when an asymptotic expansion exists",
        "character_rule": "deg(C_S)+|S|=16",
        "conclusion": "The homogenized Kummer quotient, 26-wall localization, and algebraic de Rham differential form a graded complex.",
        "scope": "Algebraic localized de Rham complex before physical cycle selection or Gauss-Manin quotient."
    });
    fs::write(
        "../results/five-site-asymmetric-graded-localization.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    ).unwrap();
    println!("relations=5 walls=26 rational_degree=-10");
}

fn main() {
    std::thread::Builder::new().stack_size(128 * 1024 * 1024)
        .spawn(run).unwrap().join().unwrap();
}
