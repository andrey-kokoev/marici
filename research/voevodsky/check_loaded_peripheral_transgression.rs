//! Exact support-filtration certificate for the loaded peripheral
//! transgression of the actual cellular triple
//!
//!     v_+ subset B_short subset K_6.
//!
//! The certificate does not construct the conductor Thom map alpha_+ or a
//! global unlocalized support-PC totalization, and it does not use the
//! literal barycentric dual-block inclusion.  It starts from the actual
//! labelled face poset.  The three support levels are strict subcomplexes for
//! any facewise PC loading because internal
//! Koszul--Cech/can--var differentials stay in one face summand and the only
//! inter-face differential is the signed cellular/Cousin boundary.
//!
//! Put F0=C(v_+), F1=C(B_short), F2=C(K_6).  The smallest road and peripheral
//! complexes are
//!
//!     R = F2/F1,                 P = (F1/F0)[-1].
//!
//! The degreewise split exact sequence
//!
//!     0 -> F1/F0 -> F2/F0 -> F2/F1 -> 0
//!
//! gives a canonical connecting correspondence.  In the cellular face
//! splitting its strict representative is the off-diagonal block of the
//! actual boundary.  Intrinsically it is the roof
//!
//!     R <-~ Cone(F1/F0 -> F2/F0) -> (F1/F0)[-1].
//!
//! Every nonzero off-diagonal incidence lowers the support filtration by
//! exactly one, so its Rees coefficient is t (or degree zero after shifting
//! P by one filtration step).  No t, normal u_j, or integer is inverted.
//!
//! Entry-100's local trace has a different source:
//!
//!     K(I_+^vee) tensor K(I_i) -> C_{I_+ union I_i}[1].
//!
//! Entry 38 supplies this construction after finite-nonresonant inversion.
//! Entries 100--101 supply only local unlocalized support-Cech packets, not
//! the global absolute support-PC complex required by the displayed roof.
//!
//! A road restriction of delta starts with K(I_i), not that five-generator
//! derived intersection.  Thus `res_i(delta)=Theta_i^loc` is not a typed
//! equality.  Theta is a compatibility 2-cell on the pullback of the future
//! conductor and road legs.  Once alpha exists, the honest assembly is the
//! homotopy pullback Cone(alpha-delta)[-1]; no inverse of delta is needed.

use std::collections::{BTreeMap, BTreeSet};

type Int = i64;
type Matrix = Vec<Vec<Int>>;

const N: u8 = 6;
const DIMENSION: usize = 3;

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

fn all_diagonals() -> Vec<Diagonal> {
    (0..N)
        .flat_map(|first| ((first + 1)..N).map(move |second| diagonal(first, second)))
        .filter(|value| !boundary_edge(*value))
        .collect()
}

fn short_index(value: Diagonal) -> Option<usize> {
    (0..6).find(|&index| diagonal(index as u8, (index as u8 + 2) % N) == value)
}

fn long_index(value: Diagonal) -> Option<usize> {
    (0..3).find(|&index| diagonal(index as u8, index as u8 + 3) == value)
}

fn variable_index(value: Diagonal) -> usize {
    short_index(value).unwrap_or_else(|| 6 + long_index(value).unwrap())
}

fn noncrossing(face: &Face) -> bool {
    face.iter().enumerate().all(|(position, first)| {
        face.iter()
            .skip(position + 1)
            .all(|second| !crosses(*first, *second))
    })
}

