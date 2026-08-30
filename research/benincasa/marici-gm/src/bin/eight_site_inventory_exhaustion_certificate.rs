use serde_json::{json, Value};
use std::{
    collections::{BTreeMap, BTreeSet},
    fs,
};

const N: usize = 8;

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
    let partition = read("../results/eight-site-inventory-partition.json");
    let inventory = read("../results/eight-site-full-source-inventory.json");
    let replication = read("../results/eight-site-full-source-inventory-p1000033.json");
    let positive = read("../results/eight-site-positive-base-gate-compact.json");
    let rank4 = read("../results/eight-site-rank4-universal-jacobian.json");
    let rank5 = read("../results/eight-site-rank5-universal-jacobian-compact.json");
    let rank6 = read("../results/eight-site-rank6-universal-jacobian-compact.json");
    let rank7 = read("../results/eight-site-rank7-universal-jacobian-compact.json");
    let cartier = read("../results/eight-site-gram-cartier-audit-compact.json");
    assert_eq!(partition["orbit_count"], json!(21652));
    assert_eq!(partition["class_count"], json!(7855));
    assert_eq!(rank4["classes"].as_array().unwrap().len(), 36);
    assert_eq!(rank5["classes"].as_array().unwrap().len(), 2101);
    assert_eq!(rank6["classes"].as_array().unwrap().len(), 10983);
    assert_eq!(rank7["classes"].as_array().unwrap().len(), 8532);
    assert_eq!(positive["blocked_by_wall_rank"]["4"], json!(36));
    assert_eq!(positive["positive_open_by_wall_rank"]["4"], json!(0));
    assert_eq!(positive["blocked_by_wall_rank"]["5"], json!(2101));
    assert_eq!(positive["positive_open_by_wall_rank"]["5"], json!(0));
    assert_eq!(positive["positive_open_by_wall_rank"]["6"], json!(10983));
    assert_eq!(positive["positive_open_by_wall_rank"]["7"], json!(8532));

    let compact = |value: &Value| {
        value["all_orbits"].as_array().unwrap().iter().map(|item| (
            item["canonical_key"].as_str().unwrap().to_string(),
            (item["stabilizer_order"].as_u64().unwrap(), item["enumerated_source_multiplicity"].as_u64().unwrap())
        )).collect::<BTreeMap<_,_>>()
    };
    assert_eq!(inventory["source_term_count"], replication["source_term_count"]);
    assert_eq!(inventory["cyclic_orbit_count"], replication["cyclic_orbit_count"]);
    assert_eq!(compact(&inventory), compact(&replication));

    let positive_index = positive["orbits"].as_array().unwrap().iter().map(|item| {
        (item["canonical_key"].as_str().unwrap(), item)
    }).collect::<BTreeMap<_,_>>();
    let mut k_linear = 0usize;
    let mut kl_linear = 0usize;
    for item in rank4["classes"].as_array().unwrap() {
        assert!(!item["fully_saturated_common_gcd_is_constant"]
            .as_bool()
            .unwrap());
        assert!(item["source_normalized_projective_multiplier"].is_object());
        let residual = item["residual_common_gcd_after_Gram_soft_lower_saturation"].as_str().unwrap();
        if residual.contains("(-3+2*k)") { k_linear += 1; }
        if residual.contains("(7+6*k-8*l)") { kl_linear += 1; }
        let gate = positive_index[item["canonical_key"].as_str().unwrap()];
        assert_eq!(gate["positive_cone_obstructed"], json!(true));
        assert!(gate["gordan_row_coefficients"].is_array());
    }
    assert_eq!((k_linear, kl_linear), (21, 15));
    for item in rank5["classes"]
        .as_array()
        .unwrap()
        .iter()
        .chain(rank6["classes"].as_array().unwrap())
        .chain(rank7["classes"].as_array().unwrap())
    {
        assert!(item["residual_common_gcd_is_constant"].as_bool().unwrap());
        assert!(!item["all_maximal_minors_zero"].as_bool().unwrap());
    }
    assert_eq!(cartier["orbit_count"], json!(21652));
    assert_eq!(cartier["fiber_count"], json!(43304));
    for item in cartier["orbits"].as_array().unwrap() {
        for fiber in item["fibers"].as_array().unwrap() {
            assert!(fiber["generic_cartier"].as_bool().unwrap());
            assert!(fiber["reduced_generic_cartier"].as_bool().unwrap());
            assert_eq!(fiber["cartier_length_at_generic_divisor_point"], json!(1));
        }
    }
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
        let gate=positive_index[item["canonical_key"].as_str().unwrap()];
        json!({"canonical_key":item["canonical_key"],"stabilizer_order":source["stabilizer_order"],"orbit_size":source["orbit_size"],"source_representative":source["representative"],"source_normalized_projective_multiplier":item["source_normalized_projective_multiplier"],"real_sheet_condition":{"strictly_positive_X":"empty","exact_obstruction":"Gordan alternative","base_relations":gate["base_relations"],"row_coefficients":gate["gordan_row_coefficients"]},"Bunch_Davies_activation":"absent because strict positive-X is necessary","charts":charts})
    }).collect::<Vec<_>>();
    let packet = json!({
        "schema":"marici.eight_site_inventory_exhaustion_certificate.v1",
        "frozen_inventory":{"labelled_terms":173216,"orbits":21652,"classes":7855,"primes":[1000003,1000033],"exact_completeness_certificate":{"denominator_minor_Hadamard_bound":"12^8 = 429981696 < 1000003*1000033","affine_minor_Hadamard_bound":"8^9 = 134217728 < 1000003*1000033","argument":"a nonzero exact denominator or affine minor cannot vanish modulo both primes within these bounds; identical key, stabilizer, and multiplicity maps therefore certify the rank-pruned inventory exactly"}},
        "classification":{
            "rank4":{"orbits":36,"classification":"coefficient horizontal discriminant candidates after Gram/soft/lower saturation; physically empty by exact positive-base Gordan certificates","linear_occurrence_families":{"2k-3":21,"7+6k-8l":15},"positive_physical":0},
            "rank5":{"orbits":2101,"classification":"higher-codimension critical support only; no common codimension-one Jacobian factor; independently positive-X empty"},
            "rank6":{"orbits":10983,"classification":"higher-codimension critical support (possibly empty); no common codimension-one Jacobian factor","positive_X_open":10983},
            "rank7":{"orbits":8532,"classification":"higher-codimension critical support (possibly empty); no common codimension-one Jacobian factor","positive_X_open":8532}
        },
        "terminal_theorem":"no source-admitted eight-site orbit carries a horizontal physical divisor in the strictly positive X_i Bunch-Davies chamber",
        "separation":"Carrier incidence != coefficient discriminant != physical activation persists on the complete frozen C8 inventory",
        "candidate_obligations":{"labelled_atlases":candidate_atlases.len(),"Gram_soft_lower_saturation":36,"exact_projective_multipliers":36,"positive_X_and_BD_exclusions":36,"all_orbit_Gram_boundary_fibers":cartier["fiber_count"],"all_generic_Cartier_length_one":cartier["fiber_count"]},
        "routing_gram":{"determinant":"-1/4*k*(6+7*k)","extension_only_parameter":"l","Gram_boundaries":["k=0","k=-6/7"]},
        "candidate_occurrence_atlases":candidate_atlases,
        "scope":"finite exhaustion theorem for the complete frozen eight-site source inventory; it does not assert an all-site or all-loop theorem"
    });
    fs::write(
        "../results/eight-site-inventory-exhaustion-certificate.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"orbits":21652,"rank4_candidates":36,"rank5_no_divisor":2101,"rank6_no_divisor":10983,"rank7_no_divisor":8532,"physical_horizontal_divisors":0,"candidate_atlases":candidate_atlases.len()})
    );
}
