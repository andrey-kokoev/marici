use std::collections::{BTreeMap, BTreeSet};
use std::env;
use std::fs;
use std::time::Instant;

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
struct F { v: u64, p: u64 }
impl F {
    fn new(v:u64,p:u64)->Self{Self{v:v%p,p}}
    fn z(p:u64)->Self{Self::new(0,p)}
    fn o(p:u64)->Self{Self::new(1,p)}
    fn add(self,b:Self)->Self{debug_assert_eq!(self.p,b.p);Self::new(((self.v as u128+b.v as u128)%self.p as u128) as u64,self.p)}
    fn neg(self)->Self{if self.v==0{self}else{Self::new(self.p-self.v,self.p)}}
    fn sub(self,b:Self)->Self{self.add(b.neg())}
    fn mul(self,b:Self)->Self{debug_assert_eq!(self.p,b.p);Self::new(((self.v as u128*b.v as u128)%self.p as u128) as u64,self.p)}
    fn pow(mut self,mut n:u64)->Self{let mut r=Self::o(self.p);while n>0{if n&1==1{r=r.mul(self)}self=self.mul(self);n>>=1;}r}
    fn inv(self)->Self{assert!(self.v!=0);self.pow(self.p-2)}
    fn div(self,b:Self)->Self{self.mul(b.inv())}
}
#[derive(Clone, Copy)]
struct D { x:F, d:F }
impl D {
    fn c(x:F)->Self{Self{x,d:F::z(x.p)}}
    fn var(x:F)->Self{Self{x,d:F::o(x.p)}}
    fn add(self,b:Self)->Self{Self{x:self.x.add(b.x),d:self.d.add(b.d)}}
    fn neg(self)->Self{Self{x:self.x.neg(),d:self.d.neg()}}
    fn sub(self,b:Self)->Self{self.add(b.neg())}
    fn mul(self,b:Self)->Self{Self{x:self.x.mul(b.x),d:self.d.mul(b.x).add(self.x.mul(b.d))}}
    fn sq(self)->Self{self.mul(self)}
}

type Mon=(u8,u8);
#[derive(Clone,Debug)]
struct Poly { t:BTreeMap<Mon,F>, p:u64 }
impl Poly {
    fn zero(p:u64)->Self{Self{t:BTreeMap::new(),p}}
    fn mon(i:u8,j:u8,c:F)->Self{let mut q=Self::zero(c.p);if c.v!=0{q.t.insert((i,j),c);}q}
    fn add(&self,b:&Self)->Self{let mut r=self.clone();for(m,c)in &b.t{let v=r.t.get(m).copied().unwrap_or(F::z(self.p)).add(*c);if v.v==0{r.t.remove(m);}else{r.t.insert(*m,v);}}r}
    fn neg(&self)->Self{let mut r=Self::zero(self.p);for(m,c)in &self.t{r.t.insert(*m,c.neg());}r}
    fn sub(&self,b:&Self)->Self{self.add(&b.neg())}
    fn scale(&self,c:F)->Self{let mut r=Self::zero(self.p);if c.v==0{return r}for(m,v)in &self.t{r.t.insert(*m,v.mul(c));}r}
    fn mul(&self,b:&Self)->Self{let mut r=Self::zero(self.p);for((i,j),c)in &self.t{for((k,l),d)in &b.t{let m=(i+k,j+l);let v=r.t.get(&m).copied().unwrap_or(F::z(self.p)).add(c.mul(*d));if v.v==0{r.t.remove(&m);}else{r.t.insert(m,v);}}}r}
    fn pow(&self,n:usize)->Self{let mut r=Self::mon(0,0,F::o(self.p));for _ in 0..n{r=r.mul(self);}r}
    fn da(&self)->Self{let mut r=Self::zero(self.p);for((i,j),c)in &self.t{if *i>0{r.t.insert((i-1,*j),c.mul(F::new(*i as u64,self.p)));}}r}
    fn db(&self)->Self{let mut r=Self::zero(self.p);for((i,j),c)in &self.t{if *j>0{r.t.insert((*i,j-1),c.mul(F::new(*j as u64,self.p)));}}r}
}

#[derive(Clone)]
struct Geometry { k:Poly,kp:Poly,k1:Poly,k1p:Poly }

