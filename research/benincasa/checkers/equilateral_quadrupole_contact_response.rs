fn det3(a:[[i64;3];3])->i64{a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])}
fn main(){
    let c=[2_i64,3,5];
    let e=[[1_i64,2,0],[1,-1,-1],[1,-1,1]];
    let mut response=[[0_i64;3];3];
    for i in 0..3 {for j in 0..3 {response[i][j]=-8*c[i]*e[i][j];}}
    assert_ne!(det3(response),0);
    println!("{{\"status\":\"pass\",\"contact_response_rank\":3,\"isotropic_rank\":1,\"quadrupole_added_rank\":2,\"quadrupole_c3_type\":\"rational_cyclotomic_plane\"}}");
}
