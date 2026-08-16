//! Ordered dP6 log-link dictionary for the marked K6 half-corridors.
//!
//! The two toric contractions label the six maximal dP6 cones by all ordered
//! pairs of distinct physical roads.  The omitted road therefore selects a
//! marked q_k corridor, while reversal of the ordered pair selects the other
//! normalization half.  This checker derives the resulting 24 source-state
//! columns and their legal target Boolean chains.
//!
//! Scope: finite labelled log-link/carrier comparison.  It does not construct
//! the extraordinary line-valued Gysin transformation or literal six-functor
//! stalk map.

use std::collections::BTreeSet;

const N: u8 = 6;
type Diagonal = (u8, u8);
type Face = BTreeSet<Diagonal>;

const ROADS: [Diagonal; 3] = [(1, 4), (0, 3), (2, 5)];
const PI: [usize; 6] = [0, 0, 1, 1, 2, 2];
const PI_CR: [usize; 6] = [1, 2, 2, 0, 0, 1];

fn diagonal(a: u8, b: u8) -> Diagonal {
    if a < b {
        (a, b)
    } else {
        (b, a)
    }
}

fn short(i: usize) -> Diagonal {
    diagonal(i as u8, (i as u8 + 2) % N)
}

fn face(values: &[Diagonal]) -> Face {
    values.iter().copied().collect()
}

fn rotate_diagonal((a, b): Diagonal) -> Diagonal {
    diagonal((a + 2) % N, (b + 2) % N)
}

fn rotate_face(value: &Face) -> Face {
    value.iter().copied().map(rotate_diagonal).collect()
}

fn crosses(first: Diagonal, second: Diagonal) -> bool {
    let (a, c) = first;
    let (b, d) = second;
    if a == b || a == d || c == b || c == d {
        return false;
    }
    let between = |x: u8, left: u8, right: u8| {
        let span = (right + N - left) % N;
        let position = (x + N - left) % N;
        position > 0 && position < span
    };
    between(b, a, c) != between(d, a, c) && between(a, b, d) != between(c, b, d)
}

fn compatible(value: &Face) -> bool {
    value
        .iter()
        .all(|a| value.iter().all(|b| a == b || !crosses(*a, *b)))
}

fn intersection(left: &Face, right: &Face) -> Face {
    left.intersection(right).copied().collect()
}

fn ordered_half_edges(half: &[Face; 3]) -> [[Diagonal; 2]; 2] {
    let first = intersection(&half[0], &half[1]);
    let second = intersection(&half[1], &half[2]);
    assert_eq!(first.len(), 2);
    assert_eq!(second.len(), 2);
    let persistent: Vec<_> = first.intersection(&second).copied().collect();
    assert_eq!(persistent.len(), 1);
    let persistent = persistent[0];
    let first_moving: Vec<_> = first.difference(&face(&[persistent])).copied().collect();
    let second_moving: Vec<_> = second.difference(&face(&[persistent])).copied().collect();
    assert_eq!(first_moving.len(), 1);
    assert_eq!(second_moving.len(), 1);
    [
        [first_moving[0], persistent],
        [second_moving[0], persistent],
    ]
}

fn rotate_times(mut value: Face, count: usize) -> Face {
    for _ in 0..count {
        value = rotate_face(&value);
    }
    value
}

fn base_halves() -> ([Face; 3], [Face; 3]) {
    let d03 = diagonal(0, 3);
    let plus = face(&[short(1), short(3), short(5)]);
    let minus = face(&[short(0), short(2), short(4)]);
    let v10 = face(&[d03, short(1), short(3)]);
    let central = face(&[d03, short(0), short(3)]);
    let v01 = face(&[d03, short(0), short(4)]);
    ([plus, v10, central.clone()], [minus, v01, central])
}

fn road_halves(road: usize) -> ([Face; 3], [Face; 3]) {
    // Base is road 1 = D03. Rotation sends 1 -> 2 -> 0.
    let turns = match road {
        0 => 2,
        1 => 0,
        2 => 1,
        _ => unreachable!(),
    };
    let (plus, minus) = base_halves();
    (
        plus.map(|value| rotate_times(value, turns)),
        minus.map(|value| rotate_times(value, turns)),
    )
}

fn normal_removals(mask: u8) -> Vec<(u8, i64)> {
    let mut result = Vec::new();
    let mut position = 0usize;
    for bit in 0u8..2 {
        if mask & (1 << bit) != 0 {
            let sign = if (1 + position) % 2 == 0 { 1 } else { -1 };
            result.push((mask & !(1 << bit), sign));
            position += 1;
        }
    }
    result
}

fn complement(first: usize, second: usize) -> usize {
    (0..3)
        .find(|value| *value != first && *value != second)
        .unwrap()
}

