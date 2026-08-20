use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap().expand()
}

fn pulled(e: &Atom) -> Atom {
    let mut out = e.clone();
    for variable in ["p", "q", "A", "B"] {
        out = out
            .replace(a(variable).to_pattern())
            .with(a(&format!("rho*{variable}h")).to_pattern())
            .expand();
    }
    out
}

fn coeff(e: &Atom, order: usize) -> Atom {
    let rho = symbol!("marici::rho");
    let mut derivative = pulled(e);
    for _ in 0..order {
        derivative = derivative.derivative(rho).expand();
    }
    let factorial = (1..=order).product::<usize>().max(1);
    (derivative / a(&factorial.to_string()))
        .replace(a("rho").to_pattern())
        .with(a("0").to_pattern())
        .expand()
}

fn valuation(e: &Atom) -> (usize, Atom) {
    for order in 0..=12 {
        let coefficient = coeff(e, order);
        if coefficient != a("0") {
            return (order, coefficient);
        }
    }
    panic!("valuation exceeds bound")
}

fn main() {
    let u = a("2/3+p");
    let v = a("q");
    let aa = a("A");
    let bb = a("-1/3+B");
    let x = a("1");
    let y = ((&u + &v - a("2")) / a("2")).expand();
    let z = ((&u - &v) / a("2")).expand();
    let c = (-u.clone()).expand();
    let h = (&x * &x + &y * &y - &z * &z).expand();
    let ga = ((&x * &x - &c * &c) * (&x * &x - &y * &y - &z * &z)
        - a("2") * &c * &c * &z * &z)
        .expand();
    let gb = ((&y * &y - &c * &c) * (&y * &y - &x * &x - &z * &z)
        - a("2") * &c * &c * &z * &z)
        .expand();
    let hh = (&z * &z
        * ((&c * &c - &y * &y) * (&c * &c - &x * &x) + &c * &c * &z * &z))
        .expand();
    let k = (&aa * &aa * &aa * &aa - &h * &aa * &aa * &bb * &bb
        + &y * &y * &bb * &bb * &bb * &bb
        + &ga * &aa * &aa
        + &gb * &bb * &bb
        + &hh)
        .expand();
    let k1a = (-a("2") * &c * (a("1") - &y * &y + &z * &z)).expand();
    let k1b = (-a("2") * &c * (&y * &y - a("1") + &z * &z)).expand();
    let k1h = (a("2") * &c * &z * &z
        * (a("2") * &c * &c - a("1") - &y * &y + &z * &z))
        .expand();
    let k1 = (&k1a * &aa * &aa + &k1b * &bb * &bb + &k1h).expand();
    let l1 = (&bb + a("1") - &u).expand();
    let l2 = (&aa + (&v - a("2") - &u) / a("2")).expand();

    let base_k = k
        .replace(a("p").to_pattern()).with(a("0").to_pattern())
        .replace(a("q").to_pattern()).with(a("0").to_pattern())
        .expand();
    println!("K_base_factor={}", base_k.factor());
    println!("dA_K_base_factor={}", base_k.derivative(symbol!("marici::A")).expand().factor());
    println!("dB_K_base_factor={}", base_k.derivative(symbol!("marici::B")).expand().factor());

    let (vk, ik) = valuation(&k);
    let (vk1, ik1) = valuation(&k1);
    let (vl1, il1) = valuation(&l1);
    let (vl2, il2) = valuation(&l2);
    println!("center=(u,v,a,b)=(2/3,0,0,-1/3)");
    println!("joint_ideal=(p,q,A,B)");
    println!("nu_K={vk}");
    println!("K_initial={}", ik.factor());
    println!("nu_K1={vk1}");
    println!("K1_initial={}", ik1.factor());
    println!("nu_L1={vl1}");
    println!("L1_initial={il1}");
    println!("nu_L2={vl2}");
    println!("L2_initial={il2}");
    for order in vk..=6 {
        println!("K_radial_{order}={}", coeff(&k, order));
    }
    for order in vk1..=5 {
        println!("K1_radial_{order}={}", coeff(&k1, order));
    }
    let k3_on_double = coeff(&k, 3)
        .replace(a("Bh").to_pattern()).with(a("ph+qh").to_pattern())
        .expand();
    println!("K3_on_double_plane={}", k3_on_double.factor());
}
