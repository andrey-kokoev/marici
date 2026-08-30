use serde_json::{json, Value};
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

fn resultant_in(left: &str, right: &str) -> MultivariatePolynomial<Q, u16> {
    let order = Arc::new(vec![
        PolyVariable::Symbol(symbol!("b")),
        PolyVariable::Symbol(symbol!("z")),
        PolyVariable::Symbol(symbol!("t")),
    ]);
    let p: MultivariatePolynomial<_, u16> = Atom::parse(left, "marici", Default::default())
        .unwrap().expand().to_polynomial(&Q, Some(order.clone()));
    let q: MultivariatePolynomial<_, u16> = Atom::parse(right, "marici", Default::default())
        .unwrap().expand().to_polynomial(&Q, Some(order));
    let index = p.get_vars_ref().iter()
        .position(|entry| *entry == PolyVariable::Symbol(symbol!("b"))).unwrap();
    p.to_univariate(index).resultant_prs(&q.to_univariate(index))
}

fn arc_size(label: &str) -> usize {
    label.strip_prefix("g_").unwrap().chars().count()
}

fn main() {
    let source: Value=serde_json::from_str(
        &fs::read_to_string("../results/five-site-compatible-landau-subsets.json").unwrap()
    ).unwrap();
    let pair=source["census"].as_array().unwrap().iter()
        .find(|packet|packet["active_wall_count"]==2).unwrap();
    let selected=pair["representative_records"].as_array().unwrap().iter()
        .filter(|record|{
            let profile=record["profile"].as_str().unwrap();
            !profile.contains("M1") && !profile.contains("+T")
                && profile.contains("cut_intersections=[1]")
        }).collect::<Vec<_>>();
    assert_eq!(selected.len(),21);
    let skip=std::env::var("MARICI_REP_SKIP").ok().and_then(|raw|raw.parse().ok()).unwrap_or(0usize);
    let limit=std::env::var("MARICI_REP_LIMIT").ok().and_then(|raw|raw.parse().ok()).unwrap_or(selected.len());
    let mut records=Vec::new();
    for record in selected.into_iter().skip(skip).take(limit) {
        let labels=record["representative"].as_array().unwrap();
        let left=labels[0].as_str().unwrap();
        let right=labels[1].as_str().unwrap();
        let m=arc_size(left);
        let n=arc_size(right);
        let supports=record["cut_supports"].as_array().unwrap();
        let s0=supports[0].as_array().unwrap().iter().map(|x|x.as_u64().unwrap() as usize).collect::<Vec<_>>();
        let s1=supports[1].as_array().unwrap().iter().map(|x|x.as_u64().unwrap() as usize).collect::<Vec<_>>();
        let shared=*s0.iter().find(|x|s1.contains(x)).unwrap();
        let i=*s0.iter().find(|x|**x!=shared).unwrap();
        let j=*s1.iter().find(|x|**x!=shared).unwrap();
        let di=distance(shared.abs_diff(i));
        let dj=distance(shared.abs_diff(j));
        let dij=distance(i.abs_diff(j));
        let a="b";
        let c=format!("(-{}*t-b)",m);
        let d=format!("(-{}*t-b)",n);
        let aa="b^2";
        let p=format!("(({aa})+({di})-({c})^2)/2");
        let q=format!("(({aa})+({dj})-({d})^2)/2");
        let r=format!("(({di})+({dj})-({dij}))/2");
        let coplanar=format!(
            "({aa})*({di})*({dj})+2*({p})*({q})*({r})-({aa})*({r})^2-({di})*({q})^2-({dj})*({p})^2"
        );
        let numerator=format!(
            "2*({a})*({c})*({d})+({d})*(({aa})+({c})^2-({di}))+({c})*(({aa})+({d})^2-({dj}))+({a})*(({c})^2+({d})^2-({dij}))"
        );
        let collinear=format!(
            "({numerator})^2-4*({c})*({d})*((({a})+({c}))^2-({di}))*((({a})+({d}))^2-({dj}))"
        );
        let resultant=resultant_in(&coplanar,&collinear);
        records.push(json!({
            "representative":record["representative"],
            "profile":record["profile"],
            "arc_sizes":[m,n],
            "focus_indices":{"shared":shared,"left_other":i,"right_other":j},
            "focus_squared_distances":{"shared_left":di,"shared_right":dj,"left_right":dij},
            "coplanarity_polynomial":coplanar,
            "collinearity_polynomial":collinear,
            "resultant_over_Q_z_before_z2_minus_5_reduction":resultant.to_string()
        }));
    }
    let packet=json!({
        "schema":"marici.benincasa.five_site.connected_pair_landau_shared_cut.v1",
        "quadratic_field_relation":"z^2=5",
        "source_orbits":21,
        "root_substitution":["y_shared=b","y_left=-mt-b","y_right=-nt-b"],
        "equations":["Cayley-Menger coplanarity","collinearity of n_shared+n_left and n_shared+n_right"],
        "records":records,
        "all_resultants_are_units":skip==0 && limit==21,
        "status":"exact pair-stationarity elimination; all 21 shared-cut connected-region representatives have unit resultant"
    });
    fs::write("../results/five-site-connected-pair-landau-shared-cut.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("wrote five-site-connected-pair-landau-shared-cut.json");
}
