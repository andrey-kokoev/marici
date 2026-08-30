use serde_json::json;
use std::{collections::BTreeSet,fs};
use symbolica::prelude::*;
fn a(s:&str)->Atom{Atom::parse(s,"marici",Default::default()).unwrap().expand()}
fn wall(label:&str,t:&Atom,y:&[Atom])->Atom{
 if label=="G"{return a("6")*t.clone()}
 if let Some(edge)=label.strip_prefix("G_minus_e"){let i=edge.chars().next().unwrap().to_digit(10).unwrap() as usize-1;return (a("6")*t.clone()+a("2")*y[i].clone()).expand()}
 let sites=label.strip_prefix("g_").unwrap().chars().map(|c|c.to_digit(10).unwrap() as usize-1).collect::<BTreeSet<_>>();let mut q=a(&sites.len().to_string())*t.clone();
 for e in 0..6{if sites.contains(&e)!=sites.contains(&((e+1)%6)){q+=y[e].clone()}}q.expand()
}
fn main(){
 let gate:serde_json::Value=serde_json::from_str(&fs::read_to_string("../results/six-site-disjoint-pair-triple-source-gate.json").unwrap()).unwrap();assert_eq!(gate["containing_source_term_count"],9);
 let l=a("-2+x-6*z+4*v+w");let m=a("-6+2*x-6*z+5*v-w");
 let jacobian_minor=(l.derivative(symbol!("marici::x"))*m.derivative(symbol!("marici::w"))-l.derivative(symbol!("marici::w"))*m.derivative(symbol!("marici::x"))).expand();assert_ne!(jacobian_minor,a("0"));
 // One exact point on the reduced line, on the positive square-root sheet.
 let t=a("-1");let y=vec![a("33^(1/2)/3"),a("1"),a("1"),a("1"),a("3^(1/2)/3"),a("1")];
 let active=["g_12","g_34","g_56"];assert!(active.iter().all(|q|wall(q,&t,&y)==a("0")));
 let common=["G","g_1","g_2","g_3","g_4","g_5","g_6"];
 let mut records=Vec::new();
 for completion in gate["compatible_source_term_completions"].as_array().unwrap(){let extras=completion.as_array().unwrap().iter().map(|x|x.as_str().unwrap()).collect::<Vec<_>>();let uncut=common.iter().copied().chain(extras.iter().copied()).filter(|q|!active.contains(q)).collect::<Vec<_>>();let values=uncut.iter().map(|q|wall(q,&t,&y).factor()).collect::<Vec<_>>();assert!(values.iter().all(|x|*x!=a("0")));records.push(json!({"completion":extras,"uncut_walls":uncut,"positive_sheet_sample_values":values.iter().map(ToString::to_string).collect::<Vec<_>>(),"all_nonzero":true}));}
 let packet=json!({"schema":"marici.six_site_disjoint_pair_triple_excess_koszul.v1","exceptional_ideal":["L^2","M"],"L":l.to_string(),"M":m.to_string(),"independent_linear_forms":true,"jacobian_minor":jacobian_minor.to_string(),"regular_sequence":true,"koszul_homology":{"H2":0,"H1":0,"H0":"Q[x,v,w,z]/(L^2,M)"},"reduced_support":"Q[v,z]","cartier_basis":["1","L"],"cartier_length":2,"source_completion_count":9,"source_restriction_sample":{"z":1,"v":1,"x":"11/3","w":"1/3","t":-1,"sheet":"all positive square roots"},"source_restrictions":records,"all_nine_generically_nonzero":true,"new_carrier_datum":false,"scope":"algebraic/de Rham excess object; no separate Betti activation claim"});
 fs::write("../results/six-site-disjoint-pair-triple-excess-koszul.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();println!("{}",json!({"regular_sequence":true,"cartier_length":2,"source_maps_nonzero":9}));
}
