//! Dependency-free verifier for emitted remainder-monotonicity Taylor cells.
use std::{env,fs};
fn main(){
 let path=env::args().nth(1).unwrap_or_else(||"research/voevodsky/results/remainder_monotonicity_transition_interval.csv".into());
 let text=fs::read_to_string(&path).expect("read certificate");
 let mut prev:Option<f64>=None;let mut count=0usize;let mut weakest=f64::INFINITY;let mut start=0.0;let mut end=0.0;
 for line in text.lines().skip(1){
  if line.trim().is_empty(){continue} let v:Vec<f64>=line.split(',').map(|x|x.parse().expect("finite decimal")).collect();assert_eq!(v.len(),5);
  let(a,b,c,m,tail)=(v[0],v[1],v[2],v[3],v[4]);assert!(a.is_finite()&&b.is_finite()&&c.is_finite()&&m.is_finite()&&tail.is_finite());assert!(a<b&&m>=0.0&&tail>=0.0);
  if let Some(x)=prev{assert!((a-x).abs()<=16.0*f64::EPSILON*x.abs().max(1.0),"gap or overlap: {x} -> {a}")}else{start=a}
  let radius=(b-a)/2.0;let lower=c-radius*m-tail;assert!(lower>0.0,"Taylor cell failed [{a},{b}]: {lower}");weakest=weakest.min(lower);prev=Some(b);end=b;count+=1;
 }
 assert!(count>0);
 println!("{{\"schema\":\"marici.voevodsky.remainder-taylor-cover-rust.v1\",\"passed\":true,\"cells\":{count},\"interval\":[{start:.17},{end:.17}],\"weakest_lower\":{weakest:.17},\"input\":\"{path}\"}}");
}
