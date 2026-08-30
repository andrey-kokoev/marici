//! Source-derived Laurent residue on a transverse arc through P6=D=0.
mod source {
    #![allow(dead_code)]
    include!("marked_relative_reduction_engine.rs");

    fn y(u:F,v:F)->F{u.add(v).mul(F::n(2).inv()).sub(F::o())}
    fn p6(u:F,v:F)->F{let u2=u.mul(u);let u3=u2.mul(u);let u4=u3.mul(u);let v2=v.mul(v);
        F::o().sub(u).sub(v).add(v2.mul(F::n(4).inv())).add(u.mul(v).mul(F::n(2).inv()))
        .sub(u2.mul(F::n(7)).mul(F::n(4).inv())).add(u2.mul(v)).add(u3).sub(u3.mul(v)).add(u4)}
    fn split_line(u0:u64,v0:u64,axis:char,master:usize,trivial:bool)->Option<F>{let s=solve(&geometry(u0,v0,axis),master,8);let(mask,coords)=fixed_signature(&s);
        if !s.consistent||!s.residual_zero||s.rank!=117||mask!=3847||coords!=vec![0,1,2,8,9,10,11]{return None}
        let u=F::n(u0);let v=F::n(v0);let yy=y(u,v);let alpha=F::o().sub(yy.mul(yy)).mul(yy.mul(yy).sub(u.mul(u).mul(u.mul(u))));if alpha.0==0{return None}
        let c1=s.values[9].mul(alpha.inv());if trivial{return Some(c1)}let h=u.mul(u.add(v)).mul(u.add(v).sub(F::n(4))).mul(p6(u,v)).mul(F::n(4).inv());Some(s.values[8].sub(h.mul(c1)))}
    fn arc_value(s:u64)->Option<F>{let u=F::o().add(F::n(s));let v=F::o().add(F::n(2).mul(F::n(s)));
        let bu=split_line(u.0,v.0,'u',1,false)?;let bv=split_line(u.0,v.0,'v',1,false)?;Some(bu.add(F::n(2).mul(bv)))}
    fn ord(a:&[F])->usize{a.iter().position(|x|x.0!=0).unwrap_or(usize::MAX)}
    fn pt(mut a:Vec<F>)->Vec<F>{while a.last().is_some_and(|x|x.0==0){a.pop();}a}
    fn pa(a:&[F],b:&[F])->Vec<F>{let mut r=vec![F::z();a.len().max(b.len())];for(i,x)in a.iter().enumerate(){r[i]=r[i].add(*x)}for(i,x)in b.iter().enumerate(){r[i]=r[i].add(*x)}pt(r)}
    fn ps(a:&[F],b:&[F])->Vec<F>{pa(a,&b.iter().map(|x|x.neg()).collect::<Vec<_>>())}
    fn pm(a:&[F],b:&[F])->Vec<F>{if a.is_empty()||b.is_empty(){return vec![]}let mut r=vec![F::z();a.len()+b.len()-1];for(i,x)in a.iter().enumerate(){for(j,y)in b.iter().enumerate(){r[i+j]=r[i+j].add(x.mul(*y))}}pt(r)}
    fn pd(mut a:Vec<F>,b:&[F])->(Vec<F>,Vec<F>){let mut q=vec![F::z();a.len().saturating_sub(b.len())+1];while a.len()>=b.len()&&!a.is_empty(){let k=a.len()-b.len();let c=a[a.len()-1].mul(b[b.len()-1].inv());q[k]=c;for(j,x)in b.iter().enumerate(){a[k+j]=a[k+j].sub(c.mul(*x))}a=pt(a)}(pt(q),a)}
    fn pg(mut a:Vec<F>,mut b:Vec<F>)->Vec<F>{while!b.is_empty(){let(_,r)=pd(a,b.as_slice());a=b;b=r}if a.is_empty(){return a}let z=a[a.len()-1].inv();a.into_iter().map(|x|x.mul(z)).collect()}
    fn pp(mut a:Vec<F>,mut n:u64,m:&[F])->Vec<F>{let mut r=vec![F::o()];while n>0{if n&1==1{r=pd(pm(&r,&a),m).1}a=pd(pm(&a,&a),m).1;n>>=1}r}
    fn linear_roots(f:&[F])->Vec<F>{let x=vec![F::z(),F::o()];let xp=pp(x,P,f);let mut g=pg(f.to_vec(),ps(&xp,&[F::z(),F::o()]));let mut roots=Vec::new();for c in 1..=128_u64{if g.len()<=1{break}if g.len()==2{roots.push(g[0].neg().mul(g[1].inv()));break}let a=vec![F::n(c),F::o()];let h=pg(g.clone(),ps(&pp(a,(P-1)/2,&g),&[F::o()]));if h.len()>1&&h.len()<g.len(){if h.len()==2{roots.push(h[0].neg().mul(h[1].inv()))}g=pd(g,&h).0;}}
        if g.len()==2{roots.push(g[0].neg().mul(g[1].inv()))}roots}
    fn dpoly(u:F,v:F)->F{F::n(4).neg().add(F::n(12).mul(u)).sub(F::n(6).mul(u).mul(v)).add(F::n(4).mul(v)).sub(F::n(9).mul(u).mul(u)).add(F::n(4).mul(u).mul(u).mul(v)).sub(v.mul(v))}
    fn hpoly(u:F,v:F)->F{F::n(2).neg().sub(F::n(3).mul(u)).add(F::n(2).mul(u).mul(v)).add(v).sub(u.mul(u).mul(v)).add(u.mul(u).mul(u))}
    fn d_roots(u:F)->Vec<F>{let e=F::n(4).sub(F::n(6).mul(u)).add(F::n(4).mul(u).mul(u));let f=F::n(4).neg().add(F::n(12).mul(u)).sub(F::n(9).mul(u).mul(u));let disc=e.mul(e).add(F::n(4).mul(f));let s=disc.pow((P+1)/4);if s.mul(s)!=disc{return vec![]}let twoinv=F::n(2).inv();vec![e.sub(s).mul(twoinv),e.add(s).mul(twoinv)]}
    fn generic_point()->(F,F){let cubic=vec![F::o(),F::n(8).neg(),F::n(12),F::n(4).neg()];for u in linear_roots(&cubic){for v in d_roots(u){if p6(u,v).0==0&&dpoly(u,v).0==0&&u!=F::o(){return(u,v)}}}panic!("no split generic P6-D point over this prime")}
    fn generic_h_point()->(F,F){let cubic=vec![F::n(2).neg(),F::n(2),F::n(2),F::o().neg()];for u in linear_roots(&cubic){let e=F::o().add(F::n(2).mul(u)).sub(u.mul(u));if e.0==0{continue}let f=F::n(2).neg().sub(F::n(3).mul(u)).add(u.mul(u).mul(u));let v=f.neg().mul(e.inv());if p6(u,v).0==0&&hpoly(u,v).0==0&&u.0!=0{return(u,v)}}panic!("no split generic P6-H point over this prime")}
    fn generic_p6_point()->(F,F){let start=std::env::var("MARICI_P6_U_START").ok().and_then(|x|x.parse().ok()).unwrap_or(3_u64);for n in start..=start+512{let u=F::n(n);let u2=u.mul(u);let u3=u2.mul(u);let u4=u3.mul(u);let b=F::n(4).neg().add(F::n(2).mul(u)).add(F::n(4).mul(u2)).sub(F::n(4).mul(u3));let c=F::n(4).sub(F::n(4).mul(u)).sub(F::n(7).mul(u2)).add(F::n(4).mul(u3)).add(F::n(4).mul(u4));for v in linear_roots(&[c,b,F::o()]){let(_,ap,_)=gradients(u,v,false);let yy=y(u,v);let alpha=F::o().sub(yy.mul(yy)).mul(yy.mul(yy).sub(u4));if p6(u,v).0==0&&ap.0!=0&&alpha.0!=0{return(u,v)}}}panic!("no generic split P6 point over this prime")}
    fn gradients(u:F,v:F,h_mode:bool)->(F,F,F){let u2=u.mul(u);let u3=u2.mul(u);let p_u=F::n(4).mul(u3).sub(F::n(3).mul(u2).mul(v)).add(F::n(3).mul(u2)).add(F::n(2).mul(u).mul(v)).sub(F::n(7).mul(u).mul(F::n(2).inv())).add(v.mul(F::n(2).inv())).sub(F::o());let p_v=u3.neg().add(u2).add(u.mul(F::n(2).inv())).add(v.mul(F::n(2).inv())).sub(F::o());let(w_u,w_v)=if h_mode{(F::n(3).neg().add(F::n(2).mul(v)).sub(F::n(2).mul(u).mul(v)).add(F::n(3).mul(u2)),F::o().add(F::n(2).mul(u)).sub(u2))}else{(F::n(12).sub(F::n(6).mul(v)).sub(F::n(18).mul(u)).add(F::n(8).mul(u).mul(v)),F::n(4).sub(F::n(6).mul(u)).add(F::n(4).mul(u2)).sub(F::n(2).mul(v)))};let jac=p_u.mul(w_v).sub(p_v.mul(w_u));let arc_p=p_u.add(F::n(2).mul(p_v));let arc_w=w_u.add(F::n(2).mul(w_v));(jac,arc_p,arc_w)}
    pub fn run()->String{
        let h_mode=std::env::var_os("MARICI_P6_H_WALL").is_some();let generic_trivial=std::env::var_os("MARICI_P6_GENERIC_TRIVIAL").is_some();let(u0,v0)=if generic_trivial{generic_p6_point()}else if h_mode{generic_h_point()}else{generic_point()};let(jac,arc_p,arc_w)=if generic_trivial{let(_,ap,_)=gradients(u0,v0,false);(F::o(),ap,F::o())}else{gradients(u0,v0,h_mode)};assert!(arc_p.0!=0&&(generic_trivial||(jac.0!=0&&arc_w.0!=0)));let master=if generic_trivial{std::env::var("MARICI_P6_MASTER").ok().and_then(|x|x.parse().ok()).unwrap_or(0)}else if h_mode{2}else{1};assert!(master<3);let mut values=Vec::new();for s in 1..=72_u64{let ss=F::n(s);let u=u0.add(ss);let v=v0.add(F::n(2).mul(ss));let bu=split_line(u.0,v.0,'u',master,generic_trivial);let bv=split_line(u.0,v.0,'v',master,generic_trivial);if let(Some(x),Some(y))=(bu,bv){values.push((ss,x.add(F::n(2).mul(y))))}}
        assert!(values.len()>=60);let discovery=&values[..48];let verification=&values[48..];
        let mut found=None;for total in 0..=40{for dd in 0..=total{let nd=total-dd;if let Some((n,d))=rational_interpolate(discovery,nd,dd){
            let ok=verification.iter().all(|(x,y)|{let ev=|a:&[F]|a.iter().rev().fold(F::z(),|q,c|q.mul(*x).add(*c));ev(&n)==y.mul(ev(&d))});
            if ok{found=Some((n,d,nd,dd));break}}}if found.is_some(){break}}
        let(n,d,nd,dd)=found.expect("held-out rational interpolation");let on=ord(&n);let od=ord(&d);let valuation=on as isize-od as isize;
        let leading=n[on].mul(d[od].inv());
        format!(concat!("{{\"schema\":\"marici.p6_wall_exceptional_source_residue.v4\",\"wall\":\"{}\",\"prime\":{},\"point_mod_p\":[{},{}],\"resultant_branch\":\"{}\",\"transverse_jacobian_mod_p\":{},\"arc_derivatives_mod_p\":[{},{}],\"arc\":\"u=u0+s,v=v0+2s\",\"source_direction\":\"{}\",\"target_line\":\"{}\",\"accepted_samples\":{},\"discovery_samples\":48,\"verification_samples\":{},\"numerator_degree\":{},\"denominator_degree\":{},\"numerator_order\":{},\"denominator_order\":{},\"valuation\":{},\"leading_coefficient_mod_p\":{},\"logarithmic_residue_nonzero\":{}}}"),if generic_trivial{"generic_P6"}else if h_mode{"H"}else{"D"},P,u0.0,v0.0,if generic_trivial{"P6"}else if h_mode{"-2+2u+2u^2-u^3"}else{"1-8u+12u^2-4u^3"},jac.0,arc_p.0,arc_w.0,if generic_trivial{match master{0=>"top",1=>"wall1",_=>"wall2"}}else if h_mode{"wall2"}else{"wall1"},if generic_trivial{"trivial_algebraic"}else{"P6^-1/2"},values.len(),verification.len(),nd,dd,on,od,valuation,leading.0,valuation==-1)
    }
}
fn main(){
    let json=source::run();
    if let Some(path)=std::env::args().nth(1){std::fs::write(path,json).unwrap()}else{println!("{json}")}
}
