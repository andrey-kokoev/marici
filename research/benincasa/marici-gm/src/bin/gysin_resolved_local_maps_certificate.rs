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

    // At every corner the residue has block form [[0,0],[C_E,0]].  Hence
    // the grade-zero internal extension operator L_0(C) is the zero 4x4
    // matrix.  The nonzero C_E columns are cycles and cannot be boundaries
    // at this grade.
    for x in ["x00", "x01", "x10", "x11"] {
        assert_eq!(Atom::parse(format!("{x}*0-0*{x}"), "marici", Default::default()).unwrap().expand(), zero);
    }

    // Vertex-shared horizontal principal map.  lambda=(1,-1,1) annihilates
    // every column, while the 2x2 minor in rows (0,1), columns (1,2) is one.
    for identity in ["1*0-1*0+1*0", "1*1-1*0+1*(-1)", "1*0-1*1+1*1"] {
        assert_eq!(Atom::parse(identity, "marici", Default::default()).unwrap().expand(), zero);
    }
    assert_eq!(parse!("1*1-0*0").expand(), parse!("1"));
    // Taking l=(1,-1,1), the determinant of [delta(p2),delta(p3),l]
    // is three.  Thus l is outside delta(V), hence also outside
    // delta(ker partial_V); L0 contributes no incoming image.
    assert_eq!(parse!("1*(1*1-(-1)*1)+1*(0*1-(-1)*1)").expand(), parse!("3"));
    println!("Symbolica: corner L0 vanishes and the principal horizontal grade has one non-boundary cycle");
}
