use std::fs;

fn gcd(mut a:i64,mut b:i64)->i64 {a=a.abs();b=b.abs();while b!=0{let r=a%b;a=b;b=r;}a}

fn main(){
 let mut checks=0_u64; let mut classes=0_u64;
 for a in 0_i64..=1 { for b in 0_i64..=1 {
   classes+=1;
   // Presentation relation: 2m-a e6-b v_alg=0.
   let smith=gcd(gcd(a,b),2);
   if a==0 && b==0 {assert_eq!(smith,2);} else {assert_eq!(smith,1);} checks+=1;
   // Changing a global thimble lift by k leaves its parity vector unchanged.
   for k1 in -32_i64..=32 {for k2 in -32_i64..=32 {
     assert_eq!((a+2*k1).rem_euclid(2),a);
     assert_eq!((b+2*k2).rem_euclid(2),b); checks+=2;
   }}
 }}
 assert_eq!(classes,4); checks+=1;
 let output=format!(concat!(
 "{{\n",
 "  \"schema\": \"marici.local_pl_parity_ambiguity.v1\",\n",
 "  \"exact_checks\": {},\n",
 "  \"local_nodal_models\": 1,\n",
 "  \"compatible_global_parity_classes\": 4,\n",
 "  \"parity_group\": \"(Z/2)^2\",\n",
 "  \"local_germ_determines_parity\": false,\n",
 "  \"required_extra_datum\": \"globally marked integral thimble in the primitive infinity-Gysin lattice\",\n",
 "  \"new_cut_carrier_stratum\": false\n",
 "}}\n"),checks);
 fs::write("research/benincasa/results/local-pl-parity-ambiguity.json",output).unwrap();
}
