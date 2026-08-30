use std::collections::BTreeMap;
#[derive(Clone,Copy,Debug,Default)]struct C{r:f64,i:f64}
impl C{fn n(r:f64,i:f64)->Self{Self{r,i}}fn abs(self)->f64{(self.r*self.r+self.i*self.i).sqrt()}}
impl std::ops::Add for C{type Output=Self;fn add(self,x:Self)->Self{Self::n(self.r+x.r,self.i+x.i)}}
impl std::ops::Mul for C{type Output=Self;fn mul(self,x:Self)->Self{Self::n(self.r*x.r-self.i*x.i,self.r*x.i+self.i*x.r)}}
impl std::ops::Mul<f64> for C{type Output=Self;fn mul(self,x:f64)->Self{Self::n(self.r*x,self.i*x)}}
impl std::ops::Div for C{type Output=Self;fn div(self,x:Self)->Self{let d=x.r*x.r+x.i*x.i;Self::n((self.r*x.r+self.i*x.i)/d,(self.i*x.r-self.r*x.i)/d)}}
#[derive(Clone,Copy)]struct T{ft:[i32;3],f0:[i32;3],nt:i32,n0:i32,c:C}
fn af(a:[i32;3],b:[i32;3])->[i32;3]{[a[0]+b[0],a[1]+b[1],a[2]+b[2]]}
fn mul(a:&[T],b:&[T])->Vec<T>{let mut o=Vec::new();for x in a{for y in b{o.push(T{ft:af(x.ft,y.ft),f0:af(x.f0,y.f0),nt:x.nt+y.nt,n0:x.n0+y.n0,c:x.c*y.c})}}o}
fn ph(x:f64)->C{C::n(x.cos(),x.sin())}
fn be(a:i32,p:f64,eta:f64)->Vec<T>{let base=if a==1{C::n(1.,p*eta)*ph(-p*eta)}else{C::n(1.,-p*eta)*ph(p*eta)};let lin=C::n(0.,-(a as f64)*p);vec![T{ft:[a,0,0],f0:[0;3],nt:0,n0:0,c:base*(1./p.powi(3))},T{ft:[a,0,0],f0:[0;3],nt:1,n0:0,c:base*lin*(1./p.powi(3))}]}
fn se(b:i32,p:f64,eta:f64)->Vec<T>{let base=if b==1{C::n(1.,p*eta)*ph(-p*eta)}else{C::n(1.,-p*eta)*ph(p*eta)};let lin=C::n(0.,-(b as f64)*p);vec![T{ft:[0;3],f0:[b,0,0],nt:0,n0:0,c:base*(1./p.powi(3))},T{ft:[0;3],f0:[b,0,0],nt:0,n0:1,c:base*lin*(1./p.powi(3))}]}
fn internal(b:i32,index:usize,m:f64)->Vec<T>{let mut ft=[0;3];let mut f0=[0;3];ft[index]=-b;f0[index]=b;let lt=C::n(0.,b as f64*m);let l0=C::n(0.,-(b as f64)*m);let z=C::n(1./m.powi(3),0.);vec![T{ft,f0,nt:0,n0:0,c:z},T{ft,f0,nt:1,n0:0,c:z*lt},T{ft,f0,nt:0,n0:1,c:z*l0},T{ft,f0,nt:1,n0:1,c:z*lt*l0}]}
fn bw(b:i32,s:f64)->Vec<T>{if b==1{vec![T{ft:[0;3],f0:[0;3],nt:0,n0:-3,c:C::n(-1./(s*s),0.)},T{ft:[0;3],f0:[0;3],nt:0,n0:-2,c:C::n(0.,1./s)}]}else{vec![T{ft:[0;3],f0:[0;3],nt:0,n0:-3,c:C::n(1./(s*s),0.)},T{ft:[0;3],f0:[0;3],nt:0,n0:-2,c:C::n(0.,1./s)}]}}
fn omega(f:[i32;3],p:f64,q:f64,k:f64)->f64{f[0]as f64*p+f[1]as f64*q+f[2]as f64*k}
fn fall(n:i32,r:usize)->f64{(0..r).map(|j|f64::from(n-j as i32)).product()}
fn pc(n:i32,r:usize,w:f64)->C{let s=if r%2==0{1.}else{-1.};C::n(s*fall(n,r),0.)/(0..=r).fold(C::n(1.,0.),|z,_|z*C::n(0.,w))}
fn add<K:Ord>(m:&mut BTreeMap<K,C>,k:K,v:C){let z=m.entry(k).or_default();*z=*z+v}
fn main(){let p=std::env::var("MARICI_P").ok().and_then(|x|x.parse().ok()).unwrap_or(1.1);let q=std::env::var("MARICI_Q").ok().and_then(|x|x.parse().ok()).unwrap_or(0.8);let k=std::env::var("MARICI_K").ok().and_then(|x|x.parse().ok()).unwrap_or(0.9);let eta=std::env::var("MARICI_ETA").ok().and_then(|x|x.parse().ok()).unwrap_or(-0.15);let s=p+q+k;let mut raw=Vec::new();
 for a in[1,-1]{for b in[1,-1]{let bulk=vec![T{ft:[0;3],f0:[0;3],nt:-2,n0:0,c:C::n(a as f64,0.)}];raw.extend(mul(&mul(&mul(&mul(&bulk,&bw(b,s)),&be(a,p,eta)),&se(b,p,eta)),&mul(&internal(b,1,q),&internal(b,2,k))))}}
 let mut lower:BTreeMap<([i32;3],i32),C>=BTreeMap::new();let mut upper:BTreeMap<([i32;3],i32,[i32;3],i32),C>=BTreeMap::new();let max_r=8usize;
 for t in raw{let w=omega(t.ft,p,q,k);assert!(w.abs()>1e-10);for r in 0..=max_r{let power=t.nt-r as i32+t.n0;if power<0{break}let a=pc(t.nt,r,w);add(&mut lower,(af(t.ft,t.f0),power),t.c*a*(-1.));}if t.n0>=0{add(&mut upper,(t.f0,t.n0,t.ft,t.nt),t.c);}}
 let spatial=(p*p+q*q+k*k).powi(2);for c in lower.values_mut(){*c=*c*spatial}for c in upper.values_mut(){*c=*c*spatial}lower.retain(|_,c|c.abs()>1e-10);upper.retain(|_,c|c.abs()>1e-10);
 for grade in[2,1,0]{let rows:Vec<_>=lower.iter().filter(|((_,n),_)|*n==grade).collect();println!("grade_{grade}_lower_term_count={}",rows.len());for((f,_),c)in rows{println!("grade_{grade}_lower_frequency_{f:?}=({:.15e},{:.15e})",c.r,c.i);println!("LOWER|BS|{grade}|{},{},{}|{:.17e}|{:.17e}",f[0],f[1],f[2],c.r,c.i)}}
 let mut us:BTreeMap<(i32,[i32;3]),usize>=BTreeMap::new();for((f0,power,_,_),_)in&upper{if*power<=1{*us.entry((*power,*f0)).or_default()+=1;}}
 for((power,f),count)in us{println!("observation_endpoint_grade_{power}_frequency_{f:?}_primitive_classes={count}");}
 for((fb,power,fo,n),c)in&upper{println!("OBS|BS|{},{},{}|{}|{},{},{}|{}|none|{:.17e}|{:.17e}",fb[0],fb[1],fb[2],power,fo[0],fo[1],fo[2],n,c.r,c.i);}
 assert!(lower.keys().filter(|(_,n)|*n==2).all(|(f,_)|f[1]==0&&f[2]==0&&matches!(f[0],-2|0|2)));
 println!("grade2_regression_support_passes=true");println!("lower_grades_derived_without_fitting=true");}
