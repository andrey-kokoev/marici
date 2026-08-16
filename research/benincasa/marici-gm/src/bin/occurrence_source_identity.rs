mod frozen {
    #![allow(dead_code)]
    include!("../../../check_split_occurrence_weight_zero.rs");
    pub fn source_residue(x:i128,y:i128,n:i128,which31:bool)->(i128,i128) {
        let q=residue(x,y,n,which31); (q.n,q.d)
    }
    pub fn source_primitive(x:i128,y:i128,which31:bool)->Vec<(i128,i128)> {
        primitive_polynomial(x,y,which31).1.into_iter().map(|q|(q.n,q.d)).collect()
    }
    pub fn identity_residual(x:i128,y:i128,n:i128,which31:bool)->(i128,i128) {
        let z=identity_components(x,y,n,which31).into_iter().fold(Rat::Z,|a,(u,v)|a.add(Rat::new(u,v)));
        (z.n,z.d)
    }
    pub fn identity_components(x:i128,y:i128,n:i128,which31:bool)->[(i128,i128);4] {
        let (l,mut h)=primitive_polynomial(x,y,which31);
        let mut p=numerator_polynomial(x,y,which31);
        for k in 0..h.len() { if k%2==0 { h[k]=Rat::Z; } }
        for k in 0..p.len() { if k%2==1 { p[k]=Rat::Z; } }
        let eval=|poly:&[Rat]|poly.iter().rev().fold(Rat::Z,|z,&c|z.scale(n,1).add(c));
        let mut dh=Rat::Z;
        for (k,&c) in h.iter().enumerate().skip(1) {
            let mut term=c.scale(k as i128,1);
            for _ in 0..k-1 {term=term.scale(n,1);}
            dh=dh.add(term);
        }
        let hn=eval(&h); let pn=eval(&p);
        let v=x*y*n*n-2*(x+y);
        let mut v5=1_i128;for _ in 0..5{v5*=v;}
        let z=[dh.scale(v,1),hn.scale(-9*x*y*n,1),pn.neg(),l.scale(v5,x*y)];
        z.map(|q|(q.n,q.d))
    }
}

use std::{collections::BTreeMap, env, fs};

const TMAX: i32 = 10;
const RMIN: i32 = -6;
const RMAX: i32 = 8;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct F<const P: u64>(u64);

impl<const P: u64> F<P> {
    const Z: Self = Self(0);
    const O: Self = Self(1);
    fn i(n: i128) -> Self {
        let p = P as i128;
        Self(((n % p + p) % p) as u64)
    }
    fn add(self, r: Self) -> Self {
        let z = self.0 as u128 + r.0 as u128;
        Self((z % P as u128) as u64)
    }
    fn neg(self) -> Self { if self.0 == 0 { self } else { Self(P-self.0) } }
    fn sub(self, r: Self) -> Self { self.add(r.neg()) }
    fn mul(self, r: Self) -> Self { Self(((self.0 as u128*r.0 as u128)%P as u128) as u64) }
    fn pow(self, mut k: u64) -> Self {
        let mut a=self; let mut z=Self::O;
        while k>0 { if k&1==1 { z=z.mul(a); } k>>=1; if k>0 { a=a.mul(a); } }
        z
    }
    fn inv(self) -> Self { assert_ne!(self,Self::Z); self.pow(P-2) }
    fn div(self,r:Self)->Self{self.mul(r.inv())}
    fn rat(n:i128,d:i128)->Self{Self::i(n).div(Self::i(d))}
}

#[derive(Clone, Debug)]
struct S<const P:u64>(BTreeMap<(i32,i32),F<P>>);

