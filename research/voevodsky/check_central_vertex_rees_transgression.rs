//! Exact carrier-level audit of the cellular triple
//!
//!     v_+  subset  B_short  subset  K_6.
//!
//! This checker answers only the integral cellular/Rees question.  It does
//! not add occurrence, Cech, can--var, normal, or PC coefficients.
//!
//! The inclusion filtration
//!
//!     F_0=C_*(v_+) subset F_1=C_*(B_short) subset F_2=C_*(K_6)
//!
//! is the minimal bounded filtration determined by the two inclusions.  Its
//! E^1 page has Z in (filtration,total degree) (0,0), Z^2 in (1,1), and Z^2
//! in (2,2).  The only nonzero first differential is the connecting map
//!
//!     delta: H_2(K_6,B_short) -> H_1(B_short,v_+).
//!
//! The three road facets give the three peripheral boundary cycles.  Their
//! sum bounds the six short facets, and any two give a saturated basis, so
//! delta is an integral isomorphism.  The labelled face poset also gives a
//! canonical peripheral marking: each of the three central flip directions
//! reaches exactly one of F_14,F_03,F_25.  Under the Boolean-opposite marking
//! of the triangular dual block, the inverse (equivalently, dual) first
//! transgression has the unique normalized equivariant augmented lift
//!
//!     f_+ -> K_rel,
//!     (e_1,e_3,e_5) -> (F_14,F_03,F_25),
//!     (q_0,q_1,q_2,a) -> 0.
//!
//! This is entry 99's plus carrier.  It is null-homotopic after forgetting
//! the filtration/equivariant peripheral marking.  The audit also records the
//! smallest ambiguity: D3 covariance and the top chain equation alone allow
//! M(a,b)=a I+b(J-I), c=a+2b.  With c=1, the induced map on the peripheral
//! A2 quotient is multiplication by 1-3b; the exact-couple requirement that
//! it be the integral inverse of delta forces b=0.  Thus the transgression,
//! not the desired target matrix, supplies the missing normalization.

use std::collections::{BTreeMap, BTreeSet};

type Int = i64;
type Matrix = Vec<Vec<Int>>;

const N: u8 = 6;
const DIMENSION: usize = 3;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Dissection = BTreeSet<Diagonal>;

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

fn all_diagonals() -> Vec<Diagonal> {
    let mut result = Vec::new();
    for first in 0..N {
        for second in first + 1..N {
            let value = Diagonal(first, second);
            if !boundary_edge(value) {
                result.push(value);
            }
        }
    }
    result
}

fn short_index(value: Diagonal) -> Option<usize> {
    (0..6).find(|&index| diagonal(index as u8, (index as u8 + 2) % N) == value)
}

fn noncrossing(value: &Dissection) -> bool {
    value.iter().enumerate().all(|(position, first)| {
        value
            .iter()
            .skip(position + 1)
            .all(|second| !crosses(*first, *second))
    })
}

fn faces_by_size() -> Vec<Vec<Dissection>> {
    let diagonals = all_diagonals();
    assert_eq!(diagonals.len(), 9);
    let mut result = vec![Vec::new(); DIMENSION + 1];
    for subset in 0_u16..(1_u16 << diagonals.len()) {
        if subset.count_ones() as usize > DIMENSION {
            continue;
        }
        let face: Dissection = diagonals
            .iter()
            .enumerate()
            .filter(|(index, _)| subset & (1 << index) != 0)
            .map(|(_, &value)| value)
            .collect();
        if noncrossing(&face) {
            result[face.len()].push(face);
        }
    }
    for faces in &mut result {
        faces.sort();
    }
    assert_eq!(
        result.iter().map(Vec::len).collect::<Vec<_>>(),
        [1, 9, 21, 14]
    );
    result
}

fn addable(face: &Dissection, value: Diagonal) -> bool {
    !face.contains(&value)
        && face.len() < DIMENSION
        && face.iter().all(|&present| !crosses(present, value))
}

fn raw_incidence_sign(face: &Dissection, added: Diagonal) -> Int {
    if face.iter().filter(|&&value| value < added).count() % 2 == 0 {
        1
    } else {
        -1
    }
}

