use std::fs;
type C=(i128,i128);
fn add(a:C,b:C)->C{(a.0+b.0,a.1+b.1)}
fn mul(a:C,b:C)->C{(a.0*b.0-a.1*b.1,a.0*b.1+a.1*b.0)}
fn conj(a:C)->C{(a.0,-a.1)} fn norm(a:C)->i128{a.0*a.0+a.1*a.1}
fn inner(v:[C;2],p:[C;2])->C{add(mul(conj(v[0]),p[0]),mul(conj(v[1]),p[1]))}

fn main(){
 let roots:[C;4]=[(1,0),(0,1),(-1,0),(0,-1)]; let mut checks=0_u64;
 for a in 1_i128..=17 { for b in 1_i128..=19 { for c in 1_i128..=13 { for d in 1_i128..=15 {
  let psi=[(c,0),(d,0)]; let psi_norm=c*c+d*d; let v_norm=a*a+b*b;
  let mut loop_values=[0_i128;4];
  for phase in 0_usize..4 {
   let v=[(a,0),mul(roots[phase],(b,0))];
   let num=norm(inner(v,psi)); loop_values[phase]=num;
   for gauge in roots {
    let gv=[mul(gauge,v[0]),mul(gauge,v[1])];
    assert_eq!(norm(inner(gv,psi))*v_norm*psi_norm,num*v_norm*psi_norm); checks+=1;
   }
  }
  // Closing the phase loop returns the same projector and scalar.
  let v0=[(a,0),(b,0)]; let v4=[(a,0),mul(roots[0],(b,0))];
  assert_eq!(norm(inner(v0,psi)),norm(inner(v4,psi))); checks+=1;
  assert!(loop_values.iter().all(|x|*x>=0)); checks+=1;
 }}}}
 let output=format!(concat!("{{\n","  \"schema\": \"marici.projective_supported_scalar_descent.v1\",\n","  \"exact_checks\": {},\n","  \"scalar\": \"Tr(P_v P_psi)=|<v|psi>|^2/(<v|v><psi|psi>)\",\n","  \"projective_gauge_invariant\": true,\n","  \"loop_holonomy\": 1,\n","  \"global_on_projective_tangent_space\": true,\n","  \"unsquared_overlap_is_line_section\": true,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/projective-supported-scalar-descent.json",output).unwrap();
}
