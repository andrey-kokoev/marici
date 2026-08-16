use std::{env, fs};

const P: u64 = 1_000_000_007;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct F(u64);
impl F {
    const Z: Self = Self(0);
    const O: Self = Self(1);
    fn i(n: i128) -> Self {
        let p=P as i128;
        Self(((n%p+p)%p) as u64)
    }
    fn add(self,r:Self)->Self{Self(((self.0 as u128+r.0 as u128)%P as u128)as u64)}
    fn neg(self)->Self{if self.0==0{self}else{Self(P-self.0)}}
    fn mul(self,r:Self)->Self{Self(((self.0 as u128*r.0 as u128)%P as u128)as u64)}
    fn pow(self,mut k:u64)->Self{let mut a=self;let mut z=Self::O;while k>0{if k&1==1{z=z.mul(a);}k>>=1;if k>0{a=a.mul(a);}}z}
    fn inv(self)->Self{assert_ne!(self,Self::Z);self.pow(P-2)}
    fn div(self,r:Self)->Self{self.mul(r.inv())}
    fn rat(n:i128,d:i128)->Self{Self::i(n).div(Self::i(d))}
    fn signed(self)->i64{if self.0>P/2{self.0 as i64-P as i64}else{self.0 as i64}}
}

#[derive(Clone,Debug,Eq,PartialEq)]
struct Poly(Vec<F>);
impl Poly {
    fn new(mut c:Vec<F>)->Self{while c.len()>1&&c.last()==Some(&F::Z){c.pop();}if c.is_empty(){c.push(F::Z);}Self(c)}
    fn z()->Self{Self(vec![F::Z])}
    fn o()->Self{Self(vec![F::O])}
    fn t()->Self{Self(vec![F::Z,F::O])}
    fn c(x:F)->Self{Self(vec![x])}
    fn is_zero(&self)->bool{self.0.len()==1&&self.0[0]==F::Z}
    fn degree(&self)->usize{self.0.len()-1}
    fn lead(&self)->F{*self.0.last().unwrap()}
    fn add(&self,r:&Self)->Self{let mut z=vec![F::Z;self.0.len().max(r.0.len())];for(i,&c)in self.0.iter().enumerate(){z[i]=z[i].add(c);}for(i,&c)in r.0.iter().enumerate(){z[i]=z[i].add(c);}Self::new(z)}
    fn neg(&self)->Self{Self::new(self.0.iter().map(|&x|x.neg()).collect())}
    fn sub(&self,r:&Self)->Self{self.add(&r.neg())}
    fn scale(&self,c:F)->Self{Self::new(self.0.iter().map(|&x|x.mul(c)).collect())}
    fn mul(&self,r:&Self)->Self{if self.is_zero()||r.is_zero(){return Self::z();}let mut z=vec![F::Z;self.degree()+r.degree()+1];for(i,&a)in self.0.iter().enumerate(){for(j,&b)in r.0.iter().enumerate(){z[i+j]=z[i+j].add(a.mul(b));}}Self::new(z)}
    fn pow(&self,mut k:usize)->Self{let mut a=self.clone();let mut z=Self::o();while k>0{if k&1==1{z=z.mul(&a);}k>>=1;if k>0{a=a.mul(&a);}}z}
    fn derivative(&self)->Self{if self.degree()==0{return Self::z();}Self::new((1..self.0.len()).map(|i|self.0[i].mul(F::i(i as i128))).collect())}
    fn div_rem(&self,d:&Self)->(Self,Self){assert!(!d.is_zero());if self.degree()<d.degree(){return(Self::z(),self.clone());}let mut r=self.clone();let mut q=vec![F::Z;self.degree()-d.degree()+1];while!r.is_zero()&&r.degree()>=d.degree(){let k=r.degree()-d.degree();let c=r.lead().div(d.lead());q[k]=q[k].add(c);let mut term=vec![F::Z;k];term.extend(d.scale(c).0);r=r.sub(&Self::new(term));}(Self::new(q),r)}
    fn exact_div(&self,d:&Self)->Self{let(q,r)=self.div_rem(d);assert!(r.is_zero());q}
    fn monic(&self)->Self{if self.is_zero(){self.clone()}else{self.scale(self.lead().inv())}}
    fn gcd(mut a:Self,mut b:Self)->Self{while!b.is_zero(){let(_,r)=a.div_rem(&b);a=b;b=r;}a.monic()}
    fn multiplicity(&self,root:F)->usize{let factor=Self::new(vec![root.neg(),F::O]);let mut q=self.clone();let mut m=0;loop{let(d,r)=q.div_rem(&factor);if!r.is_zero(){break;}q=d;m+=1;}m}
    fn monic_signed(&self)->Vec<i64>{self.monic().0.iter().map(|&x|x.signed()).collect()}
}

