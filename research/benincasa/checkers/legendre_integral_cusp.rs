use std::fs;

type M=[[i64;2];2];
fn mul(a:M,b:M)->M {[[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],[a[1][0]*b[0][0]+a[1][1]*b[1][0],a[1][0]*b[0][1]+a[1][1]*b[1][1]]]}
fn tr(a:M)->M {[[a[0][0],a[1][0]],[a[0][1],a[1][1]]]}
fn sub(a:M,b:M)->M {[[a[0][0]-b[0][0],a[0][1]-b[0][1]],[a[1][0]-b[1][0],a[1][1]-b[1][1]]]}

fn main(){
 let id=[[1,0],[0,1]]; let j=[[0,1],[-1,0]];
 let t_leg=[[-1,-2],[0,-1]]; let t_src=[[1,2],[0,1]];
 let n=sub(t_src,id); let mut checks=0_u64;
 assert_eq!(mul(mul(tr(t_src),j),t_src),j); checks+=1;
 assert_eq!(mul(n,n),[[0,0],[0,0]]); checks+=1;
 assert_ne!(n,[[0,0],[0,0]]); checks+=1;
 assert_eq!(t_src[0][0]*t_src[1][1]-t_src[0][1]*t_src[1][0],1); checks+=1;
 // The Kummer sign cancels the Legendre factor's semisimple sign.
 let full=[[-t_leg[0][0],-t_leg[0][1]],[-t_leg[1][0],-t_leg[1][1]]];
 assert_eq!(full,t_src); checks+=1;
 // The primitive image of N has index two in its saturated invariant line.
 let image_generator=n[0][1].abs(); assert_eq!(image_generator,2); checks+=1;
 let output=format!(concat!(
 "{{\n",
 "  \"schema\": \"marici.legendre_integral_cusp.v2\",\n",
 "  \"exact_checks\": {},\n",
 "  \"legendre_factor_monodromy\": [[-1,-2],[0,-1]],\n",
 "  \"source_normalized_kummer_twisted_monodromy\": [[1,2],[0,1]],\n",
 "  \"semisimple_signs_cancel\": true,\n",
 "  \"nilpotent_rank\": 1,\n",
 "  \"nilpotent_square_zero\": true,\n",
 "  \"integral_cusp_width\": 2,\n",
 "  \"full_rank_nine_integral_extension_resolved\": false,\n",
 "  \"new_cut_carrier_stratum\": false\n",
 "}}\n"),checks);
 fs::write("research/benincasa/results/legendre-integral-cusp.json",output).unwrap();
}
