fn popcount(mut x:usize)->usize{let mut n=0;while x>0{n+=x&1;x>>=1;}n}
fn main(){
    let mu:Vec<i64>=(0..8).map(|s|(-2_i64).pow(popcount(s) as u32)).collect();
    for cell in 0..8 {
        let cumulative:i64=(0..8).filter(|s|s & !cell==0).map(|s|mu[s]).sum();
        assert_eq!(cumulative,if popcount(cell)%2==0{1}else{-1});
    }
    // Boolean zeta matrix is unit triangular in cardinality-refining order,
    // hence this preimage is unique over Z.
    println!("{{\"status\":\"pass\",\"zeta_transform\":\"(-2)^|S| -> (-1)^|T|\",\"mobius_preimage_unique\":true,\"native_character\":\"cell_orientation_parity\"}}");
}
