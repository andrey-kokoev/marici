use std::collections::BTreeSet;

fn set(xs: &[&'static str]) -> BTreeSet<&'static str> {
    xs.iter().copied().collect()
}

fn main() {
    // Pullbacks to C_12,23 at generic kinematics. Constant nonzero source
    // forms do not define fiber divisors and are omitted from these sets.
    let shared = set(&["b=y+z (q_g1)", "b=x+y (q_g3)"]);
    let mut d12 = shared.clone();
    d12.insert("b=x (q_g23)");
    let mut d23 = shared.clone();
    d23.insert("b=z (q_g12)");

    let only_12: Vec<_> = d12.difference(&d23).copied().collect();
    let only_23: Vec<_> = d23.difference(&d12).copied().collect();
    assert_eq!(only_12, vec!["b=x (q_g23)"]);
    assert_eq!(only_23, vec!["b=z (q_g12)"]);
    assert_ne!(d12, d23);

    // The common restriction domain removes the union. In U12 the point
    // b=z remains an interior point of the ambient surface but is deleted
    // from the curve, so C_common -> U12 is not closed/proper. Cyclically,
    // b=x gives the obstruction in U23.
    let union: BTreeSet<_> = d12.union(&d23).copied().collect();
    assert!(union.contains("b=z (q_g12)") && !d12.contains("b=z (q_g12)"));
    assert!(union.contains("b=x (q_g23)") && !d23.contains("b=x (q_g23)"));

    println!("{{");
    println!("  \"common_curve\": \"C_12,23: c=a=-E, w^2=K_12,23(b)\",");
    println!("  \"pullback_D12\": [\"b=y+z\", \"b=x+y\", \"b=x\"],");
    println!("  \"pullback_D23\": [\"b=y+z\", \"b=x+y\", \"b=z\"],");
    println!("  \"generic_mismatch\": [\"b=x only in D12\", \"b=z only in D23\"],");
    println!("  \"common_restriction_open\": \"C minus (D12 union D23)\",");
    println!("  \"closed_in_U12\": false,");
    println!("  \"closed_in_U23\": false,");
    println!("  \"proper_gysin_span\": false,");
    println!("  \"locally_closed_in_both\": true,");
    println!("  \"six_functor_bang_span\": \"canonically typed\",");
    println!("  \"proper_gysin_repair\": \"would add the opposite lower occurrence to each sector boundary\",");
    println!("  \"proper_gysin_repair_authorized\": false,");
    println!("  \"classification\": \"existing carrier plus source-boundary common refinement; ordinary Gysin fails but support-sensitive bang correspondence survives\"");
    println!("}}");
}
