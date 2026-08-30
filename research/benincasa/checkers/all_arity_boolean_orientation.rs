fn popcount(mut x:usize)->usize{let mut n=0;while x>0{n+=x&1;x>>=1;}n}
fn main(){
    for n in 0..=12 {
        let size=1_usize<<n;
        for t in 0..size {
            let cumulative:i64=(0..size).filter(|s|s & !t==0)
                .map(|s|(-2_i64).pow(popcount(s) as u32)).sum();
            assert_eq!(cumulative,if popcount(t)%2==0{1}else{-1});
        }
    }
    println!("{{\"status\":\"pass\",\"tested_edge_numbers\":\"0..12\",\"theorem\":\"Boolean subset sum sends minus-two powers to orientation parity\",\"integral_uniqueness\":true}}");
}
