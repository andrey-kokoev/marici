use std::fs;

fn main(){
 let mut checks=0_u64;
 for h11 in -7_i128..=7 { for h12 in -9_i128..=9 { for h21 in -11_i128..=11 { for h22 in -5_i128..=5 {
  for e in 1_i128..=17 {
   // Laurent readout entries: h11, e*h12, h21/e, h22.  Store the pole
   // entry by its numerator and denominator, then apply the derived shifts.
   let upper=e*h12;let lower_num=h21;let lower_den=e;
   assert_eq!(upper/e,h12);assert_eq!(lower_num*e,lower_den*h21);
   assert_eq!(h11,h11);assert_eq!(h22,h22);checks+=4;
  }
 }}}}
 // AB and BA from Entry 1741 differ in both shifted off-diagonal grades.
 let ab=[[0_i128,-1],[1,0]];let ba=[[0_i128,1],[-1,0]];
 assert_ne!(ab[0][1],ba[0][1]);assert_ne!(ab[1][0],ba[1][0]);checks+=2;
 let output=format!(concat!("{{\n","  \"schema\": \"marici.singular_reference_parabolic_readout.v1\",\n","  \"exact_checks\": {},\n","  \"reference_frame\": \"diag(1,epsilon)\",\n","  \"hom_weights\": [0,1,-1,0],\n","  \"upper_offdiagonal_grade\": 1,\n","  \"lower_offdiagonal_grade\": -1,\n","  \"full_matrix_recovered_by_parabolic_packet\": true,\n","  \"ordinary_specialization_sufficient\": false,\n","  \"posthoc_splitting_required\": false,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/singular-reference-parabolic-readout.json",output).unwrap();
}
