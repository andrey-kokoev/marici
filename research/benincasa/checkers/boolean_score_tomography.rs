fn popcount(mut x:usize)->usize{let mut n=0;while x>0{n+=x&1;x>>=1;}n}
fn main(){
    for n in 0..=10 {
        let size=1_usize<<n;
        let v:Vec<i64>=(0..size).map(|s|3*s as i64-7).collect();
        let moments:Vec<i64>=(0..size).map(|t|(0..size).filter(|s|s&t==t).map(|s|v[s]).sum()).collect();
        let recovered:Vec<i64>=(0..size).map(|s|(0..size).filter(|t|t&s==s)
            .map(|t|if popcount(t^s)%2==0{moments[t]}else{-moments[t]}).sum()).collect();
        assert_eq!(recovered,v);
    }
    println!("{{\"status\":\"pass\",\"tested_edge_numbers\":\"0..10\",\"moment_map\":\"M_T=sum over S containing T of v_S\",\"mobius_reconstruction\":true,\"maximum_score_order\":\"number_of_edges\"}}");
}