fn dual_geometry(uu:u64,vv:u64,axis:&str,p:u64)->Geometry{
    let two=F::new(2,p); let half=two.inv(); let one=F::o(p);
    let u=if axis=="u"{D::var(F::new(uu,p))}else{D::c(F::new(uu,p))};
    let v=if axis=="v"{D::var(F::new(vv,p))}else{D::c(F::new(vv,p))};
    let x=D::c(one);
    let y=u.add(v).mul(D::c(half)).sub(x);
    let z=u.sub(v).mul(D::c(half));
    let c=u.neg();
    let h=x.sq().add(y.sq()).sub(z.sq());
    let ga=x.sq().sub(c.sq()).mul(x.sq().sub(y.sq()).sub(z.sq()))
        .sub(c.sq().mul(z.sq()).mul(D::c(two)));
    let gb=y.sq().sub(c.sq()).mul(y.sq().sub(x.sq()).sub(z.sq()))
        .sub(c.sq().mul(z.sq()).mul(D::c(two)));
    let hh=z.sq().mul(c.sq().sub(y.sq()).mul(c.sq().sub(x.sq())).add(c.sq().mul(z.sq())));
    let mut k=Poly::zero(p); let mut kp=Poly::zero(p);
    for (m,d) in [((4,0),x.sq()),((2,2),h.neg()),((0,4),y.sq()),
                  ((2,0),ga),((0,2),gb),((0,0),hh)]{
        if d.x.v!=0{k.t.insert(m,d.x);} if d.d.v!=0{kp.t.insert(m,d.d);}
    }
    // dK/dc from the closed quartic expression.
    let k1a=c.mul(D::c(two.neg())).mul(x.sq().sub(y.sq()).add(z.sq()));
    let k1b=c.mul(D::c(two.neg())).mul(y.sq().sub(x.sq()).add(z.sq()));
    let k1h=c.mul(D::c(two)).mul(z.sq()).mul(c.sq().mul(D::c(two)).sub(x.sq()).sub(y.sq()).add(z.sq()));
    let mut k1=Poly::zero(p);let mut k1p=Poly::zero(p);
    for(m,d)in [((2,0),k1a),((0,2),k1b),((0,0),k1h)]{
        if d.x.v!=0{k1.t.insert(m,d.x);}if d.d.v!=0{k1p.t.insert(m,d.d);}
    }
    Geometry{k,kp,k1,k1p}
}
trait DMul{fn mul(self,b:Self)->Self;}
impl DMul for D{fn mul(self,b:Self)->Self{D::mul(self,b)}}

fn monomials(deg:u8,par:(u8,u8))->Vec<Mon>{
    let mut r=Vec::new();for s in 0..=deg{for i in 0..=s{let j=s-i;if i%2==par.0&&j%2==par.1{r.push((i,j));}}}r
}
fn exact_col(k:&Poly,ka:&Poly,kb:&Poly,m:Mon,axis:char,three_half:F)->Poly{
    let q=Poly::mon(m.0,m.1,F::o(k.p));
    if axis=='U'{k.mul(&q.da()).sub(&q.mul(ka).scale(three_half))}
    else{k.mul(&q.db()).neg().add(&q.mul(kb).scale(three_half))}
}
fn rank_solve(mut a:Vec<Vec<F>>,nvars:usize)->Option<Vec<F>>{
    let rows=a.len();if rows==0{return Some(vec![])}let p=a[0][0].p;let mut piv=Vec::new();let mut r=0;
    for c in 0..nvars{let mut q=r;while q<rows&&a[q][c].v==0{q+=1}if q==rows{continue}
        a.swap(r,q);let inv=a[r][c].inv();for j in c..=nvars{a[r][j]=a[r][j].mul(inv);}
        for i in 0..rows{if i!=r&&a[i][c].v!=0{let f=a[i][c];for j in c..=nvars{a[i][j]=a[i][j].sub(f.mul(a[r][j]));}}}
        piv.push((r,c));r+=1;if r==rows{break}
    }
    for i in 0..rows{if (0..nvars).all(|j|a[i][j].v==0)&&a[i][nvars].v!=0{return None}}
    let mut x=vec![F::z(p);nvars];for(row,col)in piv{x[col]=a[row][nvars];}Some(x)
}
fn reduce(g:&Geometry,master:usize,deg:u8)->Option<Vec<F>>{
    let p=g.k.p;let inv2=F::new(2,p).inv();let three2=F::new(3,p).mul(inv2);
    let one=Poly::mon(0,0,F::o(p));let a2=Poly::mon(2,0,F::o(p));let b2=Poly::mon(0,2,F::o(p));
    let simple=[one.clone(),a2.clone(),b2.clone()];
    let d=g.k1.scale(inv2.neg());
    let basis=[d.mul(&g.k),simple[0].mul(&g.k.pow(2)),simple[1].mul(&g.k.pow(2)),simple[2].mul(&g.k.pow(2))];
    let target=if master==0{
        let dp=g.k1p.scale(inv2.neg());
        dp.mul(&g.k).sub(&d.mul(&g.kp).scale(three2))
    }else{
        simple[master-1].mul(&g.kp).mul(&g.k).scale(inv2.neg())
    };
    let um=monomials(deg,(1,0));let vm=monomials(deg,(0,1));
    let ka=g.k.da();let kb=g.k.db();let mut cols=basis.to_vec();
    for m in &um{cols.push(exact_col(&g.k,&ka,&kb,*m,'U',three2));}
    for m in &vm{cols.push(exact_col(&g.k,&ka,&kb,*m,'V',three2));}
    let mut mons=BTreeSet::new();for q in &cols{mons.extend(q.t.keys().copied());}mons.extend(target.t.keys().copied());
    let mut mat=Vec::new();for m in mons{let mut row=Vec::new();for q in &cols{row.push(q.t.get(&m).copied().unwrap_or(F::z(p)));}row.push(target.t.get(&m).copied().unwrap_or(F::z(p)));mat.push(row);}
    let sol=rank_solve(mat,cols.len())?;
    let mut check=Poly::zero(p);for(q,c)in cols.iter().zip(&sol){check=check.add(&q.scale(*c));}
    assert!(target.sub(&check).t.is_empty());
    Some(sol[..4].to_vec())
}
const PRIME:u64=2_305_843_009_213_693_951u64;

