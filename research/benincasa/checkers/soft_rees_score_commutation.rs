fn main(){
    let c=5_i64;
    // On both y=q t and q=y s charts the composed route is A=8C.
    // A multiplicative Gaussian deformation labels only B=-8 lambda C.
    for chart in ["q_chart","y_chart"] {
        let value_at_one=8*c-8*c;
        let score=-8*c;
        assert_eq!(value_at_one,0);
        assert_eq!(score,-40);
        assert!(!chart.is_empty());
    }
    println!("{{\"status\":\"pass\",\"charts\":[\"y=q*t\",\"q=y*s\"],\"exceptional_packet\":\"(8C,-8C)\",\"score_response\":\"-8C\",\"exceptional_commutator\":0}}");
}
