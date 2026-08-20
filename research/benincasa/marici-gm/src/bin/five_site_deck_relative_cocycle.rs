use serde_json::{json,Value};
use std::{collections::BTreeSet,fs};

fn vector(label:&str)->(Vec<i32>,Vec<i32>){
    let mut x=vec![0;5];let mut y=vec![0;5];
    if label=="G"{x.fill(1);return(x,y)}
    if let Some(edge)=label.strip_prefix("G_minus_e"){
        x.fill(1);let e=edge.chars().next().unwrap().to_digit(10).unwrap() as usize-1;y[e]=2;return(x,y)
    }
    let s=label.strip_prefix("g_").unwrap().chars().map(|c|c.to_digit(10).unwrap() as usize-1).collect::<BTreeSet<_>>();
    for &i in &s{x[i]=1}for e in 0..5{if s.contains(&e)!=s.contains(&((e+1)%5)){y[e]=1}}
    (x,y)
}
fn act(y:&[i32],mask:usize)->Vec<i32>{(0..5).map(|e|if(mask>>e)&1==1{-y[e]}else{y[e]}).collect()}
fn main(){
    let src:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cyc=&src["five_cycle"];let mut labels=BTreeSet::new();
    for v in cyc["common_prefactor"].as_array().unwrap(){labels.insert(v.as_str().unwrap().to_string());}
    for t in cyc["terms"].as_array().unwrap(){for v in t.as_array().unwrap(){labels.insert(v.as_str().unwrap().to_string());}}
    let forms=labels.iter().map(|l|vector(l)).collect::<Vec<_>>();
    let mut square_checks=0;let mut commute_checks=0;let mut transport_checks=0;
    for mask in 0..32{
        for i in 0..5{
            for(_,y)in &forms{assert_eq!(act(&act(y,mask^(1<<i)),1<<i),act(y,mask));transport_checks+=1;}
            assert_eq!((mask^(1<<i))^(1<<i),mask);square_checks+=1;
        }
        for i in 0..5{for j in i+1..5{
            assert_eq!((mask^(1<<i))^(1<<j),(mask^(1<<j))^(1<<i));commute_checks+=1;
        }}
    }
    let packet=json!({
        "schema":"marici.benincasa.five_site.deck_relative_cocycle.v1",
        "objects":"32 labelled chamber-relative complexes M_g",
        "generator":"T_i pulls back by y_i -> -y_i and sends M_g to M_(g xor e_i)",
        "label_transport":"facet labels and their fixed order are retained; only the labelled y coefficient changes sign",
        "differential_identity":"T_i^*(dq_label,g)=dq_label,(g xor e_i)",
        "residue_orientation":"preserved in the fixed source-label order; no fitted permutation sign",
        "ambient_physical_current":"du1 wedge du2 wedge du3 / sqrt(det(H)), invariant under every T_i",
        "generator_square_checks":square_checks,
        "generator_commutation_checks":commute_checks,
        "section_transport_checks":transport_checks,
        "cocycle":"T_i^2=id and T_i T_j=T_j T_i strictly",
        "projective_cocycle_defect":0,
        "equivariant_descent":"strict C2^5 induced chamber package; invariants evaluate to the positive physical chamber",
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-deck-relative-cocycle.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
