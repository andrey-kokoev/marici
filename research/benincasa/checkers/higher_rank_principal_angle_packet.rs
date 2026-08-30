use std::fs;

fn main(){
 let mut checks=0_u64;
 for x in 0_i128..=61 { for y in 0_i128..=67 {
  let s=x+y; let p=x*y;
  let mut prev2=2_i128; let mut prev1=s;
  assert_eq!(x*x-s*x+p,0); assert_eq!(y*y-s*y+p,0); checks+=2;
  for k in 2_u32..=9 {
   let current=s*prev1-p*prev2;
   assert_eq!(current,x.pow(k)+y.pow(k));
   prev2=prev1;prev1=current;checks+=1;
  }
 }}
 // Two realizable rank-two projector pairs with the same trace overlap one:
 // principal spectra {0,1} and {9/25,16/25}.  Their determinants differ.
 assert_eq!(0_i128*25+25,9+16);
 assert_ne!(0_i128*25,9_i128*16); checks+=2;
 let output=format!(concat!("{{\n","  \"schema\": \"marici.higher_rank_principal_angle_packet.v1\",\n","  \"exact_checks\": {},\n","  \"rank_two_packet\": \"trace and determinant of P Q P\",\n","  \"general_packet\": \"characteristic polynomial / squared principal-angle spectrum\",\n","  \"total_born_overlap_sufficient\": false,\n","  \"static_pair_classified_by_principal_angles\": true,\n","  \"loop_holonomy_tested\": false,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/higher-rank-principal-angle-packet.json",output).unwrap();
}
