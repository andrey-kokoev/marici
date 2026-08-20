use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn a(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn main() {
    let k0 = a("K0");
    let k2 = a("K2");
    let k4 = a("K4");
    let z = a("z");
    let xi = a("xi");
    let disc = (k2.clone().pow(2)-a("4")*k0.clone()*k4.clone()).expand();
    let finite = (k4.clone()*z.clone().pow(2)+k2.clone()*z.clone()+k0.clone()).expand();
    let infinity = (k0.clone()*xi.clone().pow(2)+k2.clone()*xi.clone()+k4.clone()).expand();

    // Boundary restriction of the discriminant is a doubled Cartier section
    // in both projective charts.
    assert_eq!(disc.clone().replace(a("K0").to_pattern()).with(a("0").to_pattern()).expand(), k2.clone().pow(2));
    assert_eq!(disc.replace(a("K4").to_pattern()).with(a("0").to_pattern()).expand(), k2.clone().pow(2));
    assert_eq!(finite.replace(a("K0").to_pattern()).with(a("0").to_pattern()).expand(),
               (z.clone()*(k4.clone()*z+k2.clone())).expand());
    assert_eq!(infinity.replace(a("K4").to_pattern()).with(a("0").to_pattern()).expand(),
               (xi.clone()*(k0.clone()*xi+k2.clone())).expand());

    let packet = json!({
        "schema":"marici.benincasa.five_site_radial_collision_corners.v1",
        "engine":"Symbolica 2.2 exact characteristic-zero identities",
        "projective_radial_branch":"K4*z^2+K2*z*w+K0*w^2",
        "finite_endpoint":{
            "divisor":"K0=0",
            "chart":"w=1",
            "branch":"z*(K4*z+K2)",
            "collision_restriction":"D_rad|K0=K2^2",
            "scheme_intersection":"(K0,K2^2)",
            "cartier_length":2
        },
        "infinity_endpoint":{
            "divisor":"K4=0",
            "chart":"z=1, xi=w/z",
            "branch":"xi*(K0*xi+K2)",
            "collision_restriction":"D_rad|K4=K2^2",
            "scheme_intersection":"(K4,K2^2)",
            "cartier_length":2
        },
        "triple_endpoint_intersection":{
            "ideal":"(K0,K4,K2^2)",
            "reduced_support":"(K0,K4,K2)",
            "transverse_ring":"Q[K2]/(K2^2)",
            "cartier_length":2,
            "positive_koszul_homology":0
        },
        "classification":"nonreduced coefficient intersection on existing endpoint divisors",
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-radial-collision-corners.json",
              serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
