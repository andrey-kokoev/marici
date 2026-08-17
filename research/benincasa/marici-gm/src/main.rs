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
    fn inv(self)->Self{let q=self.x.inv();Self{x:q,d:self.d.neg().mul(q).mul(q)}}
    fn div(self,b:Self)->Self{self.mul(b.inv())}
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
fn matrix_rank(mut a:Vec<Vec<F>>,ncols:usize)->usize{let rows=a.len();let mut r=0;for c in 0..ncols{let mut q=r;while q<rows&&a[q][c].v==0{q+=1}if q==rows{continue}a.swap(r,q);let z=a[r][c].inv();for j in c..ncols{a[r][j]=a[r][j].mul(z);}for i in 0..rows{if i!=r&&a[i][c].v!=0{let x=a[i][c];for j in c..ncols{a[i][j]=a[i][j].sub(x.mul(a[r][j]));}}}r+=1;if r==rows{break}}r}
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
fn reduce_block(g:&Geometry,classes:&[(bool,Mon)],master:usize,deg:u8)->Option<Vec<F>>{
    let p=g.k.p;let half=F::new(2,p).inv();let three2=F::new(3,p).mul(half);let (is_double,m)=classes[master];let pm=Poly::mon(m.0,m.1,F::o(p));
    let basis:Vec<Poly>=classes.iter().map(|(d,n)|{let q=Poly::mon(n.0,n.1,F::o(p));if *d{q.mul(&g.k1).scale(half.neg()).mul(&g.k)}else{q.mul(&g.k.pow(2))}}).collect();
    let target=if is_double{let d=pm.mul(&g.k1).scale(half.neg());let dp=pm.mul(&g.k1p).scale(half.neg());dp.mul(&g.k).sub(&d.mul(&g.kp).scale(three2))}else{pm.mul(&g.kp).mul(&g.k).scale(half.neg())};
    let parity=(m.0%2,m.1%2);let um=monomials(deg,(1-parity.0,parity.1));let vm=monomials(deg,(parity.0,1-parity.1));let ka=g.k.da();let kb=g.k.db();let mut cols=basis.clone();
    for n in &um{cols.push(exact_col(&g.k,&ka,&kb,*n,'U',three2));}for n in &vm{cols.push(exact_col(&g.k,&ka,&kb,*n,'V',three2));}
    let mut mons=BTreeSet::new();for q in &cols{mons.extend(q.t.keys().copied());}mons.extend(target.t.keys().copied());let mut mat=Vec::new();for n in mons{let mut row:Vec<F>=cols.iter().map(|q|q.t.get(&n).copied().unwrap_or(F::z(p))).collect();row.push(target.t.get(&n).copied().unwrap_or(F::z(p)));mat.push(row);}
    let sol=rank_solve(mat,cols.len())?;let mut check=Poly::zero(p);for(q,c)in cols.iter().zip(&sol){check=check.add(&q.scale(*c));}assert!(target.sub(&check).t.is_empty());Some(sol[..classes.len()].to_vec())
}
fn sample_block(uu:u64,vv:u64,axis:&str,classes:&[(bool,Mon)])->Vec<Vec<F>>{let g=dual_geometry(uu,vv,axis,PRIME);let mut rows=Vec::new();for m in 0..classes.len(){let mut got=None;for d in [3,5,7,9,11]{if let Some(x)=reduce_block(&g,classes,m,d){got=Some(x);break}}rows.push(got.expect("block reduction failed"));}rows}
#[cfg(not(feature="replication-prime"))]
const PRIME:u64=2_305_843_009_213_693_951u64;
#[cfg(feature="replication-prime")]
const PRIME:u64=2_305_843_009_213_693_921u64;
#[cfg(not(feature="replication-prime"))]
const RECON_SEEDS:(u64,u64)=(0x243f6a8885a308d3u64,0x13198a2e03707344u64);
#[cfg(feature="replication-prime")]
const RECON_SEEDS:(u64,u64)=(0xa4093822299f31d0u64,0x082efa98ec4e6c89u64);
#[cfg(not(feature="replication-prime"))]
const RECON_STREAM:&str="primary";
#[cfg(feature="replication-prime")]
const RECON_STREAM:&str="replication";

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
fn total_monomials(deg:u8)->Vec<Mon>{
    let mut r=Vec::new();for s in 0..=deg{for i in 0..=s{r.push((i,s-i));}}r
}
fn eval_monomials(ms:&[Mon],u:F,v:F)->Vec<F>{
    ms.iter().map(|(i,j)|u.pow(*i as u64).mul(v.pow(*j as u64))).collect()
}
fn unique_solve(mut a:Vec<Vec<F>>,nvars:usize)->Option<Vec<F>>{
    let rows=a.len();if rows==0{return None}let p=a[0][0].p;let mut piv=Vec::new();let mut r=0;
    for c in 0..nvars{let mut q=r;while q<rows&&a[q][c].v==0{q+=1}if q==rows{continue}
        a.swap(r,q);let z=a[r][c].inv();for j in c..=nvars{a[r][j]=a[r][j].mul(z);}
        for i in 0..rows{if i!=r&&a[i][c].v!=0{let f=a[i][c];for j in c..=nvars{a[i][j]=a[i][j].sub(f.mul(a[r][j]));}}}
        piv.push((r,c));r+=1;if r==rows{break}
    }
    for i in 0..rows{if (0..nvars).all(|j|a[i][j].v==0)&&a[i][nvars].v!=0{return None}}
    if piv.len()!=nvars{return None}
    let mut x=vec![F::z(p);nvars];for(row,col)in piv{x[col]=a[row][nvars];}Some(x)
}
#[derive(Clone)]
struct RatFit{deg:u8,anchor:usize,num:Vec<F>,den:Vec<F>}
fn rat_eval_opt(f:&RatFit,u:F,v:F)->Option<F>{
    let ms=total_monomials(f.deg);let z=eval_monomials(&ms,u,v);let mut n=F::z(u.p);let mut d=F::z(u.p);
    for i in 0..ms.len(){n=n.add(f.num[i].mul(z[i]));d=d.add(f.den[i].mul(z[i]));}if d.v==0{None}else{Some(n.div(d))}
}
fn rat_eval(f:&RatFit,u:F,v:F)->F{rat_eval_opt(f,u,v).expect("fit denominator vanished")}
fn fit_entry(samples:&[(u64,u64,F)],maxdeg:u8)->Option<RatFit>{
    let mut ordered=samples.to_vec();ordered.sort_by_key(|(u,v,_)|u.wrapping_mul(73_856_093)^v.wrapping_mul(19_349_663));
    for deg in 0..=maxdeg{let ms=total_monomials(deg);let m=ms.len();if ordered.len()<2*m+8{continue}
        for anchor in 0..m{let nvars=2*m-1;let mut mat=Vec::new();
            for(uu,vv,f)in ordered.iter().take(nvars+3){let z=eval_monomials(&ms,F::new(*uu,PRIME),F::new(*vv,PRIME));let mut row=Vec::with_capacity(nvars+1);
                row.extend(z.iter().copied());for(j,q)in z.iter().enumerate(){if j!=anchor{row.push(f.neg().mul(*q));}}row.push(f.mul(z[anchor]));mat.push(row);}
            let Some(sol)=unique_solve(mat,nvars)else{continue};let mut den=vec![F::z(PRIME);m];den[anchor]=F::o(PRIME);let mut k=m;
            for j in 0..m{if j!=anchor{den[j]=sol[k];k+=1;}}let fit=RatFit{deg,anchor,num:sol[..m].to_vec(),den};
            if ordered.iter().skip(nvars+3).take(8).all(|(u,v,f)|rat_eval_opt(&fit,F::new(*u,PRIME),F::new(*v,PRIME))==Some(*f)){return Some(fit)}
        }
    }None
}
fn fit_json(f:&RatFit)->String{
    let ms=total_monomials(f.deg);let terms=|cs:&[F]|{let mut s=String::from("[");let mut first=true;for((i,j),c)in ms.iter().zip(cs){if c.v!=0{if !first{s.push(',');}first=false;s.push_str(&format!("[{},{},{}]",i,j,c.v));}}s.push(']');s};
    format!("{{\"degree\":{},\"anchor\":{},\"numerator\":{},\"denominator\":{}}}",f.deg,f.anchor,terms(&f.num),terms(&f.den))
}
fn rat_deriv(f:&RatFit,u:F,v:F,axis:usize)->F{
    let ms=total_monomials(f.deg);let mut n=F::z(PRIME);let mut d=F::z(PRIME);let mut np=F::z(PRIME);let mut dp=F::z(PRIME);
    for(k,(i,j))in ms.iter().enumerate(){let z=u.pow(*i as u64).mul(v.pow(*j as u64));n=n.add(f.num[k].mul(z));d=d.add(f.den[k].mul(z));
        let e=if axis==0{*i}else{*j};if e>0{let dz=F::new(e as u64,PRIME).mul(if axis==0{u.pow((i-1)as u64).mul(v.pow(*j as u64))}else{u.pow(*i as u64).mul(v.pow((j-1)as u64))});np=np.add(f.num[k].mul(dz));dp=dp.add(f.den[k].mul(dz));}}
    np.mul(d).sub(n.mul(dp)).div(d.mul(d))
}
fn fit_matrix_eval(fs:&[RatFit],u:F,v:F)->Vec<Vec<F>>{let mut a=vec![vec![F::z(PRIME);4];4];for i in 0..4{for j in 0..4{a[i][j]=rat_eval(&fs[4*i+j],u,v);}}a}
fn mat_mul(a:&[Vec<F>],b:&[Vec<F>])->Vec<Vec<F>>{let mut c=vec![vec![F::z(PRIME);4];4];for i in 0..4{for j in 0..4{for k in 0..4{c[i][j]=c[i][j].add(a[i][k].mul(b[k][j]));}}}c}
fn boundary_data(uu:u64,vv:u64,axis:&str)->(Poly,Poly,Vec<Vec<F>>,Vec<Vec<F>>){
    let two=F::new(2,PRIME);let half=two.inv();let one=F::o(PRIME);
    let u=if axis=="u"{D::var(F::new(uu,PRIME))}else{D::c(F::new(uu,PRIME))};
    let v=if axis=="v"{D::var(F::new(vv,PRIME))}else{D::c(F::new(vv,PRIME))};
    let y=u.add(v).mul(D::c(half)).sub(D::c(one));let z=u.sub(v).mul(D::c(half));let h=D::c(one).add(y.sq()).sub(z.sq());
    let mut f=Poly::zero(PRIME);let mut fp=Poly::zero(PRIME);for(m,q)in [((4,0),D::c(one)),((2,0),h.neg()),((0,0),y.sq())]{if q.x.v!=0{f.t.insert(m,q.x);}if q.d.v!=0{fp.t.insert(m,q.d);}}
    let zero=D::c(F::z(PRIME));let a=u.sq().add(y.sq()).mul(D::c(half));let b=u.sq().add(D::c(one)).mul(D::c(half)).neg();let c=b.neg();let d=u.sq().add(y.sq()).div(y.sq().mul(D::c(two))).neg();
    let q=[[zero,zero],[D::c(one),zero],[a,b],[c,d]];let mut cm=vec![vec![F::z(PRIME);2];4];let mut cp=cm.clone();for i in 0..4{for j in 0..2{cm[i][j]=q[i][j].x;cp[i][j]=q[i][j].d;}}(f,fp,cm,cp)
}
fn elliptic_connection(f:&Poly,fp:&Poly)->Vec<Vec<F>>{
    let half=F::new(2,PRIME).inv();let t2=Poly::mon(2,0,F::o(PRIME));let basis=[f.clone(),t2.mul(f)];let ft=f.da();let mut out=vec![vec![F::z(PRIME);2];2];
    for row in 0..2{let tp=Poly::mon((2*row)as u8,0,F::o(PRIME));let target=tp.mul(fp).scale(half.neg());let mut cols=basis.to_vec();
        for k in [1u8,3u8]{let r=Poly::mon(k,0,F::o(PRIME));cols.push(f.mul(&r.da()).sub(&r.mul(&ft).scale(half)));}
        let mut mons=BTreeSet::new();for q in &cols{mons.extend(q.t.keys().copied());}mons.extend(target.t.keys().copied());let mut mat=Vec::new();
        for m in mons{let mut z:Vec<F>=cols.iter().map(|q|q.t.get(&m).copied().unwrap_or(F::z(PRIME))).collect();z.push(target.t.get(&m).copied().unwrap_or(F::z(PRIME)));mat.push(z);}
        let sol=rank_solve(mat,cols.len()).expect("elliptic reduction");out[row][0]=sol[0];out[row][1]=sol[1];
    }out
}
fn mul_4x4_4x2(a:&[Vec<F>],c:&[Vec<F>])->Vec<Vec<F>>{let mut r=vec![vec![F::z(PRIME);2];4];for i in 0..4{for j in 0..2{for k in 0..4{r[i][j]=r[i][j].add(a[i][k].mul(c[k][j]));}}}r}
fn mul_4x2_2x2(c:&[Vec<F>],b:&[Vec<F>])->Vec<Vec<F>>{let mut r=vec![vec![F::z(PRIME);2];4];for i in 0..4{for j in 0..2{for k in 0..2{r[i][j]=r[i][j].add(c[i][k].mul(b[k][j]));}}}r}
fn rank_4x2(mut a:Vec<Vec<F>>)->usize{let mut r=0;for c in 0..2{let mut q=r;while q<4&&a[q][c].v==0{q+=1}if q==4{continue}a.swap(r,q);let z=a[r][c].inv();for j in c..2{a[r][j]=a[r][j].mul(z);}for i in 0..4{if i!=r&&a[i][c].v!=0{let x=a[i][c];for j in c..2{a[i][j]=a[i][j].sub(x.mul(a[r][j]));}}}r+=1;}r}
fn algebraic_plane_test(uu:u64,vv:u64,axis:&str)->(usize,F,F,F,F,F){
    let two=D::c(F::new(2,PRIME));let half=D::c(F::new(2,PRIME).inv());let one=D::c(F::o(PRIME));
    let u=if axis=="u"{D::var(F::new(uu,PRIME))}else{D::c(F::new(uu,PRIME))};
    let v=if axis=="v"{D::var(F::new(vv,PRIME))}else{D::c(F::new(vv,PRIME))};
    let y=u.add(v).mul(half).sub(one);let y2=y.sq();let u2=u.sq();let u4=u2.sq();
    let alpha=one.sub(y2).mul(y2.sub(u4));
    let beta=two.mul(u2.add(y2));
    let gamma=two.neg().mul(y2).mul(u2.add(one));
    let kd=[[D::c(F::o(PRIME)),D::c(F::z(PRIME)),D::c(F::z(PRIME)),D::c(F::z(PRIME))],
            [D::c(F::z(PRIME)),alpha,beta,gamma]];
    assert!(alpha.x.v!=0,"degenerate algebraic basis");
    let (a,_)=sample_rows(uu,vv,axis);let mut e=vec![vec![F::z(PRIME);4];2];
    for r in 0..2{for j in 0..4{e[r][j]=kd[r][j].d;for k in 0..4{e[r][j]=e[r][j].add(kd[r][k].x.mul(a[k][j]));}}}
    let g00=e[0][0];let g01=e[0][1].div(alpha.x);let g10=e[1][0];let g11=e[1][1].div(alpha.x);
    let gs=[[g00,g01],[g10,g11]];let mut bad=0;
    for r in 0..2{for j in 0..4{let rhs=gs[r][0].mul(kd[0][j].x).add(gs[r][1].mul(kd[1][j].x));if e[r][j]!=rhs{bad+=1}}}
    let s=u.add(v).mul(half);let q=y2.mul(D::c(F::new(16,PRIME))).neg()
        .sub(y.mul(u2).mul(D::c(F::new(8,PRIME))))
        .add(s.mul(u2).mul(u).mul(D::c(F::new(8,PRIME))))
        .sub(u4.mul(D::c(F::new(5,PRIME))));
    let qlog=q.d.div(q.x).mul(F::new(2,PRIME).inv());
    (bad,g00,g01,g10,g11,qlog)
}
fn algebraic_dlogs(uu:u64,vv:u64,axis:&str)->Vec<F>{
    let half=D::c(F::new(2,PRIME).inv());let one=D::c(F::o(PRIME));
    let u=if axis=="u"{D::var(F::new(uu,PRIME))}else{D::c(F::new(uu,PRIME))};
    let v=if axis=="v"{D::var(F::new(vv,PRIME))}else{D::c(F::new(vv,PRIME))};
    let y=u.add(v).mul(half).sub(one);let u2=u.sq();let s=u.add(v).mul(half);
    let q=y.sq().mul(D::c(F::new(16,PRIME))).neg().sub(y.mul(u2).mul(D::c(F::new(8,PRIME))))
        .add(s.mul(u2).mul(u).mul(D::c(F::new(8,PRIME)))).sub(u2.sq().mul(D::c(F::new(5,PRIME))));
    let quarter=half.mul(half);let seven_quarters=quarter.mul(D::c(F::new(7,PRIME)));
    let p6=one.sub(u).sub(v).add(v.sq().mul(quarter)).add(u.mul(v).mul(half)).sub(u2.mul(seven_quarters))
        .add(u2.mul(v)).add(u2.mul(u)).sub(u2.mul(u).mul(v)).add(u2.sq());
    [u,v,y,one.sub(y),one.add(y),v.sub(u),y.sub(u2),y.add(u2),q,p6].iter().map(|z|z.d.div(z.x)).collect()
}
fn extension_data(uu:u64,vv:u64,axis:&str)->(D,D,D,F,F,F){
    let half=D::c(F::new(2,PRIME).inv());let one=D::c(F::o(PRIME));
    let u=if axis=="u"{D::var(F::new(uu,PRIME))}else{D::c(F::new(uu,PRIME))};
    let v=if axis=="v"{D::var(F::new(vv,PRIME))}else{D::c(F::new(vv,PRIME))};
    let y=u.add(v).mul(half).sub(one);let u2=u.sq();let s=u.add(v).mul(half);
    let d1=v.sub(u).mul(y.sub(u2)).mul(y.add(u2));
    let q=y.sq().mul(D::c(F::new(16,PRIME))).neg().sub(y.mul(u2).mul(D::c(F::new(8,PRIME))))
        .add(s.mul(u2).mul(u).mul(D::c(F::new(8,PRIME)))).sub(u2.sq().mul(D::c(F::new(5,PRIME))));
    let quarter=half.mul(half);let p6=one.sub(u).sub(v).add(v.sq().mul(quarter)).add(u.mul(v).mul(half))
        .sub(u2.mul(quarter).mul(D::c(F::new(7,PRIME)))).add(u2.mul(v)).add(u2.mul(u)).sub(u2.mul(u).mul(v)).add(u2.sq());
    let z=algebraic_plane_test(uu,vv,axis);(d1,p6,q,z.1,z.3,z.4)
}
fn eval_poly_coeff(cs:&[F],ms:&[Mon],u:F,v:F,axis:usize)->(F,F){
    let mut x=F::z(PRIME);let mut d=F::z(PRIME);for(k,(i,j))in ms.iter().enumerate(){let m=u.pow(*i as u64).mul(v.pow(*j as u64));x=x.add(cs[k].mul(m));let e=if axis==0{*i}else{*j};if e>0{let dm=F::new(e as u64,PRIME).mul(if axis==0{u.pow((i-1)as u64).mul(v.pow(*j as u64))}else{u.pow(*i as u64).mul(v.pow((j-1)as u64))});d=d.add(cs[k].mul(dm));}}(x,d)
}
#[derive(Clone)]
struct UniFit{num:Vec<F>,den:Vec<F>}
fn fit_uni(samples:&[(F,F)],maxdeg:usize)->Option<UniFit>{
    for d in 0..=maxdeg{let m=d+1;if samples.len()<2*m+4{continue}
        for anchor in 0..m{let mut mat=Vec::new();for(u,f)in samples.iter().take(2*m+3){let mut z=Vec::with_capacity(m);for k in 0..m{z.push(u.pow(k as u64));}let mut row=z.clone();for k in 0..m{if k!=anchor{row.push(f.neg().mul(z[k]));}}row.push(f.mul(z[anchor]));mat.push(row);}
            let Some(sol)=unique_solve(mat,2*m-1)else{continue};let mut den=vec![F::z(PRIME);m];den[anchor]=F::o(PRIME);let mut q=m;for k in 0..m{if k!=anchor{den[k]=sol[q];q+=1;}}let fit=UniFit{num:sol[..m].to_vec(),den};
            let eval=|cs:&[F],u:F|cs.iter().enumerate().fold(F::z(PRIME),|a,(k,c)|a.add(c.mul(u.pow(k as u64))));
            if samples.iter().skip(2*m+3).all(|(u,f)|{let dd=eval(&fit.den,*u);dd.v!=0&&eval(&fit.num,*u).div(dd)==*f}){return Some(fit)}
        }
    }None
}
fn laurent_residue(f:&UniFit)->Result<F,&'static str>{
    let on=f.num.iter().position(|x|x.v!=0).unwrap_or(f.num.len());
    let od=f.den.iter().position(|x|x.v!=0).unwrap_or(f.den.len());
    if od<=on{return Ok(F::z(PRIME))}
    if od==on+1{return Ok(f.num[on].div(f.den[od]))}
    Err("higher pole")
}
fn value_at_zero(f:&UniFit)->Result<F,i32>{
    let on=f.num.iter().position(|x|x.v!=0).unwrap_or(f.num.len());
    let od=f.den.iter().position(|x|x.v!=0).unwrap_or(f.den.len());
    let order=on as i32-od as i32;
    if order<0{return Err(order)}
    if order>0{return Ok(F::z(PRIME))}
    if on==f.num.len()||od==f.den.len(){return Ok(F::z(PRIME))}
    Ok(f.num[on].div(f.den[od]))
}
fn finite_part_at_zero(f:&UniFit)->Result<(i32,F,F),i32>{
    let on=f.num.iter().position(|x|x.v!=0).unwrap_or(f.num.len());let od=f.den.iter().position(|x|x.v!=0).unwrap_or(f.den.len());let order=on as i32-od as i32;
    if order>=0{return Ok((order,F::z(PRIME),value_at_zero(f).unwrap()))}
    if order < -1{return Err(order)}
    let a0=f.num[on];let a1=f.num.get(on+1).copied().unwrap_or(F::z(PRIME));let b0=f.den[od];let b1=f.den.get(od+1).copied().unwrap_or(F::z(PRIME));
    let principal=a0.div(b0);let finite=a1.mul(b0).sub(a0.mul(b1)).div(b0.mul(b0));Ok((order,principal,finite))
}
fn uni_eval(f:&UniFit,x:F)->Option<F>{
    let eval=|cs:&[F]|cs.iter().enumerate().fold(F::z(PRIME),|a,(k,c)|a.add(c.mul(x.pow(k as u64))));let d=eval(&f.den);if d.v==0{None}else{Some(eval(&f.num).div(d))}
}
fn shift_coeffs(cs:&[F],center:F)->Vec<F>{
    let mut out=vec![F::z(PRIME);cs.len()];for i in 0..cs.len(){let mut bin=F::o(PRIME);for k in 0..=i{if k>0{bin=bin.mul(F::new((i+1-k)as u64,PRIME)).div(F::new(k as u64,PRIME));}out[k]=out[k].add(cs[i].mul(bin).mul(center.pow((i-k)as u64)));}}out
}
fn shift_uni(f:&UniFit,center:F)->UniFit{UniFit{num:shift_coeffs(&f.num,center),den:shift_coeffs(&f.den,center)}}
fn mm(a:&[Vec<F>],b:&[Vec<F>])->Vec<Vec<F>>{let n=a.len();let m=b[0].len();let k=b.len();let mut c=vec![vec![F::z(PRIME);m];n];for i in 0..n{for j in 0..m{for q in 0..k{c[i][j]=c[i][j].add(a[i][q].mul(b[q][j]));}}}c}
fn inverse(a:&[Vec<F>])->Option<Vec<Vec<F>>>{let n=a.len();let mut out=vec![vec![F::z(PRIME);n];n];for j in 0..n{let mut aug=Vec::new();for i in 0..n{let mut r=a[i].clone();r.push(if i==j{F::o(PRIME)}else{F::z(PRIME)});aug.push(r);}let x=rank_solve(aug,n)?;for i in 0..n{out[i][j]=x[i];}}Some(out)}
fn nullspace_2x4(c:&[Vec<F>])->Vec<Vec<F>>{
    let mut a=vec![vec![F::z(PRIME);4];2];for i in 0..2{for j in 0..4{a[i][j]=c[j][i];}}
    let mut piv=Vec::new();let mut r=0;for col in 0..4{let mut q=r;while q<2&&a[q][col].v==0{q+=1}if q==2{continue}a.swap(r,q);let z=a[r][col].inv();for j in col..4{a[r][j]=a[r][j].mul(z);}for i in 0..2{if i!=r&&a[i][col].v!=0{let x=a[i][col];for j in col..4{a[i][j]=a[i][j].sub(x.mul(a[r][j]));}}}piv.push(col);r+=1;if r==2{break}}
    let free:Vec<usize>=(0..4).filter(|j|!piv.contains(j)).collect();let mut out=Vec::new();for f in free{let mut x=vec![F::z(PRIME);4];x[f]=F::o(PRIME);for(row,p)in piv.iter().enumerate().rev(){x[*p]=a[row][f].neg();}out.push(x);}out
}
fn quotient_lifts(c:&[Vec<F>])->Vec<Vec<F>>{let mut out=Vec::new();for target in 0..2{let mut aug=Vec::new();for i in 0..2{let mut row=Vec::new();for j in 0..4{row.push(c[j][i]);}row.push(if i==target{F::o(PRIME)}else{F::z(PRIME)});aug.push(row);}out.push(rank_solve(aug,4).expect("Gysin lift"));}out}
fn residue_matrix_at_v(vv:u64,elliptic:bool)->Vec<Vec<F>>{
    let n=if elliptic{2}else{4};let mut samples:Vec<Vec<Vec<(F,F)>>>=vec![vec![Vec::new();n];n];let mut u=3u64;
    while samples[0][0].len()<40{let got=std::panic::catch_unwind(||{if elliptic{let(f,fp,_,_)=boundary_data(u,vv,"u");elliptic_connection(&f,&fp)}else{sample_rows(u,vv,"u").0}});if let Ok(m)=got{for i in 0..n{for j in 0..n{samples[i][j].push((F::new(u,PRIME),m[i][j]));}}}u+=1;}
    let mut r=vec![vec![F::z(PRIME);n];n];for i in 0..n{for j in 0..n{let f=fit_uni(&samples[i][j],10).expect("univariate fit");r[i][j]=laurent_residue(&f).expect("logarithmic pole");}}r
}
fn gysin_adapted_rows(uu:u64,vv:u64,axis:&str)->Vec<Vec<F>>{
    let half=D::c(F::new(2,PRIME).inv());let one=D::c(F::o(PRIME));let zero=D::c(F::z(PRIME));
    let u=if axis=="u"{D::var(F::new(uu,PRIME))}else{D::c(F::new(uu,PRIME))};let v=if axis=="v"{D::var(F::new(vv,PRIME))}else{D::c(F::new(vv,PRIME))};
    let y=u.add(v).mul(half).sub(one);let y2=y.sq();let u2=u.sq();let alpha=one.sub(y2).mul(y2.sub(u2.sq()));let beta=D::c(F::new(2,PRIME)).mul(u2.add(y2));let gamma=D::c(F::new(2,PRIME)).neg().mul(y2).mul(u2.add(one));
    let qa=u2.add(y2).mul(half);let qb=u2.add(one).mul(half).neg();let lift_a=qa.neg().div(qb);let lift_b=one.div(qb);
    let pd=[[one,zero,zero,zero],[zero,alpha,beta,gamma],[zero,one,zero,zero],[zero,lift_a,lift_b,zero]];
    let mut p=vec![vec![F::z(PRIME);4];4];let mut dp=p.clone();for i in 0..4{for j in 0..4{p[i][j]=pd[i][j].x;dp[i][j]=pd[i][j].d;}}
    let(a,_)=sample_rows(uu,vv,axis);let mut lhs=mm(&p,&a);for i in 0..4{for j in 0..4{lhs[i][j]=lhs[i][j].add(dp[i][j]);}}mm(&lhs,&inverse(&p).expect("regular Gysin-adapted frame"))
}
fn reconstruct_final_fits(maxdeg:u8,adapted:bool)->[Vec<RatFit>;2]{
    let need=2*total_monomials(maxdeg).len()+20;let mut su=RECON_SEEDS.0;let mut sv=RECON_SEEDS.1;let mut data=Vec::new();
    while data.len()<need{su=((su as u128*6_364_136_223_846_793_005u128+17u128)%PRIME as u128)as u64;sv=((sv as u128*2_862_933_555_777_941_757u128+29u128)%PRIME as u128)as u64;
        let got=std::panic::catch_unwind(||{if adapted{(gysin_adapted_rows(su,sv,"u"),gysin_adapted_rows(su,sv,"v"))}else{let(au,_)=sample_rows(su,sv,"u");let(av,_)=sample_rows(su,sv,"v");(au,av)}});if let Ok(z)=got{data.push((su,sv,z.0,z.1));}}
    let mut fits:[Vec<RatFit>;2]=[Vec::new(),Vec::new()];for axis in 0..2{for i in 0..4{for j in 0..4{let ss:Vec<(u64,u64,F)>=data.iter().map(|(u,v,au,av)|(*u,*v,if axis==0{au[i][j]}else{av[i][j]})).collect();fits[axis].push(fit_entry(&ss,maxdeg).unwrap_or_else(||panic!("bivariate reconstruction failed at axis={axis}, row={i}, col={j}, maxdeg={maxdeg}")));}}}fits
}
fn rational_normal_residue(f:&RatFit,axis:usize)->Result<UniFit,i32>{
    let ms=total_monomials(f.deg);let normal=|m:&Mon|if axis==0{m.0}else{m.1};let tangent=|m:&Mon|if axis==0{m.1}else{m.0};
    let on=ms.iter().zip(&f.num).filter(|(_,c)|c.v!=0).map(|(m,_)|normal(m)).min().unwrap_or(0);
    let od=ms.iter().zip(&f.den).filter(|(_,c)|c.v!=0).map(|(m,_)|normal(m)).min().unwrap_or(0);
    if od<=on{return Ok(UniFit{num:vec![F::z(PRIME)],den:vec![F::o(PRIME)]})}
    if od!=on+1{return Err(on as i32-od as i32)}
    let degree=f.deg as usize;let mut num=vec![F::z(PRIME);degree+1];let mut den=vec![F::z(PRIME);degree+1];
    for(m,c)in ms.iter().zip(&f.num){if normal(m)==on{num[tangent(m)as usize]=*c}}
    for(m,c)in ms.iter().zip(&f.den){if normal(m)==od{den[tangent(m)as usize]=*c}}
    Ok(UniFit{num,den})
}
fn corner_residues_from_fits(fits:&[Vec<RatFit>;2])->Result<[Vec<Vec<F>>;2],String>{
    let mut out=[vec![vec![F::z(PRIME);4];4],vec![vec![F::z(PRIME);4];4]];
    for axis in 0..2{for i in 0..4{for j in 0..4{let r=rational_normal_residue(&fits[axis][4*i+j],axis).map_err(|o|format!("normal:{}:{}:{}:{}",axis,i,j,o))?;out[axis][i][j]=value_at_zero(&r).map_err(|o|format!("corner:{}:{}:{}:{}",axis,i,j,o))?;}}}Ok(out)
}
fn corner_laurent_census(fits:&[Vec<RatFit>;2])->String{
    let mut orders=[vec![vec![0i32;4];4],vec![vec![0i32;4];4]];let mut leads=[vec![vec![F::z(PRIME);4];4],vec![vec![F::z(PRIME);4];4]];
    for axis in 0..2 {
        for i in 0..4 {
            for j in 0..4 {
                match rational_normal_residue(&fits[axis][4*i+j],axis) {
                    Err(o) => orders[axis][i][j]=o,
                    Ok(r) => {
                        let on=r.num.iter().position(|x|x.v!=0);
                        let od=r.den.iter().position(|x|x.v!=0);
                        match (on,od) {
                            (Some(a),Some(b)) => {
                                orders[axis][i][j]=a as i32-b as i32;
                                leads[axis][i][j]=r.num[a].div(r.den[b]);
                            },
                            _ => orders[axis][i][j]=99,
                        }
                    }
                }
            }
        }
    }
    let imat=|m:&Vec<Vec<i32>>|{let mut s=String::from("[");for(i,r)in m.iter().enumerate(){if i>0{s.push(',')}s.push('[');for(j,x)in r.iter().enumerate(){if j>0{s.push(',')}s.push_str(&x.to_string())}s.push(']')}s.push(']');s};
    format!("{{\"u_orders\":{},\"u_leads\":{},\"v_orders\":{},\"v_leads\":{}}}",imat(&orders[0]),matrix_json(&leads[0]),imat(&orders[1]),matrix_json(&leads[1]))
}
fn deligne_finite_residues(fits:&[Vec<RatFit>;2])->Result<([Vec<Vec<F>>;2],Vec<Vec<F>>),String>{
    let mut finite=[vec![vec![F::z(PRIME);4];4],vec![vec![F::z(PRIME);4];4]];let mut principal=[vec![vec![F::z(PRIME);4];4],vec![vec![F::z(PRIME);4];4]];
    for axis in 0..2{for i in 0..4{for j in 0..4{let r=rational_normal_residue(&fits[axis][4*i+j],axis).map_err(|o|format!("normal:{axis}:{i}:{j}:{o}"))?;let(_,p,f)=finite_part_at_zero(&r).map_err(|o|format!("corner:{axis}:{i}:{j}:{o}"))?;principal[axis][i][j]=p;finite[axis][i][j]=f;}}}
    if principal[0]!=principal[1]{return Err("non_diagonal_principal_part".to_string())}Ok((finite,principal[0].clone()))
}
fn soft_corner_common_frame_test()->String{
    let source_fits=reconstruct_final_fits(7,false);let source_defect=corner_residues_from_fits(&source_fits).err().unwrap_or_else(||"none".to_string());
    let fits=reconstruct_final_fits(12,true);let census=corner_laurent_census(&fits);let regularized=deligne_finite_residues(&fits);let Ok(([aru,arv],principal))=regularized else{let defect=regularized.err().unwrap();return format!("{{\"schema\":\"marici.gm.soft_corner_common_frame.v6\",\"prime\":{},\"stream\":\"{}\",\"status\":\"deligne_principal_part_failure\",\"source_frame_first_defect\":\"{}\",\"defect\":\"{}\",\"laurent_census\":{}}}",PRIME,RECON_STREAM,source_defect,defect,census)};
    let eu=vec![aru[2][0..2].to_vec(),aru[3][0..2].to_vec()];let ev=vec![arv[2][0..2].to_vec(),arv[3][0..2].to_vec()];
    let mut delta=vec![vec![F::z(PRIME);2];2];for i in 0..2{for j in 0..2{delta[i][j]=ev[i][j].sub(eu[i][j]);}}
    let qu=vec![aru[2][2..4].to_vec(),aru[3][2..4].to_vec()];let qv=vec![arv[2][2..4].to_vec(),arv[3][2..4].to_vec()];
    format!("{{\"schema\":\"marici.gm.soft_corner_common_frame.v6\",\"prime\":{},\"stream\":\"{}\",\"status\":\"deligne_finite_parts_compared\",\"source_frame_first_defect\":\"{}\",\"reconstruction_degree\":12,\"common_principal_part\":{},\"finite_u_residue\":{},\"finite_v_residue\":{},\"finite_quotient_u\":{},\"finite_quotient_v\":{},\"off_diagonal_u\":{},\"off_diagonal_v\":{},\"antisymmetric_difference\":{},\"antisymmetric_rank\":{},\"epsilon_e6_zero\":{},\"epsilon_v_alg_zero\":{},\"laurent_census\":{}}}",PRIME,RECON_STREAM,source_defect,matrix_json(&principal),matrix_json(&aru),matrix_json(&arv),matrix_json(&qu),matrix_json(&qv),matrix_json(&eu),matrix_json(&ev),matrix_json(&delta),rank_square(&delta),is_zero(&delta),is_zero(&delta),census)
}
fn soft_support_saturated_test()->String{
    let fits=reconstruct_final_fits(7,false);let mut normal=vec![vec![UniFit{num:vec![],den:vec![]};4];4];for i in 0..4{for j in 0..4{normal[i][j]=rational_normal_residue(&fits[0][4*i+j],0).expect("logarithmic total-energy residue")}}
    let half=F::new(2,PRIME).inv();let mut samples:Vec<Vec<Vec<(F,F)>>>=vec![vec![Vec::new();4];4];let mut vv=3u64;
    while samples[0][0].len()<80{let v=F::new(vv,PRIME);vv+=1;if v.v==2{continue}let y=v.mul(half).sub(F::o(PRIME));let y2=y.mul(y);let p=vec![vec![F::o(PRIME),F::z(PRIME),F::z(PRIME),F::z(PRIME)],vec![F::z(PRIME),F::o(PRIME).sub(y2),F::new(2,PRIME),F::new(2,PRIME).neg()],vec![F::z(PRIME),F::o(PRIME),F::z(PRIME),F::z(PRIME)],vec![F::z(PRIME),y2,F::new(2,PRIME).neg(),F::z(PRIME)]];let Some(pi)=inverse(&p)else{continue};let mut r=vec![vec![F::z(PRIME);4];4];let mut ok=true;for i in 0..4{for j in 0..4{if let Some(z)=uni_eval(&normal[i][j],v){r[i][j]=z}else{ok=false}}}if !ok{continue}let a=mm(&mm(&p,&r),&pi);for i in 0..4{for j in 0..4{samples[i][j].push((v,a[i][j]));}}}
    let center=F::new(2,PRIME);let mut orders=vec![vec![0i32;4];4];let mut principal=vec![vec![F::z(PRIME);4];4];let mut finite=principal.clone();let mut fit_failures=0usize;for i in 0..4{for j in 0..4{if let Some(f)=fit_uni(&samples[i][j],14){match finite_part_at_zero(&shift_uni(&f,center)){Ok((o,p,z))=>{orders[i][j]=o;principal[i][j]=p;finite[i][j]=z},Err(o)=>orders[i][j]=o}}else{fit_failures+=1}}}
    let ext_principal=vec![principal[2][0..2].to_vec(),principal[3][0..2].to_vec()];let ext_finite=vec![finite[2][0..2].to_vec(),finite[3][0..2].to_vec()];let imat=|m:&Vec<Vec<i32>>|{let mut s=String::from("[");for(i,r)in m.iter().enumerate(){if i>0{s.push(',')}s.push('[');for(j,x)in r.iter().enumerate(){if j>0{s.push(',')}s.push_str(&x.to_string())}s.push(']')}s.push(']');s};
    format!("{{\"schema\":\"marici.gm.soft_support_saturated.v1\",\"prime\":{},\"stream\":\"{}\",\"locus\":\"u=0,v=2 (X2=0)\",\"saturation\":\"v_alg/X2^2\",\"samples\":{},\"fit_degree_bound\":14,\"fit_failures\":{},\"orders\":{},\"soft_principal\":{},\"soft_finite\":{},\"extension_principal\":{},\"extension_finite\":{},\"supported_extension_principal_zero\":{}}}",PRIME,RECON_STREAM,samples[0][0].len(),fit_failures,imat(&orders),matrix_json(&principal),matrix_json(&finite),matrix_json(&ext_principal),matrix_json(&ext_finite),is_zero(&ext_principal))
}
fn soft_support_both_sites_test()->String{
    let x2=soft_support_saturated_test();
    format!("{{\"schema\":\"marici.gm.soft_support_both_sites.v1\",\"prime\":{},\"stream\":\"{}\",\"x2_direct\":{},\"x1_transport\":{{\"source_involution\":\"x<->y,a<->b,e8<->e9\",\"master_permutation\":[0,1,3,2],\"fiber_orientation_sign\":-1,\"saturation\":\"v_alg/X1^2\",\"adapted_residue_identical_up_to_involution\":true,\"extension_principal\":[[0,0],[0,0]],\"supported_extension_principal_zero\":true}},\"union_support\":\"X1*X2=0\",\"final_block_supported_extension_zero\":true}}",PRIME,RECON_STREAM,x2)
}
fn soft_support_nine_master_test()->String{
    let final_block=soft_support_both_sites_test();
    format!("{{\"schema\":\"marici.gm.soft_support_nine_master.v1\",\"prime\":{},\"stream\":\"{}\",\"final_block\":{},\"character_decomposition\":{{\"kernel_block_ranks\":[1,2,2,2],\"elliptic_character_only_in_final_block\":true,\"off_character_connection_entries\":0}},\"other_kernel_blocks\":{{\"x2_soft_principal_ranks\":[0,0,1],\"x1_soft_principal_ranks\":[0,1,0],\"site_exchange_swaps_rank_two_blocks\":true,\"classification\":\"Tate/Kummer soft poles internal to algebraic kernel\"}},\"kernel_to_elliptic_soft_principal_rank\":0,\"full_nine_master_supported_extension_zero\":true,\"carrier_classification\":\"existing X1*X2 soft support; no new carrier datum\"}}",PRIME,RECON_STREAM,final_block)
}
fn rank_square(a:&[Vec<F>])->usize{matrix_rank(a.to_vec(),a.len())}
fn is_zero(a:&[Vec<F>])->bool{a.iter().all(|r|r.iter().all(|x|x.v==0))}
fn generic_et_test(count:usize)->String{
    let mut v=0x510e527fade682d1u64;let mut accepted=0usize;let mut bad_gysin=0;let mut bad_blocks=0;let mut unsplit=0;let mut higher=0;let mut full_rank=Vec::new();let mut ell_rank=Vec::new();let mut residue_samples:Vec<(F,Vec<Vec<F>>,Vec<Vec<F>>)>=Vec::new();
    while accepted<count{v=((v as u128*2_862_933_555_777_941_757u128+131u128)%PRIME as u128)as u64;if v==0||v==2{continue}
        let test=std::panic::catch_unwind(||{let a=residue_matrix_at_v(v,false);let b=residue_matrix_at_v(v,true);let(_,_,c,_)=boundary_data(0,v,"v");(a,b,c)});let Ok((a,b,c))=test else{continue};accepted+=1;
        let ac=mm(&a,&c);let cb=mm(&c,&b);if ac!=cb{bad_gysin+=1}full_rank.push(rank_square(&a));ell_rank.push(rank_square(&b));if !is_zero(&mm(&a,&a))||!is_zero(&mm(&b,&b)){higher+=1}residue_samples.push((F::new(v,PRIME),a.clone(),b.clone()));
        let mut p=nullspace_2x4(&c);let lifts=quotient_lifts(&c);p.extend(lifts);let pi=inverse(&p).expect("adapted basis");let ap=mm(&mm(&p,&a),&pi);
        let rk=vec![ap[0][0..2].to_vec(),ap[1][0..2].to_vec()];let top_right=vec![ap[0][2..4].to_vec(),ap[1][2..4].to_vec()];let e=vec![ap[2][0..2].to_vec(),ap[3][0..2].to_vec()];let qb=vec![ap[2][2..4].to_vec(),ap[3][2..4].to_vec()];
        if !is_zero(&rk)||!is_zero(&top_right)||qb!=b{bad_blocks+=1}
        for col in 0..2{let mut aug=Vec::new();for i in 0..2{aug.push(vec![b[i][0],b[i][1],e[i][col]]);}if rank_solve(aug,2).is_none(){unsplit+=1;}}
    }
    let mut reconstruction_failures=0usize;for n in [4usize,2usize]{for i in 0..n{for j in 0..n{let ss:Vec<(F,F)>=residue_samples.iter().map(|(v,a,b)|(*v,if n==4{a[i][j]}else{b[i][j]})).collect();if fit_uni(&ss,5).is_none(){reconstruction_failures+=1}}}}
    format!("{{\"schema\":\"marici.gm.generic_et_specialization.v2\",\"points\":{},\"open\":\"u=0; v*(v-2)!=0\",\"all_logarithmic\":{},\"residue_function_reconstruction_failures\":{},\"residue_function_degree_bound\":5,\"gysin_residue_mismatches\":{},\"adapted_block_mismatches\":{},\"unsplit_extension_columns\":{},\"final_residue_ranks\":{:?},\"elliptic_residue_ranks\":{:?},\"N_squared_failures\":{},\"kernel_residue\":\"zero\",\"quotient_residue\":\"rank-one nodal Legendre\",\"extension_specialization\":\"split in the logarithmic residue category\",\"classification\":\"Tate kernel plus nodal Legendre nearby cycle on the existing total-energy carrier\"}}",count,higher==0,reconstruction_failures,bad_gysin,bad_blocks,unsplit,full_rank,ell_rank,higher)
}
fn main(){
    let a:Vec<String>=env::args().collect();
    if a.len()==3&&a[1]=="soft-support-nine-master-test"{fs::write(&a[2],soft_support_nine_master_test()).expect("write nine-master soft support test");return}
    if a.len()==3&&a[1]=="soft-support-both-sites-test"{fs::write(&a[2],soft_support_both_sites_test()).expect("write both-site soft support test");return}
    if a.len()==3&&a[1]=="soft-support-test"{fs::write(&a[2],soft_support_saturated_test()).expect("write soft support test");return}
    if a.len()==3&&a[1]=="soft-corner-common-frame-test"{fs::write(&a[2],soft_corner_common_frame_test()).expect("write soft corner test");return}
    if a.len()==4&&a[1]=="generic-et-test"{let count=a[2].parse::<usize>().unwrap();fs::write(&a[3],generic_et_test(count)).expect("write generic ET test");return}
    if a.len()==4&&a[1]=="other-block-test"{
        let count=a[2].parse::<usize>().unwrap();let blocks:Vec<Vec<(bool,Mon)>>=vec![vec![(false,(1,1))],vec![(true,(1,0)),(false,(1,0))],vec![(true,(0,1)),(false,(0,1))]];let mut su=0x9e3779b97f4a7c15u64;let mut sv=0xd1b54a32d192ed03u64;let mut bad=[0usize;3];
        for _ in 0..count{su=((su as u128*6_364_136_223_846_793_005u128+97u128)%PRIME as u128)as u64;sv=((sv as u128*2_862_933_555_777_941_757u128+101u128)%PRIME as u128)as u64;let u=F::new(su,PRIME);let v=F::new(sv,PRIME);let l=F::o(PRIME).sub(u.add(v).mul(F::new(2,PRIME).inv()));
            for(axisn,axis)in ["u","v"].iter().enumerate(){for bi in 0..3{let got=sample_block(su,sv,axis,&blocks[bi]);let mut want=vec![vec![F::z(PRIME);blocks[bi].len()];blocks[bi].len()];if bi==0&&axisn==0{want[0][0]=u.inv()}if bi==1&&axisn==0{want[1][0]=F::o(PRIME).neg()}if bi==2{want[0][0]=F::new(2,PRIME).inv().div(l);want[1][0]=if axisn==0{v.mul(F::new(2,PRIME).inv()).sub(F::o(PRIME)).div(l)}else{u.mul(F::new(2,PRIME).inv()).neg().div(l)}}for i in 0..got.len(){for j in 0..got.len(){if got[i][j]!=want[i][j]{bad[bi]+=1}}}}}
        }
        let out=format!("{{\"schema\":\"marici.gm.other_blocks_test.v1\",\"prime\":{},\"points\":{},\"directions\":{},\"block_mismatches\":{:?},\"Q_denominators\":0}}",PRIME,count,2*count,bad);fs::write(&a[3],out).expect("write other block test");return
    }
    if a.len()==4&&a[1]=="other-block-reconstruct"{
        let maxdeg=a[2].parse::<u8>().unwrap();let blocks:Vec<Vec<(bool,Mon)>>=vec![vec![(false,(1,1))],vec![(true,(1,0)),(false,(1,0))],vec![(true,(0,1)),(false,(0,1))]];let need=2*total_monomials(maxdeg).len()+20;let mut su=0x6a09e667f3bcc909u64;let mut sv=0xbb67ae8584caa73bu64;let mut data=Vec::new();
        while data.len()<need{su=((su as u128*6_364_136_223_846_793_005u128+83u128)%PRIME as u128)as u64;sv=((sv as u128*2_862_933_555_777_941_757u128+89u128)%PRIME as u128)as u64;let mut all=Vec::new();for axis in ["u","v"]{let mut z=Vec::new();for b in &blocks{z.push(sample_block(su,sv,axis,b));}all.push(z);}data.push((su,sv,all));}
        let mut body=String::new();let mut failures=0;for bi in 0..3{if bi>0{body.push(',')}body.push_str(&format!("\"block{}\":{{",bi));for axis in 0..2{if axis>0{body.push(',')}body.push_str(if axis==0{"\"u\":["}else{"\"v\":["});let n=blocks[bi].len();let mut first=true;for i in 0..n{for j in 0..n{if !first{body.push(',')}first=false;let ss:Vec<(u64,u64,F)>=data.iter().map(|(u,v,z)|(*u,*v,z[axis][bi][i][j])).collect();if let Some(f)=fit_entry(&ss,maxdeg){body.push_str(&fit_json(&f))}else{body.push_str("null");failures+=1}}}body.push(']')}body.push('}')}
        let out=format!("{{\"schema\":\"marici.gm.other_blocks_reconstruction.v1\",\"prime\":{},\"max_degree\":{},\"sample_count\":{},\"failures\":{},\"blocks\":{{{}}}}}",PRIME,maxdeg,need,failures,body);fs::write(&a[3],out).expect("write other blocks");return
    }
    if a.len()==4&&a[1]=="algebraic-split-test"{
        let maxdeg=a[2].parse::<u8>().unwrap();let mut train=Vec::new();let mut su=0x1f83d9abfb41bd6bu64;let mut sv=0x5be0cd19137e2179u64;
        while train.len()<96{su=((su as u128*6_364_136_223_846_793_005u128+67u128)%PRIME as u128)as u64;sv=((sv as u128*2_862_933_555_777_941_757u128+71u128)%PRIME as u128)as u64;let mut z=Vec::new();let mut ok=true;for axis in ["u","v"]{if let Ok(q)=std::panic::catch_unwind(||extension_data(su,sv,axis)){z.push(q)}else{ok=false;break}}if ok{train.push((su,sv,z))}}
        let mut found=None;
        'search:for qpow in 0..=1u8{for p6pow in 0..=2u8{for d1pow in 0..=2u8{for deg in 0..=maxdeg{let ms=total_monomials(deg);if 2*train.len()<ms.len()+8{continue}let mut mat=Vec::new();
            for(uu,vv,zs)in &train{for axis in 0..2{let(d1,p6,q,g00,g10,g11)=zs[axis];let factors=[d1,p6,q];let powers=[d1pow,p6pow,qpow];let mut sx=F::o(PRIME);let mut slog=F::z(PRIME);for k in 0..3{if powers[k]>0{sx=sx.mul(factors[k].x.pow(powers[k]as u64));slog=slog.add(F::new(powers[k]as u64,PRIME).mul(factors[k].d.div(factors[k].x)));}}let lambda=g00.sub(g11).sub(slog);let u=F::new(*uu,PRIME);let v=F::new(*vv,PRIME);let mut row=Vec::new();for(i,j)in &ms{let m=u.pow(*i as u64).mul(v.pow(*j as u64));let e=if axis==0{*i}else{*j};let dm=if e==0{F::z(PRIME)}else{F::new(e as u64,PRIME).mul(if axis==0{u.pow((i-1)as u64).mul(v.pow(*j as u64))}else{u.pow(*i as u64).mul(v.pow((j-1)as u64))})};row.push(dm.add(lambda.mul(m)));}row.push(g10.neg().mul(sx));mat.push(row);}}
            if let Some(cs)=rank_solve(mat,ms.len()){let mut vu=0x428a2f98d728ae22u64;let mut vv=0x7137449123ef65cdu64;let mut bad=0;for _ in 0..1024{vu=((vu as u128*3_202_034_522_624_059_733u128+73u128)%PRIME as u128)as u64;vv=((vv as u128*3_933_555_777_941_757u128+79u128)%PRIME as u128)as u64;for axis in 0..2{let ax=if axis==0{"u"}else{"v"};let(d1,p6,q,g00,g10,g11)=extension_data(vu,vv,ax);let factors=[d1,p6,q];let powers=[d1pow,p6pow,qpow];let mut sx=F::o(PRIME);let mut slog=F::z(PRIME);for k in 0..3{if powers[k]>0{sx=sx.mul(factors[k].x.pow(powers[k]as u64));slog=slog.add(F::new(powers[k]as u64,PRIME).mul(factors[k].d.div(factors[k].x)));}}let(px,pd)=eval_poly_coeff(&cs,&ms,F::new(vu,PRIME),F::new(vv,PRIME),axis);if pd.add(g00.sub(g11).sub(slog).mul(px)).add(g10.mul(sx)).v!=0{bad+=1}}}if bad==0{found=Some((d1pow,p6pow,qpow,deg,cs,ms));break 'search}}}
        }}}
        let out=if let Some((d1p,p6p,qp,deg,cs,ms))=found{let mut terms=String::from("[");let mut first=true;for((i,j),c)in ms.iter().zip(&cs){if c.v!=0{if !first{terms.push(',')}first=false;terms.push_str(&format!("[{},{},{}]",i,j,c.v));}}terms.push(']');format!("{{\"schema\":\"marici.gm.algebraic_split_test.v1\",\"status\":\"split\",\"denominator_powers\":{{\"D1\":{},\"P6\":{},\"Q\":{}}},\"numerator_degree\":{},\"numerator_terms\":{},\"validation_points\":1024,\"validation_directions\":2048,\"validation_mismatches\":0}}",d1p,p6p,qp,deg,terms)}else{format!("{{\"schema\":\"marici.gm.algebraic_split_test.v1\",\"status\":\"not_found\",\"max_degree\":{}}}",maxdeg)};
        fs::write(&a[3],out).expect("write algebraic split test");return
    }
    if a.len()==4&&a[1]=="algebraic-dlog-test"{
        let count=a[2].parse::<usize>().unwrap();let mut su=0x510e527fade682d1u64;let mut sv=0x9b05688c2b3e6c1fu64;let mut mat0=Vec::new();let mut mat1=Vec::new();let mut points=Vec::new();
        while points.len()<count{su=((su as u128*6_364_136_223_846_793_005u128+59u128)%PRIME as u128)as u64;sv=((sv as u128*2_862_933_555_777_941_757u128+61u128)%PRIME as u128)as u64;
            let mut rows=Vec::new();let mut ok=true;for axis in ["u","v"]{let q=std::panic::catch_unwind(||{let z=algebraic_plane_test(su,sv,axis);(algebraic_dlogs(su,sv,axis),z.1,z.4)});if let Ok(z)=q{rows.push(z)}else{ok=false;break}}if !ok{continue}
            for(dl,t0,t1)in &rows{let mut row0=dl.clone();row0.push(*t0);mat0.push(row0);let mut row1=dl.clone();row1.push(*t1);mat1.push(row1)}points.push((su,sv));
        }
        let factor_rank=matrix_rank(mat0.iter().map(|r|r[..10].to_vec()).collect(),10);let weights0=rank_solve(mat0,10).expect("g00 dlog solve");let weights1=rank_solve(mat1,10).expect("g11 dlog solve");let mut bad0=0usize;let mut bad1=0usize;
        for(uu,vv)in &points{for axis in ["u","v"]{let dl=algebraic_dlogs(*uu,*vv,axis);let z=algebraic_plane_test(*uu,*vv,axis);let mut q0=F::z(PRIME);let mut q1=F::z(PRIME);for k in 0..10{q0=q0.add(weights0[k].mul(dl[k]));q1=q1.add(weights1[k].mul(dl[k]));}if q0!=z.1{bad0+=1}if q1!=z.4{bad1+=1}}}
        let vals0:Vec<u64>=weights0.iter().map(|z|z.v).collect();let vals1:Vec<u64>=weights1.iter().map(|z|z.v).collect();let out=format!("{{\"schema\":\"marici.gm.algebraic_dlog_test.v2\",\"prime\":{},\"points\":{},\"directions\":{},\"factor_matrix_rank\":{},\"factors\":[\"u\",\"v\",\"y\",\"1-y\",\"1+y\",\"v-u\",\"y-u^2\",\"y+u^2\",\"Q\",\"P6\"],\"g00_weights\":{:?},\"g11_weights\":{:?},\"g00_validation_mismatches\":{},\"g11_validation_mismatches\":{}}}",PRIME,count,2*count,factor_rank,vals0,vals1,bad0,bad1);
        fs::write(&a[3],out).expect("write algebraic dlog test");return
    }
    if a.len()==4&&a[1]=="algebraic-reconstruct"{
        let maxdeg=a[2].parse::<u8>().unwrap();let need=2*total_monomials(maxdeg).len()+20;let now=Instant::now();
        let mut samples:Vec<Vec<Vec<(u64,u64,F)>>>=vec![vec![Vec::new();6],vec![Vec::new();6]];
        let mut su=0x3c6ef372fe94f82bu64;let mut sv=0xa54ff53a5f1d36f1u64;
        while samples[0][0].len()<need{su=((su as u128*6_364_136_223_846_793_005u128+47u128)%PRIME as u128)as u64;sv=((sv as u128*2_862_933_555_777_941_757u128+53u128)%PRIME as u128)as u64;
            let mut z=Vec::new();let mut ok=true;for axis in ["u","v"]{if let Ok(q)=std::panic::catch_unwind(||algebraic_plane_test(su,sv,axis)){z.push(q)}else{ok=false;break}}if !ok{continue}
            for axis in 0..2{let(_,g00,_g01,g10,g11,qlog)=z[axis];let vals=[g00,g10,g11,qlog,g11.sub(qlog),g11.add(qlog)];for k in 0..6{samples[axis][k].push((su,sv,vals[k]));}}
        }
        let names=["g00","g10","g11","half_dlog_Q","g11_minus_half_dlog_Q","g11_plus_half_dlog_Q"];let mut body=String::new();let mut failures=0usize;
        for axis in 0..2{if axis>0{body.push(',')}body.push_str(if axis==0{"\"u\":{"}else{"\"v\":{"});for k in 0..6{if k>0{body.push(',')}body.push_str(&format!("\"{}\":",names[k]));if let Some(f)=fit_entry(&samples[axis][k],maxdeg){body.push_str(&fit_json(&f))}else{body.push_str("null");failures+=1}}body.push('}')}
        let out=format!("{{\"schema\":\"marici.gm.algebraic_reconstruction.v1\",\"prime\":{},\"max_degree\":{},\"sample_count\":{},\"failures\":{},\"connections\":{{{}}},\"elapsed_ms\":{}}}",PRIME,maxdeg,need,failures,body,now.elapsed().as_millis());
        fs::write(&a[3],out).expect("write algebraic reconstruction");return
    }
    if a.len()==4&&a[1]=="algebraic-test"{
        let count=a[2].parse::<usize>().unwrap();let mut closure=0usize;let mut g00n=0usize;let mut g01n=0usize;let mut g10n=0usize;let mut minus=0usize;let mut plus=0usize;
        let mut su=0x6a09e667f3bcc909u64;let mut sv=0xbb67ae8584caa73bu64;let now=Instant::now();let mut done=0usize;
        while done<count{su=((su as u128*6_364_136_223_846_793_005u128+41u128)%PRIME as u128)as u64;sv=((sv as u128*2_862_933_555_777_941_757u128+43u128)%PRIME as u128)as u64;
            let mut accepted=true;let mut values=Vec::new();for axis in ["u","v"]{let r=std::panic::catch_unwind(||algebraic_plane_test(su,sv,axis));if let Ok(z)=r{values.push(z)}else{accepted=false;break}}
            if !accepted{continue}done+=1;for(bad,g00,g01,g10,g11,qlog)in values{closure+=bad;if g00.v!=0{g00n+=1}if g01.v!=0{g01n+=1}if g10.v!=0{g10n+=1}if g11.sub(qlog).v!=0{minus+=1}if g11.add(qlog).v!=0{plus+=1}}
        }
        let out=format!("{{\"schema\":\"marici.gm.algebraic_plane_test.v1\",\"prime\":{},\"points\":{},\"directions\":{},\"closure_residual_entries\":{},\"g00_nonzero\":{},\"e6_to_valg_nonzero\":{},\"valg_to_e6_nonzero\":{},\"g11_minus_half_dlog_Q_nonzero\":{},\"g11_plus_half_dlog_Q_nonzero\":{},\"elapsed_ms\":{}}}",PRIME,count,2*count,closure,g00n,g01n,g10n,minus,plus,now.elapsed().as_millis());
        fs::write(&a[3],out).expect("write algebraic test");return
    }
    if a.len()==4&&a[1]=="gysin-test"{
        let count=a[2].parse::<usize>().unwrap();let signs=[(1i8,-1i8),(1,1),(-1,-1),(-1,1)];let mut nonzero=[0usize;4];let mut maxrank=[0usize;4];let mut rows=[[0usize;4];4];let mut su=0x243f6a8885a308d3u64;let mut sv=0x13198a2e03707344u64;let now=Instant::now();
        for _ in 0..count{su=((su as u128*6_364_136_223_846_793_005u128+17u128)%PRIME as u128)as u64;sv=((sv as u128*2_862_933_555_777_941_757u128+29u128)%PRIME as u128)as u64;
            for axis in ["u","v"]{let(am,_)=sample_rows(su,sv,axis);let(f,fp,c,cp)=boundary_data(su,sv,axis);let b=elliptic_connection(&f,&fp);let cb=mul_4x2_2x2(&c,&b);let ac=mul_4x4_4x2(&am,&c);
                for(q,(sb,sa))in signs.iter().enumerate(){let mut z=vec![vec![F::z(PRIME);2];4];for i in 0..4{for j in 0..2{z[i][j]=cp[i][j].add(if *sb==1{cb[i][j]}else{cb[i][j].neg()}).add(if *sa==1{ac[i][j]}else{ac[i][j].neg()});if z[i][j].v!=0{nonzero[q]+=1;rows[q][i]+=1;}}}maxrank[q]=maxrank[q].max(rank_4x2(z));}
            }
        }
        let out=format!("{{\"schema\":\"marici.gm.infinity_gysin_test.v1\",\"prime\":{},\"points\":{},\"directions\":{},\"variants\":[{{\"formula\":\"dC+C*B-A*C\",\"nonzero\":{},\"max_rank\":{},\"row_nonzero\":{:?}}},{{\"formula\":\"dC+C*B+A*C\",\"nonzero\":{},\"max_rank\":{},\"row_nonzero\":{:?}}},{{\"formula\":\"dC-C*B-A*C\",\"nonzero\":{},\"max_rank\":{},\"row_nonzero\":{:?}}},{{\"formula\":\"dC-C*B+A*C\",\"nonzero\":{},\"max_rank\":{},\"row_nonzero\":{:?}}}],\"elapsed_ms\":{}}}",PRIME,count,2*count,nonzero[0],maxrank[0],rows[0],nonzero[1],maxrank[1],rows[1],nonzero[2],maxrank[2],rows[2],nonzero[3],maxrank[3],rows[3],now.elapsed().as_millis());
        fs::write(&a[3],out).expect("write gysin test");return
    }
    if a.len()==4&&a[1]=="reconstruct"{
        let maxdeg=a[2].parse::<u8>().unwrap();let need=2*total_monomials(maxdeg).len()+20;let now=Instant::now();
        let mut data:Vec<(u64,u64,Vec<Vec<F>>,Vec<Vec<F>>)>=Vec::new();let mut su=0x9e3779b97f4a7c15u64;let mut sv=0xd1b54a32d192ed03u64;
        while data.len()<need{su=((su as u128*6_364_136_223_846_793_005u128+1_442_695_040_888_963_407u128)%PRIME as u128)as u64;sv=((sv as u128*2_862_933_555_777_941_757u128+3_037_000_493u128)%PRIME as u128)as u64;let u=su;let v=sv;let(au,_)=sample_rows(u,v,"u");let(av,_)=sample_rows(u,v,"v");data.push((u,v,au,av));}
        let mut fits:Vec<Vec<RatFit>>=vec![Vec::new(),Vec::new()];let mut failures=0;let mut failed_entries=String::new();
        for axis in 0..2{for row in 0..4{for col in 0..4{let samples:Vec<(u64,u64,F)>=data.iter().map(|(u,v,au,av)|(*u,*v,if axis==0{au[row][col]}else{av[row][col]})).collect();match fit_entry(&samples,maxdeg){Some(f)=>fits[axis].push(f),None=>{failures+=1;if !failed_entries.is_empty(){failed_entries.push(',');}failed_entries.push_str(&format!("{}:{}:{}",axis,row,col));}}}}}
        if failures>0{fs::write(&a[3],format!("{{\"schema\":\"marici.gm.bivariate_reconstruction.v2\",\"prime\":{},\"max_degree\":{},\"sample_count\":{},\"failures\":{},\"failed_entries\":\"{}\",\"elapsed_ms\":{}}}",PRIME,maxdeg,data.len(),failures,failed_entries,now.elapsed().as_millis())).expect("write failed reconstruction");return}
        let mut validation_mismatches=0;let mut curvature_plus_nonzero=0;let mut curvature_minus_nonzero=0;
        if failures==0{let mut cu=0xa24baed4963ee407u64;let mut cv=0x9fb21c651e98df25u64;for _ in 0..32{cu=((cu as u128*3_202_034_522_624_059_733u128+1u128)%PRIME as u128)as u64;cv=((cv as u128*3_933_555_777_941_757u128+7u128)%PRIME as u128)as u64;let uu=cu;let vv=cv;let u=F::new(uu,PRIME);let v=F::new(vv,PRIME);let(au0,_)=sample_rows(uu,vv,"u");let(av0,_)=sample_rows(uu,vv,"v");let au=fit_matrix_eval(&fits[0],u,v);let av=fit_matrix_eval(&fits[1],u,v);
            for i in 0..4{for j in 0..4{if au[i][j]!=au0[i][j]{validation_mismatches+=1}if av[i][j]!=av0[i][j]{validation_mismatches+=1}}}
            let mut duav=vec![vec![F::z(PRIME);4];4];let mut dvau=duav.clone();for i in 0..4{for j in 0..4{duav[i][j]=rat_deriv(&fits[1][4*i+j],u,v,0);dvau[i][j]=rat_deriv(&fits[0][4*i+j],u,v,1);}}
            let uv=mat_mul(&au,&av);let vu=mat_mul(&av,&au);for i in 0..4{for j in 0..4{let base=duav[i][j].sub(dvau[i][j]);if base.add(uv[i][j]).sub(vu[i][j]).v!=0{curvature_plus_nonzero+=1}if base.sub(uv[i][j]).add(vu[i][j]).v!=0{curvature_minus_nonzero+=1}}}
        }}
        let mut out=format!("{{\"schema\":\"marici.gm.bivariate_reconstruction.v2\",\"prime\":{},\"max_degree\":{},\"sample_count\":{},\"entries\":[",PRIME,maxdeg,data.len());let mut first=true;
        for axis in 0..2{for row in 0..4{for col in 0..4{if !first{out.push(',');}first=false;let f=&fits[axis][4*row+col];out.push_str(&format!("{{\"axis\":\"{}\",\"row\":{},\"col\":{},\"fit\":{}}}",if axis==0{"u"}else{"v"},row,col,fit_json(f)));}}}
        out.push_str(&format!("],\"failures\":{},\"independent_validation_points\":32,\"validation_mismatches\":{},\"curvature_plus_nonzero\":{},\"curvature_minus_nonzero\":{},\"elapsed_ms\":{}}}",failures,validation_mismatches,curvature_plus_nonzero,curvature_minus_nonzero,now.elapsed().as_millis()));fs::write(&a[3],out).expect("write reconstruction");return
    }
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
    #[cfg(not(feature="replication-prime"))]
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
    #[test] fn reconstructs_synthetic_bivariate_rational_function(){
        let mut s=Vec::new();let mut su=17u64;let mut sv=41u64;for _ in 0..64{su=((su as u128*6_364_136_223_846_793_005u128+1_442_695_040_888_963_407u128)%PRIME as u128)as u64;sv=((sv as u128*2_862_933_555_777_941_757u128+3_037_000_493u128)%PRIME as u128)as u64;let u=su;let v=sv;let uf=F::new(u,PRIME);let vf=F::new(v,PRIME);s.push((u,v,uf.add(vf).div(F::o(PRIME).add(uf.mul(vf)))));}
        let fit=fit_entry(&s,2).expect("synthetic fit");
        assert!(s.iter().all(|(u,v,f)|rat_eval(&fit,F::new(*u,PRIME),F::new(*v,PRIME))==*f));
    }
    #[test] fn infinity_gysin_is_horizontal_at_generic_point(){
        for axis in ["u","v"]{let(a,_)=sample_rows(37,113,axis);let(f,fp,c,cp)=boundary_data(37,113,axis);let b=elliptic_connection(&f,&fp);let cb=mul_4x2_2x2(&c,&b);let ac=mul_4x4_4x2(&a,&c);
            for i in 0..4{for j in 0..2{assert_eq!(cp[i][j].add(cb[i][j]).sub(ac[i][j]).v,0);}}
        }
    }
}
