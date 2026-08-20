use serde_json::json;
use std::fs;

fn character(character: u8, sheet: u8) -> i64 {
    if (character & sheet).count_ones() % 2 == 0 { 1 } else { -1 }
}

fn main() {
    let mut hadamard_checks = 0_u64;
    for left in 0_u8..32 {
        for right in 0_u8..32 {
            let sum = (0_u8..32)
                .map(|sheet| character(left, sheet) * character(right, sheet))
                .sum::<i64>();
            assert_eq!(sum, if left == right { 32 } else { 0 });
            hadamard_checks += 1;
        }
    }

    // Delta-sheet coefficient/cycle pairing is preserved under simultaneous
    // regular translation of both arguments.
    let mut sheet_pairing_checks = 0_u64;
    for generator in 0_u8..5 {
        let shift = 1_u8 << generator;
        for coefficient_sheet in 0_u8..32 {
            for cycle_sheet in 0_u8..32 {
                let before = coefficient_sheet == cycle_sheet;
                let after = (coefficient_sheet ^ shift) == (cycle_sheet ^ shift);
                assert_eq!(before, after);
                sheet_pairing_checks += 1;
            }
        }
    }

    // In the Fourier/character basis, both factors have the same real
    // character, so the diagonal pairing is deck invariant.
    let mut character_pairing_checks = 0_u64;
    for generator in 0_u8..5 {
        for coefficient_character in 0_u8..32 {
            for cycle_character in 0_u8..32 {
                let before = coefficient_character == cycle_character;
                let sign_left = character(coefficient_character, 1 << generator);
                let sign_right = character(cycle_character, 1 << generator);
                let after = before && sign_left * sign_right == 1;
                assert_eq!(before, after);
                character_pairing_checks += 1;
            }
        }
    }

    // Evaluation at the positive sheet is transported to evaluation at the
    // translated sheet; pairing a transported coefficient vector with that
    // transported cycle returns the same scalar component.
    let mut chamber_evaluation_checks = 0_u64;
    for deck in 0_u8..32 {
        for source_sheet in 0_u8..32 {
            let transported_coefficient_index = source_sheet ^ deck;
            let transported_cycle_index = deck;
            let before = source_sheet == 0;
            let after = transported_coefficient_index == transported_cycle_index;
            assert_eq!(before, after);
            chamber_evaluation_checks += 1;
        }
    }

    let packet = json!({
        "schema": "marici.benincasa.five_site.kummer_betti_pairing.v1",
        "coefficient_representation": "regular rank-32 sheet module, equivalently the sum of all Kummer characters",
        "betti_representation": "regular rank-32 orbit of Gamma_+",
        "pairing_sheet_basis": "<e_g,Gamma_h>=delta_(g,h)",
        "pairing_character_basis": "Hadamard/Fourier diagonal; H H^T=32 I",
        "hadamard_orthogonality_checks": hadamard_checks,
        "sheet_pairing_covariance_checks": sheet_pairing_checks,
        "character_pairing_covariance_checks": character_pairing_checks,
        "joint_chamber_evaluation_checks": chamber_evaluation_checks,
        "result": "The coefficient-Betti pairing is strictly invariant under simultaneous deck transport.",
        "physical_meaning": "A chamber scalar is continuation-covariant when coefficient branch and relative cycle are transported together.",
        "qualification": "This fixes representation-theoretic descent, not period normalization or monodromy around non-Kummer discriminants.",
        "new_carrier_datum": false
    });
    fs::write(
        "../results/five-site-kummer-betti-pairing.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", serde_json::to_string(&packet).unwrap());
}
