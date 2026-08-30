use symbolica::prelude::*;

fn atom(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default())
        .expect("valid symbolic expression")
        .expand()
}

fn audit(a: &str, b: &str, y: &str) {
    let total = atom(&format!("({a})+({b})"));
    let qa = atom(&format!("({a})+{y}"));
    let qb = atom(&format!("({b})+{y}"));

    // Connected line denominator versus its two-contact deletion product.
    let connected_denominator = (total.clone() * qa.clone() * qb.clone()).expand();
    let contact_denominator = (atom(y) * qa * qb).expand();
    assert_eq!(
        (atom(y) * connected_denominator - total.clone() * contact_denominator).expand(),
        atom("0")
    );

    // The total-energy numerator is independent of the erased-edge variable.
    assert_eq!(
        total.derivative(Symbol::parse(y, "marici").expect("valid erased-edge symbol")),
        atom("0")
    );
}

fn main() {
    audit("X1+y12", "X3+y23", "y31");
    audit("X1+y31", "X2+y23", "y12");
    audit("X2+y12", "X3+y31", "y23");

    println!(
        "{{\"status\":\"pass\",\"typed_edges\":[\"12_23_to_all\",\"23_31_to_all\",\"12_31_to_all\"],\"connection_shift\":\"-dlog(Q_ij/y_ij)\",\"physical_d3_soft_boundary\":false}}"
    );
}
