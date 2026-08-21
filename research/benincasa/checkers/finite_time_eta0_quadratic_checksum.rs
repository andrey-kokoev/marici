#[derive(Clone,Copy,Default)]struct C{r:f64,i:f64}
impl C{fn n(r:f64,i:f64)->Self{Self{r,i}}fn cj(self)->Self{Self::n(self.r,-self.i)}}
impl std::ops::Add for C{type Output=Self;fn add(self,x:Self)->Self{Self::n(self.r+x.r,self.i+x.i)}}
impl std::ops::Sub for C{type Output=Self;fn sub(self,x:Self)->Self{Self::n(self.r-x.r,self.i-x.i)}}
impl std::ops::Mul for C{type Output=Self;fn mul(self,x:Self)->Self{Self::n(self.r*x.r-self.i*x.i,self.r*x.i+self.i*x.r)}}
impl std::ops::Mul<f64> for C{type Output=Self;fn mul(self,x:f64)->Self{Self::n(self.r*x,self.i*x)}}
fn ph(x:f64)->C{C::n(x.cos(),x.sin())}
fn gt(k:f64,a:f64,b:f64)->C{(C::n(1.,k*a)*C::n(1.,-k*b)*ph(-k*(a-b)))*(1./k.powi(3))}
fn lt(k:f64,a:f64,b:f64)->C{gt(k,a,b).cj()}
fn gab(a:i32,b:i32,k:f64,x:f64,y:f64)->C{match(a,b){
 (1,1)=>if x>=y{gt(k,x,y)}else{lt(k,x,y)},(1,-1)=>lt(k,x,y),
 (-1,1)=>gt(k,x,y),(-1,-1)=>if y>=x{gt(k,x,y)}else{lt(k,x,y)},_=>unreachable!()}}
fn ext(a:i32,p:f64,e:f64,t:f64)->C{if a==1{gt(p,e,t)}else{lt(p,e,t)}}
fn ck(s:f64,e0:f64)->C{C::n(1./(s*s*e0),-1./s)}
fn bw(a:i32,s:f64,e0:f64)->C{let c=ck(s,e0)*(1./(e0*e0));if a==1{c*(-1.)}else{c.cj()}}
fn nested(p:f64,q:f64,k:f64,e:f64,t1:f64,t2:f64)->C{
 (gt(p,e,t1)-lt(p,e,t1))*(gt(p,e,t2)*gt(q,t1,t2)*gt(k,t1,t2)-lt(p,e,t2)*lt(q,t1,t2)*lt(k,t1,t2))*(1./(t1*t1*t2*t2))
}
fn graph(a:i32,b:i32,wa:C,wb:C,p:f64,q:f64,k:f64,e:f64,t1:f64,t2:f64)->C{
 wa*wb*ext(a,p,e,t1)*ext(b,p,e,t2)*gab(a,b,q,t1,t2)*gab(a,b,k,t1,t2)
}
fn amplitude(p:f64,q:f64,k:f64,e0:f64,e:f64)->f64{
 let span=e-e0;let n=(span/0.018).ceil()as usize;let h=span/(n as f64);let s=p+q+k;
 let mut tri=C::default();let mut m1=C::default();let mut m2=C::default();
 for i in 0..n{let t1=e0+(i as f64+0.5)*h;
  for j in 0..=i{let t2=e0+(j as f64+0.5)*h;let w=if j==i{0.5}else{1.};tri=tri+nested(p,q,k,e,t1,t2)*(w*h*h);}
  for a in[1,-1]{for b in[1,-1]{
   let bulk=C::n(a as f64/(t1*t1),0.);
   m1=m1+graph(a,b,bulk,bw(b,s,e0),p,q,k,e,t1,e0)*h;
   m2=m2+graph(a,b,bw(a,s,e0),bulk,p,q,k,e,e0,t1)*h;
  }}
 }
 let mut bb=C::default();for a in[1,-1]{for b in[1,-1]{bb=bb+graph(a,b,bw(a,s,e0),bw(b,s,e0),p,q,k,e,e0,e0);}}
 let inside=tri*2.0+m1+m2+bb;assert!(inside.i.abs()<2e-8);let spatial=(p*p+q*q+k*k).powi(2);-0.5*inside.r*spatial
}
fn solve(mut a:Vec<Vec<f64>>,mut b:Vec<f64>)->Vec<f64>{let n=b.len();for i in 0..n{let mut m=i;for j in i+1..n{if a[j][i].abs()>a[m][i].abs(){m=j}}a.swap(i,m);b.swap(i,m);let d=a[i][i];for k in i..n{a[i][k]/=d}b[i]/=d;for j in 0..n{if j!=i{let f=a[j][i];for k in i..n{a[j][k]-=f*a[i][k]}b[j]-=f*b[i]}}}b}
fn main(){
 let(p,q,k,e)=(1.1,0.8,0.9,-0.15);let theta=0.73;let mut rows=Vec::new();let mut ys=Vec::new();
 for cycle in 3..11{let e0=e-(theta+2.*std::f64::consts::PI*(cycle as f64))/(2.*p);let y=amplitude(p,q,k,e0,e);rows.push(vec![e0*e0,e0,1.,1./e0,1./(e0*e0)]);ys.push(y);}
 let m=5;let mut ata=vec![vec![0.;m];m];let mut aty=vec![0.;m];for(r,y)in rows.iter().zip(&ys){for i in 0..m{aty[i]+=r[i]*y;for j in 0..m{ata[i][j]+=r[i]*r[j]}}}
 let c=solve(ata,aty);let s=(p*p+q*q+k*k).powi(2);let sum=p+q+k;let d=q+k-p;
 let j0=s/(p.powi(3)*q*k*sum*sum);let j1=s/(p.powi(4)*q*k*d);let j2=s/(p.powi(3)*q*k*sum*d);
 let f=(1.-p*p*e*e)*theta.cos()+2.*p*e*theta.sin();let predicted=(f*(j1-2.*j0-4.*j2)-(1.+p*p*e*e)*j0)/p;
 let rel=(c[0]-predicted).abs()/predicted.abs().max(1e-30);
 println!("{{\n  \"schema\": \"marici.finite_time_eta0_quadratic_checksum.v1\",\n  \"status\": \"naive_fit_rejected\",\n  \"sample_count\": 8,\n  \"fitted_eta0_squared\": {:.15e},\n  \"source_pointwise_prediction\": {:.15e},\n  \"relative_defect\": {:.15e},\n  \"reason\": \"unresolved internal frequencies alias into a polynomial fit along a fixed external phase\"\n}}",c[0],predicted,rel);
}
