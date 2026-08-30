use serde_json::{json, Value};
use std::{collections::BTreeMap, fs};

fn read(path: &str) -> Value {
    serde_json::from_str(&fs::read_to_string(path).unwrap()).unwrap()
}

fn parse_i64(value: &Value) -> i64 {
    value.as_str().unwrap().parse().unwrap()
}

fn main() {
    let exhaustion = read("../results/eight-site-inventory-exhaustion-certificate.json");
    let rank4 = read("../results/eight-site-rank4-universal-jacobian.json");
    let candidates = exhaustion["candidate_occurrence_atlases"]
        .as_array()
        .unwrap();
    let rank4_index = rank4["classes"]
        .as_array()
        .unwrap()
        .iter()
        .map(|item| (item["canonical_key"].as_str().unwrap(), item))
        .collect::<BTreeMap<_, _>>();

    assert_eq!(candidates.len(), 36);
    let mut families = BTreeMap::<&str, usize>::new();
    let mut records = Vec::new();
    for candidate in candidates {
        let key = candidate["canonical_key"].as_str().unwrap();
        let item = rank4_index[key];
        let residual = item["residual_common_gcd_after_Gram_soft_lower_saturation"]
            .as_str()
            .unwrap();
        let family = if residual.contains("(-3+2*k)") {
            "2*k-3"
        } else if residual.contains("(7+6*k-8*l)") {
            "7+6*k-8*l"
        } else {
            panic!("unclassified rank-four divisor for {key}")
        };
        *families.entry(family).or_default() += 1;

        // Verify the Gordan obstruction itself rather than trusting the
        // serialized verdict.  A nonzero nonnegative element of the row span
        // annihilates every solution X of R_X X=0 and therefore excludes
        // X_i>0.
        let sheet = &candidate["real_sheet_condition"];
        let relations = sheet["base_relations"].as_array().unwrap();
        let coefficients = sheet["row_coefficients"].as_array().unwrap();
        assert_eq!(relations.len(), coefficients.len());
        let n = relations[0].as_array().unwrap().len();
        assert_eq!(n, 8);
        let mut obstruction = vec![0i64; n];
        for (row, coefficient) in relations.iter().zip(coefficients) {
            let coefficient = parse_i64(coefficient);
            for (entry, value) in row.as_array().unwrap().iter().zip(&mut obstruction) {
                *value += coefficient * parse_i64(entry);
            }
        }
        assert!(obstruction.iter().all(|entry| *entry >= 0));
        assert!(obstruction.iter().any(|entry| *entry > 0));
        let deliberate_positive_test = obstruction.iter().sum::<i64>();
        assert!(deliberate_positive_test > 0);

        let charts = candidate["charts"].as_array().unwrap();
        assert_eq!(charts.len(), 8);
        let orientations = charts
            .iter()
            .map(|chart| chart["residue_wedge_sorting_sign"].as_i64().unwrap())
            .collect::<Vec<_>>();
        assert!(orientations.iter().all(|sign| sign.abs() == 1));

        // The determinant has one displayed copy of the relevant irreducible
        // linear factor.  Over its generic DVR this gives a length-one
        // coefficient grade.  The source-normalized adjugate identity fixes
        // its conormal occurrence line before physical pairing.
        let factor_token = if family == "2*k-3" {
            "(-3+2*k)"
        } else {
            "(7+6*k-8*l)"
        };
        assert_eq!(residual.matches(factor_token).count(), 1);
        let companion = residual.replacen(factor_token, "1", 1);
        assert!(companion.len() > 100);
        assert!(companion.contains('X') || companion.contains('t'));
        assert_eq!(
            candidate["source_normalized_projective_multiplier"]["identity"],
            json!("lambda*J=det(J)*e_1")
        );

        records.push(json!({
            "canonical_key":key,
            "linear_coefficient_divisor":family,
            "generic_coefficient_grade":{"rank":1,"cartier_length":1,"reason":"simple determinant valuation with source-normalized adjugate line"},
            "companion_coefficient_discriminant":{"present":true,"physical_support_pullback":"empty independently of its irreducible decomposition"},
            "gordan_obstruction_vector":obstruction,
            "deliberate_failure_test":{"putative_X":[1,1,1,1,1,1,1,1],"obstruction_pairing":deliberate_positive_test,"predicted_zero_if_on_wall":0,"result":"nonzero contradiction"},
            "physical_support_pullback":"empty on Gamma_BD={X_i>0}",
            "occurrence_orientation_signs":orientations,
            "supported_comparison":{
                "source":"relative chains supported on Gamma_BD",
                "target":"ordinary coefficient grade supported on the rank-four wall intersected with the displayed divisor",
                "map":"unique zero map because the target support has empty pullback to Gamma_BD",
                "orientation":"retained in all eight occurrence charts; multiplication of zero by either sign is zero",
                "physical_image_rank":0,
                "ordinary_transport":"identity on the zero image",
                "lift_independence":"strict: the supported source object is zero before any lift or chart choice"
            },
            "comparison_cone":{
                "coefficient_grade_survives":true,
                "physical_class_survives":false,
                "classification":"dormant coefficient support over the unchanged Carrier"
            }
        }));
    }
    assert_eq!(families.get("2*k-3"), Some(&21));
    assert_eq!(families.get("7+6*k-8*l"), Some(&15));

    let packet = json!({
        "schema":"marici.eight_site_supported_activation_gate.v1",
        "frozen_physical_chain":"Gamma_BD: X_i>0 with the source Bunch-Davies boundary value",
        "frozen_operations":["ordinary restriction","ordinary boundary Gysin/residue","ordinary localization/Cut support pullback"],
        "support_axiom":"each frozen ordinary operation is support-local and cannot create a section after pullback to an empty support",
        "candidate_divisor_families":{"2*k-3":21,"7+6*k-8*l":15},
        "candidate_count":records.len(),
        "records":records,
        "physical_image_rank":0,
        "linear_coefficient_grade_rank":36,
        "companion_discriminants":"36 nonconstant exact factors; every irreducible component has the same empty physical pullback, without assigning an unproved total nearby-cycle rank",
        "ordinary_transport":"identity on the zero supported image for every occurrence chart",
        "lift_independence":"strict, because vanishing occurs before weighted, normal, or analytic lifts",
        "terminal_classification":"every divisor component of all 36 C8 coefficient discriminants is dormant under ordinary support-local pullback from the literal Bunch-Davies chamber",
        "remaining_gate":"source-defined Leray/nearby specialization may be nonzero even when ordinary pullback is empty and is not decided by this checker",
        "new_carrier_structure":false,
        "scope":"ordinary source-derived support-local operations over the unchanged C8 Carrier; Leray/nearby activation, coefficient monodromy, and analytic continuation are not classified"
    });
    fs::write(
        "../results/eight-site-supported-activation-gate.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"candidates":36,"coefficient_grade_rank":36,"physical_image_rank":0,"lift_independent":true,"new_carrier":false})
    );
}
