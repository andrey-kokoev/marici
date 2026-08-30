use std::fs;
type V=[i128;3];
fn cross(a:V,b:V)->V{[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]}
fn dot(a:V,b:V)->i128{a[0]*b[0]+a[1]*b[1]+a[2]*b[2]}

fn main(){
 let mut checks=0_u64;
 for x in -19_i128..=19 { for y in -21_i128..=21 {
  let d=1+x*x+y*y;
  // Bloch vector n=N/d for the projector of psi=(1,x+iy)/sqrt(d).
  let n=[2*x,2*y,1-x*x-y*y];
  // Numerators of partial_x n and partial_y n over d^2.
  let nx=[2*(1-x*x+y*y),-4*x*y,-4*x];
  let ny=[-4*x*y,2*(1+x*x-y*y),-4*y];
  // n dot (dn_x cross dn_y)=4/d^2, hence Berry curvature is
  // one half of this: 2 dx wedge dy/d^2.
  assert_eq!(dot(n,cross(nx,ny)),4*d*d*d);
  checks+=1;
 }}
 let output=format!(concat!("{{\n","  \"schema\": \"marici.complex_kernel_berry_curvature.v1\",\n","  \"exact_checks\": {},\n","  \"projector_chart\": \"psi=(1,z)/sqrt(1+|z|^2)\",\n","  \"berry_curvature\": \"2 dx wedge dy/(1+x^2+y^2)^2\",\n","  \"projector_formula\": \"F=(1/2)n dot (dn cross dn)\",\n","  \"local_phase_forgotten\": true,\n","  \"curvature_retained_by_density_path\": true,\n","  \"independent_flat_twist_retained\": false,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/complex-kernel-berry-curvature.json",output).unwrap();
}
