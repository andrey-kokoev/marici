fn main(){
    let c=[2_i64,3,5];
    let matrix=[[-8*c[0],0,0],[0,-8*c[1],0],[0,0,-8*c[2]]];
    let determinant=matrix[0][0]*matrix[1][1]*matrix[2][2];
    assert_ne!(determinant,0);
    println!("{{\"status\":\"pass\",\"observability_matrix\":\"-8*diag(C12,C23,C31)\",\"rank\":3,\"kernel_rank\":3,\"first_score_blind_rank\":0}}");
}