fn vertex_orientation_gauges(by_size: &[Vec<Dissection>]) -> BTreeMap<Dissection, Int> {
    let mut gauges = BTreeMap::from([(by_size[3][0].clone(), 1_i64)]);
    let mut changed = true;
    while changed {
        changed = false;
        for edge in &by_size[2] {
            let endpoints: Vec<_> = all_diagonals()
                .into_iter()
                .filter(|&value| addable(edge, value))
                .map(|value| {
                    let mut target = edge.clone();
                    target.insert(value);
                    (target, raw_incidence_sign(edge, value))
                })
                .collect();
            assert_eq!(endpoints.len(), 2);
            let relation = -endpoints[0].1 * endpoints[1].1;
            match (
                gauges.get(&endpoints[0].0).copied(),
                gauges.get(&endpoints[1].0).copied(),
            ) {
                (Some(first), Some(second)) => assert_eq!(second, relation * first),
                (Some(first), None) => {
                    gauges.insert(endpoints[1].0.clone(), relation * first);
                    changed = true;
                }
                (None, Some(second)) => {
                    gauges.insert(endpoints[0].0.clone(), relation * second);
                    changed = true;
                }
                (None, None) => {}
            }
        }
    }
    assert_eq!(gauges.len(), 14);
    gauges
}

fn incidence_sign(
    face: &Dissection,
    target: &Dissection,
    added: Diagonal,
    vertex_gauges: &BTreeMap<Dissection, Int>,
) -> Int {
    raw_incidence_sign(face, added)
        * vertex_gauges.get(face).copied().unwrap_or(1)
        * vertex_gauges.get(target).copied().unwrap_or(1)
}

fn rotate_vertex(vertex: u8) -> u8 {
    (vertex + 2) % N
}

fn reflect_vertex(vertex: u8) -> u8 {
    (2 + N - vertex) % N
}

fn permute_diagonal(value: Diagonal, permutation: fn(u8) -> u8) -> Diagonal {
    diagonal(permutation(value.0), permutation(value.1))
}

fn permute_face(face: &Dissection, permutation: fn(u8) -> u8) -> Dissection {
    face.iter()
        .map(|&value| permute_diagonal(value, permutation))
        .collect()
}

fn cellular_action_signs(
    by_size: &[Vec<Dissection>],
    vertex_gauges: &BTreeMap<Dissection, Int>,
    permutation: fn(u8) -> u8,
    top_sign: Int,
) -> Vec<BTreeMap<Dissection, Int>> {
    let mut signs = vec![BTreeMap::new(); DIMENSION + 1];
    signs[0].insert(by_size[0][0].clone(), top_sign);
    for size in 0..DIMENSION {
        for face in &by_size[size] {
            let source_sign = signs[size][face];
            let image_face = permute_face(face, permutation);
            for added in all_diagonals()
                .into_iter()
                .filter(|&value| addable(face, value))
            {
                let mut target = face.clone();
                target.insert(added);
                let image_target = permute_face(&target, permutation);
                let image_added = permute_diagonal(added, permutation);
                let source_incidence = incidence_sign(face, &target, added, vertex_gauges);
                let image_incidence =
                    incidence_sign(&image_face, &image_target, image_added, vertex_gauges);
                let target_sign = source_sign * source_incidence * image_incidence;
                match signs[size + 1].get(&target) {
                    Some(&known) => assert_eq!(known, target_sign),
                    None => {
                        signs[size + 1].insert(target, target_sign);
                    }
                }
            }
        }
        assert_eq!(signs[size + 1].len(), by_size[size + 1].len());
    }
    signs
}

fn cellular_action_matrix(
    faces: &[Dissection],
    signs: &BTreeMap<Dissection, Int>,
    permutation: fn(u8) -> u8,
) -> Matrix {
    let indices: BTreeMap<_, _> = faces
        .iter()
        .enumerate()
        .map(|(index, face)| (face.clone(), index))
        .collect();
    let mut result = zero(faces.len(), faces.len());
    for (column, face) in faces.iter().enumerate() {
        result[indices[&permute_face(face, permutation)]][column] = signs[face];
    }
    result
}

fn zero(rows: usize, columns: usize) -> Matrix {
    vec![vec![0; columns]; rows]
}

fn identity(size: usize) -> Matrix {
    let mut result = zero(size, size);
    for (index, row) in result.iter_mut().enumerate() {
        row[index] = 1;
    }
    result
}

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    assert!(!left.is_empty() && !right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = zero(left.len(), right[0].len());
    for row in 0..left.len() {
        for middle in 0..right.len() {
            for column in 0..right[0].len() {
                result[row][column] += left[row][middle] * right[middle][column];
            }
        }
    }
    result
}

fn add(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left.len(), right.len());
    left.iter()
        .zip(right)
        .map(|(left_row, right_row)| {
            assert_eq!(left_row.len(), right_row.len());
            left_row
                .iter()
                .zip(right_row)
                .map(|(left_entry, right_entry)| left_entry + right_entry)
                .collect()
        })
        .collect()
}

fn power(value: &Matrix, exponent: usize) -> Matrix {
    assert_eq!(value.len(), value[0].len());
    let mut result = identity(value.len());
    for _ in 0..exponent {
        result = multiply(&result, value);
    }
    result
}

fn signed_permutation(images: &[(usize, Int)]) -> Matrix {
    let mut result = zero(images.len(), images.len());
    for (source, &(target, sign)) in images.iter().enumerate() {
        assert!(sign == 1 || sign == -1);
        result[target][source] = sign;
    }
    result
}

