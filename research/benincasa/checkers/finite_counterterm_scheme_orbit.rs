fn det3(m: [[i64; 3]; 3]) -> i64 {
    m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
}

fn rank3(m: [[i64; 3]; 3]) -> usize {
    if det3(m) != 0 { 3 } else { 0 }
}

fn main() {
    // Twice the source shape vectors in the ordered response basis
    // (1, p^2 eta^2, p^4 eta^4). Independent nonzero column scalings
    // from H/M and epsilon do not affect rank.
    let response_map = [[2, -6, -5], [-2, -2, -5], [0, 0, -2]];
    let determinant = det3(response_map);
    let rank = rank3(response_map);

    assert_eq!(determinant, 32);
    assert_eq!(rank, 3);

    println!("determinant={determinant}");
    println!("rank={rank}");
    println!("response_dimension=3");
    println!("scheme_orbit_is_full=true");
    println!("scheme_invariant_linear_quotient_dimension=0");
}
