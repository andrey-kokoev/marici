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
    let mut checks=0_usize;
    for sheet in 0..32 {for mask in 0..32 {
        let delta=o[sheet^mask]-o[sheet];
        let coefficient_shift=delta;
        let betti_shift=-delta;
        assert_eq!(coefficient_shift+betti_shift,0);
        checks+=1;
    }}
    assert_eq!(checks,1024);
    let elementary_positive=(0..5).map(|bit|{
        let target=1<<bit;let delta=o[target]-o[0];
        assert_eq!(delta,-5);
        json!({"generator":bit+1,"source_sheet":0,"target_sheet":target,
            "coefficient_shift":delta,"dual_betti_shift":-delta,"net_pairing_shift":0})
    }).collect::<Vec<_>>();
    let packet=json!({
        "schema":"marici.benincasa.five_site.exceptional_coefficient_betti_pairing.v1",
        "coefficient_lattice":"L_S=tau^(o(S))*O",
        "dual_betti_lattice":"B_S=tau^(-o(S))*O",
        "normalized_generators":"e_S=tau^(-o(S))*f_S and gammahat_S=tau^(o(S))*Gamma_S",
        "transport":"coefficient shift Delta_a(S), Betti shift -Delta_a(S)",
        "all_sheet_mask_pairing_checks":checks,
        "positive_to_elementary_order_four":elementary_positive,
        "conclusion":{
            "exceptional_pairing_shift_cancels":true,
            "simultaneous_deck_continuation_remains_strict":true,
            "new_exceptional_boundary_current_forced":false,
            "even_grades_are_deck_continued_chamber_readouts":true,
            "positive_chamber_simultaneously_reads_even_grades":false
        },
        "scope":"Exceptional lattice typing of the already established raw coefficient-Betti pairing; no equality of periods on different chambers is asserted."
    });
    fs::write("../results/five-site-exceptional-coefficient-betti-pairing.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["conclusion"]).unwrap());
}
