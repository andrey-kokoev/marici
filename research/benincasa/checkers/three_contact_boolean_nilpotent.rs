// Nilpotent-orbit module of the product of three logarithmic contacts.

fn variation(label: usize, basis_mask: usize) -> Option<usize> {
    let bit = 1_usize << label;
    if basis_mask & bit == 0 {
        None
    } else {
        Some(basis_mask ^ bit)
    }
}

fn main() {
    let mut hilbert = [0_usize; 4];
    for mask in 0_usize..8 {
        hilbert[mask.count_ones() as usize] += 1;
        for i in 0..3 {
            // N_i^2=0.
            let twice = variation(i, mask).and_then(|m| variation(i, m));
            assert_eq!(twice, None);
            for j in 0..3 {
                // The labelled variations commute.
                let ij = variation(i, mask).and_then(|m| variation(j, m));
                let ji = variation(j, mask).and_then(|m| variation(i, m));
                assert_eq!(ij, ji);
            }
        }
    }
    assert_eq!(hilbert, [1, 3, 3, 1]);

    // Every basis vector is obtained uniquely from tau_1 tau_2 tau_3 by
    // applying the complementary set of variations.
    let top = 0b111_usize;
    let mut orbit = [false; 8];
    for applied in 0_usize..8 {
        let mut state = Some(top);
        for i in 0..3 {
            if applied & (1 << i) != 0 {
                state = state.and_then(|m| variation(i, m));
            }
        }
        orbit[state.expect("top orbit cannot vanish for distinct labels")] = true;
    }
    assert!(orbit.iter().all(|seen| *seen));

    println!(
        "{{\"status\":\"pass\",\"module_rank\":8,\"hilbert\":[1,3,3,1],\"commuting\":true,\"square_zero\":true,\"top_cyclic\":true}}"
    );
}
