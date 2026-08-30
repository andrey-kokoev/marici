fn popcount(mut x:usize)->usize{let mut n=0;while x>0{n+=x&1;x>>=1;}n}
fn main(){
    let mut variation=0_i64; let mut positive=0_i64; let mut negative=0_i64;
    for s in 0..8 {let k=popcount(s);let abs=1_i64<<k;let sign=if k%2==0{1}else{-1};
        variation+=abs;if sign>0{positive+=abs}else{negative+=abs};
        assert_eq!(sign*abs,(-2_i64).pow(k as u32));
    }
    assert_eq!((positive,negative,variation),(13,14,27));
    println!("{{\"status\":\"pass\",\"jordan_positive_mass\":13,\"jordan_negative_mass\":14,\"total_variation\":27,\"sampling_law\":\"product_Bernoulli_2_over_3\",\"readout\":\"27*parity\"}}");
}
