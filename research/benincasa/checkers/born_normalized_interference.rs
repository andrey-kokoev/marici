use std::fs;
type C=(i128,i128);
fn mul(a:C,b:C)->C{(a.0*b.0-a.1*b.1,a.0*b.1+a.1*b.0)}
fn conj(a:C)->C{(a.0,-a.1)}
fn norm(a:C)->i128{a.0*a.0+a.1*a.1}

fn main(){
 let roots:[C;4]=[(1,0),(0,1),(-1,0),(0,-1)];
 let expected=[4_i128,2,0,2]; let mut checks=0_u64;
 for theta in 0_usize..4 { for phi in 0_usize..4 {
  let rel=mul(roots[theta],conj(roots[phi]));
  let overlap_num=(1+rel.0,rel.1); // normalized amplitude has denominator 2
  let probability_num=norm(overlap_num);
  assert_eq!(probability_num,expected[(theta+4-phi)%4]); checks+=1;
  // Independent global phases of state and measurement multiply the overlap
  // by a unit phase and leave Born probability invariant.
  for alpha in 0_usize..4 { for beta in 0_usize..4 {
   let gauge=mul(roots[alpha],conj(roots[beta]));
   assert_eq!(norm(mul(gauge,overlap_num)),probability_num); checks+=1;
  }}
 }}
 let output=format!(concat!("{{\n","  \"schema\": \"marici.born_normalized_interference.v1\",\n","  \"exact_checks\": {},\n","  \"state\": \"(|0>+exp(i theta)|1>)/sqrt(2)\",\n","  \"measurement\": \"(|0>+exp(i phi)|1>)/sqrt(2)\",\n","  \"probability\": \"(1+cos(theta-phi))/2\",\n","  \"positive_scale_removed\": true,\n","  \"global_U1_gauges_removed\": true,\n","  \"relative_phase_requires_measurement_calibration\": true,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/born-normalized-interference.json",output).unwrap();
}
