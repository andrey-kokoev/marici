// Exact rank test in the frozen nine-master source basis.

fn rank_two(x1: i128) -> bool {
    // Iy=e2; Iq=e3-X1*e4 in coordinates e1,...,e9.
    let iy = [0_i128, 1, 0, 0, 0, 0, 0, 0, 0];
    let iq = [0_i128, 0, 1, -x1, 0, 0, 0, 0, 0];

    // The e2/e3 minor is identically one.
    iy[1] * iq[2] - iy[2] * iq[1] == 1
}

fn main() {
    for x1 in -32_i128..=32 {
        assert!(rank_two(x1));
    }
    println!(
        "{{\"status\":\"pass\",\"x1_samples\":65,\"Iy\":\"e2\",\"Iq\":\"e3-X1*e4\",\"source_basis_rank\":2,\"universal_rank_one_relation\":false}}"
    );
}
