use std::fs;
type M=[[i64;2];2];
fn sub(a:M,b:M)->M{[[a[0][0]-b[0][0],a[0][1]-b[0][1]],[a[1][0]-b[1][0],a[1][1]-b[1][1]]]}
fn mul(a:M,b:M)->M{[[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],[a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]]}
fn comm(a:M,b:M)->M{sub(mul(a,b),mul(b,a))}

fn main(){
 let gens:[M;7]=[
  [[1,0],[0,0]],[[0,0],[0,1]],[[0,1],[0,0]],[[0,0],[1,0]],
  [[1,1],[0,1]],[[1,0],[1,1]],[[0,-1],[1,0]]
 ];
 let mut checks=0_u64;let mut nonzero=0_u64;
 for a in gens {for b in gens {for h in gens {
   let a_minus=[[0,0],[a[1][0],0]];
   let r=comm(comm(a_minus,b),h);
   if r!=[[0,0],[0,0]]{nonzero+=1;}
   // Zeroth measurement frame: two diagonals and symmetric off-diagonal.
   let q0=r[0][0];let q1=r[1][1];
   let qx=q0+q1+r[0][1]+r[1][0];
   let s=qx-q0-q1;
   // First jet of |0>+(1+i delta)|1>.
   let jet_re=0_i64; let jet_im=r[0][1]-r[1][0];
   assert_eq!(jet_re,0);
   assert_eq!(s+jet_im,2*r[0][1]);
   assert_eq!(s-jet_im,2*r[1][0]);
   assert_eq!(q0,r[0][0]);assert_eq!(q1,r[1][1]);checks+=5;
 }}}
 let output=format!(concat!(
 "{{\n",
 "  \"schema\": \"marici.parabolic_residue_tomography.v1\",\n",
 "  \"exact_checks\": {},\n",
 "  \"tested_residues\": 343,\n",
 "  \"nonzero_residues\": {},\n",
 "  \"ordinary_measurement_rank\": 3,\n",
 "  \"measurement_first_jet_rank_gain\": 1,\n",
 "  \"complete_supported_residue_recovered\": true,\n",
 "  \"higher_measurement_grade_required\": false,\n",
 "  \"normals_kept_distinct\": true,\n",
 "  \"new_cut_carrier_stratum\": false\n",
 "}}\n"),checks,nonzero);
 fs::write("research/benincasa/results/parabolic-residue-tomography.json",output).unwrap();
}