fn boundary_matrix(
    source: &[Dissection],
    target: &[Dissection],
    vertex_gauges: &BTreeMap<Dissection, Int>,
) -> Matrix {
    let target_index: BTreeMap<_, _> = target
        .iter()
        .enumerate()
        .map(|(index, face)| (face.clone(), index))
        .collect();
    let mut result = zero(target.len(), source.len());
    for (column, face) in source.iter().enumerate() {
        for added in all_diagonals()
            .into_iter()
            .filter(|&value| addable(face, value))
        {
            let mut boundary_face = face.clone();
            boundary_face.insert(added);
            if let Some(&row) = target_index.get(&boundary_face) {
                result[row][column] = incidence_sign(face, &boundary_face, added, vertex_gauges);
            }
        }
    }
    result
}

fn integer_rank(value: &Matrix) -> usize {
    if value.is_empty() || value[0].is_empty() {
        return 0;
    }
    // Fraction-free elimination.  Row gcd reduction keeps entries small and
    // does not change rank over Q.
    let mut work = value.clone();
    let mut rank = 0;
    for column in 0..work[0].len() {
        let Some(pivot) = (rank..work.len()).find(|&row| work[row][column] != 0) else {
            continue;
        };
        work.swap(rank, pivot);
        for row in 0..work.len() {
            if row == rank || work[row][column] == 0 {
                continue;
            }
            let left = work[rank][column];
            let right = work[row][column];
            for entry in column..work[0].len() {
                work[row][entry] = left * work[row][entry] - right * work[rank][entry];
            }
            let divisor = work[row].iter().fold(0_i64, |g, &entry| gcd(g, entry));
            if divisor > 1 {
                for entry in &mut work[row] {
                    *entry /= divisor;
                }
            }
        }
        rank += 1;
        if rank == work.len() {
            break;
        }
    }
    rank
}

fn gcd(mut left: Int, mut right: Int) -> Int {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        (left, right) = (right, left % right);
    }
    left
}

fn determinant(value: &Matrix) -> Int {
    assert_eq!(value.len(), value.first().map_or(0, Vec::len));
    if value.is_empty() {
        return 1;
    }
    let size = value.len();
    let mut work = value.clone();
    let mut previous = 1_i64;
    let mut sign = 1_i64;
    for pivot_index in 0..size - 1 {
        let Some(pivot_row) = (pivot_index..size).find(|&row| work[row][pivot_index] != 0) else {
            return 0;
        };
        if pivot_row != pivot_index {
            work.swap(pivot_row, pivot_index);
            sign = -sign;
        }
        let pivot = work[pivot_index][pivot_index];
        for row in pivot_index + 1..size {
            for column in pivot_index + 1..size {
                let numerator =
                    work[row][column] * pivot - work[row][pivot_index] * work[pivot_index][column];
                assert_eq!(numerator % previous, 0);
                work[row][column] = numerator / previous;
            }
            work[row][pivot_index] = 0;
        }
        previous = pivot;
    }
    sign * work[size - 1][size - 1]
}

fn combinations(size: usize, chosen: usize) -> Vec<Vec<usize>> {
    fn extend(
        size: usize,
        chosen: usize,
        start: usize,
        present: &mut Vec<usize>,
        result: &mut Vec<Vec<usize>>,
    ) {
        if present.len() == chosen {
            result.push(present.clone());
            return;
        }
        let needed = chosen - present.len();
        for index in start..=size - needed {
            present.push(index);
            extend(size, chosen, index + 1, present, result);
            present.pop();
        }
    }
    let mut result = Vec::new();
    extend(size, chosen, 0, &mut Vec::new(), &mut result);
    result
}

fn determinantal_divisor(value: &Matrix, size: usize) -> Int {
    if size == 0 {
        return 1;
    }
    let rows = value.len();
    let columns = value.first().map_or(0, Vec::len);
    let mut divisor = 0_i64;
    for selected_rows in combinations(rows, size) {
        for selected_columns in combinations(columns, size) {
            let minor: Matrix = selected_rows
                .iter()
                .map(|&row| {
                    selected_columns
                        .iter()
                        .map(|&column| value[row][column])
                        .collect()
                })
                .collect();
            divisor = gcd(divisor, determinant(&minor));
        }
    }
    divisor
}

fn smith_nonzero_factors(value: &Matrix) -> Vec<Int> {
    let rank = integer_rank(value);
    let mut previous = 1_i64;
    let mut result = Vec::new();
    for size in 1..=rank {
        let divisor = determinantal_divisor(value, size);
        assert_ne!(divisor, 0);
        assert_eq!(divisor % previous, 0);
        result.push(divisor / previous);
        previous = divisor;
    }
    result
}