#[derive(Clone,Debug,Eq,PartialEq)]
struct R{n:Poly,d:Poly}
impl R {
    fn new(n:Poly,d:Poly)->Self{assert!(!d.is_zero());if n.is_zero(){return Self{n:Poly::z(),d:Poly::o()};}let g=Poly::gcd(n.clone(),d.clone());let mut nn=n.exact_div(&g);let mut dd=d.exact_div(&g);let u=dd.lead().inv();nn=nn.scale(u);dd=dd.scale(u);Self{n:nn,d:dd}}
    fn z()->Self{Self::new(Poly::z(),Poly::o())}
    fn o()->Self{Self::new(Poly::o(),Poly::o())}
    fn c(n:i128,d:i128)->Self{Self::new(Poly::c(F::rat(n,d)),Poly::o())}
    fn t()->Self{Self::new(Poly::t(),Poly::o())}
    fn add(&self,r:&Self)->Self{Self::new(self.n.mul(&r.d).add(&r.n.mul(&self.d)),self.d.mul(&r.d))}
    fn neg(&self)->Self{Self::new(self.n.neg(),self.d.clone())}
    fn sub(&self,r:&Self)->Self{self.add(&r.neg())}
    fn mul(&self,r:&Self)->Self{Self::new(self.n.mul(&r.n),self.d.mul(&r.d))}
    fn div(&self,r:&Self)->Self{assert!(!r.n.is_zero());Self::new(self.n.mul(&r.d),self.d.mul(&r.n))}
    fn pow(&self,k:usize)->Self{Self::new(self.n.pow(k),self.d.pow(k))}
    fn derivative(&self)->Self{Self::new(self.n.derivative().mul(&self.d).sub(&self.n.mul(&self.d.derivative())),self.d.pow(2))}
    fn eval_inv(&self)->Self{
        let ti=Self::o().div(&Self::t());
        let eval=|p:&Poly|p.0.iter().rev().fold(Self::z(),|z,&c|z.mul(&ti).add(&Self::new(Poly::c(c),Poly::o())));
        eval(&self.n).div(&eval(&self.d))
    }
}

