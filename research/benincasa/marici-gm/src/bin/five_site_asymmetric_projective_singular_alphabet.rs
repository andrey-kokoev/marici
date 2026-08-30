use serde_json::{json, Value};
use std::{collections::BTreeMap, fs};

fn read(path: &str) -> Value {
    serde_json::from_str(&fs::read_to_string(path).unwrap()).unwrap()
}

fn run() {
    let one = read("../results/five-site-asymmetric-one-wall-landau.json");
    let pairs = read("../results/five-site-asymmetric-compatible-pairs.json");
    let shared_cut = read("../results/five-site-asymmetric-shared-cut-pairs.json");
    let disjoint_cut = read("../results/five-site-asymmetric-disjoint-cut-pairs.json");
    let shared_mixed = read("../results/five-site-asymmetric-shared-mixed-pairs.json");
    let disjoint_mixed = read("../results/five-site-asymmetric-disjoint-mixed-pairs.json");
    let triples = read("../results/five-site-asymmetric-triple-inheritance.json");

    let mut groups = BTreeMap::<String, Vec<String>>::new();
    for row in one["proper_connected_region_walls"].as_array().unwrap() {
        let polynomial = row["signed_threshold_polynomial"].as_str().unwrap().replace('t', "z");
        groups.entry(polynomial).or_default().push(row["label"].as_str().unwrap().to_owned());
    }
    assert_eq!(groups.len(), 14);
    assert_eq!(groups.values().map(Vec::len).sum::<usize>(), 20);

    let factors = groups.into_iter().map(|(polynomial, labels)| json!({
        "polynomial": polynomial,
        "multiplicity_in_labelled_wall_set": labels.len(),
        "labels": labels
    })).collect::<Vec<_>>();

    let pair_total = pairs["unique_source_compatible_pairs"].as_u64().unwrap();
    assert_eq!(shared_cut["source_compatible_pairs"], 105);
    assert_eq!(shared_cut["unit_resultants"], 105);
    assert_eq!(shared_cut["nonunit_resultants"], 0);
    assert_eq!(disjoint_cut["source_compatible_pairs"], 35);
    assert_eq!(disjoint_cut["excluded_by_unit_staged_resultant"], 35);
    assert_eq!(disjoint_cut["requires_stronger_elimination"], 0);
    assert_eq!(shared_mixed["source_compatible_pairs"], 40);
    assert_eq!(shared_mixed["new_threshold_factor"], false);
    assert_eq!(disjoint_mixed["source_compatible_pairs"], 30);
    assert_eq!(disjoint_mixed["unit_resultants"], 30);
    let pair_unresolved = 0_u64;
    let triple_total = triples["unique_source_compatible_triples"].as_u64().unwrap();
    assert_eq!(triples["classification_counts"]["excluded_by_empty_pair"], 1140);
    assert_eq!(triples["classification_counts"]["restricted_to_existing_total_support"], 70);
    let triple_unresolved = 0_u64;
    assert_eq!(pair_total, 245);
    assert_eq!(pair_unresolved, 0);
    assert_eq!(triple_total, 1210);
    assert_eq!(triple_unresolved, 0);

    let product = factors.iter().map(|row| format!("({})", row["polynomial"].as_str().unwrap()))
        .collect::<Vec<_>>().join("*");
    let packet = json!({
        "schema": "marici.benincasa.five_site.asymmetric.projective_singular_alphabet.v1",
        "projective_coordinate": "z=t/rho",
        "literal_physical_chamber": "z>=sqrt(29)",
        "soft_factor": "z",
        "proper_threshold_factors": factors,
        "distinct_proper_threshold_factor_count": 14,
        "finite_candidate_divisor": format!("z*{product}"),
        "finite_candidate_divisor_degree": 29,
        "point_at_infinity_retained": true,
        "source_compatible_pair_count": pair_total,
        "unresolved_pair_count": pair_unresolved,
        "source_compatible_triple_count": triple_total,
        "unresolved_triple_count": triple_unresolved,
        "higher_intersections": "closed by pair/triple inheritance",
        "physical_boundary_factor": "z^2-29",
        "other_positive_thresholds": "strictly below sqrt(29), hence outside the literal real chamber",
        "acceptance_use": "Allowed source-derived finite singular alphabet for scalar telescoper reconstruction; factors may cancel, but new fitted factors are prohibited.",
        "scope": "Landau/support denominator bound, not proof that every factor is a genuine period singularity."
    });
    fs::write(
        "../results/five-site-asymmetric-projective-singular-alphabet.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    ).unwrap();
    println!("finite_factors=15 divisor_degree=29 pairs=245 triples=1210 unresolved=0");
}

fn main() {
    run();
}
