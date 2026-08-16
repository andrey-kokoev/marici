use std::collections::BTreeSet;

type Diagonal = (u8, u8);
type Face = BTreeSet<Diagonal>;
type Ray = (usize, i8);

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

fn anchors(ray: Ray) -> BTreeSet<Face> {
    let (plus, minus) = road_halves(ray.0);
    let path = if ray.1 > 0 { plus } else { minus };
    [path[0].clone(), path[2].clone()].into_iter().collect()
}

fn main() {
    let rays = (0..3)
        .flat_map(|axis| [(axis, -1_i8), (axis, 1_i8)])
        .collect::<Vec<_>>();
    let mut admissible = 0;
    let mut sheetwise = 0;
    let mut cross_sheet = 0;
    let mut shared_anchor_edges = 0;
    let mut cross_sheet_empty = 0;
    let mut forbidden_opposites_shared = 0;

    for i in 0..rays.len() {
        for j in (i + 1)..rays.len() {
            let left = rays[i];
            let right = rays[j];
            let common = anchors(left)
                .intersection(&anchors(right))
                .cloned()
                .collect::<BTreeSet<_>>();
            if left.0 == right.0 {
                assert_eq!(left.1, -right.1);
                assert_eq!(common.len(), 1);
                forbidden_opposites_shared += 1;
                continue;
            }

            admissible += 1;
            if left.1 == right.1 {
                sheetwise += 1;
                assert_eq!(common.len(), 1);
                shared_anchor_edges += 1;
            } else {
                cross_sheet += 1;
                assert!(common.is_empty());
                cross_sheet_empty += 1;
            }
        }
    }

    assert_eq!(admissible, 12);
    assert_eq!(sheetwise, 6);
    assert_eq!(cross_sheet, 6);
    assert_eq!(shared_anchor_edges, 6);
    assert_eq!(cross_sheet_empty, 6);
    assert_eq!(forbidden_opposites_shared, 3);

    println!(
        "{{\"status\":\"falsified_scoped_existing_half_gallery_cross_sheet_gluing\",\"toric_two_cones\":12,\"sheetwise_two_cones\":6,\"sheetwise_shared_anchor\":6,\"cross_sheet_two_cones\":6,\"cross_sheet_shared_anchor\":0,\"forbidden_opposite_ray_pairs\":3,\"forbidden_pairs_shared_center\":3,\"existing_half_gallery_concatenation_constructs_cross_sheet_edges\":false,\"new_cross_sheet_bridge_correspondences_required\":6,\"global_maximal_cone_gluing_constructed\":false,\"mapping_fiber_instantiated\":false}}"
    );
}