impl<const P:u64> S<P> {
    fn mono(t:i32,r:i32,c:i128)->Self{
        let mut m=BTreeMap::new(); let z=F::i(c);
        if z!=F::Z {m.insert((t,r),z);} Self(m)
    }
    fn field(t:i32,r:i32,c:F<P>)->Self{
        let mut m=BTreeMap::new(); if c!=F::Z {m.insert((t,r),c);} Self(m)
    }
    fn add(&self,q:&Self)->Self{
        let mut out=self.0.clone();
        for(&k,&v) in &q.0 {
            let z=out.get(&k).copied().unwrap_or(F::Z).add(v);
            if z==F::Z {out.remove(&k);} else {out.insert(k,z);}
        } Self(out)
    }
    fn scale(&self,c:F<P>)->Self{
        Self(self.0.iter().filter_map(|(&k,&v)|{
            let z=v.mul(c);(z!=F::Z).then_some((k,z))
        }).collect())
    }
    fn mul(&self,q:&Self)->Self{
        let mut out=Self(BTreeMap::new());
        for(&(ta,ra),&a) in &self.0 {for(&(tb,rb),&b) in &q.0 {
            let(t,r)=(ta+tb,ra+rb);
            if(0..=TMAX).contains(&t)&&(RMIN..=RMAX).contains(&r){
                out=out.add(&Self::field(t,r,a.mul(b)));
            }
        }} out
    }
    fn pow(&self,mut k:usize)->Self{
        let mut a=self.clone();let mut z=Self::mono(0,0,1);
        while k>0 {if k&1==1{z=z.mul(&a);}k>>=1;if k>0{a=a.mul(&a);}}z
    }
    fn coeff(&self,t:i32,r:i32)->F<P>{self.0.get(&(t,r)).copied().unwrap_or(F::Z)}
}

fn binomial_m32<const P:u64>(j:usize)->F<P>{
    let mut z=F::O;
    for k in 0..j {z=z.mul(F::rat(-3-2*k as i128,2*(k as i128+1)));}
    z
}
fn geom<const P:u64>(unit:&S<P>,terms:usize)->S<P>{
    assert_eq!(unit.coeff(0,0),F::O);
    let u=unit.add(&S::mono(0,0,-1));let mut out=S::mono(0,0,1);let mut pow=S::mono(0,0,1);
    for j in 1..=terms {pow=pow.mul(&u);out=out.add(&pow.scale(F::i(if j%2==0{1}else{-1})));}
    out
}
fn m32<const P:u64>(unit:&S<P>,terms:usize)->S<P>{
    assert_eq!(unit.coeff(0,0),F::O);
    let u=unit.add(&S::mono(0,0,-1));let mut out=S::mono(0,0,1);let mut pow=S::mono(0,0,1);
    for j in 1..=terms {pow=pow.mul(&u);out=out.add(&pow.scale(binomial_m32(j)));}
    out
}

fn weighted_kl<const P:u64>(x:i128,y:i128,n:i128)->(S<P>,S<P>){
    let tau2=S::mono(2,0,1);
    let total=tau2.clone();
    let z=tau2.add(&S::mono(0,0,-(x+y)));
    let cut=tau2.scale(F::i(-1));
    let aa=S::mono(0,0,y).add(&S::mono(2,1,1));
    let bb=S::mono(0,0,x).add(&S::mono(2,1,-1)).add(&S::mono(3,0,n));
    let x2=S::mono(0,0,x*x);let y2=S::mono(0,0,y*y);
    let a2=aa.pow(2);let b2=bb.pow(2);let z2=z.pow(2);let c2=cut.pow(2);
    let h=x2.add(&y2).add(&z2.scale(F::i(-1)));
    let f=x2.mul(&a2.pow(2)).add(&h.mul(&a2).mul(&b2).scale(F::i(-1))).add(&y2.mul(&b2.pow(2)));
    let ga=x2.add(&c2.scale(F::i(-1))).mul(&x2.add(&y2.scale(F::i(-1))).add(&z2.scale(F::i(-1))))
        .add(&c2.mul(&z2).scale(F::i(-2)));
    let gb=y2.add(&c2.scale(F::i(-1))).mul(&y2.add(&x2.scale(F::i(-1))).add(&z2.scale(F::i(-1))))
        .add(&c2.mul(&z2).scale(F::i(-2)));
    let hh=z2.mul(&c2.add(&y2.scale(F::i(-1))).mul(&c2.add(&x2.scale(F::i(-1)))).add(&c2.mul(&z2)));
    let k=f.add(&ga.mul(&a2)).add(&gb.mul(&b2)).add(&hh);
    let bracket=x2.add(&y2.scale(F::i(-1))).add(&z2).mul(&a2)
        .add(&y2.add(&x2.scale(F::i(-1))).add(&z2).mul(&b2))
        .add(&z2.mul(&total.pow(2).scale(F::i(2)).add(&x2.scale(F::i(-1))).add(&y2.scale(F::i(-1))).add(&z2)).scale(F::i(-1)));
    let l=total.mul(&bracket).scale(F::i(2));
    let ks=S(k.0.into_iter().filter_map(|((t,r),c)|(t>=6).then_some(((t-6,r),c))).collect());
    let ls=S(l.0.into_iter().filter_map(|((t,r),c)|(t>=4).then_some(((t-4,r),c))).collect());
    (ks,ls)
}

