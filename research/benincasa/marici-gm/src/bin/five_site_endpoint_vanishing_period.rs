use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn a(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn main() {
    let t = a("t");
    let k2 = a("K2");
    let k4 = a("K4");
    let k0 = a("K0");

    // Finite endpoint: z=-K2*t/K4 and y=(K2/sqrt(K4))*eta,
    // eta^2=-t(1-t).  Verify the pulled-back branch equation.
    let z = -k2.clone()*t.clone()/k4.clone();
    let p_fin = (z.clone()*(k4.clone()*z+k2.clone())).together().cancel().expand();
    let expected_fin = (-k2.clone().pow(2)*t.clone()*(a("1")-t.clone())/k4.clone())
        .together().cancel().expand();
    assert_eq!(p_fin, expected_fin);

    // Infinity endpoint: xi=-K2*t/K0, with the exchanged equation.
    let xi = -k2.clone()*t.clone()/k0.clone();
    let p_inf = (xi.clone()*(k0.clone()*xi+k2.clone())).together().cancel().expand();
    let expected_inf = (-k2.clone().pow(2)*t.clone()*(a("1")-t)/k0.clone())
        .together().cancel().expand();
    assert_eq!(p_inf, expected_inf);

    let packet = json!({
        "schema":"marici.benincasa.five_site.endpoint_vanishing_period.v1",
        "finite_substitution":"z=-K2*t/K4",
        "finite_branch_pullback":"P=-(K2^2/K4)*t*(1-t)",
        "finite_form_pullback":"dz/sqrt(P)=-dt/(sqrt(K4)*sqrt(-t*(1-t)))",
        "finite_closed_cycle_period":"up to ordered orientation: 2*pi*i/sqrt(K4)",
        "infinity_substitution":"xi=-K2*t/K0",
        "infinity_branch_pullback":"P=-(K2^2/K0)*t*(1-t)",
        "infinity_form_pullback":"dxi/sqrt(P)=-dt/(sqrt(K0)*sqrt(-t*(1-t)))",
        "infinity_closed_cycle_period":"up to ordered orientation: 2*pi*i/sqrt(K0)",
        "K2_valuation_of_period":0,
        "local_gysin_rank":1,
        "physical_BD_chain_selected":false,
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-endpoint-vanishing-period.json",
              serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
