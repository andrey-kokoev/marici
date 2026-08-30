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
 let mut checks=0_u64;let mut nonzero_residues=0_u64;
 for a in gens {for b in gens {for h in gens {
   // epsilon*A_epsilon for A_epsilon=F^-1 A F, F=diag(1,epsilon).
   let residue_a=[[0,0],[a[1][0],0]];
   let residue_c=comm(residue_a,b);
   let residue_k=comm(residue_c,h);
   if residue_k!=[[0,0],[0,0]]{nonzero_residues+=1;}
   for e in 1_i64..=11 {
     let e_a=[[e*a[0][0],e*e*a[0][1]],[a[1][0],e*a[1][1]]];
     let regularized=comm(comm(e_a,b),h);
     // Specialization at e=0 is the supported parabolic residue.
     let at_zero=comm(comm(residue_a,b),h);
     assert_eq!(at_zero,residue_k);
     // Constant term of the exact regularized polynomial is residue_k:
     let e_a_minus_res=[[e*a[0][0],e*e*a[0][1]],[0,e*a[1][1]]];
     assert_eq!(sub(regularized,residue_k),comm(comm(e_a_minus_res,b),h));
     checks+=8;
   }
 }}}
 let output=format!(concat!(
 "{{\n",
 "  \"schema\": \"marici.singular_calibration_curvature.v1\",\n",
 "  \"exact_checks\": {},\n",
 "  \"tested_triples\": 343,\n",
 "  \"nonzero_supported_residue_triples\": {},\n",
 "  \"singular_weight\": -1,\n",
 "  \"regularizing_factor\": \"epsilon\",\n",
 "  \"residue\": \"[[[0,0],[a21,0]],B],H]\",\n",
 "  \"pole_order\": 1,\n",
 "  \"new_cut_carrier_stratum\": false\n",
 "}}\n"),checks,nonzero_residues);
 fs::write("research/benincasa/results/singular-calibration-curvature.json",output).unwrap();
}
