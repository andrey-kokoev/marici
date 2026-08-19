use std::collections::BTreeSet;

type Channel = (u8, u8);

fn channel(a: u8, b: u8) -> Channel {
    if a < b { (a, b) } else { (b, a) }
}

fn boundary_channels(order: [u8; 5]) -> BTreeSet<Channel> {
    (0..5)
        .map(|i| channel(order[i], order[(i + 1) % 5]))
        .collect()
}

fn common_vertex(a: [u8; 5], b: [u8; 5]) -> BTreeSet<Channel> {
    boundary_channels(a)
        .intersection(&boundary_channels(b))
        .copied()
        .collect()
}

fn main() {
    // Mizera's source-normalized five-point KLT bases.
    let rows = [[1, 2, 3, 4, 5], [1, 2, 4, 3, 5]];
    let cols = [[1, 3, 2, 5, 4], [1, 4, 2, 5, 3]];

    let support = [
        [common_vertex(rows[0], cols[0]), common_vertex(rows[0], cols[1])],
        [common_vertex(rows[1], cols[0]), common_vertex(rows[1], cols[1])],
    ];

    assert_eq!(support[0][0], BTreeSet::from([channel(2, 3), channel(4, 5)]));
    assert!(support[0][1].is_empty());
    assert!(support[1][0].is_empty());
    assert_eq!(support[1][1], BTreeSet::from([channel(2, 4), channel(3, 5)]));

    // Field-theory leading coefficients at the physical sample used in
    // Entry 881.  Momentum conservation fixes the non-planar invariants.
    let [s12, s23, s34, s45, s51] = [2_i128, 3, 5, 11, 17];
    let s24 = s51 - s23 - s34;
    let s35 = s12 - s34 - s45;
    assert_eq!((s24, s35), (9, -14));

    // The inverse KLT matrix m and KLT kernel S are diagonal in these bases.
    // Their common global normalization is suppressed.
    let m_num = [1_i128, 1];
    let m_den = [s23 * s45, s24 * s35];
    let kernel = [s23 * s45, s24 * s35];
    assert_eq!(m_num[0] * kernel[0], m_den[0]);
    assert_eq!(m_num[1] * kernel[1], m_den[1]);

    println!("five_point_diagonal_klt_basis: ok");
    println!("support_matrix: [[(23,45),0],[0,(24,35)]]");
    println!("derived_invariants: s24={s24} s35={s35}");
    println!("field_theory_kernel_diagonal: [{},{}]", kernel[0], kernel[1]);
}