fn residue<const P:u64>(x:i128,y:i128,n:i128,which31:bool)->Option<F<P>>{
    let(k,l)=weighted_kl(x,y,n);
    let k00=F::i(4*x*y*(n*n*x*y-2*(x+y)));
    if k00==F::Z{return None;}
    let ku=k.scale(k00.inv());
    let km=m32(&ku,10);
    let q1=S::mono(0,0,1).add(&S::mono(2,1,-1).add(&S::mono(2,0,-1)).add(&S::mono(3,0,n)).scale(F::rat(1,2*x)));
    let q2=S::mono(0,0,1).add(&S::mono(2,1,1).add(&S::mono(2,0,-1)).scale(F::rat(1,2*y)));
    let q3=S::mono(0,0,1).add(&S::mono(1,0,n));
    let mut d=geom(&q1,10).mul(&geom(&q2,10)).mul(&geom(&q3,10)).scale(F::rat(1,4*x*y));
    let occ=if which31{S::mono(0,-1,1)}else{
        let mut z=S(BTreeMap::new());
        for j in 0..=4 {z=z.add(&S::field(j,-(j+1),F::i(-n.pow(j as u32))));}z
    };
    d=d.mul(&occ);
    Some(d.mul(&l).mul(&km).scale(F::rat(-1,2)).coeff(4,-1))
}

