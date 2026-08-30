use serde_json::{json, Value};
use std::{
    collections::{BTreeMap, BTreeSet},
    fs,
};

const N: usize = 7;

fn read(path: &str) -> Value {
    serde_json::from_str(&fs::read_to_string(path).unwrap()).unwrap()
}
fn parse_region(name: &str) -> Option<BTreeSet<usize>> {
    name.strip_prefix("g_").map(|d| {
        d.chars()
            .map(|c| c.to_digit(10).unwrap() as usize - 1)
            .collect()
    })
}
fn rotate_label(name: &str, shift: usize) -> String {
    if let Some(region) = parse_region(name) {
        return format!(
            "g_{}",
            region
                .iter()
                .map(|s| ((s + shift) % N + 1).to_string())
                .collect::<String>()
        );
    }
    let digits = name
        .strip_prefix("G_minus_e")
        .unwrap()
        .chars()
        .map(|c| c.to_digit(10).unwrap() as usize - 1)
        .collect::<Vec<_>>();
    format!(
        "G_minus_e{}{}",
        (digits[0] + shift) % N + 1,
        (digits[1] + shift) % N + 1
    )
}
fn sorting_sign(words: &[String]) -> i32 {
    let inversions = (0..words.len())
        .flat_map(|i| ((i + 1)..words.len()).map(move |j| (i, j)))
        .filter(|(i, j)| words[*i] > words[*j])
        .count();
    if inversions % 2 == 0 {
        1
    } else {
        -1
    }
}

fn main() {
    let partition = read("../results/seven-site-inventory-partition.json");
    let inventory = read("../results/seven-site-full-source-inventory.json");
    let positive = read("../results/seven-site-positive-base-gate.json");
    let rank4 = read("../results/seven-site-rank4-final-multiplier-audit.json");
    let rank5 = read("../results/seven-site-universal-jacobian-rank5-all-orbits.json");
    let rank6 = read("../results/seven-site-universal-jacobian-rank6-all-orbits.json");
    let universal_atlas = read("../results/seven-site-maximal-flag-atlas.json");
    assert_eq!(partition["orbit_count"], json!(2104));
    assert_eq!(rank4["classes"].as_array().unwrap().len(), 104);
    assert_eq!(rank5["classes"].as_array().unwrap().len(), 974);
    assert_eq!(rank6["classes"].as_array().unwrap().len(), 1026);
    assert_eq!(positive["blocked_by_wall_rank"]["4"], json!(104));
    assert_eq!(positive["positive_open_by_wall_rank"]["4"], json!(0));
    for item in rank4["classes"].as_array().unwrap() {
        assert!(!item["fully_saturated_common_gcd_is_constant"]
            .as_bool()
            .unwrap());
        assert!(item["source_normalized_projective_multiplier"].is_object());
        for fiber in item["Gram_specializations"].as_array().unwrap() {
            assert!(fiber["principal_ideal"].as_bool().unwrap());
            assert!(fiber["reduced_cartier"].as_bool().unwrap());
            assert_eq!(fiber["cartier_length"], json!(1));
        }
    }
    for item in rank5["classes"]
        .as_array()
        .unwrap()
        .iter()
        .chain(rank6["classes"].as_array().unwrap())
    {
        assert!(item["residual_common_gcd_is_constant"].as_bool().unwrap());
        assert!(!item["all_maximal_minors_zero"].as_bool().unwrap());
    }
    assert_eq!(
        universal_atlas["certification"],
        json!("49 exact labelled squared-distance pullback identities")
    );
    let inventory_index = inventory["all_orbits"]
        .as_array()
        .unwrap()
        .iter()
        .map(|item| (item["canonical_key"].as_str().unwrap(), item))
        .collect::<BTreeMap<_, _>>();
    let candidate_atlases=rank4["classes"].as_array().unwrap().iter().map(|item|{
        let labels=item["labels"].as_array().unwrap().iter().map(|v|v.as_str().unwrap().to_string()).collect::<Vec<_>>();
        let charts=(0..N).map(|shift|{let transported=labels.iter().map(|l|rotate_label(l,shift)).collect::<Vec<_>>();let sign=sorting_sign(&transported);let mut canonical=transported.clone();canonical.sort();json!({"shift":shift,"transported_order":transported,"canonical_order":canonical,"residue_wedge_sorting_sign":sign})}).collect::<Vec<_>>();
        let source=inventory_index[item["canonical_key"].as_str().unwrap()];
        json!({"canonical_key":item["canonical_key"],"stabilizer_order":source["stabilizer_order"],"orbit_size":source["orbit_size"],"source_representative":source["representative"],"charts":charts})
    }).collect::<Vec<_>>();
    let packet = json!({
        "schema":"marici.seven_site_inventory_exhaustion_certificate.v1",
        "frozen_inventory":{"orbits":2104,"classes":728},
        "classification":{
            "rank4":{"orbits":104,"classification":"genuine algebraic horizontal discriminant candidates after Gram/soft/lower saturation; physically empty by exact positive-base Gordan certificates","positive_physical":0},
            "rank5":{"orbits":974,"classification":"higher-codimension critical center only; no common codimension-one Jacobian factor"},
            "rank6":{"orbits":1026,"classification":"higher-codimension critical center (possibly empty); no common codimension-one Jacobian factor"}
        },
        "terminal_theorem":"no source-admitted seven-site orbit carries a horizontal physical divisor in the strictly positive X_i Bunch-Davies chamber",
        "candidate_obligations":{"labelled_atlases":candidate_atlases.len(),"Gram_soft_lower_saturation":104,"exact_projective_multipliers":104,"positive_X_and_BD_exclusions":104,"Gram_Cartier_fibers":208,"bad_Cartier_fibers":0},
        "universal_routing_atlas":{"charts":universal_atlas["charts"].as_array().unwrap().len(),"certification":universal_atlas["certification"]},
        "candidate_occurrence_atlases":candidate_atlases,
        "scope":"finite exhaustion theorem for the complete frozen seven-site source inventory; it does not assert an all-site or all-loop theorem"
    });
    fs::write(
        "../results/seven-site-inventory-exhaustion-certificate.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"orbits":2104,"rank4_candidates":104,"rank5_no_divisor":974,"rank6_no_divisor":1026,"physical_horizontal_divisors":0,"candidate_atlases":candidate_atlases.len()})
    );
}
