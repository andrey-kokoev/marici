use std::fs;

fn main(){
 let mut checks=0_u64;let mut accepted=0_u64;let mut relative_z=0_u64;
 // Vertices: three marked generators w0,w1,w2 and two algebraic lines a0,a1.
 // Entry 868's exact candidate has all six incidence coefficients nonzero.
 for mask in 0_u32..32 {
   let mut s=[1_i32;5];for i in 0..5{if (mask>>i)&1==1{s[i]=-1;}}
   let mut preserves=true;
   for wi in 0..3 {for aj in 3..5 {
     if s[wi]!=s[aj]{preserves=false;}checks+=1;
   }}
   if preserves{
     accepted+=1;
     if s[3]!=s[4]{relative_z+=1;}
   }
 }
 assert_eq!(accepted,2);assert_eq!(relative_z,0);checks+=2;
 let output=format!(concat!(
 "{{\n",
 "  \"schema\": \"marici.marked_extension_sign_centralizer.v1\",\n",
 "  \"sign_assignments_tested\": 32,\n",
 "  \"edge_checks\": {},\n",
 "  \"accepted_sign_assignments\": 2,\n",
 "  \"accepted_assignments\": [\"all_plus\",\"all_minus\"],\n",
 "  \"relative_Z_on_algebraic_lines_allowed\": false,\n",
 "  \"candidate_antiunitary_structure\": \"global_sign_times_K\",\n",
 "  \"source_identity_certificate_complete\": false,\n",
 "  \"new_cut_carrier_stratum\": false\n",
 "}}\n"),checks);
 fs::write("research/benincasa/results/marked-extension-sign-centralizer.json",output).unwrap();
}
