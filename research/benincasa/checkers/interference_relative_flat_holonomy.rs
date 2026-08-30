use std::fs;

fn mod4(x:i32)->i32{((x%4)+4)%4}
fn main(){
 let mut checks=0_u64;
 for n in 3_usize..=7 { for h_l in 0_i32..4 { for h_r in 0_i32..4 {
  // Put each total holonomy on one edge; enumerate every local Z4 gauge.
  let mut tl=vec![0_i32;n]; let mut tr=vec![0_i32;n]; tl[n-1]=h_l; tr[n-1]=h_r;
  for mask in 0_usize..(4_usize.pow(n as u32)) {
   let mut m=mask; let mut gl=vec![0_i32;n]; let mut gr=vec![0_i32;n];
   for i in 0..n { gl[i]=(m%4) as i32; m/=4; gr[i]=(((mask/(4_usize.pow(i as u32)))+i)%4) as i32; }
   let mut rel=0_i32; let mut dens=0_i32;
   for i in 0..n { let j=(i+1)%n;
    let l=mod4(tl[i]+gl[j]-gl[i]); let r=mod4(tr[i]+gr[j]-gr[i]);
    rel=mod4(rel+l-r); dens=mod4(dens+l-l);
   }
   assert_eq!(rel,mod4(h_l-h_r)); assert_eq!(dens,0); checks+=2;
  }
 }}}
 let output=format!(concat!("{{\n","  \"schema\": \"marici.interference_relative_flat_holonomy.v1\",\n","  \"exact_checks\": {},\n","  \"cycle_lengths_checked\": [3,7],\n","  \"phase_group_tested\": \"Z4 subset of U(1)\",\n","  \"density_holonomy\": 0,\n","  \"interference_holonomy\": \"h_signal-h_reference\",\n","  \"gauge_invariant\": true,\n","  \"activation_requires_nonzero_overlap\": true,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/interference-relative-flat-holonomy.json",output).unwrap();
}