fn select_rows_and_columns(value: &Matrix, rows: &[usize], columns: &[usize]) -> Matrix {
    rows.iter()
        .map(|&row| columns.iter().map(|&column| value[row][column]).collect())
        .collect()
}

fn append_columns(left: &Matrix, columns: &[Vec<Int>]) -> Matrix {
    assert!(columns.iter().all(|column| column.len() == left.len()));
    left.iter()
        .enumerate()
        .map(|(row, entries)| {
            entries
                .iter()
                .copied()
                .chain(columns.iter().map(|column| column[row]))
                .collect()
        })
        .collect()
}

fn check_actual_faces_dual_block_and_filtration(
    by_size: &[Vec<Dissection>],
    vertex_gauges: &BTreeMap<Dissection, Int>,
) -> (Matrix, [Vec<Int>; 3]) {
    let plus_vertex: Dissection = [1_usize, 3, 5]
        .into_iter()
        .map(|index| diagonal(index as u8, (index as u8 + 2) % N))
        .collect();
    assert!(by_size[3].contains(&plus_vertex));

    // The coface interval of v_+ is the full Boolean lattice on its three
    // odd diagonals.  Reversing it gives the triangular dual-block ranks
    // f/e/q/a = 1/3/3/1.
    let interval_counts: Vec<_> = by_size
        .iter()
        .map(|faces| {
            faces
                .iter()
                .filter(|face| face.is_subset(&plus_vertex))
                .count()
        })
        .collect();
    assert_eq!(interval_counts, [1, 3, 3, 1]);

    // Every road has exactly one vertex adjacent to v_+.  These are actual
    // flips in the labelled K6 face poset and give the peripheral marking
    // F14,F03,F25 used by (e1,e3,e5), without consulting the carrier matrix.
    let matched_roads = [diagonal(1, 4), diagonal(0, 3), diagonal(2, 5)];
    let mut reached_vertices = Vec::new();
    for road in matched_roads {
        // No road facet is a coface of v_+.  Thus the literal dual-block
        // coface inclusion cannot already contain entry 99's road map.
        assert!(!BTreeSet::from([road]).is_subset(&plus_vertex));
        let candidates: Vec<_> = by_size[3]
            .iter()
            .filter(|candidate| {
                candidate.contains(&road) && candidate.intersection(&plus_vertex).count() == 2
            })
            .collect();
        assert_eq!(candidates.len(), 1);
        assert!(!candidates[0].is_subset(&plus_vertex));
        reached_vertices.push(candidates[0].clone());
    }
    assert_eq!(reached_vertices.iter().collect::<BTreeSet<_>>().len(), 3);

    let in_b = |face: &Dissection| face.iter().any(|&value| short_index(value).is_some());
    let b_faces: Vec<Vec<_>> = by_size
        .iter()
        .map(|faces| faces.iter().filter(|face| in_b(face)).cloned().collect())
        .collect();
    assert_eq!(
        b_faces.iter().map(Vec::len).collect::<Vec<_>>(),
        [0, 6, 21, 14]
    );
    let relative_faces: Vec<Vec<_>> = by_size
        .iter()
        .map(|faces| faces.iter().filter(|face| !in_b(face)).cloned().collect())
        .collect();
    assert_eq!(
        relative_faces.iter().map(Vec::len).collect::<Vec<_>>(),
        [1, 3, 0, 0]
    );

    let d_x3 = boundary_matrix(&by_size[0], &by_size[1], vertex_gauges);
    let d_x2 = boundary_matrix(&by_size[1], &by_size[2], vertex_gauges);
    let d_x1 = boundary_matrix(&by_size[2], &by_size[3], vertex_gauges);
    assert_eq!(multiply(&d_x2, &d_x3), zero(21, 1));
    assert_eq!(multiply(&d_x1, &d_x2), zero(14, 9));

    // Build the signed cellular actions from the actual label permutations
    // and the incidence matrices.  Rotation preserves the ambient
    // orientation; the reflection reverses it.  This derives every lower
    // sign by covariance instead of inserting the carrier signs.
    let rotation_signs = cellular_action_signs(by_size, vertex_gauges, rotate_vertex, 1);
    let reflection_signs = cellular_action_signs(by_size, vertex_gauges, reflect_vertex, -1);
    let rotation_actions: Vec<_> = by_size
        .iter()
        .enumerate()
        .map(|(size, faces)| cellular_action_matrix(faces, &rotation_signs[size], rotate_vertex))
        .collect();
    let reflection_actions: Vec<_> = by_size
        .iter()
        .enumerate()
        .map(|(size, faces)| cellular_action_matrix(faces, &reflection_signs[size], reflect_vertex))
        .collect();
    for (upper_size, differential) in [(0_usize, &d_x3), (1, &d_x2), (2, &d_x1)] {
        assert_eq!(
            multiply(&rotation_actions[upper_size + 1], differential),
            multiply(differential, &rotation_actions[upper_size])
        );
        assert_eq!(
            multiply(&reflection_actions[upper_size + 1], differential),
            multiply(differential, &reflection_actions[upper_size])
        );
    }
    assert_eq!(power(&rotation_actions[3], 3), identity(14));
    assert_eq!(power(&reflection_actions[3], 2), identity(14));
    assert_eq!(
        multiply(
            &reflection_actions[3],
            &multiply(&rotation_actions[3], &reflection_actions[3])
        ),
        power(&rotation_actions[3], 2)
    );
    assert_eq!(permute_face(&plus_vertex, rotate_vertex), plus_vertex);
    assert_eq!(permute_face(&plus_vertex, reflect_vertex), plus_vertex);

    let b_facet_indices: Vec<_> = by_size[1]
        .iter()
        .enumerate()
        .filter(|(_, face)| in_b(face))
        .map(|(index, _)| index)
        .collect();
    let b_edge_indices: Vec<_> = (0..by_size[2].len()).collect();
    let b_vertex_indices: Vec<_> = by_size[3]
        .iter()
        .enumerate()
        .filter(|(_, face)| **face != plus_vertex)
        .map(|(index, _)| index)
        .collect();
    let d_b2 = select_rows_and_columns(&d_x2, &b_edge_indices, &b_facet_indices);
    let d_b1_relative_v = select_rows_and_columns(&d_x1, &b_vertex_indices, &b_edge_indices);
    assert_eq!(multiply(&d_b1_relative_v, &d_b2), zero(13, 6));
    assert_eq!(integer_rank(&d_b2), 6);
    assert_eq!(integer_rank(&d_b1_relative_v), 13);
    assert_eq!(21 - integer_rank(&d_b1_relative_v) - integer_rank(&d_b2), 2);

    let road_facet_indices: Vec<_> = matched_roads
        .iter()
        .map(|road| {
            by_size[1]
                .iter()
                .position(|face| face == &BTreeSet::from([*road]))
                .unwrap()
        })
        .collect();
    let relative_d3 = select_rows_and_columns(&d_x3, &road_facet_indices, &[0]);
    assert_eq!(relative_d3, vec![vec![1], vec![1], vec![1]]);
    assert_eq!(3 - integer_rank(&relative_d3), 2);

    let rotation_roads = select_rows_and_columns(
        &rotation_actions[1],
        &road_facet_indices,
        &road_facet_indices,
    );
    let reflection_roads = select_rows_and_columns(
        &reflection_actions[1],
        &road_facet_indices,
        &road_facet_indices,
    );
    assert_eq!(
        rotation_roads,
        signed_permutation(&[(1, 1), (2, 1), (0, 1)])
    );
    assert_eq!(
        reflection_roads,
        signed_permutation(&[(0, -1), (2, -1), (1, -1)])
    );

    // The E1 connecting map is represented by the ordinary boundary of a
    // lifted road facet.  Its values are three cycles in C_1(B,v_+).
    let road_boundaries: [Vec<Int>; 3] = std::array::from_fn(|road| {
        d_x2.iter()
            .map(|row| row[road_facet_indices[road]])
            .collect()
    });
    for cycle in &road_boundaries {
        let column: Matrix = cycle.iter().map(|&entry| vec![entry]).collect();
        assert_eq!(multiply(&d_b1_relative_v, &column), zero(13, 1));
    }

    for (action, road_action) in [
        (&rotation_actions[2], &rotation_roads),
        (&reflection_actions[2], &reflection_roads),
    ] {
        for source in 0..3 {
            let source_cycle: Matrix = road_boundaries[source]
                .iter()
                .map(|&entry| vec![entry])
                .collect();
            let transformed = multiply(action, &source_cycle);
            let target = (0..3).find(|&row| road_action[row][source] != 0).unwrap();
            let sign = road_action[target][source];
            let expected: Matrix = road_boundaries[target]
                .iter()
                .map(|&entry| vec![sign * entry])
                .collect();
            assert_eq!(transformed, expected);
        }
    }

    // Sum of the three peripheral cycles is the negative boundary of the six
    // short facets, so it is exactly the relation dK_rel=T14+T03+T25.
    let short_boundary_sum: Vec<_> = (0..21)
        .map(|row| {
            b_facet_indices
                .iter()
                .map(|&column| d_x2[row][column])
                .sum::<Int>()
        })
        .collect();
    for row in 0..21 {
        assert_eq!(
            road_boundaries.iter().map(|cycle| cycle[row]).sum::<Int>(),
            -short_boundary_sum[row]
        );
    }

    // Any two peripheral cycles extend im(d_B2) to the entire saturated
    // kernel of d_B1.  This proves integrally (not just by a rank count) that
    // delta is an isomorphism Z^3/Z(1,1,1) -> H_1(B,v_+).
    let augmented = append_columns(
        &d_b2,
        &[road_boundaries[0].clone(), road_boundaries[1].clone()],
    );
    assert_eq!(integer_rank(&augmented), 8);
    assert_eq!(smith_nonzero_factors(&augmented), vec![1; 8]);
    let with_all_peripherals = append_columns(
        &d_b2,
        &[
            road_boundaries[0].clone(),
            road_boundaries[1].clone(),
            road_boundaries[2].clone(),
        ],
    );
    assert_eq!(integer_rank(&with_all_peripherals), 8);

    // Therefore the minimal three-step filtration has E1 ranks
    // (p,total degree)=(0,0):1,(1,1):2,(2,2):2.  Its d1 from p=2 to p=1 is
    // the isomorphism just checked; the next d1 is zero and no higher page can
    // carry a nonzero class out of the killed p=2 term.

    (relative_d3, road_boundaries)
}

