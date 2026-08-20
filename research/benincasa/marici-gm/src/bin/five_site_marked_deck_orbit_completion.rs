use serde_json::{json,Value};
use std::{collections::{BTreeMap,BTreeSet},fs};

fn active_edges(label:&str)->Vec<usize>{
    if label=="G"{return vec![]}
    if let Some(edge)=label.strip_prefix("G_minus_e"){
        return vec![edge.chars().next().unwrap().to_digit(10).unwrap() as usize-1]
    }
    let s=label.strip_prefix("g_").unwrap().chars().map(|c|c.to_digit(10).unwrap() as usize-1).collect::<BTreeSet<_>>();
    (0..5).filter(|e|s.contains(e)!=s.contains(&((e+1)%5))).collect()
}
fn main(){
    let src:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cycle=&src["five_cycle"];
    let mut labels=BTreeSet::new();
    for v in cycle["common_prefactor"].as_array().unwrap(){labels.insert(v.as_str().unwrap().to_string());}
    for term in cycle["terms"].as_array().unwrap(){for v in term.as_array().unwrap(){labels.insert(v.as_str().unwrap().to_string());}}
    assert_eq!(labels.len(),26);
    let mut profile=BTreeMap::<usize,usize>::new();
    let mut character_mult=vec![0_usize;32];
    let mut completed=0;
    for label in &labels{
        let active=active_edges(label); *profile.entry(active.len()).or_default()+=1;
        completed+=1_usize<<active.len();
        // The orbit permutation module contains once every character whose
        // support is a subset of the active edge set.
        for sub in 0..(1_usize<<active.len()){
            let mut mask=0;
            for (j,e) in active.iter().enumerate(){if(sub>>j)&1==1{mask|=1<<e;}}
            character_mult[mask]+=1;
        }
    }
    assert_eq!(profile.get(&0),Some(&1));assert_eq!(profile.get(&1),Some(&5));assert_eq!(profile.get(&2),Some(&20));
    assert_eq!(completed,91);assert_eq!(character_mult[0],26);
    for e in 0..5{assert_eq!(character_mult[1<<e],9);}
    for i in 0..5{for j in i+1..5{assert_eq!(character_mult[(1<<i)|(1<<j)],2);}}
    for (mask,m) in character_mult.iter().enumerate(){if mask.count_ones()>=3{assert_eq!(*m,0);}}
    assert_eq!(character_mult.iter().sum::<usize>(),91);
    let packet=json!({
        "schema":"marici.benincasa.five_site.marked_deck_orbit_completion.v1",
        "physical_positive_arrangement_size":26,
        "physical_arrangement_deck_stable":false,
        "orbit_profiles":[
            {"type":"total-energy G","count":1,"active_sheets":0,"orbit_size":1},
            {"type":"G-minus-edge","count":5,"active_sheets":1,"orbit_size":2},
            {"type":"proper connected partial energy","count":20,"active_sheets":2,"orbit_size":4}
        ],
        "orbit_completed_arrangement_size":completed,
        "C2_5_character_multiplicities":{
            "trivial":26,
            "each_single_edge_character":9,
            "each_two_edge_character":2,
            "weight_three_or_higher":0
        },
        "dimension_check":"26+5*9+10*2=91",
        "physical_positive_sections":"one non-invariant basis choice in each orbit, fixed by the Euclidean y_i>=0 chamber",
        "invariant_average":"canonical only after orbit completion; it changes the physical marked divisor and is not physical descent",
        "occurrence_kernel_contrast":"the complementary occurrence differences are deck trivial even though the full marked divisor is not deck stable",
        "classification":"sector-specific signed-energy coefficient completion over unchanged carrier",
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-marked-deck-orbit-completion.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
