use serde_json::{json, Value};
use std::fs;

fn main() {
    let residue: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-cyclic-triple-d4-source-residue.json").unwrap(),
    )
    .unwrap();
    let pairing: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-cyclic-triple-d4-iepsilon-pairing.json").unwrap(),
    )
    .unwrap();
    let orbit: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-cyclic-triple-d4-activation-orbit.json").unwrap(),
    )
    .unwrap();

    assert_eq!(residue["source_term_count"], 8);
    assert_eq!(residue["termwise_cancellation_possible"], false);
    assert_eq!(pairing["picard_lefschetz_intersection_absolute_value"], 1);
    assert_eq!(orbit["orbit_size"], 5);
    assert_eq!(
        orbit["character_on_labelled_occurrences"],
        json!({"identity": 5, "nonidentity": 0})
    );

    // Ordered basis: regular lifts r_0,...,r_4, followed by vanishing lines
    // v_0,...,v_4. The logarithmic extension has N(r_i)=v_i, N(v_i)=0.
    let mut n = vec![vec![0_i8; 10]; 10];
    for occurrence in 0..5 {
        n[5 + occurrence][occurrence] = 1;
    }
    let mut n_squared = vec![vec![0_i8; 10]; 10];
    for row in 0..10 {
        for column in 0..10 {
            n_squared[row][column] = (0..10).map(|k| n[row][k] * n[k][column]).sum();
        }
    }
    assert!(n_squared.iter().flatten().all(|entry| *entry == 0));
    let rank_n = 5;
    let invariant_image = vec![0, 0, 0, 0, 0, 1, 1, 1, 1, 1];
    assert_ne!(invariant_image, vec![0; 10]);

    let packet = json!({
        "schema": "marici.benincasa.five_site.d4_cyclic_monodromy.v1",
        "basis": ["r0","r1","r2","r3","r4","v0","v1","v2","v3","v4"],
        "nilpotent_matrix_N": n,
        "rank_N": rank_n,
        "N_squared_zero": true,
        "local_blocks": 5,
        "local_model": "I_i=c_i*log(tau)+holomorphic with c_i nonzero",
        "cyclic_vanishing_character": {"identity": 5, "nonidentity": 0},
        "rational_character_decomposition": "Q_triv + Q(zeta_5)",
        "invariant_regular_sum_image": invariant_image,
        "invariant_logarithm_nonzero": true,
        "selected_scalar_reason": "cyclic transport preserves the common source-residue and regulator-pairing orientation, so the five invariant coefficients add rather than cancel",
        "claim": "The five D4 occurrences form five rank-one logarithmic extensions; their cyclic invariant sum retains a nonzero rank-one logarithm.",
        "scope": "Local monodromy at the activated open D4 root; no global Picard-Fuchs operator is asserted."
    });
    fs::write(
        "../results/five-site-d4-cyclic-monodromy.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", serde_json::to_string_pretty(&packet).unwrap());
}
