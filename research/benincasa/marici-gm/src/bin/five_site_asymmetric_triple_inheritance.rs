use serde_json::{json, Value};
use std::{collections::{BTreeMap, BTreeSet}, fs};

fn cut_support(label: &str) -> Vec<usize> {
    if label == "G" { return vec![]; }
    if let Some(edge) = label.strip_prefix("G_minus_e") {
        return vec![edge.chars().next().unwrap().to_digit(10).unwrap() as usize];
    }
    let sites = label.strip_prefix("g_").unwrap().chars()
        .map(|digit| digit.to_digit(10).unwrap() as usize)
        .collect::<BTreeSet<_>>();
    (1..=5).filter(|edge|
        sites.contains(edge) != sites.contains(&(edge % 5 + 1))
    ).collect()
}

fn pair_class(left: &str, right: &str) -> &'static str {
    if left == "G" || right == "G" { return "existing_total_support"; }
    let left_m = left.starts_with("G_minus_e");
    let right_m = right.starts_with("G_minus_e");
    assert!(!(left_m && right_m));
    let a = cut_support(left);
    let b = cut_support(right);
    let overlap = a.iter().filter(|edge| b.contains(edge)).count();
    if left_m || right_m {
        if overlap == 1 { "existing_one_wall_support" } else { "empty_pair_locus" }
    } else if overlap == 2 {
        "existing_total_support"
    } else {
        "empty_pair_locus"
    }
}

fn main() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()
    ).unwrap();
    let cycle = &source["five_cycle"];
    let common = cycle["common_prefactor"].as_array().unwrap().iter()
        .map(|entry| entry.as_str().unwrap().to_owned()).collect::<Vec<_>>();
    let mut multiplicity = BTreeMap::<Vec<String>, usize>::new();
    for term in cycle["terms"].as_array().unwrap() {
        let mut labels = common.clone();
        labels.extend(term.as_array().unwrap().iter()
            .map(|entry| entry.as_str().unwrap().to_owned()));
        for i in 0..labels.len() {
            for j in i+1..labels.len() {
                for k in j+1..labels.len() {
                    let mut triple = vec![labels[i].clone(), labels[j].clone(), labels[k].clone()];
                    triple.sort();
                    *multiplicity.entry(triple).or_default() += 1;
                }
            }
        }
    }
    assert_eq!(multiplicity.len(), 1210);
    let mut counts = BTreeMap::<String, usize>::new();
    let records = multiplicity.iter().map(|(triple, source_count)| {
        let classes = [(0_usize,1_usize),(0,2),(1,2)].into_iter().map(|(i,j)|
            json!({"labels":[triple[i],triple[j]],"class":pair_class(&triple[i],&triple[j])})
        ).collect::<Vec<_>>();
        let class = if classes.iter().any(|row| row["class"] == "empty_pair_locus") {
            "excluded_by_empty_pair"
        } else if classes.iter().any(|row| row["class"] == "existing_total_support") {
            "restricted_to_existing_total_support"
        } else {
            "requires_fresh_three_wall_elimination"
        };
        *counts.entry(class.to_owned()).or_default() += 1;
        json!({
            "labels": triple,
            "source_term_multiplicity": source_count,
            "pair_subobjects": classes,
            "classification": class
        })
    }).collect::<Vec<_>>();
    let unresolved = *counts.get("requires_fresh_three_wall_elimination").unwrap_or(&0);
    let packet = json!({
        "schema": "marici.benincasa.five_site.asymmetric_triple_inheritance.v1",
        "unique_source_compatible_triples": records.len(),
        "classification_counts": counts,
        "requires_fresh_elimination": unresolved,
        "records": records,
        "typing": "Every conclusion is inherited from a labelled pair subobject classified in Entries 1261, 1262, and 1266."
    });
    fs::write(
        "../results/five-site-asymmetric-triple-inheritance.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    ).unwrap();
    println!("triples=1210 unresolved={unresolved}");
}
