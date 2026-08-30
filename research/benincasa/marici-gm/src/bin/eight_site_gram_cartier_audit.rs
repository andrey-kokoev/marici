use serde_json::{json, Value};
use std::{collections::BTreeMap, fs};
use symbolica::prelude::*;

fn a(source: &str) -> Atom {
    Atom::parse(source, "marici", Default::default()).unwrap().expand()
}

fn main() {
    let variables = (1..=8)
        .map(|index| Symbol::parse(format!("X{index}"), "marici").unwrap())
        .chain(["k", "l"].into_iter().map(|name| Symbol::parse(name, "marici").unwrap()))
        .chain((0..8).map(|index| Symbol::parse(format!("t{index}"), "marici").unwrap()))
        .collect::<Vec<_>>();
    let mut factor_cache = BTreeMap::<String, (bool, bool)>::new();
    let mut records = Vec::new();
    let mut counts = BTreeMap::<String, usize>::new();
    for rank in 4..=7 {
        let path = format!("../results/eight-site-rank{rank}-universal-jacobian.json");
        let packet: Value = serde_json::from_str(&fs::read_to_string(&path).unwrap()).unwrap();
        for item in packet["classes"].as_array().unwrap() {
            let mut fibers = Vec::new();
            for fiber in item["Gram_specializations"].as_array().unwrap() {
                let expression = fiber["ideal_gcd"].as_str().unwrap().to_string();
                let (nonconstant, squarefree) = *factor_cache.entry(expression.clone()).or_insert_with(|| {
                    let polynomial = a(&expression).to_polynomial::<_, u16>(&Q, variables.clone());
                    let nonconstant = !polynomial.is_constant();
                    let singular = (0..variables.len())
                        .map(|variable| polynomial.derivative(variable))
                        .filter(|derivative| !derivative.is_zero())
                        .fold(polynomial.clone(), |current, derivative| current.gcd(&derivative));
                    (nonconstant, singular.is_constant())
                });
                let generic_length = usize::from(nonconstant && squarefree);
                *counts.entry(format!("rank{rank}_generic_length_{generic_length}")).or_default() += 1;
                fibers.push(json!({
                    "k":fiber["k"],
                    "divisorial_hull_generator":expression,
                    "global_polynomial_principal":fiber["principal_ideal"],
                    "generic_cartier":nonconstant,
                    "reduced_generic_cartier":nonconstant && squarefree,
                    "cartier_length_at_generic_divisor_point":generic_length
                }));
            }
            records.push(json!({
                "canonical_key":item["canonical_key"],
                "wall_rank":rank,
                "fibers":fibers
            }));
        }
    }
    let packet = json!({
        "schema":"marici.eight_site_gram_cartier_audit.v1",
        "criterion":"For each specialized cover ideal, its polynomial gcd is the divisorial-hull generator. It is generically Cartier when nonconstant and has generic Cartier length one when squarefree; global polynomial principality is retained separately.",
        "Gram_boundaries":["k=0","k=-6/7"],
        "orbit_count":records.len(),
        "fiber_count":records.len()*2,
        "unique_divisorial_hull_generators":factor_cache.len(),
        "counts":counts,
        "orbits":records
    });
    fs::write(
        "../results/eight-site-gram-cartier-audit.json",
        serde_json::to_string_pretty(&packet).unwrap()+"\n"
    ).unwrap();
    println!("{}", json!({"orbits":packet["orbit_count"],"fibers":packet["fiber_count"],"unique_generators":packet["unique_divisorial_hull_generators"],"counts":packet["counts"]}));
}
