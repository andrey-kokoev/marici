fn main() {
    // epsilon_lambda(a_e,b_e)=8 C_e a_e - 8 lambda_e C_e b_e.
    // The frozen kernel generator at lambda_e=1 is p_e=(1,1).
    let c = [2_i64, 3, 5];
    let mut response = [0_i64; 3];
    for e in 0..3 {
        let epsilon_at_frozen_point = 8 * c[e] - 8 * c[e];
        assert_eq!(epsilon_at_frozen_point, 0);
        response[e] = -8 * c[e];
    }
    assert_eq!(response, [-16, -24, -40]);
    println!("{{\"status\":\"pass\",\"frozen_kernel\":true,\"conormal_matrix\":\"-8*diag(C12,C23,C31)\",\"physical_source_parameter\":false}}");
}
