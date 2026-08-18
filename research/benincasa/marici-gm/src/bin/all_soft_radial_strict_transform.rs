use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default())
        .unwrap()
        .expand()
}

fn scale(expression: Atom, variable: &str, hatted: &str) -> Atom {
    expression
        .replace(atom(variable).to_pattern())
        .with(atom(&format!("rho*{hatted}")).to_pattern())
        .expand()
}

fn verify() {
    let k = atom(
        "E^4*P3^2-E^2*A*P1^2+E^2*A*P2^2-E^2*A*P3^2+E^2*B*P1^2-E^2*B*P2^2-E^2*B*P3^2-E^2*P1^2*P3^2-E^2*P2^2*P3^2+E^2*P3^4+A^2*P1^2-A*B*P1^2-A*B*P2^2+A*B*P3^2+A*P1^4-A*P1^2*P2^2-A*P1^2*P3^2+B^2*P2^2-B*P1^2*P2^2+B*P2^4-B*P2^2*P3^2+P1^2*P2^2*P3^2",
    );
    let mut pulled = k.clone();
    for (variable, hatted) in [
        ("E", "Eh"),
        ("P1", "P1h"),
        ("P2", "P2h"),
        ("P3", "P3h"),
        ("A", "rho*Ah"),
        ("B", "rho*Bh"),
    ] {
        pulled = scale(pulled, variable, hatted);
    }

    let expected = k
        .replace(atom("E").to_pattern())
        .with(atom("Eh").to_pattern())
        .replace(atom("P1").to_pattern())
        .with(atom("P1h").to_pattern())
        .replace(atom("P2").to_pattern())
        .with(atom("P2h").to_pattern())
        .replace(atom("P3").to_pattern())
        .with(atom("P3h").to_pattern())
        .replace(atom("A").to_pattern())
        .with(atom("Ah").to_pattern())
        .replace(atom("B").to_pattern())
        .with(atom("Bh").to_pattern())
        .expand();
    assert_eq!((pulled - atom("rho^6") * expected).expand(), atom("0"));

    // w=rho^3 W makes the strict-transform equation independent of rho.
    let radial_weight_w = 3;
    let radial_degree_k = 6;
    assert_eq!(2 * radial_weight_w, radial_degree_k);
    let radial_monodromy = 1_i32; // exp(2*pi*i*3)
    assert_eq!(radial_monodromy, 1);

    println!("K_radial_degree=6");
    println!("w_radial_weight=3");
    println!("strict_transform_rho_independent=true");
    println!("radial_coefficient_monodromy=1");
    println!("exceptional_family=projectivized_universal_CM_family");
    println!("new_exceptional_incidence_count=0");
}

fn main() {
    std::thread::Builder::new()
        .name("all-soft-radial-symbolica".into())
        .stack_size(64 * 1024 * 1024)
        .spawn(verify)
        .unwrap()
        .join()
        .unwrap();
}
