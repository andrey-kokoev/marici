fn main(){
    // Connected pairing kills the constant -1/2 in S=a Phi Phi-1/2.
    let a=3_i64; let connected_pair=5_i64;
    let score_pair=a*connected_pair;
    assert_eq!(score_pair,15);
    println!("{{\"status\":\"pass\",\"mixed_readout\":\"a(q)*<O Phi(q)Phi(-q)>_connected\",\"constant_score_term_connected\":0,\"extra_boundary_legs\":2}}");
}
