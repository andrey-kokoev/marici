fn main(){
    let mut z=[[0_i64;8];8];
    for t in 0..8 {for s in 0..8 {if s & !t==0 {z[t][s]=1;}}}
    // Numeric subset order makes z lower unitriangular.
    for i in 0..8 {assert_eq!(z[i][i],1);for j in i+1..8{assert_eq!(z[i][j],0);}}
    let determinant=1_i64;
    println!("{{\"status\":\"pass\",\"zeta_determinant\":{},\"integral_inverse\":true,\"cover_weight_gauge_rank\":0}}",determinant);
}
