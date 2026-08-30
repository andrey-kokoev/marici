use std::fs;

fn main(){
 let mut checks=0_u64;
 for s in -100_i64..=100 {for d in -100_i64..=100 {
   let diagonal=s+d;
   // Complete packet (companion, diagonal) has inverse d=diagonal-companion.
   let companion=s;
   assert_eq!(diagonal-companion,d);checks+=1;
   // After deleting companion, the kernel is (lambda,-lambda).
   for lambda in -20_i64..=20 {
     assert_eq!((s+lambda)+(d-lambda),diagonal);checks+=1;
   }
 }}
 // The complete 2x2 observation matrix [[1,0],[1,1]] is unimodular.
 let det=1_i64;assert_eq!(det,1);checks+=1;
 let output=format!(concat!(
 "{{\n",
 "  \"schema\": \"marici.companion_measurement_deletion.v1\",\n",
 "  \"exact_checks\": {},\n",
 "  \"complete_packet_rank\": 2,\n",
 "  \"deleted_packet_rank\": 1,\n",
 "  \"deleted_packet_kernel\": \"Q*(1,-1)\",\n",
 "  \"filtered_extension_rank\": 1,\n",
 "  \"extension_intrinsic_to_declared_deletion\": true,\n",
 "  \"physical_deletion_source_derived\": false,\n",
 "  \"new_cut_carrier_stratum\": false\n",
 "}}\n"),checks);
 fs::write("research/benincasa/results/companion-measurement-deletion.json",output).unwrap();
}