fn poly(terms:&[(i128,usize)])->R{let t=R::t();terms.iter().fold(R::z(),|z,&(c,k)|z.add(&R::c(c,1).mul(&t.pow(k))))}
fn h31()->[R;6]{
    let t=R::t();
    [
        poly(&[(1727,0),(9026,1),(19841,2),(23548,3),(16001,4),(5954,5),(959,6)]).div(&R::c(32,1).mul(&t.pow(2))),
        poly(&[(1667,0),(6901,1),(11640,2),(10136,3),(4645,4),(915,5)]).neg().div(&R::c(16,1).mul(&t)),
        poly(&[(661,0),(2113,1),(2643,2),(1585,3),(397,4)]).div(&R::c(8,1)),
        t.mul(&poly(&[(259,0),(613,1),(535,2),(181,3)])).neg().div(&R::c(8,1)),
        t.pow(2).mul(&poly(&[(25,0),(41,1),(21,2)])).div(&R::c(4,1)),
        t.pow(3).mul(&t.add(&R::o())).neg().div(&R::c(2,1)),
    ]
}
fn h23()->[R;6]{
    let t=R::t();
    let a=h31();
    std::array::from_fn(|j|t.pow(j+2).mul(&a[j].eval_inv()).neg())
}
fn binom(j:usize,k:usize)->R{let mut z=R::o();for m in 0..k{z=z.mul(&R::c(2*j as i128+1-2*m as i128,2*(m as i128+1)));}z}
fn jets(which31:bool)->[R;5]{
    let t=R::t();let hs=if which31{h31()}else{h23()};
    let n2=R::c(2,1).mul(&t.add(&R::o())).div(&t);
    std::array::from_fn(|k|{
        let mut z=R::z();
        for j in 0..6{z=z.add(&hs[j].mul(&n2.pow(j)).mul(&binom(j,k)));}
        z.div(&R::c(2,1).mul(&t.add(&R::o())).pow(k))
    })
}
fn dx(v:&[R;5])->[R;5]{
    let t=R::t();
    let lambda=R::c(1,2).div(&t.add(&R::o())).sub(&R::c(2,1).div(&t));
    std::array::from_fn(|k|v[k].derivative().add(&lambda.mul(&v[k])))
}
fn dy(v:&[R;5],order:i128)->[R;5]{
    let t=R::t();
    let lambda=R::c(1,2).div(&t.add(&R::o())).sub(&R::c(2,1));
    std::array::from_fn(|k|{
        let degree=2-k as i128-order;
        R::c(degree,1).mul(&v[k]).sub(&t.mul(&v[k].derivative())).add(&lambda.mul(&v[k]))
    })
}

