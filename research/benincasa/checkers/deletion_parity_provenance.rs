fn popcount(mut x:usize)->usize{let mut n=0;while x>0{n+=x&1;x>>=1;}n}
fn main(){
    let graph_expansion=[1_i64;8];
    let subdivision=core::array::from_fn::<i64,8,_>(|s|(-2_i64).pow(popcount(s) as u32));
    assert!(graph_expansion.iter().all(|x|*x==1));
    assert_eq!(subdivision,[1,-2,-2,4,-2,4,4,-8]);
    assert_ne!(graph_expansion,subdivision);
    println!("{{\"status\":\"pass\",\"erased_graph_coefficients\":\"all_+1\",\"subdivision_coefficients\":\"(-2)^cardinality\",\"parity_is_keldysh_outcome\":false}}");
}
