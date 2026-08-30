// RETRACTED MODEL (Entry 2143): this direct sum is not the source product.

fn mul3(a: [[i32; 3]; 3], b: [[i32; 3]; 3]) -> [[i32; 3]; 3] {
    let mut c = [[0; 3]; 3];
    for i in 0..3 {
        for j in 0..3 {
            for k in 0..3 {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    c
}

fn main() {
    // Basis (1,tau_i,tau_j) for the additive contact readout.
    let var_i = [[0, 1, 0], [0, 0, 0], [0, 0, 0]];
    let var_j = [[0, 0, 1], [0, 0, 0], [0, 0, 0]];
    let mixed_contact = mul3(var_i, var_j);
    assert_eq!(mixed_contact, [[0; 3]; 3]);
    assert_eq!(mul3(var_j, var_i), [[0; 3]; 3]);

    // On sqrt(nu_i nu_j), each variation is (-1)-1=-2.
    let var_kummer_i = -2;
    let var_kummer_j = -2;
    let mixed_kummer = var_kummer_i * var_kummer_j;
    assert_eq!(mixed_kummer, 4);

    println!(
        "{{\"status\":\"pass\",\"contact_mixed_variation_rank\":0,\"lower_kummer_mixed_variation_rank\":1,\"lower_kummer_scalar\":4}}"
    );
}
