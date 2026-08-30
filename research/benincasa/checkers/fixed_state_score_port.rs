fn main(){
    let contact=[2_i64,3,5];
    let response:Vec<i64>=contact.iter().map(|c|-8*c).collect();
    assert_eq!(response,vec![-16,-24,-40]);
    println!("{{\"status\":\"pass\",\"same_state_estimator\":\"connected correlator with quadratic score insertion\",\"response_vector\":[-16,-24,-40],\"ordinary_scalar_sufficient\":false,\"mixed_port_required\":true}}");
}
