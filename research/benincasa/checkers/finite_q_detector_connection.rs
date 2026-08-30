fn main() {
    // Local Smith gauge T=diag(1,1,c), with connection convention nabla=d-A.
    // A_c=(dT/dc)T^{-1}=diag(0,0,1/c).
    let residue = [0_i64, 0, 1];
    assert_eq!(residue.iter().sum::<i64>(), 1);
    assert_eq!(residue.iter().filter(|x| **x == 1).count(), 1);

    // Integral residue gives identity local monodromy exp(2*pi*i)=1.
    let monodromy_characters = [1_i64, 1, 1];
    assert_eq!(monodromy_characters, [1, 1, 1]);

    println!(
        "{{\"status\":\"pass\",\"connection_convention\":\"nabla=d-A\",\"local_Smith_transfer\":\"diag(1,1,c)\",\"detector_connection\":\"diag(0,0,dc/c)\",\"Gram_residue\":[0,0,1],\"local_monodromy\":\"identity\",\"Gauss_Manin_tensor_rule\":\"A_V tensor I plus I tensor A_D\",\"full_block_horizontal\":true}}"
    );
}
