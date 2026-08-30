use std::fs;
type M=[[i128;2];2];
fn mm(a:M,b:M)->M{[[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],[a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]]}
fn inv(a:M)->M{let d=a[0][0]*a[1][1]-a[0][1]*a[1][0];assert!(d==1||d== -1);[[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]}
fn read(h:M,f:M)->M{mm(mm(inv(f),h),f)}
fn main(){
 let a=[[-1,0],[0,1]];let b=[[0,1],[1,0]];let ab=mm(a,b);let ba=mm(b,a);
 let frames=[[[1,0],[0,1]],[[1,1],[0,1]],[[1,0],[1,1]],[[0,-1],[1,0]],[[-1,0],[0,1]],[[0,1],[1,0]]];
 let mut checks=0_u64;
 for f in frames{let mab=read(ab,f);let mba=read(ba,f);assert_ne!(mab,mba);checks+=1;
  for g in frames{
   let transformed_h=mm(mm(g,ab),inv(g));let transformed_f=mm(g,f);
   assert_eq!(read(transformed_h,transformed_f),mab);checks+=1;
  }
  for s in frames{
   assert_eq!(read(ab,mm(f,s)),mm(mm(inv(s),mab),s));checks+=1;
  }
 }
 let output=format!(concat!("{{\n","  \"schema\": \"marici.framed_matrix_holonomy_readout.v1\",\n","  \"exact_checks\": {},\n","  \"readout\": \"inv(F) H F\",\n","  \"physical_fiber_gauge_invariant\": true,\n","  \"reference_relabelling_covariant\": true,\n","  \"distinguishes_AB_from_BA\": true,\n","  \"requires_labelled_reference_basis\": true,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/framed-matrix-holonomy-readout.json",output).unwrap();
}
