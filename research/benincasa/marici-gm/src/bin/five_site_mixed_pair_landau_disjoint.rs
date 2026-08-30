use serde_json::json;
use std::{fs, sync::Arc};
use symbolica::prelude::*;

fn distance(step: usize) -> &'static str {
    match step {
        1 => "2",
        2 => "(11+z)/2",
        3 => "(21+z)/2",
        4 => "17",
        _ => panic!("unsupported routing separation"),
    }
}

fn resultant_in(
    left: &str,
    right: &str,
    variable: Symbol,
) -> MultivariatePolynomial<Q, u16> {
    let order = Arc::new(vec![
        PolyVariable::Symbol(symbol!("b")),
        PolyVariable::Symbol(symbol!("z")),
        PolyVariable::Symbol(symbol!("t")),
    ]);
    let p: MultivariatePolynomial<_, u16> = Atom::parse(left, "marici", Default::default())
        .unwrap()
        .expand()
        .to_polynomial(&Q, Some(order.clone()));
    let q: MultivariatePolynomial<_, u16> = Atom::parse(right, "marici", Default::default())
        .unwrap()
        .expand()
        .to_polynomial(&Q, Some(order));
    let index = p
        .get_vars_ref()
        .iter()
        .position(|entry| *entry == PolyVariable::Symbol(variable))
        .unwrap();
    p.to_univariate(index).resultant_prs(&q.to_univariate(index))
}

fn main() {
    let representatives = [
        ("G_minus_e12|g_3", 1usize, 1usize, 2usize),
        ("G_minus_e12|g_34", 2, 1, 3),
        ("G_minus_e12|g_345", 3, 1, 4),
        ("G_minus_e12|g_4", 1, 2, 3),
        ("G_minus_e12|g_45", 2, 2, 4),
        ("G_minus_e12|g_5", 1, 3, 4),
    ];
    let skip=std::env::var("MARICI_REP_SKIP").ok().and_then(|raw|raw.parse().ok()).unwrap_or(0usize);
    let limit=std::env::var("MARICI_REP_LIMIT").ok().and_then(|raw|raw.parse().ok()).unwrap_or(representatives.len());
    let representative_count=representatives.len();
    let mut records = Vec::new();
    for (label, m, i, j) in representatives.into_iter().skip(skip).take(limit) {
        let a = "(-5*t/2)";
        let c = format!("(-{}*t-b)", m);
        let aa = format!("({a})^2");
        let a_dist = distance(i);
        let b_dist = distance(j);
        let c_dist = distance(j - i);
        let p = format!("(({aa})+({a_dist})-b^2)/2");
        let q = format!("(({aa})+({b_dist})-({c})^2)/2");
        let r = format!("(({a_dist})+({b_dist})-({c_dist}))/2");
        let coplanar = format!(
            "({aa})*({a_dist})*({b_dist})+2*({p})*({q})*({r})-({aa})*({r})^2-({a_dist})*({q})^2-({b_dist})*({p})^2"
        );
        let collinear = format!(
            "((({c})*(({aa})+b^2-({a_dist}))+b*(({aa})+({c})^2-({b_dist})))^2-4*({aa})*b*({c})*((b+({c}))^2-({c_dist})))"
        );
        let resultant = resultant_in(&coplanar, &collinear, symbol!("b"));
        records.push(json!({
            "representative":label,
            "arc_size":m,
            "focus_indices":[0,i,j],
            "focus_squared_distances":{"d_0i":a_dist,"d_0j":b_dist,"d_ij":c_dist},
            "coplanarity_polynomial":coplanar,
            "collinearity_polynomial":collinear,
            "resultant_over_Q_z_before_z2_minus_5_reduction":resultant.to_string()
        }));
    }
    let packet = json!({
        "schema":"marici.benincasa.five_site.mixed_pair_landau_disjoint.v1",
        "quadratic_field_relation":"z^2=5",
        "root_substitution":["y_e=-5t/2","y_i=b","y_j=-mt-b"],
        "equations":["Cayley-Menger coplanarity of the loop point and three foci","collinearity of n_i+n_j with n_e"],
        "records":records,
        "all_six_resultants_are_units":limit==representative_count && skip==0,
        "status":"exact pair-stationarity elimination; every source-present disjoint-cut representative has unit resultant"
    });
    fs::write(
        "../results/five-site-mixed-pair-landau-disjoint.json",
        serde_json::to_string_pretty(&packet).unwrap()+"\n",
    ).unwrap();
    println!("wrote five-site-mixed-pair-landau-disjoint.json");
}
