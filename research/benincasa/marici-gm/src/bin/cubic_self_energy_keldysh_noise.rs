use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn main() {
    let greater_q = atom("Fq+rq/2");
    let lesser_q = atom("Fq-rq/2");
    let greater_k = atom("Fk+rk/2");
    let lesser_k = atom("Fk-rk/2");

    let noise = (greater_q.clone() * greater_k.clone()
        + lesser_q.clone() * lesser_k.clone()).expand().factor();
    let spectral = (greater_q * greater_k - lesser_q * lesser_k).expand().factor();

    assert_eq!((noise.clone() - atom("2*Fq*Fk+rq*rk/2")).expand(), atom("0"));
    assert_eq!((spectral.clone() - atom("Fq*rk+rq*Fk")).expand(), atom("0"));

    let diagonal_noise = noise
        .replace(atom("Fk").to_pattern()).with(atom("Fq").to_pattern())
        .replace(atom("rk").to_pattern()).with(atom("rq").to_pattern())
        .expand().factor();
    assert_eq!((diagonal_noise.clone() - atom("2*Fq^2+rq^2/2")).expand(), atom("0"));

    println!("noise_block={noise}");
    println!("spectral_block={spectral}");
    println!("diagonal_noise={diagonal_noise}");
    println!("contour_metric_removed_before_positivity_test=true");
}
