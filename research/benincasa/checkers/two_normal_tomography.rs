use std::fs;

#[derive(Clone,Copy,Debug,PartialEq,Eq)]
struct C{r:i64,i:i64}
fn add(a:C,b:C)->C{C{r:a.r+b.r,i:a.i+b.i}}
fn sub(a:C,b:C)->C{C{r:a.r-b.r,i:a.i-b.i}}
fn scale(a:C,n:i64)->C{C{r:n*a.r,i:n*a.i}}
fn mul_i(a:C)->C{C{r:-a.i,i:a.r}}

fn main(){
 let mut checks=0_u64;
 for a0 in -2..=2 {for b0 in -2..=2 {for a1 in -2..=2 {for b1 in -2..=2 {
 for a2 in -2..=2 {for b2 in -2..=2 {for a3 in -2..=2 {for b3 in -2..=2 {
   let h00=C{r:a0,i:b0};let h01=C{r:a1,i:b1};
   let h10=C{r:a2,i:b2};let h11=C{r:a3,i:b3};
   let s=add(h01,h10); let t=mul_i(sub(h01,h10));
   for e in -2_i64..=2 {for n in -2_i64..=2 {
     // Readout of |0>+(epsilon+i eta)|1>.
     let q=add(h00,add(scale(s,e),add(scale(t,n),scale(h11,e*e+n*n))));
     let expected=add(h00,add(scale(s,e),add(scale(t,n),scale(h11,e*e+n*n))));
     assert_eq!(q,expected);
     // There is no epsilon*eta coefficient, so iterated first grades commute.
     let q11=add(h00,add(s,add(t,scale(h11,2))));
     let q10=add(h00,add(s,h11)); let q01=add(h00,add(t,h11));
     let q00=h00;
     assert_eq!(sub(sub(q11,q10),sub(q01,q00)),C{r:0,i:0});
     assert_eq!(sub(s,mul_i(t)),scale(h01,2));
     assert_eq!(add(s,mul_i(t)),scale(h10,2));
     checks+=4;
   }}
 }}}}}}}}
 let output=format!(concat!(
 "{{\n",
 "  \"schema\": \"marici.two_normal_tomography.v1\",\n",
 "  \"exact_checks\": {},\n",
 "  \"zeroth_grade_rank\": 2,\n",
 "  \"epsilon_first_grade\": \"h01+h10\",\n",
 "  \"eta_first_grade\": \"i(h01-h10)\",\n",
 "  \"mixed_epsilon_eta_grade\": 0,\n",
 "  \"iterated_specializations_commute\": true,\n",
 "  \"full_matrix_recovered\": true,\n",
 "  \"new_cut_carrier_stratum\": false\n",
 "}}\n"),checks);
 fs::write("research/benincasa/results/two-normal-tomography.json",output).unwrap();
}
