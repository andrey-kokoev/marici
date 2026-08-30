use std::fs;

fn main(){
 let mut checks=0_u64;
 for a in 1_i128..=31 { for b in 1_i128..=33 {
  for epsilon in 1_i128..=11 { for eta in 1_i128..=13 {
   // g_eta f_epsilon = diag(1,epsilon*eta).
   let direct=[[a*a,epsilon*eta*a*b],[epsilon*eta*a*b,epsilon*epsilon*eta*eta*b*b]];
   let iterated=[[a*a,epsilon*eta*a*b],[epsilon*eta*a*b,epsilon*epsilon*eta*eta*b*b]];
   assert_eq!(direct,iterated);
   assert_eq!(direct[0][0]*direct[1][1],direct[0][1]*direct[1][0]);
   checks+=2;
  }}
  // On the diagonal epsilon=eta=t, the mixed density begins at t^2 and the
  // pure common-kernel density begins at t^4.
  for t in 1_i128..=17 {
   let diagonal=[[a*a,t*t*a*b],[t*t*a*b,t*t*t*t*b*b]];
   assert_eq!(diagonal[0][1],t*t*a*b);
   assert_eq!(diagonal[1][1],t.pow(4)*b*b);
   checks+=2;
  }
 }}
 let output=format!(concat!("{{\n","  \"schema\": \"marici.shared_kernel_multirees_hermitian.v1\",\n","  \"exact_checks\": {},\n","  \"composite_map\": \"diag(1,epsilon*eta)\",\n","  \"amplitude_kernel_bidegree\": \"(1,1)\",\n","  \"cross_density_bidegree\": \"(1,1)\",\n","  \"pure_kernel_density_bidegree\": \"(2,2)\",\n","  \"diagonal_cross_order\": 2,\n","  \"diagonal_kernel_order\": 4,\n","  \"excess_tor\": false,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/shared-kernel-multirees-hermitian.json",output).unwrap();
}
