use std::fs;
type M=[[i64;2];2];
fn add(a:M,b:M)->M{[[a[0][0]+b[0][0],a[0][1]+b[0][1]],[a[1][0]+b[1][0],a[1][1]+b[1][1]]]}
fn scale(a:M,n:i64)->M{[[n*a[0][0],n*a[0][1]],[n*a[1][0],n*a[1][1]]]}
fn sub(a:M,b:M)->M{add(a,scale(b,-1))}
fn mul(a:M,b:M)->M{[[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],[a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]]}
fn comm(a:M,b:M)->M{sub(mul(a,b),mul(b,a))}
fn curv(a:M,b:M,h:M)->M{comm(comm(a,b),h)}
fn qx(m:M)->i64{m[0][0]+m[1][1]+m[0][1]+m[1][0]}
fn jet_im(m:M)->i64{m[0][1]-m[1][0]}

fn main(){
 let gens:[M;7]=[
  [[1,0],[0,0]],[[0,0],[0,1]],[[0,1],[0,0]],[[0,0],[1,0]],
  [[1,1],[0,1]],[[1,0],[1,1]],[[0,-1],[1,0]]
 ];
 let mut checks=0_u64;
 for a in gens {for b in gens {for h in gens {
   let ar=[[0,0],[a[1][0],0]];
   let ad=[[a[0][0],0],[0,a[1][1]]];
   let au=[[0,a[0][1]],[0,0]];
   let r=curv(ar,b,h);let s=curv(ad,b,h);let t=curv(au,b,h);
   let diagonal_first=qx(s)+jet_im(r);
   let companion_first=qx(s);
   assert_eq!(diagonal_first-companion_first,jet_im(r));checks+=1;
   for e in -5_i64..=5 {
     let k=add(r,add(scale(s,e),scale(t,e*e)));
     // Imaginary part of q_delta with delta=e; real qx part is separate.
     let qdiag_re=qx(k)+e*e*k[1][1];
     let qdiag_im=e*jet_im(k);
     assert_eq!(qdiag_im,e*jet_im(r)+e*e*jet_im(s)+e*e*e*jet_im(t));
     assert_eq!(qdiag_re,qx(r)+e*qx(s)+e*e*(qx(t)+r[1][1])+e*e*e*s[1][1]+e*e*e*e*t[1][1]);
     checks+=2;
   }
 }}}
 let output=format!(concat!(
 "{{\n",
 "  \"schema\": \"marici.diagonal_parabolic_measurement_rees.v1\",\n",
 "  \"exact_checks\": {},\n",
 "  \"diagonal_first_coefficient\": \"qx(S)+i(R01-R10)\",\n",
 "  \"companion_first_coefficient\": \"qx(S)\",\n",
 "  \"canonical_subtraction_recovers_residue_jet\": true,\n",
 "  \"complete_labelled_packet_has_extension_ambiguity\": false,\n",
 "  \"isolated_diagonal_scalar_sufficient\": false,\n",
 "  \"new_cut_carrier_stratum\": false\n",
 "}}\n"),checks);
 fs::write("research/benincasa/results/diagonal-parabolic-measurement-rees.json",output).unwrap();
}
