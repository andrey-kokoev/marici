use std::fs;
type M=[[i64;2];2];
fn add(a:M,b:M)->M{[[a[0][0]+b[0][0],a[0][1]+b[0][1]],[a[1][0]+b[1][0],a[1][1]+b[1][1]]]}
fn neg(a:M)->M{[[-a[0][0],-a[0][1]],[-a[1][0],-a[1][1]]]}
fn sub(a:M,b:M)->M{add(a,neg(b))}
fn mul(a:M,b:M)->M{[[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],[a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]]}
fn comm(a:M,b:M)->M{sub(mul(a,b),mul(b,a))}
fn tr(a:M)->i64{a[0][0]+a[1][1]}

fn main(){
 let gens:[M;7]=[
  [[1,0],[0,0]],[[0,0],[0,1]],[[0,1],[0,0]],[[0,0],[1,0]],
  [[1,1],[0,1]],[[1,0],[1,1]],[[0,-1],[1,0]]
 ];
 let mut checks=0_u64;let mut nonzero=0_u64;
 for a in gens {for b in gens {
  let ab=comm(a,b);if ab!=[[0,0],[0,0]]{nonzero+=1;}
  for h00 in -3..=3 {for h01 in -3..=3 {for h10 in -3..=3 {for h11 in -3..=3 {
   let h=[[h00,h01],[h10,h11]];
   let route_ab=comm(a,comm(b,h));let route_ba=comm(b,comm(a,h));
   let defect=sub(route_ab,route_ba);let curvature=comm(ab,h);
   assert_eq!(defect,curvature);checks+=4;
   // Four labelled scalar effects reconstruct the complete defect.
   let q0=defect[0][0];let q1=defect[1][1];
   let qx=tr(defect)+defect[0][1]+defect[1][0];
   let qy_im=defect[0][1]-defect[1][0];
   let s=qx-q0-q1;
   assert_eq!(s-qy_im,2*defect[1][0]);
   assert_eq!(s+qy_im,2*defect[0][1]);checks+=2;
  }}}}
 }}
 let output=format!(concat!(
 "{{\n",
 "  \"schema\": \"marici.noncommuting_calibration_curvature.v1\",\n",
 "  \"exact_checks\": {},\n",
 "  \"calibration_pairs\": 49,\n",
 "  \"noncommuting_pairs\": {},\n",
 "  \"mixed_defect\": \"ad_[A,B](H)\",\n",
 "  \"jacobi_identity_verified\": true,\n",
 "  \"tomographic_packet_detects_complete_defect\": true,\n",
 "  \"classification\": \"coefficient_curvature\",\n",
 "  \"new_cut_carrier_stratum\": false\n",
 "}}\n"),checks,nonzero);
 fs::write("research/benincasa/results/noncommuting-calibration-curvature.json",output).unwrap();
}
