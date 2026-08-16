//! Full-log product-Rees packet to literal entry143 vertex realization.
//!
//! For every ordered pair of crossing long roads, the two legal edges of the
//! complementary marked corridor have one common label and two moving labels.
//! The product-Rees log-excess cap leaves two normal axes; the conductor Tor
//! axis is the unique axis surviving both chart restrictions.  This forces,
//! rather than stipulates, the bijection
//!
//!     Tor -> persistent label,
//!     normal_0 -> first moving label,
//!     normal_1 -> second moving label.
//!
//! The checker constructs the integral 8x16 full-log cap for each ordered
//! pair, its literal three-label Boolean realization, and both relative
//! adjacent-edge residues.  It then compares the source-selected edges under
//! the physical reflection v -> 3-v.  Exactly one edge per ordered pair lands
//! on the unselected third edge of the reflected vertex.  Thus the pairwise
//! realization is primitive, but the present two-edge source boundary is not
//! physically reflection closed.  A full three-edge vertex-star BC datum is
//! the minimal finite repair.

use std::collections::{BTreeMap, BTreeSet};

const N: u8 = 6;
type Diagonal = (u8, u8);
type Face = BTreeSet<Diagonal>;

const ROADS: [Diagonal; 3] = [(1, 4), (0, 3), (2, 5)];
const ORDERED: [(usize, usize); 6] = [(0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (2, 1)];

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

fn rotate_vertex(v: u8) -> u8 {
    (v + 2) % N
}

fn reflect_vertex(v: u8) -> u8 {
    (9 - v) % N
}

fn permute_diagonal((a, b): Diagonal, action: fn(u8) -> u8) -> Diagonal {
    diagonal(action(a), action(b))
}

fn permute_face(value: &Face, action: fn(u8) -> u8) -> Face {
    value
        .iter()
        .copied()
        .map(|label| permute_diagonal(label, action))
        .collect()
}

fn rotate_times(mut value: Face, count: usize) -> Face {
    for _ in 0..count {
        value = permute_face(&value, rotate_vertex);
    }
    value
}

fn road_halves(road: usize) -> ([Face; 3], [Face; 3]) {
    let d03 = diagonal(0, 3);
    let plus = face(&[short(1), short(3), short(5)]);
    let minus = face(&[short(0), short(2), short(4)]);
    let v10 = face(&[d03, short(1), short(3)]);
    let central = face(&[d03, short(0), short(3)]);
    let v01 = face(&[d03, short(0), short(4)]);
    let turns = match road {
        0 => 2,
        1 => 0,
        2 => 1,
        _ => unreachable!(),
    };
    (
        [plus, v10, central.clone()].map(|x| rotate_times(x, turns)),
        [minus, v01, central].map(|x| rotate_times(x, turns)),
    )
}

fn intersection(left: &Face, right: &Face) -> Face {
    left.intersection(right).copied().collect()
}

fn ordered_edges(half: &[Face; 3]) -> [Face; 2] {
    [
        intersection(&half[0], &half[1]),
        intersection(&half[1], &half[2]),
    ]
}

fn complement(first: usize, second: usize) -> usize {
    (0..3)
        .find(|value| *value != first && *value != second)
        .unwrap()
}

fn crossing((a, b): Diagonal, (c, d): Diagonal) -> bool {
    let between = |x: u8, start: u8, end: u8| {
        let mut y = (start + 1) % N;
        while y != end {
            if y == x {
                return true;
            }
            y = (y + 1) % N;
        }
        false
    };
    between(c, a, b) != between(d, a, b) && between(a, c, d) != between(b, c, d)
}

fn selected_position(mask: u8, bit: usize) -> usize {
    (0..bit).filter(|index| mask & (1 << index) != 0).count()
}

fn contraction(mask: u8, bit: usize) -> Option<(u8, i64)> {
    if mask & (1 << bit) == 0 {
        return None;
    }
    let sign = if selected_position(mask, bit) % 2 == 0 {
        1
    } else {
        -1
    };
    Some((mask & !(1 << bit), sign))
}

fn permutation_sign(values: &[Diagonal]) -> i64 {
    let inversions = (0..values.len())
        .flat_map(|i| (i + 1..values.len()).map(move |j| (i, j)))
        .filter(|(i, j)| values[*i] > values[*j])
        .count();
    if inversions % 2 == 0 {
        1
    } else {
        -1
    }
}

fn wedge_map(source_labels: &[Diagonal; 3], target_order: &[Diagonal], mask: u8) -> (u8, i64) {
    let selected: Vec<_> = source_labels
        .iter()
        .enumerate()
        .filter_map(|(bit, label)| (mask & (1 << bit) != 0).then_some(*label))
        .collect();
    let mut target_mask = 0u8;
    for label in &selected {
        let position = target_order
            .iter()
            .position(|candidate| candidate == label)
            .unwrap();
        target_mask |= 1 << position;
    }
    (target_mask, permutation_sign(&selected))
}

fn target_normal_boundary(face_size: usize, mask: u8) -> Vec<(u8, i64)> {
    let mut out = Vec::new();
    let mut position = 0usize;
    for bit in 0..face_size {
        if mask & (1 << bit) != 0 {
            let exponent = 3 - face_size + position;
            out.push((mask & !(1 << bit), if exponent % 2 == 0 { 1 } else { -1 }));
            position += 1;
        }
    }
    out
}

// Contract Lambda*(a,b,c,tau) by delta=(-1,+1,0,0), then express the
// result in Lambda*(d=a+b,c,tau).  Target axes are (d,c,tau).
fn full_log_cap_column(source_mask: u8) -> BTreeMap<u8, i64> {
    let mut contracted: BTreeMap<u8, i64> = BTreeMap::new();
    for bit in 0..2 {
        if let Some((lower, wedge_sign)) = contraction(source_mask, bit) {
            let delta = if bit == 0 { -1 } else { 1 };
            *contracted.entry(lower).or_default() += wedge_sign * delta;
        }
    }

    let mut result = BTreeMap::new();
    for target_mask in 0u8..8 {
        let has_d = target_mask & 1 != 0;
        let mut representative = 0u8;
        if has_d {
            representative |= 1 << 1; // b coefficient of d=a+b
        }
        if target_mask & 2 != 0 {
            representative |= 1 << 2;
        }
        if target_mask & 4 != 0 {
            representative |= 1 << 3;
        }
        let coefficient = *contracted.get(&representative).unwrap_or(&0);
        if has_d {
            let with_a = (representative & !(1 << 1)) | (1 << 0);
            assert_eq!(*contracted.get(&with_a).unwrap_or(&0), coefficient);
        }
        if coefficient != 0 {
            result.insert(target_mask, coefficient);
        }
    }
    result
}

fn main() {
    // The 8x16 cap is explicitly assembled.  The eight selected preimages
    // b^omega (or a^b^omega when d occurs) give a diagonal unit minor.
    let cap: Vec<_> = (0u8..16).map(full_log_cap_column).collect();
    let mut pivots = Vec::new();
    for target_mask in 0u8..8 {
        let mut source_mask = 1 << 1;
        if target_mask & 1 != 0 {
            source_mask |= 1 << 0;
        }
        if target_mask & 2 != 0 {
            source_mask |= 1 << 2;
        }
        if target_mask & 4 != 0 {
            source_mask |= 1 << 3;
        }
        let column = &cap[source_mask as usize];
        assert_eq!(column.len(), 1);
        assert_eq!(column.get(&target_mask).copied().unwrap().abs(), 1);
        pivots.push(source_mask);
    }
    let unique_pivots: BTreeSet<_> = pivots.iter().copied().collect();
    assert_eq!(unique_pivots.len(), 8);

    let mut literal_rows = 0usize;
    let mut residue_rows = 0usize;
    let mut residue_chain_squares = 0usize;
    let mut unique_axis_assignments = 0usize;
    let mut vertices = Vec::new();
    let mut edge_pairs = Vec::new();

    for (left, right) in ORDERED {
        assert!(crossing(ROADS[left], ROADS[right]));
        let road = complement(left, right);
        let positive = right == (left + 1) % 3;
        let (plus, minus) = road_halves(road);
        let edges = ordered_edges(if positive { &plus } else { &minus });
        assert_eq!(edges[0].len(), 2);
        assert_eq!(edges[1].len(), 2);

        let common = intersection(&edges[0], &edges[1]);
        assert_eq!(common.len(), 1);
        let persistent = *common.iter().next().unwrap();
        let moving_0 = *edges[0].difference(&common).next().unwrap();
        let moving_1 = *edges[1].difference(&common).next().unwrap();
        assert_ne!(moving_0, moving_1);

        let mut vertex = edges[0].clone();
        vertex.extend(edges[1].iter().copied());
        assert_eq!(vertex.len(), 3);
        for first in &vertex {
            for second in &vertex {
                if first < second {
                    assert!(!crossing(*first, *second));
                }
            }
        }

        // Exhaust all six axis permutations.  The Tor axis must occur in both
        // chart-edge packets, while normal_i must occur only in chart i.
        // Exactly one assignment satisfies these intrinsic restrictions.
        let target_labels: Vec<_> = vertex.iter().copied().collect();
        let permutations = [
            [0usize, 1, 2],
            [0, 2, 1],
            [1, 0, 2],
            [1, 2, 0],
            [2, 0, 1],
            [2, 1, 0],
        ];
        let mut local_assignments = 0usize;
        for permutation in permutations {
            let assigned = [
                target_labels[permutation[0]],
                target_labels[permutation[1]],
                target_labels[permutation[2]],
            ];
            let chart_0: Face = [assigned[0], assigned[1]].into_iter().collect();
            let chart_1: Face = [assigned[0], assigned[2]].into_iter().collect();
            if chart_0 == edges[0] && chart_1 == edges[1] {
                local_assignments += 1;
                assert_eq!(assigned, [persistent, moving_0, moving_1]);
            }
        }
        assert_eq!(local_assignments, 1);
        unique_axis_assignments += local_assignments;

        // Source axes after the excess cap are (tau, normal_0, normal_1).
        let source_labels = [persistent, moving_0, moving_1];
        let target_order: Vec<_> = vertex.iter().copied().collect();
        for source_mask in 0u8..8 {
            let (target_mask, coefficient) = wedge_map(&source_labels, &target_order, source_mask);
            assert_eq!(coefficient.abs(), 1);
            literal_rows += 1;

            // Compare the independently defined source exterior differential
            // with entry143's literal |S|=3 normal differential.
            for bit in 0..3 {
                let Some((source_lower, source_sign)) = contraction(source_mask, bit) else {
                    continue;
                };
                let (target_lower, lower_coefficient) =
                    wedge_map(&source_labels, &target_order, source_lower);
                let target_term = target_normal_boundary(3, target_mask)
                    .into_iter()
                    .find(|(lower, _)| *lower == target_lower)
                    .unwrap();
                assert_eq!(coefficient * target_term.1, source_sign * lower_coefficient);
            }
        }

        // The first edge forgets normal_1; the second forgets normal_0.
        // Naturality of contraction proves both adjacent-edge BC rows.
        for (edge_index, missing_axis) in [(0usize, 2usize), (1, 1)] {
            let edge_order: Vec<_> = edges[edge_index].iter().copied().collect();
            let retained_labels = if edge_index == 0 {
                [persistent, moving_0]
            } else {
                [persistent, moving_1]
            };
            for edge_mask in 0u8..4 {
                let mut source_mask = 0u8;
                for bit in 0..2 {
                    if edge_mask & (1 << bit) != 0 {
                        let source_bit = if bit == 0 {
                            0
                        } else if edge_index == 0 {
                            1
                        } else {
                            2
                        };
                        source_mask |= 1 << source_bit;
                    }
                }
                source_mask |= 1 << missing_axis;
                let (source_lower, source_residue) =
                    contraction(source_mask, missing_axis).unwrap();
                let (vertex_mask, vertex_coefficient) =
                    wedge_map(&source_labels, &target_order, source_mask);
                let missing_label = source_labels[missing_axis];
                let missing_target = target_order
                    .iter()
                    .position(|label| *label == missing_label)
                    .unwrap();
                let (target_lower, target_residue) =
                    contraction(vertex_mask, missing_target).unwrap();
                let (mapped_lower, mapped_coefficient) =
                    wedge_map(&source_labels, &target_order, source_lower);
                assert_eq!(target_lower, mapped_lower);
                assert_eq!(
                    vertex_coefficient * target_residue,
                    source_residue * mapped_coefficient
                );

                let selected_edge_labels: Vec<_> = retained_labels
                    .iter()
                    .enumerate()
                    .filter_map(|(bit, label)| (edge_mask & (1 << bit) != 0).then_some(*label))
                    .collect();
                let edge_target_mask = selected_edge_labels.iter().fold(0u8, |mask, label| {
                    mask | (1 << edge_order.iter().position(|x| x == label).unwrap())
                });
                assert_eq!(edge_target_mask.count_ones(), edge_mask.count_ones());
                residue_rows += 1;

                // After residue, source and literal edge differentials agree.
                for bit in 0..2 {
                    if edge_mask & (1 << bit) == 0 {
                        continue;
                    }
                    let source_edge_sign = if selected_position(edge_mask, bit) % 2 == 0 {
                        1
                    } else {
                        -1
                    };
                    let lower = edge_target_mask
                        & !(1
                            << edge_order
                                .iter()
                                .position(|label| *label == retained_labels[bit])
                                .unwrap());
                    let target_edge_sign = target_normal_boundary(2, edge_target_mask)
                        .into_iter()
                        .find(|(candidate, _)| *candidate == lower)
                        .unwrap()
                        .1;
                    let edge_coefficient = permutation_sign(&selected_edge_labels);
                    let lower_selected: Vec<_> = retained_labels
                        .iter()
                        .enumerate()
                        .filter_map(|(candidate_bit, label)| {
                            (candidate_bit != bit && edge_mask & (1 << candidate_bit) != 0)
                                .then_some(*label)
                        })
                        .collect();
                    let lower_coefficient = permutation_sign(&lower_selected);
                    // The uniform codimension-one residue contributes the
                    // standard suspension sign between |S|=3 and |S|=2.
                    assert_eq!(
                        edge_coefficient * target_edge_sign,
                        -source_edge_sign * lower_coefficient
                    );
                    residue_chain_squares += 1;
                }
            }
        }

        vertices.push(vertex);
        edge_pairs.push(edges);
    }

    assert_eq!(unique_axis_assignments, 6);
    assert_eq!(literal_rows, 48);
    assert_eq!(residue_rows, 48);
    assert_eq!(residue_chain_squares, 48);

    // Rotation preserves the ordered source corridor assignment.  Physical
    // reflection does preserve the six literal vertices, but it does not
    // preserve the two selected source corridor edges at the reflected pair.
    // Count this mismatch instead of silently replacing the source corridors
    // by target-chosen reflected edges.
    let mut reflected_vertex_rows = 0usize;
    let mut reflected_selected_edge_rows = 0usize;
    let mut reflected_legal_but_unselected_edge_rows = 0usize;
    for (index, vertex) in vertices.iter().enumerate() {
        let rotated = permute_face(vertex, rotate_vertex);
        let rotated_index = vertices
            .iter()
            .position(|candidate| candidate == &rotated)
            .unwrap();
        for edge in &edge_pairs[index] {
            assert!(edge_pairs[rotated_index].contains(&permute_face(edge, rotate_vertex)));
        }
        let reflected = permute_face(vertex, reflect_vertex);
        let reflected_index = vertices
            .iter()
            .position(|candidate| candidate == &reflected)
            .unwrap();
        reflected_vertex_rows += 1;
        let mut local_selected = 0usize;
        let mut reflected_edges = BTreeSet::new();
        for edge in &edge_pairs[index] {
            let reflected_edge = permute_face(edge, reflect_vertex);
            assert!(reflected_edge.is_subset(&reflected));
            reflected_edges.insert(reflected_edge.clone());
            if edge_pairs[reflected_index].contains(&reflected_edge) {
                reflected_selected_edge_rows += 1;
                local_selected += 1;
            } else {
                reflected_legal_but_unselected_edge_rows += 1;
            }
        }
        assert_eq!(local_selected, 1);

        // The reflected pair and the target-selected pair together give all
        // three codimension-one faces of the common triangulation vertex.
        reflected_edges.extend(edge_pairs[reflected_index].iter().cloned());
        let all_vertex_edges: BTreeSet<_> = reflected
            .iter()
            .map(|missing| {
                reflected
                    .iter()
                    .filter(|label| *label != missing)
                    .copied()
                    .collect::<Face>()
            })
            .collect();
        assert_eq!(reflected_edges, all_vertex_edges);
    }
    assert_eq!(reflected_vertex_rows, 6);
    assert_eq!(
        reflected_selected_edge_rows + reflected_legal_but_unselected_edge_rows,
        12
    );
    assert_eq!(reflected_selected_edge_rows, 6);
    assert_eq!(reflected_legal_but_unselected_edge_rows, 6);

    println!(
        "{}",
        r#"{"status":"falsified_scoped_two_edge_physical_reflection_closure","ordered_pairs":6,"full_log_source_states_per_pair":16,"post_cap_states_per_pair":8,"full_log_matrix_rows":48,"full_log_matrix_columns":96,"full_log_matrix_rank":48,"full_log_smith_all_ones":true,"axis_assignment_unique_per_pair":true,"tor_axis_maps_to_unique_persistent_corridor_label":true,"two_post_cap_normal_axes_map_to_two_moving_labels":true,"literal_entry143_vertex_rows":48,"adjacent_edge_residue_rows":48,"residue_chain_squares":48,"D3_rotation":true,"physical_reflection":"v_to_3_minus_v","physical_reflection_vertex_rows":6,"physical_reflection_selected_edge_rows":6,"physical_reflection_legal_but_unselected_edge_rows":6,"full_three_edge_vertex_star_closes":true,"base_inversions":false,"spatial_six_functor_push_pull_constructed":false,"literal_endpoint_extensions_constructed":false,"based_qSigma_connector_constructed":false,"endpoint_Q_mapping_fiber_instantiated":false,"minimal_additional_datum":"one third-edge wall Beck-Chevalley cell per ordered pair, promoting the source boundary to the full three-edge literal vertex star","next_gate":"construct the full vertex-star log-BM correspondence and derive its third-edge wall restriction before attaching endpoint and qSigma rows"}"#
    );
}
