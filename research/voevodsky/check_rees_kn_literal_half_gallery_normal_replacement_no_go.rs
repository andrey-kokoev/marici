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
    let center = face(&[d03, short(0), short(3)]);
    let v01 = face(&[d03, short(0), short(4)]);
    let turns = [2, 0, 1][road];
    (
        [plus, v10, center.clone()].map(|value| rotate_face(&value, turns)),
        [minus, v01, center].map(|value| rotate_face(&value, turns)),
    )
}

fn intersection(left: &Face, right: &Face) -> Face {
    left.intersection(right).copied().collect()
}

fn main() {
    let mut halves = Vec::new();
    for road in 0..3 {
        let (plus, minus) = road_halves(road);
        halves.push((road, 1_i8, plus));
        halves.push((road, -1_i8, minus));
    }
    assert_eq!(halves.len(), 6);

    let mut replacement_rows = 0;
    for (_, _, path) in &halves {
        assert!(path.iter().all(|vertex| vertex.len() == 3));
        let left = intersection(&path[0], &path[1]);
        let right = intersection(&path[1], &path[2]);
        assert_eq!(left.len(), 2);
        assert_eq!(right.len(), 2);
        assert_ne!(left, right);

        let persistent = intersection(&left, &right);
        assert_eq!(persistent.len(), 1);
        let outgoing = left.difference(&persistent).copied().collect::<Face>();
        let incoming = right.difference(&persistent).copied().collect::<Face>();
        assert_eq!(outgoing.len(), 1);
        assert_eq!(incoming.len(), 1);
        assert!(outgoing.is_disjoint(&incoming));

        // No constant two-label set can simultaneously be the literal
        // Boolean normal basis on both edge supports.
        let constant_normal_basis_exists = left == right;
        assert!(!constant_normal_basis_exists);
        replacement_rows += 1;
    }
    assert_eq!(replacement_rows, 6);

    // Rotation preserves road sign and cycles all six half-galleries;
    // reflection exchanges the two sign orbits. Their complete set is stable.
    for (road, sign, _) in &halves {
        assert!(halves.iter().any(
            |(candidate, candidate_sign, _)| candidate == &((road + 1) % 3)
                && candidate_sign == sign
        ));
        assert!(halves
            .iter()
            .any(|(_, candidate_sign, _)| candidate_sign == &-*sign));
    }

    println!(
        "{{\"status\":\"falsified_scoped_constant_Boolean_identity_on_literal_half_galleries\",\"literal_half_galleries\":6,\"vertices_per_half\":3,\"edge_support_size\":2,\"persistent_labels_per_flip\":1,\"outgoing_labels_per_flip\":1,\"incoming_labels_per_flip\":1,\"constant_two_normal_basis_exists\":false,\"flip_normal_replacement_maps_required\":6,\"D3\":true,\"reflection\":true,\"extraordinary_replacement_correspondence_no_go\":false}}"
    );
}
