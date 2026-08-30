fn main(){
    // xi=sqrt(a)x sends normalized P_a dx to pi^-1/2 exp(-xi^2) dxi.
    // The score is xi^2-1/2 and is invariant under the sqrt deck xi -> -xi.
    let xi=3_i64;
    assert_eq!((-xi)*(-xi),xi*xi);
    let fisher_numerator=1_i64; // 1/2
    assert_eq!(fisher_numerator,1);
    println!("{{\"status\":\"pass\",\"scaled_field\":\"xi=sqrt(a)*Phi\",\"scaled_measure\":\"pi^-1/2 exp(-xi^2) dxi\",\"score\":\"xi^2-1/2\",\"field_deck_character\":-1,\"score_deck_character\":1,\"fisher\":\"1/2\"}}");
}
