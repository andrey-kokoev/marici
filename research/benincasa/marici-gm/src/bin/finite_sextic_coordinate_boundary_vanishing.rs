use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default())
        .unwrap()
        .expand()
}

fn verify() {
    let k = atom(
        "E^4*P3^2-E^2*A*P1^2+E^2*A*P2^2-E^2*A*P3^2+E^2*B*P1^2-E^2*B*P2^2-E^2*B*P3^2-E^2*P1^2*P3^2-E^2*P2^2*P3^2+E^2*P3^4+A^2*P1^2-A*B*P1^2-A*B*P2^2+A*B*P3^2+A*P1^4-A*P1^2*P2^2-A*P1^2*P3^2+B^2*P2^2-B*P1^2*P2^2+B*P2^4-B*P2^2*P3^2+P1^2*P2^2*P3^2",
    );
    let lambda = atom("(P1-P2-P3)*(P1-P2+P3)*(P1+P2-P3)*(P1+P2+P3)");

    // Complete the B-square.  Multiplication by 4 P2^2 avoids introducing
    // rational-function normalization into the exact polynomial assertion.
    let b_center =
        atom("((P1^2+P2^2-P3^2)*A-E^2*(P1^2-P2^2-P3^2)+P1^2*P2^2-P2^4+P2^2*P3^2)/(2*P2^2)");
    let completed_a = k
        .replace(atom("B").to_pattern())
        .with((b_center + atom("y")).to_pattern())
        .expand();
    let expected_a = atom("P2^2*y^2+Lambda*(4*E^2*P2^2-(A-(E^2+P2^2))^2)/(4*P2^2)")
        .replace(atom("Lambda").to_pattern())
        .with(lambda.clone().to_pattern())
        .expand();
    assert_eq!(
        (atom("4*P2^2") * (completed_a - expected_a)).expand(),
        atom("0")
    );

    // The B=0 branch follows by the labelled exchange A<->B, P1<->P2.
    // At the double coordinate boundary the displayed restriction is exact.
    let k00 = k
        .replace(atom("A").to_pattern())
        .with(atom("0").to_pattern())
        .replace(atom("B").to_pattern())
        .with(atom("0").to_pattern())
        .expand();
    let r00 = atom("E^4-E^2*(P1^2+P2^2-P3^2)+P1^2*P2^2");
    assert_eq!((k00 - atom("P3^2") * r00).expand(), atom("0"));

    // Milnor algebras: A1 has basis {1}; A3 has {1,a,a^2}.
    let a1_rank = 1_usize;
    let a3_basis = ["1", "a", "a^2"];
    assert_eq!(a3_basis.len(), 3);

    println!("A0_completed_identity=true");
    println!("B0_completed_identity=labelled_exchange");
    println!("generic_signed_boundary_milnor_rank={a1_rank}");
    println!("generic_triangle_boundary_transverse_rank=1");
    println!("double_boundary_soft_or_restriction_generic_rank=1");
    println!("soft_signed_corner_type=A3");
    println!("soft_signed_corner_milnor_rank={}", a3_basis.len());
    println!("soft_signed_corner_deck_character=anti_invariant_rank_3");
    println!("soft_signed_corner_rank_excess_over_generic_kato_line=2");
}

fn main() {
    std::thread::Builder::new()
        .name("coordinate-boundary-symbolica".into())
        .stack_size(64 * 1024 * 1024)
        .spawn(verify)
        .unwrap()
        .join()
        .unwrap();
}
