use std::fs;
type V=[i128;3];type M=[[i128;3];3];
fn mv(a:M,x:V)->V{[a[0][0]*x[0]+a[0][1]*x[1]+a[0][2]*x[2],a[1][0]*x[0]+a[1][1]*x[1]+a[1][2]*x[2],a[2][0]*x[0]+a[2][1]*x[1]+a[2][2]*x[2]]}
fn mm(a:M,b:M)->M{let mut o=[[0_i128;3];3];for i in 0..3{for j in 0..3{for k in 0..3{o[i][j]+=a[i][k]*b[k][j];}}}o}
fn tr(a:M)->M{[[a[0][0],a[1][0],a[2][0]],[a[0][1],a[1][1],a[2][1]],[a[0][2],a[1][2],a[2][2]]]}
fn main(){
 let e1=[1,0,0];let e2=[0,1,0];let e3=[0,0,1];
 let r12=[[0,-1,0],[1,0,0],[0,0,1]];
 let r23=[[1,0,0],[0,0,-1],[0,1,0]];
 let r31=[[0,0,1],[0,1,0],[-1,0,0]];
 assert_eq!(mv(r12,e1),e2);assert_eq!(mv(r23,e2),e3);assert_eq!(mv(r31,e3),e1);
 let h=mm(r31,mm(r23,r12));
 assert_eq!(mv(h,e1),e1);assert_eq!(mv(h,e2),e3);assert_eq!(mv(h,e3),[0,-1,0]);
 let p=[[0,0,0],[0,1,0],[0,0,1]];
 assert_eq!(mm(mm(h,p),tr(h)),p);
 assert_ne!(h,[[1,0,0],[0,1,0],[0,0,1]]);
 let reverse=tr(h);assert_eq!(mm(h,reverse),[[1,0,0],[0,1,0],[0,0,1]]);
 let checks=9_u64;
 let output=format!(concat!("{{\n","  \"schema\": \"marici.rank_two_projector_loop_holonomy.v1\",\n","  \"exact_checks\": {},\n","  \"loop\": \"e1->e2->e3->e1 octant triangle\",\n","  \"endpoint_projector_equal\": true,\n","  \"endpoint_principal_angles\": [0,0],\n","  \"fiber_holonomy\": \"[[0,-1],[1,0]] in basis (e2,e3)\",\n","  \"holonomy_nontrivial\": true,\n","  \"projector_path_required\": true,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/rank-two-projector-loop-holonomy.json",output).unwrap();
}
