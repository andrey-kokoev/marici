use num_bigint::BigInt;
use num_integer::Integer;
use num_traits::{One, Signed, ToPrimitive, Zero};
use serde_json::Value;
use std::fs;

fn egcd(a:i128,b:i128)->(i128,i128,i128){if b==0{(a,1,0)}else{let(g,x,y)=egcd(b,a%b);(g,y,x-(a/b)*y)}}
fn inv_mod(a:u64,p:u64)->u64{let(g,x,_)=egcd(a as i128,p as i128);assert_eq!(g,1);x.rem_euclid(p as i128)as u64}
fn crt(residues:&[(u64,u64)]) -> (BigInt,BigInt) {
    let mut x=BigInt::zero();let mut m=BigInt::one();
    for(r,p)in residues{let pb=BigInt::from(*p);let xm=x.mod_floor(&pb).to_u64().unwrap();let mm=m.mod_floor(&pb).to_u64().unwrap();let delta=((*r as i128-xm as i128).rem_euclid(*p as i128))as u64;let k=((delta as u128*inv_mod(mm,*p)as u128)%*p as u128)as u64;x+=&m*BigInt::from(k);m*=pb}
    (x,m)
}
fn ratrec(x:&BigInt,m:&BigInt)->Option<(BigInt,BigInt)>{
    let bound=(m/BigInt::from(2u8)).sqrt();let(mut r0,mut r1)=(m.clone(),x.clone());let(mut t0,mut t1)=(BigInt::zero(),BigInt::one());
    while r1.abs()>bound{let q=&r0/&r1;(r0,r1)=(r1.clone(),r0-&q*&r1);(t0,t1)=(t1.clone(),t0-q*t1)}
    if t1.is_zero()||t1.abs()>bound{return None}let(mut n,mut d)=(r1,t1);if d.is_negative(){n=-n;d=-d}if (&n-x*&d).mod_floor(m)!=BigInt::zero(){return None}Some((n,d))
}
fn coeffs(v:&Value,key:&str)->Vec<u64>{v[key].as_array().unwrap().iter().map(|x|x.as_u64().unwrap()).collect()}
fn main(){
    let packets:Vec<Value>=std::env::args().skip(1).map(|path|serde_json::from_str(&fs::read_to_string(path).unwrap()).unwrap()).collect();assert!(packets.len()>=2);let primes:Vec<u64>=packets.iter().map(|x|x["prime"].as_u64().unwrap()).collect();for i in 0..primes.len(){for j in 0..i{assert_ne!(primes[i],primes[j])}}
    let base=packets[0]["entries"].as_array().unwrap();assert_eq!(base.len(),24);let mut out=Vec::new();
    for(i,x)in base.iter().enumerate(){for packet in packets.iter().skip(1){let y=&packet["entries"][i];for key in ["axis","row","column","numerator_degree","denominator_degree"]{assert_eq!(x[key],y[key],"shape mismatch entry={i} key={key}")}}
        let mut lifted=Vec::new();for key in ["denominator","numerator"]{let vectors:Vec<Vec<u64>>=packets.iter().map(|packet|coeffs(&packet["entries"][i],key)).collect();for v in &vectors{assert_eq!(v.len(),vectors[0].len())}let z:Vec<String>=(0..vectors[0].len()).map(|j|{let rs:Vec<_>=vectors.iter().zip(&primes).map(|(v,p)|(v[j],*p)).collect();let(c,m)=crt(&rs);let(n,d)=ratrec(&c,&m).unwrap_or_else(||panic!("rational reconstruction failed entry={i} key={key} coefficient={j}"));if d==BigInt::one(){n.to_string()}else{format!("{n}/{d}")}}).collect();lifted.push(z)}
        out.push(format!("{{\"axis\":{},\"row\":{},\"column\":{},\"numerator_degree\":{},\"denominator_degree\":{},\"denominator\":{:?},\"numerator\":{:?}}}",x["axis"],x["row"],x["column"],x["numerator_degree"],x["denominator_degree"],lifted[0],lifted[1]))}
    let product=primes.iter().fold(BigInt::one(),|z,p|z*BigInt::from(*p));println!("{{\"schema\":\"marici.benincasa.marked_extension_crt_lift.v2\",\"reconstruction_primes\":{:?},\"modulus_product\":\"{}\",\"certification_status\":\"modular_candidate_exact_source_substitution_pending\",\"entries\":[{}]}}",primes,product,out.join(","));
}
