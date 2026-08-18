use std::collections::BTreeMap;

const P:u64=2_305_843_009_213_693_951;
#[derive(Clone,Copy,PartialEq,Eq)]
struct F(u64);
impl F {
    fn n(x:u64)->Self{Self(x%P)}
    fn z()->Self{Self(0)}
    fn o()->Self{Self(1)}
    fn add(self,x:Self)->Self{Self::n(((self.0 as u128+x.0 as u128)%P as u128) as u64)}
    fn neg(self)->Self{if self.0==0{self}else{Self(P-self.0)}}
    fn mul(self,x:Self)->Self{Self::n(((self.0 as u128*x.0 as u128)%P as u128) as u64)}
    fn pow(mut self,mut n:u64)->Self{let mut r=Self::o();while n>0{if n&1==1{r=r.mul(self)}self=self.mul(self);n>>=1}r}
    fn inv(self)->Self{self.pow(P-2)}
}
type Mon=(i32,i32); // first variable, b
#[derive(Clone)]
struct Poly(BTreeMap<Mon,F>);
impl Poly {
    fn z()->Self{Self(BTreeMap::new())}
    fn one()->Self{Self::mon(0,0,F::o())}
    fn mon(x:i32,b:i32,c:F)->Self{let mut p=Self::z();if c!=F::z(){p.0.insert((x,b),c);}p}
    fn add(&self,q:&Self)->Self{let mut r=self.clone();for(m,c)in&q.0{let v=r.0.get(m).copied().unwrap_or(F::z()).add(*c);if v==F::z(){r.0.remove(m);}else{r.0.insert(*m,v);}}r}
    fn scale(&self,c:F)->Self{Self(self.0.iter().filter_map(|(m,x)|{let v=x.mul(c);if v==F::z(){None}else{Some((*m,v))}}).collect())}
    fn mul(&self,q:&Self)->Self{let mut r=Self::z();for((x,b),c)in&self.0{for((y,d),e)in&q.0{r=r.add(&Self::mon(x+y,b+d,c.mul(*e)));}}r}
    fn pow(&self,n:usize)->Self{(0..n).fold(Self::one(),|r,_|r.mul(self))}
    fn db(&self)->Self{Self(self.0.iter().filter_map(|((x,b),c)|if *b==0{None}else{Some(((*x,b-1),c.mul(F::n(*b as u64))))}).collect())}
}

fn second_chart(p:&Poly,alpha_shift:i32)->Poly {
    let mut out=Poly::z();
    for((s,b),c)in p.0.iter(){
        out=out.add(&Poly::mon(alpha_shift-2*s,*b,*c));
    }
    out
}

// Remainder modulo psi=alpha^2+(1-b^2)/2, using
// alpha^2=(b^2-1)/2.  The result has alpha degree at most one.
fn remainder_mod_psi(p:&Poly)->Poly {
    let half=F::n(2).inv();
    let beta=Poly::mon(0,2,half).add(&Poly::mon(0,0,half.neg()));
    let mut out=Poly::z();
    for((a,b),c)in&p.0 {
        assert!(*a>=0);
        let k=(*a as usize)/2;
        let parity=*a%2;
        out=out.add(&Poly::mon(parity,*b,*c).mul(&beta.pow(k)));
    }
    out
}

fn main(){
    let half=F::n(2).inv();
    let s=Poly::mon(1,0,F::o());
    let b=Poly::mon(0,1,F::o());
    let one=Poly::one();
    let c=one.add(&b);
    let d=one.add(&b.pow(2).scale(F::o().neg()));
    let phi=one.add(&s.mul(&d).scale(half));
    let f=phi.pow(2);
    let kb=s.mul(&b).mul(&phi).scale(F::n(2).neg());
    let ka=phi.scale(F::n(4));
    let mut tested=0usize;
    let mut minimum_alpha=i32::MAX;
    let mut failures=Vec::new();
    for (sa,sb) in [(1usize,1usize),(1,0),(0,1),(0,0)] {
        let ea=2-sa;
        let eb=2-sb;
        for i in 0..=32usize { for j in 0..=32usize {
            let bj=b.pow(j);
            let mut pp=bj.db().mul(&c.pow(ea)).mul(&f).scale(F::o().neg());
            if sa==1 {pp=pp.add(&bj.mul(&c.pow(ea-1)).mul(&f));}
            pp=pp.add(&bj.mul(&c.pow(ea)).mul(&kb).scale(F::n(3).mul(half)));
            let mut qq=bj.mul(&c.pow(ea)).mul(&f).scale(F::n(i as u64));
            if sb==1 {qq=qq.add(&bj.mul(&c.pow(ea)).mul(&f).scale(F::o().neg()));}
            qq=qq.add(&bj.mul(&c.pow(ea)).mul(&ka).scale(F::n(3).mul(half).neg()));
            for(name,raw,shift)in[
                ("p",pp,i as i32+eb as i32+4),
                ("q",qq,i as i32+eb as i32+3)
            ]{
                let transformed=second_chart(&raw,shift);
                let min=transformed.0.keys().map(|m|m.0).min().unwrap_or(0);
                minimum_alpha=minimum_alpha.min(min);
                let divisible=remainder_mod_psi(&transformed).0.is_empty();
                if min<0||!divisible{failures.push(format!("{name}:sa{sa}:sb{sb}:i{i}:j{j}:min{min}:div{divisible}"));}
                tested+=1;
            }
        }}
    }
    assert!(failures.is_empty(),"{:?}",&failures[..failures.len().min(8)]);
    // psi=0 is alpha^2=(b^2-1)/2.  It is smooth at alpha=0,b=+/-1
    // because partial_b psi=-b is nonzero there; projection to b has
    // simple ramification and deck involution alpha -> -alpha.
    println!("{{\"schema\":\"marici.benincasa.weighted_second_chart.v2\",\"stacky_atlas\":\"u=tau^2,a=tau*alpha\",\"coarse_coordinate\":\"t=alpha^2\",\"exceptional_equation\":\"psi^2=0\",\"psi\":\"alpha^2+(1-b^2)/2\",\"tested_coefficients\":{tested},\"index_box\":\"0<=i,j<=32; all four sectors; p and q\",\"minimum_alpha_exponent\":{minimum_alpha},\"all_transforms_regular\":true,\"all_exact_coefficients_divisible_by_psi\":true,\"atlas_reduced_quotient\":\"F[alpha,b]/(psi)\",\"coarse_reduced_section\":\"F[b]\",\"points_over_b_plus_minus_1\":[\"(alpha,b)=(0,1)\",\"(alpha,b)=(0,-1)\"],\"smooth_at_these_points\":true,\"mu2_atlas_involution\":\"alpha->-alpha\",\"physical_time_root_identification\":\"NOT_ASSERTED\"}}");
}
