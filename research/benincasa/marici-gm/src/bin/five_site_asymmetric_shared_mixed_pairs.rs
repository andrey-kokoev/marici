use serde_json::{json, Value};
use std::fs;

const P: [[i64; 3]; 5] = [
    [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 2, 3], [-2, -3, -4],
];

fn proper_data(label: &str) -> (usize, i64) {
    let sites = label.strip_prefix("g_").unwrap().chars()
        .map(|digit| digit.to_digit(10).unwrap() as usize - 1).collect::<Vec<_>>();
    let mut sum = [0_i64; 3];
    for site in &sites {
        for k in 0..3 { sum[k] += P[*site][k]; }
    }
    (sites.len(), sum.iter().map(|entry| entry * entry).sum())
}

fn main() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-asymmetric-compatible-pairs.json").unwrap()
    ).unwrap();
    let selected = source["records"].as_array().unwrap().iter().filter(|record| {
        if record["first_gate_class"] != "contains_one_cut_total" { return false; }
        let supports = record["cut_supports"].as_array().unwrap();
        let a = supports[0].as_array().unwrap();
        let b = supports[1].as_array().unwrap();
        a.iter().any(|edge| b.contains(edge))
    }).collect::<Vec<_>>();
    assert_eq!(selected.len(), 40);

    let records = selected.iter().map(|record| {
        let labels = record["labels"].as_array().unwrap();
        let proper = labels.iter().map(|x| x.as_str().unwrap())
            .find(|label| label.starts_with("g_")).unwrap();
        let one_cut = labels.iter().map(|x| x.as_str().unwrap())
            .find(|label| label.starts_with("G_minus_e")).unwrap();
        let (m, norm) = proper_data(proper);
        json!({
            "labels": record["labels"],
            "proper_wall": proper,
            "one_cut_wall": one_cut,
            "region_size": m,
            "P_A_squared": norm,
            "root_assignment": ["y_shared=-5t/2", format!("y_other=(5-2*{})t/2",m)],
            "parallel_branch": format!("{}*t^2-{}", (5-m)*(5-m), norm),
            "antiparallel_branch": format!("{}*t^2-{}", m*m, norm),
            "classification": "one-wall thresholds of A-complement and A"
        })
    }).collect::<Vec<_>>();

    let packet = json!({
        "schema": "marici.benincasa.five_site.asymmetric_shared_mixed_pairs.v1",
        "source_compatible_pairs": 40,
        "records": records,
        "new_threshold_factor": false,
        "scope": "One-cut-total plus proper-region pairs sharing the labelled cut occurrence."
    });
    fs::write(
        "../results/five-site-asymmetric-shared-mixed-pairs.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    ).unwrap();
    println!("shared_mixed=40 new_threshold_factor=false");
}
