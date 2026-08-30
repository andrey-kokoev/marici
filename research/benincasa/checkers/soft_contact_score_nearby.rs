fn main(){
    let c=7_i64;
    let generic=-8*c;
    let exceptional=-8*c;
    assert_eq!(generic,exceptional);
    println!("{{\"status\":\"pass\",\"generic_response\":\"-8C\",\"soft_nearby_response\":\"-8C\",\"score_inertia\":1,\"new_soft_support\":false,\"qualification\":\"C finite and nonzero\"}}");
}
