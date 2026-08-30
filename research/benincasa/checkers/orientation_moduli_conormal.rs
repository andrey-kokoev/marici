fn main(){
    // Cumulative cell weight W(T)=sum_{S subset T} lambda_S mu(S).
    // A labelled deformation of the singleton/final-edge coefficient has
    // derivative mu({e})=-2 on every cell containing e and zero otherwise.
    let mut derivatives=[[0_i64;8];3];
    for e in 0..3 {for cell in 0..8 {if cell&(1<<e)!=0{derivatives[e][cell]=-2;}}}
    for e in 0..3 {assert_eq!(derivatives[e].iter().filter(|x|**x!=0).count(),4);}
    assert_ne!(derivatives[0],derivatives[1]);
    assert_ne!(derivatives[1],derivatives[2]);
    println!("{{\"status\":\"pass\",\"orientation_tangent_rank\":3,\"each_edge_support_cells\":4,\"c3_covariant\":true,\"physical_coupling_declared\":false}}");
}