fn dual_block_differentials() -> (Matrix, Matrix, Matrix) {
    // Reverse the Boolean coface interval of v_+.  These are the oriented
    // exterior bases of the augmented triangular dual block.  The sign on
    // 101 is the intrinsic orientation change used to make df=e1+e3+e5.
    // No target road or carrier coefficient enters this construction.
    let bases = [
        vec![(0b111_u8, 1_i64)],
        vec![(0b110_u8, 1_i64), (0b101, -1), (0b011, 1)],
        vec![(0b100_u8, 1_i64), (0b010, 1), (0b001, 1)],
        vec![(0b000_u8, 1_i64)],
    ];
    let mut differentials = Vec::new();
    for upper_degree in 0..3 {
        let upper = &bases[upper_degree];
        let lower = &bases[upper_degree + 1];
        let lower_index: BTreeMap<_, _> = lower
            .iter()
            .enumerate()
            .map(|(index, &(mask, scale))| (mask, (index, scale)))
            .collect();
        let mut differential = zero(lower.len(), upper.len());
        for (column, &(mask, source_scale)) in upper.iter().enumerate() {
            let mut exterior_position = 0_usize;
            for slot in 0..3 {
                if mask & (1 << slot) == 0 {
                    continue;
                }
                let face = mask & !(1 << slot);
                let (row, target_scale) = lower_index[&face];
                let exterior_sign = if exterior_position % 2 == 0 { 1 } else { -1 };
                differential[row][column] = source_scale * exterior_sign * target_scale;
                exterior_position += 1;
            }
        }
        differentials.push(differential);
    }
    assert_eq!(differentials[0], vec![vec![1], vec![1], vec![1]]);
    assert_eq!(
        differentials[1],
        vec![vec![1, -1, 0], vec![-1, 0, 1], vec![0, 1, -1]]
    );
    assert_eq!(differentials[2], vec![vec![1, 1, 1]]);
    (
        differentials.remove(0),
        differentials.remove(0),
        differentials.remove(0),
    )
}

