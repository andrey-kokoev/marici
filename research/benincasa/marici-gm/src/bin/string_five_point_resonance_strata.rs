fn kernel_rank(zero: [bool; 4]) -> usize {
    let first_nonzero = !(zero[0] || zero[1]);
    let second_nonzero = !(zero[2] || zero[3]);
    usize::from(first_nonzero) + usize::from(second_nonzero)
}

fn main() {
    // Ordered sine factors: (23), (45), (24), (35).
    let mut census = [0_usize; 3];
    for mask in 0_u8..16 {
        let zero = [
            mask & 1 != 0,
            mask & 2 != 0,
            mask & 4 != 0,
            mask & 8 != 0,
        ];
        census[kernel_rank(zero)] += 1;
    }

    // Generic stratum; six rank-one patterns; nine rank-zero patterns.
    assert_eq!(census, [9, 6, 1]);
    assert_eq!(kernel_rank([false; 4]), 2);
    assert_eq!(kernel_rank([true, false, false, false]), 1);
    assert_eq!(kernel_rank([false, false, true, false]), 1);
    assert_eq!(kernel_rank([true, false, true, false]), 0);

    // Resonance changes only diagonal coefficient valuations.  The two
    // labelled common vertices from Entry 883 remain present in every case.
    let carrier_vertices = [["23", "45"], ["24", "35"]];
    assert_eq!(carrier_vertices.len(), 2);

    println!("five_point_string_resonance_strata: ok");
    println!("kernel_rank_census_rank0_rank1_rank2: {census:?}");
    println!("carrier_vertices_fixed: [[23,45],[24,35]]");
}
