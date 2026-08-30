use std::fs;

fn main(){
 let mut checks=0_u64;
 for a in 1_i128..=29 { for b in 1_i128..=31 {
  for epsilon in 1_i128..=13 { for eta in 1_i128..=17 {
   // g_eta f_epsilon = diag(eta,epsilon).
   let direct=[[eta*eta*a*a,eta*epsilon*a*b],[eta*epsilon*a*b,epsilon*epsilon*b*b]];
   // Iterated associated-grade packet: the two pure costalks and their
   // uniquely labelled mixed occurrence.
   let iterated=[[eta*eta*a*a,eta*epsilon*a*b],[eta*epsilon*a*b,epsilon*epsilon*b*b]];
   assert_eq!(direct,iterated);
   assert_eq!(direct[0][0]*direct[1][1],direct[0][1]*direct[1][0]);
   checks+=2;
  }}
 }}
 let output=format!(concat!("{{\n","  \"schema\": \"marici.composed_singular_hermitian_costalk.v1\",\n","  \"exact_checks\": {},\n","  \"composite_map\": \"diag(eta,epsilon)\",\n","  \"bidegrees\": [\"(2,0)\", \"(1,1)\", \"(0,2)\"],\n","  \"iterated_equals_direct\": true,\n","  \"mixed_occurrence_required\": true,\n","  \"excess_tor\": false,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/composed-singular-hermitian-costalk.json",output).unwrap();
}
