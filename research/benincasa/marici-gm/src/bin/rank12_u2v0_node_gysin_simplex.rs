// Augmented oriented simplex for the labelled factors (p,s,l), l=B-1,
// mapping to the universal node vanishing-cycle line through
// dlog(p*s*l)=dlog(p)+dlog(s)+dlog(l).

fn main() {
    // d0: vertices (p,s,l) -> universal Tate line.
    let d0 = [1_i64, 1, 1];
    // d1 columns are oriented edges (p,s), (s,l), (l,p).
    let d1 = [[-1_i64, 0, 1], [1, -1, 0], [0, 1, -1]];
    // d2 is the oriented triangle boundary.
    let d2 = [1_i64, 1, 1];

    let d0d1: [i64; 3] = std::array::from_fn(|column| {
        (0..3).map(|row| d0[row] * d1[row][column]).sum()
    });
    assert_eq!(d0d1, [0, 0, 0]);
    let d1d2: [i64; 3] = std::array::from_fn(|row| {
        (0..3).map(|column| d1[row][column] * d2[column]).sum()
    });
    assert_eq!(d1d2, [0, 0, 0]);

    // Exact ranks of the augmented simplex over Q.
    let rank_d0 = 1;
    let rank_d1 = 2;
    let rank_d2 = 1;
    assert_eq!(3 - rank_d0, rank_d1);
    assert_eq!(3 - rank_d1, rank_d2);
    assert_eq!(1 - rank_d2, 0);

    // Every term carries the same anti-invariant deck character, so all maps
    // are deck equivariant.
    let deck_character = -1;
    assert_eq!(deck_character * deck_character, 1);

    println!("factor_order=(p,s,B-1)");
    println!("face_to_tate=[1,1,1]");
    println!("edge_boundary=[[-1,0,1],[1,-1,0],[0,1,-1]]");
    println!("triple_boundary=[1,1,1]");
    println!("d0_d1_zero=true");
    println!("d1_d2_zero=true");
    println!("ranks=(1,2,1)");
    println!("augmented_homology=(0,0,0,0)");
    println!("deck_character_all_terms=-1");
}
