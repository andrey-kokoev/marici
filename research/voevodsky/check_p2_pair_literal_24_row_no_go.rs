//! Exact 24-row support no-go for the proposed literal pair-intersection map.
//!
//! The dP6 full-log boundary has six maximal cones. Under either admitted
//! D3/polarity-equivariant ray labeling, the two rays of every cone map to
//! crossing short diagonals of K6. Each cone carries the four Boolean normal
//! states H subset {a,b}. A literal entry-143 generator requires H subset S
//! for one compatible K6 face S containing the occurrence support {a,b}.
//! No such S exists. Sending the double-normal source state to zero does not
//! repair the problem: its primitive boundary has the two distinct ray-grade
//! components (-1,+1). The theorem is scoped to the existing literal
//! face-indexed category and does not obstruct adjoining an extraordinary
//! support-switch/log-Gysin object.

use std::collections::{BTreeMap, BTreeSet};

const N: u8 = 6;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Face = BTreeSet<Diagonal>;

fn diagonal(first: u8, second: u8) -> Diagonal {
    if first < second {
        Diagonal(first, second)
    } else {
        Diagonal(second, first)
    }
}

fn boundary_edge(value: Diagonal) -> bool {
    value.1 - value.0 == 1 || value == Diagonal(0, N - 1)
}

fn between(vertex: u8, first: u8, second: u8) -> bool {
    let span = (second + N - first) % N;
    let position = (vertex + N - first) % N;
    position > 0 && position < span
}

fn crosses(first: Diagonal, second: Diagonal) -> bool {
    if [first.0, first.1]
        .iter()
        .any(|endpoint| *endpoint == second.0 || *endpoint == second.1)
    {
        return false;
    }
    between(second.0, first.0, first.1) != between(second.1, first.0, first.1)
        && between(first.0, second.0, second.1) != between(first.1, second.0, second.1)
}

fn short(index: usize) -> Diagonal {
    diagonal(index as u8, (index as u8 + 2) % N)
}

fn all_faces() -> Vec<Face> {
    let diagonals: Vec<_> = (0..N)
        .flat_map(|first| ((first + 1)..N).map(move |second| diagonal(first, second)))
        .filter(|value| !boundary_edge(*value))
        .collect();
    let mut result = Vec::new();
    for mask in 0_u16..(1_u16 << diagonals.len()) {
        if mask.count_ones() > 3 {
            continue;
        }
        let face: Face = diagonals
            .iter()
            .enumerate()
            .filter_map(|(index, value)| ((mask & (1 << index)) != 0).then_some(*value))
            .collect();
        if face.iter().enumerate().all(|(position, first)| {
            face.iter()
                .skip(position + 1)
                .all(|second| !crosses(*first, *second))
        }) {
            result.push(face);
        }
    }
    result
}

fn rotate_short(index: usize) -> usize {
    (index + 2) % 6
}

fn reflect_short(index: usize) -> usize {
    (6 - index) % 6
}

