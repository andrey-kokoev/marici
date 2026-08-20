//! Nima-owned bounded polynomial-module witness search.
//!
//! This deliberately avoids a rational-function RREF section.  It evaluates
//! the frozen 132 source identities over a prime field and solves directly
//! for polynomial coefficient functions while retaining configurable exact
//! sector freedom.  A successful modular pilot is discovery evidence only;
//! characteristic-zero certification still requires reconstructing the
//! witness and checking every cleared identity exactly.

mod source {
    #![allow(dead_code)]
    include!("marked_relative_reduction_engine.rs");

    pub struct EvaluatedSystem {
        pub prime: u64,
        pub matrix: Vec<Vec<u64>>,
        pub rhs: Vec<u64>,
    }

    fn polynomials(g:&Geometry, master:usize)->(Vec<Poly>,Poly){
        let cs = classes(&g);
        let mut cols: Vec<Poly> = cs.iter().map(|q| common(&g, q)).collect();
        for (sa, sb) in [(1, 1), (1, 0), (0, 1), (0, 0)] {
            for m in monomials(8) {
                cols.push(exact(&g, sa, sb, m, false));
                cols.push(exact(&g, sa, sb, m, true));
            }
        }
        assert_eq!(cols.len(), 372);
        let rhs_poly = target(&g, &cs[master]);
        (cols,rhs_poly)
    }

    pub fn evaluated_system(u: u64, v: u64, axis: char, master: usize) -> EvaluatedSystem {
        let g = geometry(u, v, axis);
        let (cols,rhs_poly)=polynomials(&g,master);
        let generic=geometry(7,11,axis);
        let (generic_cols,generic_rhs)=polynomials(&generic,master);
        let mut mons = BTreeSet::new();
        for col in &generic_cols { mons.extend(col.0.keys().copied()); }
        mons.extend(generic_rhs.0.keys().copied());
        let mons: Vec<_> = mons.into_iter().collect();
        assert_eq!(mons.len(), 132);
        let matrix = mons.iter().map(|m| cols.iter()
            .map(|q| q.0.get(m).copied().unwrap_or(F::z()).0)
            .collect()).collect();
        let rhs = mons.iter().map(|m| rhs_poly.0.get(m).copied().unwrap_or(F::z()).0).collect();
        EvaluatedSystem { prime: P, matrix, rhs }
    }
}

use serde_json::Value;
use std::fs;

fn add(a: u64, b: u64, p: u64) -> u64 { ((a as u128 + b as u128) % p as u128) as u64 }
fn sub(a: u64, b: u64, p: u64) -> u64 { if a >= b { a - b } else { p - (b - a) } }
fn mul(a: u64, b: u64, p: u64) -> u64 { ((a as u128 * b as u128) % p as u128) as u64 }
fn pow(mut a: u64, mut n: u64, p: u64) -> u64 { let mut r=1; while n>0 { if n&1==1 {r=mul(r,a,p)} a=mul(a,a,p); n>>=1 } r }
fn inv(a: u64, p: u64) -> u64 { assert_ne!(a,0); pow(a,p-2,p) }

fn monomials(degree: usize) -> Vec<(usize, usize)> {
    (0..=degree).flat_map(|s| (0..=s).map(move |i| (i, s-i))).collect()
}

fn monomial_values(u: u64, v: u64, mons: &[(usize,usize)], p: u64) -> Vec<u64> {
    mons.iter().map(|(i,j)| mul(pow(u,*i as u64,p),pow(v,*j as u64,p),p)).collect()
}

fn rational_mod(text: &str, p: u64) -> u64 {
    let mut fields=text.split('/');
    let n: i128=fields.next().unwrap().parse().unwrap();
    let d: u64=fields.next().map(|x|x.parse().unwrap()).unwrap_or(1);
    assert!(fields.next().is_none());
    let nm=if n>=0 {(n as u128 % p as u128) as u64} else {sub(0,((-n) as u128%p as u128)as u64,p)};
    mul(nm,inv(d%p,p),p)
}

#[derive(Clone)]
struct Candidate { numerator_degree:usize, denominator_degree:usize, numerator:Vec<String>, denominator:Vec<String> }

fn load_candidates(path:&str, axis:&str, master:usize)->Vec<Candidate> {
    let root:Value=serde_json::from_str(&fs::read_to_string(path).unwrap()).unwrap();
    let mut out=Vec::new();
    for row in 0..4 {
        let entry=root["entries"].as_array().unwrap().iter().find(|e|
            e["axis"].as_str()==Some(axis) && e["row"].as_u64()==Some(row) && e["column"].as_u64()==Some(master as u64)
        ).expect("candidate entry");
        out.push(Candidate{
            numerator_degree:entry["numerator_degree"].as_u64().unwrap()as usize,
            denominator_degree:entry["denominator_degree"].as_u64().unwrap()as usize,
            numerator:entry["numerator"].as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect(),
            denominator:entry["denominator"].as_array().unwrap().iter().map(|x|x.as_str().unwrap().to_owned()).collect(),
        });
    }
    out
}

