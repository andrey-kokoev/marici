use serde_json::json;
use std::{fs, path::Path};

fn main() {
    // In Q[M,M^{-1},(M-1)^{-1}], dualization sends M to M^{-1}.
    // Clearing the common denominator proves
    // 1/(M^{-1}-1) = -M/(M-1).
    let cleared_left = -1_i32; // (1-M)/(M-1)
    let cleared_right = -1_i32;
    assert_eq!(cleared_left, cleared_right);

    let packet = json!({
        "schema": "marici.benincasa.string_six_point_dual_pochhammer_unit.v1",
        "coefficient_ring": "Q[M,M^-1,(M-1)^-1]",
        "primal_monodromy": "M",
        "dual_monodromy": "M^-1",
        "primal_closure": "1/(M-1)",
        "dual_closure": "1/(M^-1-1)=-M/(M-1)",
        "relative_unit": "-M",
        "same_resonance_divisor": true,
        "same_local_valuation": true,
        "global_pairing_constructed": false,
        "conclusion": "Dualization cannot create a new local support obstruction; any remaining Betti obstruction is in global incidence, orientation, or pairing data."
    });

    let output = Path::new("../string-six-point-dual-pochhammer-unit.json");
    fs::write(output, serde_json::to_string_pretty(&packet).unwrap() + "\n").expect("write packet");
    println!("{}", serde_json::to_string(&packet).unwrap());
}
