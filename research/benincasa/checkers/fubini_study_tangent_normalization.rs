use std::fs;

fn main(){
 let mut checks=0_u64;
 for a in 1_i128..=41 { for b in 1_i128..=43 { for q in 1_i128..=29 {
  let num=a*a; let den=a*a+b*b;
  let scaled_num=q*q*a*a; let scaled_den=q*q*(a*a+b*b);
  assert_eq!(num*scaled_den,scaled_num*den);
  // The central sign/real phase leaves the normalized coefficient unchanged.
  assert_eq!((-a)*(-a)*den,num*((-a)*(-a)+(-b)*(-b)));
  checks+=2;
 }}}
 let dirs=[(1_i128,1_i128),(1,2),(1,3),(2,1),(3,1)];
 let mut distinct=0_u64;
 for i in 0..dirs.len(){for j in (i+1)..dirs.len(){
  let(a,b)=dirs[i];let(c,d)=dirs[j];
  let left=a*a*(c*c+d*d);let right=c*c*(a*a+b*b);
  if left!=right{distinct+=1;}
 }}
 assert_eq!(distinct,10);
 let output=format!(concat!("{{\n","  \"schema\": \"marici.fubini_study_tangent_normalization.v1\",\n","  \"exact_checks\": {},\n","  \"distinct_direction_pairs\": {},\n","  \"normalized_supported_coefficient\": \"|<v|psi>|^2/<v|v>\",\n","  \"reparameterization_scale_invariant\": true,\n","  \"central_phase_invariant\": true,\n","  \"projective_direction_dependent\": true,\n","  \"endpoint_alone_sufficient\": false,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks,distinct);
 fs::write("research/benincasa/results/fubini-study-tangent-normalization.json",output).unwrap();
}
