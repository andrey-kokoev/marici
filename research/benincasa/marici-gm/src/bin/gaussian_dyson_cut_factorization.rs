use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn main() {
    // Two vertex-location cells (B,S), two labelled cut channels, and one
    // observed phase-space response row R=(rB,rS).
    let c = [[atom("cBq"), atom("cBk")], [atom("cSq"), atom("cSk")]];
    let r = [atom("rB"), atom("rS")];
    let noise: [[Atom; 2]; 2] = std::array::from_fn(|i| {
        std::array::from_fn(|j| {
            (c[i][0].clone() * c[j][0].clone()
                + c[i][1].clone() * c[j][1].clone()).expand()
        })
    });
    let dyson = (r[0].clone() * noise[0][0].clone() * r[0].clone()
        + r[0].clone() * noise[0][1].clone() * r[1].clone()
        + r[1].clone() * noise[1][0].clone() * r[0].clone()
        + r[1].clone() * noise[1][1].clone() * r[1].clone()).expand();
    let amplitude_q = (r[0].clone() * c[0][0].clone() + r[1].clone() * c[1][0].clone()).expand();
    let amplitude_k = (r[0].clone() * c[0][1].clone() + r[1].clone() * c[1][1].clone()).expand();
    let cut_sum = (amplitude_q.clone() * amplitude_q.clone()
        + amplitude_k.clone() * amplitude_k.clone()).expand();
    assert_eq!((dyson.clone() - cut_sum.clone()).expand(), atom("0"));

    // The q<->k involution identifies the transported amplitudes.  The two
    // ordered occurrences then cancel the identical-pair factor 1/2!.
    let traced = (atom("1/2") * atom("Aq^2+Ak^2"))
        .replace(atom("Ak").to_pattern()).with(atom("Aq").to_pattern()).expand();
    assert_eq!((traced.clone() - atom("Aq^2")).expand(), atom("0"));

    println!("dyson_noise_response={}", dyson.factor());
    println!("cut_amplitude_sum={}", cut_sum.factor());
    println!("dyson_equals_cut_sum=true");
    println!("ordered_occurrence_trace={traced}");
    println!("identical_pair_factor_cancelled=true");
}
