use std::fs;

fn main(){
 let mut checks=0_u64;
 for n in 3_usize..=12 {
  let mut transition=vec![1_i32;n]; transition[n-1]=-1;
  for mask in 0_usize..(1_usize<<n) {
   let gauge:Vec<i32>=(0..n).map(|i|if (mask>>i)&1==0 {1}else{-1}).collect();
   let mut amp_hol=1_i32; let mut density_hol=1_i32;
   for i in 0..n {
    let j=(i+1)%n;
    let transformed=gauge[j]*transition[i]*gauge[i];
    amp_hol*=transformed;
    density_hol*=transformed*transformed;
   }
   assert_eq!(amp_hol,-1);
   assert_eq!(density_hol,1);
   checks+=2;
  }
 }
 // Endpoint lift k -> -k leaves the rank-one projector fixed.
 let k=[3_i128,4_i128]; let minus=[-3_i128,-4_i128];
 let p=[[k[0]*k[0],k[0]*k[1]],[k[1]*k[0],k[1]*k[1]]];
 let q=[[minus[0]*minus[0],minus[0]*minus[1]],[minus[1]*minus[0],minus[1]*minus[1]]];
 assert_eq!(p,q); checks+=1;
 let output=format!(concat!("{{\n","  \"schema\": \"marici.rotating_kernel_z2_holonomy.v1\",\n","  \"exact_checks\": {},\n","  \"cycle_lengths_checked\": [3,12],\n","  \"amplitude_holonomy\": -1,\n","  \"density_holonomy\": 1,\n","  \"gauge_invariant\": true,\n","  \"coefficient_object\": \"real amplitude line local system\",\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/rotating-kernel-z2-holonomy.json",output).unwrap();
}
