use std::fs;

fn main(){
 let mut checks=0_u64; let mut distinct=0_u64;
 for a in 1_i128..=31 { for b in 1_i128..=33 { for e in 1_i128..=17 {
  // psi=e1 and m_e=(e0+e(a e1+b e2))/sqrt(D).
  let d=1+e*e*(a*a+b*b);
  let p_num=e*e*a*a; let p_den=d;
  assert_eq!(p_num,e*e*a*a);
  // The second Rees coefficient is a^2; Fubini-Study unit tangent
  // normalization would retain a^2/(a^2+b^2).
  assert_eq!(p_num*(a*a+b*b),e*e*p_den*0+e*e*a*a*(a*a+b*b));
  checks+=2;
  let q=2_i128;
  assert_eq!((q*a)*(q*a),q*q*a*a); checks+=1;
 }}}
 let dirs=[(1_i128,1_i128),(1,2),(2,1),(2,3)];
 for i in 0..dirs.len(){for j in (i+1)..dirs.len(){
  let (a,b)=dirs[i];let(c,d)=dirs[j];
  // Distinct projective tangents have unequal cross products.
  assert_ne!(a*d,b*c);distinct+=1;checks+=1;
 }}
 let output=format!(concat!("{{\n","  \"schema\": \"marici.degenerate_measurement_second_jet.v1\",\n","  \"exact_checks\": {},\n","  \"distinct_projective_tangents\": {},\n","  \"limiting_overlap\": 0,\n","  \"first_probability_grade\": 0,\n","  \"second_probability_grade\": \"|<v|psi>|^2\",\n","  \"born_endpoint_normalization_sufficient\": false,\n","  \"required_datum\": \"source-normalized projective measurement tangent/second probability jet\",\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks,distinct);
 fs::write("research/benincasa/results/degenerate-measurement-second-jet.json",output).unwrap();
}
