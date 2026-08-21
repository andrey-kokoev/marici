use serde_json::{json,Value};
use std::{collections::BTreeSet,fs};

fn rotate_mask(mask:usize)->usize{((mask<<1)&31)|(mask>>4)}
fn cut_support(label:&str)->Vec<usize>{
    let sites=label.strip_prefix("g_").unwrap().chars().map(|d|d.to_digit(10).unwrap()as usize-1).collect::<BTreeSet<_>>();
    (0..5).filter(|e|sites.contains(e)!=sites.contains(&((e+1)%5))).collect()
}
fn grows(label:&str,mask:usize)->usize{if label=="G"{0}else if label.starts_with("G_minus_e"){1}else{
    let c=cut_support(label);usize::from(((mask>>c[0])&1)==((mask>>c[1])&1))}}
fn rotate_label(label:&str)->String{
    if label=="G"{return label.to_owned();}
    if let Some(edge)=label.strip_prefix("G_minus_e"){
        let digits=edge.chars().map(|d|(d.to_digit(10).unwrap()%5+1)as u8).collect::<Vec<_>>();
        return format!("G_minus_e{}{}",digits[0],digits[1]);
    }
    let mut digits=label.strip_prefix("g_").unwrap().chars().map(|d|(d.to_digit(10).unwrap()%5+1)as u8).collect::<Vec<_>>();
    digits.sort();format!("g_{}",digits.into_iter().map(|d|char::from(b'0'+d)).collect::<String>())
}
fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cycle=&source["five_cycle"];
    let common=cycle["common_prefactor"].as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect::<Vec<_>>();
    let terms=cycle["terms"].as_array().unwrap().iter().map(|t|t.as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect::<Vec<_>>()).collect::<Vec<Vec<String>>>();
    let labels=common.iter().chain(terms.iter().flatten()).cloned().collect::<BTreeSet<_>>();
    let mut failures=Vec::new();
    for label in &labels{let rotated=rotate_label(label);if !labels.contains(&rotated){failures.push(json!({"kind":"label_closure","label":label,"rotated":rotated}));continue;}
        for mask in 0..32{if grows(label,mask)!=grows(&rotated,rotate_mask(mask)){failures.push(json!({"kind":"growth_naturality","label":label,"mask":mask}));}}
    }
    let term_set=terms.iter().map(|t|{let mut s=t.clone();s.sort();s}).collect::<BTreeSet<_>>();
    let term_failures=terms.iter().filter(|t|{let mut r=t.iter().map(|x|rotate_label(x)).collect::<Vec<_>>();r.sort();!term_set.contains(&r)}).count();
    let packet=json!({"schema":"marici.benincasa.five_site.cyclic_boundary_naturality.v1","label_count":labels.len(),"sheet_count":32,
        "label_sheet_checks":labels.len()*32,"growth_failures":failures,"term_count":terms.len(),"term_rotation_failures":term_failures,
        "orientation_weights_all_one":cycle["orientation_normalized_term_weights"].as_array().unwrap().iter().all(|x|x.as_i64()==Some(1)),
        "commutes":failures.is_empty()&&term_failures==0});
    fs::write("../results/five-site-cyclic-boundary-naturality.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();println!("{}",serde_json::to_string(&packet).unwrap());
}
