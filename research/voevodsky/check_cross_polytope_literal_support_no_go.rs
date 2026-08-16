use std::collections::BTreeSet;

type Diagonal = (u8, u8);
type Face = BTreeSet<Diagonal>;

const ORDERED: [(usize, usize); 6] = [(0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (2, 1)];
const SIGNED_AXIS: [(usize, i8); 6] = [(2, 1), (1, -1), (0, 1), (2, -1), (1, 1), (0, -1)];

fn diagonal(a: u8, b: u8) -> Diagonal {
    if a < b {
        (a, b)
    } else {
        (b, a)
    }
}

fn short(index: usize) -> Diagonal {
    diagonal(index as u8, (index as u8 + 2) % 6)
}

fn face(values: &[Diagonal]) -> Face {
    values.iter().copied().collect()
}

fn rotate_face(value: &Face, turns: usize) -> Face {
    value
        .iter()
        .map(|(a, b)| diagonal((a + 2 * turns as u8) % 6, (b + 2 * turns as u8) % 6))
        .collect()
}

fn road_halves(road: usize) -> ([Face; 3], [Face; 3]) {
    let d03 = diagonal(0, 3);
    let plus = face(&[short(1), short(3), short(5)]);
    let minus = face(&[short(0), short(2), short(4)]);
    let v10 = face(&[d03, short(1), short(3)]);
    let central = face(&[d03, short(0), short(3)]);
    let v01 = face(&[d03, short(0), short(4)]);
    let turns = [2, 0, 1][road];
    (
        [plus, v10, central.clone()].map(|value| rotate_face(&value, turns)),
        [minus, v01, central].map(|value| rotate_face(&value, turns)),
    )
}

fn intersection(left: &Face, right: &Face) -> Face {
    left.intersection(right).copied().collect()
}

fn ordered_vertex(left: usize, right: usize) -> Face {
    let road = (0..3)
        .find(|value| *value != left && *value != right)
        .unwrap();
    let positive = right == (left + 1) % 3;
    let (plus, minus) = road_halves(road);
    let half = if positive { plus } else { minus };
    let edge0 = intersection(&half[0], &half[1]);
    let edge1 = intersection(&half[1], &half[2]);
    edge0.union(&edge1).copied().collect()
}

fn vertex_for(axis: usize, sign: i8) -> usize {
    (0..6)
        .find(|vertex| SIGNED_AXIS[*vertex] == (axis, sign))
        .unwrap()
}

fn main() {
    let vertices = ORDERED
        .into_iter()
        .map(|(left, right)| ordered_vertex(left, right))
        .collect::<Vec<_>>();
    assert_eq!(vertices.len(), 6);

    let mut empty_pair_incidences = 0;
    let mut one_label_pair_incidences = 0;
    let mut empty_triple_supports = 0;
    let mut pure_faces = 0;
    let mut mixed_faces = 0;

    for mask in 0_u8..8 {
        let signs =
            std::array::from_fn::<_, 3, _>(
                |axis| {
                    if mask & (1 << axis) == 0 {
                        1_i8
                    } else {
                        -1_i8
                    }
                },
            );
        let selected = [
            vertex_for(0, signs[0]),
            vertex_for(1, signs[1]),
            vertex_for(2, signs[2]),
        ];
        let negative = signs.iter().filter(|sign| **sign < 0).count();
        if negative == 0 || negative == 3 {
            pure_faces += 1;
        } else {
            mixed_faces += 1;
        }

        for (a, b) in [
            (selected[0], selected[1]),
            (selected[0], selected[2]),
            (selected[1], selected[2]),
        ] {
            let common = intersection(&vertices[a], &vertices[b]);
            if signs[SIGNED_AXIS[a].0] == signs[SIGNED_AXIS[b].0] {
                assert_eq!(common.len(), 1);
                one_label_pair_incidences += 1;
            } else {
                assert!(common.is_empty());
                empty_pair_incidences += 1;
            }
        }

        let triple = intersection(
            &intersection(&vertices[selected[0]], &vertices[selected[1]]),
            &vertices[selected[2]],
        );
        assert!(triple.is_empty());
        empty_triple_supports += 1;
    }

    assert_eq!(pure_faces, 2);
    assert_eq!(mixed_faces, 6);
    assert_eq!(one_label_pair_incidences, 12);
    assert_eq!(empty_pair_incidences, 12);
    assert_eq!(empty_triple_supports, 8);
    // Each geometric edge occurs in two triangular faces.
    assert_eq!(one_label_pair_incidences / 2, 6);
    assert_eq!(empty_pair_incidences / 2, 6);

    println!(
        "{{\"status\":\"falsified_scoped_ordinary_face_poset_realization\",\"octahedral_faces\":8,\"pure_sheet_faces\":2,\"mixed_faces\":6,\"pair_incidences_with_one_label_support\":12,\"distinct_sheetwise_supported_edges\":6,\"pair_incidences_with_empty_support\":12,\"distinct_cross_sheet_unsupported_edges\":6,\"triple_support_empty_faces\":8,\"ordinary_cross_edge_corestrictions_exist\":false,\"ordinary_face_corestrictions_exist\":false,\"extraordinary_cross_edge_and_face_maps_required\":true,\"global_extraordinary_correspondence_no_go\":false}}"
    );
}
