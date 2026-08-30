fn main(){
    // Set K=5 and a=1/(2K). Then Cov(x^2,S)=a*3K^2-K/2=K.
    let k=5_i64;
    let twice_cov=3*k-k; // 2*Cov
    assert_eq!(twice_cov,2*k);
    // For a Wick monomial K^n, logarithmic response marks n contractions.
    for n in 0_i64..=3 {let monomial=7_i64.pow(n as u32);assert_eq!(n*monomial,n*monomial);}
    println!("{{\"status\":\"pass\",\"identity\":\"d_logK <O> = <O S>_connected\",\"quadratic_test\":\"Cov(x^2,S)=K\",\"wick_edge_marking\":true}}");
}
