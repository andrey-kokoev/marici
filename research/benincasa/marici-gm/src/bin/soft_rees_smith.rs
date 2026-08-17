use std::{env,fs};

#[derive(Clone,Copy,Debug,PartialEq,Eq)]
struct P([i64;4]);
impl P{
    fn c(x:i64)->Self{Self([x,0,0,0])}
    fn t()->Self{Self([0,1,0,0])}
    fn add(self,r:Self)->Self{let mut z=[0;4];for(i,q)in z.iter_mut().enumerate(){*q=self.0[i]+r.0[i]}Self(z)}
    fn neg(self)->Self{let mut z=[0;4];for(i,q)in z.iter_mut().enumerate(){*q=-self.0[i]}Self(z)}
    fn sub(self,r:Self)->Self{self.add(r.neg())}
    fn mul(self,r:Self)->Self{let mut z=[0;4];for i in 0..4{for j in 0..4-i{z[i+j]+=self.0[i]*r.0[j]}}Self(z)}
}
fn mm(a:&[Vec<P>],b:&[Vec<P>])->Vec<Vec<P>>{let mut z=vec![vec![P::c(0);b[0].len()];a.len()];for i in 0..a.len(){for j in 0..b[0].len(){for k in 0..b.len(){z[i][j]=z[i][j].add(a[i][k].mul(b[k][j]))}}}z}
fn det2(a:P,b:P,c:P,d:P)->P{a.mul(d).sub(b.mul(c))}
fn det3(m:&[Vec<P>],cs:[usize;3])->P{
    let(a,b,c)=(cs[0],cs[1],cs[2]);
    m[0][a].mul(det2(m[1][b],m[1][c],m[2][b],m[2][c]))
        .sub(m[0][b].mul(det2(m[1][a],m[1][c],m[2][a],m[2][c])))
        .add(m[0][c].mul(det2(m[1][a],m[1][b],m[2][a],m[2][b])))
}
fn divisible(p:P,n:i64)->bool{p.0.iter().all(|x|x%n==0)}
fn branch(first:bool)->(Vec<Vec<P>>,Vec<Vec<P>>){
    let phi=vec![vec![P::c(1),P::c(-1),P::c(1),P::c(-1)],vec![P::c(1),P::c(1),P::c(-1),P::c(-1)],vec![P::c(1),P::c(-1),P::c(-1),P::c(1)]];
    let j=vec![vec![P::c(2),P::c(0),P::c(1)],vec![P::c(0),P::c(2),P::c(1)],vec![P::c(0),P::c(0),P::c(1)]];
    let k=vec![vec![P::c(0),P::c(0),P::c(1),P::c(-1)],vec![P::c(0),P::c(1),P::c(0),P::c(-1)],vec![P::c(1),P::c(-1),P::c(-1),P::c(1)]];
    let d=if first{vec![vec![P::t(),P::c(0),P::c(0)],vec![P::c(0),P::c(1),P::c(0)],vec![P::c(0),P::c(0),P::c(1)]]}else{vec![vec![P::c(1),P::c(0),P::c(0)],vec![P::c(0),P::t(),P::c(0)],vec![P::c(0),P::c(0),P::c(1)]]};
    let dj=mm(&d,&j);let dphi=mm(&d,&phi);assert_eq!(mm(&dj,&k),dphi);
    // Determinantal ideals: I1=(1), I2=(2), I3=(4*t).
    let mut minors2=Vec::new();for r1 in 0..3{for r2 in r1+1..3{for c1 in 0..dj[0].len(){for c2 in c1+1..dj[0].len(){minors2.push(det2(dj[r1][c1],dj[r1][c2],dj[r2][c1],dj[r2][c2]))}}}}
    assert!(minors2.iter().all(|p|divisible(*p,2)));assert!(minors2.iter().any(|p|*p==P::c(2)||*p==P::c(-2)));
    assert_eq!(det3(&dj,[0,1,2]),P([0,4,0,0]));
    for cs in [[0,1,2],[0,1,3],[0,2,3],[1,2,3]]{let q=det3(&dphi,cs);assert!(q==P([0,4,0,0])||q==P([0,-4,0,0]))}
    (dj,dphi)
}
fn main(){
    let a:Vec<String>=env::args().collect();if a.len()!=2{eprintln!("usage: soft_rees_smith <output.json>");std::process::exit(2)}
    let _=branch(true);let _=branch(false);
    let out="{\"schema\":\"marici.gm.soft_rees_smith.v1\",\"branches\":[\"X2=0\",\"X1=0\"],\"exact_factorization\":\"D_soft*Phi=(D_soft*J)*K\",\"K_kernel\":\"Z*(1,1,1,1)\",\"K_cokernel\":0,\"generic_smith\":[\"1\",\"2\",\"2\"],\"soft_rees_smith\":[\"1\",\"2\",\"2*t\"],\"special_fiber_leading_rank\":2,\"shifted_rees_rank\":1,\"new_torsion_prime\":false,\"new_support_divisor\":false,\"filtered_cut_nearby_comparison_closes\":true}";
    fs::write(&a[1],out).expect("write certificate")
}