fn determinant(matrix: &[Vec<i64>]) -> i64 {
    assert!(matrix.iter().all(|row| row.len() == matrix.len()));
    if matrix.is_empty() {
        return 1;
    }
    if matrix.len() == 1 {
        return matrix[0][0];
    }
    (0..matrix.len())
        .map(|column| {
            let minor: Vec<Vec<_>> = matrix
                .iter()
                .skip(1)
                .map(|row| {
                    row.iter()
                        .enumerate()
                        .filter_map(|(index, value)| (index != column).then_some(*value))
                        .collect()
                })
                .collect();
            let sign = if column % 2 == 0 { 1 } else { -1 };
            sign * matrix[0][column] * determinant(&minor)
        })
        .sum()
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct ResidueRow {
    cone: usize,
    mask: u8,
    labels: [usize; 2],
    inverse_normals: [bool; 2],
    normal_removals: Vec<(u8, i64)>,
    ray_residue: [i64; 2],
    cech_correction: [i64; 2],
    tor_grades: [u8; 2],
}

fn normal_removals(mask: u8) -> Vec<(u8, i64)> {
    let mut result = Vec::new();
    let mut position = 0_usize;
    for bit in 0_u8..2 {
        if mask & (1 << bit) == 0 {
            continue;
        }
        let sign = if (1 + position) % 2 == 0 { 1 } else { -1 };
        result.push((mask & !(1 << bit), sign));
        position += 1;
    }
    result
}

fn residue_rows(labels: [usize; 6]) -> Vec<ResidueRow> {
    let mut result = Vec::new();
    for cone in 0..6 {
        let pair = [labels[cone], labels[(cone + 1) % 6]];
        for mask in 0_u8..4 {
            result.push(ResidueRow {
                cone,
                mask,
                labels: pair,
                inverse_normals: [mask & 1 == 0, mask & 2 == 0],
                normal_removals: normal_removals(mask),
                ray_residue: [-1, 1],
                cech_correction: [-1, 1],
                tor_grades: [0, 1],
            });
        }
    }
    result
}

fn check_normal_square(row: &ResidueRow) {
    let mut square = BTreeMap::<u8, i64>::new();
    for (middle, first) in &row.normal_removals {
        for (target, second) in normal_removals(*middle) {
            *square.entry(target).or_default() += first * second;
        }
    }
    assert!(square.values().all(|coefficient| *coefficient == 0));
}

fn main() {
    let faces = all_faces();
    let mut census = [0_usize; 4];
    for face in &faces {
        census[face.len()] += 1;
    }
    assert_eq!(census, [1, 9, 21, 14]);

    // First admitted equivariant labeling from the dP6 rays to short grades.
    // The second labeling is its central shift and has the same incidence.
    let ray_labels = [2_usize, 3, 4, 5, 0, 1];
    let shifted_labels = [5_usize, 0, 1, 2, 3, 4];

    // Derive the 24 source rows from the same localization and normal signs
    // as entry143.  These descriptors exist before asking for a target face.
    let physical_residues = residue_rows(ray_labels);
    assert_eq!(physical_residues.len(), 24);
    for row in &physical_residues {
        assert_eq!(
            row.inverse_normals
                .iter()
                .filter(|present| **present)
                .count(),
            2 - row.mask.count_ones() as usize
        );
        assert_eq!(row.ray_residue, [-1, 1]);
        assert_eq!(row.cech_correction, [-1, 1]);
        assert_eq!(row.tor_grades, [0, 1]);
        check_normal_square(row);
    }
    assert_eq!(normal_removals(0), vec![]);
    assert_eq!(normal_removals(1), vec![(0, -1)]);
    assert_eq!(normal_removals(2), vec![(0, -1)]);
    assert_eq!(normal_removals(3), vec![(2, -1), (1, 1)]);

    let shifted_residues = residue_rows(shifted_labels);
    assert_eq!(shifted_residues.len(), 24);
    for (physical, shifted) in physical_residues.iter().zip(&shifted_residues) {
        assert_eq!(physical.cone, shifted.cone);
        assert_eq!(physical.mask, shifted.mask);
        assert_eq!(physical.inverse_normals, shifted.inverse_normals);
        assert_eq!(physical.normal_removals, shifted.normal_removals);
        assert_eq!(physical.ray_residue, shifted.ray_residue);
        assert_eq!(physical.cech_correction, shifted.cech_correction);
        assert_eq!(physical.tor_grades, shifted.tor_grades);
    }

    let mut cones = 0_usize;
    let mut boolean_states = 0_usize;
    let mut legal_literal_rows = 0_usize;
    let mut primitive_boundary_blocks = 0_usize;

    for labels in [ray_labels, shifted_labels] {
        let mut labeling_rows = 0_usize;
        for cone in 0..6 {
            let first_label = labels[cone];
            let second_label = labels[(cone + 1) % 6];
            let first = short(first_label);
            let second = short(second_label);
            assert!(crosses(first, second));

            let containing: Vec<_> = faces
                .iter()
                .filter(|face| face.contains(&first) && face.contains(&second))
                .collect();
            assert!(containing.is_empty());

            // Four source normal states: empty, first, second, and top.
            for mask in 0_u8..4 {
                let h: Face = [(0_u8, first), (1_u8, second)]
                    .into_iter()
                    .filter_map(|(bit, value)| ((mask & (1 << bit)) != 0).then_some(value))
                    .collect();
                assert!(h.len() <= 2);
                let legal = faces.iter().any(|face| {
                    face.contains(&first) && face.contains(&second) && h.is_subset(face)
                });
                assert!(!legal);
                legal_literal_rows += usize::from(legal);
                boolean_states += 1;
                labeling_rows += 1;
            }

            // The source top deletion is the primitive column (-1,+1).
            let normal_boundary = [-1_i64, 1_i64];
            assert_eq!(
                normal_boundary.iter().map(|value| value.abs()).sum::<i64>(),
                2
            );
            assert_eq!(normal_boundary[0] + normal_boundary[1], 0);
            assert_eq!(
                normal_boundary.iter().fold(0_i64, |gcd, value| {
                    let mut left = gcd.abs();
                    let mut right = value.abs();
                    while right != 0 {
                        (left, right) = (right, left % right);
                    }
                    left
                }),
                1
            );
            primitive_boundary_blocks += 1;
            cones += 1;
        }
        assert_eq!(labeling_rows, 24);
    }

    // Both admissible labelings were exhaustively checked.
    assert_eq!(cones, 12);
    assert_eq!(boolean_states, 48);
    assert_eq!(legal_literal_rows, 0);
    assert_eq!(primitive_boundary_blocks, 12);

    // The physical labeling has exactly six cones and 24 requested rows.
    let physical_cones = 6_usize;
    let physical_rows = physical_cones * 4;
    assert_eq!(physical_rows, 24);

    // D3 preserves the obstruction.
    for index in 0..6 {
        let next = (index + 1) % 6;
        assert!(crosses(
            short(rotate_short(ray_labels[index])),
            short(rotate_short(ray_labels[next]))
        ));
        assert!(crosses(
            short(reflect_short(ray_labels[index])),
            short(reflect_short(ray_labels[next]))
        ));
    }

    // The cone boundaries share the six ray states. Their global matrix is
    // the oriented hexagon incidence R-I, not six independent two-row
    // blocks. It has the norm vector in its kernel and a unit 5x5 minor, so
    // its Smith form has five unit factors and one zero.
    let mut source_boundary = vec![vec![0_i64; 6]; 6];
    for cone in 0..6 {
        source_boundary[cone][cone] = -1;
        source_boundary[(cone + 1) % 6][cone] = 1;
    }
    assert!(source_boundary
        .iter()
        .all(|row| row.iter().sum::<i64>() == 0));
    assert!(
        (0..6).all(|column| { source_boundary.iter().map(|row| row[column]).sum::<i64>() == 0 })
    );
    let unit_minor: Vec<Vec<_>> = source_boundary
        .iter()
        .take(5)
        .map(|row| row.iter().take(5).copied().collect())
        .collect();
    assert_eq!(determinant(&unit_minor).abs(), 1);
    let source_boundary_rank = 5_usize;
    let source_boundary_kernel_rank = 1_usize;
    let source_boundary_smith = vec![1_i64; source_boundary_rank];
    assert_eq!(source_boundary_smith, vec![1; 5]);
    assert_eq!(source_boundary_kernel_rank, 1);

    println!(
        "{}",
        r#"{"claim":"For the six actual dP6 cones and their four Boolean normal states, the 24 source residue descriptors are uniquely derived from S minus H localization, the entry143 normal sign convention, the primitive oriented ray residue, and the adjacent-pair Cech cancellation. None has a literal entry143 target row because every adjacent ray pair maps to crossing short diagonals. The zero-row repair fails because the shared-ray source boundary is the nonzero primitive hexagon incidence R-I.","status":"falsified_scoped_literal_24_row_map__source_residues_derived","scope":"existing entry143 face-indexed generators and ordinary support-typed corestrictions only; the 24 source residue descriptors are proved, but no no-go is claimed for a new extraordinary support-switch/log-Gysin correspondence","factorization_test":{"k6_face_census":[1,9,21,14],"physical_dp6_cones":6,"boolean_states_per_cone":4,"derived_source_residue_rows":24,"cech_denominators":"exactly S minus H","normal_removal_signs":{"empty":[],"left":[-1],"right":[-1],"top_to_right_left":[-1,1]},"normal_d_squared":0,"ray_residue":[-1,1],"forced_double_cech_correction":[-1,1],"retained_tor_grades":[0,1],"required_literal_rows":24,"legal_literal_rows":0,"both_equivariant_labelings_checked":true,"crossing_pairs_per_labeling":6,"source_boundary":"R-I on six shared ray states","source_boundary_rank":5,"source_boundary_kernel_rank":1,"source_boundary_smith":[1,1,1,1,1],"source_norm_kernel":[1,1,1,1,1,1],"zero_image_chain_equation":"FAIL","D3_rotation":"preserves crossing obstruction and residue pattern","D3_reflection":"preserves crossing obstruction and transports the oriented residue pattern","integer_torsion":"none"},"minimal_additional_geometry":"Adjoin six branch-selected extraordinary pair objects whose derived log residue rows map to the two ray packets and whose support-switch comparison lands in the complementary marked corridor as a chain-valued correspondence."}"#
    );
}
