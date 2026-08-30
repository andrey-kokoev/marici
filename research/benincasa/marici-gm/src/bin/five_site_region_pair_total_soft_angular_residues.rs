use serde_json::{json,Value};
use std::{collections::BTreeSet,fs};
use symbolica::prelude::*;

fn a(s:&str)->Atom { Atom::parse(s,"marici",Default::default()).unwrap() }

fn cuts(label:&str)->Vec<usize>{
    let sites:BTreeSet<usize>=label[2..].chars().map(|c|c.to_digit(10).unwrap() as usize-1).collect();
    (0..5).filter(|&e|sites.contains(&e)!=sites.contains(&((e+1)%5))).collect()
}

fn wall(label:&str)->Atom{
    if label=="G" { return a("5*t"); }
    if label.starts_with("G_minus_e") {
        let e=label[9..10].parse::<usize>().unwrap();
        return a(&format!("5*t+2*y{}",e));
    }
    let n=label[2..].len();
    let mut z=a(&format!("{}*t",n));
    for e in cuts(label){ z+=a(&format!("y{}",e+1)); }
    z.expand()
}

fn solve_wall(label:&str)->(Atom,Atom){
    if label=="G" { return (a("t"),a("0")); }
    if label.starts_with("G_minus_e") {
        let e=label[9..10].parse::<usize>().unwrap();
        return (a(&format!("y{}",e)),a("-5*t/2"));
    }
    let cs=cuts(label); let pivot=cs[0];
    let mut rhs=a(&format!("-{}*t",label[2..].len()));
    for &e in &cs[1..]{rhs-=a(&format!("y{}",e+1));}
    (a(&format!("y{}",pivot+1)),rhs.expand())
}

fn restrict_active(x:Atom)->Atom{
    x.replace(a("y5").to_pattern()).with(a("-3*t-y3").to_pattern())
     .replace(a("y4").to_pattern()).with(a("-3*t-y2").to_pattern())
     .together().cancel().expand()
}

fn solve_restricted(label:&str)->(Atom,Atom){
    match label{
        "G"=>(a("t"),a("0")),
        "G_minus_e34"=>(a("y3"),a("-5*t/2")),
        "G_minus_e45"=>(a("y2"),a("-t/2")),
        "g_1"=>(a("y1"),a("y3+2*t")),
        "g_2"=>(a("y1"),a("-t-y2")),
        "g_3"=>(a("y3"),a("-t-y2")),
        "g_4"=>(a("y3"),a("y2+2*t")),
        "g_5"=>(a("y3"),a("-5*t-y2")),
        "g_12"|"g_1235"=>(a("y3"),a("y2-t")),
        "g_1234"=>(a("y3"),a("-2*t-y2")),
        "g_1245"=>(a("y3"),a("-4*t-y2")),
        _=>panic!("unexpected residual label {label}")
    }
}

fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cyc=&source["five_cycle"];
    let common=cyc["common_prefactor"].as_array().unwrap();
    let mut sum=a("0"); let mut labels=BTreeSet::new(); let mut count=0usize;
    for term in cyc["terms"].as_array().unwrap(){
        let ts:Vec<&str>=term.as_array().unwrap().iter().map(|x|x.as_str().unwrap()).collect();
        if !(ts.contains(&"g_123")&&ts.contains(&"g_125")){continue;}
        count+=1; let mut den=a("1");
        for x in common.iter().map(|x|x.as_str().unwrap()).chain(ts.iter().copied().filter(|x|*x!="g_123"&&*x!="g_125")){
            labels.insert(x.to_string()); den*=wall(x);
        }
        sum+=a("1")/den;
    }
    assert_eq!(count,10);
    let combined=sum.together().cancel();
    let mut records=Vec::new(); let mut surviving=Vec::new();
    for label in labels.iter(){
        let w=wall(&label); let (var,repl)=solve_wall(&label);
        let residue=(combined.clone()*w).together().cancel()
            .replace(var.to_pattern()).with(repl.to_pattern()).together().cancel();
        let nonzero=residue!=a("0");
        if nonzero{surviving.push(label.clone());}
        records.push(json!({"label":label,"simple_residue_nonzero":nonzero,"residue_expression":residue.factor().to_string()}));
    }
    let restricted=restrict_active(combined.clone());
    let mut restricted_records=Vec::new();
    for label in labels.iter(){
        let w=restrict_active(wall(label)); let (var,repl)=solve_restricted(label);
        let simple=(restricted.clone()*w.clone()).together().cancel()
            .replace(var.to_pattern()).with(repl.to_pattern()).together().cancel();
        let double=(restricted.clone()*w.clone()*w).together().cancel()
            .replace(var.to_pattern()).with(repl.to_pattern()).together().cancel();
        restricted_records.push(json!({
            "label":label,
            "restricted_linear_form":restrict_active(wall(label)).factor().to_string(),
            "simple_residue_nonzero":simple!=a("0"),
            "double_leading_nonzero":double!=a("0"),
            "simple_residue_expression":simple.factor().to_string(),
            "double_leading_expression":double.factor().to_string()
        }));
    }
    let packet=json!({
        "schema":"marici.five_site_region_pair_total_soft_angular_residues.v1",
        "representative":["g_123","g_125"],
        "source_term_count":count,
        "candidate_facet_count":records.len(),
        "surviving_simple_pole_count":surviving.len(),
        "surviving_simple_poles":surviving,
        "records":records,
        "combined_expression":combined.factor().to_string(),
        "active_restriction":["y5=-3*t-y3","y4=-3*t-y2"],
        "restricted_expression":restricted.factor().to_string(),
        "restricted_records":restricted_records,
        "restricted_coincidence":"g_1235|active = -g_12|active",
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-region-pair-total-soft-angular-residues.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",json!({"source_term_count":count,"candidate_facet_count":packet["candidate_facet_count"],"surviving_simple_pole_count":packet["surviving_simple_pole_count"],"surviving_simple_poles":packet["surviving_simple_poles"]}));
}
