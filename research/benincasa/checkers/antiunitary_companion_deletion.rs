use std::fs;
#[derive(Clone,Copy,Debug,PartialEq,Eq)]struct C{r:i64,i:i64}
type M=[[C;2];2];
fn c(r:i64,i:i64)->C{C{r,i}}
fn addc(a:C,b:C)->C{c(a.r+b.r,a.i+b.i)}
fn mulc(a:C,b:C)->C{c(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r)}
fn add(a:M,b:M)->M{[[addc(a[0][0],b[0][0]),addc(a[0][1],b[0][1])],[addc(a[1][0],b[1][0]),addc(a[1][1],b[1][1])]]}
fn scale(a:M,n:i64)->M{[[c(n*a[0][0].r,n*a[0][0].i),c(n*a[0][1].r,n*a[0][1].i)],[c(n*a[1][0].r,n*a[1][0].i),c(n*a[1][1].r,n*a[1][1].i)]]}
fn mul(a:M,b:M)->M{[[addc(mulc(a[0][0],b[0][0]),mulc(a[0][1],b[1][0])),addc(mulc(a[0][0],b[0][1]),mulc(a[0][1],b[1][1]))],[addc(mulc(a[1][0],b[0][0]),mulc(a[1][1],b[1][0])),addc(mulc(a[1][0],b[0][1]),mulc(a[1][1],b[1][1]))]]}
fn conj(a:M)->M{[[c(a[0][0].r,-a[0][0].i),c(a[0][1].r,-a[0][1].i)],[c(a[1][0].r,-a[1][0].i),c(a[1][1].r,-a[1][1].i)]]}

fn main(){
 let z=[[c(1,0),c(0,0)],[c(0,0),c(-1,0)]];
 let id=[[c(1,0),c(0,0)],[c(0,0),c(1,0)]];
 let x=[[c(0,0),c(1,0)],[c(1,0),c(0,0)]];
 let y=[[c(0,0),c(0,-1)],[c(0,1),c(0,0)]];
 let theta=|m:M|mul(mul(z,conj(m)),z);
 assert_eq!(theta(id),id);assert_eq!(theta(x),scale(x,-1));
 assert_eq!(theta(y),y);assert_eq!(theta(z),z);
 let mut checks=4_u64;
 for ai in -4..=4 {for ax in -4..=4 {for ay in -4..=4 {for az in -4..=4 {
   let m=add(add(scale(id,ai),scale(x,ax)),add(scale(y,ay),scale(z,az)));
   let expected=add(add(scale(id,ai),scale(x,-ax)),add(scale(y,ay),scale(z,az)));
   assert_eq!(theta(m),expected);assert_eq!(theta(theta(m)),m);checks+=2;
 }}}}
 let ex=add(id,x);let ey=add(id,y);
 assert_eq!(add(ex,theta(ex)),scale(id,2)); // invariant projection deletes X
 assert_eq!(theta(ey),ey);checks+=2;
 let output=format!(concat!(
 "{{\n",
 "  \"schema\": \"marici.antiunitary_companion_deletion.v1\",\n",
 "  \"exact_checks\": {},\n",
 "  \"involution\": \"Theta=ZK\",\n",
 "  \"pauli_characters\": {{\"I\":1,\"X\":-1,\"Y\":1,\"Z\":1}},\n",
 "  \"invariant_rank\": 3,\n",
 "  \"real_superposition_companion_deleted\": true,\n",
 "  \"imaginary_superposition_direction_retained\": true,\n",
 "  \"entry_1760_deletion_realized\": true,\n",
 "  \"cosmological_source_carries_theta\": false,\n",
 "  \"new_cut_carrier_stratum\": false\n",
 "}}\n"),checks);
 fs::write("research/benincasa/results/antiunitary-companion-deletion.json",output).unwrap();
}
