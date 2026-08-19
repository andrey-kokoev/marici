use serde_json::json;

fn main() {
    // Each pair is (boundary monodromy square-root monomial, valuation in the
    // source Fitting minor).  Z is a declared Laurent unit, so
    // A3^2-Z^2 = Z^2*((A3/Z)^2-1), and similarly for A3*B34.
    let factors = [
        ("A2",2), ("A3",2), ("A2*B24",1), ("A3*B34",1),
        ("Z*A2",1), ("Z*A2*B24",2), ("A3/Z",1), ("A3*B34/Z",2),
    ];
    let packet_factors: Vec<_> = factors.iter().map(|(m,v)| json!({
        "monodromy_square_root":m,
        "twisted_boundary_factor":format!("({m})^2-1"),
        "fitting_valuation":v,
        "existing_incidence_wall":true
    })).collect();
    assert_eq!(factors.iter().map(|(_,v)|v).sum::<i32>(),12);

    // Rank-one local model: boundary of a loaded endpoint generator is
    // (M-1)e.  A closed regularization requires (M-1)^{-1}; without this
    // localization the chamber-chain lattice need not equal twisted homology.
    let packet=json!({
        "schema":"marici.benincasa.string_six_point_twisted_boundary_support.v1",
        "local_boundary_equation":"partial(gamma)=(M-1)e",
        "closure_coefficient":"1/(M-1)",
        "coordinate_convention":"M=A^2 because A=exp(i*pi*s)",
        "fitting_factors":packet_factors,
        "total_fitting_zero_valuation":12,
        "all_fitting_zeros_are_twisted_boundary_resonances":true,
        "new_carrier_divisor_required":false,
        "unlocalized_chamber_lattice_equals_betti_lattice":false,
        "localized_comparison_candidate":true
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-twisted-boundary-support.json",&text).unwrap(); print!("{text}");
}
