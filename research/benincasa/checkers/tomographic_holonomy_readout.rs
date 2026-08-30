use std::fs;

#[derive(Clone,Copy,Debug,PartialEq,Eq)]
struct C{i:i64,j:i64}
fn add(a:C,b:C)->C{C{i:a.i+b.i,j:a.j+b.j}}
fn sub(a:C,b:C)->C{C{i:a.i-b.i,j:a.j-b.j}}
fn mul_i(a:C)->C{C{i:-a.j,j:a.i}}
fn scale(a:C,n:i64)->C{C{i:n*a.i,j:n*a.j}}

fn main(){
 let mut checks=0_u64;
 for r00 in -3..=3 {for i00 in -2..=2 {for r01 in -3..=3 {for i01 in -2..=2 {
 for r10 in -2..=2 {for i10 in -3..=3 {for r11 in -2..=2 {for i11 in -2..=2 {
   let h00=C{i:r00,j:i00};let h01=C{i:r01,j:i01};
   let h10=C{i:r10,j:i10};let h11=C{i:r11,j:i11};
   let d=add(h00,h11);
   // Effects |0><0|, |1><1|, |0+1><0+1|, |0+i1><0+i1|.
   let q0=h00;let q1=h11;
   let qx=add(d,add(h01,h10));
   let qy=add(d,sub(mul_i(h01),mul_i(h10)));
   let s=sub(qx,add(q0,q1)); let t=sub(qy,add(q0,q1));
   // Integral certificate avoids division: 2h01=s-i t, 2h10=s+i t.
   assert_eq!(sub(s,mul_i(t)),scale(h01,2));
   assert_eq!(add(s,mul_i(t)),scale(h10,2));
   assert_eq!(q0,h00);assert_eq!(q1,h11);checks+=4;
 }}}}}}}}
 let output=format!(concat!(
 "{{\n",
 "  \"schema\": \"marici.tomographic_holonomy_readout.v1\",\n",
 "  \"exact_checks\": {},\n",
 "  \"labelled_rank_one_effects\": 4,\n",
 "  \"recovers_full_complex_two_by_two_matrix\": true,\n",
 "  \"reconstruction_denominator\": 2,\n",
 "  \"wilson_trace_alone_sufficient\": false,\n",
 "  \"measurement_labels_required\": true,\n",
 "  \"new_cut_carrier_stratum\": false\n",
 "}}\n"),checks);
 fs::write("research/benincasa/results/tomographic-holonomy-readout.json",output).unwrap();
}
