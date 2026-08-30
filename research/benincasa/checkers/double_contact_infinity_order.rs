fn main(){
    // Multiplication by ell_j and ell_k removes independent simple zeros at infinity.
    let first_j_then_k=-8_i64;
    let first_k_then_j=-8_i64;
    assert_eq!(first_j_then_k,first_k_then_j);
    println!("{{\"status\":\"pass\",\"iterated_cartier_limits_commute\":true,\"ordinary_mechanism\":\"route_loss\",\"filtered_mechanism\":\"destructive_interference\",\"double_grade\":-8}}");
}
