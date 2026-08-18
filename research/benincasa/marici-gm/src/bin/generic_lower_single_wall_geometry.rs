use std::collections::BTreeMap;

const N: usize = 6;
type Exp = [u8; N];

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct Poly(BTreeMap<Exp, i128>);

impl Poly {
    fn term(exp: Exp, coefficient: i128) -> Self {
        let mut out = Self::default();
        if coefficient != 0 { out.0.insert(exp, coefficient); }
        out
    }
    fn constant(value: i128) -> Self { Self::term([0; N], value) }
    fn var(index: usize) -> Self {
        let mut exp = [0; N]; exp[index] = 1; Self::term(exp, 1)
    }
    fn add(&self, rhs: &Self) -> Self {
        let mut out = self.clone();
        for (m,c) in &rhs.0 {
            let next = out.0.get(m).copied().unwrap_or(0) + c;
            if next == 0 { out.0.remove(m); } else { out.0.insert(*m,next); }
        }
        out
    }
    fn scale(&self, c: i128) -> Self {
        let mut out=Self::default();
        for (m,v) in &self.0 { if c*v != 0 { out.0.insert(*m,c*v); } }
        out
    }
    fn sub(&self, rhs:&Self)->Self { self.add(&rhs.scale(-1)) }
    fn mul(&self, rhs:&Self)->Self {
        let mut out=Self::default();
        for (lm,lc) in &self.0 { for (rm,rc) in &rhs.0 {
            let mut m=[0;N]; for i in 0..N { m[i]=lm[i]+rm[i]; }
            let next=out.0.get(&m).copied().unwrap_or(0)+lc*rc;
            if next==0 {out.0.remove(&m);} else {out.0.insert(m,next);}
        }} out
    }
    fn pow(&self, mut n:u8)->Self {
        let mut out=Self::constant(1); let mut base=self.clone();
        while n>0 { if n&1==1 {out=out.mul(&base);} n>>=1; if n>0 {base=base.mul(&base);} }
        out
    }
    fn coefficient_ts(&self, ti:u8, si:u8)->Self {
        let mut out=Self::default();
        for (m,c) in &self.0 {
            if m[4]==ti && m[5]==si {
                let mut q=*m; q[4]=0; q[5]=0; out.0.insert(q,*c);
            }
        }
        out
    }
    fn eval_params(&self, point:[i128;4])->i128 {
        self.0.iter().map(|(m,c)| {
            assert_eq!(m[4],0); assert_eq!(m[5],0);
            let mut v=*c; for i in 0..4 {v*=point[i].pow(u32::from(m[i]));} v
        }).sum()
    }
    fn format_params(&self)->String {
        if self.0.is_empty(){return "0".into();}
        let names=["X1","P1","P2","P3"];
        let mut terms:Vec<_>=self.0.iter().collect();
        terms.sort_by_key(|(m,_)| std::cmp::Reverse(m[..4].iter().sum::<u8>()));
        terms.into_iter().map(|(m,c)|{
            let fs:Vec<_>=(0..4).filter(|i|m[*i]>0).map(|i|if m[i]==1{names[i].into()}else{format!("{}^{}",names[i],m[i])}).collect();
            if fs.is_empty(){c.to_string()} else if *c==1{fs.join("*")} else if *c== -1{format!("-{}",fs.join("*"))} else {format!("{}*{}",c,fs.join("*"))}
        }).collect::<Vec<_>>().join(" + ").replace("+ -","- ")
    }
}

fn sum(xs:&[Poly])->Poly { xs.iter().fold(Poly::default(),|a,b|a.add(b)) }

