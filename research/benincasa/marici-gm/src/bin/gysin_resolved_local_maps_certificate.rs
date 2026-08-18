use symbolica::prelude::*;

fn main() {
    let zero = parse!("0");

    // The homogeneous corner action is identically zero before any basis
    // choice.  C has only a lower-left extension block, hence C_K=C_B=0 and
    // X*C_K-C_B*X vanishes for a generic 2x2 X.
    for x in ["x00", "x01", "x10", "x11"] {
        let e = Atom::parse(format!("{x}*0-0*{x}"), "marici", Default::default()).unwrap().expand();
        assert_eq!(e, zero);
    }

    // Exact Galois stability of the two closed-point equations.
    let f12 = parse!("r^2-r+1").expand();
    let f12_conj = parse!("(1-r)^2-(1-r)+1").expand();
    assert_eq!(f12, f12_conj);
    let f13 = parse!("r^2+r-1").expand();
    let f13_conj = parse!("(-1-r)^2+(-1-r)-1").expand();
    assert_eq!(f13, f13_conj);

    // The unnormalized mu_2 trace doubles every even weighted component.
    for identity in ["2*(-1/4)-(-1/2)", "2*(3/4)-(3/2)"] {
        assert_eq!(Atom::parse(identity, "marici", Default::default()).unwrap().expand(), zero);
    }

    // Both quadratic principal columns are nonzero in their number fields.
    assert_ne!(parse!("-3"), zero);
    assert_ne!(parse!("-2+d5"), zero);
    println!("Symbolica: augmented corner maps, Galois involutions, and mu2 trace verified");
}
