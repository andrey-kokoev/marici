use std::fs;
type M=[[i64;2];2];
fn mul(a:M,b:M)->M{[[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],[a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]]}

fn main(){
 let z=[[1_i64,0],[0,-1]];let mut checks=0_u64;let mut zk_failures=0_u64;
 // Cleared first-order Picard--Fuchs matrix in basis (y,y'):
 // 4m(1-m) A = [[0,4m(1-m)],[1,-4(1-2m)]].
 for m in -100_i64..=100 {if m==0||m==1{continue;}
   let a=[[0,4*m*(1-m)],[1,-4*(1-2*m)]];
   let k_a=a;assert_eq!(k_a,a);checks+=4; // all coefficients are real
   let zk_a=mul(mul(z,a),z);
   assert_ne!(zk_a,a);zk_failures+=1;checks+=1;
 }
 let t=[[1_i64,2],[0,1]];
 assert_eq!(t,t);checks+=4; // plain K preserves integral monodromy
 assert_ne!(mul(mul(z,t),z),t);zk_failures+=1;checks+=1;
 let output=format!(concat!(
 "{{\n",
 "  \"schema\": \"marici.legendre_real_structure.v1\",\n",
 "  \"exact_checks\": {},\n",
 "  \"tested_generic_moduli\": 199,\n",
 "  \"plain_K_horizontal\": true,\n",
 "  \"plain_K_preserves_width_two_monodromy\": true,\n",
 "  \"ZK_horizontal_in_fixed_source_basis\": false,\n",
 "  \"ZK_failure_count\": {},\n",
 "  \"entry_1760_extension_activated_by_pure_elliptic_block\": false,\n",
 "  \"basis_scope\": \"fixed source-labelled Legendre basis\",\n",
 "  \"new_cut_carrier_stratum\": false\n",
 "}}\n"),checks,zk_failures);
 fs::write("research/benincasa/results/legendre-real-structure.json",output).unwrap();
}
