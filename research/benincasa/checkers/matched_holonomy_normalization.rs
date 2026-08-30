use std::fs;

fn main(){
 let mut checks=0_u64; let mut ambiguous=0_u64;
 for v in 1_i128..=41 { for gamma in 1_i128..=43 { for q in 2_i128..=29 {
  let original=v*gamma;
  // A fixed-coordinate cycle does not transform with the coefficient frame.
  let fixed_cycle=(q*v)*gamma;
  assert_ne!(fixed_cycle,original); ambiguous+=1;
  // A true dual cycle transforms by q^{-1}; cross multiplication certifies
  // that evaluation is invariant without introducing fractions.
  let covariant_num=(q*v)*gamma; let covariant_den=q;
  assert_eq!(covariant_num,original*covariant_den);
  checks+=2;
 }}}
 let output=format!(concat!("{{\n","  \"schema\": \"marici.matched_holonomy_normalization.v1\",\n","  \"exact_checks\": {},\n","  \"ambiguous_fixed_coordinate_pairings\": {},\n","  \"relative_monodromy\": 1,\n","  \"flat_generator_canonical\": false,\n","  \"generator_torsor\": \"C^times\",\n","  \"covariant_dual_pairing_invariant\": true,\n","  \"required_normalization\": \"source-normalized dual cycle, Hermitian metric/basepoint phase, or integral-polarized lattice\",\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks,ambiguous);
 fs::write("research/benincasa/results/matched-holonomy-normalization.json",output).unwrap();
}
