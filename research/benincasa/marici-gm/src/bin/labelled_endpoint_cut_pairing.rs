use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn main() {
    // A_B=br+i bi and A_S=sr+i si.  Conjugation reverses i.
    let bb = atom("br^2+bi^2");
    let bs_left = atom("br*sr+bi*si+i*(bi*sr-br*si)");
    let bs_right = atom("br*sr+bi*si-i*(bi*sr-br*si)");
    let ss = atom("sr^2+si^2");
    let labelled_sum = (bb.clone() + bs_left.clone() + bs_right.clone() + ss.clone()).expand();
    let norm = atom("(br+sr)^2+(bi+si)^2");
    assert_eq!((labelled_sum.clone() - norm.clone()).expand(), atom("0"));
    let conjugated_left = bs_left
        .replace(atom("i").to_pattern()).with(atom("-i").to_pattern()).expand();
    assert_eq!((conjugated_left - bs_right).expand(), atom("0"));

    println!("bb={bb}");
    println!("mixed_sum={}", (atom("2") * atom("br*sr+bi*si")).expand());
    println!("ss={ss}");
    println!("labelled_cut_sum={}", labelled_sum.factor());
    println!("positive_norm={}", norm.factor());
    println!("location_multiplicities=1,2,1");
    println!("mixed_occurrences_exchanged_by_conjugation=true");
}
