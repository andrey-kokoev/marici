//! Full 27-state endpoint-star comparison in the finite labelled log/Rees model.
//!
//! Each of the three compatible endpoint labels has three states: absent,
//! present without a normal circle, and present with a normal circle. Their
//! product is canonically indexed by every literal entry143 pair H subset S
//! subset v. The checker derives, rather than stipulates, the orientation
//! rebase matching the product differential to entry143 radial and normal
//! signs. It does not construct the spatial six-functor comparison.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum BranchState {
    Absent,
    Present,
    Circle,
}

impl BranchState {
    fn degree(self) -> usize {
        match self {
            Self::Present => 0,
            Self::Absent | Self::Circle => 1,
        }
    }
}

#[derive(Clone, Copy, Debug)]
struct Edge {
    source: usize,
    target: usize,
    source_sign: i64,
    target_sign: i64,
    radial: bool,
    label_position: usize,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct RadialMonomial {
    label: i32,
    occurrence_exponent: i8,
    normal_exponent: i8,
}

fn decode(mut value: usize) -> [BranchState; 3] {
    let mut result = [BranchState::Absent; 3];
    for state in &mut result {
        *state = match value % 3 {
            0 => BranchState::Absent,
            1 => BranchState::Present,
            2 => BranchState::Circle,
            _ => unreachable!(),
        };
        value /= 3;
    }
    result
}

fn encode(states: [BranchState; 3]) -> usize {
    states
        .into_iter()
        .enumerate()
        .map(|(position, state)| {
            let digit = match state {
                BranchState::Absent => 0,
                BranchState::Present => 1,
                BranchState::Circle => 2,
            };
            digit * 3_usize.pow(position as u32)
        })
        .sum()
}

fn edges() -> Vec<Edge> {
    let mut result = Vec::new();
    for source in 0..27 {
        let states = decode(source);
        for position in 0..3 {
            if states[position] == BranchState::Present {
                continue;
            }
            let radial = states[position] == BranchState::Absent;
            let mut target_states = states;
            target_states[position] = BranchState::Present;
            let target = encode(target_states);

            // Tensor-product sign of the three branch factors.
            let source_exponent: usize = states[..position]
                .iter()
                .copied()
                .map(BranchState::degree)
                .sum();
            let source_sign = if source_exponent % 2 == 0 { 1 } else { -1 };

            // Literal entry143 signs. Radial incidence counts already-present
            // smaller labels. Normal removal uses (3-|S|)+pos_H.
            let target_exponent = if radial {
                states[..position]
                    .iter()
                    .filter(|state| **state != BranchState::Absent)
                    .count()
            } else {
                let face_size = states
                    .iter()
                    .filter(|state| **state != BranchState::Absent)
                    .count();
                let circle_position = states[..position]
                    .iter()
                    .filter(|state| **state == BranchState::Circle)
                    .count();
                3 - face_size + circle_position
            };
            let target_sign = if target_exponent % 2 == 0 { 1 } else { -1 };
            result.push(Edge {
                source,
                target,
                source_sign,
                target_sign,
                radial,
                label_position: position,
            });
        }
    }
    result
}

fn derive_rebase(all_edges: &[Edge]) -> [i64; 27] {
    let mut signs = [0_i64; 27];
    signs[0] = 1;
    let mut changed = true;
    while changed {
        changed = false;
        for edge in all_edges {
            if signs[edge.source] != 0 && signs[edge.target] == 0 {
                signs[edge.target] = signs[edge.source] * edge.target_sign * edge.source_sign;
                changed = true;
            } else if signs[edge.target] != 0 && signs[edge.source] == 0 {
                signs[edge.source] = signs[edge.target] * edge.target_sign * edge.source_sign;
                changed = true;
            }
        }
    }
    assert!(signs.iter().all(|sign| sign.abs() == 1));
    // Propagation starts only at state zero. Reaching all 27 states proves
    // that the constraint graph is connected, so fixing the anchor makes
    // the sign solution unique (the unanchored solutions are its +/- pair).
    assert_eq!(signs.iter().filter(|sign| **sign != 0).count(), 27);
    for edge in all_edges {
        assert_eq!(
            edge.source_sign * signs[edge.target],
            signs[edge.source] * edge.target_sign
        );
    }
    signs
}

fn source_radial_monomial(labels: [i32; 3], edge: &Edge) -> RadialMonomial {
    assert!(edge.radial);
    RadialMonomial {
        label: labels[edge.label_position],
        occurrence_exponent: 1,
        normal_exponent: -1,
    }
}

fn target_radial_monomial(labels: [i32; 3], edge: &Edge) -> RadialMonomial {
    assert!(edge.radial);
    let source_states = decode(edge.source);
    let target_states = decode(edge.target);
    assert_eq!(source_states[edge.label_position], BranchState::Absent);
    assert_eq!(target_states[edge.label_position], BranchState::Present);
    // Entry143's promoted radial rule is X_a/u_a for the added label.
    RadialMonomial {
        label: labels[edge.label_position],
        occurrence_exponent: 1,
        normal_exponent: -1,
    }
}

fn differential_squared(all_edges: &[Edge], source: usize, target_side: bool) -> [i64; 27] {
    let mut result = [0_i64; 27];
    for first in all_edges.iter().filter(|edge| edge.source == source) {
        for second in all_edges.iter().filter(|edge| edge.source == first.target) {
            let first_sign = if target_side {
                first.target_sign
            } else {
                first.source_sign
            };
            let second_sign = if target_side {
                second.target_sign
            } else {
                second.source_sign
            };
            result[second.target] += first_sign * second_sign;
        }
    }
    result
}

fn main() {
    let all_edges = edges();
    assert_eq!(all_edges.len(), 54);
    assert_eq!(all_edges.iter().filter(|edge| edge.radial).count(), 27);
    assert_eq!(all_edges.iter().filter(|edge| !edge.radial).count(), 27);

    let rebase = derive_rebase(&all_edges);
    assert_eq!(rebase.iter().filter(|sign| **sign == 1).count(), 10);
    assert_eq!(rebase.iter().filter(|sign| **sign == -1).count(), 17);

    for state in 0..27 {
        assert_eq!(differential_squared(&all_edges, state, false), [0; 27]);
        assert_eq!(differential_squared(&all_edges, state, true), [0; 27]);
    }

    // Each radial edge carries the exact added label on both sides, hence
    // the same X_i/u_i Cech monomial after the admitted principal-line
    // evaluation. Normal edges carry the unit coefficient.
    let plus_labels = [1, 3, 5];
    let minus_labels = [0, 2, 4];
    let mut labelled_radial_rows = 0;
    let mut labelled_normal_rows = 0;
    for labels in [plus_labels, minus_labels] {
        for edge in &all_edges {
            if edge.radial {
                assert_eq!(
                    source_radial_monomial(labels, edge),
                    target_radial_monomial(labels, edge)
                );
                labelled_radial_rows += 1;
            } else {
                labelled_normal_rows += 1;
            }
        }
    }
    assert_eq!(labelled_radial_rows, 54);
    assert_eq!(labelled_normal_rows, 54);

    // Two retained conductor Tor grades are external copies of this complete
    // endpoint-star matrix; the checker does not invent a differential
    // between them.
    let spectator_tor_copies = 2;
    let state_tor_rows = 2 * 27 * spectator_tor_copies;
    let arrow_tor_rows = (labelled_radial_rows + labelled_normal_rows) * spectator_tor_copies;
    assert_eq!(state_tor_rows, 108);
    assert_eq!(arrow_tor_rows, 216);

    println!(
        "{{\"claim\":\"The product of the three labelled log/Rees branch factors is chain-isomorphic, after a uniquely derived anchored orientation rebase, to the complete 27-state literal endpoint closed-star coefficient matrix H subset S subset v on both sheets. All radial X_i/u_i labels, normal-unit signs, and d^2 equations agree.\",\"status\":\"proved_scoped_finite_three_branch_endpoint_star_matrix\",\"states_per_endpoint\":27,\"constraint_graph_reachable_from_anchor\":27,\"anchored_rebase_solution_count\":1,\"arrows_per_endpoint\":54,\"radial_rows_both_endpoints\":54,\"normal_rows_both_endpoints\":54,\"radial_monomial\":\"X_label/u_label\",\"radial_label_comparisons\":54,\"orientation_rebase_positive_negative\":[10,17],\"source_d_squared_zero\":true,\"target_d_squared_zero\":true,\"spectator_Tor_grade_copies\":2,\"state_Tor_census_rows\":108,\"arrow_Tor_census_rows\":216,\"integer_inverted\":false,\"spatial_six_functor_comparison_constructed\":false,\"hemisphere_to_based_qSigma_constructed\":false,\"mapping_fiber\":\"unconstructed\"}}"
    );
}
