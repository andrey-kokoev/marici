use std::collections::{BTreeMap, BTreeSet};

type Diagonal = (u8, u8);
type Face = BTreeSet<Diagonal>;
type Edge = (usize, usize);

const ORDERED: [(usize, usize); 6] = [(0, 1), (0, 2), (1, 2), (1, 0), (2, 0), (2, 1)];

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

fn short_index(value: Diagonal) -> Option<usize> {
    (0..6).find(|index| short(*index) == value)
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

fn edge(a: usize, b: usize) -> Edge {
    if a < b {
        (a, b)
    } else {
        (b, a)
    }
}

fn main() {
    let vertices = ORDERED
        .into_iter()
        .map(|(left, right)| ordered_vertex(left, right))
        .collect::<Vec<_>>();
    assert_eq!(vertices.len(), 6);

    let mut short_fibres = BTreeMap::<usize, Vec<usize>>::new();
    for (sector, vertex) in vertices.iter().enumerate() {
        let short_labels = vertex
            .iter()
            .filter_map(|label| short_index(*label))
            .collect::<Vec<_>>();
        assert_eq!(short_labels.len(), 2);
        for label in short_labels {
            short_fibres.entry(label).or_default().push(sector);
        }
    }
    assert_eq!(short_fibres.len(), 6);
    assert!(short_fibres.values().all(|fibre| fibre.len() == 2));

    let literal_edges = short_fibres
        .values()
        .map(|fibre| edge(fibre[0], fibre[1]))
        .collect::<BTreeSet<_>>();
    let dp6_boundary_edges = (0..6)
        .map(|sector| edge(sector, (sector + 1) % 6))
        .collect::<BTreeSet<_>>();

    assert_eq!(literal_edges.len(), 6);
    assert_eq!(dp6_boundary_edges.len(), 6);
    assert!(literal_edges.is_disjoint(&dp6_boundary_edges));
    assert!(literal_edges.iter().all(|(a, b)| a % 2 == b % 2));
    assert!(dp6_boundary_edges.iter().all(|(a, b)| a % 2 != b % 2));

    let union = literal_edges
        .union(&dp6_boundary_edges)
        .copied()
        .collect::<BTreeSet<_>>();
    assert_eq!(union.len(), 12);
    let opposite = (0..3).map(|i| edge(i, i + 3)).collect::<BTreeSet<_>>();
    let complete = (0..6)
        .flat_map(|a| ((a + 1)..6).map(move |b| edge(a, b)))
        .collect::<BTreeSet<_>>();
    assert_eq!(
        union,
        complete
            .difference(&opposite)
            .copied()
            .collect::<BTreeSet<_>>()
    );

    let faces = (0_u8..8)
        .map(|mask| {
            (0..3)
                .map(|pair| {
                    if mask & (1 << pair) == 0 {
                        pair
                    } else {
                        pair + 3
                    }
                })
                .collect::<BTreeSet<_>>()
        })
        .collect::<Vec<_>>();
    assert_eq!(faces.len(), 8);
    for face in &faces {
        assert_eq!(face.len(), 3);
        assert!(face.iter().enumerate().all(|(position, a)| face
            .iter()
            .skip(position + 1)
            .all(|b| union.contains(&edge(*a, *b)))));
    }
    for present in &union {
        assert_eq!(
            faces
                .iter()
                .filter(|face| face.contains(&present.0) && face.contains(&present.1))
                .count(),
            2
        );
    }
    assert_eq!(6_i32 - union.len() as i32 + faces.len() as i32, 2);

    println!(
        "{{\"status\":\"falsified_scoped_dp6_boundary_as_literal_facet_clutching\",\"ordered_sectors\":6,\"sector_short_incidences\":12,\"literal_short_facet_edges\":6,\"dp6_boundary_edges\":6,\"common_edges\":0,\"literal_edges_same_sheet\":true,\"dp6_edges_cross_sheet\":true,\"minimal_union_graph\":\"octahedral_K6_minus_matching\",\"union_edges\":12,\"octahedral_faces\":8,\"euler_characteristic\":2,\"octahedral_log_correspondence_constructed\":false,\"global_correspondence_no_go\":false}}"
    );
}
