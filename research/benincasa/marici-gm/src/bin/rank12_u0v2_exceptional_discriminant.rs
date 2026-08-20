use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default())
        .unwrap()
        .expand()
}

fn clean(expression: Atom) -> Atom {
    expression.expand().together().cancel().factor()
}

fn main() {
    let s = atom("s");
    let alpha = atom("2") * (atom("1") - &s);
    let beta = -(s.clone() * &s + atom("2") * &s + atom("5")) / atom("2");
    let gamma = (&s + atom("1")) * (&s + atom("1"));
    let delta = (s.clone() * &s * &s + &s * &s + atom("3") * &s - atom("5"))
        / atom("2");
    let epsilon = (s.clone() * &s * &s * &s
        + atom("4") * &s * &s * &s
        + atom("14") * &s * &s
        - atom("44") * &s
        + atom("25"))
        / atom("16");

    let discriminant_a_zero = clean(&delta * &delta - atom("4") * &gamma * &epsilon);
    let determinant = clean(atom("4") * &gamma - &alpha * &alpha);
    let x_critical = clean((-atom("2") * &gamma * &beta + &alpha * &delta) / &determinant);
    let b_critical = clean((-atom("2") * &delta + &alpha * &beta) / &determinant);
    let critical_value = clean(
        &x_critical * &x_critical
            + &alpha * &x_critical * &b_critical
            + &beta * &x_critical
            + &gamma * &b_critical * &b_critical
            + &delta * &b_critical
            + &epsilon,
    );

    let l1_square_discriminant = clean(s.clone() * &s + atom("6") * &s + atom("1"));
    let l2_slope = clean(&s + atom("1"));
    let l2_constant = clean(&s - atom("1"));

    println!("A_zero_discriminant={discriminant_a_zero}");
    println!("nonzero_A_linear_determinant={determinant}");
    println!("nonzero_A_Xcritical={x_critical}");
    println!("nonzero_A_Bcritical={b_critical}");
    println!("nonzero_A_critical_value={critical_value}");
    println!("L1_square_collision={l1_square_discriminant}");
    println!("L2_square_slope={l2_slope}");
    println!("L2_square_constant={l2_constant}");
}
