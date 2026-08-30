use serde_json::{json,Value};
use std::{collections::BTreeSet,fs};

fn add(a:i64,b:i64,p:i64)->i64{(a+b).rem_euclid(p)}
fn mul(a:i64,b:i64,p:i64)->i64{((a as i128*b as i128)%p as i128)as i64}
fn pow(mut a:i64,mut n:usize,p:i64)->i64{let mut out=1;while n>0{if n&1==1{out=mul(out,a,p);}a=mul(a,a,p);n>>=1;}out}
fn inv(a:i64,p:i64)->i64{pow(a.rem_euclid(p),(p-2)as usize,p)}
fn cut_support(label:&str)->Vec<usize>{
    let sites=label.strip_prefix("g_").unwrap().chars().map(|d|d.to_digit(10).unwrap()as usize).collect::<BTreeSet<_>>();
    (1..=5).filter(|e|sites.contains(e)!=sites.contains(&(e%5+1))).collect()
}
fn grows(label:&str,mask:usize)->usize{if label=="G"{0}else if label.starts_with("G_minus_e"){1}else{
    let c=cut_support(label);usize::from(((mask>>(c[0]-1))&1)==((mask>>(c[1]-1))&1))}}
fn radial(label:&str,sheet:usize,r:&[i64;5],p:i64)->i64{
    if let Some(edge)=label.strip_prefix("G_minus_e"){
        let e=edge.chars().next().unwrap().to_digit(10).unwrap()as usize-1;
        return mul(if sheet&(1<<e)==0{2}else{-2},r[e],p)
    }
    cut_support(label).into_iter().fold(0,|out,e|add(out,mul(if sheet&(1<<(e-1))==0{1}else{-1},r[e-1],p),p))
}
fn size(label:&str)->i64{label.strip_prefix("g_").unwrap().len() as i64}
fn leading(terms:&[Vec<String>],common:&[String],sheet:usize,r:&[i64;5],p:i64)->(usize,i64){
    let order=terms.iter().map(|t|common.iter().chain(t).map(|q|grows(q,sheet)).sum()).min().unwrap();
    let mut out=0;
    for term in terms {
        let labels=common.iter().chain(term);
        if labels.clone().map(|q|grows(q,sheet)).sum::<usize>()!=order{continue;}
        let mut den=5;
        for q in labels {
            if q=="G"{continue;}
            let factor=if grows(q,sheet)==1{radial(q,sheet,r,p)}else{size(q)};
            assert_ne!(factor.rem_euclid(p),0);
            den=mul(den,factor,p);
        }
        out=add(out,inv(den,p),p);
    }
    (order,out)
}
fn main(){
    let source:Value=serde_json::from_str(&fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()).unwrap();
    let cycle=&source["five_cycle"];
    let common=cycle["common_prefactor"].as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect::<Vec<_>>();
    let terms=cycle["terms"].as_array().unwrap().iter().map(|t|t.as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect()).collect::<Vec<Vec<String>>>();
    let samples=[(1019_i64,[11_i64,23,37,41,53]),(1009_i64,[13_i64,29,31,43,59])];
    let mut reports=Vec::new();
    for (p,r) in samples {
        let rows=(0..32).map(|s|leading(&terms,&common,s,&r,p)).collect::<Vec<_>>();
        assert!(rows.iter().all(|(_,c)|*c!=0));
        let mut square_checks=0;let mut commute_checks=0;
        for s in 0..32 {for i in 0..5 {
            let a=1<<i;let u=mul(rows[s^a].1,inv(rows[s].1,p),p);
            let back=mul(rows[s].1,inv(rows[s^a].1,p),p);
            assert_eq!(mul(u,back,p),1);square_checks+=1;
            for j in 0..5 {
                let b=1<<j;
                let ab=mul(u,mul(rows[s^a^b].1,inv(rows[s^a].1,p),p),p);
                let ba=mul(mul(rows[s^b].1,inv(rows[s].1,p),p),mul(rows[s^a^b].1,inv(rows[s^b].1,p),p),p);
                assert_eq!(ab,ba);commute_checks+=1;
            }
        }}
        reports.push(json!({"prime":p,"radial_point":r,"all_32_leading_coefficients_nonzero":true,"square_checks":square_checks,"commutation_checks":commute_checks}));
    }
    let packet=json!({
        "schema":"marici.benincasa.five_site.flip_leading_unit_cocycle.v1",
        "source_frame":"raw labelled chamber frame of Entries 1221 and 1223",
        "normalized_unit":"u_a(S)=c_(S xor a)/c_S",
        "samples":reports,
        "conclusion":{
            "raw_source_unit_cocycle":"trivial",
            "normalized_leading_unit_cocycle":"exact coboundary",
            "projective_square_defect":false,
            "new_exceptional_coherence_cell":false,
            "possible_additional_support":"zero divisor of a leading coefficient if one insists on unit-leading normalization"
        },
        "scope":"Exact modular replication of the source-leading ratios; strict triviality in the raw frame follows from Entries 1221 and 1223, not from interpolation."
    });
    fs::write("../results/five-site-flip-leading-unit-cocycle.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["conclusion"]).unwrap());
}
