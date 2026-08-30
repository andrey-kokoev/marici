//! Test the primitive-independent marked extension against the two exact
//! algebraic lines of Entry 867.  This uses the frozen source reduction at
//! generic finite-field points; it does not reconstruct rational functions.
mod source {
    #![allow(dead_code)]
    include!("marked_relative_reduction_engine.rs");

    fn y(u: F, v: F) -> F { u.add(v).mul(F::n(2).inv()).sub(F::o()) }
    fn p6(u: F, v: F) -> F {
        let u2=u.mul(u); let u3=u2.mul(u); let u4=u3.mul(u); let v2=v.mul(v);
        F::o().sub(u).sub(v).add(v2.mul(F::n(4).inv()))
            .add(u.mul(v).mul(F::n(2).inv()))
            .sub(u2.mul(F::n(7)).mul(F::n(4).inv()))
            .add(u2.mul(v)).add(u3).sub(u3.mul(v)).add(u4)
    }

    pub fn project(u0:u64,v0:u64,axis:char,master:usize)->Option<([u64;2],[u64;2])>{
        let s=solve(&geometry(u0,v0,axis),master,8);
        let(mask,coords)=fixed_signature(&s);
        if !s.consistent||!s.residual_zero||s.rank!=117||mask!=3847||coords!=vec![0,1,2,8,9,10,11]{return None}
        let b=[s.values[8],s.values[9],s.values[10],s.values[11]];
        let u=F::n(u0); let v=F::n(v0); let yy=y(u,v);
        let alpha=F::o().sub(yy.mul(yy)).mul(yy.mul(yy).sub(u.mul(u).mul(u.mul(u))));
        if alpha.0==0{return None}
        let c1=b[1].mul(alpha.inv());
        let beta=F::n(2).mul(u.mul(u).add(yy.mul(yy)));
        let gamma=F::n(2).mul(yy.mul(yy)).mul(u.mul(u).add(F::o())).neg();
        let residual=[b[2].sub(beta.mul(c1)).0,b[3].sub(gamma.mul(c1)).0];
        let h=u.mul(u.add(v)).mul(u.add(v).sub(F::n(4))).mul(p6(u,v)).mul(F::n(4).inv());
        let split=[b[0].sub(h.mul(c1)).0,c1.0];
        Some((split,residual))
    }
    pub fn prime()->u64{P}
}

fn main(){
    let samples=[(7,11),(13,19),(23,29),(31,37),(41,47)];
    let mut records=Vec::new(); let mut nonzero=[0usize;2]; let mut total=0usize;
    for (u,v) in samples { for axis in ['u','v'] { for master in 0..3 {
        let (split,residual)=source::project(u,v,axis,master).expect("generic source solve failed");
        assert_eq!(residual,[0,0],"fixed final block leaves algebraic plane");
        for i in 0..2 { if split[i]!=0 { nonzero[i]+=1; } }
        total+=1;
        records.push(format!("{{\"u\":{u},\"v\":{v},\"axis\":\"{axis}\",\"source\":{master},\"split_coordinates\":[{},{}]}}",split[0],split[1]));
    }}}
    let json=format!("{{\"schema\":\"marici.benincasa.marked_extension_algebraic_line_support.v1\",\"prime\":{},\"samples\":5,\"tested_columns\":{},\"nonzero_counts\":[{},{}],\"algebraic_plane_residual_zero\":true,\"records\":[{}]}}",source::prime(),total,nonzero[0],nonzero[1],records.join(","));
    if let Some(path)=std::env::args().nth(1){std::fs::write(path,json).expect("write result packet")}else{println!("{json}")}
}
