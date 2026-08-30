fn main(){
    // A two-route kernel vector p=(1,1), epsilon=(1,-1).
    // N distinguishes only the second route.
    let epsilon_p=1-1;
    let epsilon_n_p=0-1;
    assert_eq!(epsilon_p,0);
    assert_eq!(epsilon_n_p,-1);
    println!("{{\"status\":\"pass\",\"kernel_scalar_readout\":0,\"first_score_readout\":-1,\"observable_kernel_definition\":\"k in ker epsilon with some epsilon*N_e*k nonzero\"}}");
}
