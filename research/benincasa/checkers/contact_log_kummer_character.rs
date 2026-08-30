// Exact monodromy-character audit for the common normal wall nu=0.

fn mat_mul(a: [[i32; 2]; 2], b: [[i32; 2]; 2]) -> [[i32; 2]; 2] {
    let mut c = [[0; 2]; 2];
    for i in 0..2 {
        for j in 0..2 {
            for k in 0..2 {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    c
}

fn main() {
    // Basis (1, tau), tau=(2*pi*i)^(-1)log(nu): tau -> tau+1.
    let t_log = [[1, 1], [0, 1]];
    let identity = [[1, 0], [0, 1]];
    let n = [[0, 1], [0, 0]];
    assert_eq!(mat_mul(n, n), [[0, 0], [0, 0]]);
    assert_ne!(n, [[0, 0], [0, 0]]);

    // A lower-sector radical sqrt(nu_i nu_j), with nu_j generic, has
    // semisimple monodromy -1 around nu_i=0.
    let t_kummer = -1;

    // An intertwiner f: Kummer -> logarithmic block would obey
    // T_log f = -f.  The exact matrix T_log+I has determinant four.
    let intertwiner_matrix = [
        [t_log[0][0] - t_kummer, t_log[0][1]],
        [t_log[1][0], t_log[1][1] - t_kummer],
    ];
    let det = intertwiner_matrix[0][0] * intertwiner_matrix[1][1]
        - intertwiner_matrix[0][1] * intertwiner_matrix[1][0];
    assert_eq!(det, 4);
    assert_ne!(t_log, identity);

    println!(
        "{{\"status\":\"pass\",\"support\":\"nu=0\",\"log_unipotent_rank\":1,\"log_N_squared_zero\":true,\"kummer_character\":-1,\"intertwiner_rank\":0}}"
    );
}
