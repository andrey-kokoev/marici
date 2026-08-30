fn det3(y:[i64;3])->i64{(y[1]-y[0])*(y[2]-y[0])*(y[2]-y[1])}
fn main(){
    assert_ne!(det3([2,3,5]),0);
    assert_eq!(det3([2,2,5]),0);
    assert_eq!(det3([2,2,2]),0);
    println!("{{\"status\":\"pass\",\"evaluation_basis\":[\"1\",\"y\",\"y^2\"],\"determinant\":\"(y23-y12)(y31-y12)(y31-y23)\",\"generic_rank\":3,\"two_equal_rank\":2,\"all_equal_rank\":1}}");
}
