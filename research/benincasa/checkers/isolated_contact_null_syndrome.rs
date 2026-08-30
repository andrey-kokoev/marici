// Exact hostile test for a kinematics-independent isolated-contact circuit.

fn matrix_times(s: [i128; 3], c: [i128; 3], v: [i128; 4]) -> [i128; 3] {
    [
        4 * s[0] * v[0] - 8 * c[1] * c[2] * v[3],
        4 * s[1] * v[1] - 8 * c[0] * c[2] * v[3],
        4 * s[2] * v[2] - 8 * c[0] * c[1] * v[3],
    ]
}

fn primitive_kernel(s: [i128; 3], c: [i128; 3]) -> [i128; 4] {
    [
        2 * c[1] * c[2] * s[1] * s[2],
        2 * c[0] * c[2] * s[0] * s[2],
        2 * c[0] * c[1] * s[0] * s[1],
        s[0] * s[1] * s[2],
    ]
}

fn proportional(a: [i128; 4], b: [i128; 4]) -> bool {
    (0..4).all(|i| (0..4).all(|j| a[i] * b[j] == a[j] * b[i]))
}

fn main() {
    let s1 = [3_i128, 5, 7];
    let c1 = [11_i128, 13, 17];
    let s2 = [19_i128, 23, 29];
    let c2 = [31_i128, 37, 41];
    let k1 = primitive_kernel(s1, c1);
    let k2 = primitive_kernel(s2, c2);

    assert_eq!(matrix_times(s1, c1, k1), [0, 0, 0]);
    assert_eq!(matrix_times(s2, c2, k2), [0, 0, 0]);
    assert!(!proportional(k1, k2));
    assert_ne!(matrix_times(s1, c1, [2, 2, 2, 1]), [0, 0, 0]);
    assert_ne!(matrix_times(s2, c2, [2, 2, 2, 1]), [0, 0, 0]);

    println!(
        "{{\"status\":\"pass\",\"pointwise_kernel_rank\":1,\"constant_kernel_line\":false,\"forgotten_spectator_vector_221\":false}}"
    );
}
