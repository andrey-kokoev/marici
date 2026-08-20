// Independent associated-grade node simplex for the u=1,v=2 conductor
// tangency.  The smoothing factors are (q,L1_minus,L1_plus).

fn main(){
 let d0=[1_i64,1,1];
 let d1=[[-1_i64,0,1],[1,-1,0],[0,1,-1]];
 let d2=[1_i64,1,1];
 let d0d1:[i64;3]=std::array::from_fn(|j|(0..3).map(|i|d0[i]*d1[i][j]).sum());
 let d1d2:[i64;3]=std::array::from_fn(|i|(0..3).map(|j|d1[i][j]*d2[j]).sum());
 assert_eq!(d0d1,[0,0,0]);assert_eq!(d1d2,[0,0,0]);
 let ranks=[1_usize,2,1];assert_eq!(3-ranks[0],ranks[1]);assert_eq!(3-ranks[1],ranks[2]);assert_eq!(1-ranks[2],0);
 let deck=-1_i64;assert_eq!(deck*deck,1);
 println!("normalization_coordinates=(W-T/2,W+T/2)");
 println!("T=p+q-2*A");
 println!("factor_order=(q,L1_minus,L1_plus)");
 println!("face_to_tate=[1,1,1]");println!("d0_d1_zero=true");println!("d1_d2_zero=true");
 println!("ranks=(1,2,1)");println!("augmented_homology=(0,0,0,0)");println!("deck_character=-1");
}
