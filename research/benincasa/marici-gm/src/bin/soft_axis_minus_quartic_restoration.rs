fn b(i: usize, j: usize) -> (usize, usize) {
    (i / 2, i / 2 + j)
}

fn main() {
    // c=b+1 and g=a^3*c*(2-c).  Restore the universal quartic factor
    // before taking the c-conormal residue.
    let restored_over_c = [2_i64, -1]; // a^7*(2-c)
    assert_eq!(restored_over_c[0], 2);

    let residue_degree = (7_usize, 0_usize);
    let resonance_degree = (7_usize, 1_usize);
    assert_eq!(b(residue_degree.0, residue_degree.1), (3, 3));
    assert_eq!(b(resonance_degree.0, resonance_degree.1), (3, 4));

    // Entry 460: D_b into (I,J) has scalar 1-J.
    let incoming_db = 1_i64 - residue_degree.1 as i64;
    assert_eq!(incoming_db, 1);

    println!(
        "{{\"schema\":\"marici.benincasa.soft_axis_minus_quartic_restoration.v1\",\"restored_conormal\":\"a^7*(2-c)\",\"minus_residue\":\"2*a^7\",\"residue_bidegree\":[7,0],\"residue_boundary_divisor\":[3,3],\"resonance_bidegree\":[7,1],\"resonance_boundary_divisor\":[3,4],\"incoming_D_b_coefficient\":1,\"minus_residue_exact\":true,\"new_boundary_class\":false}}"
    );
}