fn eval_candidate(c:&Candidate,u:u64,v:u64,p:u64)->Option<u64>{
    let nmons=monomials(c.numerator_degree); let dmons=monomials(c.denominator_degree);
    assert_eq!(nmons.len(),c.numerator.len()); assert_eq!(dmons.len(),c.denominator.len());
    let nv=monomial_values(u,v,&nmons,p); let dv=monomial_values(u,v,&dmons,p);
    let n=nv.iter().zip(&c.numerator).fold(0,|z,(m,q)|add(z,mul(*m,rational_mod(q,p),p),p));
    let d=dv.iter().zip(&c.denominator).fold(0,|z,(m,q)|add(z,mul(*m,rational_mod(q,p),p),p));
    (d!=0).then(||mul(n,inv(d,p),p))
}

fn allowed_columns(exact_degree:usize)->Vec<usize>{
    let mut out:Vec<usize>=(0..12).collect(); let mut column=12;
    for _stratum in 0..4 { for degree in 0..=8 { for _ in 0..2*(degree+1) { if degree<=exact_degree {out.push(column)} column+=1; } } }
    assert_eq!(column,372); out
}

fn solve(mut a:Vec<Vec<u64>>, variables:usize, p:u64)->Option<(Vec<u64>,usize)>{
    let rows=a.len(); let mut pivots=Vec::new(); let mut r=0;
    for c in 0..variables {
        let Some(q)=(r..rows).find(|i|a[*i][c]!=0) else {continue};
        a.swap(r,q); let z=inv(a[r][c],p); for j in c..=variables {a[r][j]=mul(a[r][j],z,p)}
        for i in r+1..rows { if a[i][c]!=0 {let z=a[i][c]; for j in c..=variables {a[i][j]=sub(a[i][j],mul(z,a[r][j],p),p)}} }
        pivots.push((r,c)); r+=1; if r==rows {break}
    }
    if (r..rows).any(|i|a[i][..variables].iter().all(|x|*x==0)&&a[i][variables]!=0){return None}
    let mut x=vec![0;variables];
    for (row,column) in pivots.iter().rev(){let mut z=a[*row][variables];for j in column+1..variables{z=sub(z,mul(a[*row][j],x[j],p),p)}x[*column]=z}
    Some((x,pivots.len()))
}

fn verifies_at(
    solution:&[u64], columns:&[usize], nmons:&[(usize,usize)], dmons:&[(usize,usize)],
    candidates:&[Candidate], u:u64, v:u64, axis:char, master:usize, p:u64
)->bool{
    let sys=source::evaluated_system(u,v,axis,master);
    let nv=monomial_values(u,v,nmons,p); let dv=monomial_values(u,v,dmons,p);
    let dbase=columns.len()*nmons.len();
    let mut denominator=1;
    for mi in 1..dmons.len(){denominator=add(denominator,mul(solution[dbase+mi-1],dv[mi],p),p)}
    if denominator==0{return false}
    let mut values=vec![0;372];
    for (ci,column) in columns.iter().enumerate(){values[*column]=nv.iter().enumerate().fold(0,|z,(mi,m)|add(z,mul(solution[ci*nmons.len()+mi],*m,p),p))}
    for row in 0..132 {
        let lhs=columns.iter().fold(0,|z,column|add(z,mul(sys.matrix[row][*column],values[*column],p),p));
        if lhs!=mul(denominator,sys.rhs[row],p){return false}
    }
    for (offset,column) in (8..12).enumerate(){
        let Some(f)=eval_candidate(&candidates[offset],u,v,p)else{return false};
        if values[column]!=mul(denominator,f,p){return false}
    }
    true
}

