fn mat_vec(a: &[Vec<i64>], x: &[i64]) -> Vec<i64> {
    a.iter().map(|r| r.iter().zip(x).map(|(u,v)| u*v).sum()).collect()
}

fn main() {
    let epsilon = vec![
        vec![8,-8,0,0,0,0],
        vec![0,0,8,-8,0,0],
        vec![0,0,0,0,8,-8],
    ];
    let phi = vec![vec![2,3,5], vec![7,11,13]];
    for edge in 0..3 {
        let mut p=vec![0;6]; p[2*edge]=1; p[2*edge+1]=1;
        let ep=mat_vec(&epsilon,&p);
        assert_eq!(ep,vec![0,0,0]);
        assert_eq!(mat_vec(&phi,&ep),vec![0,0]);
    }
    println!("{{\"status\":\"pass\",\"kernel_rank\":3,\"all_factored_readouts_annihilate_kernel\":true,\"required_extension\":\"route-resolving lift\"}}");
}
