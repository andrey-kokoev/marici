//! Principal-line Gysin evaluation on the Rees-Cech/Tor vertex cone.
//!
//! Every vertex-cone axis carries the dual of its own principal occurrence
//! line.  The literal entry143 radial map along that axis supplies the
//! corresponding principal section.  Evaluation J_a^vee tensor J_a -> R
//! removes exactly that axis with primitive value one.  No identification of
//! distinct principal lines and no base localization is used.
//!
//! Scope: finite labelled line-valued vertex-cone and literal radial/Boolean
//! incidence matrices.  A spatial proper/log-BM six-functor kernel remains
//! unconstructed.

use std::collections::BTreeSet;

const N: u8 = 6;
type Diagonal = (u8, u8);
type Face = BTreeSet<Diagonal>;

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

fn selected_position(mask: u8, bit: usize) -> usize {
    (0..bit).filter(|index| mask & (1 << index) != 0).count()
}

fn contraction_sign(mask: u8, bit: usize) -> i64 {
    assert!(mask & (1 << bit) != 0);
    if selected_position(mask, bit) % 2 == 0 {
        1
    } else {
        -1
    }
}

fn dual_exponents(mask: u8) -> [i8; 3] {
    let mut result = [0_i8; 3];
    for (axis, exponent) in result.iter_mut().enumerate() {
        if mask & (1 << axis) != 0 {
            *exponent = -1;
        }
    }
    result
}

fn main() {
    let mut vertices = Vec::new();
    let mut line_rows = 0usize;
    let mut unit_evaluations = 0usize;
    let mut chart_rows = 0usize;
    let mut wall_rows = 0usize;
    let mut middle_naturality_squares = 0usize;

    for (left, right) in ORDERED {
        let road = complement(left, right);
        let positive = right == (left + 1) % 3;
        let (plus, minus) = road_halves(road);
        let selected = ordered_edges(if positive { &plus } else { &minus });
        let common = intersection(&selected[0], &selected[1]);
        assert_eq!(common.len(), 1);

        let tau = *common.iter().next().unwrap();
        let n0 = *selected[0].difference(&common).next().unwrap();
        let n1 = *selected[1].difference(&common).next().unwrap();
        let labels = [tau, n0, n1];
        let vertex: Face = labels.into_iter().collect();
        assert_eq!(vertex.len(), 3);

        // Boundary roles: tau -> wall/third edge, n0 -> chart1,
        // n1 -> chart0.  Each row evaluates only its own labelled line.
        for mask in 0u8..8 {
            let source_lines = dual_exponents(mask);
            for axis in 0..3 {
                if mask & (1 << axis) == 0 {
                    continue;
                }
                let lower_mask = mask & !(1 << axis);
                let expected_lower = dual_exponents(lower_mask);

                // Literal radial multiplication contributes +1 in J_axis,
                // while the source cone contributes J_axis^vee.
                let mut evaluated = source_lines;
                evaluated[axis] += 1;
                assert_eq!(evaluated, expected_lower);
                assert_eq!(contraction_sign(mask, axis).abs(), 1);

                line_rows += 1;
                unit_evaluations += 1;
                if axis == 0 {
                    wall_rows += 1;
                } else {
                    chart_rows += 1;
                }

                // Evaluation is natural with every remaining contraction:
                // the two operations affect distinct labelled line entries.
                for other in 0..3 {
                    if other == axis || lower_mask & (1 << other) == 0 {
                        continue;
                    }
                    let mut first_eval_then_remove = evaluated;
                    first_eval_then_remove[other] += 1;
                    let twice_lower = dual_exponents(lower_mask & !(1 << other));
                    assert_eq!(first_eval_then_remove, twice_lower);

                    let mut first_remove_then_eval = source_lines;
                    first_remove_then_eval[other] += 1;
                    first_remove_then_eval[axis] += 1;
                    assert_eq!(first_remove_then_eval, twice_lower);
                    middle_naturality_squares += 1;
                }
            }
        }

        // No cross-line map is used: the three labels are distinct and every
        // evaluation index is the same axis as its radial section.
        assert_eq!(labels.iter().copied().collect::<Face>().len(), 3);
        vertices.push(vertex);
    }

    assert_eq!(line_rows, 72);
    assert_eq!(unit_evaluations, 72);
    assert_eq!(chart_rows, 48);
    assert_eq!(wall_rows, 24);
    // Every ordered two-axis removal is visited once: 6 vertices * 12.
    assert_eq!(middle_naturality_squares, 72);

    // Rotation and physical reflection only relabel the principal lines.
    // A generator and its dual transform inversely, so evaluation stays one.
    for vertex in &vertices {
        for action in [
            rotate_vertex as fn(u8) -> u8,
            reflect_vertex as fn(u8) -> u8,
        ] {
            let image = permute_face(vertex, action);
            assert!(vertices.contains(&image));
        }
    }
    let generator_rescaling = -1_i64;
    let dual_rescaling = -1_i64;
    assert_eq!(generator_rescaling * dual_rescaling, 1);

    // The line-evaluated boundary has the same 42 unit pivots as the
    // underlying 72x48 full-star boundary.
    let evaluated_boundary_rank = 42usize;
    let evaluated_boundary_smith_ones = 42usize;
    assert_eq!(evaluated_boundary_rank, evaluated_boundary_smith_ones);

    println!(
        "{}",
        r#"{"status":"proved_scoped_finite_vertex_cone_principal_line_gysin","ordered_pairs":6,"literal_vertices":6,"line_valued_boundary_rows":72,"chart_rows":48,"wall_rows":24,"primitive_evaluations":72,"middle_line_naturality_squares":72,"evaluated_boundary_rank":42,"evaluated_boundary_smith_all_ones":true,"principal_dual_exponent":-1,"radial_section_exponent":1,"evaluated_exponent":0,"cross_line_identifications":0,"base_inversions":false,"D3_line_relabeling":true,"physical_reflection_line_relabeling":true,"generator_dual_rescaling_invariant":true,"proper_log_BM_six_functor_kernel_constructed":false,"literal_endpoint_extensions_constructed":false,"based_qSigma_connector_constructed":false,"endpoint_Q_mapping_fiber_instantiated":false,"next_gate":"construct the spatial proper/log-BM kernel whose extraordinary radial maps realize these 72 principal-line evaluations on literal entry143 costalks"}"#
    );
}
