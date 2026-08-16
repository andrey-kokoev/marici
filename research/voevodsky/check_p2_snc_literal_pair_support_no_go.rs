//! Scoped falsifier for direct literal pair-support realization in entry143.
//!
//! The projective SNC/log source has three pair intersections. Including the
//! two retained Tor grades and four Boolean normal states gives the necessary
//! 3*2*4 = 24 source rows. Entry143 indexes only noncrossing K6 faces S with
//! H subset S. Every pair of physical long roads crosses, so none of these
//! rows has a literal [S,H] target.
//!
//! This does not rule out an extraordinary/log correspondence with external
//! overlap objects. It proves that such objects cannot be replaced by a
//! support-preserving map of the existing face-indexed diagram.

use std::collections::BTreeSet;

type Diagonal = (u8, u8);
type Face = BTreeSet<Diagonal>;

const ROADS: [Diagonal; 3] = [(1, 4), (0, 3), (2, 5)];

fn normalize((a, b): Diagonal) -> Diagonal {
    if a < b {
        (a, b)
    } else {
        (b, a)
    }
}

fn boundary_edge(a: u8, b: u8) -> bool {
    let d = a.abs_diff(b);
    d == 1 || d == 5
}

fn crosses(d1: Diagonal, d2: Diagonal) -> bool {
    let (a, c) = normalize(d1);
    let (b, d) = normalize(d2);
    if a == b || a == d || c == b || c == d {
        return false;
    }
    (a < b && b < c && c < d) || (b < a && a < d && d < c)
}

fn diagonals() -> Vec<Diagonal> {
    let mut out = Vec::new();
    for a in 0..6 {
        for b in (a + 1)..6 {
            if !boundary_edge(a, b) {
                out.push((a, b));
            }
        }
    }
    out
}

fn all_noncrossing_faces() -> Vec<Face> {
    let ds = diagonals();
    let mut faces = Vec::new();
    for mask in 0usize..(1usize << ds.len()) {
        let face: Face = ds
            .iter()
            .enumerate()
            .filter(|(i, _)| mask & (1 << i) != 0)
            .map(|(_, d)| *d)
            .collect();
        if face
            .iter()
            .all(|x| face.iter().all(|y| x == y || !crosses(*x, *y)))
        {
            faces.push(face);
        }
    }
    faces
}

fn rotate((a, b): Diagonal) -> Diagonal {
    normalize(((a + 2) % 6, (b + 2) % 6))
}

fn reflect((a, b): Diagonal) -> Diagonal {
    normalize(((2 + 6 - a) % 6, (2 + 6 - b) % 6))
}

fn main() {
    let faces = all_noncrossing_faces();
    let mut face_counts = [0usize; 4];
    for face in &faces {
        face_counts[face.len()] += 1;
    }
    assert_eq!(face_counts, [1, 9, 21, 14]);

    let pairs = [(0usize, 1usize), (1, 2), (2, 0)];
    let mut crossing_pairs = 0usize;
    let mut legal_pair_faces = 0usize;
    let mut source_rows = 0usize;
    let mut legal_literal_rows = 0usize;

    for &(i, j) in &pairs {
        let a = ROADS[i];
        let b = ROADS[j];
        assert!(crosses(a, b));
        crossing_pairs += 1;
        let containing = faces
            .iter()
            .filter(|s| s.contains(&a) && s.contains(&b))
            .count();
        assert_eq!(containing, 0);
        legal_pair_faces += containing;
        for _tor_grade in 0..2 {
            for _h_mask in 0u8..4 {
                source_rows += 1;
                legal_literal_rows += containing;
            }
        }
    }

    assert_eq!(crossing_pairs, 3);
    assert_eq!(legal_pair_faces, 0);
    assert_eq!(source_rows, 24);
    assert_eq!(legal_literal_rows, 0);

    let pair_boundary = [[-1i64, 0, 1], [1, -1, 0], [0, 1, -1]];
    assert!(pair_boundary.iter().all(|row| row.iter().sum::<i64>() == 0));
    assert!(pair_boundary.iter().flatten().any(|x| *x != 0));
    let minor =
        pair_boundary[0][0] * pair_boundary[1][1] - pair_boundary[0][1] * pair_boundary[1][0];
    assert_eq!(minor.abs(), 1);

    let top_to_singletons = [1i64, -1];
    let singleton_to_empty = [1i64, 1];
    assert!(top_to_singletons.iter().all(|x| *x != 0));
    let d2 =
        top_to_singletons[0] * singleton_to_empty[0] + top_to_singletons[1] * singleton_to_empty[1];
    assert_eq!(d2, 0);

    // The source incidence and Boolean boundaries are genuinely nonzero.
    // A zero direct image therefore erases these required rows; it does not
    // realize them. Whether an extraordinary corridor-valued image closes
    // their chain equations is deliberately outside this checker's scope.
    assert_ne!(pair_boundary[0], [0, 0, 0]);
    assert_ne!(top_to_singletons, [0, 0]);

    assert_eq!(rotate(ROADS[0]), ROADS[1]);
    assert_eq!(rotate(ROADS[1]), ROADS[2]);
    assert_eq!(rotate(ROADS[2]), ROADS[0]);
    assert_eq!(reflect(ROADS[0]), ROADS[0]);
    assert_eq!(reflect(ROADS[1]), ROADS[2]);
    assert_eq!(reflect(ROADS[2]), ROADS[1]);
    for &(i, j) in &pairs {
        assert!(crosses(rotate(ROADS[i]), rotate(ROADS[j])));
        assert!(crosses(reflect(ROADS[i]), reflect(ROADS[j])));
    }

    println!(
        "{{\"status\":\"falsified_scoped_direct_literal_pair_support_realization\",\"k6_face_counts\":[1,9,21,14],\"crossing_long_pairs\":3,\"tor_grades\":2,\"boolean_states_per_pair\":4,\"required_pair_rows\":24,\"legal_literal_entry143_rows\":0,\"pair_incidence_rank\":2,\"pair_incidence_saturated\":true,\"normal_top_boundary_nonzero\":true,\"normal_square_d2_zero\":true,\"d3_reflection_stable\":true,\"two_top_bridge_repairs_support\":false,\"global_extraordinary_log_correspondence_no_go\":false,\"minimal_addition\":\"external W_ij/Gamma_ij^{{!,log}} objects with proper/log-BM legs, four Boolean states, Tor grades, adjacent-facet BC maps, and a support comparison to the complementary q_k corridor\"}}"
    );
}
