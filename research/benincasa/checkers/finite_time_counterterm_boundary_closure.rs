#[derive(Clone,Copy,Debug,Default)]struct C{r:f64,i:f64}
impl C{fn n(r:f64,i:f64)->Self{Self{r,i}}fn abs(self)->f64{(self.r*self.r+self.i*self.i).sqrt()}}
impl std::ops::Add for C{type Output=Self;fn add(self,x:Self)->Self{Self::n(self.r+x.r,self.i+x.i)}}
impl std::ops::Sub for C{type Output=Self;fn sub(self,x:Self)->Self{Self::n(self.r-x.r,self.i-x.i)}}
impl std::ops::Mul for C{type Output=Self;fn mul(self,x:Self)->Self{Self::n(self.r*x.r-self.i*x.i,self.r*x.i+self.i*x.r)}}
impl std::ops::Mul<f64> for C{type Output=Self;fn mul(self,x:f64)->Self{Self::n(self.r*x,self.i*x)}}
impl std::ops::Div for C{type Output=Self;fn div(self,x:Self)->Self{let d=x.r*x.r+x.i*x.i;Self::n((self.r*x.r+self.i*x.i)/d,(self.i*x.r-self.r*x.i)/d)}}

fn falling(n:i32,r:usize)->f64{(0..r).map(|j|f64::from(n-j as i32)).product()}
fn pc(n:i32,r:usize,w:f64)->C{let s=if r%2==0{1.}else{-1.};C::n(s*falling(n,r),0.)/(0..=r).fold(C::n(1.,0.),|z,_|z*C::n(0.,w))}
fn monomials(op:&str,p:f64)->Vec<(i32,C)>{match op{
 "c1"=>vec![(0,C::n(p.powi(4),0.))],
 "c2"=>vec![(-2,C::n(p*p,0.)),(-1,C::n(0.,-2.*p.powi(3))),(0,C::n(-p.powi(4),0.))],
 "c3"=>vec![(0,C::n(p.powi(4),0.)),(1,C::n(0.,-2.*p.powi(5))),(2,C::n(-p.powi(6),0.))],
 _=>panic!("unknown counterterm")}}
fn coefficient(op:&str,grade:i32,eta:f64,p:f64)->C{
 let x=p*eta;let external=C::n(1.,x)*C::n(1.,x);let mut endpoint=C::default();
 for(n,c)in monomials(op,p){for r in 0..=8{let power=n-r as i32;if power<grade{break}if power==grade{endpoint=endpoint+c*pc(n,r,2.*p)*(-1.);}}}
 // The in-in commutator supplies -i. Common real normalizations are irrelevant.
 external*endpoint*C::n(0.,-1.)
}
fn interpolate(op:&str,grade:i32,p:f64)->([C;3],f64){let h=0.2;let fm=coefficient(op,grade,-h,p);let f0=coefficient(op,grade,0.,p);let fp=coefficient(op,grade,h,p);let a=[f0,(fp-fm)*(1./(2.*h)),(fp+fm-f0*2.)*(1./(2.*h*h))];let probe=0.31;let fit=a[0]+a[1]*probe+a[2]*(probe*probe);(a,(coefficient(op,grade,probe,p)-fit).abs())}
fn obstruction(a:[C;3],p:f64)->f64{let cc=2.*a[0].r;let ec=2.*a[1].r;let e2c=2.*a[2].r;let ss=2.*a[0].i;let es=2.*a[1].i;let e2s=2.*a[2].i;[ec+2.*p*ss,p*p*ss+e2s,p*p*cc+e2c,-2.*p*cc+es].iter().fold(0.0_f64,|m,x|m.max(x.abs()))}
fn main(){let p=1.1;let cases=[("c1",0),("c2",0),("c3",2),("c3",1),("c3",0)];let mut maximum=0.0_f64;
 for(op,grade)in cases{let(a,interp)=interpolate(op,grade,p);let defect=obstruction(a,p);maximum=maximum.max(interp).max(defect);println!("operator={op} grade={grade} interpolation={interp:.17e} closure={defect:.17e}");assert!(interp<1e-11&&defect<1e-11);}
 println!("maximum_defect={maximum:.17e}");println!("all_counterterm_endpoint_grades_close=true");println!("new_response_direction_required=false");}
