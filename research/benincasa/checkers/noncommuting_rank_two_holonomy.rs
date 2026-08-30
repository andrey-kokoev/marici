use std::fs;
type M=[[i128;4];4];
fn id()->M{[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]}
fn rot(i:usize,j:usize)->M{let mut r=id();r[i][i]=0;r[j][j]=0;r[j][i]=1;r[i][j]=-1;r}
fn mm(a:M,b:M)->M{let mut o=[[0_i128;4];4];for i in 0..4{for j in 0..4{for k in 0..4{o[i][j]+=a[i][k]*b[k][j];}}}o}
fn tr(a:M)->M{let mut o=[[0_i128;4];4];for i in 0..4{for j in 0..4{o[i][j]=a[j][i];}}o}
fn main(){
 let p=[[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]];
 let r13=rot(0,2);let a=mm(r13,r13);
 let b=mm(rot(3,0),mm(rot(2,1),mm(rot(1,3),rot(0,2))));
 assert_eq!(mm(mm(a,p),tr(a)),p);assert_eq!(mm(mm(b,p),tr(b)),p);
 let af=[[a[0][0],a[0][1]],[a[1][0],a[1][1]]];
 let bf=[[b[0][0],b[0][1]],[b[1][0],b[1][1]]];
 assert_eq!(af,[[-1,0],[0,1]]);assert_eq!(bf,[[0,1],[1,0]]);
 let ab=mm(a,b);let ba=mm(b,a);assert_ne!(ab,ba);
 let abf=[[ab[0][0],ab[0][1]],[ab[1][0],ab[1][1]]];
 let baf=[[ba[0][0],ba[0][1]],[ba[1][0],ba[1][1]]];
 assert_eq!(abf,[[0,-1],[1,0]]);assert_eq!(baf,[[0,1],[-1,0]]);
 let output=concat!("{\n","  \"schema\": \"marici.noncommuting_rank_two_holonomy.v1\",\n","  \"exact_checks\": 7,\n","  \"holonomy_A\": \"diag(-1,1)\",\n","  \"holonomy_B\": \"swap\",\n","  \"AB_equals_BA\": false,\n","  \"endpoint_projector_equal\": true,\n","  \"ordered_matrix_readout_required\": true,\n","  \"scalar_conjugacy_data_sufficient\": false,\n","  \"new_cut_carrier_stratum\": false\n","}\n");
 fs::write("research/benincasa/results/noncommuting-rank-two-holonomy.json",output).unwrap();
}
