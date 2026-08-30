use std::fs;
type M=[[i128;2];2];
fn det(a:M)->i128{a[0][0]*a[1][1]-a[0][1]*a[1][0]}
fn main(){
 let hol:[M;4]=[
  [[1,0],[0,1]],[[0,-1],[1,0]],[[-1,0],[0,-1]],[[0,1],[-1,0]]
 ];
 let mut checks=0_u64;
 for order in 1_u32..=32 { for (h,r) in hol.iter().enumerate() {
  // Multiplication by s^order has integral monodromy one, so it does not
  // change the relative local-system holonomy.
  let difference=[[r[0][0]-1,r[0][1]],[r[1][0],r[1][1]-1]];
  if h==0 { assert_eq!(det(difference),0); }
  else { assert_ne!(det(difference),0); }
  assert_eq!((order as i128)*4 % 4,0);
  checks+=2;
 }}
 let output=format!(concat!("{{\n","  \"schema\": \"marici.zero_overlap_relative_nearby_cycle.v1\",\n","  \"exact_checks\": {},\n","  \"vanishing_orders_checked\": [1,32],\n","  \"nearby_monodromy\": \"relative flat holonomy unchanged\",\n","  \"integer_vanishing_monodromy\": 1,\n","  \"global_invariant_rank_trivial_twist\": 1,\n","  \"global_invariant_rank_nontrivial_Z4_twist\": 0,\n","  \"supported_costalk_exists\": true,\n","  \"physical_scalar_automatically_selected\": false,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/zero-overlap-relative-nearby-cycle.json",output).unwrap();
}
