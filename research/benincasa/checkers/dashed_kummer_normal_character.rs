// Character bookkeeping for the dashed-edge factor y^{-1} along nu=0.

fn main() {
    let y_residue: i32 = -1;
    let y_winding_along_nu_loop: i32 = 0;
    let exponent_along_nu = y_residue * y_winding_along_nu_loop;

    // Integral exponent gives trivial character even around y=0; with y fixed
    // along the nu-loop the exponent is identically zero.
    assert_eq!(exponent_along_nu, 0);
    let dashed_character_along_nu = 1;
    let required_character_along_nu = -1;
    assert_ne!(dashed_character_along_nu, required_character_along_nu);

    println!(
        "{{\"status\":\"pass\",\"dashed_residue\":-1,\"nu_loop_y_winding\":0,\"dashed_nu_character\":1,\"required_nu_character\":-1,\"twist_supplied\":false}}"
    );
}
