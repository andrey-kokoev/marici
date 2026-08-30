fn main(){
    // Direct expansion of exp(-i H + i S0), after the common +p conversion:
    // bulk = J1, one-boundary mixed = -2 J2, two-boundary = -J0.
    // Eq. (19) prints J1 - 4 J2 - 2 J0 before the c3 term.
    let w_from_mixed=4.0/2.0;
    let w2_from_boundary=2.0;
    let multiplicative_square=w_from_mixed*w_from_mixed;
    assert_eq!(w_from_mixed,2.0);
    assert_eq!(multiplicative_square,4.0);
    assert_eq!(w2_from_boundary,2.0);
    assert_ne!(multiplicative_square,w2_from_boundary);
    println!("{{");
    println!("  \"schema\": \"marici.finite_time_endpoint_multiplicativity_obstruction.v1\",");
    println!("  \"direct_oscillatory_basis\": [\"J1\", \"-2J2\", \"-J0\"],");
    println!("  \"published_oscillatory_basis\": [\"J1\", \"-4J2\", \"-2J0\"],");
    println!("  \"weight_required_by_mixed\": 2,");
    println!("  \"weight_square_required_by_boundary_boundary\": 2,");
    println!("  \"actual_square_of_mixed_weight\": 4,");
    println!("  \"multiplicative_endpoint_weight_exists\": false");
    println!("}}");
}
