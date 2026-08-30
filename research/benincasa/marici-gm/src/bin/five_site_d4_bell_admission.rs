use serde_json::{json, Value};
use std::{collections::BTreeSet, fs};

fn collect_keys(value: &Value, keys: &mut BTreeSet<String>) {
    match value {
        Value::Object(object) => {
            for (key, child) in object {
                keys.insert(key.clone());
                collect_keys(child, keys);
            }
        }
        Value::Array(array) => {
            for child in array {
                collect_keys(child, keys);
            }
        }
        _ => {}
    }
}

fn main() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap(),
    )
    .unwrap();
    let monodromy: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-d4-cyclic-monodromy.json").unwrap(),
    )
    .unwrap();
    let readout: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-d4-readout-decomposition.json").unwrap(),
    )
    .unwrap();

    assert_eq!(source["five_cycle"]["term_count"], 180);
    assert_eq!(monodromy["local_blocks"], 5);
    assert_eq!(readout["scalar_readout_covector"], json!([1, 1, 1, 1, 1]));

    let mut keys = BTreeSet::new();
    collect_keys(&source, &mut keys);
    collect_keys(&monodromy, &mut keys);
    collect_keys(&readout, &mut keys);
    let required_bell_keys = [
        "wing_a",
        "wing_b",
        "setting_a",
        "setting_b",
        "outcome_a",
        "outcome_b",
        "joint_probability",
        "normalization",
        "no_signalling",
        "chsh",
    ];
    let present_required_keys = required_bell_keys
        .iter()
        .filter(|key| keys.contains(**key))
        .copied()
        .collect::<Vec<_>>();
    assert!(present_required_keys.is_empty());

    let packet = json!({
        "schema": "marici.benincasa.five_site.d4_bell_admission.v1",
        "frozen_sources": [
            "five-cycle-ofpt-packet.json",
            "five-site-d4-cyclic-monodromy.json",
            "five-site-d4-readout-decomposition.json"
        ],
        "positive_pre_bell_structure": {
            "labelled_occurrence_channels": 5,
            "nontrivial_augmentation_dimension": 4,
            "physical_scalar_ports": 1,
            "nonzero_scalar_logarithm": true
        },
        "bell_gate_order": [
            "source-defined bipartite preparation and wing decomposition",
            "two independently selectable local settings per wing",
            "exclusive local outcome effects",
            "normalized positive joint readout",
            "no-signalling marginals",
            "CHSH and Tsirelson audit"
        ],
        "bell_gate_vector": [0,0,0,0,0,0],
        "first_failure": "no source-defined bipartite wing decomposition",
        "present_required_bell_schema_keys": present_required_keys,
        "typing_warning": "five cyclic occurrence labels are not two local measurement wings; augmentation directions are not detector settings",
        "claim": "The frozen D4 packet contains rich labelled readout data but does not yet define a Bell experiment.",
        "scope": "Bounded census of the three named frozen packets; not a no-go theorem for cosmological Bell tests."
    });
    fs::write(
        "../results/five-site-d4-bell-admission.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", serde_json::to_string_pretty(&packet).unwrap());
}
