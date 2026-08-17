use std::{collections::BTreeMap,env,fs};

#[derive(Clone,Debug,PartialEq,Eq)]
struct P(BTreeMap<(u8,u8),i64>);
impl P{
    fn c(n:i64)->Self{let mut z=BTreeMap::new();if n!=0{z.insert((0,0),n);}Self(z)}
    fn x()->Self{let mut z=BTreeMap::new();z.insert((1,0),1);Self(z)}
    fn y()->Self{let mut z=BTreeMap::new();z.insert((0,1),1);Self(z)}
    fn add(&self,r:&Self)->Self{let mut z=self.0.clone();for(m,c)in &r.0{let q=z.get(m).copied().unwrap_or(0)+c;if q==0{z.remove(m);}else{z.insert(*m,q);}}Self(z)}
    fn neg(&self)->Self{Self(self.0.iter().map(|(m,c)|(*m,-c)).collect())}
    fn sub(&self,r:&Self)->Self{self.add(&r.neg())}
    fn mul(&self,r:&Self)->Self{let mut z=Self::c(0);for((i,j),a)in &self.0{for((k,l),b)in &r.0{let mut q=BTreeMap::new();q.insert((i+k,j+l),a*b);z=z.add(&Self(q));}}z}
    fn scale(&self,n:i64)->Self{self.mul(&Self::c(n))}
}
fn mm(a:&[Vec<P>],b:&[Vec<P>])->Vec<Vec<P>>{let mut z=vec![vec![P::c(0);b[0].len()];a.len()];for i in 0..a.len(){for j in 0..b[0].len(){for k in 0..b.len(){z[i][j]=z[i][j].add(&a[i][k].mul(&b[k][j]))}}}z}
fn det2(a:&P,b:&P,c:&P,d:&P)->P{a.mul(d).sub(&b.mul(c))}
fn det3(m:&[Vec<P>])->P{
    m[0][0].mul(&det2(&m[1][1],&m[1][2],&m[2][1],&m[2][2]))
        .sub(&m[0][1].mul(&det2(&m[1][0],&m[1][2],&m[2][0],&m[2][2])))
        .add(&m[0][2].mul(&det2(&m[1][0],&m[1][1],&m[2][0],&m[2][1])))
}
fn main(){
    let a:Vec<String>=env::args().collect();if a.len()!=2{eprintln!("usage: double_soft_rees <output.json>");std::process::exit(2)}
    let z=P::c(0);let o=P::c(1);let x=P::x();let y=P::y();
    let phi=vec![vec![P::c(1),P::c(-1),P::c(1),P::c(-1)],vec![P::c(1),P::c(1),P::c(-1),P::c(-1)],vec![P::c(1),P::c(-1),P::c(-1),P::c(1)]];
    let j=vec![vec![P::c(2),z.clone(),o.clone()],vec![z.clone(),P::c(2),o.clone()],vec![z.clone(),z.clone(),o.clone()]];
    let k=vec![vec![z.clone(),z.clone(),o.clone(),P::c(-1)],vec![z.clone(),o.clone(),z.clone(),P::c(-1)],vec![o.clone(),P::c(-1),P::c(-1),o.clone()]];
    let d=vec![vec![y.clone(),z.clone(),z.clone()],vec![z.clone(),x.clone(),z.clone()],vec![z.clone(),z.clone(),o.clone()]];
    let dj=mm(&d,&j);let dphi=mm(&d,&phi);assert_eq!(mm(&dj,&k),dphi);
    // Unimodular rows R1<-R1-yR3, R2<-R2-xR3.
    let mut normal=dj.clone();for c in 0..3{normal[0][c]=normal[0][c].sub(&y.mul(&normal[2][c]));normal[1][c]=normal[1][c].sub(&x.mul(&normal[2][c]));}
    assert_eq!(normal,vec![vec![y.scale(2),z.clone(),z.clone()],vec![z.clone(),x.scale(2),z.clone()],vec![z.clone(),z.clone(),o.clone()]]);
    assert_eq!(det3(&dj),x.mul(&y).scale(4));
    let mut minors=Vec::new();for r1 in 0..3{for r2 in r1+1..3{for c1 in 0..3{for c2 in c1+1..3{minors.push(det2(&dj[r1][c1],&dj[r1][c2],&dj[r2][c1],&dj[r2][c2]));}}}}
    assert!(minors.contains(&x.scale(2)));assert!(minors.contains(&y.scale(2)));
    let out="{\"schema\":\"marici.gm.double_soft_rees.v1\",\"base_ring\":\"Z[x,y]\",\"exact_factorization\":\"diag(y,x,1)*Phi=(diag(y,x,1)*J)*K\",\"unimodular_presentation\":[\"1\",\"2*x\",\"2*y\"],\"fitting_ideals\":{\"I1\":\"(1)\",\"I2\":\"(2*x,2*y)\",\"I3\":\"(4*x*y)\"},\"ordinary_origin_rank\":1,\"x_rees_rank\":1,\"y_rees_rank\":1,\"total_multirees_rank\":3,\"one_variable_smith_form_applicable\":false,\"new_torsion_prime\":false,\"new_irreducible_support\":false,\"new_carrier_datum\":false}";
    fs::write(&a[1],out).expect("write certificate")
}
