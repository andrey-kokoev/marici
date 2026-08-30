fn main(){
    let block_sizes=[2_usize,1,3];
    let labelled_dimension=1_usize<<block_sizes.iter().sum::<usize>();
    let quotient_dimension=block_sizes.iter().map(|m|m+1).product::<usize>();
    assert_eq!(labelled_dimension,64);
    assert_eq!(quotient_dimension,24);
    println!("{{\"status\":\"pass\",\"block_sizes\":[2,1,3],\"labelled_route_dimension\":64,\"momentum_score_quotient_dimension\":24,\"dimension_formula\":\"product over energy blocks of (multiplicity+1)\"}}");
}
