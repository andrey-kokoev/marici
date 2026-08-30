use symbolica::prelude::*;

fn atom(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default())
        .expect("valid symbolic expression")
        .expand()
}

fn main() {
    let q_total = atom("x1+x2+2*ya");
    let q1 = atom("x1+ya+yb");
    let q2 = atom("x2+ya+yb");

    // Equation (2.30), certified after clearing denominators.
    let denominator_a = atom("ya*(x1+x2+2*ya)*(x1+ya+yb)*(x2+ya+yb)");
    let denominator_ab = atom("ya*yb*(x1+ya+yb)*(x2+ya+yb)");
    assert_eq!(
        (atom("yb") * denominator_a - q_total.clone() * denominator_ab).expand(),
        atom("0")
    );
    assert_eq!((q_total.clone() - (q1.clone() + q2.clone() - atom("2*yb"))).expand(), atom("0"));

    // The adapter has zero valuation on either endpoint-contact divisor away
    // from yb=0 and q_total=0.  Substitution leaves a nonzero generic factor.
    let on_q1_numerator = q_total
        .clone()
        .replace(atom("x1").to_pattern())
        .with(atom("-ya-yb").to_pattern())
        .expand();
    let on_q2_numerator = q_total
        .replace(atom("x2").to_pattern())
        .with(atom("-ya-yb").to_pattern())
        .expand();
    assert_eq!(on_q1_numerator, atom("x2+ya-yb"));
    assert_eq!(on_q2_numerator, atom("x1+ya-yb"));

    println!(
        "{{\"status\":\"pass\",\"adjacent_map\":\"(x1+x2+2ya)/yb\",\"contact_valuations\":[0,0],\"exceptional_support\":[\"yb=0\",\"x1+x2+2ya=0\"]}}"
    );
}
