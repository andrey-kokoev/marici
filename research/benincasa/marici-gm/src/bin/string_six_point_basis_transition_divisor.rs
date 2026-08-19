use std::collections::BTreeMap;

fn add(map: &mut BTreeMap<&'static str, i32>, factor: &'static str, exponent: i32) {
    *map.entry(factor).or_default() += exponent;
}

fn main() {
    let mut dense = BTreeMap::new();
    for factor in ["s12", "s13", "s14", "s23", "s24", "s34", "s1234"] {
        add(&mut dense, factor, 2);
    }
    for factor in ["s234", "s123", "s124", "s134"] {
        add(&mut dense, factor, 1);
    }

    let blocks = [
        [("s12", 2), ("s34", 1), ("s35", 1), ("s45", 1), ("s345", 1)],
        [("s13", 2), ("s24", 1), ("s25", 1), ("s45", 1), ("s245", 1)],
        [("s14", 2), ("s23", 1), ("s35", 1), ("s25", 1), ("s235", 1)],
    ];
    let mut block = BTreeMap::new();
    for factors in blocks {
        for (factor, exponent) in factors {
            add(&mut block, factor, exponent);
        }
    }

    let mut transition = dense.clone();
    for (factor, exponent) in &block {
        add(&mut transition, factor, -*exponent);
    }
    transition.retain(|_, exponent| *exponent != 0);

    for pivot in ["s12", "s13", "s14"] {
        assert!(!transition.contains_key(pivot));
    }
    let zeros: BTreeMap<_, _> = transition.iter().filter(|(_, e)| **e > 0).collect();
    let poles: BTreeMap<_, _> = transition.iter().filter(|(_, e)| **e < 0).collect();
    assert_eq!(zeros.values().map(|e| **e).sum::<i32>(), 9);
    assert_eq!(poles.values().map(|e| -**e).sum::<i32>(), 9);

    let json = serde_json::json!({
        "schema": "marici.benincasa.string_six_point_basis_transition_divisor.v1",
        "common_left_basis": ["123456","124356","132456","134256","142356","143256"],
        "dense_right_basis": ["562341","562431","563241","563421","564231","564321"],
        "block_right_basis": ["153462","154362","152463","154263","152364","153264"],
        "definition": "T = M_block K_dense",
        "identity": "K_block T = K_dense",
        "dense_determinant": dense,
        "block_determinant": block,
        "transition_divisor": transition,
        "zero_order": 9,
        "pole_order": 9,
        "new_nonchannel_divisor": false,
        "passed": true
    });
    println!("{}", serde_json::to_string_pretty(&json).unwrap());
}
