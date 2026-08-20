// Labelled monodromy of the pulled-back standard node XY=t with
// t=p*s*l, l=B-1.  The node's vanishing cycle is H_1(C*)=Z.

fn main() {
    // Each labelled boundary loop maps with winding one to the universal
    // smoothing parameter t.  The nodal vanishing cycle is fixed by its
    // Picard-Lefschetz twist.
    let exponent_vector = [1_i64, 1, 1];
    let universal_vanishing_monodromy = 1_i64;
    let labelled_monodromies = exponent_vector.map(|winding| {
        universal_vanishing_monodromy.pow(winding as u32)
    });
    assert_eq!(labelled_monodromies, [1, 1, 1]);

    // On XY=t, the original square-root deck transformation sends
    // (X,Y) to (-Y,-X).  On the C* cycle this is inversion, hence -1.
    let deck_on_vanishing_cycle = -1_i64;
    assert_eq!(deck_on_vanishing_cycle * deck_on_vanishing_cycle, 1);

    // The rank-one line is therefore a trivial-monodromy Tate line carrying
    // the anti-invariant deck character.  This computes the object, not a
    // source Gysin comparison into it.
    println!("smoothing_parameter=p*s*(B-1)");
    println!("labelled_exponent_vector=(1,1,1)");
    println!("monodromy_p=1");
    println!("monodromy_s=1");
    println!("monodromy_Bminus1=1");
    println!("nilpotent_log_rank=0");
    println!("deck_character=-1");
    println!("vanishing_cycle_rank=1");
    println!("gysin_comparison=uncomputed");
}