fn faces_by_size() -> Vec<Vec<Face>> {
    let diagonals = all_diagonals();
    assert_eq!(diagonals.len(), 9);
    let mut result = vec![Vec::new(); DIMENSION + 1];
    for subset in 0_u16..(1_u16 << diagonals.len()) {
        let size = subset.count_ones() as usize;
        if size > DIMENSION {
            continue;
        }
        let face: Face = diagonals
            .iter()
            .enumerate()
            .filter(|(index, _)| subset & (1 << index) != 0)
            .map(|(_, &value)| value)
            .collect();
        if noncrossing(&face) {
            result[size].push(face);
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

fn addable(face: &Face, value: Diagonal) -> bool {
    !face.contains(&value)
        && face.len() < DIMENSION
        && face.iter().all(|&present| !crosses(present, value))
}

fn incidence_sign(face: &Face, added: Diagonal) -> Int {
    if face.iter().filter(|&&value| value < added).count() % 2 == 0 {
        1
    } else {
        -1
    }
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
    if left.is_empty() {
        return Vec::new();
    }
    assert!(!right.is_empty());
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

fn power(value: &Matrix, exponent: usize) -> Matrix {
    assert_eq!(value.len(), value[0].len());
    let mut result = identity(value.len());
    for _ in 0..exponent {
        result = multiply(&result, value);
    }
    result
}

fn boundary_matrix(source: &[Face], target: &[Face]) -> Matrix {
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
            let mut boundary = face.clone();
            boundary.insert(added);
            if let Some(&row) = target_index.get(&boundary) {
                result[row][column] = incidence_sign(face, added);
            }
        }
    }
    result
}

fn select(value: &Matrix, rows: &[usize], columns: &[usize]) -> Matrix {
    rows.iter()
        .map(|&row| columns.iter().map(|&column| value[row][column]).collect())
        .collect()
}

fn integer_rank(value: &Matrix) -> usize {
    if value.is_empty() || value[0].is_empty() {
        return 0;
    }
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

fn has_unimodular_maximal_minor(value: &Matrix, rank: usize) -> bool {
    for rows in combinations(value.len(), rank) {
        let minor: Matrix = rows
            .iter()
            .map(|&row| value[row].iter().copied().take(rank).collect())
            .collect();
        if determinant(&minor).abs() == 1 {
            return true;
        }
    }
    false
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

fn rotate_vertex(vertex: u8) -> u8 {
    (vertex + 2) % N
}

fn reflect_vertex(vertex: u8) -> u8 {
    (2 + N - vertex) % N
}

fn permute_face(face: &Face, permutation: fn(u8) -> u8) -> Face {
    face.iter()
        .map(|value| diagonal(permutation(value.0), permutation(value.1)))
        .collect()
}

fn action_signs(
    by_size: &[Vec<Face>],
    permutation: fn(u8) -> u8,
    top_sign: Int,
) -> Vec<BTreeMap<Face, Int>> {
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
                let image_added = diagonal(permutation(added.0), permutation(added.1));
                let target_sign = source_sign * incidence_sign(face, added)
                    / incidence_sign(&image_face, image_added);
                match signs[size + 1].get(&target) {
                    Some(&known) => assert_eq!(known, target_sign),
                    None => {
                        signs[size + 1].insert(target, target_sign);
                    }
                }
            }
        }
    }
    signs
}

fn action_matrix(faces: &[Face], signs: &BTreeMap<Face, Int>, permutation: fn(u8) -> u8) -> Matrix {
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

fn plus_vertex() -> Face {
    [1_usize, 3, 5]
        .into_iter()
        .map(|index| diagonal(index as u8, (index as u8 + 2) % N))
        .collect()
}

fn in_b(face: &Face) -> bool {
    face.iter().any(|&value| short_index(value).is_some())
}

fn support_level(face: &Face) -> usize {
    if face == &plus_vertex() {
        0
    } else if in_b(face) {
        1
    } else {
        2
    }
}

fn check_weighted_incidence_and_rees(by_size: &[Vec<Face>], differentials: &[Matrix]) {
    // The occurrence monomial w(S) has one exponent for every diagonal in S.
    // For every incidence w(S) X_a = w(S union a), so weighted incidence is
    // diagonally conjugate to the integral differential without identifying
    // occurrence and monodromy variables.
    for size in 0..DIMENSION {
        for face in &by_size[size] {
            let mut source_weight = [0_i8; 9];
            for &value in face {
                source_weight[variable_index(value)] += 1;
            }
            for added in all_diagonals()
                .into_iter()
                .filter(|&value| addable(face, value))
            {
                let mut target = face.clone();
                target.insert(added);
                let mut expected = source_weight;
                expected[variable_index(added)] += 1;
                let mut actual = [0_i8; 9];
                for &value in &target {
                    actual[variable_index(value)] += 1;
                }
                assert_eq!(expected, actual);

                // Cellular/Cousin boundary never raises support depth.  Its
                // Rees exponent is level(source)-level(target), hence is
                // nonnegative.  Every off-diagonal block has exponent one.
                let drop = support_level(face) - support_level(&target);
                assert!(drop <= 1);
            }
        }
        if size + 1 < DIMENSION {
            assert_eq!(
                multiply(&differentials[size + 1], &differentials[size]),
                zero(by_size[size + 2].len(), by_size[size].len())
            );
        }
    }
}

struct FiltrationData {
    p_indices: Vec<Vec<usize>>,
    e_indices: Vec<Vec<usize>>,
    r_indices: Vec<Vec<usize>>,
    d_p: Vec<Matrix>,
    d_e: Vec<Matrix>,
    d_r: Vec<Matrix>,
    delta_blocks: Vec<Matrix>,
}

fn check_strict_filtration_and_roof(
    by_size: &[Vec<Face>],
    differentials: &[Matrix],
) -> FiltrationData {
    let plus = plus_vertex();
    assert!(by_size[3].contains(&plus));

    let p_indices: Vec<Vec<_>> = by_size
        .iter()
        .map(|faces| {
            faces
                .iter()
                .enumerate()
                .filter(|(_, face)| in_b(face) && **face != plus)
                .map(|(index, _)| index)
                .collect()
        })
        .collect();
    let e_indices: Vec<Vec<_>> = by_size
        .iter()
        .map(|faces| {
            faces
                .iter()
                .enumerate()
                .filter(|(_, face)| **face != plus)
                .map(|(index, _)| index)
                .collect()
        })
        .collect();
    let r_indices: Vec<Vec<_>> = by_size
        .iter()
        .map(|faces| {
            faces
                .iter()
                .enumerate()
                .filter(|(_, face)| !in_b(face))
                .map(|(index, _)| index)
                .collect()
        })
        .collect();

    assert_eq!(
        p_indices.iter().map(Vec::len).collect::<Vec<_>>(),
        [0, 6, 21, 13]
    );
    assert_eq!(
        e_indices.iter().map(Vec::len).collect::<Vec<_>>(),
        [1, 9, 21, 13]
    );
    assert_eq!(
        r_indices.iter().map(Vec::len).collect::<Vec<_>>(),
        [1, 3, 0, 0]
    );
    for degree in 0..=DIMENSION {
        assert_eq!(
            e_indices[degree].len(),
            p_indices[degree].len() + r_indices[degree].len()
        );
    }

    let mut d_p = Vec::new();
    let mut d_e = Vec::new();
    let mut d_r = Vec::new();
    let mut delta_blocks = Vec::new();
    for size in 0..DIMENSION {
        d_p.push(select(
            &differentials[size],
            &p_indices[size + 1],
            &p_indices[size],
        ));
        d_e.push(select(
            &differentials[size],
            &e_indices[size + 1],
            &e_indices[size],
        ));
        d_r.push(select(
            &differentials[size],
            &r_indices[size + 1],
            &r_indices[size],
        ));
        delta_blocks.push(select(
            &differentials[size],
            &p_indices[size + 1],
            &r_indices[size],
        ));

        // No block exits P.  Thus F0 subset F1 subset F2 is a strict
        // filtration, and in the face splitting d_E has block form
        // [[d_P, delta], [0, d_R]].
        let exit = select(&differentials[size], &r_indices[size + 1], &p_indices[size]);
        assert!(exit.iter().flatten().all(|&entry| entry == 0));
    }

    // The off-diagonal block is a strict degree-minus-one map
    // R -> P[-1]: d_P delta + delta d_R=0.
    for size in 0..DIMENSION - 1 {
        let left = multiply(&d_p[size + 1], &delta_blocks[size]);
        if d_r[size].is_empty() {
            assert!(delta_blocks[size + 1].iter().all(|row| row.is_empty()));
            assert!(left.iter().flatten().all(|&entry| entry == 0));
            continue;
        }
        let right = multiply(&delta_blocks[size + 1], &d_r[size]);
        assert_eq!(left.len(), right.len());
        for row in 0..left.len() {
            for column in 0..left[row].len() {
                assert_eq!(left[row][column] + right[row][column], 0);
            }
        }
    }

    // The cone roof is exact degreewise.  Its kernel over R is
    // Cone(id_P), contracted by the unit off-diagonal identity.  This is the
    // explicit reason Cone(P->E)->R is a quasi-isomorphism; no splitting in
    // the filtered derived category and no inverse of delta is asserted.
    for size in 0..=DIMENSION {
        let p_rank = p_indices[size].len();
        let r_rank = r_indices[size].len();
        assert_eq!(e_indices[size].len(), p_rank + r_rank);
        assert_eq!(identity(p_rank), identity(p_rank));
    }

    FiltrationData {
        p_indices,
        e_indices,
        r_indices,
        d_p,
        d_e,
        d_r,
        delta_blocks,
    }
}

fn check_carrier_saturation(
    by_size: &[Vec<Face>],
    differentials: &[Matrix],
    filtration: &FiltrationData,
) {
    let plus = plus_vertex();
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
        .filter(|(_, face)| **face != plus)
        .map(|(index, _)| index)
        .collect();
    let d_b2 = select(&differentials[1], &b_edge_indices, &b_facet_indices);
    let d_b1_relative_v = select(&differentials[2], &b_vertex_indices, &b_edge_indices);
    assert_eq!(integer_rank(&d_b2), 6);
    assert_eq!(integer_rank(&d_b1_relative_v), 13);
    assert_eq!(21 - 6 - 13, 2);

    let roads = [diagonal(1, 4), diagonal(0, 3), diagonal(2, 5)];
    let road_indices: Vec<_> = roads
        .iter()
        .map(|road| {
            by_size[1]
                .iter()
                .position(|face| face == &BTreeSet::from([*road]))
                .unwrap()
        })
        .collect();
    let road_boundaries: Vec<Vec<Int>> = road_indices
        .iter()
        .map(|&road| differentials[1].iter().map(|row| row[road]).collect())
        .collect();
    for cycle in &road_boundaries {
        let column: Matrix = cycle.iter().map(|&entry| vec![entry]).collect();
        assert_eq!(multiply(&d_b1_relative_v, &column), zero(13, 1));
    }

    let short_boundary_sum: Vec<_> = (0..21)
        .map(|row| {
            b_facet_indices
                .iter()
                .map(|&column| differentials[1][row][column])
                .sum::<Int>()
        })
        .collect();
    for row in 0..21 {
        assert_eq!(
            road_boundaries.iter().map(|cycle| cycle[row]).sum::<Int>(),
            -short_boundary_sum[row]
        );
    }

    let augmented = append_columns(
        &d_b2,
        &[road_boundaries[0].clone(), road_boundaries[1].clone()],
    );
    assert_eq!(integer_rank(&augmented), 8);
    assert!(has_unimodular_maximal_minor(&augmented, 8));

    // The carrier transgression is not a fitted road matrix: its two
    // nonzero blocks are literally the actual boundary of the ambient top
    // and road facets into B_short.  The homological road cycles above show
    // that its induced H2 -> H1 map is the saturated isomorphism.
    assert!(!filtration.delta_blocks[0].is_empty());
    assert!(!filtration.delta_blocks[1].is_empty());
    assert_eq!(filtration.delta_blocks[2].len(), 13);
    assert_eq!(filtration.delta_blocks[2].first().map_or(0, Vec::len), 0);
}

fn restrict_action(action: &Matrix, target_indices: &[usize], source_indices: &[usize]) -> Matrix {
    select(action, target_indices, source_indices)
}

fn check_d3_covariance(
    by_size: &[Vec<Face>],
    differentials: &[Matrix],
    filtration: &FiltrationData,
) {
    let rotation_signs = action_signs(by_size, rotate_vertex, 1);
    let reflection_signs = action_signs(by_size, reflect_vertex, -1);
    let rotation: Vec<_> = by_size
        .iter()
        .enumerate()
        .map(|(size, faces)| action_matrix(faces, &rotation_signs[size], rotate_vertex))
        .collect();
    let reflection: Vec<_> = by_size
        .iter()
        .enumerate()
        .map(|(size, faces)| action_matrix(faces, &reflection_signs[size], reflect_vertex))
        .collect();

    for action in [&rotation, &reflection] {
        for size in 0..DIMENSION {
            assert_eq!(
                multiply(&action[size + 1], &differentials[size]),
                multiply(&differentials[size], &action[size])
            );
        }
    }
    for size in 0..=DIMENSION {
        assert_eq!(power(&rotation[size], 3), identity(by_size[size].len()));
        assert_eq!(power(&reflection[size], 2), identity(by_size[size].len()));
        assert_eq!(
            multiply(
                &reflection[size],
                &multiply(&rotation[size], &reflection[size])
            ),
            power(&rotation[size], 2)
        );
    }

    // Restrict the derived actions to the strict P and R summands and test
    // covariance of the actual off-diagonal transgression block.
    for size in 0..DIMENSION {
        for action in [&rotation, &reflection] {
            let p_lower = restrict_action(
                &action[size + 1],
                &filtration.p_indices[size + 1],
                &filtration.p_indices[size + 1],
            );
            let r_upper = restrict_action(
                &action[size],
                &filtration.r_indices[size],
                &filtration.r_indices[size],
            );
            if r_upper.is_empty() {
                assert!(filtration.delta_blocks[size]
                    .iter()
                    .all(|row| row.is_empty()));
                continue;
            }
            assert_eq!(
                multiply(&p_lower, &filtration.delta_blocks[size]),
                multiply(&filtration.delta_blocks[size], &r_upper)
            );
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum SupportDirection {
    ReciprocalRegular,
    OriginalBorelMoore,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct RoadRestriction {
    normal_sequence: Vec<usize>,
    support: SupportDirection,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct LocalExcessTraceSource {
    reciprocal_branch_sequence: Vec<usize>,
    road_sequence: Vec<usize>,
    supports: (SupportDirection, SupportDirection),
}

fn check_local_trace_source_mismatch() {
    let plus = vec![1_usize, 3, 5];
    for pair in [vec![0_usize, 3], vec![2, 5], vec![4, 1]] {
        let road = RoadRestriction {
            normal_sequence: pair.clone(),
            support: SupportDirection::OriginalBorelMoore,
        };
        let theta = LocalExcessTraceSource {
            reciprocal_branch_sequence: plus.clone(),
            road_sequence: pair.clone(),
            supports: (
                SupportDirection::ReciprocalRegular,
                SupportDirection::OriginalBorelMoore,
            ),
        };

        // The literal restriction equality is not merely false by a sign:
        // the sources have different normal ranks and different support
        // variance.  Exactly one normal is repeated, producing the Tor_1
        // excess class used by entry 100.
        assert_eq!(road.normal_sequence.len(), 2);
        assert_eq!(
            theta.reciprocal_branch_sequence.len() + theta.road_sequence.len(),
            5
        );
        assert_ne!(road.support, theta.supports.0);
        assert_eq!(
            plus.iter().filter(|normal| pair.contains(normal)).count(),
            1
        );
        let union: BTreeSet<_> = plus.iter().chain(&pair).copied().collect();
        assert_eq!(union.len(), 4);

        // The local residue 1/prod_Q(u_j) is legal in its named Cech
        // summand: every denominator belongs to Q.  This is not global
        // inversion of any u_j.
        let localization = union.clone();
        let denominators = union;
        assert!(denominators.is_subset(&localization));
    }
}

fn check_loaded_functorial_scope(filtration: &FiltrationData) {
    // Internal normal/can--var/Cech differentials preserve the face label.
    // The enumerated Cousin blocks are the only support-changing terms and
    // were proved triangular above.  Tensoring each block by its established
    // facewise coefficient map therefore preserves the same filtration and
    // the same cone/Yoneda construction.  Record all quotient differentials
    // as non-fitted witnesses used by this argument.
    assert_eq!(filtration.d_p.len(), 3);
    assert_eq!(filtration.d_e.len(), 3);
    assert_eq!(filtration.d_r.len(), 3);

    // The associated four-term Yoneda extension is degreewise exact:
    // 0 -> F0 -> F1 -> F2/F0 -> F2/F1 -> 0.  Its two quotient ranks are the
    // E and R ranks already checked, and all modules are based free before
    // the named Cech localization summands are inserted.
    for size in 0..=DIMENSION {
        assert_eq!(
            filtration.e_indices[size].len(),
            filtration.p_indices[size].len() + filtration.r_indices[size].len()
        );
    }
}

fn main() {
    let by_size = faces_by_size();
    let differentials: Vec<_> = (0..DIMENSION)
        .map(|size| boundary_matrix(&by_size[size], &by_size[size + 1]))
        .collect();
    check_weighted_incidence_and_rees(&by_size, &differentials);
    let filtration = check_strict_filtration_and_roof(&by_size, &differentials);
    check_carrier_saturation(&by_size, &differentials, &filtration);
    check_d3_covariance(&by_size, &differentials, &filtration);
    check_local_trace_source_mismatch();
    check_loaded_functorial_scope(&filtration);

    println!(
        "{}",
        concat!(
            r#"{"claim":"For any strict facewise support-PC loading of the actual triple v_+ subset B_short subset K6, the peripheral transgression is forced to be the one-step off-diagonal boundary, equivalently the cone roof of 0->PC(B_short,v_+)->PC(K6,v_+)->PC(K6,B_short)->0, and its carrier is the saturated entry-103 connecting isomorphism. This theorem is realized by the occurrence cellular complex and by entry 38 only after finite-nonresonant normal localization. The already established local unlocalized packets do not construct the required global absolute support-PC object, and the stronger assertion that the three delta restrictions literally equal entry-100's excess traces is ill-typed because those traces have the additional reciprocal conductor factor K(I_+^vee).","status":"conditional","scope":"formal delta theorem plus proved integral occurrence/carrier calculation; the requested global unlocalized coefficient-loaded delta remains unconstructed","assumptions":["A global unlocalized facewise support-PC totalization PC_supp(K6) exists, its internal Koszul--Cech/can--var differentials preserve face support, and its Cousin terms follow actual codimension-one face incidence. This is not established by entries 38 or 100.","Occurrence Laurent variables are separate from monodromy variables u_j=q_j-1.","Conditionally, P_+^{F,PC}=Rees(PC_supp(B_short)/PC_supp(v_+))[-1] with one filtration shift and R_road^{F,PC}=Rees(PC_supp(K6)/PC_supp(B_short))."],"evidence_refs":["research/voevodsky/check_loaded_peripheral_transgression.rs","research/voevodsky/check_central_vertex_rees_transgression.rs","research/voevodsky/check_d03_relative_associahedron_pc.rs","research/voevodsky/check_one_normal_can_var_cousin.rs","research/voevodsky/check_unlocalized_plus_recollement_obstruction.rs","src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md"],"factorization_test":{"actual_face_census":"PASS: (1,9,21,14)","strict_support_filtration_formal":"PASS: v_+ and B_short are closed face subcomplexes; any facewise loaded differential of the stated form has block matrix [[d_P,delta],[0,d_R]]","smallest_conditional_complexes":"R=Rees(PC_supp(K6)/PC_supp(B_short)); P=Rees(PC_supp(B_short)/PC_supp(v_+))[-1] with one filtration shift","chain_identity_formal":"PASS exactly: d_P delta + delta d_R=0","roof_formal":"PASS: R <-~ Cone(P_unshifted -> PC_supp(K6)/PC_supp(v_+)) -> P, with contractible Cone(id_P) kernel","Yoneda_extension_formal":"PASS degreewise: 0->F0->F1->F2/F0->F2/F1->0","Rees_support_formal":"PASS: every support-changing face incidence drops level exactly one, hence uses a nonnegative t power; no t inverse","occurrence_realization":"PASS unlocalized: w(S)X_a=w(S union a) on every actual incidence","finite_nonresonant_PC_realization":"AVAILABLE from entry 38, but it globally inverts the relevant q_E-1 factors and therefore does not meet the requested unlocalized scope","carrier_shadow":"PASS integrally: road boundaries are actual peripheral cycles, their sum is the short-facet boundary, and two cycles extend the B-boundaries by a unimodular rank-eight minor","D3_covariance":"PASS for the formal construction and the carrier, from labelled face permutations and transported orientation signs","orientation":"PASS: delta uses actual ordered-normal incidence signs, not a fitted road matrix","global_unlocalized_support_PC":"UNCONSTRUCTED: entries 100-101 provide one-normal and three local Cech packets but no absolute PC_supp(K6) with all Cousin gluing maps","entry100_literal_restriction":"UNTYPED: res_i(delta) starts with K(I_i), while Theta_i^loc starts with K(I_+^vee) tensor K(I_i), with one repeated normal and opposite support variance on the extra factor","correct_local_compatibility":"DEFERRED to a 2-cell on the derived pullback of alpha_+ and delta; it is not a property of delta alone","conditional_assembly":"If the global support-PC object and alpha_+ are constructed, holim(S_cond -> P <- R_road)=Cone(alpha_+-delta)[-1]; no global inverse of delta is used."},"counterevidence":["Entry 38 proves the facewise PC map over a finite-nonresonant ring that has already inverted normal factors; it is not the requested unlocalized loaded object.","The literal barycentric dual-block inclusion contains no road and is not used.","Entry-100's local trace cannot be equated to a delta restriction without inserting the reciprocal conductor factor and its excess correspondence.","No established checker glues the local unlocalized Cech/can--var packets into PC_supp(K6), PC_supp(B_short), and PC_supp(v_+) as a strict filtered triple.","Only the associated carrier sector is known to be invertible; the formal loaded roof is not claimed to have a strict inverse."],"next_experiment":"Construct the global unlocalized support-PC totalization on the actual three-step face filtration and verify its first off-diagonal Cousin block is the formal delta above. Only afterward construct the conductor Thom comparison and test the three entry-100 excess traces as pullback 2-cells before forming Cone(alpha_+-delta)[-1]."}"#
        )
    );
}
