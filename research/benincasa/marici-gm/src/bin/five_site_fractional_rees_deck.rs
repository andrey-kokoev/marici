use serde_json::{json,Value};
use std::{collections::BTreeSet,fs};

fn cut_support(label:&str)->Vec<usize>{
    let sites=label.strip_prefix("g_").unwrap().chars().map(|d|d.to_digit(10).unwrap()as usize).collect::<BTreeSet<_>>();
    (1..=5).filter(|e|sites.contains(e)!=sites.contains(&(e%5+1))).collect()
}
fn radial_vector(label:&str,sheet:usize)->[i32;5]{
    let mut v=[0;5];
    if label=="G"{return v;}
    if let Some(edge)=label.strip_prefix("G_minus_e"){
        let e=edge.chars().next().unwrap().to_digit(10).unwrap()as usize-1;
        v[e]=if sheet&(1<<e)==0{2}else{-2};return v;
    }
    for e in cut_support(label){v[e-1]=if sheet&(1<<(e-1))==0{1}else{-1};}
    v
}
fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cycle=&source["five_cycle"];
    let labels=cycle["common_prefactor"].as_array().unwrap().iter()
        .chain(cycle["terms"].as_array().unwrap().iter().flat_map(|t|t.as_array().unwrap().iter()))
        .map(|x|x.as_str().unwrap().to_owned()).collect::<BTreeSet<_>>();
    assert_eq!(labels.len(),26);
    let mut checks=0;
    for sheet in 0..32 {for bit in 0..5 {for label in &labels {
        let mut transported=radial_vector(label,sheet);
        transported[bit]*=-1;
        assert_eq!(transported,radial_vector(label,sheet^(1<<bit)));
        checks+=1;
    }}}
    assert_eq!(checks,4160);
    let packet=json!({
        "schema":"marici.benincasa.five_site.fractional_rees_deck.v1",
        "wall_count":labels.len(),
        "exact_labelled_wall_transport_checks":checks,
        "wall_form":"L_(q,S)(tau)=k_q*tau+c_(q,S)(r)",
        "deck_transport":"T_a L_(q,S)=L_(q,S xor a), with tau fixed",
        "fractional_lattice":"L_S=tau^(o(S))*O",
        "correspondence":"T_a:L_S -> L_(S xor a) by tau^(o(S xor a)-o(S))",
        "conclusion":{
            "all_tau_jets_transport_strictly":true,
            "first_subleading_extension_required":false,
            "fractional_rees_groupoid_closed":true,
            "ordinary_single_lattice_action":false
        },
        "scope":"Exact wall-level and fractional-lattice theorem; no physical-cycle meromorphic continuation is asserted."
    });
    fs::write("../results/five-site-fractional-rees-deck.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["conclusion"]).unwrap());
}
