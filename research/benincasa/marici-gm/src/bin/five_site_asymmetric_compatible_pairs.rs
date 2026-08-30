use serde_json::{json, Value};
use std::{collections::{BTreeMap, BTreeSet}, fs};

fn pairs(labels: &[String]) -> Vec<Vec<String>> {
    let mut result = Vec::new();
    for i in 0..labels.len() {
        for j in i + 1..labels.len() {
            let mut pair = vec![labels[i].clone(), labels[j].clone()];
            pair.sort();
            result.push(pair);
        }
    }
    result
}

fn cut_support(label: &str) -> Vec<usize> {
    if label == "G" {
        return vec![];
    }
    if let Some(edge) = label.strip_prefix("G_minus_e") {
        return vec![edge.chars().next().unwrap().to_digit(10).unwrap() as usize];
    }
    let sites = label
        .strip_prefix("g_").unwrap()
        .chars().map(|digit| digit.to_digit(10).unwrap() as usize)
        .collect::<BTreeSet<_>>();
    (1..=5).filter(|edge| {
        sites.contains(edge) != sites.contains(&(edge % 5 + 1))
    }).collect()
}

fn kind(label: &str) -> String {
    if label == "G" {
        "total".to_owned()
    } else if label.starts_with("G_minus_e") {
        "one_cut_total".to_owned()
    } else {
        format!("proper_{}", label.strip_prefix("g_").unwrap().len())
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
        assert_eq!(labels.len(), 10);
        for pair in pairs(&labels) {
            *multiplicity.entry(pair).or_default() += 1;
        }
    }
    assert_eq!(multiplicity.len(), 245);

    let mut class_counts = BTreeMap::<String, usize>::new();
    let records = multiplicity.iter().map(|(pair, count)| {
        let cuts = pair.iter().map(|label| cut_support(label)).collect::<Vec<_>>();
        let contains_total = pair.iter().any(|label| label == "G");
        let both_proper = pair.iter().all(|label| label.starts_with("g_"));
        let same_cut = both_proper && cuts[0] == cuts[1];
        let class = if contains_total {
            "forced_total_energy"
        } else if same_cut {
            "same_cut_proper_pair"
        } else if pair.iter().any(|label| label.starts_with("G_minus_e")) {
            "contains_one_cut_total"
        } else {
            match cuts[0].iter().filter(|edge| cuts[1].contains(edge)).count() {
                0 => "disjoint_cut_proper_pair",
                1 => "shared_cut_proper_pair",
                2 => "same_cut_proper_pair",
                _ => unreachable!()
            }
        };
        *class_counts.entry(class.to_owned()).or_default() += 1;
        json!({
            "labels": pair,
            "kinds": pair.iter().map(|label| kind(label)).collect::<Vec<_>>(),
            "cut_supports": cuts,
            "source_term_multiplicity": count,
            "first_gate_class": class
        })
    }).collect::<Vec<_>>();

    let packet = json!({
        "schema": "marici.benincasa.five_site.asymmetric_compatible_pairs.v1",
        "source_terms": 180,
        "walls_per_term": 10,
        "unique_source_compatible_pairs": records.len(),
        "first_gate_counts": class_counts,
        "records": records,
        "typing": "Occurrence-labelled source compatibility only; no cyclic quotient and no Landau solution claim."
    });
    fs::write(
        "../results/five-site-asymmetric-compatible-pairs.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    ).unwrap();
    println!("wrote five-site-asymmetric-compatible-pairs.json");
}
