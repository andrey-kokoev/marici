use serde_json::json;
use std::fs;

fn rotate(label:&str,shift:usize)->String{
    if label=="G"{return label.to_owned();}
    if let Some(edge)=label.strip_prefix("G_minus_e"){
        let digits=edge.chars().map(|c|(c.to_digit(10).unwrap() as usize-1+shift)%5+1).collect::<Vec<_>>();
        return format!("G_minus_e{}{}",digits[0],digits[1]);
    }
    let mut sites=label.strip_prefix("g_").unwrap().chars().map(|c|(c.to_digit(10).unwrap() as usize-1+shift)%5+1).collect::<Vec<_>>();
    sites.sort();format!("g_{}",sites.iter().map(ToString::to_string).collect::<String>())
}
fn base_sign(label:&str)->i8{match label{
    "G"=>-1,"g_1"|"g_2"|"g_3"|"g_4"=>1,"g_12"|"g_34"|"g_5"=>0,
    "G_minus_e23"|"G_minus_e45"|"G_minus_e51"|"g_125"|"g_345"|"g_1234"=>-1,
    _=>panic!("unexpected inverse-transported wall {label}")}}

fn main(){
    let source:serde_json::Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let pairing:serde_json::Value=serde_json::from_str(&fs::read_to_string("../results/five-site-cyclic-triple-d4-iepsilon-pairing.json").unwrap()).unwrap();
    assert_eq!(pairing["picard_lefschetz_intersection_absolute_value"],1);
    let common=source["five_cycle"]["common_prefactor"].as_array().unwrap();
    let base=["g_12","g_34","g_5"];
    let mut orbit=Vec::new();
    for shift in 0..5{
        let active=base.iter().map(|label|rotate(label,shift)).collect::<Vec<_>>();
        let inverse=(5-shift)%5;let mut containing=Vec::new();
        for (index,term) in source["five_cycle"]["terms"].as_array().unwrap().iter().enumerate(){
            let walls=common.iter().chain(term.as_array().unwrap()).map(|value|value.as_str().unwrap()).collect::<Vec<_>>();
            if active.iter().all(|active|walls.contains(&active.as_str())){
                let sign=walls.iter().filter(|wall|!active.iter().any(|active|active==**wall))
                    .map(|wall|base_sign(&rotate(wall,inverse))).product::<i8>();
                assert_eq!(sign,-1);containing.push(index);
            }
        }
        assert_eq!(containing.len(),8);
        orbit.push(json!({"shift":shift,"active_walls":active,"containing_source_terms":containing,
            "source_term_count":8,"common_local_residue_sign":-1,"positive_regulator_pairing":true,
            "local_intersection_absolute_value":1}));
    }
    assert_eq!(orbit.iter().map(|row|row["active_walls"].to_string()).collect::<std::collections::BTreeSet<_>>().len(),5);
    let packet=json!({"schema":"marici.five_site_cyclic_triple_d4_activation_orbit.v1","orbit_group":"C5",
        "orbit_size":5,"records":orbit,"character_on_labelled_occurrences":{"identity":5,"nonidentity":0},
        "claim":"the activated D4 fold forms one free five-occurrence physical singularity orbit","new_carrier_datum":false});
    fs::write("../results/five-site-cyclic-triple-d4-activation-orbit.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",json!({"orbit_size":5,"source_terms_per_occurrence":8,"intersection_absolute_value":1}));
}