fn poly<const P:u64>(x:F<P>,y:F<P>,terms:&[(i128,u32,u32)])->F<P>{
    terms.iter().fold(F::Z,|z,&(c,px,py)|z.add(F::i(c).mul(x.pow(px as u64)).mul(y.pow(py as u64))))
}
fn h31<const P:u64>(x:F<P>,y:F<P>)->[F<P>;6]{
    [
        poly(x,y,&[(1727,0,6),(9026,1,5),(19841,2,4),(23548,3,3),(16001,4,2),(5954,5,1),(959,6,0)]).div(F::i(32).mul(x.pow(2)).mul(y.pow(2))),
        poly(x,y,&[(1667,0,5),(6901,1,4),(11640,2,3),(10136,3,2),(4645,4,1),(915,5,0)]).neg().div(F::i(16).mul(x).mul(y)),
        poly(x,y,&[(661,0,4),(2113,1,3),(2643,2,2),(1585,3,1),(397,4,0)]).div(F::i(8)),
        x.mul(y).mul(poly(x,y,&[(259,0,3),(613,1,2),(535,2,1),(181,3,0)])).neg().div(F::i(8)),
        x.pow(2).mul(y.pow(2)).mul(poly(x,y,&[(25,0,2),(41,1,1),(21,2,0)])).div(F::i(4)),
        x.pow(3).mul(y.pow(3)).mul(x.add(y)).neg().div(F::i(2)),
    ]
}
fn verify_point<const P:u64>(xi:i128,yi:i128,ni:i128)->Option<()>{
    let x=F::i(xi);let y=F::i(yi);let n=F::i(ni);
    let v=x.mul(y).mul(n.pow(2)).sub(F::i(2).mul(x.add(y)));
    if x==F::Z||y==F::Z||x==y||v==F::Z{return None;}
    let r31=residue::<P>(xi,yi,ni,true)?;
    let r23=residue::<P>(xi,yi,ni,false)?;
    let r31_neg=residue::<P>(xi,yi,-ni,true)?;
    let r23_neg=residue::<P>(xi,yi,-ni,false)?;
    if (xi,yi,ni)==(1,2,1) {
        let (a,b)=frozen::source_residue(xi,yi,ni,true);
        let (c,d)=frozen::source_residue(xi,yi,ni,false);
        let (an,bn)=frozen::source_residue(xi,yi,-ni,true);
        let (cn,dn)=frozen::source_residue(xi,yi,-ni,false);
        assert_eq!(r31,F::rat(a,b),"modular r31 differs frozen exact source");
        assert_eq!(r23,F::rat(c,d),"modular r23 differs frozen exact source");
        assert_eq!(r31_neg,F::rat(an,bn),"modular r31(-n) differs frozen exact source");
        assert_eq!(r23_neg,F::rat(cn,dn),"modular r23(-n) differs frozen exact source");
        let exact_res=frozen::identity_residual(xi,yi,ni,true);
        assert_eq!(exact_res.0,0,"frozen exact identity itself failed");
        let exact_h=frozen::source_primitive(xi,yi,true);
        assert!(exact_h.len()<=12,"frozen primitive has degrees beyond reconstructed n^11: len={}",exact_h.len());
        let candidate=h31(x,y);
        for j in 0..6 {
            let (hn,hd)=exact_h[2*j+1];
            assert_eq!(candidate[j],F::rat(hn,hd),"candidate H coefficient differs frozen solve j={j}");
        }
    }
    for which31 in [true,false] {
        let hs=if which31{h31(x,y)}else{let q=h31(y,x);[q[0].neg(),q[1].neg(),q[2].neg(),q[3].neg(),q[4].neg(),q[5].neg()]};
        let mut h=F::Z;let mut dh=F::Z;
        for(j,&c)in hs.iter().enumerate(){let d=(2*j+1)as u64;h=h.add(c.mul(n.pow(d)));dh=dh.add(F::i(d as i128).mul(c).mul(n.pow(d-1)));}
        let l=if which31{
            F::i(-(3*xi*xi+7*xi*yi+6*yi*yi)).div(F::i(2*xi*yi))
        }else{
            F::i(6*xi*xi+7*xi*yi+3*yi*yi).div(F::i(2*xi*yi))
        };
        let source_even=if which31{r31.add(r31_neg)}else{r23.add(r23_neg)}.div(F::i(2));
        let parts=[dh.mul(v),F::i(9).mul(x).mul(y).mul(n).mul(h).neg(),
            source_even.mul(v.pow(4)).neg(),l.div(x.mul(y)).mul(v.pow(5))];
        if (xi,yi,ni)==(1,2,1) && which31 {
            let exact=frozen::identity_components(xi,yi,ni,which31);
            for j in 0..4 { assert_eq!(parts[j],F::rat(exact[j].0,exact[j].1),"component mismatch j={j}"); }
        }
        let residual=parts.into_iter().fold(F::Z,|a,b|a.add(b));
        assert_eq!(residual,F::Z,"identity failure p={P} x={xi} y={yi} n={ni} occ={which31}");
    }
    let expected=F::i(3).mul(n.pow(2)).mul(x.sub(y)).mul(x.add(y))
        .mul(n.pow(4).mul(x.pow(2)).mul(y.pow(2)).sub(F::i(7).mul(n.pow(2)).mul(x).mul(y).mul(x.add(y))).add(F::i(5).mul(x.add(y).pow(2))))
        .div(F::i(2).mul(x).mul(y).mul(v.pow(2)));
    assert_eq!(r31.add(r23),expected);
    Some(())
}

fn run<const P:u64>(side:i128)->u64{
    let mut checks=0;
    for x in 1..=side {for y in 1..=side {for n in 1..=side {
        if verify_point::<P>(x,y,n).is_some(){checks+=1;}
    }}}
    checks
}

fn main(){
    let output=env::args().nth(1).expect("output path");
    let side=12_i128;
    let a=run::<1_000_000_007>(side);
    let b=run::<1_000_000_009>(side);
    let c=run::<998_244_353>(side);
    let json=format!(
        "{{\n  \"schema\":\"marici.occurrence-source-identity.v2\",\n  \"method\":\"independent_frozen_bivariate_source_series_over_prime_fields\",\n  \"primitive_parity\":\"odd\",\n  \"source_numerator_projection\":\"even_part_(P(n)+P(-n))/2\",\n  \"highest_odd_primitive_degree\":11,\n  \"h31_n11\":\"-x^3*y^3*(x+y)/2\",\n  \"h23_n11\":\"+x^3*y^3*(x+y)/2\",\n  \"grid_side\":{},\n  \"primes\":[1000000007,1000000009,998244353],\n  \"valid_points_per_prime\":[{},{},{}],\n  \"occurrence_identities_per_valid_point\":2,\n  \"unsplit_checks_per_valid_point\":1,\n  \"all_checks_passed\":true,\n  \"new_carrier_incidence\":false\n}}\n",side,a,b,c);
    fs::write(output,json).expect("write certificate");
}
