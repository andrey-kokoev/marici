#[derive(Clone,Copy,Debug,Default)]struct C{r:f64,i:f64}
impl C{fn n(r:f64,i:f64)->Self{Self{r,i}}fn cj(self)->Self{Self::n(self.r,-self.i)}fn abs(self)->f64{(self.r*self.r+self.i*self.i).sqrt()}}
impl std::ops::Add for C{type Output=Self;fn add(self,x:Self)->Self{Self::n(self.r+x.r,self.i+x.i)}}
impl std::ops::Sub for C{type Output=Self;fn sub(self,x:Self)->Self{Self::n(self.r-x.r,self.i-x.i)}}
impl std::ops::Mul for C{type Output=Self;fn mul(self,x:Self)->Self{Self::n(self.r*x.r-self.i*x.i,self.r*x.i+self.i*x.r)}}
impl std::ops::Mul<f64> for C{type Output=Self;fn mul(self,x:f64)->Self{Self::n(self.r*x,self.i*x)}}
impl std::ops::Div<C> for C{type Output=Self;fn div(self,x:Self)->Self{let d=x.r*x.r+x.i*x.i;Self::n((self.r*x.r+self.i*x.i)/d,(self.i*x.r-self.r*x.i)/d)}}
#[derive(Clone,Copy)]struct T{ft:[i32;3],f0:[i32;3],nt:i32,n0:i32,c:C}
fn addf(a:[i32;3],b:[i32;3])->[i32;3]{[a[0]+b[0],a[1]+b[1],a[2]+b[2]]}
fn mul(a:&[T],b:&[T])->Vec<T>{let mut o=Vec::new();for x in a{for y in b{o.push(T{ft:addf(x.ft,y.ft),f0:addf(x.f0,y.f0),nt:x.nt+y.nt,n0:x.n0+y.n0,c:x.c*y.c})}}o}
fn ph(x:f64)->C{C::n(x.cos(),x.sin())}
fn bulk_external(a:i32,p:f64,eta:f64)->Vec<T>{let base=if a==1{C::n(1.,p*eta)*ph(-p*eta)}else{C::n(1.,-p*eta)*ph(p*eta)};let lin=if a==1{C::n(0.,-p)}else{C::n(0.,p)};vec![T{ft:[a,0,0],f0:[0,0,0],nt:0,n0:0,c:base*(1./p.powi(3))},T{ft:[a,0,0],f0:[0,0,0],nt:1,n0:0,c:base*lin*(1./p.powi(3))}]}
fn boundary_external(b:i32,p:f64,eta:f64)->Vec<T>{let base=if b==1{C::n(1.,p*eta)*ph(-p*eta)}else{C::n(1.,-p*eta)*ph(p*eta)};let lin=if b==1{C::n(0.,-p)}else{C::n(0.,p)};vec![T{ft:[0,0,0],f0:[b,0,0],nt:0,n0:0,c:base*(1./p.powi(3))},T{ft:[0,0,0],f0:[b,0,0],nt:0,n0:1,c:base*lin*(1./p.powi(3))}]}
fn internal(b:i32,index:usize,m:f64)->Vec<T>{let mut ft=[0;3];let mut f0=[0;3];ft[index]=-b;f0[index]=b;let lt=if b==1{C::n(0.,m)}else{C::n(0.,-m)};let l0=if b==1{C::n(0.,-m)}else{C::n(0.,m)};vec![T{ft,f0,nt:0,n0:0,c:C::n(1./m.powi(3),0.)},T{ft,f0,nt:1,n0:0,c:lt*(1./m.powi(3))},T{ft,f0,nt:0,n0:1,c:l0*(1./m.powi(3))},T{ft,f0,nt:1,n0:1,c:lt*l0*(1./m.powi(3))}]}
fn bw(b:i32,s:f64)->Vec<T>{if b==1{vec![T{ft:[0;3],f0:[0;3],nt:0,n0:-3,c:C::n(-1./(s*s),0.)},T{ft:[0;3],f0:[0;3],nt:0,n0:-2,c:C::n(0.,1./s)}]}else{vec![T{ft:[0;3],f0:[0;3],nt:0,n0:-3,c:C::n(1./(s*s),0.)},T{ft:[0;3],f0:[0;3],nt:0,n0:-2,c:C::n(0.,1./s)}]}}
fn main(){let p=std::env::var("MARICI_P").ok().and_then(|x|x.parse().ok()).unwrap_or(1.1);let q=std::env::var("MARICI_Q").ok().and_then(|x|x.parse().ok()).unwrap_or(0.8);let k=std::env::var("MARICI_K").ok().and_then(|x|x.parse().ok()).unwrap_or(0.9);let eta=std::env::var("MARICI_ETA").ok().and_then(|x|x.parse().ok()).unwrap_or(-0.15);let s=p+q+k;let mut out:Vec<([i32;3],C)>=Vec::new();
 for a in[1,-1]{for b in[1,-1]{let bulk=vec![T{ft:[0;3],f0:[0;3],nt:-2,n0:0,c:C::n(a as f64,0.)}];let x=mul(&mul(&mul(&mul(&bulk,&bw(b,s)),&bulk_external(a,p,eta)),&boundary_external(b,p,eta)),&mul(&internal(b,1,q),&internal(b,2,k)));for t in x{if t.nt+t.n0==2{let omega=t.ft[0]as f64*p+t.ft[1]as f64*q+t.ft[2]as f64*k;assert!(omega.abs()>1e-10);let c=t.c/C::n(0.,omega)*(-1.);let f=addf(t.ft,t.f0);if let Some((_,z))=out.iter_mut().find(|(g,_)|*g==f){*z=*z+c}else{out.push((f,c))}}}}}
 // Relative to a bulk Hamiltonian insertion, the boundary vertex enters
 // through +i S0 in fin0.  After the two mixed placements are combined,
 // this reverses the naive common-Hamiltonian sign.
 for(_,c)in&mut out{*c=*c*(p*p+q*q+k*k).powi(2)}out.sort_by_key(|x|x.0);
 assert!(out.iter().all(|(f,_)|f[1]==0&&f[2]==0&&matches!(f[0],-2|0|2)));let plus=out.iter().find(|(f,_)|f[0]==2).unwrap().1;let minus=out.iter().find(|(f,_)|f[0]==-2).unwrap().1;let zero=out.iter().find(|(f,_)|f[0]==0).unwrap().1;assert!((minus-plus.cj()).abs()<1e-11&&zero.i.abs()<1e-11);
 let shape=ph(-2.*p*eta)*C::n(1.-p*p*eta*eta,2.*p*eta)*0.5;let amplitude=(plus/shape)*p;let j2=(p*p+q*q+k*k).powi(2)/(p.powi(3)*q*k*s*(q+k-p));assert!((amplitude-C::n(-2.*j2,0.)).abs()<1e-10);
 for(f,c)in&out{println!("grade2_frequency_{}p=({:.15e},{:.15e})",f[0],c.r,c.i)}println!("internal_frequency_support_cancelled=true");println!("grade2_reality=true");println!("direct_oscillatory_basis=-2J2");}
