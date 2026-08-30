use serde_json::{json,Value};
use std::{collections::BTreeMap,fs};

fn main(){
    let source:Value=serde_json::from_str(
        &fs::read_to_string("../results/five-site-two-normal-rees.json").unwrap()
    ).unwrap();
    let mut orders=[0_i32;32];
    for row in source["tau_sheet_orders"].as_array().unwrap(){
        let sheet=row["sheet"].as_u64().unwrap() as usize;
        orders[sheet]=row["tau_vanishing_order"].as_i64().unwrap() as i32;
    }
    let mut flips=Vec::new();
    for bit in 0..5 {
        let mut shifts=BTreeMap::<i32,usize>::new();
        let mut pole_examples=Vec::new();
        for sheet in 0..32 {
            let target=sheet^(1<<bit);
            let shift=orders[target]-orders[sheet];
            *shifts.entry(shift).or_default()+=1;
            if shift<0 && pole_examples.len()<4 {
                pole_examples.push(json!({"source":sheet,"target":target,"shift":shift}));
            }
        }
        assert!(shifts.keys().any(|x|*x<0));
        assert!(shifts.keys().any(|x|*x>0));
        flips.push(json!({
            "generator":bit+1,
            "shift_histogram":shifts.into_iter().map(|(shift,count)|(shift.to_string(),count)).collect::<BTreeMap<_,_>>(),
            "negative_shift_examples":pole_examples,
            "regular_on_raw_sheet_sum":true,
            "regular_on_valuation_normalized_lattice":false
        }));
    }
    let global=31_usize;
    assert!((0..32).all(|s|orders[s^global]==orders[s]));
    let packet=json!({
        "schema":"marici.benincasa.five_site.elementary_flip_rees.v1",
        "normalization":"e_S=tau^(-o(S))*f_S",
        "transition":"T_i(e_S)=tau^(o(S xor 2^i)-o(S))*e_(S xor 2^i)",
        "elementary_flips":flips,
        "global_complement":{
            "mask":31,
            "all_shifts_zero":true,
            "regular_graded_automorphism":true
        },
        "conclusion":{
            "raw_deck_action_regular":true,
            "elementary_flip_filtered_degree_zero":false,
            "elementary_flip_requires_meromorphic_or_hecke_modification":true,
            "only_global_complement_is_regular_on_associated_grading":true
        },
        "scope":"Exact valuation-shift census for the 32-sheet five-site two-normal exceptional lattice; no Hecke extension is adjoined."
    });
    fs::write("../results/five-site-elementary-flip-rees.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["conclusion"]).unwrap());
}
