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
    [u,v,y,one.sub(y),one.add(y),v.sub(u),y.sub(u2),y.add(u2),q].iter().map(|z|z.d.div(z.x)).collect()
}
fn main(){
    let a:Vec<String>=env::args().collect();
    if a.len()==4&&a[1]=="algebraic-dlog-test"{
        let count=a[2].parse::<usize>().unwrap();let mut su=0x510e527fade682d1u64;let mut sv=0x9b05688c2b3e6c1fu64;let mut mat=Vec::new();let mut points=Vec::new();
        while points.len()<count{su=((su as u128*6_364_136_223_846_793_005u128+59u128)%PRIME as u128)as u64;sv=((sv as u128*2_862_933_555_777_941_757u128+61u128)%PRIME as u128)as u64;
            let mut rows=Vec::new();let mut ok=true;for axis in ["u","v"]{let q=std::panic::catch_unwind(||{let z=algebraic_plane_test(su,sv,axis);(algebraic_dlogs(su,sv,axis),z.4)});if let Ok(z)=q{rows.push(z)}else{ok=false;break}}if !ok{continue}
            for(dl,t)in &rows{let mut row=dl.clone();row.push(*t);mat.push(row)}points.push((su,sv));
        }
        let factor_rank=matrix_rank(mat.iter().map(|r|r[..9].to_vec()).collect(),9);let weights=rank_solve(mat,9).expect("dlog solve");let mut bad=0usize;
        for(uu,vv)in &points{for axis in ["u","v"]{let dl=algebraic_dlogs(*uu,*vv,axis);let target=algebraic_plane_test(*uu,*vv,axis).4;let mut z=F::z(PRIME);for k in 0..9{z=z.add(weights[k].mul(dl[k]));}if z!=target{bad+=1}}}
        let vals:Vec<u64>=weights.iter().map(|z|z.v).collect();let out=format!("{{\"schema\":\"marici.gm.algebraic_dlog_test.v1\",\"prime\":{},\"points\":{},\"directions\":{},\"factor_matrix_rank\":{},\"factors\":[\"u\",\"v\",\"y\",\"1-y\",\"1+y\",\"v-u\",\"y-u^2\",\"y+u^2\",\"Q\"],\"weights\":{:?},\"validation_mismatches\":{}}}",PRIME,count,2*count,factor_rank,vals,bad);
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
