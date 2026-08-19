//! Modular divisibility census for the four fixed candidate denominators.
//! No symbolic factorization is used.
use serde_json::Value;
use std::collections::BTreeMap;
use std::fs;

#[cfg(not(feature="replication-prime"))] const P:u64=2_305_843_009_213_693_951;
#[cfg(feature="replication-prime")] const P:u64=2_305_843_009_213_693_921;
type Mon=(usize,usize); type Poly=BTreeMap<Mon,u64>;
fn sub(a:u64,b:u64)->u64{if a>=b{a-b}else{P-(b-a)}}
fn mul(a:u64,b:u64)->u64{((a as u128*b as u128)%P as u128)as u64}
fn pow(mut a:u64,mut n:u64)->u64{let mut r=1;while n>0{if n&1==1{r=mul(r,a)}a=mul(a,a);n>>=1}r}
fn inv(a:u64)->u64{pow(a,P-2)}
fn rational(s:&str)->u64{let mut q=s.split('/');let n:i128=q.next().unwrap().parse().unwrap();let d:u64=q.next().map(|x|x.parse().unwrap()).unwrap_or(1);let n=if n>=0{n as u64%P}else{sub(0,(-n)as u64%P)};mul(n,inv(d%P))}
fn mons(d:usize)->Vec<Mon>{(0..=d).flat_map(|s|(0..=s).map(move|i|(i,s-i))).collect()}
fn poly(values:&[Value],degree:usize)->Poly{mons(degree).into_iter().zip(values).filter_map(|(m,x)|{let c=rational(x.as_str().unwrap());(c!=0).then_some((m,c))}).collect()}
fn lead(p:&Poly)->Option<(Mon,u64)>{p.iter().max_by_key(|((i,j),_)|(i+j,*i,*j)).map(|(m,c)|(*m,*c))}
fn divisible(numerator:&Poly,denominator:&Poly)->bool{
    quotient(numerator,denominator).is_some()
}
fn quotient(numerator:&Poly,denominator:&Poly)->Option<Poly>{
    let mut r=numerator.clone();let Some(((di,dj),dc))=lead(denominator)else{return None};
    let mut out=Poly::new();
    while let Some(((ri,rj),rc))=lead(&r){
        if ri<di||rj<dj{return None}let m=(ri-di,rj-dj);let c=mul(rc,inv(dc));out.insert(m,c);
        for((i,j),q)in denominator{let target=(i+m.0,j+m.1);let value=sub(*r.get(&target).unwrap_or(&0),mul(c,*q));if value==0{r.remove(&target);}else{r.insert(target,value);}}
    }
    Some(out)
}
fn valuation(poly:&Poly,factor:&Poly)->usize{
    let mut value=poly.clone();let mut order=0;
    while let Some(next)=quotient(&value,factor){value=next;order+=1}
    order
}
fn quartic()->Poly{
    [((4,0),sub(0,1)),((3,1),4),((3,0),sub(0,4)),((2,1),sub(0,4)),((2,0),4),((1,1),sub(0,8)),((0,2),sub(0,4)),((1,0),16),((0,1),16),((0,0),sub(0,16))].into_iter().collect()
}
fn main(){
    let path=std::env::args().nth(1).unwrap_or_else(||"../marked-extension-charzero-candidate.json".into());let axis=std::env::var("MARICI_FACTOR_AXIS").unwrap_or_else(|_|"u".into());let master=std::env::var("MARICI_FACTOR_MASTER").ok().and_then(|x|x.parse().ok()).unwrap_or(0u64);
    let root:Value=serde_json::from_str(&fs::read_to_string(path).unwrap()).unwrap();let mut ds=Vec::new();let mut degrees=Vec::new();
    for row in 0..4u64{let e=root["entries"].as_array().unwrap().iter().find(|e|e["axis"].as_str()==Some(&axis)&&e["row"].as_u64()==Some(row)&&e["column"].as_u64()==Some(master)).unwrap();let d=e["denominator_degree"].as_u64().unwrap()as usize;degrees.push(d);ds.push(poly(e["denominator"].as_array().unwrap(),d));}
    let matrix:Vec<Vec<bool>>=(0..4).map(|i|(0..4).map(|j|divisible(&ds[i],&ds[j])).collect()).collect();
    let q=quartic();let mut q_orders=Vec::new();
    for row in 0..4u64{let e=root["entries"].as_array().unwrap().iter().find(|e|e["axis"].as_str()==Some(&axis)&&e["row"].as_u64()==Some(row)&&e["column"].as_u64()==Some(master)).unwrap();let nd=e["numerator_degree"].as_u64().unwrap()as usize;let n=poly(e["numerator"].as_array().unwrap(),nd);q_orders.push((valuation(&n,&q),valuation(&ds[row as usize],&q)));}
    println!("{{\"schema\":\"marici.nima.candidate_denominator_divisibility.v2\",\"prime\":{},\"axis\":\"{}\",\"master\":{},\"degrees\":{:?},\"row_denominator_divisible_by_column\":{:?},\"q_orders_num_den\":{:?}}}",P,axis,master,degrees,matrix,q_orders);
}
