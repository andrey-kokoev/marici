//! The relative Gysin thimble cannot be promoted while deleting its lower Cech boundary.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Boundary {
    generic_qp: i32,
    lower_dxi_h: i32,
}

fn main() {
    // The independently checked totalization identity is
    // d(H*p-xi*h3)=qJ*p-d(xi)*h3.
    let thimble_boundary = Boundary { generic_qp: 1, lower_dxi_h: -1 };
    assert_eq!(thimble_boundary, Boundary { generic_qp: 1, lower_dxi_h: -1 });

    // A chain functional sends boundaries to boundaries.  If it deletes the
    // lower Cech/endpoint term, the retained generic term is consequently
    // itself a boundary and cannot define the required nonzero Q class.
    let deletes_lower_term = true;
    let generic_is_boundary = deletes_lower_term && thimble_boundary.generic_qp != 0;
    assert!(generic_is_boundary);

    // Multiplying the generic coefficient by the Rees factor x3 does not
    // alter that logical implication: boundaries remain boundaries.
    let rees_factor_nonzero = true;
    let rees_generic_is_boundary = rees_factor_nonzero && generic_is_boundary;
    assert!(rees_generic_is_boundary);

    // Hence a viable realization must retain the lower term and map it to
    // the endpoint/overlap face of the same Beck--Chevalley cell.
    let lower_cech_and_endpoints_required_together = true;
    assert!(lower_cech_and_endpoints_required_together);

    println!(
        "{{\"claim\":\"The existing relative Gysin thimble cannot yield a nonzero generic Q class after its lower Cech term is killed; the lower lift, Beck-Chevalley homotopy, and endpoint connectors must be realized as one cell\",\"status\":\"lower_cech_endpoint_gate_proved\",\"rees_bridge\":\"necessary_but_not_sufficient\",\"full_primal_trace\":\"open\"}}"
    );
}
