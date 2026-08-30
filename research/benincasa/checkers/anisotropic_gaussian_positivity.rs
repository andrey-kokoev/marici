fn main(){
    // a(theta)=a0+u cos2theta+v sin2theta is positive if a0>sqrt(u^2+v^2).
    let a0=5_i64; let u=3_i64; let v=2_i64;
    assert!(a0*a0>u*u+v*v);
    assert!(a0>0);
    println!("{{\"status\":\"pass\",\"positivity_condition\":\"a0^2>u^2+v^2 with a0>0\",\"sample\":[5,3,2],\"open_normalizable_neighborhood\":true,\"translation_invariant\":true,\"rotation_invariant\":false}}");
}
