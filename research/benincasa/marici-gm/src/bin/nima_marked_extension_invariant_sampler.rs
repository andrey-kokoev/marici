//! Sample the three primitive-independent mixed extension functionals.
mod source {
    #![allow(dead_code)]
    include!("marked_relative_reduction_engine.rs");
    pub fn sample(u:u64,v:u64,axis:char,master:usize)->Option<[u64;3]>{
        let s=solve(&geometry(u,v,axis),master,8);let(mask,_)=fixed_signature(&s);if !s.consistent||!s.residual_zero||s.rank!=117||mask!=3847{return None}
        let x=&s.witness[3..12];let c=F::n(3).mul(F::n(u)).add(F::n(v)).sub(F::n(2)).mul(F::n(2).inv());
        Some([
            x[2].sub(F::n(u+1).mul(x[1])).0,
            x[3].sub(F::n(u).mul(x[0])).add(x[1]).0,
            x[4].sub(F::n(u).mul(c).mul(x[0])).add(c.mul(x[1])).0,
        ])
    }
    pub fn prime()->u64{P}
}
fn main(){
    let wanted:usize=std::env::var("MARICI_INVARIANT_SAMPLES").ok().and_then(|x|x.parse().ok()).unwrap_or(220);let mut records=Vec::new();let mut seed=0u64;
    while records.len()<wanted{let u=7+2*(seed%31);let v=11+4*(seed/31);seed+=1;let mut axes=Vec::new();let mut ok=true;for axis in['u','v']{let mut values=Vec::new();for master in 0..3{if let Some(q)=source::sample(u,v,axis,master){values.push(q)}else{ok=false;break}}if !ok{break}let rows=[values.clone(),values[..1].to_vec()].concat();axes.push(format!("{{\"u\":{},\"v\":{},\"axis\":\"{}\",\"fixed_extension_e6_e9_mod_p\":{:?}}}",u,v,axis,rows));}if ok{records.extend(axes)}}
    let json=format!("{{\"schema\":\"marici.nima.marked_extension_invariant_sampler.v1\",\"prime\":{},\"wall_quotient_blocks\":[{}]}}",source::prime(),records.join(","));
    if let Some(path)=std::env::args().nth(1){std::fs::write(path,json).unwrap()}else{println!("{json}")}
}
