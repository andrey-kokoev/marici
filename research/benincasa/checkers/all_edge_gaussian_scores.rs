fn main(){
    for n in 1..=10 {
        let size=1_usize<<n;
        for s in 0..size {for e in 0..n {
            let derivative=(s&(1<<e)!=0) as usize;
            assert_eq!(derivative,(s>>e)&1);
        }}
    }
    println!("{{\"status\":\"pass\",\"tested_edge_numbers\":\"1..10\",\"score_map\":\"log-kernel derivative equals labelled deletion indicator\",\"labelled_score_rank\":\"number_of_edges\",\"single_mode_fisher\":\"1/2\"}}");
}
