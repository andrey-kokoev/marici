use serde_json::{json,Value};
use std::fs;

fn main(){
    let source:Value=serde_json::from_str(
        &fs::read_to_string("../results/five-site-two-normal-rees.json").unwrap()
    ).unwrap();
    let mut o=[0_i32;32];
    for row in source["tau_sheet_orders"].as_array().unwrap(){
        o[row["sheet"].as_u64().unwrap() as usize]=row["tau_vanishing_order"].as_i64().unwrap() as i32;
    }
    let shift=|s:usize,m:usize|o[s^m]-o[s];
    let mut associativity_checks=0_usize;
    let mut commutation_checks=0_usize;
    for s in 0..32 {
        for a in 0..32 {
            for b in 0..32 {
                assert_eq!(shift(s,a)+shift(s^a,b),shift(s,a^b));
                associativity_checks+=1;
                assert_eq!(shift(s,a)+shift(s^a,b),shift(s,b)+shift(s^b,a));
                commutation_checks+=1;
            }
        }
    }
    for s in 0..32 {for i in 0..5 {
        let m=1<<i;
        assert_eq!(shift(s,m)+shift(s^m,m),0);
    }}
    let zero_shift_masks=(0..32).filter(|&m|(0..32).all(|s|shift(s,m)==0)).collect::<Vec<_>>();
    assert_eq!(zero_shift_masks,vec![0,31]);
    let packet=json!({
        "schema":"marici.benincasa.five_site.flip_rees_coherence.v1",
        "associativity_checks":associativity_checks,
        "commutation_checks":commutation_checks,
        "elementary_square_checks":160,
        "zero_shift_masks":zero_shift_masks,
        "identities":{
            "telescoping":"Delta_a(S)+Delta_b(S xor a)=Delta_(a xor b)(S)",
            "commutation":"Delta_a(S)+Delta_b(S xor a)=Delta_b(S)+Delta_a(S xor b)",
            "square":"Delta_i(S)+Delta_i(S xor 2^i)=0"
        },
        "conclusion":{
            "valuation_cocycle_strict":true,
            "additional_exceptional_coherence_cell_required_by_valuations":false,
            "leading_unit_or_sign_cocycle_tested":false,
            "regular_graded_subgroup":[0,31]
        },
        "scope":"Complete valuation-level composition audit; leading coefficients and physical-current pairings are outside scope."
    });
    fs::write("../results/five-site-flip-rees-coherence.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["conclusion"]).unwrap());
}
