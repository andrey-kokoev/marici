#[derive(Clone, Copy, Debug, PartialEq, Eq)]
struct D(i128,i128); // x0 + u*x1, u^2=0
impl std::ops::Add for D{type Output=D;fn add(self,r:D)->D{D(self.0+r.0,self.1+r.1)}}
impl std::ops::Mul for D{type Output=D;fn mul(self,r:D)->D{D(self.0*r.0,self.0*r.1+self.1*r.0)}}
fn s(n:i128,x:D)->D{D(n*x.0,n*x.1)}
fn main(){
 for a in[-3i128,-1,2,5]{for b in[-2i128,0,3]{for m in[D(1,0),D(2,-1),D(-3,4)]{
  let aa=D(a,0);let u=D(0,1);
  let a2=aa*aa;let a3=a2*aa;let a4=a2*a2;let c=D(1-b*b,0);
  let k=a4+u*a2*c;
  let ka=s(4,a3)+s(2,u*aa*c);
  let ku=a2*c;
  // Twice the proposed lift is (a^2*m, 0, 2*u*a*m).
  let twice_lift_boundary=(a2*m)*ka+s(2,(u*aa*m)*ku);
  let h=s(2,aa*m);
  assert_eq!(twice_lift_boundary,s(2,h*k));
 }}}
 println!("{{\"schema\":\"marici.benincasa.a2_euler_homotopy.v1\",\"three_gradient_lift_exists\":true,\"lift\":\"(a^2 m/2,0,u a m)\",\"specialized_lift\":\"(a^2 m/2,0,0)\",\"new_carrier_datum\":false}}");
}
