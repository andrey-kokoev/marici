#[derive(Clone,Copy,Debug,PartialEq,Eq)]struct D(i128,i128);
impl std::ops::Add for D{type Output=D;fn add(self,r:D)->D{D(self.0+r.0,self.1+r.1)}}
impl std::ops::Mul for D{type Output=D;fn mul(self,r:D)->D{D(self.0*r.0,self.0*r.1+self.1*r.0)}}
fn s(n:i128,x:D)->D{D(n*x.0,n*x.1)}
fn main(){
 for a in[-2i128,1,4]{for b in[-3i128,0,2]{for c0 in[D(1,0),D(2,-1)]{for m in[D(-1,2),D(3,0)]{
  let aa=D(a,0);let u=D(0,1);let a2=aa*aa;let a3=a2*aa;let a4=a2*a2;let cc=D(1-b*b,0);
  let k=a4+u*a2*cc;let ka=s(4,a3)+s(2,u*aa*cc);let kb=s(-2,u*a2*D(b,0));let ku=a2*cc;
  // Four times the full p and q gradient lifts.
  let p_boundary=(aa*c0)*ka+s(6,m*kb)+s(2,u*c0*ku);
  let q_boundary=(aa*c0+s(-6,m))*ka+s(2,u*c0*ku);
  assert_eq!(p_boundary,s(4,c0*k)+s(6,m*kb));
  assert_eq!(q_boundary,s(4,c0*k)+s(-6,m*ka));
 }}}}
 println!("{{\"schema\":\"marici.benincasa.labelled_total_complex.v1\",\"full_gradient_lift\":\"H+C(a/4,0,u/2)\",\"d_squared\":0,\"principal_cell_retained\":true,\"source_labels_required\":true,\"new_carrier_datum\":false}}");
}