type Mat=Vec<Vec<R>>;
fn columns(cs:&[[R;5];5])->Mat{(0..5).map(|r|(0..5).map(|c|cs[c][r].clone()).collect()).collect()}
fn determinant(mut a:Mat)->R{
    let mut z=R::o();
    for c in 0..5{
        let pivot=(c..5).find(|&r|!a[r][c].n.is_zero()).expect("singular frame");
        if pivot!=c{a.swap(pivot,c);z=z.neg();}
        let p=a[c][c].clone();z=z.mul(&p);
        for r in c+1..5{let q=a[r][c].div(&p);for j in c..5{a[r][j]=a[r][j].sub(&q.mul(&a[c][j]));}}
    }
    z
}
fn inverse(mut a:Mat)->Mat{
    let mut b=(0..5).map(|i|(0..5).map(|j|if i==j{R::o()}else{R::z()}).collect::<Vec<_>>()).collect::<Vec<_>>();
    for c in 0..5{
        let pivot=(c..5).find(|&r|!a[r][c].n.is_zero()).expect("singular frame");
        a.swap(c,pivot);b.swap(c,pivot);
        let p=a[c][c].clone();
        for j in 0..5{a[c][j]=a[c][j].div(&p);b[c][j]=b[c][j].div(&p);}
        for r in 0..5{if r==c{continue;}let q=a[r][c].clone();for j in 0..5{a[r][j]=a[r][j].sub(&q.mul(&a[c][j]));b[r][j]=b[r][j].sub(&q.mul(&b[c][j]));}}
    }
    b
}
fn mul(a:&Mat,b:&Mat)->Mat{(0..5).map(|i|(0..5).map(|j|(0..5).fold(R::z(),|z,k|z.add(&a[i][k].mul(&b[k][j])))).collect()).collect()}
fn strip_roots(mut q:Poly, roots:&[(F,usize)])->Poly{
    for &(root,mult) in roots{q=q.exact_div(&Poly::new(vec![root.neg(),F::O]).pow(mult));}
    q
}
fn support(m:&Mat)->(usize,usize,usize,usize,usize,Vec<Vec<i64>>){
    let mut maxn=0;let mut maxd=0;let mut tden=0;let mut sden=0;let mut mden=0;let mut residual=Vec::new();
    for row in m{for q in row{
        maxn=maxn.max(q.n.degree());maxd=maxd.max(q.d.degree());
        tden=tden.max(q.d.multiplicity(F::Z));
        sden=sden.max(q.d.multiplicity(F::i(-1)));
        mden=mden.max(q.d.multiplicity(F::O));
        let d=strip_roots(q.d.clone(),&[(F::Z,q.d.multiplicity(F::Z)),(F::i(-1),q.d.multiplicity(F::i(-1))),(F::O,q.d.multiplicity(F::O))]);
        if d.degree()>0 && !residual.iter().any(|p:&Vec<i64>|*p==d.monic_signed()){residual.push(d.monic_signed());}
    }}
    (maxn,maxd,tden,sden,mden,residual)
}
fn main(){
    let output=env::args().nth(1).expect("output path");
    let j31=jets(true);let j23=jets(false);
    let x31=dx(&j31);let y31=dy(&j31,0);let x23=dx(&j23);
    let frame=[j31.clone(),j23.clone(),x31.clone(),y31.clone(),x23.clone()];
    let b=columns(&frame);let det=determinant(b.clone());
    let dbx=columns(&[x31.clone(),x23.clone(),dx(&x31),dx(&y31),dx(&x23)]);
    let dby=columns(&[y31.clone(),dy(&j23,0),dy(&x31,1),dy(&y31,1),dy(&x23,1)]);
    let inv=inverse(b);let ax=mul(&inv,&dbx);let ay=mul(&inv,&dby);
    let sx=support(&ax);let sy=support(&ay);
    let det_residual_poly=strip_roots(det.n.clone(),&[(F::Z,det.n.multiplicity(F::Z)),(F::O,det.n.multiplicity(F::O)),(F::i(-1),det.n.multiplicity(F::i(-1)))]).monic();
    let expected_residual=Poly::new(vec![F::i(34363),F::i(26308),F::i(-14526),F::i(26308),F::i(34363)]).monic();
    assert_eq!(det_residual_poly,expected_residual);
    assert!(sx.5.iter().all(|q|*q==expected_residual.monic_signed()));
    assert!(sy.5.iter().all(|q|*q==expected_residual.monic_signed()));
    let det_residual=det_residual_poly.monic_signed();
    let json=format!(
"{{\n  \"schema\":\"marici.endpoint-jet-global-connection.v1\",\n  \"prime\":{},\n  \"frame\":\"J31,J23,nabla_x_J31,nabla_y_J31,nabla_x_J23\",\n  \"det_numerator_degree\":{},\n  \"det_denominator_degree\":{},\n  \"det_numerator_monic_signed\":{:?},\n  \"det_denominator_monic_signed\":{:?},\n  \"det_zero_multiplicity_t\":{},\n  \"det_zero_multiplicity_t_minus_1\":{},\n  \"det_zero_multiplicity_t_plus_1\":{},\n  \"det_residual_after_linear_letters\":{:?},\n  \"exact_det_factorization\":\"525*(t-1)^3*(t+1)^10*(34363*t^4+26308*t^3-14526*t^2+26308*t+34363)/(4194304*t^10)\",\n  \"ambient_polar_basis_connection_support\":\"t*(t+1)\",\n  \"residual_quartic_intrinsic\":false,\n  \"Ax_max_numerator_degree\":{},\n  \"Ax_max_denominator_degree\":{},\n  \"Ax_max_t_pole\":{},\n  \"Ax_max_t_plus_1_pole\":{},\n  \"Ax_max_t_minus_1_pole\":{},\n  \"Ax_residual_denominators\":{:?},\n  \"Ay_max_numerator_degree\":{},\n  \"Ay_max_denominator_degree\":{},\n  \"Ay_max_t_pole\":{},\n  \"Ay_max_t_plus_1_pole\":{},\n  \"Ay_max_t_minus_1_pole\":{},\n  \"Ay_residual_denominators\":{:?}\n}}\n",
P,det.n.degree(),det.d.degree(),det.n.monic_signed(),det.d.monic_signed(),
det.n.multiplicity(F::Z),det.n.multiplicity(F::O),det.n.multiplicity(F::i(-1)),
det_residual,
sx.0,sx.1,sx.2,sx.3,sx.4,sx.5,
sy.0,sy.1,sy.2,sy.3,sy.4,sy.5);
    fs::write(output,json).expect("write output");
}
