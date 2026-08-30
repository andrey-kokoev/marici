fn main() {
    let edges = [2_i64, 3_i64, 5_i64];
    for et in [1_i64, 7, 19] {
        for mask in 0_u8..8 {
            let mut shifted = et;
            for (i, y) in edges.iter().enumerate() {
                if mask & (1 << i) != 0 { shifted += 2*y; }
            }
            assert!(shifted >= et && shifted > 0);
        }
    }
    println!("{{\"status\":\"pass\",\"sectors\":8,\"claim\":\"E_T^(S)>=E_T>0\"}}");
}
