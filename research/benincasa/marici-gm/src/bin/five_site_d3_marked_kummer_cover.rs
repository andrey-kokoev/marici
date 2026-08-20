use serde_json::{json, Value};
use std::{collections::{BTreeMap, BTreeSet}, fs};

fn facet_vector(label:&str)->(Vec<i32>,Vec<i32>){
    let mut x=vec![0;5]; let mut y=vec![0;5];
    if label=="G" { x.fill(1); return(x,y); }
    if let Some(edge)=label.strip_prefix("G_minus_e") {
        x.fill(1);
        let first=edge.chars().next().unwrap().to_digit(10).unwrap() as usize;
        y[first-1]=2; return(x,y);
    }
    let digits=label.strip_prefix("g_").unwrap();
    let sites=digits.chars().map(|c|c.to_digit(10).unwrap() as usize-1).collect::<BTreeSet<_>>();
    for &i in &sites{x[i]=1;}
    for e in 0..5{if sites.contains(&e)!=sites.contains(&((e+1)%5)){y[e]=1;}}
    (x,y)
}
fn linear_form(x:&[i32],y:&[i32])->String{
    let mut terms=Vec::new();
    for i in 0..5{if x[i]!=0{terms.push(if x[i]==1{format!("X{}",i+1)}else{format!("{}*X{}",x[i],i+1)});}}
    for i in 0..5{if y[i]!=0{terms.push(if y[i]==1{format!("y{}",i+1)}else{format!("{}*y{}",y[i],i+1)});}}
    terms.join("+")
}
fn main(){
    let src:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cycle=&src["five_cycle"];
    assert_eq!(cycle["term_count"].as_u64(),Some(180));
    assert_eq!(cycle["facet_count"].as_u64(),Some(26));
    let mut labels=BTreeSet::new();
    for v in cycle["common_prefactor"].as_array().unwrap(){labels.insert(v.as_str().unwrap().to_string());}
    for term in cycle["terms"].as_array().unwrap(){for v in term.as_array().unwrap(){labels.insert(v.as_str().unwrap().to_string());}}
    assert_eq!(labels.len(),26);
    let mut forms=BTreeMap::new();
    for label in labels {let(x,y)=facet_vector(&label);forms.insert(label,json!({"x":x,"y":y,"form":linear_form(&x,&y)}));}
    let packet=json!({
        "schema":"marici.benincasa.five_site.d3_marked_kummer_cover.v1",
        "physical_base":"three u-coordinates on a labelled det(H)!=0 Gram pivot",
        "routing_convention":"r1=0; r2=q1; r3=q2; r4=q3; r5=q4=sum c_i q_i; y_i^2=(ell-r_i)^2",
        "polynomial_radicals_after_clearing_detH":[
            "F1=u^T adj(H) u",
            "F2=F1-2 det(H) u1+det(H) h11",
            "F3=F1-2 det(H) u2+det(H) h22",
            "F4=F1-2 det(H) u3+det(H) h33",
            "F5=F1-2 det(H) c^T u+det(H) c^T H c"
        ],
        "cover_equations":"det(H)*y_i^2=F_i, i=1,...,5",
        "generic_cover_degree":32,
        "generic_deck_group":"C2^5 with five labelled sign characters",
        "physical_real_sheet":"y_i>=0 selected by the Euclidean loop chamber",
        "branch_support":"det(H)=0 or one of the five labelled edge-soft divisors F_i=0",
        "facet_count":26,
        "term_count":180,
        "all_marked_denominators":"linear in (X_i,y_i) on the Kummer cover; algebraic after forgetting y_i",
        "facet_forms":forms,
        "classification":"existing labelled energy/Cut carrier pulled back to a sector-specific multi-Kummer coefficient cover",
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-d3-marked-kummer-cover.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&json!({"facets":26,"terms":180,"cover_degree":32,"deck":"C2^5"})).unwrap());
}
