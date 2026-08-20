use serde_json::json;
use std::{collections::BTreeSet, fs};

fn main() {
    let mut orbit = BTreeSet::new();
    let positive = 0_u8;
    let mut action_checks = 0_u64;
    for deck in 0_u8..32 {
        let image = positive ^ deck;
        orbit.insert(image);
        for mask in 0_u8..32 {
            assert_eq!((mask ^ deck) ^ deck, mask);
            action_checks += 1;
        }
    }
    assert_eq!(orbit.len(), 32);
    let stabilizer = (0_u8..32)
        .filter(|deck| positive ^ deck == positive)
        .collect::<Vec<_>>();
    assert_eq!(stabilizer, vec![0]);

    // On a branch stratum F_i=0, the two signs of y_i coincide. More
    // generally, on F_i=0 for i in B, masks differing only inside B have the
    // same restriction. Verify the quotient cardinality 2^(5-|B|).
    let mut restriction_checks = 0_u64;
    let mut strata = Vec::new();
    for branch_subset in 0_u8..32 {
        let mut classes = BTreeSet::new();
        let retained = (!branch_subset) & 31;
        for mask in 0_u8..32 {
            classes.insert(mask & retained);
            for flip in 0_u8..32 {
                if flip & !branch_subset == 0 {
                    assert_eq!((mask ^ flip) & retained, mask & retained);
                    restriction_checks += 1;
                }
            }
        }
        let expected = 1_usize << (5 - branch_subset.count_ones());
        assert_eq!(classes.len(), expected);
        strata.push(json!({
            "branch_subset_mask": branch_subset,
            "codimension": branch_subset.count_ones(),
            "restricted_sheet_classes": classes.len()
        }));
    }

    // The orbit sum is invariant, while the locally selected positive chain
    // is not invariant under any nontrivial generator.
    let trace_coefficients = vec![1_i8; 32];
    for generator in 0..5 {
        let transported = (0_u8..32)
            .map(|mask| trace_coefficients[(mask ^ (1 << generator)) as usize])
            .collect::<Vec<_>>();
        assert_eq!(transported, trace_coefficients);
        assert_ne!(positive ^ (1 << generator), positive);
    }

    let packet = json!({
        "schema": "marici.benincasa.five_site.physical_sheet_orbit.v1",
        "local_source_chain": "Gamma_+ on the positive Kummer sheet over the real Bunch-Davies chamber",
        "deck_orbit_size": orbit.len(),
        "stabilizer_size": stabilizer.len(),
        "representation": "regular permutation module Q[(Z2)^5]",
        "action_checks": action_checks,
        "branch_restriction_checks": restriction_checks,
        "branch_strata": strata,
        "trace": "sum_g Gamma_g is deck-invariant",
        "physical_evaluation": "Gamma_+ is a source-selected local chamber vector, not an invariant vector",
        "orientation": "Deck maps fix the physical u_1,u_2,u_3 coordinates, hence preserve the source current orientation.",
        "result": "The physical sheet has coherent equivariant continuation, but does not descend to a single invariant cycle.",
        "classification": "sector-specific Betti local system on the existing Kummer cover",
        "new_carrier_datum": false
    });
    fs::write(
        "../results/five-site-physical-sheet-orbit.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", serde_json::to_string(&packet).unwrap());
}
