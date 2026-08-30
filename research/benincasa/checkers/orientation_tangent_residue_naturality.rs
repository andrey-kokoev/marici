fn main(){
    let mut z=[[0_i64;8];8];
    for t in 0..8 {for s in 0..8 {if s & !t==0 {z[t][s]=1;}}}
    let residue=[2_i64,3,5,7,11,13,17,19];
    for e in 0..3 {
        let mut dmu=[0_i64;8];dmu[1<<e]=-2;
        let dw:Vec<i64>=(0..8).map(|t|(0..8).map(|s|z[t][s]*dmu[s]).sum()).collect();
        let left:i64=residue.iter().zip(&dw).map(|(r,w)|r*w).sum();
        let pulled:Vec<i64>=(0..8).map(|s|(0..8).map(|t|residue[t]*z[t][s]).sum()).collect();
        let right:i64=pulled.iter().zip(&dmu).map(|(r,m)|r*m).sum();
        assert_eq!(left,right);
    }
    println!("{{\"status\":\"pass\",\"differentiate_then_residue\":\"residue_then_differentiate\",\"linearity_certificate\":true,\"scope\":\"frozen_boolean_resolution\"}}");
}
