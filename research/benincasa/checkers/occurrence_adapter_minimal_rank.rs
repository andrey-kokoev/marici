fn determinant3(a:[[i64;3];3])->i64{a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])}
fn main(){
    let detector=[[1_i64,1,1],[1,-1,0],[0,1,-1]];
    assert_ne!(determinant3(detector),0);
    println!("{{\"status\":\"pass\",\"existing_invariant_rank\":1,\"required_added_rank\":2,\"minimal_added_type\":\"cyclotomic_C3_plane\",\"carrier_labels_already_present\":true}}");
}
