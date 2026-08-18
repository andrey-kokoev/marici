fn main(){
 for a2 in[-3i128,0,2,7]{for k in[-5i128,1,4]{for h in[-2i128,3]{for d in[-7i128,0,6]{for p in[-4i128,2]{
  // The sector identity is d(a^2 f)=a^2 d(f)+h(f)K.
  let d_a2_f=a2*d+h*k;
  let left=d_a2_f+k*(a2*p-h);
  let right=a2*(d+k*p);
  assert_eq!(left,right);
 }}}}}
 println!("{{\"schema\":\"marici.benincasa.a2_principal_strictification.v1\",\"strict_chain_map\":true,\"source_action\":\"(f,p)->(a^2 f,a^2 p-h(f))\",\"principal_cell_required\":true,\"new_carrier_datum\":false}}");
}
