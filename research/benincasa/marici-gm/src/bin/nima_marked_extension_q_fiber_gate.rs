//! Generic-quartic specialization gate for the fixed final extension rows.
mod source {
    #![allow(dead_code)]
    include!("marked_relative_reduction_engine.rs");
    pub struct Gate { pub rank:usize,pub mask:u16,pub fixed:Vec<usize>,pub residual:bool,pub consistent:bool,pub pivot_hash:u64 }
    pub fn gate(u:u64,v:u64,axis:char,master:usize)->Gate{
        let s=solve(&geometry(u,v,axis),master,8);let(mask,fixed)=fixed_signature(&s);
        Gate{rank:s.rank,mask,fixed,residual:s.residual_zero,consistent:s.consistent,pivot_hash:pivot_hash(&s.pivot_cols)}
    }
    pub fn prime()->u64{P}
}
fn add(a:u64,b:u64,p:u64)->u64{((a as u128+b as u128)%p as u128)as u64}
fn sub(a:u64,b:u64,p:u64)->u64{if a>=b{a-b}else{p-(b-a)}}
fn mul(a:u64,b:u64,p:u64)->u64{((a as u128*b as u128)%p as u128)as u64}
fn pow(mut a:u64,mut n:u64,p:u64)->u64{let mut r=1;while n>0{if n&1==1{r=mul(r,a,p)}a=mul(a,a,p);n>>=1}r}
fn inv(a:u64,p:u64)->u64{pow(a,p-2,p)}
fn neg(a:u64,p:u64)->u64{if a==0{0}else{p-a}}
fn q(u:u64,v:u64,p:u64)->u64{
    let u2=mul(u,u,p);let u3=mul(u2,u,p);let u4=mul(u3,u,p);let v2=mul(v,v,p);
    let mut z=neg(u4,p);z=add(z,mul(4,mul(u3,v,p),p),p);z=sub(z,mul(4,u3,p),p);z=sub(z,mul(4,mul(u2,v,p),p),p);z=add(z,mul(4,u2,p),p);z=sub(z,mul(8,mul(u,v,p),p),p);z=sub(z,mul(4,v2,p),p);z=add(z,mul(16,u,p),p);z=add(z,mul(16,v,p),p);sub(z,16,p)
}
fn roots(u:u64,p:u64)->Vec<u64>{
    assert_eq!(p%4,3,"default prime is required for the bounded square-root gate");
    let u2=mul(u,u,p);let u3=mul(u2,u,p);let u4=mul(u3,u,p);
    let b=add(sub(sub(mul(4,u3,p),mul(4,u2,p),p),mul(8,u,p),p),16,p);
    let c=sub(add(add(add(neg(u4,p),neg(mul(4,u3,p),p),p),mul(4,u2,p),p),mul(16,u,p),p),16,p);
    let a=neg(4,p);let disc=sub(mul(b,b,p),mul(mul(4,a,p),c,p),p);let s=pow(disc,(p+1)/4,p);
    if mul(s,s,p)!=disc{return Vec::new()}let den=inv(mul(2,a,p),p);let r1=mul(add(neg(b,p),s,p),den,p);let r2=mul(sub(neg(b,p),s,p),den,p);if r1==r2{vec![r1]}else{vec![r1,r2]}
}
fn main(){
    let p=source::prime();let mut records=Vec::new();
    'scan:for u in 2..200u64{for v in roots(u,p){assert_eq!(q(u,v,p),0,"u={u} v={v}");let mut gates=Vec::new();let mut accepted=true;for axis in ['u','v']{for master in 0..3{let g=source::gate(u,v,axis,master);accepted&=g.rank==117&&g.mask==3847&&g.fixed==vec![0,1,2,8,9,10,11]&&g.residual&&g.consistent;gates.push(format!("{{\"axis\":\"{}\",\"master\":{},\"rank\":{},\"mask\":{},\"pivot_hash\":{},\"residual_zero\":{},\"consistent\":{}}}",axis,master,g.rank,g.mask,g.pivot_hash,g.residual,g.consistent));}}
        records.push(format!("{{\"u\":{},\"v\":{},\"Q\":0,\"accepted\":{},\"gates\":[{}]}}",u,v,accepted,gates.join(",")));if records.len()==4{break 'scan}
    }}
    assert_eq!(records.len(),4);println!("{{\"schema\":\"marici.nima.marked_extension_q_fiber_gate.v1\",\"prime\":{},\"points\":[{}],\"interpretation\":\"rank-117 fixed-coordinate charts on exact Q fibers; does not certify the full extension\"}}",p,records.join(","));
}
