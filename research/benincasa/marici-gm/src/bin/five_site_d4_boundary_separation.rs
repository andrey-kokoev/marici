use serde_json::{json, Value};
use std::fs;

fn main() {
    let census: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-cyclic-triple-region-census.json").unwrap(),
    )
    .unwrap();
    let record = census["records"]
        .as_array()
        .unwrap()
        .iter()
        .find(|record| record["representative"] == "g_12|g_34|g_5")
        .unwrap();

    assert_eq!(record["squarefree"], true);
    assert_eq!(record["coprime_to_both_free_coordinate_soft_tests"], true);
    assert_eq!(record["coprime_to_entry_1870_and_lower_union"], true);
    assert_eq!(
        record["fixed_linear_y_over_t"],
        json!([null, "-3/2", null, "-1/2", "-1/2"])
    );

    let d4 = [202_304_i64, -231_696, 95_289, -16_576, 1_024];
    assert_ne!(d4[0], 0);
    let packet = json!({
        "schema": "marici.benincasa.five_site.d4_boundary_separation.v1",
        "representative": "g_12|g_34|g_5",
        "D4_coefficients_ascending_in_z": d4,
        "total_energy_test": {"support": "z=t^2=0", "D4_at_zero": d4[0], "intersects": false},
        "fixed_coordinate_soft_test": {
            "fixed_y_over_t": record["fixed_linear_y_over_t"],
            "all_nonzero_for_t_nonzero": true,
            "intersection_requires_z_zero": true
        },
        "free_coordinate_soft_test": {
            "free_y_indices": record["free_y_indices"],
            "coprime_to_both_soft_eliminants": record["coprime_to_both_free_coordinate_soft_tests"]
        },
        "lower_wall_test": {
            "coprime_to_certified_lower_union": record["coprime_to_entry_1870_and_lower_union"]
        },
        "claim": "D4 is disjoint from total-energy, all edge-soft, and certified lower-wall support on the frozen cyclic slice.",
        "scope": "Frozen homogeneous cyclic slice only; dehomogeneous intersections are not excluded."
    });
    fs::write(
        "../results/five-site-d4-boundary-separation.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", serde_json::to_string_pretty(&packet).unwrap());
}
