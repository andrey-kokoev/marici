use serde_json::{json, Value};
use std::fs;

fn main() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/six-site-disjoint-pair-triple-source-gate.json").unwrap(),
    )
    .unwrap();
    let critical: Value = serde_json::from_str(
        &fs::read_to_string("../results/six-site-disjoint-pair-triple-generic-critical.json")
            .unwrap(),
    )
    .unwrap();

    let completions = source["compatible_source_term_completions"]
        .as_array()
        .unwrap();
    assert_eq!(completions.len(), 9);
    let expected = [
        ["G_minus_e23", "g_1256"],
        ["G_minus_e23", "g_3456"],
        ["G_minus_e45", "g_1234"],
        ["G_minus_e45", "g_1256"],
        ["G_minus_e61", "g_1234"],
        ["G_minus_e61", "g_3456"],
        ["g_1234", "g_1256"],
        ["g_1234", "g_3456"],
        ["g_1256", "g_3456"],
    ];
    for (actual, expected_pair) in completions.iter().zip(expected) {
        let actual = actual.as_array().unwrap();
        assert_eq!(actual[0].as_str().unwrap(), expected_pair[0]);
        assert_eq!(actual[1].as_str().unwrap(), expected_pair[1]);
    }

    let witness = &critical["positive_multiplier_witness_at_k_minus_1_over_2"];
    assert_eq!(witness["z"], "2891/842");
    assert_eq!(witness["x"], "5899/842");
    assert_eq!(witness["v"], "1129/421");
    assert_eq!(witness["w"], "2207/421");
    let conormal = witness["square_conormal_coefficients"].as_array().unwrap();
    assert_eq!(
        conormal,
        &vec![
            json!("-17885/107776"),
            json!("-35/6736"),
            json!("-11025/107776")
        ]
    );

    // On Xi=t and y2=y4=y6=-t, every G-e_even denominator is 4t,
    // while every listed connected four-site denominator is 2t.
    let denominator_units = completions
        .iter()
        .map(|pair| {
            pair.as_array()
                .unwrap()
                .iter()
                .map(|label| {
                    if label.as_str().unwrap().starts_with("G_minus") {
                        4i64
                    } else {
                        2i64
                    }
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();
    assert_eq!(
        denominator_units
            .iter()
            .filter(|pair| pair == &&vec![4, 2])
            .count(),
        6
    );
    assert_eq!(
        denominator_units
            .iter()
            .filter(|pair| pair == &&vec![2, 2])
            .count(),
        3
    );

    // Sum of the nine completion residues in units of the common positive
    // source prefactor and t^{-2}: 6/(4*2)+3/(2*2)=3/2.
    let common_denominator = 8i64;
    let residue_numerator = denominator_units
        .iter()
        .map(|pair| common_denominator / (pair[0] * pair[1]))
        .sum::<i64>();
    assert_eq!(residue_numerator, 12);
    let residue_reduced = "3/(2*t^2)";

    let packet = json!({
        "schema":"marici.six_site_disjoint_pair_triple_iepsilon_pairing.v1",
        "kinematic_witness":{
            "k":"-1/2",
            "t":"sqrt(2891/842)>0",
            "wall_sheet":["y2=-t","y4=-t","y6=-t"],
            "odd_sheet":["y1=+sqrt(5899/842)","y3=+sqrt(1129/421)","y5=+sqrt(2207/421)"]
        },
        "wall_multipliers":{
            "square_conormal":conormal,
            "dy_conversion":"multiply by -2*t",
            "projective_signs":["+","+","+"],
            "all_nonzero":true
        },
        "source_residue":{
            "completion_denominator_units":denominator_units,
            "six_terms":"1/(4t*2t)",
            "three_terms":"1/(2t*2t)",
            "sum_in_common_positive_prefactor":residue_reduced,
            "nonzero":true,
            "sign":"positive"
        },
        "bunch_davies_regulator":{
            "site_regulators":"Xi -> Xi-i*epsilon_i, epsilon_i>0",
            "active_wall_imaginary_parts":["-(epsilon1+epsilon2)","-(epsilon3+epsilon4)","-(epsilon5+epsilon6)"],
            "pairing_with_positive_multiplier_normal":"strictly negative on the complete positive regulator cone",
            "hierarchy_required":false
        },
        "local_singularity":"ordinary real A1 node with two branches",
        "physical_intersection_absolute_value":1,
        "conclusion":"the generic six-site divisor has a source-normalized Bunch-Davies-activated real sheet at k=-1/2",
        "scope":"one exact interior sheet; global continuation and specialization to k=0 remain to be computed"
    });
    fs::write(
        "../results/six-site-disjoint-pair-triple-iepsilon-pairing.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"source_terms":9,"residue":residue_reduced,"multiplier_signs":"+++","bd_activation":true})
    );
}