fn main() {
    let ordered: Vec<_> = (0..6).map(|cone| (PI[cone], PI_CR[cone])).collect();
    assert_eq!(
        ordered,
        vec![(0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (2, 1)]
    );
    let ordered_set: BTreeSet<_> = ordered.iter().copied().collect();
    assert_eq!(ordered_set.len(), 6);
    assert!(ordered.iter().all(|(a, b)| a != b));

    let mut source_columns = 0usize;
    let mut target_boolean_terms = 0usize;
    let mut plus_cones = 0usize;
    let mut minus_cones = 0usize;
    let mut complements = [0usize; 3];

    for cone in 0..6 {
        let (first, second) = ordered[cone];
        let road = complement(first, second);
        complements[road] += 1;
        let positive = second == (first + 1) % 3;
        if positive {
            plus_cones += 1;
        } else {
            minus_cones += 1;
        }

        let (plus_half, minus_half) = road_halves(road);
        let half = if positive { plus_half } else { minus_half };
        assert_eq!(half[0].len(), 3);
        assert_eq!(half[1].len(), 3);
        assert_eq!(half[2].len(), 3);
        assert!(half.iter().all(compatible));

        let ordered_edges = ordered_half_edges(&half);

        for mask in 0u8..4 {
            source_columns += 1;
            for labels in &ordered_edges {
                let edge = face(labels);
                assert!(compatible(&edge));
                let h: Face = labels
                    .iter()
                    .enumerate()
                    .filter_map(|(bit, value)| ((mask & (1 << bit)) != 0).then_some(*value))
                    .collect();
                assert!(h.is_subset(&edge));
                assert_eq!(edge.difference(&h).count(), 2 - mask.count_ones() as usize);
                target_boolean_terms += 1;
            }

            let mut d2 = 0i64;
            for (middle, first_sign) in normal_removals(mask) {
                for (_, second_sign) in normal_removals(middle) {
                    d2 += first_sign * second_sign;
                }
            }
            assert_eq!(d2, 0);
        }

        let polar = (cone + 3) % 6;
        assert_eq!(ordered[polar], (second, first));
        assert_eq!(complement(ordered[polar].0, ordered[polar].1), road);
    }

    assert_eq!(plus_cones, 3);
    assert_eq!(minus_cones, 3);
    assert_eq!(complements, [2, 2, 2]);
    assert_eq!(source_columns, 24);
    assert_eq!(target_boolean_terms, 48);

    // Rotation by two fan cones rotates both ordered road labels and the
    // complementary marked corridor.
    for cone in 0..6 {
        let rotated = (cone + 2) % 6;
        assert_eq!(ordered[rotated].0, (ordered[cone].0 + 1) % 3);
        assert_eq!(ordered[rotated].1, (ordered[cone].1 + 1) % 3);
        assert_eq!(
            complement(ordered[rotated].0, ordered[rotated].1),
            (complement(ordered[cone].0, ordered[cone].1) + 1) % 3
        );
    }

    // The three marked corridors use the actual physical long labels.
    for road in 0..3 {
        let (plus, minus) = road_halves(road);
        assert!(plus[1].contains(&ROADS[road]));
        assert!(plus[2].contains(&ROADS[road]));
        assert!(minus[1].contains(&ROADS[road]));
        assert!(minus[2].contains(&ROADS[road]));
        assert_eq!(plus[2], minus[2]);

        let next = (road + 1) % 3;
        let (next_plus, next_minus) = road_halves(next);
        for (source, target) in [
            (ordered_half_edges(&plus), ordered_half_edges(&next_plus)),
            (ordered_half_edges(&minus), ordered_half_edges(&next_minus)),
        ] {
            for edge in 0..2 {
                for label in 0..2 {
                    assert_eq!(rotate_diagonal(source[edge][label]), target[edge][label]);
                }
            }
        }
    }

    println!(
        "{}",
        r#"{"status":"proved_scoped_ordered_dp6_log_link_to_marked_half_corridor_dictionary","ordered_cone_road_pairs":[[0,1],[0,2],[1,2],[1,0],[2,0],[2,1]],"polarity":"cone i+3 reverses the ordered road pair","complementary_corridors_each":2,"plus_half_cones":3,"minus_half_cones":3,"source_boolean_columns":24,"target_legal_boolean_terms":48,"target_label_order":"moving_then_persistent","normal_d_squared":0,"d3_rotation_exact_on_ordered_boolean_basis":true,"retained_tor_grades":[0,1],"ordinary_crossing_face_map":false,"extraordinary_occurrence_line_map_constructed":false,"literal_six_functor_stalk_map_constructed":false,"adjacent_facet_bc_coefficients_constructed":false,"strict_reflection_comparison_constructed":false,"next_gate":"derive the occurrence-line/excess-Gysin transformation on one ordered cone and prove that its two endpoint restrictions are the adjacent long-facet packets; the carrier target dictionary is now forced"}"#
    );
}
