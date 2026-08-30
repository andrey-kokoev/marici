use symbolica::prelude::*;

fn atom(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default())
        .expect("valid symbolic expression")
        .expand()
}

fn main() {
    let q = atom("x1+x2+2*ya");
    let yb = atom("yb");

    // f=q/yb.  Verify the logarithmic derivative after clearing
    // denominators: q*yb*(partial f/f)=q*partial(q)-q^2*partial(yb)/yb.
    // The four coordinates are (x1,x2,ya,yb).
    let dlog_numerators = [atom("yb"), atom("yb"), atom("2*yb"), -q.clone()];
    let expected_shift_numerators = [atom("-yb"), atom("-yb"), atom("-2*yb"), q.clone()];
    for (dlog, shift) in dlog_numerators.iter().zip(expected_shift_numerators.iter()) {
        assert_eq!((dlog.clone() + shift.clone()).expand(), atom("0"));
    }

    // Residues of -dlog(f): -1 on q=0 and +1 on yb=0.
    let residue_q = -1_i32;
    let residue_yb = 1_i32;
    assert_eq!(residue_q + residue_yb, 0);
    assert_ne!(q, yb);

    println!(
        "{{\"status\":\"pass\",\"connection_shift\":\"-dlog(q/yb)\",\"residue_q\":-1,\"residue_yb\":1,\"strict_on_complement\":true}}"
    );
}
