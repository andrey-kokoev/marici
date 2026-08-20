use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default())
        .unwrap()
        .expand()
}

fn radial_initial(expression: &Atom, order: usize) -> Atom {
    let mut pulled = expression.clone();
    for variable in ["p", "q", "A", "B"] {
        pulled = pulled
            .replace(atom(variable).to_pattern())
            .with(atom(&format!("rho*{variable}h")).to_pattern())
            .expand();
    }
    (pulled / atom(&format!("rho^{order}")))
        .expand()
        .replace(atom("rho").to_pattern())
        .with(atom("0").to_pattern())
        .expand()
}

fn main() {
    let p = atom("p");
    let q = atom("q");
    let a = atom("A");
    let b = atom("B-1");
    let x = atom("1");
    let y = (&p + &q) / atom("2");
    let z = atom("-1") + (&p - &q) / atom("2");
    let c = -p.clone();

    let h = (&x * &x + &y * &y - &z * &z).expand();
    let ga = ((&x * &x - &c * &c) * (&x * &x - &y * &y - &z * &z)
        - atom("2") * &c * &c * &z * &z)
        .expand();
    let gb = ((&y * &y - &c * &c) * (&y * &y - &x * &x - &z * &z)
        - atom("2") * &c * &c * &z * &z)
        .expand();
    let hh = (&z
        * &z
        * ((&c * &c - &y * &y) * (&c * &c - &x * &x)
            + &c * &c * &z * &z))
        .expand();

    let k = (&a * &a * &a * &a - &h * &a * &a * &b * &b
        + &y * &y * &b * &b * &b * &b
        + &ga * &a * &a
        + &gb * &b * &b
        + &hh)
        .expand();

    let k1a = (-atom("2") * &c * (atom("1") - &y * &y + &z * &z)).expand();
    let k1b = (-atom("2") * &c * (&y * &y - atom("1") + &z * &z)).expand();
    let k1h = (atom("2")
        * &c
        * &z
        * &z
        * (atom("2") * &c * &c - atom("1") - &y * &y + &z * &z))
        .expand();
    let k1 = (&k1a * &a * &a + &k1b * &b * &b + &k1h).expand();

    let k4 = radial_initial(&k, 4);
    let k1_3 = radial_initial(&k1, 3);
    let l1_1 = radial_initial(&atom("B-p"), 1);
    let l2_1 = radial_initial(&atom("A+(q-p)/2"), 1);
    assert_ne!(k4, atom("0"));
    assert_ne!(k1_3, atom("0"));
    assert_eq!(l1_1, atom("Bh-ph"));
    assert_eq!(l2_1, atom("Ah+(qh-ph)/2"));

    // A relative form n dA dB/(L1^a L2^b K^(h/2)) acquires
    // order nu(n)+2-a-b-2h on the joint blowup.  The classes below
    // preserve the source ordering (Omega111, Omega101, Omega110, e1..e9).
    let form_orders = [-2_i32, -1, -1, 2, 1, 0, 1, 0, -1, 0, 2, 2];

    println!("center=(u,v)=(0,2)");
    println!("joint_ideal=(p,q,A,B)");
    println!("nu_K=4");
    println!("nu_K1=3");
    println!("nu_L1=1");
    println!("nu_L2=1");
    println!("K_initial={k4}");
    println!("K_initial_factored={}", k4.clone().factor());
    println!("K1_initial={k1_3}");
    println!("K1_initial_factored={}", k1_3.clone().factor());
    println!("L1_initial={l1_1}");
    println!("L2_initial={l2_1}");
    println!("relative_form_orders={form_orders:?}");
}
