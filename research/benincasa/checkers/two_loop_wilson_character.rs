use std::collections::BTreeSet;
use std::fs;
type M=[[i128;2];2];
fn id()->M{[[1,0],[0,1]]}
fn mm(a:M,b:M)->M{[[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],[a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]]}
fn tr(a:M)->i128{a[0][0]+a[1][1]} fn tp(a:M)->M{[[a[0][0],a[1][0]],[a[0][1],a[1][1]]]}
fn word(bits:usize,n:usize,a:M,b:M)->M{let mut o=id();for i in 0..n{o=mm(o,if(bits>>i)&1==0{a}else{b});}o}
fn rotate(bits:usize,n:usize)->usize{((bits>>1)|((bits&1)<<(n-1)))&((1<<n)-1)}
fn main(){
 let a=[[-1,0],[0,1]];let b=[[0,1],[1,0]];
 let gauges=[id(),[[-1,0],[0,-1]],a,[[-a[0][0],0],[0,-a[1][1]]],b,[[0,-1],[-1,0]],[[0,-1],[1,0]],[[0,1],[-1,0]]];
 let mut checks=0_u64;let mut values=BTreeSet::new();
 for n in 1_usize..=10{for bits in 0_usize..(1_usize<<n){
  let w=word(bits,n,a,b);let value=tr(w);values.insert(value);
  let mut r=bits;for _ in 0..n{r=rotate(r,n);assert_eq!(tr(word(r,n,a,b)),value);checks+=1;}
  for g in gauges{assert_eq!(tr(mm(mm(g,w),tp(g))),value);checks+=1;}
 }}
 let ab=mm(a,b);let ba=mm(b,a);assert_eq!(tr(ab),tr(ba));checks+=1;
 let comm=mm(mm(mm(a,b),a),b);assert_eq!(comm,[[-1,0],[0,-1]]);assert_eq!(tr(comm),-2);checks+=2;
 assert_eq!(values,BTreeSet::from([-2_i128,0,2]));checks+=1;
 let output=format!(concat!("{{\n","  \"schema\": \"marici.two_loop_wilson_character.v1\",\n","  \"exact_checks\": {},\n","  \"word_lengths_checked\": [1,10],\n","  \"wilson_values\": [-2,0,2],\n","  \"trace_commutator\": -2,\n","  \"detects_noncommutativity\": true,\n","  \"distinguishes_AB_from_BA\": false,\n","  \"cyclic_word_invariant\": true,\n","  \"full_frame_recovered\": false,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/two-loop-wilson-character.json",output).unwrap();
}
