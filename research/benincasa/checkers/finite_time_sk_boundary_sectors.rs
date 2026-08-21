#[derive(Clone,Copy,Debug,Default)] struct C{re:f64,im:f64}
impl C{
 fn n(re:f64,im:f64)->Self{Self{re,im}} fn cj(self)->Self{Self::n(self.re,-self.im)}
 fn abs(self)->f64{(self.re*self.re+self.im*self.im).sqrt()}
}
impl std::ops::Add for C{type Output=Self;fn add(self,r:Self)->Self{Self::n(self.re+r.re,self.im+r.im)}}
impl std::ops::Sub for C{type Output=Self;fn sub(self,r:Self)->Self{Self::n(self.re-r.re,self.im-r.im)}}
impl std::ops::Mul for C{type Output=Self;fn mul(self,r:Self)->Self{Self::n(self.re*r.re-self.im*r.im,self.re*r.im+self.im*r.re)}}
impl std::ops::Mul<f64> for C{type Output=Self;fn mul(self,r:f64)->Self{Self::n(self.re*r,self.im*r)}}

fn ph(x:f64)->C{C::n(x.cos(),x.sin())}
fn gt(k:f64,a:f64,b:f64)->C{(C::n(1.,k*a)*C::n(1.,-k*b)*ph(-k*(a-b)))*(1./k.powi(3))}
fn lt(k:f64,a:f64,b:f64)->C{gt(k,a,b).cj()}
fn gab(a:i32,b:i32,k:f64,x:f64,y:f64)->C{match(a,b){
 (1,1)=>if x>=y{gt(k,x,y)}else{lt(k,x,y)},(1,-1)=>lt(k,x,y),
 (-1,1)=>gt(k,x,y),(-1,-1)=>if y>=x{gt(k,x,y)}else{lt(k,x,y)},_=>unreachable!()}}
fn ext(a:i32,p:f64,eta:f64,t:f64)->C{if a==1{gt(p,eta,t)}else{lt(p,eta,t)}}
fn ck(sum:f64,eta0:f64)->C{C::n(1./(sum*sum*eta0),-1./sum)}
fn bw(branch:i32,sum:f64,eta0:f64)->C{
 let c=ck(sum,eta0)*(1.0/(eta0*eta0)); if branch==1{c*(-1.)}else{c.cj()}
}
fn bulk_w(branch:i32,t:f64)->C{C::n(branch as f64/(t*t),0.)}
fn graph(a:i32,b:i32,wa:C,wb:C,p:f64,q:f64,k:f64,eta:f64,t1:f64,t2:f64)->C{
 wa*wb*ext(a,p,eta,t1)*ext(b,p,eta,t2)*gab(a,b,q,t1,t2)*gab(a,b,k,t1,t2)
}
fn main(){
 let(p,q,k,eta0,eta)=(1.1,0.8,0.9,-5.,-0.15); let sum=p+q+k;
 let n=20000usize;let h=(eta-eta0)/(n as f64);
 let mut mixed_bulk_boundary=C::default();let mut mixed_boundary_bulk=C::default();
 for i in 0..n{let t=eta0+(i as f64+0.5)*h;for a in[1,-1]{for b in[1,-1]{
  mixed_bulk_boundary=mixed_bulk_boundary+graph(a,b,bulk_w(a,t),bw(b,sum,eta0),p,q,k,eta,t,eta0)*h;
  mixed_boundary_bulk=mixed_boundary_bulk+graph(a,b,bw(a,sum,eta0),bulk_w(b,t),p,q,k,eta,eta0,t)*h;
 }}}
 let mut boundary_boundary=C::default();for a in[1,-1]{for b in[1,-1]{
  boundary_boundary=boundary_boundary+graph(a,b,bw(a,sum,eta0),bw(b,sum,eta0),p,q,k,eta,eta0,eta0);
 }}
 let mixed_defect=(mixed_bulk_boundary-mixed_boundary_bulk).abs()/mixed_bulk_boundary.abs().max(1e-30);
 assert!(mixed_defect<1e-12,"mixed placement defect={}",mixed_defect);
 assert!((mixed_bulk_boundary+mixed_boundary_bulk).im.abs()<1e-12);
 assert!(boundary_boundary.im.abs()<1e-12);
 println!("{{");
 println!("  \"schema\": \"marici.finite_time_sk_boundary_sectors.v1\",");
 println!("  \"grid\": {n},");
 println!("  \"mixed_bulk_boundary_re\": {:.15e},",mixed_bulk_boundary.re);
 println!("  \"mixed_boundary_bulk_re\": {:.15e},",mixed_boundary_bulk.re);
 println!("  \"mixed_placement_relative_defect\": {:.15e},",mixed_defect);
 println!("  \"mixed_sum_real\": true,");
 println!("  \"boundary_boundary_re\": {:.15e},",boundary_boundary.re);
 println!("  \"boundary_boundary_real\": true");
 println!("}}");
}