fn compactified_k(sign:i128)->Poly {
    // Parameter order: X1,P1,P2,P3; local coordinates: t,s.
    let x=Poly::var(0); let p1=Poly::var(1); let p2=Poly::var(2); let p3=Poly::var(3);
    let t=Poly::var(4); let s=Poly::var(5);
    let a=Poly::constant(sign).add(&t);
    let b=Poly::constant(1);
    let c=Poly::constant(-1).sub(&x.mul(&s));
    let p1s=p1.pow(2); let p2s=p2.pow(2); let p3s=p3.pow(2);
    let a2=a.pow(2); let b2=b.pow(2); let c2=c.pow(2);
    let k4=sum(&[
        p1s.mul(&a.pow(4)), p1s.mul(&a2).mul(&b2).scale(-1),
        p1s.mul(&a2).mul(&c2).scale(-1), p1s.mul(&b2).mul(&c2),
        p2s.mul(&a2).mul(&b2).scale(-1), p2s.mul(&a2).mul(&c2),
        p2s.mul(&b.pow(4)), p2s.mul(&b2).mul(&c2).scale(-1),
        p3s.mul(&a2).mul(&b2), p3s.mul(&a2).mul(&c2).scale(-1),
        p3s.mul(&b2).mul(&c2).scale(-1), p3s.mul(&c.pow(4)),
    ]);
    let k2=sum(&[
        p1.pow(4).mul(&a2), p1s.mul(&p2s).mul(&a2).scale(-1),
        p1s.mul(&p2s).mul(&b2).scale(-1), p1s.mul(&p3s).mul(&a2).scale(-1),
        p1s.mul(&p3s).mul(&c2).scale(-1), p2.pow(4).mul(&b2),
        p2s.mul(&p3s).mul(&b2).scale(-1), p2s.mul(&p3s).mul(&c2).scale(-1),
        p3.pow(4).mul(&c2),
    ]);
    let k0=p1s.mul(&p2s).mul(&p3s);
    k4.add(&k2.mul(&s.pow(2))).add(&k0.mul(&s.pow(4)))
}

fn main(){
    let x=Poly::var(0); let p1=Poly::var(1); let p2=Poly::var(2); let p3=Poly::var(3); let t=Poly::var(4);
    let lambda=p1.sub(&p2).sub(&p3)
        .mul(&p1.sub(&p2).add(&p3))
        .mul(&p1.add(&p2).sub(&p3))
        .mul(&p1.add(&p2).add(&p3));
    let expected_node=p1.pow(2).sub(&x.pow(2)).mul(&lambda).scale(16);
    let expected_boundary=p1.pow(2).mul(&t.mul(&t.add(&Poly::constant(2))).pow(2));
    let mut determinants=Vec::new();
    for sign in [1_i128,-1_i128] {
        let k=compactified_k(sign);
        assert_eq!(k.coefficient_ts(0,0),Poly::default());
        assert_eq!(k.coefficient_ts(1,0),Poly::default());
        assert_eq!(k.coefficient_ts(0,1),Poly::default());
        let boundary:Poly=if sign==1 {
            k.0.iter().filter(|(m,_)|m[5]==0).map(|(m,c)|Poly::term(*m,*c)).fold(Poly::default(),|a,b|a.add(&b))
        } else {
            let expected=p1.pow(2).mul(&t.mul(&t.sub(&Poly::constant(2))).pow(2));
            let got=k.0.iter().filter(|(m,_)|m[5]==0).map(|(m,c)|Poly::term(*m,*c)).fold(Poly::default(),|a,b|a.add(&b));
            assert_eq!(got,expected); got
        };
        if sign==1 { assert_eq!(boundary,expected_boundary); }
        let qtt=k.coefficient_ts(2,0);
        let qts=k.coefficient_ts(1,1);
        let qss=k.coefficient_ts(0,2);
        let determinant=qtt.mul(&qss).scale(4).sub(&qts.pow(2));
        assert_eq!(determinant,expected_node);
        assert!(!determinant.0.is_empty());
        assert_ne!(determinant.eval_params([2,5,7,11]),0);
        println!("SIGN={sign} Q_TT={}",qtt.format_params());
        println!("SIGN={sign} Q_TS={}",qts.format_params());
        println!("SIGN={sign} Q_SS={}",qss.format_params());
        println!("SIGN={sign} NODE_DISCRIMINANT={}",determinant.format_params());
        println!("SIGN={sign} NODE_DISCRIMINANT_FACTORED=16*(P1-X1)*(P1+X1)*Lambda_P");
        println!("SIGN={sign} NODE_DISCRIMINANT_SAMPLE={}",determinant.eval_params([2,5,7,11]));
        determinants.push(determinant);
    }
    assert_eq!(determinants[0],determinants[1]);
    println!("BOUNDARY_COMPONENTS=2");
    println!("BOUNDARY_INTERSECTIONS=2");
    println!("GENERIC_BOUNDARY_SINGULARITY=A1_AT_EACH_INTERSECTION");
}
