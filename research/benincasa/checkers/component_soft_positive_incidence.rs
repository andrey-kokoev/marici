// Finite exact audit of the nonnegative linear-incidence lemma.

fn main() {
    let mut tested = 0_usize;
    for xj in 0_i32..=4 {
        for xk in 0_i32..=4 {
            for yij in 0_i32..=4 {
                for yik in 0_i32..=4 {
                    let q = xj + xk + yij + yik;
                    assert_eq!(q == 0, xj == 0 && xk == 0 && yij == 0 && yik == 0);
                    tested += 1;
                }
            }
        }
    }
    assert_eq!(tested, 625);
    println!(
        "{{\"status\":\"pass\",\"nonnegative_packets\":625,\"q_zero_iff_all_four_summands_zero\":true,\"positive_interior_incidence\":false}}"
    );
}
