//! Compare the generic u+v-2 source signature with its finite Q intersection.
mod source {
    #![allow(dead_code)]
    include!("marked_relative_reduction_engine.rs");
    pub fn signature(u:u64,v:u64)->(usize,u16,u64){
        let s=solve(&geometry(u,v,'u'),0,8);
        let(mask,_)=fixed_signature(&s);
        (s.rank,mask,pivot_hash(&s.pivot_cols))
    }
    pub fn prime()->u64{P}
}

fn sub(a:u64,b:u64,p:u64)->u64{if a>=b{a-b}else{p-(b-a)}}
fn mul(a:u64,b:u64,p:u64)->u64{((a as u128*b as u128)%p as u128)as u64}
fn pow(mut a:u64,mut n:u64,p:u64)->u64{let mut r=1;while n>0{if n&1==1{r=mul(r,a,p)}a=mul(a,a,p);n>>=1}r}
fn inv(a:u64,p:u64)->u64{pow(a,p-2,p)}

fn main(){
    let p=source::prime();
    let mut generic=Vec::new();
    for u in 3..9 {
        let v=sub(2,u,p);
        let (rank,mask,pivot_hash)=source::signature(u,v);
        generic.push(format!("{{\"u\":{u},\"v\":{v},\"rank\":{rank},\"mask\":{mask},\"pivot_hash\":{pivot_hash}}}"));
    }
    let u=mul(8,inv(5,p),p);
    let v=mul(2,inv(5,p),p);
    let (rank,mask,pivot_hash)=source::signature(u,v);
    println!("{{\"schema\":\"marici.nima.marked_extension_linear_divisor_excess.v1\",\"prime\":{p},\"generic\":[{}],\"Q_intersection\":{{\"u\":{u},\"v\":{v},\"rank\":{rank},\"mask\":{mask},\"pivot_hash\":{pivot_hash}}}}}",generic.join(","));
}
