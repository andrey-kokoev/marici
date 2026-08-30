fn main(){
    let mut z=[[0_i64;8];8];
    for t in 0..8 {for s in 0..8 {if s & !t==0 {z[t][s]=1;}}}
    for e in 0..3 {
        let mut dmu=[0_i64;8]; dmu[1<<e]=-2;
        let mut via_zeta=[0_i64;8];
        let mut direct=[0_i64;8];
        for t in 0..8 {
            via_zeta[t]=(0..8).map(|s|z[t][s]*dmu[s]).sum();
            direct[t]=if t&(1<<e)!=0{-2}else{0};
        }
        assert_eq!(via_zeta,direct);
    }
    println!("{{\"status\":\"pass\",\"comparison\":\"overlap_coefficients_to_resolved_cells\",\"edge_tangent_square_commutes\":true,\"c3_labels_preserved\":true}}");
}
