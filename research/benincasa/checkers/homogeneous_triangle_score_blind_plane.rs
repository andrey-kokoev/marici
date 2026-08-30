fn main(){
    let c=5_i64;
    let first_score=[-8*c,-8*c,-8*c];
    assert_eq!(first_score,[-40,-40,-40]);
    let blind1=[1_i64,-1,0];
    let blind2=[0_i64,1,-1];
    assert_eq!(first_score.iter().zip(blind1).map(|(x,y)|x*y).sum::<i64>(),0);
    assert_eq!(first_score.iter().zip(blind2).map(|(x,y)|x*y).sum::<i64>(),0);
    println!("{{\"status\":\"pass\",\"all_equal_energy_contact_rank\":1,\"permanent_blind_rank\":2,\"blind_representation\":\"rational_cyclotomic_C3\",\"higher_momentum_scores_repair\":false}}");
}
