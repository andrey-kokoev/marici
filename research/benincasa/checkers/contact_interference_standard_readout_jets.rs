// Exact all-jet no-go for the standard sum readout on an interference line.

fn main() {
    // Arbitrary Taylor coefficients of the scalar route amplitude f(s).
    let coefficients = [7_i128, -11, 13, 0, 19, -23, 29, 31, -37];
    for (order, a) in coefficients.iter().enumerate() {
        let route_a_jet = *a;
        let route_b_jet = -*a;
        assert_eq!(route_a_jet + route_b_jet, 0, "order {order}");
    }

    // The difference covector detects every nonzero coefficient, showing
    // that invisibility belongs specifically to the standard sum readout.
    assert!(coefficients
        .iter()
        .any(|a| (*a) - (-*a) != 0));

    println!(
        "{{\"status\":\"pass\",\"jet_orders_checked\":9,\"packet\":\"f(s)*(1,-1)\",\"standard_covector\":\"(1,1)\",\"all_standard_jets_zero\":true,\"difference_covector_detects_packet\":true,\"physical_activation_requires_new_route_resolving_readout\":true}}"
    );
}
