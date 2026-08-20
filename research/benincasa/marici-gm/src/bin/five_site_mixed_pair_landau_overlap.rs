use serde_json::{json, Value};
use std::fs;

fn main() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-compatible-landau-subsets.json").unwrap(),
    )
    .unwrap();
    let pair = source["census"]
        .as_array()
        .unwrap()
        .iter()
        .find(|packet| packet["active_wall_count"] == 2)
        .unwrap();
    let records = pair["representative_records"].as_array().unwrap();
    let shared_cut = records
        .iter()
        .filter(|record| {
            let profile = record["profile"].as_str().unwrap();
            profile.contains("M1") && profile.contains("cut_intersections=[1]")
        })
        .collect::<Vec<_>>();
    let disjoint_cut = records
        .iter()
        .filter(|record| {
            let profile = record["profile"].as_str().unwrap();
            profile.contains("M1") && profile.contains("cut_intersections=[0]")
                && !profile.contains("+T")
        })
        .count();

    assert_eq!(shared_cut.len(), 8);
    assert_eq!(disjoint_cut, 6);

    let thresholds = (1..=4)
        .map(|m| {
            json!({
                "arc_size":m,
                "same_direction_condition":format!("|P_A|^2-{}t^2",(5-m)*(5-m)),
                "opposite_direction_condition":format!("|P_A|^2-{}t^2",m*m),
                "classification":"the one-wall thresholds of the complementary regions A^c and A"
            })
        })
        .collect::<Vec<_>>();

    let packet = json!({
        "schema":"marici.benincasa.five_site.mixed_pair_landau_overlap.v1",
        "source_packet":"five-site-compatible-landau-subsets.json",
        "shared_cut_free_C5_orbits":shared_cut.len(),
        "shared_cut_labelled_pairs":5*shared_cut.len(),
        "disjoint_cut_free_C5_orbits_remaining":disjoint_cut,
        "wall_equations":["5t+2y_i=0","mt+y_i+y_j=0"],
        "root_values":["y_i=-5t/2","y_j=(5-2m)t/2"],
        "stationarity":"the two signed unit root directions are parallel or antiparallel",
        "thresholds":thresholds,
        "new_nonzero_t_factor":false,
        "scope":"shared-cut M1+A_m pairs only; no claim for disjoint-cut three-focus pairs"
    });
    fs::write(
        "../results/five-site-mixed-pair-landau-overlap.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("wrote five-site-mixed-pair-landau-overlap.json");
}
