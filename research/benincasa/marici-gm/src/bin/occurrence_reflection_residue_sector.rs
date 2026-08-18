use std::collections::BTreeMap;

fn main() {
    let sigma: BTreeMap<&str, &str> = [
        ("X1", "X1"), ("X2", "X3"), ("X3", "X2"),
        ("y12", "y31"), ("y23", "y23"), ("y31", "y12"),
        ("q_g1", "q_g1"), ("q_g2", "q_g3"), ("q_g3", "q_g2"),
        ("q_g12", "q_g31"), ("q_g23", "q_g23"), ("q_g31", "q_g12"),
        ("q_G12", "q_G31"), ("q_G23", "q_G23"), ("q_G31", "q_G12"),
    ].into_iter().collect();

    for (label, image) in &sigma {
        assert_eq!(sigma.get(image), Some(label), "sigma_23 must be involutive on {label}");
    }

    let source_a = ["q_g1", "q_g2", "q_g3", "q_G12", "q_g23"];
    let source_b = ["q_g1", "q_g2", "q_g3", "q_G12", "q_g31"];
    let image = |source: [&str; 5]| source.map(|name| *sigma.get(name).unwrap());
    let image_a = image(source_a);
    let image_b = image(source_b);

    assert_eq!(image_a, ["q_g1", "q_g3", "q_g2", "q_G31", "q_g23"]);
    assert_eq!(image_b, ["q_g1", "q_g3", "q_g2", "q_G31", "q_g12"]);
    assert!(image_a.iter().all(|name| *name != "q_G12"));
    assert!(image_b.iter().all(|name| *name != "q_G12"));

    println!("OCCURRENCE REFLECTION RESIDUE-SECTOR CERTIFICATE: PASS");
    println!("sigma23(q_G12)=q_G31");
    println!("image_summand_g23={}", image_a.join(","));
    println!("image_summand_g31={}", image_b.join(","));
    println!("same_q_G12_chart_intertwiner_typed=false");
}
