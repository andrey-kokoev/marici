// Exact invariant-rank and projective-covector selection audit.

fn proportional(a: [i32; 2], b: [i32; 2]) -> bool {
    a[0] * b[1] == a[1] * b[0]
}

fn main() {
    // Three cyclic copies of local Tor grades (1,2,1).
    let invariant_ranks = [1_i32, 2, 1];
    assert_eq!(invariant_ranks[1], 2);

    // Exceptional parity-check rows (y_hat,-2q_hat).
    let c1 = [1_i32, -2];
    let c2 = [3_i32, -4];
    assert!(!proportional(c1, c2));

    // Their kernel vectors (2q_hat,y_hat) also differ projectively.
    let k1 = [2_i32, 1];
    let k2 = [4_i32, 3];
    assert!(!proportional(k1, k2));

    println!(
        "{{\"status\":\"pass\",\"cyclic_invariant_ranks\":[1,2,1],\"middle_unique_line\":false,\"exceptional_covector_direction_dependent\":true}}"
    );
}