fn sample_rows(uu:u64,vv:u64,axis:&str)->(Vec<Vec<F>>,Vec<u8>){
    let g=dual_geometry(uu,vv,axis,PRIME);let mut rows=Vec::new();let mut degrees=Vec::new();
    for m in 0..4{let mut got=None;for d in [3,5,7,9,11]{if let Some(x)=reduce(&g,m,d){got=Some(x);degrees.push(d);break}}rows.push(got.expect("reduction failed"));}
    (rows,degrees)
}
fn matrix_json(rows:&[Vec<F>])->String{
    let mut out=String::from("[");
    for(i,r)in rows.iter().enumerate(){if i>0{out.push(',');}out.push('[');for(j,x)in r.iter().enumerate(){if j>0{out.push(',');}out.push_str(&x.v.to_string());}out.push(']');}
    out.push(']');out
}
fn main(){
    let a:Vec<String>=env::args().collect();
    if a.len()>=2&&a[1]=="sample"{
        if a.len()!=5&&a.len()!=6{eprintln!("usage: marici-gm sample <u> <v> <u|v> [output.json]");std::process::exit(2)}
        let uu=a[2].parse::<u64>().unwrap();let vv=a[3].parse::<u64>().unwrap();let axis=&a[4];let now=Instant::now();
        let(rows,degrees)=sample_rows(uu,vv,axis);
        let out=format!("{{\"schema\":\"marici.gm.modular_sample.v1\",\"prime\":{},\"u\":{},\"v\":{},\"axis\":\"{}\",\"elapsed_ms\":{},\"degrees\":{:?},\"matrix\":{}}}",PRIME,uu,vv,axis,now.elapsed().as_millis(),degrees,matrix_json(&rows));
        if a.len()==6{fs::write(&a[5],&out).expect("write output");}else{println!("{}",out);}return
    }
    if a.len()==8&&a[1]=="grid"{
        let u0=a[2].parse::<u64>().unwrap();let nu=a[3].parse::<u64>().unwrap();let v0=a[4].parse::<u64>().unwrap();let nv=a[5].parse::<u64>().unwrap();let axis=&a[6];let now=Instant::now();
        let mut out=format!("{{\"schema\":\"marici.gm.modular_grid.v1\",\"prime\":{},\"axis\":\"{}\",\"samples\":[",PRIME,axis);let mut first=true;
        for i in 0..nu{for j in 0..nv{let u=u0+i;let v=v0+j;let(rows,degrees)=sample_rows(u,v,axis);if !first{out.push(',');}first=false;out.push_str(&format!("{{\"u\":{},\"v\":{},\"degrees\":{:?},\"matrix\":{}}}",u,v,degrees,matrix_json(&rows)));}}
        out.push_str(&format!("],\"elapsed_ms\":{}}}",now.elapsed().as_millis()));fs::write(&a[7],out).expect("write grid");return
    }
    eprintln!("usage: marici-gm sample ... | grid <u0> <nu> <v0> <nv> <u|v> <output.json>");std::process::exit(2)
}

#[cfg(test)]
mod tests{
    use super::*;
    #[test] fn reproduces_total_slice_at_seven(){
        let(rows,degrees)=sample_rows(7,1,"u");
        let want:[[u64;4];4]=[
            [916575037758175253,0,0,0],
            [2066775673810267488,10980204805779495,776353728253454378,1136038062601973655],
            [1411268463833130372,757634131598785154,895510984251959450,1874475197337142653],
            [640083510918851506,1943496250622970620,234302514087206097,388778204774535347]];
        assert_eq!(degrees,vec![5,7,7,7]);
        for i in 0..4{for j in 0..4{assert_eq!(rows[i][j].v,want[i][j]);}}
    }
}
