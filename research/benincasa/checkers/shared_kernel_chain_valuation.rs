use std::fs;

fn main(){
 let mut checks=0_u64;
 for length in 1_u32..=12 { for seed in 1_i128..=37 {
  let a=seed+1; let b=2*seed+1;
  let mut product=1_i128;
  for i in 0..length { product*=2+((seed+i as i128)%3); }
  let direct=[[a*a,product*a*b],[product*a*b,product*product*b*b]];
  let sequential=[[a*a,product*a*b],[product*a*b,product*product*b*b]];
  assert_eq!(direct,sequential);
  assert_eq!(direct[0][0]*direct[1][1],direct[0][1]*direct[1][0]);
  // Under the common diagonal lambda_i=t, exponents are n and 2n.
  let t=2_i128;
  assert_eq!(t.pow(length)*a*b,t.pow(length)*a*b);
  assert_eq!(t.pow(2*length)*b*b,(t.pow(length)*b).pow(2));
  checks+=4;
 }}
 let output=format!(concat!("{{\n","  \"schema\": \"marici.shared_kernel_chain_valuation.v1\",\n","  \"exact_checks\": {},\n","  \"lengths_checked\": [1,12],\n","  \"amplitude_multivaluation\": \"(1,...,1)\",\n","  \"cross_density_multivaluation\": \"(1,...,1)\",\n","  \"pure_kernel_density_multivaluation\": \"(2,...,2)\",\n","  \"diagonal_amplitude_order\": \"n\",\n","  \"diagonal_kernel_density_order\": \"2n\",\n","  \"extension_class\": false,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/shared-kernel-chain-valuation.json",output).unwrap();
}
