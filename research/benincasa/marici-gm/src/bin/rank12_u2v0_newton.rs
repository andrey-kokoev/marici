use symbolica::prelude::*;

fn a(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn pulled(expression: &Atom) -> Atom {
    let mut out = expression.clone();
    for variable in ["p", "q", "A", "B"] {
        out = out
            .replace(a(variable).to_pattern())
            .with(a(&format!("rho*{variable}h")).to_pattern())
            .expand();
    }
    out
}

fn initial(expression: &Atom, order: usize) -> Atom {
    (pulled(expression) / a(&format!("rho^{order}")))
        .expand()
        .replace(a("rho").to_pattern())
        .with(a("0").to_pattern())
        .expand()
}

fn coefficient(expression: &Atom, order: usize) -> Atom {
    let rho = symbol!("marici::rho");
    let mut differentiated = pulled(expression);
    for _ in 0..order {
        differentiated = differentiated.derivative(rho).expand();
    }
    let factorial = (1..=order).product::<usize>().max(1);
    (differentiated / a(&factorial.to_string()))
        .replace(a("rho").to_pattern())
        .with(a("0").to_pattern())
        .expand()
}

fn valuation(expression: &Atom) -> (usize, Atom) {
    for order in 0..=12 {
        let candidate = initial(expression, order);
        if candidate != a("0") {
            return (order, candidate);
        }
    }
    panic!("valuation exceeds audit bound");
}

fn main() {
    // Source chart: u=E/X1, v=(X1+X2-X3)/X1, X1=1.
    // Center (u,v)=(2,0), marked intersection (a,b)=(2,1).
    let u = a("2+p");
    let v = a("q");
    let aa = a("2+A");
    let bb = a("1+B");
    let x = a("1");
    let y = ((&u + &v - a("2")) / a("2")).expand();
    let z = ((&u - &v) / a("2")).expand();
    let c = (-u.clone()).expand();

    let h = (&x * &x + &y * &y - &z * &z).expand();
    let ga = ((&x * &x - &c * &c) * (&x * &x - &y * &y - &z * &z)
        - a("2") * &c * &c * &z * &z).expand();
    let gb = ((&y * &y - &c * &c) * (&y * &y - &x * &x - &z * &z)
        - a("2") * &c * &c * &z * &z).expand();
    let hh = (&z * &z * ((&c * &c - &y * &y) * (&c * &c - &x * &x)
        + &c * &c * &z * &z)).expand();
    let k = (&aa * &aa * &aa * &aa - &h * &aa * &aa * &bb * &bb
        + &y * &y * &bb * &bb * &bb * &bb + &ga * &aa * &aa
        + &gb * &bb * &bb + &hh).expand();

    let k1a = (-a("2") * &c * (a("1") - &y * &y + &z * &z)).expand();
    let k1b = (-a("2") * &c * (&y * &y - a("1") + &z * &z)).expand();
    let k1h = (a("2") * &c * &z * &z
        * (a("2") * &c * &c - a("1") - &y * &y + &z * &z)).expand();
    let k1 = (&k1a * &aa * &aa + &k1b * &bb * &bb + &k1h).expand();
    let l1 = (&bb + a("1") - &u).expand();
    let l2 = (&aa + (&v - a("2") - &u) / a("2")).expand();

    let (vk, ik) = valuation(&k);
    let (vk1, ik1) = valuation(&k1);
    let (vl1, il1) = valuation(&l1);
    let (vl2, il2) = valuation(&l2);

    println!("center=(u,v,a,b)=(2,0,2,1)");
    println!("joint_ideal=(p,q,A,B)");
    println!("nu_K={vk}");
    println!("K_initial={}", ik.factor());
    println!("nu_K1={vk1}");
    println!("K1_initial={}", ik1.factor());
    println!("nu_L1={vl1}");
    println!("L1_initial={il1}");
    println!("nu_L2={vl2}");
    println!("L2_initial={il2}");
    for order in 2..=6 {
        println!("K_radial_{order}={}", coefficient(&k, order));
    }
    for order in 1..=5 {
        println!("K1_radial_{order}={}", coefficient(&k1, order));
    }
    let k3_on_double_plane = coefficient(&k, 3)
        .replace(a("ph").to_pattern())
        .with(a("1").to_pattern())
        .replace(a("Ah").to_pattern())
        .with(a("(3-qh)/2").to_pattern())
        .expand()
        .factor();
    println!("p_chart_K3_on_double_plane={k3_on_double_plane}");
    let form_orders = [-1_i32, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1];
    println!("relative_form_orders={form_orders:?}");
}
