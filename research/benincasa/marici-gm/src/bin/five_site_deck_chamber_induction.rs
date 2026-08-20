use serde_json::{json,Value};
use std::{collections::{BTreeMap,BTreeSet},fs};

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
fn key(x:&[i32],y:&[i32])->String{format!("{:?}|{:?}",x,y)}
fn main(){
    let src:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cyc=&src["five_cycle"];let mut labels=BTreeSet::new();
    for v in cyc["common_prefactor"].as_array().unwrap(){labels.insert(v.as_str().unwrap().to_string());}
    for t in cyc["terms"].as_array().unwrap(){for v in t.as_array().unwrap(){labels.insert(v.as_str().unwrap().to_string());}}
    let base=labels.iter().map(|l|vector(l)).collect::<Vec<_>>();assert_eq!(base.len(),26);
    let mut presentations=BTreeSet::new();let mut incidence=BTreeMap::<String,usize>::new();
    for mask in 0..32{
        let mut arrangement=Vec::new();
        for(x,y)in &base{
            let ys=(0..5).map(|e|if(mask>>e)&1==1{-y[e]}else{y[e]}).collect::<Vec<_>>();
            let k=key(x,&ys);*incidence.entry(k.clone()).or_default()+=1;arrangement.push(k);
        }
        arrangement.sort();presentations.insert(arrangement.join(";"));
    }
    assert_eq!(presentations.len(),32);assert_eq!(incidence.len(),91);
    let mut mult=BTreeMap::<usize,usize>::new();for n in incidence.values(){*mult.entry(*n).or_default()+=1;}
    assert_eq!(mult.get(&32),Some(&1));assert_eq!(mult.get(&16),Some(&10));assert_eq!(mult.get(&8),Some(&80));
    assert_eq!(incidence.values().sum::<usize>(),32*26);
    let packet=json!({
        "schema":"marici.benincasa.five_site.deck_chamber_induction.v1",
        "deck_group":"C2^5",
        "physical_arrangement_stabilizer":"trivial",
        "distinct_chamber_presentations":32,
        "sections_per_presentation":26,
        "total_section_occurrences":832,
        "distinct_sections_in_union":91,
        "union_incidence_multiplicities":[
            {"section_type":"total energy","distinct":1,"presentations_each":32},
            {"section_type":"signed G-minus-edge","distinct":10,"presentations_each":16},
            {"section_type":"signed partial energy","distinct":80,"presentations_each":8}
        ],
        "equivariant_physical_object":"Ind_1^(C2^5) M_phys = direct_sum_g M_g",
        "invariants":"evaluation at the identity chamber identifies the invariant compatible tuples with M_phys after labelled deck transports are retained",
        "union_object":"cohomology of the complement of all 91 walls; obtained by additional localization and not equal to the induced chamber package",
        "canonical_map":"restriction from each chamber complement to the 91-wall complement; no inverse without extra data",
        "warning":"orbit induction is not orbit-union localization",
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-deck-chamber-induction.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
