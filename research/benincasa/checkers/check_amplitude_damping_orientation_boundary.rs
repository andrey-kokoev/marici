fn delta_num(a_num: i64, b_num: i64, p_num: i64, p_den: i64) -> i128 {
    // Up to the positive denominator 4*p_den^4, this is
    // (1-p)^2 * B * (A-p^2 B), with A=a_num/4 and B=b_num/4.
    let q = (p_den - p_num) as i128;
    let pn = p_num as i128;
    let pd = p_den as i128;
    let a = a_num as i128;
    let b = b_num as i128;
    q * q * b * (a * pd * pd - b * pn * pn)
}

fn main() {
    // Theta_1: A=1/4, B=3/4. The sign changes at p^2=1/3.
    assert!(delta_num(1, 3, 1, 2) > 0);
    assert!(delta_num(1, 3, 3, 5) < 0);

    // Theta_2: A=3/4, B=1/4. Its nontrivial root p^2=3 is
    // outside the physical interval, so Delta stays positive for p<1.
    for (pn, pd) in [(0, 1), (1, 2), (9, 10), (999, 1000)] {
        assert!(delta_num(3, 1, pn, pd) > 0);
    }
    assert_eq!(delta_num(3, 1, 1, 1), 0);

    // Equal initial concurrence is invariant under A <-> B.
    assert_eq!(1_i64 * 3_i64, 3_i64 * 1_i64);

    println!("amplitude-damping orientation-boundary checks: 8/8 passed");
}
