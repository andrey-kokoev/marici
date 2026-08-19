use num_bigint::BigInt;
use num_integer::Integer;
use num_traits::ToPrimitive;
use serde_json::Value;
use std::collections::BTreeMap;
use std::fs;

fn add(a:u64,b:u64,p:u64)->u64{((a as u128+b as u128)%p as u128)as u64}
fn mul(a:u64,b:u64,p:u64)->u64{((a as u128*b as u128)%p as u128)as u64}
fn pow(mut a:u64,mut n:u64,p:u64)->u64{let mut r=1;while n>0{if n&1==1{r=mul(r,a,p)}a=mul(a,a,p);n>>=1;}r}
fn inv(a:u64,p:u64)->u64{pow(a,p-2,p)}
fn mons(d:usize)->Vec<(usize,usize)>{(0..=d).flat_map(|s|(0..=s).map(move|i|(i,s-i))).collect()}
fn parse_q(s:&str,p:u64)->u64{let mut q=s.split('/');let n:BigInt=q.next().unwrap().parse().unwrap();let d:BigInt=q.next().unwrap_or("1").parse().unwrap();assert!(q.next().is_none());let pb=BigInt::from(p);let nr=n.mod_floor(&pb).to_u64().unwrap();let dr=d.mod_floor(&pb).to_u64().unwrap();mul(nr,inv(dr,p),p)}
fn eval(cs:&Value,d:usize,u:u64,v:u64,p:u64)->u64{cs.as_array().unwrap().iter().zip(mons(d)).fold(0,|z,(c,(i,j))|add(z,mul(parse_q(c.as_str().unwrap(),p),mul(pow(u,i as u64,p),pow(v,j as u64,p),p),p),p))}
fn main(){let mut args=std::env::args().skip(1);let candidate:Value=serde_json::from_str(&fs::read_to_string(args.next().expect("candidate packet")).unwrap()).unwrap();let samples:Value=serde_json::from_str(&fs::read_to_string(args.next().expect("held-out packet")).unwrap()).unwrap();let p=samples["prime"].as_u64().unwrap();let mut expected=BTreeMap::new();for q in samples["wall_quotient_blocks"].as_array().unwrap(){let axis=q["axis"].as_str().unwrap();let u=q["u"].as_u64().unwrap();let v=q["v"].as_u64().unwrap();let m=q["fixed_extension_e6_e9_mod_p"].as_array().unwrap();for(row,r)in m.iter().enumerate(){for(col,x)in r.as_array().unwrap().iter().enumerate(){expected.insert((axis.to_owned(),row,col,u,v),x.as_u64().unwrap());}}}let mut checked=0;for e in candidate["entries"].as_array().unwrap(){let axis=e["axis"].as_str().unwrap();let row=e["row"].as_u64().unwrap()as usize;let col=e["column"].as_u64().unwrap()as usize;let dn=e["numerator_degree"].as_u64().unwrap()as usize;let dd=e["denominator_degree"].as_u64().unwrap()as usize;for((a,r,c,u,v),want)in &expected{if a==axis&&*r==row&&*c==col{let n=eval(&e["numerator"],dn,*u,*v,p);let d=eval(&e["denominator"],dd,*u,*v,p);assert_ne!(d,0);assert_eq!(n,mul(*want,d,p),"held-out mismatch {axis}[{row},{col}] at ({u},{v})");checked+=1}}}println!("{{\"schema\":\"marici.benincasa.marked_extension_heldout_verify.v1\",\"prime\":{},\"checked_values\":{},\"all_equal\":true}}",p,checked)}
