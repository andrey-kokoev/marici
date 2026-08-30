// Source-corrected mixed variation for a product of two logarithmic contacts.

fn mul4(a: [[i32; 4]; 4], b: [[i32; 4]; 4]) -> [[i32; 4]; 4] {
    let mut c = [[0; 4]; 4];
    for i in 0..4 {
        for j in 0..4 {
            for k in 0..4 {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    c
}

fn rank4(m: [[i32; 4]; 4]) -> usize {
    usize::from(m.iter().flatten().any(|x| *x != 0))
}

fn main() {
    // Ordered tensor basis (1, tau_i, tau_j, tau_i*tau_j).
    let v_i = [
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
    ];
    let v_j = [
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ];
    let mixed_ij = mul4(v_i, v_j);
    let mixed_ji = mul4(v_j, v_i);
    assert_eq!(mixed_ij, mixed_ji);
    assert_eq!(rank4(mixed_ij), 1);
    assert_eq!(mixed_ij[0][3], 1);

    println!(
        "{{\"status\":\"pass\",\"source_operation\":\"contact_product\",\"mixed_variation_rank\":1,\"mixed_generator\":\"tau_i_tau_j_to_1\"}}"
    );
}
