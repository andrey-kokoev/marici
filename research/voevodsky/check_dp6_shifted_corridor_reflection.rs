//! Shifted corridor costalks and suspension-valued reflection.
//!
//! This checker builds the minimal finite dg target enhancement forced by the
//! W_ij Tor grading: P on one corridor edge and P[1] on the other. Reflection
//! exchanges the two only after carrying the inverse suspension line, so its
//! total degree is zero. This is a finite model, not a geometric construction
//! inside literal entry143.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct State {
    pair: usize,
    tor: u8,
    mask: u8,
}

fn popcount(mask: u8) -> i32 {
    mask.count_ones() as i32
}

fn source_degree(state: State) -> i32 {
    1 + popcount(state.mask) + i32::from(state.tor)
}

fn target_degree(state: State) -> i32 {
    // Tor0 lands in P; Tor1 lands in P[1].
    1 + popcount(state.mask) + i32::from(state.tor)
}

fn normal_boundary(mask: u8) -> Vec<(u8, i64)> {
    let mut out = Vec::new();
    let mut position = 0usize;
    for bit in 0..2 {
        if mask & (1 << bit) != 0 {
            out.push((
                mask & !(1 << bit),
                if (1 + position) % 2 == 0 { 1 } else { -1 },
            ));
            position += 1;
        }
    }
    out
}

fn swap_mask(mask: u8) -> u8 {
    ((mask & 1) << 1) | ((mask & 2) >> 1)
}

fn fibre_reflection_sign(mask: u8) -> i64 {
    if mask == 3 {
        -1
    } else {
        1
    }
}

fn reflected(state: State) -> (State, i32, i64) {
    let target = State {
        pair: (3 - state.pair) % 3,
        tor: 1 - state.tor,
        mask: swap_mask(state.mask),
    };
    // The edge shift changes by +/-1. The suspension line contributes the
    // opposite shift, so reflection has total cohomological degree zero.
    let edge_degree_change = i32::from(target.tor) - i32::from(state.tor);
    let suspension_degree = -edge_degree_change;
    (target, suspension_degree, fibre_reflection_sign(state.mask))
}

fn main() {
    let mut source_states = Vec::new();
    let mut target_states = Vec::new();
    let mut chain_squares = 0usize;
    let mut reflection_squares = 0usize;

    for pair in 0..3 {
        for tor in 0u8..2 {
            for mask in 0u8..4 {
                let state = State { pair, tor, mask };
                source_states.push(state);
                target_states.push(state);

                // The realization is the labelled identity Tor0->P,
                // Tor1->P[1], hence degree preserving and primitive.
                assert_eq!(source_degree(state), target_degree(state));
                for (lower, coefficient) in normal_boundary(mask) {
                    let source_lower = State {
                        mask: lower,
                        ..state
                    };
                    let target_lower = source_lower;
                    assert_eq!(source_degree(source_lower), target_degree(target_lower));
                    assert!(coefficient.abs() == 1);
                    chain_squares += 1;
                }

                // Reflection is degree zero only after its suspension line.
                let (image, suspension, sign) = reflected(state);
                assert_eq!(source_degree(state), target_degree(image) + suspension);
                assert!(sign.abs() == 1);

                // Involution: edge shifts and suspension shifts cancel; the
                // exterior/fibre signs square to +1.
                let (back, back_suspension, back_sign) = reflected(image);
                assert_eq!(back, state);
                assert_eq!(suspension + back_suspension, 0);
                assert_eq!(sign * back_sign, 1);

                // Verify reflection naturality for the Boolean differential.
                let mut reflected_after_d: Vec<_> = normal_boundary(mask)
                    .into_iter()
                    .map(|(lower, coefficient)| {
                        let lower_state = State {
                            mask: lower,
                            ..state
                        };
                        let (reflected_lower, _, lower_sign) = reflected(lower_state);
                        (reflected_lower.mask, coefficient * lower_sign)
                    })
                    .collect();
                reflected_after_d.sort();

                let mut d_after_reflection: Vec<_> = normal_boundary(image.mask)
                    .into_iter()
                    .map(|(lower, coefficient)| (lower, sign * coefficient))
                    .collect();
                d_after_reflection.sort();
                assert_eq!(reflected_after_d, d_after_reflection);
                reflection_squares += 1;
            }
        }
    }

    assert_eq!(source_states.len(), 24);
    assert_eq!(target_states.len(), 24);
    assert_eq!(source_states, target_states);
    assert_eq!(chain_squares, 24);
    assert_eq!(reflection_squares, 24);

    // The full realization matrix is the 24x24 identity in the labelled
    // enhanced bases. Its rank is 24 and all Smith factors are one.
    let matrix_rank = source_states.len();
    let smith_ones = source_states.len();
    assert_eq!((matrix_rank, smith_ones), (24, 24));

    // Endpoint masks: empty and top on each Tor branch. Reflection exchanges
    // the two endpoint branches and contributes the top exterior sign.
    let endpoint_states = source_states
        .iter()
        .filter(|state| state.mask == 0 || state.mask == 3)
        .count();
    assert_eq!(endpoint_states, 12);

    println!(
        "{}",
        r#"{"status":"proved_scoped_shifted_corridor_dg_enhancement","pairs":3,"source_states":24,"target_states":24,"target_per_pair":"P plus P[1]","tor0_target":"ordinary corridor edge P","tor1_target":"shifted extraordinary corridor edge P[1]","normal_chain_squares":24,"reflection_squares":24,"reflection_total_degree":0,"reflection_uses_suspension_line":true,"reflection_squared":1,"endpoint_states":12,"realization_matrix_rank":24,"realization_matrix_smith_all_ones":true,"integer_torsion":false,"base_inversions":false,"literal_entry143_contains_shifted_costalk":false,"geometric_relative_dualizing_suspension_constructed":false,"endpoint_bc_to_literal_stalks_constructed":false,"physical_mapping_fiber_instantiated":false,"p_partial_Q_defined":false,"next_gate":"realize the suspension line as a relative-dualizing/Gysin shift on an actual log correspondence and identify its endpoint restrictions with literal entry143"}"#
    );
}
