use serde_json::{json,Value};
use std::{collections::BTreeMap,fs};

fn kind(label:&str)->&'static str {
    if label=="G"{"T"} else if label.starts_with("G_minus_e"){"M1"} else {"A"}
}
fn pair_class(left:&str,right:&str,left_support:&[usize],right_support:&[usize])->&'static str {
    let lk=kind(left); let rk=kind(right);
    if lk=="T"||rk=="T" { return "t_zero"; }
    let overlap=left_support.iter().filter(|x|right_support.contains(x)).count();
    if lk=="A"&&rk=="A" {
        if overlap==2 {"t_zero"} else {"unit"}
    } else if (lk=="M1"&&rk=="A")||(lk=="A"&&rk=="M1") {
        if overlap==1 {"old_threshold"} else {"unit"}
    } else {
        panic!("pair type absent from the frozen source census: {left}|{right}")
    }
}

fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-site-compatible-landau-subsets.json").unwrap()).unwrap();
    let triple=source["census"].as_array().unwrap().iter().find(|x|x["active_wall_count"]==3).unwrap();
    let records=triple["representative_records"].as_array().unwrap();
    assert_eq!(records.len(),242);
    let mut counts:BTreeMap<String,usize>=BTreeMap::new();
    let mut output=Vec::new();
    for record in records {
        let labels=record["representative"].as_array().unwrap();
        let supports=record["cut_supports"].as_array().unwrap().iter().map(|support|support.as_array().unwrap().iter().map(|x|x.as_u64().unwrap() as usize).collect::<Vec<_>>()).collect::<Vec<_>>();
        let mut pair_classes=Vec::new();
        for (i,j) in [(0usize,1usize),(0,2),(1,2)] {
            pair_classes.push(json!({"pair":[labels[i].as_str().unwrap(),labels[j].as_str().unwrap()],"class":pair_class(labels[i].as_str().unwrap(),labels[j].as_str().unwrap(),&supports[i],&supports[j])}));
        }
        let has_unit=pair_classes.iter().any(|x|x["class"]=="unit");
        let has_t_zero=pair_classes.iter().any(|x|x["class"]=="t_zero");
        let inherited=if has_unit&&has_t_zero {"unit_and_t_zero_subpairs"}
            else if has_unit {"unit_subpair_only"}
            else if has_t_zero {"t_zero_subpair_only"}
            else {"unresolved"};
        *counts.entry(inherited.to_owned()).or_default()+=1;
        output.push(json!({"representative":record["representative"],"profile":record["profile"],"pair_classes":pair_classes,"inherited_class":inherited,"source_term_multiplicity":record["source_term_multiplicity"]}));
    }
    assert_eq!(*counts.get("unresolved").unwrap_or(&0),0);
    let packet=json!({
        "schema":"marici.benincasa.five_site.triple_landau_inheritance.v1",
        "source_triple_orbits":242,"source_labelled_triples":1210,
        "classification":["unit_and_t_zero_subpairs","unit_subpair_only","t_zero_subpair_only","unresolved"],
        "orbit_counts":counts,"records":output,
        "conclusion":"every compatible triple inherits either an impossible unit pair or total-energy support; no genuine three-wall stationarity system remains"
    });
    fs::write("../results/five-site-triple-landau-inheritance.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&json!({"orbit_counts":packet["orbit_counts"],"source_triple_orbits":242})).unwrap());
}
