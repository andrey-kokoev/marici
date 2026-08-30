use std::fs;
type V=[i128;2]; type M=[[i128;2];2];
fn mv(a:M,x:V)->V{[a[0][0]*x[0]+a[0][1]*x[1],a[1][0]*x[0]+a[1][1]*x[1]]}
fn mm(a:M,b:M)->M{[[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],[a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]]}
fn tr(a:M)->M{[[a[0][0],a[1][0]],[a[0][1],a[1][1]]]}
fn outer(a:V,b:V)->M{[[a[0]*b[0],a[0]*b[1]],[a[1]*b[0],a[1]*b[1]]]}
fn add(a:M,b:M)->M{[[a[0][0]+b[0][0],a[0][1]+b[0][1]],[a[1][0]+b[1][0],a[1][1]+b[1][1]]]}
fn h(a:V,b:V)->M{add(outer(a,b),outer(b,a))}
fn push(f:M,r:M)->M{mm(mm(f,r),tr(f))}

fn main(){
 let mut checks=0_u64;
 for x in 1_i128..=11 { for y in 1_i128..=13 { for z in 1_i128..=7 {
   let u=[x,y]; let v=[y,z];
   let f=[[1,z],[x,1]]; let g=[[2,1],[1,3]];
   assert_eq!(h(mv(f,u),mv(f,v)),push(f,h(u,v)));
   assert_eq!(outer(mv(f,u),mv(f,u)),push(f,outer(u,u)));
   assert_eq!(push(g,push(f,h(u,v))),push(mm(g,f),h(u,v)));
   checks+=3;
 }}}
 let output=format!(concat!("{{\n","  \"schema\": \"marici.hermitian_square_rees_functoriality.v1\",\n","  \"exact_checks\": {},\n","  \"density_map\": \"rho -> f rho f^T\",\n","  \"mixed_grade_natural\": true,\n","  \"composition_strict\": true,\n","  \"new_coherence_cell\": false,\n","  \"new_cut_carrier_stratum\": false\n","}}\n"),checks);
 fs::write("research/benincasa/results/hermitian-square-rees-functoriality.json",output).unwrap();
}
