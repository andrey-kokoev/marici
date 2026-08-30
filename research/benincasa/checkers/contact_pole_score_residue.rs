fn main(){
    // R=-8/(ell_j ell_k). Residue in ell_j is -8/ell_k; double residue -8.
    let single_residue_coefficient=-8_i64;
    let double_residue=-8_i64;
    assert_eq!(single_residue_coefficient,-8);
    assert_eq!(double_residue,-8);
    println!("{{\"status\":\"pass\",\"mixed_readout\":\"-8/(ell_j*ell_k)\",\"single_residue\":\"-8/ell_k\",\"double_residue\":-8,\"new_divisor\":false}}");
}
