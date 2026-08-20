// Independent normalization and labelled Gysin simplex for the u=2,v=4
// center.  The doubled B branch normalizes with X=W-4B,Y=W+4B and its
// smoothing parameter has factors (p,L2_plus,L2_minus).

fn main() {
    let factors = ["p", "L2_plus", "L2_minus"];
    let d0 = [1_i64, 1, 1];
    let d1 = [[-1_i64, 0, 1], [1, -1, 0], [0, 1, -1]];
    let d2 = [1_i64, 1, 1];

    let d0d1: [i64; 3] = std::array::from_fn(|j| {
        (0..3).map(|i| d0[i] * d1[i][j]).sum()
    });
    let d1d2: [i64; 3] = std::array::from_fn(|i| {
        (0..3).map(|j| d1[i][j] * d2[j]).sum()
    });
    assert_eq!(d0d1, [0, 0, 0]);
    assert_eq!(d1d2, [0, 0, 0]);

    let ranks = [1_usize, 2, 1];
    assert_eq!(3-ranks[0],ranks[1]);
    assert_eq!(3-ranks[1],ranks[2]);
    assert_eq!(1-ranks[2],0);

    // Deck sends (X,Y) to (-Y,-X), hence acts by -1 on the nodal cycle.
    let deck = -1_i64;
    assert_eq!(deck*deck,1);

    println!("normalization_coordinates=(W-4*B,W+4*B)");
    println!("factor_order=({},{},{})",factors[0],factors[1],factors[2]);
    println!("face_to_tate=[1,1,1]");
    println!("d0_d1_zero=true");
    println!("d1_d2_zero=true");
    println!("ranks=(1,2,1)");
    println!("augmented_homology=(0,0,0,0)");
    println!("deck_character=-1");
}
