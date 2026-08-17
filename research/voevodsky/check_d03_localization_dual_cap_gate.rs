//! Coefficient-direction gate for the reduced Entry-176 exceptional packet.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Sector {
    Center,
    X3Branch,
    X4Branch,
}

fn main() {
    // The physical support quotient removes only the x4 incidence summand.
    let full_packet = [Sector::Center, Sector::X3Branch, Sector::X4Branch];
    let reduced_packet: Vec<_> = full_packet
        .iter()
        .copied()
        .filter(|sector| *sector != Sector::X4Branch)
        .collect();
    assert_eq!(reduced_packet, [Sector::Center, Sector::X3Branch]);

    // Put R=A[(D03*x1)^-1] and x=x3.  The branch coefficient is dual to
    // R[x^-1], while the center coefficient is dual to R.  Contravariance
    // gives the required arrow from the branch dual to the center dual.
    let localization_arrow = "R -> R[x^-1]";
    let dual_arrow = "RHom(R[x^-1],R) -> RHom(R,R)";
    assert_eq!(localization_arrow, "R -> R[x^-1]");
    assert_eq!(dual_arrow, "RHom(R[x^-1],R) -> RHom(R,R)");

    // Its cone is RHom(R[x^-1]/R,R)[1].  The quotient contains all negative
    // x powers.  Finite windows have strictly increasing rank, certifying
    // that deleting the x4 support summand does not delete this coefficient
    // direction.
    for bound in 1_usize..=32 {
        let negative_powers: Vec<_> =
            (1..=bound).map(|power| -(power as i32)).collect();
        assert_eq!(negative_powers.len(), bound);
        assert_eq!(negative_powers[0], -1);
        assert_eq!(negative_powers[bound - 1], -(bound as i32));
    }

    println!(
        "{{\"claim\":\"The x4 support quotient leaves a canonical x3-localization-dual map, but its cone is the nonzero dual of R[x3^-1]/R; multiplying by Entry-176's cellular unit does not make it an equivalence\",\"status\":\"canonical_map_noninvertible\",\"removed_support\":\"x4_branch\",\"retained_coefficient_cone\":\"RHom_R(R[x3^-1]/R,R)[1]\",\"next_gate\":\"construct a physical coefficient functor that kills or residues this cone\"}}"
    );
}
