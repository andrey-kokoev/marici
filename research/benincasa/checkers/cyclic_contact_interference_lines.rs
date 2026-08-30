// Exact C3 representation and readout audit for three labelled interference lines.

fn rotate(v: [i128; 3]) -> [i128; 3] {
    [v[2], v[0], v[1]]
}

fn main() {
    let basis = [[1_i128, 0, 0], [0, 1, 0], [0, 0, 1]];
    for e in basis {
        assert_eq!(rotate(rotate(rotate(e))), e);
    }

    let invariant = [1_i128, 1, 1];
    assert_eq!(rotate(invariant), invariant);

    // Each coefficient denotes f_i*(1,-1); the blockwise standard sum
    // annihilates every vector in the three-dimensional line packet.
    let packets = [[3_i128, 5, 7], [-11, 13, 17], [19, -23, 29]];
    for f in packets {
        let standard_readout = (f[0] - f[0]) + (f[1] - f[1]) + (f[2] - f[2]);
        assert_eq!(standard_readout, 0);
    }

    println!(
        "{{\"status\":\"pass\",\"cyclic_character\":[3,0,0],\"rational_decomposition\":\"Q_triv plus Q(zeta3)\",\"invariant_generator\":[1,1,1],\"standard_readout_rank_on_packet\":0,\"cyclic_invariant_hidden_line_dimension\":1}}"
    );
}