fn main(){
    let candidate_path=std::env::args().nth(1).unwrap_or_else(||"../marked-extension-charzero-candidate.json".into());
    let axis=std::env::var("MARICI_MODULE_AXIS").unwrap_or_else(|_|"u".into());
    let master=std::env::var("MARICI_MODULE_MASTER").ok().and_then(|x|x.parse().ok()).unwrap_or(0usize);
    let coefficient_degree=std::env::var("MARICI_MODULE_COEFF_DEGREE").ok().and_then(|x|x.parse().ok()).unwrap_or(0usize);
    let denominator_degree=std::env::var("MARICI_MODULE_DEN_DEGREE").ok().and_then(|x|x.parse().ok()).unwrap_or(coefficient_degree);
    let exact_degree=std::env::var("MARICI_MODULE_EXACT_DEGREE").ok().and_then(|x|x.parse().ok()).unwrap_or(4usize);
    let candidates=load_candidates(&candidate_path,&axis,master);
    let nmons=monomials(coefficient_degree); let dmons=monomials(denominator_degree);
    let columns=allowed_columns(exact_degree);
    for fixed in 8..12 {assert!(columns.contains(&fixed))}
    let variables=columns.len()*nmons.len()+dmons.len()-1; // D(0,0)=1.
    let wanted_samples=std::env::var("MARICI_MODULE_SAMPLES").ok().and_then(|x|x.parse().ok())
        .unwrap_or((variables+120)/121+2);
    let mut samples=Vec::new(); let mut seed=0u64;
    let side=(wanted_samples as f64).sqrt().ceil() as u64;
    while samples.len()<wanted_samples {
        let u=7+2*(seed%side); let v=11+4*(seed/side); seed+=1;
        let sys=source::evaluated_system(u,v,axis.chars().next().unwrap(),master); let p=sys.prime;
        let Some(fixed_values)=candidates.iter().map(|c|eval_candidate(c,u%p,v%p,p)).collect::<Option<Vec<_>>>() else {continue};
        samples.push((u%p,v%p,sys,fixed_values));
    }
    let p=samples[0].2.prime; let mut equations=Vec::new();
    for (u,v,sys,fixed_values) in &samples {
        let nv=monomial_values(*u,*v,&nmons,p); let dv=monomial_values(*u,*v,&dmons,p);
        for row in 0..132 {
            let mut eq=vec![0;variables+1];
            for (ci,column) in columns.iter().enumerate(){for (mi,m) in nv.iter().enumerate(){eq[ci*nmons.len()+mi]=mul(sys.matrix[row][*column],*m,p)}}
            let dbase=columns.len()*nmons.len(); for mi in 1..dmons.len(){eq[dbase+mi-1]=sub(0,mul(sys.rhs[row],dv[mi],p),p)}
            eq[variables]=sys.rhs[row]; equations.push(eq);
        }
        for (offset,column) in (8..12).enumerate(){
            let mut eq=vec![0;variables+1]; let ci=columns.iter().position(|x|*x==column).unwrap();
            for (mi,m) in nv.iter().enumerate(){eq[ci*nmons.len()+mi]=*m}
            let dbase=columns.len()*nmons.len(); for mi in 1..dmons.len(){eq[dbase+mi-1]=sub(0,mul(fixed_values[offset],dv[mi],p),p)}
            eq[variables]=fixed_values[offset]; equations.push(eq);
        }
    }
    eprintln!("module pilot axis={axis} master={master} coeff_degree={coefficient_degree} denominator_degree={denominator_degree} exact_degree={exact_degree} columns={} variables={} equations={} samples={}",columns.len(),variables,equations.len(),samples.len());
    match solve(equations,variables,p){
        Some((solution,rank))=>{
            let heldout:Vec<_>=(0..12).map(|t|(101+3*t,157+7*t)).collect();
            let passed=heldout.iter().all(|(u,v)|verifies_at(&solution,&columns,&nmons,&dmons,&candidates,*u,*v,axis.chars().next().unwrap(),master,p));
            println!("{{\"schema\":\"marici.nima.marked_extension_polynomial_module_pilot.v1\",\"status\":\"{}\",\"prime\":{},\"axis\":\"{}\",\"master\":{},\"coefficient_degree\":{},\"denominator_degree\":{},\"exact_degree\":{},\"active_columns\":{},\"variables\":{},\"equations\":{},\"rank\":{},\"samples\":{},\"heldout_points\":{},\"certifies_characteristic_zero\":false}}",if passed{"modular_witness_heldout_pass"}else{"training_fit_rejected"},p,axis,master,coefficient_degree,denominator_degree,exact_degree,columns.len(),variables,samples.len()*136,rank,samples.len(),heldout.len())
        },
        None=>println!("{{\"schema\":\"marici.nima.marked_extension_polynomial_module_pilot.v1\",\"status\":\"no_witness_at_bound\",\"prime\":{},\"axis\":\"{}\",\"master\":{},\"coefficient_degree\":{},\"denominator_degree\":{},\"exact_degree\":{},\"active_columns\":{},\"variables\":{},\"equations\":{},\"samples\":{},\"certifies_characteristic_zero\":false}}",p,axis,master,coefficient_degree,denominator_degree,exact_degree,columns.len(),variables,samples.len()*136,samples.len())
    }
}
