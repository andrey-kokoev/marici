use serde_json::{json, Value};
use std::{collections::BTreeMap, fs};

fn main() {
    let gate: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-triple-inherited-support-gate.json").unwrap(),
    )
    .unwrap();
    let compiler: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-cyclic-triple-landau-ideal-compiler.json")
            .unwrap(),
    )
    .unwrap();

    let dispositions = gate["records"]
        .as_array()
        .unwrap()
        .iter()
        .map(|record| {
            (
                record["D5_representative"].as_str().unwrap().to_owned(),
                record["disposition"].as_str().unwrap().to_owned(),
            )
        })
        .collect::<BTreeMap<_, _>>();

    let mut counts = BTreeMap::<String, [usize; 3]>::new();
    let mut genuine_nonsoft = Vec::new();
    for record in compiler["records"].as_array().unwrap() {
        let representative = record["representative"].as_str().unwrap();
        let disposition = dispositions.get(representative).unwrap();
        let pure = !record["pure_t_wall_solution"].is_null();
        let nonsoft = pure
            && record["pure_t_wall_solution"]["all_pivot_y_nonzero_for_t_nonzero"]
                .as_bool()
                .unwrap();
        let count = counts.entry(disposition.clone()).or_default();
        count[0] += 1;
        count[1] += usize::from(pure);
        count[2] += usize::from(nonsoft);
        if disposition == "unclassified genuine three-wall candidate" && nonsoft {
            genuine_nonsoft.push(json!({
                "representative": representative,
                "solution": record["pure_t_wall_solution"]["solution"],
                "free_y_indices": record["pure_t_wall_solution"]["free_y_indices"]
            }));
        }
    }

    assert_eq!(counts["existing one-wall threshold support"], [33, 24, 24]);
    assert_eq!(
        counts["unclassified genuine three-wall candidate"],
        [63, 8, 4]
    );
    assert_eq!(genuine_nonsoft.len(), 4);

    let packet = json!({
        "schema": "marici.benincasa.five_site.triple_pure_t_support_join.v1",
        "sources": [
            "five-site-triple-inherited-support-gate.json",
            "five-site-cyclic-triple-landau-ideal-compiler.json"
        ],
        "counts_by_disposition": counts.into_iter().map(|(name, count)| (name, json!({
            "total": count[0], "pure_t": count[1], "nonsoft_pure_t": count[2]
        }))).collect::<BTreeMap<_, _>>(),
        "genuine_nonsoft_pure_t_representatives": genuine_nonsoft,
        "claim": "Only four D5 representatives require genuine nonsoft pure-t three-wall elimination on the frozen cyclic slice.",
        "scope": "Linear wall-solution and inherited-support gate only; no Landau discriminant or physical activation is inferred."
    });
    fs::write(
        "../results/five-site-triple-pure-t-support-join.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        serde_json::to_string_pretty(&packet["counts_by_disposition"]).unwrap()
    );
}
