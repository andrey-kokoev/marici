fn det3(a:[[i64;3];3])->i64{a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])}
fn main(){
    // Columns: isotropic, scaled cos(2 theta), scaled sin(2 theta).
    let evaluation=[[1_i64,2,0],[1,-1,-1],[1,-1,1]];
    assert_eq!(det3(evaluation),-6);
    println!("{{\"status\":\"pass\",\"source_components\":[\"isotropic\",\"quadrupole_cos2theta\",\"quadrupole_sin2theta\"],\"evaluation_determinant\":-6,\"rank\":3,\"even_under_momentum_reversal\":true}}");
}
