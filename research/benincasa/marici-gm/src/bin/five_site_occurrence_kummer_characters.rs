use serde_json::{json,Value};
use std::{collections::BTreeSet,fs};

fn sites(label:&str)->BTreeSet<usize>{
    label.strip_prefix("g_").unwrap().chars().map(|c|c.to_digit(10).unwrap() as usize-1).collect()
}
fn boundary(s:&BTreeSet<usize>)->Vec<i32>{
    (0..5).map(|e|if s.contains(&e)!=s.contains(&((e+1)%5)){1}else{0}).collect()
}
fn main(){
    let src:Value=serde_json::from_str(&fs::read_to_string("../results/five-site-qg-occurrence-kernel.json").unwrap()).unwrap();
    let transitions=src["transitions"].as_array().unwrap();
    assert_eq!(transitions.len(),240);
    let all=(0..5).collect::<BTreeSet<_>>();
    let mut type14=0;let mut type23=0;
    for tr in transitions{
        let labels=tr["source_labels"].as_array().unwrap();
        let sa=sites(labels[0].as_str().unwrap());let sb=sites(labels[1].as_str().unwrap());
        assert!(sa.is_disjoint(&sb));assert_eq!(sa.union(&sb).copied().collect::<BTreeSet<_>>(),all);
        assert_eq!(boundary(&sa),boundary(&sb));
        match sa.len().min(sb.len()){1=>type14+=1,2=>type23+=1,_=>panic!()}
    }
    assert_eq!(type14,200);assert_eq!(type23,40);
    let packet=json!({
        "schema":"marici.benincasa.five_site.occurrence_kummer_characters.v1",
        "occurrence_generators":240,
        "partition_census":{"1|4":type14,"2|3":type23},
        "identity":"partial A and complement A^c have the identical labelled boundary-edge vector",
        "deck_action":"each of the five edge-sheet flips acts identically on q_A and q_Ac",
        "occurrence_kernel_C2_5_character":"trivial on all 240 generators",
        "cyclic_module":"Q[C5]^48 retained",
        "combined_module":"trivial(C2^5) tensor Q[C5]^48",
        "first_rees_symbols":"qhat_A-qhat_Ac=2*rho*X_A are edge-sheet independent and deck invariant",
        "soft_koszul_attachment":"C2^5-equivariant with trivial action on the occurrence/Koszul factors",
        "physical_measure_twist":"tensor separately with external-Gram Kummer character det(H)^(-1/2)",
        "new_edge_kummer_character":false,
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-occurrence-kummer-characters.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
