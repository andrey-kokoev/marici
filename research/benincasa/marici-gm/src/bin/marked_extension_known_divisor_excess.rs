//! Compare generic D/H source ranks with their proper intersections with Q.
mod source {
    #![allow(dead_code)]
    include!("marked_relative_reduction_engine.rs");
    pub fn signature(u:u64,v:u64)->(usize,u16,u64){
        let s=solve(&geometry(u,v,'u'),0,8);let(mask,_)=fixed_signature(&s);
        (s.rank,mask,pivot_hash(&s.pivot_cols))
    }
    pub fn prime()->u64{P}
}
fn add(a:u64,b:u64,p:u64)->u64{((a as u128+b as u128)%p as u128)as u64}
fn sub(a:u64,b:u64,p:u64)->u64{if a>=b{a-b}else{p-(b-a)}}
fn mul(a:u64,b:u64,p:u64)->u64{((a as u128*b as u128)%p as u128)as u64}
fn neg(a:u64,p:u64)->u64{if a==0{0}else{p-a}}
fn pow(mut a:u64,mut n:u64,p:u64)->u64{let mut r=1;while n>0{if n&1==1{r=mul(r,a,p)}a=mul(a,a,p);n>>=1}r}
fn inv(a:u64,p:u64)->u64{pow(a,p-2,p)}
fn q(u:u64,v:u64,p:u64)->u64{let u2=mul(u,u,p);let u3=mul(u2,u,p);let u4=mul(u3,u,p);let v2=mul(v,v,p);let mut z=neg(u4,p);z=add(z,mul(4,mul(u3,v,p),p),p);z=sub(z,mul(4,u3,p),p);z=sub(z,mul(4,mul(u2,v,p),p),p);z=add(z,mul(4,u2,p),p);z=sub(z,mul(8,mul(u,v,p),p),p);z=sub(z,mul(4,v2,p),p);z=add(z,mul(16,u,p),p);z=add(z,mul(16,v,p),p);sub(z,16,p)}
fn d(u:u64,v:u64,p:u64)->u64{let u2=mul(u,u,p);let mut z=neg(4,p);z=add(z,mul(12,u,p),p);z=sub(z,mul(6,mul(u,v,p),p),p);z=add(z,mul(4,v,p),p);z=sub(z,mul(9,u2,p),p);z=add(z,mul(4,mul(u2,v,p),p),p);sub(z,mul(v,v,p),p)}
fn h(u:u64,v:u64,p:u64)->u64{let u2=mul(u,u,p);let u3=mul(u2,u,p);let mut z=neg(2,p);z=sub(z,mul(3,u,p),p);z=add(z,mul(2,mul(u,v,p),p),p);z=add(z,v,p);z=sub(z,mul(u2,v,p),p);add(z,u3,p)}
fn d_roots(u:u64,p:u64)->Vec<u64>{assert_eq!(p%4,3);let u2=mul(u,u,p);let a=neg(1,p);let b=add(sub(add(4,mul(4,u2,p),p),mul(6,u,p),p),0,p);let c=sub(add(neg(4,p),mul(12,u,p),p),mul(9,u2,p),p);let disc=sub(mul(b,b,p),mul(mul(4,a,p),c,p),p);let s=pow(disc,(p+1)/4,p);if mul(s,s,p)!=disc{return vec![]}let den=inv(mul(2,a,p),p);let x=mul(add(neg(b,p),s,p),den,p);let y=mul(sub(neg(b,p),s,p),den,p);if x==y{vec![x]}else{vec![x,y]}}
fn h_root(u:u64,p:u64)->Option<u64>{let u2=mul(u,u,p);let coefficient=add(sub(1,u2,p),mul(2,u,p),p);if coefficient==0{return None}let constant=add(sub(neg(2,p),mul(3,u,p),p),mul(u2,u,p),p);Some(mul(neg(constant,p),inv(coefficient,p),p))}
fn main(){let p=source::prime();let mut ds=Vec::new();let mut hs=Vec::new();for u in 2..100{for v in d_roots(u,p){assert_eq!(d(u,v,p),0);if q(u,v,p)!=0&&ds.len()<6{let(r,m,x)=source::signature(u,v);ds.push(format!("{{\"u\":{u},\"v\":{v},\"rank\":{r},\"mask\":{m},\"pivot_hash\":{x}}}"));}}if let Some(v)=h_root(u,p){assert_eq!(h(u,v,p),0);if q(u,v,p)!=0&&hs.len()<6{let(r,m,x)=source::signature(u,v);hs.push(format!("{{\"u\":{u},\"v\":{v},\"rank\":{r},\"mask\":{m},\"pivot_hash\":{x}}}"));} }if ds.len()==6&&hs.len()==6{break}}
println!("{{\"schema\":\"marici.benincasa.marked_extension_known_divisor_excess.v1\",\"prime\":{p},\"generic_D\":[{}],\"generic_H\":[{}]}}",ds.join(","),hs.join(","));}
