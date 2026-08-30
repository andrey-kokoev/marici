use serde_json::{json, Value};
use std::fs;

fn read(path: &str) -> Value {
    serde_json::from_str(&fs::read_to_string(path).unwrap()).unwrap()
}

fn write(path: &str, value: &Value) {
    fs::write(path, serde_json::to_string_pretty(value).unwrap()+"\n").unwrap();
}

fn main() {
    let mut sizes = Vec::new();
    for rank in 5..=7 {
        let source = format!("../results/eight-site-rank{rank}-universal-jacobian.json");
        let target = format!("../results/eight-site-rank{rank}-universal-jacobian-compact.json");
        let packet = read(&source);
        let classes = packet["classes"].as_array().unwrap().iter().map(|item| json!({
            "canonical_key":item["canonical_key"],
            "all_maximal_minors_zero":item["all_maximal_minors_zero"],
            "residual_common_gcd_is_constant":item["residual_common_gcd_is_constant"],
            "fully_saturated_common_gcd_is_constant":item["fully_saturated_common_gcd_is_constant"],
            "classification":item["classification"]
        })).collect::<Vec<_>>();
        write(&target, &json!({
            "schema":"marici.eight_site_universal_jacobian_compact.v1",
            "wall_rank":rank,
            "source_schema":packet["schema"],
            "classes":classes
        }));
        sizes.push(json!({"rank":rank,"records":classes.len(),"bytes":fs::metadata(&target).unwrap().len()}));
    }

    let positive = read("../results/eight-site-positive-base-gate.json");
    let positive_records = positive["orbits"].as_array().unwrap().iter().map(|item| {
        if item["wall_rank"] == json!(4) {
            item.clone()
        } else {
            json!({
                "canonical_key":item["canonical_key"],
                "wall_rank":item["wall_rank"],
                "positive_cone_obstructed":item["positive_cone_obstructed"]
            })
        }
    }).collect::<Vec<_>>();
    write("../results/eight-site-positive-base-gate-compact.json", &json!({
        "schema":"marici.eight_site_positive_base_gate_compact.v1",
        "criterion":positive["criterion"],
        "certificate_solver":positive["certificate_solver"],
        "orbit_count":positive["orbit_count"],
        "blocked_by_wall_rank":positive["blocked_by_wall_rank"],
        "positive_open_by_wall_rank":positive["positive_open_by_wall_rank"],
        "orbits":positive_records
    }));

    let cartier = read("../results/eight-site-gram-cartier-audit.json");
    let cartier_records = cartier["orbits"].as_array().unwrap().iter().map(|item| json!({
        "canonical_key":item["canonical_key"],
        "wall_rank":item["wall_rank"],
        "fibers":item["fibers"].as_array().unwrap().iter().map(|fiber|json!({
            "k":fiber["k"],
            "global_polynomial_principal":fiber["global_polynomial_principal"],
            "generic_cartier":fiber["generic_cartier"],
            "reduced_generic_cartier":fiber["reduced_generic_cartier"],
            "cartier_length_at_generic_divisor_point":fiber["cartier_length_at_generic_divisor_point"]
        })).collect::<Vec<_>>()
    })).collect::<Vec<_>>();
    write("../results/eight-site-gram-cartier-audit-compact.json", &json!({
        "schema":"marici.eight_site_gram_cartier_audit_compact.v1",
        "criterion":cartier["criterion"],
        "Gram_boundaries":cartier["Gram_boundaries"],
        "orbit_count":cartier["orbit_count"],
        "fiber_count":cartier["fiber_count"],
        "unique_divisorial_hull_generators":cartier["unique_divisorial_hull_generators"],
        "counts":cartier["counts"],
        "orbits":cartier_records
    }));
    println!("{}", json!({"rank_packets":sizes,"positive_records":positive_records.len(),"cartier_records":cartier_records.len()}));
}
