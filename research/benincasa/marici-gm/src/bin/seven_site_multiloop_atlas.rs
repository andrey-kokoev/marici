use serde_json::{json, Value};
use std::fs;

fn read(path: &str) -> Value {
    serde_json::from_str(&fs::read_to_string(path).unwrap()).unwrap()
}

fn main() {
    let selection = read("../results/seven-site-multiloop-orbit-selection.json");
    let cover = read("../results/seven-site-multiloop-cover.json");
    let universal = read("../results/seven-site-maximal-flag-atlas.json");
    let occurrence_charts = selection["labelled_C7_charts"].as_array().unwrap();
    let routing_charts = universal["charts"].as_array().unwrap();
    assert_eq!(occurrence_charts.len(), 7);
    assert_eq!(routing_charts.len(), 7);
    assert_eq!(
        cover["routing_gram_determinant"],
        universal["routing_gram_determinant"]
    );
    assert_eq!(
        universal["certification"],
        json!("49 exact labelled squared-distance pullback identities")
    );
    for shift in 0..7 {
        assert_eq!(occurrence_charts[shift]["shift"], json!(shift));
        assert_eq!(routing_charts[shift]["origin"], json!(shift + 1));
        assert_eq!(
            routing_charts[shift]["seven_cover_pullbacks_zero"],
            json!([true, true, true, true, true, true, true])
        );
    }
    let packet = json!({
        "schema":"marici.seven_site_multiloop_atlas.v1",
        "construction":"fiber product of the exact universal seven-point Gram-completed routing atlas with the selected orbit's labelled C7 occurrence atlas",
        "selected_canonical_key":selection["selected_orbit"]["canonical_key"],
        "routing_gram_determinant":cover["routing_gram_determinant"],
        "occurrence_charts":occurrence_charts,
        "Gram_completed_routing_charts":routing_charts,
        "unrestricted_normal_gram":universal["unrestricted_normal_gram"],
        "transition_orientation":"source occurrence order and wedge sorting signs are retained chart by chart",
        "certification":{
            "routing":"49 exact labelled squared-distance pullback identities inherited without changing the generic cover",
            "occurrence":"seven exact C7 transports with stabilizer and residue-wedge sign retained",
            "no_projection_loss":"unrestricted normal Gram data are carried alongside the Gram-completed routing charts"
        }
    });
    fs::write(
        "../results/seven-site-multiloop-atlas.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"occurrence_charts":occurrence_charts.len(),"routing_charts":routing_charts.len(),"pullback_identities":49})
    );
}
