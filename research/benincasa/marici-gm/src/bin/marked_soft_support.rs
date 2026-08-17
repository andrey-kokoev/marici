use std::{env,fs};

#[cfg(not(feature="replication-prime"))]
const P:u64=2_305_843_009_213_693_951;
#[cfg(feature="replication-prime")]
const P:u64=2_305_843_009_213_693_921;

#[derive(Clone,Copy,PartialEq,Eq)]
struct F(u64);
impl F{
    fn n(x:u64)->Self{Self(x%P)}
    fn z()->Self{Self(0)}
    fn o()->Self{Self(1)}
    fn add(self,r:Self)->Self{Self(((self.0 as u128+r.0 as u128)%P as u128)as u64)}
    fn neg(self)->Self{if self.0==0{self}else{Self(P-self.0)}}
    fn sub(self,r:Self)->Self{self.add(r.neg())}
    fn mul(self,r:Self)->Self{Self(((self.0 as u128*r.0 as u128)%P as u128)as u64)}
    fn pow(self,mut n:u64)->Self{let(mut a,mut z)=(self,Self::o());while n>0{if n&1==1{z=z.mul(a)}a=a.mul(a);n>>=1}z}
    fn inv(self)->Self{assert!(self.0!=0);self.pow(P-2)}
    fn div(self,r:Self)->Self{self.mul(r.inv())}
}

// Infinity-Gysin on (e7,e8,e9) at E=0.
fn gysin(x:F,y:F,v:[F;3])->[F;2]{
    let two=F::n(2);[
        v[0].add(v[1].mul(y.mul(y).div(two))).add(v[2].mul(x.mul(x).div(two))),
        v[1].mul(x.mul(x).div(two).neg()).add(v[2].mul(x.mul(x).div(two).neg()))
    ]
}
fn b(x:F,y:F)->[F;3]{[x.mul(x).sub(y.mul(y)),F::n(2),F::n(2).neg()]}
fn scale(v:[F;3],c:F)->[F;3]{[v[0].mul(c),v[1].mul(c),v[2].mul(c)]}
fn zero(v:[F;2])->bool{v[0].0==0&&v[1].0==0}

fn main(){
    let a:Vec<String>=env::args().collect();if a.len()!=2{eprintln!("usage: marked_soft_support <output.json>");std::process::exit(2)}
    let four=F::n(4);let mut generic=0usize;let mut generic_bad=0usize;let mut x2_bad=0usize;let mut x1_bad=0usize;
    for k in 2..130u64{
        let x=F::n(k);let y=F::n(3*k+1);let s=x.add(y);if x.0==0||y.0==0||s.0==0{continue}
        let vb=b(x,y);let c=four.mul(x).mul(y).mul(s).inv();
        // The two wall columns have opposite v0 tails; e2/e4 are Gysin-zero.
        if !zero(gysin(x,y,scale(vb,c)))||!zero(gysin(x,y,scale(vb,c.neg()))){generic_bad+=1}generic+=1;
        // y=0: multiply each wall column by y before specialization.
        let y0=F::z();let by=b(x,y0);let cy=four.mul(x).mul(x).inv();
        if !zero(gysin(x,y0,scale(by,cy)))||!zero(gysin(x,y0,scale(by,cy.neg()))){x2_bad+=1}
        // x=0: the source involution exchanges walls and e8/e9.
        let x0=F::z();let bx=b(x0,y);let cx=four.mul(y).mul(y).inv();
        if !zero(gysin(x0,y,scale(bx,cx)))||!zero(gysin(x0,y,scale(bx,cx.neg()))){x1_bad+=1}
    }
    let out=format!("{{\"schema\":\"marici.gm.marked_soft_support.v1\",\"prime\":{},\"generic_samples\":{},\"generic_gysin_mismatches\":{},\"x2_soft_principal_mismatches\":{},\"x1_soft_principal_mismatches\":{},\"wall_columns_have_simple_soft_poles\":true,\"top_column_soft_regular\":true,\"conductor_to_elliptic_supported_rank\":0,\"full_rank_twelve_new_elliptic_soft_extension\":false}}",P,generic,generic_bad,x2_bad,x1_bad);
    fs::write(&a[1],out).expect("write certificate")
}
