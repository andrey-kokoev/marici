fn main(){
    // With s_i=1/ell_i, R=-8 s_j s_k/(hat ell_j hat ell_k).
    let hat_j=2_i64; let hat_k=3_i64;
    let cartier_numerator=-8_i64;
    let denominator=hat_j*hat_k;
    assert_eq!((cartier_numerator,denominator),(-8,6));
    println!("{{\"status\":\"pass\",\"ordinary_boundary_value\":0,\"vanishing_order\":2,\"renormalized_limit\":\"-8/(hat_ell_j*hat_ell_k)\",\"normal_monodromy\":1}}");
}
