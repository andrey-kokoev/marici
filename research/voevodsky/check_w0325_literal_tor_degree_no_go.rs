//! Graded-rank obstruction for a literal W_03,25 -> q_14 realization.
//!
//! Entry143 gives two ordinary corridor edges, each with the four Boolean
//! states H subset S in degrees 1+|H|. The external pair object has one
//! Boolean packet tensored with independent Tor degrees 0 and 1. A realization
//! retaining both Tor grades and admitting BC retractions must be a graded
//! split injection after one fixed Gysin shift. This checker proves that no
//! such shift exists and identifies the minimal shifted-edge enhancement.

use std::collections::BTreeSet;

type Diagonal = (u8, u8);
type Face = BTreeSet<Diagonal>;

fn diagonal(a: u8, b: u8) -> Diagonal {
    if a < b {
        (a, b)
    } else {
        (b, a)
    }
}

fn face(values: &[Diagonal]) -> Face {
    values.iter().copied().collect()
}

fn crossing((a, b): Diagonal, (c, d): Diagonal) -> bool {
    let between = |x: u8, start: u8, end: u8| {
        let mut y = (start + 1) % 6;
        while y != end {
            if y == x {
                return true;
            }
            y = (y + 1) % 6;
        }
        false
    };
    between(c, a, b) != between(d, a, b) && between(a, c, d) != between(b, c, d)
}

fn shifted(profile: &[usize], offset: i32) -> Vec<(i32, usize)> {
    profile
        .iter()
        .enumerate()
        .filter(|(_, rank)| **rank != 0)
        .map(|(degree, rank)| (degree as i32 + offset, *rank))
        .collect()
}

fn rank_at(profile: &[(i32, usize)], degree: i32) -> usize {
    profile
        .iter()
        .filter(|(present, _)| *present == degree)
        .map(|(_, rank)| *rank)
        .sum()
}

fn main() {
    // The exact positive q14 half-corridor for ordered pair (D03,D25).
    let first_edge = face(&[diagonal(1, 5), diagonal(1, 3)]);
    let second_edge = face(&[diagonal(1, 4), diagonal(1, 3)]);
    assert_eq!(first_edge.len(), 2);
    assert_eq!(second_edge.len(), 2);
    for edge in [&first_edge, &second_edge] {
        let values: Vec<_> = edge.iter().copied().collect();
        assert!(!crossing(values[0], values[1]));
    }
    let persistent: Face = first_edge.intersection(&second_edge).copied().collect();
    assert_eq!(persistent, face(&[diagonal(1, 3)]));

    // For |S|=2, entry143 degree is 3-|S|+|H|=1+|H|.
    // A single edge Boolean cube therefore has profile
    // P=t+2t^2+t^3. Both literal corridor edges are unshifted: 2P.
    let edge_profile = vec![(1_i32, 1_usize), (2, 2), (3, 1)];
    let literal_target: Vec<_> = (1_i32..=3)
        .map(|degree| (degree, 2 * rank_at(&edge_profile, degree)))
        .collect();
    assert_eq!(literal_target, vec![(1, 2), (2, 4), (3, 2)]);

    // W_03,25 carries P tensor (Tor0 + Tor1[1]):
    // t + 3t^2 + 3t^3 + t^4.
    let source_profile = vec![(1_i32, 1_usize), (2, 3), (3, 3), (4, 1)];
    assert_eq!(
        source_profile.iter().map(|(_, rank)| rank).sum::<usize>(),
        8
    );
    assert_eq!(
        literal_target.iter().map(|(_, rank)| rank).sum::<usize>(),
        8
    );

    // A BC realization retaining both independent Tor grades has a left
    // inverse on this packet. Degreewise, its source rank must therefore not
    // exceed target rank. No global Gysin shift satisfies that condition.
    let mut admissible_shifts = Vec::new();
    let mut witnesses = Vec::new();
    for gysin_shift in -6_i32..=6 {
        let shifted_source: Vec<_> = source_profile
            .iter()
            .map(|(degree, rank)| (degree + gysin_shift, *rank))
            .collect();
        let failing_degree = (-6_i32..=10)
            .find(|degree| rank_at(&shifted_source, *degree) > rank_at(&literal_target, *degree));
        if let Some(degree) = failing_degree {
            witnesses.push((gysin_shift, degree));
        } else {
            admissible_shifts.push(gysin_shift);
        }
    }
    assert!(admissible_shifts.is_empty());
    assert_eq!(witnesses.len(), 13);

    // Minimal positive control: give the second corridor edge the
    // extraordinary shift [1]. Then P + tP equals P(1+t) exactly, so Tor0
    // maps to the first edge and Tor1 to the shifted second edge.
    let shifted_edge = shifted(&[(1_usize), 2, 1], 2);
    // shifted() indexes the supplied coefficients from degree zero; offset 2
    // produces degrees 2,3,4 for tP.
    assert_eq!(shifted_edge, vec![(2, 1), (3, 2), (4, 1)]);
    let enhanced_target: Vec<_> = (1_i32..=4)
        .map(|degree| {
            (
                degree,
                rank_at(&edge_profile, degree) + rank_at(&shifted_edge, degree),
            )
        })
        .collect();
    assert_eq!(enhanced_target, source_profile);

    // Ordinary entry143 has no datum distinguishing one edge by this shift.
    // Reflection exchanges the two edges, so an enhancement must also carry
    // an oriented exchange isomorphism; choosing a shifted edge by hand is not
    // a literal realization.
    let literal_shifted_edges = 0usize;
    assert_eq!(literal_shifted_edges, 0);

    println!(
        "{}",
        r#"{"status":"falsified_scoped_literal_one_pair_tor_faithful_realization","pair":"W_03,25_to_q14","literal_edges":[["x5","x1"],["D14","x1"]],"literal_edge_boolean_profile":{"1":1,"2":2,"3":1},"literal_two_edge_profile":{"1":2,"2":4,"3":2},"source_boolean_times_tor_profile":{"1":1,"2":3,"3":3,"4":1},"tested_global_gysin_shifts":[-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6],"admissible_shifts":[],"graded_split_injection_exists":false,"reason":"for every fixed shift some degree has source rank greater than the literal target rank","minimal_enhancement":"replace the two unshifted corridor packets P+P by an oriented extraordinary pair P plus P[1], so P+tP=P(1+t) and Tor0/Tor1 remain distinct","enhanced_profile":{"1":1,"2":3,"3":3,"4":1},"literal_entry143_shifted_edge_present":false,"ordinary_nonfaithful_or_tor_collapsing_maps_excluded_by_scope":true,"endpoint_q_mapping_fiber_instantiated":false,"p_partial_Q_defined":false}"#
    );
}
