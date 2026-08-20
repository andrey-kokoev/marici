use serde_json::{json, Value};
use std::{collections::{BTreeMap, BTreeSet}, fs};
use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn cut_support(label: &str) -> Vec<usize> {
    if label == "G" { return vec![]; }
    if let Some(edge) = label.strip_prefix("G_minus_e") {
        return vec![edge.chars().next().unwrap().to_digit(10).unwrap() as usize - 1];
    }
    let sites = label.strip_prefix("g_").unwrap().chars()
        .map(|c| c.to_digit(10).unwrap() as usize - 1)
        .collect::<BTreeSet<_>>();
    (0..5).filter(|edge| sites.contains(edge) != sites.contains(&((edge + 1) % 5))).collect()
}

fn main() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap(),
    ).unwrap();
    let cycle = &source["five_cycle"];
    let mut labels = BTreeSet::new();
    for label in cycle["common_prefactor"].as_array().unwrap() {
        labels.insert(label.as_str().unwrap().to_owned());
    }
    for term in cycle["terms"].as_array().unwrap() {
        for label in term.as_array().unwrap() {
            labels.insert(label.as_str().unwrap().to_owned());
        }
    }
    assert_eq!(labels.len(), 26);

    let x = atom("X"); let a = atom("a"); let b = atom("b");
    let one_cut_product = ((x.clone()+atom("2")*a.clone())*(x.clone()-atom("2")*a.clone())).expand();
    assert_eq!(one_cut_product, atom("X^2-4*a^2"));

    let mut two_cut_product = atom("1");
    for sa in [-1,1] { for sb in [-1,1] {
        two_cut_product *= x.clone()+atom(&sa.to_string())*a.clone()+atom(&sb.to_string())*b.clone();
    }}
    two_cut_product = two_cut_product.expand();
    let two_cut_expected = atom("X^4-2*(a^2+b^2)*X^2+(a^2-b^2)^2");
    assert_eq!(two_cut_product, two_cut_expected);
    let two_cut_base = atom("X^4-2*(R+S)*X^2+(R-S)^2");
    let roots = [a.clone()+b.clone(),a.clone()-b.clone(),-a.clone()+b.clone(),-a.clone()-b.clone()];
    let mut root_discriminant = atom("1");
    for i in 0..4 { for j in i+1..4 {
        root_discriminant *= (roots[i].clone()-roots[j].clone())*(roots[i].clone()-roots[j].clone());
    }}
    assert_eq!(root_discriminant.expand(),atom("4096*a^4*b^4*(a^2-b^2)^2"));
    let discriminant_factor = atom("4096*R^2*S^2*(R-S)^2").factor();

    let mut depth_counts = BTreeMap::<usize,usize>::new();
    let mut pair_counts = BTreeMap::<String,usize>::new();
    let mut records = Vec::new();
    for label in &labels {
        let support = cut_support(label);
        *depth_counts.entry(support.len()).or_default() += 1;
        if support.len() == 2 {
            let key = format!("F{}-F{}", support[0]+1, support[1]+1);
            *pair_counts.entry(key.clone()).or_default() += 1;
            records.push(json!({
                "label": label,
                "cut_edges": [support[0]+1,support[1]+1],
                "orbit_norm": two_cut_base.to_string(),
                "norm_discriminant": discriminant_factor.to_string(),
                "base_collision_factor": key
            }));
        }
    }
    assert_eq!(depth_counts.get(&0),Some(&1));
    assert_eq!(depth_counts.get(&1),Some(&5));
    assert_eq!(depth_counts.get(&2),Some(&20));
    assert_eq!(pair_counts.len(),10);
    assert!(pair_counts.values().all(|count| *count==2));

    let packet=json!({
        "schema":"marici.benincasa.five_site.marked_orbit_norms.v1",
        "engine":"Symbolica 2.2 exact characteristic-zero expansion",
        "marked_profile":{"zero_cut":1,"one_cut":5,"two_cut":20},
        "one_cut_norm":"X^2-4R",
        "one_cut_norm_discriminant":"16R",
        "two_cut_norm":two_cut_base.to_string(),
        "two_cut_norm_discriminant":discriminant_factor.to_string(),
        "physical_substitution":"R_i=F_i/det(H)",
        "residual_two_cut_collision":"R_i-R_j=0, equivalently F_i-F_j=0 away from det(H)=0",
        "edge_pair_multiplicities":pair_counts,
        "two_cut_records":records,
        "classification":{
            "norm_zero":"pushforward of an existing signed marked wall",
            "R_i_zero":"existing Kummer branch/edge-soft support",
            "R_i_minus_R_j_zero":"self-collision of labelled deck-orbit walls after projection; coefficient/relative-incidence support, not a singularity of the cover",
            "new_carrier_datum":false
        },
        "warning":"The norm discriminant belongs to the orbit-forgetting projection. It must not be promoted to a primitive wall on the occurrence-resolved cover."
    });
    fs::write("../results/five-site-marked-orbit-norms.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