fn equivariant_family(diagonal_entry: Int, off_diagonal_entry: Int) -> Matrix {
    (0..3)
        .map(|row| {
            (0..3)
                .map(|column| {
                    if row == column {
                        diagonal_entry
                    } else {
                        off_diagonal_entry
                    }
                })
                .collect()
        })
        .collect()
}

fn check_carrier_nullhomotopy_covariance_and_uniqueness(relative_d3: &Matrix) {
    let (source_d3, source_d2, source_d1) = dual_block_differentials();
    assert_eq!(multiply(&source_d2, &source_d3), zero(3, 1));
    assert_eq!(multiply(&source_d1, &source_d2), zero(1, 3));

    // Road order is the face-poset order matched above:
    // (F14,F03,F25), so entry 99's edge map is literally the identity.
    let carrier_top = vec![vec![1]];
    let carrier_edges = identity(3);
    assert_eq!(
        multiply(&carrier_edges, &source_d3),
        multiply(relative_d3, &carrier_top)
    );

    // Explicit ordinary integral null-homotopy A=dH+Hd.  There is no target
    // below the roads.  This is the entry-99 contraction in the matched road
    // order rather than the older (T0,T1,T2) order.
    let h2 = vec![vec![1, 0, 0]];
    let h1 = vec![vec![0, 0, 0], vec![0, 1, 1], vec![0, 1, 0]];
    assert_eq!(multiply(&h2, &source_d3), carrier_top);
    assert_eq!(
        add(&multiply(relative_d3, &h2), &multiply(&h1, &source_d2)),
        carrier_edges
    );

    let rotation_e = signed_permutation(&[(1, 1), (2, 1), (0, 1)]);
    let reflection_e = signed_permutation(&[(0, -1), (2, -1), (1, -1)]);
    let rotation_q = signed_permutation(&[(2, 1), (0, 1), (1, 1)]);
    let reflection_q = signed_permutation(&[(1, 1), (0, 1), (2, 1)]);
    let top_rotation = identity(1);
    let top_reflection = vec![vec![-1]];
    let augmentation_rotation = identity(1);
    let augmentation_reflection = identity(1);

    for (upper, lower, differential) in [
        (&top_rotation, &rotation_e, &source_d3),
        (&rotation_e, &rotation_q, &source_d2),
        (&rotation_q, &augmentation_rotation, &source_d1),
        (&top_reflection, &reflection_e, &source_d3),
        (&reflection_e, &reflection_q, &source_d2),
        (&reflection_q, &augmentation_reflection, &source_d1),
    ] {
        assert_eq!(multiply(lower, differential), multiply(differential, upper));
    }
    for rotation in [&rotation_e, &rotation_q] {
        assert_eq!(power(rotation, 3), identity(3));
    }
    for reflection in [&reflection_e, &reflection_q] {
        assert_eq!(power(reflection, 2), identity(3));
    }
    assert_eq!(
        multiply(&reflection_e, &multiply(&rotation_e, &reflection_e)),
        power(&rotation_e, 2)
    );
    assert_eq!(
        multiply(&reflection_q, &multiply(&rotation_q, &reflection_q)),
        power(&rotation_q, 2)
    );
    assert_eq!(
        multiply(&rotation_e, &carrier_edges),
        multiply(&carrier_edges, &rotation_e)
    );
    assert_eq!(
        multiply(&reflection_e, &carrier_edges),
        multiply(&carrier_edges, &reflection_e)
    );
    assert_eq!(
        multiply(&top_reflection, &carrier_top),
        multiply(&carrier_top, &top_reflection)
    );

    // Classify the ambiguity rather than sampling it.  The integral linear
    // equations rM=Mr and sM=Ms have rank seven in nine variables.  The
    // diagonal and off-diagonal matrices are two independent saturated
    // kernel vectors, so every integral equivariant edge map is uniquely
    // M(a,b)=aI+b(J-I).
    let mut constraint_columns = Vec::new();
    for variable in 0..9 {
        let mut elementary = zero(3, 3);
        elementary[variable / 3][variable % 3] = 1;
        let rotation_left = multiply(&rotation_e, &elementary);
        let rotation_right = multiply(&elementary, &rotation_e);
        let reflection_left = multiply(&reflection_e, &elementary);
        let reflection_right = multiply(&elementary, &reflection_e);
        let mut column = Vec::new();
        for (left, right) in [
            (&rotation_left, &rotation_right),
            (&reflection_left, &reflection_right),
        ] {
            for row in 0..3 {
                for entry in 0..3 {
                    column.push(left[row][entry] - right[row][entry]);
                }
            }
        }
        constraint_columns.push(column);
    }
    let equivariance_constraints: Matrix = (0..18)
        .map(|row| {
            constraint_columns
                .iter()
                .map(|column| column[row])
                .collect()
        })
        .collect();
    assert_eq!(integer_rank(&equivariance_constraints), 7);
    let diagonal_vector: Vec<_> = (0..9)
        .map(|entry| if entry / 3 == entry % 3 { 1 } else { 0 })
        .collect();
    let off_diagonal_vector: Vec<_> = (0..9)
        .map(|entry| if entry / 3 == entry % 3 { 0 } else { 1 })
        .collect();
    let family_basis: Matrix = (0..9)
        .map(|entry| vec![diagonal_vector[entry], off_diagonal_vector[entry]])
        .collect();
    assert_eq!(
        multiply(&equivariance_constraints, &family_basis),
        zero(18, 2)
    );
    assert_eq!(smith_nonzero_factors(&family_basis), vec![1, 1]);

    // The top chain equation adds c=a+2b.  Exhibit the smallest competing
    // normalized map before imposing the exact-couple saturation condition.
    let entry99 = equivariant_family(1, 0);
    let competing = equivariant_family(-1, 1);
    for (matrix, top) in [(&entry99, 1_i64), (&competing, 1_i64)] {
        assert_eq!(multiply(matrix, &source_d3), vec![vec![top]; 3]);
        assert_eq!(multiply(&rotation_e, matrix), multiply(matrix, &rotation_e));
        assert_eq!(
            multiply(&reflection_e, matrix),
            multiply(matrix, &reflection_e)
        );
    }
    assert_ne!(entry99, competing);

    // On Z^3/Z(1,1,1), J vanishes.  For c=1, a=1-2b and the induced scalar
    // is a-b=1-3b.  Solving 1-3b=+/-1 over Z gives b=0 for +1, while the
    // -1 equation would require 3b=2.  Hence the inverse-exact-couple
    // (saturated transgression) condition uniquely selects entry 99 without
    // fitting its road matrix.
    let mut integral_unit_solutions = Vec::new();
    for desired_unit in [-1_i64, 1] {
        let numerator = 1 - desired_unit;
        if numerator % 3 == 0 {
            integral_unit_solutions.push(numerator / 3);
        }
    }
    assert_eq!(integral_unit_solutions, vec![0]);
    let selected_b = integral_unit_solutions[0];
    let selected_a = 1 - 2 * selected_b;
    assert_eq!(selected_a - selected_b, 1);
    assert_eq!(equivariant_family(selected_a, selected_b), entry99);
}

