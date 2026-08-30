#[derive(Clone,Copy,Debug,Default)]struct C{r:f64,i:f64}
impl C{fn n(r:f64,i:f64)->Self{Self{r,i}}fn cj(self)->Self{Self::n(self.r,-self.i)}fn abs(self)->f64{(self.r*self.r+self.i*self.i).sqrt()}}
impl std::ops::Add for C{type Output=Self;fn add(self,x:Self)->Self{Self::n(self.r+x.r,self.i+x.i)}}
impl std::ops::Sub for C{type Output=Self;fn sub(self,x:Self)->Self{Self::n(self.r-x.r,self.i-x.i)}}
impl std::ops::Mul for C{type Output=Self;fn mul(self,x:Self)->Self{Self::n(self.r*x.r-self.i*x.i,self.r*x.i+self.i*x.r)}}
impl std::ops::Mul<f64> for C{type Output=Self;fn mul(self,x:f64)->Self{Self::n(self.r*x,self.i*x)}}
impl std::ops::Div<C> for C{type Output=Self;fn div(self,x:Self)->Self{let d=x.r*x.r+x.i*x.i;Self::n((self.r*x.r+self.i*x.i)/d,(self.i*x.r-self.r*x.i)/d)}}

#[derive(Clone,Copy,Debug)]struct T{f:i32,n:i32,c:C}
fn add(out:&mut Vec<T>,x:T){if let Some(t)=out.iter_mut().find(|t|t.f==x.f&&t.n==x.n){t.c=t.c+x.c}else{out.push(x)}}
fn mul(a:&[T],b:&[T])->Vec<T>{let mut o=Vec::new();for x in a{for y in b{add(&mut o,T{f:x.f+y.f,n:x.n+y.n,c:x.c*y.c})}}o}
fn external(branch:i32,p:f64,eta:f64)->Vec<T>{
 let base=if branch==1{C::n(1.,p*eta)*C::n((-p*eta).cos(),(-p*eta).sin())}else{C::n(1.,-p*eta)*C::n((p*eta).cos(),(p*eta).sin())};
 let linear=if branch==1{C::n(0.,-p)}else{C::n(0.,p)};
 vec![T{f:branch,n:0,c:base*(1./p.powi(3))},T{f:branch,n:1,c:base*linear*(1./p.powi(3))}]
}
fn boundary_weight(branch:i32,sum:f64)->Vec<T>{
 if branch==1{vec![T{f:0,n:-3,c:C::n(-1./(sum*sum),0.)},T{f:0,n:-2,c:C::n(0.,1./sum)}]}
 else{vec![T{f:0,n:-3,c:C::n(1./(sum*sum),0.)},T{f:0,n:-2,c:C::n(0.,1./sum)}]}
}
fn equal_internal(k:f64)->Vec<T>{vec![T{f:0,n:0,c:C::n(1./k.powi(3),0.)},T{f:0,n:2,c:C::n(1./k,0.)}]}
fn main(){
 let p=std::env::var("MARICI_P").ok().and_then(|x|x.parse().ok()).unwrap_or(1.1);
 let q=std::env::var("MARICI_Q").ok().and_then(|x|x.parse().ok()).unwrap_or(0.8);
 let k=std::env::var("MARICI_K").ok().and_then(|x|x.parse().ok()).unwrap_or(0.9);
 let eta=std::env::var("MARICI_ETA").ok().and_then(|x|x.parse().ok()).unwrap_or(-0.15);
 let sum=p+q+k;let internal=mul(&equal_internal(q),&equal_internal(k));let mut total=Vec::new();
 for a in[1,-1]{for b in[1,-1]{let x=mul(&mul(&boundary_weight(a,sum),&boundary_weight(b,sum)),&mul(&external(a,p,eta),&external(b,p,eta)));for t in mul(&x,&internal){add(&mut total,t)}}}
 // The two spatial vertices supply (p^2+q^2+k^2)^2. The quadratic
 // expansion of fin1 supplies the boundary-boundary factor -1/2.
 let source_weight=-0.5*(p*p+q*q+k*k).powi(2);
 for t in &mut total{t.c=t.c*source_weight;}
 total.sort_by_key(|t|(-t.n,t.f));
 for grade in[2,1,0]{let rows:Vec<_>=total.iter().filter(|t|t.n==grade&&t.c.abs()>1e-11).collect();println!("grade{grade}_term_count={}",rows.len());for t in rows{println!("grade{grade}_frequency_{}p=({:.15e},{:.15e})",t.f,t.c.r,t.c.i);println!("LOWER|SS|{grade}|{},0,0|{:.17e}|{:.17e}",t.f,t.c.r,t.c.i)}}
 let zero=total.iter().find(|t|t.n==2&&t.f==0).map(|t|t.c).unwrap_or_default();assert!(zero.i.abs()<1e-12);
 let plus=total.iter().find(|t|t.n==2&&t.f==2).unwrap().c;let minus=total.iter().find(|t|t.n==2&&t.f== -2).unwrap().c;assert!((minus-plus.cj()).abs()<1e-12);
 let shape=C::n((-2.*p*eta).cos(),(-2.*p*eta).sin())*C::n(1.-p*p*eta*eta,2.*p*eta)*0.5;
 let amplitude=(plus/shape)*p;let j0=(p*p+q*q+k*k).powi(2)/(p.powi(3)*q*k*sum*sum);assert!((amplitude-C::n(-j0,0.)).abs()<1e-11);
 assert!(total.iter().filter(|t|t.n==2).all(|t|matches!(t.f,-2|0|2)));
 println!("grade2_frequency_support=[-2p,0,2p]");println!("grade2_reality=true");println!("term_count={}",total.len());println!("direct_oscillatory_basis=-J0");
}
