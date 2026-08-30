use serde_json::{json, Value};
use std::fs;
use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default())
        .unwrap()
        .expand()
}
fn sub(e: Atom, v: &Atom, q: &Atom) -> Atom {
    e.replace(v.to_pattern()).with(q.to_pattern())
}

fn main() {
    let cover: Value = serde_json::from_str(
        &fs::read_to_string("../results/seven-site-multiloop-cover.json").unwrap(),
    )
    .unwrap();
    let real: Value = serde_json::from_str(
        &fs::read_to_string("../results/seven-site-multiloop-real-discovery.json").unwrap(),
    )
    .unwrap();
    let obstruction: Value = serde_json::from_str(
        &fs::read_to_string("../results/seven-site-multiloop-physical-obstruction.json").unwrap(),
    )
    .unwrap();
    assert_eq!(
        obstruction["conclusion"],
        json!("no positive-X_i real critical sheet on either root of C(k)")
    );
    let (f, g, h) = (
        a(cover["pulled_cover"]["F1"].as_str().unwrap()),
        a(cover["pulled_cover"]["F6"].as_str().unwrap()),
        a(cover["pulled_cover"]["F7"].as_str().unwrap()),
    );
    let k = a("k");
    let l0 = a("-2+4*x-3*B-3*D+E");
    let l1 = a("11*B-11*D+7*E");
    let (f0, g0, h0) = (
        sub(f.clone(), &k, &a("0")).factor(),
        sub(g.clone(), &k, &a("0")).factor(),
        sub(h.clone(), &k, &a("0")).factor(),
    );
    assert_eq!(
        f0.clone().expand(),
        (a("-3/16") * l0.clone() * l0.clone()).expand()
    );
    assert_eq!(g0.clone().expand(), (a("-3/8") * l0.clone()).expand());
    assert_eq!(h0.clone().expand(), (a("-3/8") * l0.clone()).expand());
    let second = a("-6/7");
    let (f1, g1, h1) = (
        sub(f, &k, &second).factor(),
        sub(g, &k, &second).factor(),
        sub(h, &k, &second).factor(),
    );
    assert_eq!(
        f1.clone().expand(),
        (a("-3/784") * l1.clone() * l1.clone()).expand()
    );
    assert_eq!(g1.clone().expand(), (a("-249/2744") * l1.clone()).expand());
    assert_eq!(h1.clone().expand(), (a("-831/2744") * l1.clone()).expand());
    let factors = [
        a("-2*s5"),
        a("-s6-p+v"),
        a("2*s2"),
        a("q+s2+u"),
        a("u-s2-q"),
        a("2*s4"),
        a("2*s6"),
        a("p+s6+v"),
    ];
    let product = factors.iter().fold(a("1"), |z, f| z * f.clone()).factor();
    assert_ne!(product, a("0"));
    let packet = json!({
        "schema":"marici.seven_site_multiloop_physical_specialization.v2",
        "source_reconstruction":{"X1":"-s6-p","X2":"s2","X3":"q","X4":"-s2-s4-q","X5":"s4-s5","X6":"s6-s5","X7":"p","common_factors":factors.iter().map(ToString::to_string).collect::<Vec<_>>(),"product":product.to_string()},
        "higher_codimension_center":{"k_equation":"2*k^2-3*k-1=0","Jacobian_rank":1,"left_multiplier_kernel":{"dimension":2,"basis":["e_F","e_G"]},"bounded_replication":real,"exact_real_sheet_obstruction":obstruction,"Bunch_Davies_activation":"absent on the positive-X_i chamber: neither real k branch admits the required positive squared energies; independently, the center is not a divisor and has no unique projective multiplier"},
        "Gram_fibers":{"k=0":{"F":f0.to_string(),"G":g0.to_string(),"H":h0.to_string(),"reduced_ideal":l0.to_string(),"free_variable":"w","Cartier_length":1,"source_visible_generically":true},"6+7k=0":{"F":f1.to_string(),"G":g1.to_string(),"H":h1.to_string(),"reduced_ideal":l1.to_string(),"free_variables":["x","w"],"Cartier_length":1,"source_visible_generically":true}},
        "classification":{"horizontal_physical_support":"absent as a divisor","vertical_coefficient_support":"two reduced Gram fibers of Cartier length one","inherited_lower_support":"soft loci are proper zeros of the displayed source factors","new_Carrier_structure":"absent"}
    });
    fs::write(
        "../results/seven-site-multiloop-physical-specialization.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"Gram_lengths":[1,1],"horizontal_divisor":false,"BD_activation":"absent on positive-X_i chamber","new_Carrier":false})
    );
}