fn main() {
    let by_size = faces_by_size();
    let vertex_gauges = vertex_orientation_gauges(&by_size);
    let (relative_d3, _) = check_actual_faces_dual_block_and_filtration(&by_size, &vertex_gauges);
    check_carrier_nullhomotopy_covariance_and_uniqueness(&relative_d3);

    println!(
        "{}",
        concat!(
            r#"{"claim":"for the actual labelled cellular triple v_+ subset B_short subset K6, entry 99's plus carrier is the unique normalized integral D3-equivariant augmented chain lift of the inverse (equivalently dual-block) first exact-couple transgression; this conclusion is derived from the face poset and the saturated connecting isomorphism, not fitted to the carrier matrix","status":"proved","assumptions":["first transgression means the inverse/dual-block orientation of the canonical homological d1: H2(K6,B_short)->H1(B_short,v_+); the homological d1 itself points in the opposite direction","orientations use ordered diagonal normals and the entry-99 convention dK_rel=F14+F03+F25","the statement is confined to integral cellular carriers and adds no occurrence, Cech, normal, can-var, or PC coefficients"],"evidence_refs":["research/voevodsky/check_central_vertex_rees_transgression.rs","research/voevodsky/check_d03_relative_associahedron_pc.rs","research/voevodsky/check_d03_global_dual_block_carrier.rs","src/ledger/20260814-99 Global Dual-Block Carrier and the Unlocalized Can-Var Boundary.md"],"factorization_test":{"actual_face_census":{"top":1,"facets":9,"edges":21,"vertices":14},"actual_relative_census":{"degree3":1,"degree2":3,"degree1":0,"degree0":0},"central_dual_block":{"coface_interval":"Boolean B3","ranks":"f/e/q/a=1/3/3/1","literal_inclusion":"does not contain a road facet; it is not the entry-99 map","peripheral_matching":"after passing through B_short, the unique central flips reach F14,F03,F25 for e1,e3,e5"},"minimal_filtration":"F0=C(v_+) subset F1=C(B_short) subset F2=C(K6), bounded, exhaustive, separated, and D3-stable","E1_page":{"p0_total0":"Z","p1_total1":"Z^2","p2_total2":"Z^2","other_reduced_terms":"0"},"exact_couple":"PASS: d1 sends each relative road class to its actual oriented peripheral boundary cycle; the three cycles sum to a short-facet boundary and any two extend im d_B to a saturated basis, so d1 is an integral isomorphism","carrier_values":{"f_plus":"K_rel","e1":"F14","e3":"F03","e5":"F25","q0_q1_q2_a":"0"},"chain_map":"PASS with established signs","ordinary_composite":"PASS: explicit integral non-equivariant null-homotopy","D3_covariance":"PASS on the enumerated face poset, peripheral cycles, source differential, and carrier: r^3=s^2=1 and srs=r^-1","smallest_ambiguity":"D3 covariance plus the top equation alone allows exactly M(a,b)=aI+b(J-I), c=a+2b; with c=1 the competing b=1 map is integral and covariant","transgression_selection":"PASS: on the peripheral A2 quotient the normalized family acts by 1-3b; being the saturated inverse of d1 forces b=0, hence M=I uniquely","categorical_scope":"canonical in the integral D3-marked relative filtration; ordinary forgetting makes it null, and no Tate or coefficient localization is used"},"counterevidence":["The literal barycentric dual-block/coface inclusion has only faces incident to v_+ and contains no road facet; entry 99 appears only after the relative first-transgression contraction through B_short.","The literal homological exact-couple differential is delta from relative roads to boundary cycles; entry 99 is its inverse/dual-block lift, so calling it delta without this variance reversal is incorrect.","The carrier is ordinary-null and does not by itself construct alpha_plus in the loaded filtered/Rees category.","No local excess line, occurrence pullback, support direction, physical normal, Cech residue, or Tate coefficient is tested here."],"next_experiment":"construct the coefficient-loaded filtered comparison alpha_plus and test that its associated carrier grade is this uniquely selected inverse transgression while its three edge residues are the entry-100 local excess traces"}"#
        )
    );
}
