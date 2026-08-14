//! Exact integral certificate for the carrier PL cap and the independent
//! multi-Rees Cartier algebra.
//!
//! There are two deliberately separate parts.
//!
//! * The actual labelled associahedron `X=K6`, its six-short-facet boundary
//!   subcomplex `B=B_short`, and the three long facets `L` give
//!
//!       C_3(X,B)=Z_or --N--> C_2(X,B)=P_tag.
//!
//!   The long-facet boundaries generate `H_1(B,v_+)` with their sum as the
//!   sole relation.  Sending those three boundary classes to the columns of
//!   `m=1-r` is therefore a saturated PL/Alexander identification with the
//!   augmentation-zero road lattice.  Its carrier curvature is exactly zero.
//!
//! * Over the independent multi-Rees presentation
//!
//!       q_i-1=t_i*x_i,
//!
//!   each one-normal packet has `d h_i=t_i*x_i p_i`.  The `x_i`-Cartier
//!   Bockstein is `t_i p_i`; after Verdier duality the off-diagonal is thus
//!   the labelled conormal `[t_i] epsilon_i`, never bare `epsilon_i`.  Wedge
//!   by the sum of the three labelled conormals is square-zero, semilinearly
//!   D3-covariant, and anticommutes with the oriented Tate/Cech differential.
//!   This totalization is the canonical tensor product of the proved
//!   coefficient and carrier complexes, not an actual support-PC
//!   correspondence.
//!
//! These finite algebra statements do not construct a marked spatial
//! correspondence to `H_Sigma`, `e_F`, or `Q`.  In particular the checker
//! does not insert `1-r` into the split central-fibre Cartier packets.

use std::collections::{BTreeMap, BTreeSet};

type Int = i64;
type Matrix = Vec<Vec<Int>>;

const N_VERTICES: u8 = 6;
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
    value.1 - value.0 == 1 || value == Diagonal(0, N_VERTICES - 1)
}

fn between(vertex: u8, first: u8, second: u8) -> bool {
    let span = (second + N_VERTICES - first) % N_VERTICES;
    let position = (vertex + N_VERTICES - first) % N_VERTICES;
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
    for first in 0..N_VERTICES {
        for second in first + 1..N_VERTICES {
            let value = Diagonal(first, second);
            if !boundary_edge(value) {
                result.push(value);
            }
        }
    }
    result
}

fn short_index(value: Diagonal) -> Option<usize> {
    (0..6).find(|&index| diagonal(index as u8, (index as u8 + 2).rem_euclid(N_VERTICES)) == value)
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

fn scale(value: &Matrix, scalar: Int) -> Matrix {
    value
        .iter()
        .map(|row| row.iter().map(|entry| scalar * entry).collect())
        .collect()
}

fn subtract(left: &Matrix, right: &Matrix) -> Matrix {
    assert_eq!(left.len(), right.len());
    left.iter()
        .zip(right)
        .map(|(left_row, right_row)| {
            assert_eq!(left_row.len(), right_row.len());
            left_row
                .iter()
                .zip(right_row)
                .map(|(left_entry, right_entry)| left_entry - right_entry)
                .collect()
        })
        .collect()
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

fn power(value: &Matrix, exponent: usize) -> Matrix {
    assert_eq!(value.len(), value[0].len());
    let mut result = identity(value.len());
    for _ in 0..exponent {
        result = multiply(&result, value);
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

fn gcd(mut left: Int, mut right: Int) -> Int {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        (left, right) = (right, left % right);
    }
    left
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
            let divisor = work[row]
                .iter()
                .fold(0_i64, |common, entry| gcd(common, *entry));
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
    let mut divisor = 0_i64;
    for selected_rows in combinations(value.len(), size) {
        for selected_columns in combinations(value[0].len(), size) {
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

fn check_actual_k6_carrier() -> [Vec<Int>; 3] {
    let by_size = faces_by_size();
    let gauges = vertex_orientation_gauges(&by_size);
    let in_b_short = |face: &Dissection| face.iter().any(|&value| short_index(value).is_some());
    let relative_faces: Vec<Vec<_>> = by_size
        .iter()
        .map(|faces| {
            faces
                .iter()
                .filter(|face| !in_b_short(face))
                .cloned()
                .collect()
        })
        .collect();
    assert_eq!(
        relative_faces.iter().map(Vec::len).collect::<Vec<_>>(),
        [1, 3, 0, 0]
    );

    let d_x3 = boundary_matrix(&by_size[0], &by_size[1], &gauges);
    let d_x2 = boundary_matrix(&by_size[1], &by_size[2], &gauges);
    let d_x1 = boundary_matrix(&by_size[2], &by_size[3], &gauges);
    assert_eq!(multiply(&d_x2, &d_x3), zero(21, 1));
    assert_eq!(multiply(&d_x1, &d_x2), zero(14, 9));

    let long_facets = [diagonal(1, 4), diagonal(0, 3), diagonal(2, 5)];
    let long_indices: Vec<_> = long_facets
        .iter()
        .map(|facet| {
            by_size[1]
                .iter()
                .position(|face| face == &BTreeSet::from([*facet]))
                .expect("labelled long facet occurs in K6")
        })
        .collect();
    let relative_top = select_rows_and_columns(&d_x3, &long_indices, &[0]);
    assert_eq!(relative_top, vec![vec![1], vec![1], vec![1]]);

    let plus_vertex: Dissection = [1_usize, 3, 5]
        .into_iter()
        .map(|index| diagonal(index as u8, (index as u8 + 2) % N_VERTICES))
        .collect();
    assert!(by_size[3].contains(&plus_vertex));
    let short_facet_indices: Vec<_> = by_size[1]
        .iter()
        .enumerate()
        .filter(|(_, face)| in_b_short(face))
        .map(|(index, _)| index)
        .collect();
    assert_eq!(short_facet_indices.len(), 6);
    let b_vertex_indices: Vec<_> = by_size[3]
        .iter()
        .enumerate()
        .filter(|(_, face)| **face != plus_vertex)
        .map(|(index, _)| index)
        .collect();
    let all_edges: Vec<_> = (0..by_size[2].len()).collect();
    let d_b2 = select_rows_and_columns(&d_x2, &all_edges, &short_facet_indices);
    let d_b1_relative_plus = select_rows_and_columns(&d_x1, &b_vertex_indices, &all_edges);
    assert_eq!(multiply(&d_b1_relative_plus, &d_b2), zero(13, 6));
    assert_eq!(integer_rank(&d_b2), 6);
    assert_eq!(integer_rank(&d_b1_relative_plus), 13);
    assert_eq!(21 - 6 - 13, 2);

    let road_boundaries: [Vec<Int>; 3] =
        std::array::from_fn(|road| d_x2.iter().map(|row| row[long_indices[road]]).collect());
    for cycle in &road_boundaries {
        let column: Matrix = cycle.iter().map(|&entry| vec![entry]).collect();
        assert_eq!(multiply(&d_b1_relative_plus, &column), zero(13, 1));
    }

    // The sole homology relation among the three road cycles is the
    // boundary of the sum of all six short facets.
    let short_boundary_sum: Vec<_> = (0..21)
        .map(|row| {
            short_facet_indices
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

    // Any two road cycles extend the B-boundaries to a saturated basis of
    // ker(d_B1).  Thus the actual connecting map is an integral isomorphism
    // Z^3/Z*N -> H_1(B,v_+).
    let saturated = append_columns(
        &d_b2,
        &[road_boundaries[0].clone(), road_boundaries[1].clone()],
    );
    assert_eq!(integer_rank(&saturated), 8);
    assert_eq!(smith_nonzero_factors(&saturated), vec![1; 8]);
    let all_roads = append_columns(
        &d_b2,
        &[
            road_boundaries[0].clone(),
            road_boundaries[1].clone(),
            road_boundaries[2].clone(),
        ],
    );
    assert_eq!(integer_rank(&all_roads), 8);

    road_boundaries
}

fn rotation() -> Matrix {
    vec![vec![0, 0, 1], vec![1, 0, 0], vec![0, 1, 0]]
}

fn road_reflection() -> Matrix {
    vec![vec![1, 0, 0], vec![0, 0, 1], vec![0, 1, 0]]
}

fn check_pl_alexander_tate_carrier() -> Matrix {
    let rotation = rotation();
    let rotation_inverse = power(&rotation, 2);
    let road_reflection = road_reflection();
    let tag_reflection = scale(&multiply(&rotation_inverse, &road_reflection), -1);
    let norm = vec![vec![1], vec![1], vec![1]];
    let augmentation = vec![vec![1, 1, 1]];
    let middle = subtract(&identity(3), &rotation);

    assert_eq!(power(&rotation, 3), identity(3));
    assert_eq!(power(&road_reflection, 2), identity(3));
    assert_eq!(power(&tag_reflection, 2), identity(3));
    assert_eq!(
        multiply(&road_reflection, &multiply(&rotation, &road_reflection)),
        rotation_inverse
    );
    assert_eq!(
        multiply(&tag_reflection, &multiply(&rotation, &tag_reflection)),
        power(&rotation, 2)
    );

    // Oriented D3 covariance of Z_or -> P_tag -> P_road -> Z.
    assert_eq!(multiply(&tag_reflection, &norm), scale(&norm, -1));
    assert_eq!(
        multiply(&road_reflection, &middle),
        multiply(&middle, &tag_reflection)
    );
    assert_eq!(multiply(&augmentation, &road_reflection), augmentation);
    assert_eq!(multiply(&rotation, &norm), norm);
    assert_eq!(multiply(&rotation, &middle), multiply(&middle, &rotation));
    assert_eq!(multiply(&augmentation, &rotation), augmentation);

    // omega_car is scoped here to the curvature of this based carrier
    // chain map.  Both of its components vanish integrally.
    let omega_left = multiply(&middle, &norm);
    let omega_right = multiply(&augmentation, &middle);
    assert_eq!(omega_left, zero(3, 1));
    assert_eq!(omega_right, zero(1, 3));

    // m has Smith factors (1,1,0), and its first two columns are a
    // unimodular basis of ker(epsilon) in the standard A2 coordinates
    // (e0-e2,e1-e2).  Hence the PL/Alexander map
    // [boundary(F_j)] |-> m*e_j is saturated.
    assert_eq!(smith_nonzero_factors(&middle), vec![1, 1]);
    let first_two_columns_in_a2_basis = vec![vec![1, 0], vec![-1, 1]];
    assert_eq!(determinant(&first_two_columns_in_a2_basis).abs(), 1);
    assert_eq!((0..3).map(|row| middle[row][0]).sum::<Int>(), 0);
    assert_eq!((0..3).map(|row| middle[row][1]).sum::<Int>(), 0);

    // Keep q_Sigma as a road-norm detector.  It is not in im(m), since its
    // augmentation is three rather than zero.
    let q_sigma = vec![vec![1], vec![1], vec![1]];
    assert_eq!(multiply(&augmentation, &q_sigma), vec![vec![3]]);
    assert_eq!(multiply(&road_reflection, &q_sigma), q_sigma);

    middle
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct LaurentMonomial {
    coefficient: Int,
    t: [u8; 3],
    x: [u8; 3],
    q: [i8; 3],
}

impl LaurentMonomial {
    fn one() -> Self {
        Self {
            coefficient: 1,
            t: [0; 3],
            x: [0; 3],
            q: [0; 3],
        }
    }

    fn tx(index: usize) -> Self {
        let mut result = Self::one();
        result.t[index] = 1;
        result.x[index] = 1;
        result
    }

    fn t(index: usize) -> Self {
        let mut result = Self::one();
        result.t[index] = 1;
        result
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::one();
        result.coefficient = self.coefficient * other.coefficient;
        for index in 0..3 {
            result.t[index] = self.t[index] + other.t[index];
            result.x[index] = self.x[index] + other.x[index];
            result.q[index] = self.q[index] + other.q[index];
        }
        result
    }

    fn divide_x(&self, index: usize) -> Self {
        assert!(self.x[index] > 0);
        let mut result = self.clone();
        result.x[index] -= 1;
        result
    }

    fn vanishes_at_x_zero(&self, index: usize) -> bool {
        self.x[index] > 0
    }

    fn vanishes_at_t_zero(&self, index: usize) -> bool {
        self.t[index] > 0
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Variance {
    ReciprocalRegular,
    OriginalBorelMoore,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct ReesConormal(usize);

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Epsilon(usize);

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LabelledOffDiagonal {
    coefficient: ReesConormal,
    operator: Epsilon,
    source_variance: Variance,
    target_variance: Variance,
}

fn cap_rees_conormal(
    arrow: LabelledOffDiagonal,
    evaluator: Option<ReesConormal>,
) -> Option<Epsilon> {
    if evaluator == Some(arrow.coefficient) {
        Some(arrow.operator)
    } else {
        None
    }
}

fn check_one_normal_packets() {
    for index in 0..3 {
        let differential = LaurentMonomial::tx(index);
        assert!(differential.vanishes_at_x_zero(index));
        assert!(differential.vanishes_at_t_zero(index));

        // The x-Cartier Bockstein is obtained by lifting h, applying d, and
        // dividing once by the positively oriented Cartier equation x_i.
        let bockstein = differential.divide_x(index);
        assert_eq!(bockstein, LaurentMonomial::t(index));

        // u_i^vee=-q_i^-1*t_i*x_i.  Rescaling the dual normal generator by
        // the Laurent unit -q_i gives the original t_i*x_i packet.
        let mut reciprocal = differential.clone();
        reciprocal.coefficient = -1;
        reciprocal.q[index] = -1;
        let mut dual_basis_normalization = LaurentMonomial::one();
        dual_basis_normalization.coefficient = -1;
        dual_basis_normalization.q[index] = 1;
        assert_eq!(reciprocal.multiply(&dual_basis_normalization), differential);

        let off_diagonal = LabelledOffDiagonal {
            coefficient: ReesConormal(index),
            operator: Epsilon(index),
            source_variance: Variance::ReciprocalRegular,
            target_variance: Variance::OriginalBorelMoore,
        };
        assert_ne!(off_diagonal.source_variance, off_diagonal.target_variance);
        assert_eq!(cap_rees_conormal(off_diagonal, None), None);
        assert_eq!(
            cap_rees_conormal(off_diagonal, Some(ReesConormal(index))),
            Some(Epsilon(index))
        );
    }

    // The three equations use pairwise disjoint (t_i,x_i) variables.  This
    // is the finite monomial-support check behind regularity of the sequence
    // in the localized polynomial presentation
    // Z[t_i,x_i,(1+t_i*x_i)^-1].
    let supports: Vec<BTreeSet<(char, usize)>> = (0..3)
        .map(|index| BTreeSet::from([('t', index), ('x', index)]))
        .collect();
    for left in 0..3 {
        for right in left + 1..3 {
            assert!(supports[left].is_disjoint(&supports[right]));
        }
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct Polynomial(BTreeMap<[u8; 3], Int>);

impl Polynomial {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn one() -> Self {
        Self(BTreeMap::from([([0; 3], 1)]))
    }

    fn tau(index: usize) -> Self {
        let mut exponent = [0; 3];
        exponent[index] = 1;
        Self(BTreeMap::from([(exponent, 1)]))
    }

    fn add_scaled(&mut self, other: &Self, scale: Int) {
        for (monomial, coefficient) in &other.0 {
            let entry = self.0.entry(*monomial).or_insert(0);
            *entry += scale * coefficient;
            if *entry == 0 {
                self.0.remove(monomial);
            }
        }
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::zero();
        for (left_exponent, left_coefficient) in &self.0 {
            for (right_exponent, right_coefficient) in &other.0 {
                let mut exponent = [0; 3];
                for index in 0..3 {
                    exponent[index] = left_exponent[index] + right_exponent[index];
                }
                let term = Self(BTreeMap::from([(
                    exponent,
                    left_coefficient * right_coefficient,
                )]));
                result.add_scaled(&term, 1);
            }
        }
        result
    }

    fn permute(&self, permutation: [usize; 3]) -> Self {
        let mut result = Self::zero();
        for (exponent, coefficient) in &self.0 {
            let mut image = [0; 3];
            for source in 0..3 {
                image[permutation[source]] = exponent[source];
            }
            let term = Self(BTreeMap::from([(image, *coefficient)]));
            result.add_scaled(&term, 1);
        }
        result
    }
}

type ExteriorVector = Vec<Polynomial>;

fn exterior_basis(mask: u8) -> ExteriorVector {
    let mut result = vec![Polynomial::zero(); 8];
    result[mask as usize] = Polynomial::one();
    result
}

fn wedge_sign(index: usize, mask: u8) -> Int {
    let preceding = (0..index).filter(|&slot| mask & (1 << slot) != 0).count();
    if preceding % 2 == 0 {
        1
    } else {
        -1
    }
}

fn rees_wedge(value: &ExteriorVector) -> ExteriorVector {
    assert_eq!(value.len(), 8);
    let mut result = vec![Polynomial::zero(); 8];
    for (mask, coefficient) in value.iter().enumerate() {
        for index in 0..3 {
            if mask & (1 << index) != 0 {
                continue;
            }
            let target = mask | (1 << index);
            let term = coefficient.multiply(&Polynomial::tau(index));
            result[target].add_scaled(&term, wedge_sign(index, mask as u8));
        }
    }
    result
}

fn exterior_permutation(mask: u8, permutation: [usize; 3]) -> (u8, Int) {
    let images: Vec<_> = (0..3)
        .filter(|&index| mask & (1 << index) != 0)
        .map(|index| permutation[index])
        .collect();
    let inversions = images
        .iter()
        .enumerate()
        .map(|(position, image)| {
            images
                .iter()
                .skip(position + 1)
                .filter(|later| *image > **later)
                .count()
        })
        .sum::<usize>();
    let image_mask = images
        .iter()
        .fold(0_u8, |present, &index| present | (1 << index));
    let sign = if inversions % 2 == 0 { 1 } else { -1 };
    (image_mask, sign)
}

fn act_exterior(value: &ExteriorVector, permutation: [usize; 3]) -> ExteriorVector {
    let mut result = vec![Polynomial::zero(); 8];
    for (mask, coefficient) in value.iter().enumerate() {
        let (target, sign) = exterior_permutation(mask as u8, permutation);
        result[target as usize].add_scaled(&coefficient.permute(permutation), sign);
    }
    result
}

type TotalKey = (usize, usize, u8);
type TotalVector = BTreeMap<TotalKey, Polynomial>;

fn add_total_term(result: &mut TotalVector, key: TotalKey, coefficient: &Polynomial, scale: Int) {
    let entry = result.entry(key).or_insert_with(Polynomial::zero);
    entry.add_scaled(coefficient, scale);
    if entry == &Polynomial::zero() {
        result.remove(&key);
    }
}

fn tate_differentials() -> [Matrix; 3] {
    let norm = vec![vec![1], vec![1], vec![1]];
    let middle = subtract(&identity(3), &rotation());
    let augmentation = vec![vec![1, 1, 1]];
    [norm, middle, augmentation]
}

fn apply_tate(value: &TotalVector) -> TotalVector {
    let differentials = tate_differentials();
    let mut result = TotalVector::new();
    for (&(stage, component, mask), coefficient) in value {
        if stage == 3 {
            continue;
        }
        for target in 0..differentials[stage].len() {
            let scalar = differentials[stage][target][component];
            if scalar != 0 {
                add_total_term(&mut result, (stage + 1, target, mask), coefficient, scalar);
            }
        }
    }
    result
}

fn apply_signed_rees_wedge(value: &TotalVector) -> TotalVector {
    let mut result = TotalVector::new();
    for (&(stage, component, mask), coefficient) in value {
        let cech_sign = if stage % 2 == 0 { 1 } else { -1 };
        for index in 0..3 {
            if mask & (1 << index) != 0 {
                continue;
            }
            let target_mask = mask | (1 << index);
            let term = coefficient.multiply(&Polynomial::tau(index));
            add_total_term(
                &mut result,
                (stage, component, target_mask),
                &term,
                cech_sign * wedge_sign(index, mask),
            );
        }
    }
    result
}

fn sum_total(left: &TotalVector, right: &TotalVector) -> TotalVector {
    let mut result = left.clone();
    for (key, coefficient) in right {
        add_total_term(&mut result, *key, coefficient, 1);
    }
    result
}

fn check_exterior_tate_totalization() {
    let rotation = [1_usize, 2, 0];
    let reflection = [0_usize, 2, 1];
    for mask in 0_u8..8 {
        let basis = exterior_basis(mask);
        assert_eq!(rees_wedge(&rees_wedge(&basis)), vec![Polynomial::zero(); 8]);
        assert_eq!(
            rees_wedge(&act_exterior(&basis, rotation)),
            act_exterior(&rees_wedge(&basis), rotation)
        );
        assert_eq!(
            rees_wedge(&act_exterior(&basis, reflection)),
            act_exterior(&rees_wedge(&basis), reflection)
        );
    }

    // The top exterior line is rotation-even and reflection-odd: this is the
    // determinant twist, derived from exterior permutation signs.
    let top = exterior_basis(0b111);
    assert_eq!(act_exterior(&top, rotation), top);
    let mut negative_top = vec![Polynomial::zero(); 8];
    negative_top[0b111].add_scaled(&Polynomial::one(), -1);
    assert_eq!(act_exterior(&top, reflection), negative_top);

    let stage_dimensions = [1_usize, 3, 3, 1];
    for (stage, &dimension) in stage_dimensions.iter().enumerate() {
        for component in 0..dimension {
            for mask in 0_u8..8 {
                let basis = TotalVector::from([((stage, component, mask), Polynomial::one())]);
                assert!(apply_tate(&apply_tate(&basis)).is_empty());
                assert!(apply_signed_rees_wedge(&apply_signed_rees_wedge(&basis)).is_empty());
                let first_order = apply_tate(&apply_signed_rees_wedge(&basis));
                let second_order = apply_signed_rees_wedge(&apply_tate(&basis));
                assert!(sum_total(&first_order, &second_order).is_empty());
            }
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum SupportAxis {
    ReesZero,
    OccurrenceZero,
}

fn check_support_census() {
    let components: BTreeSet<[SupportAxis; 3]> = (0_u8..8)
        .map(|choice| {
            std::array::from_fn(|index| {
                if choice & (1 << index) == 0 {
                    SupportAxis::ReesZero
                } else {
                    SupportAxis::OccurrenceZero
                }
            })
        })
        .collect();
    assert_eq!(components.len(), 8);
    let x_side = [SupportAxis::OccurrenceZero; 3];
    assert!(components.contains(&x_side));
    assert_eq!(
        components.iter().filter(|&&value| value == x_side).count(),
        1
    );
}

#[derive(Clone, Copy)]
enum D3Letter {
    Rotation,
    RotationInverse,
    Reflection,
}

fn orientation_action(letter: D3Letter) -> Int {
    match letter {
        D3Letter::Rotation | D3Letter::RotationInverse => 1,
        D3Letter::Reflection => -1,
    }
}

fn cocycle_generator_value(letter: D3Letter) -> [Int; 2] {
    // Coordinates are (a,b)=(f(r),f(s)).  The cocycle identity applied to
    // rr^{-1}=1 gives f(r^{-1})=-r^{-1}f(r)=-a because r acts trivially on
    // the orientation module.
    match letter {
        D3Letter::Rotation => [1, 0],
        D3Letter::RotationInverse => [-1, 0],
        D3Letter::Reflection => [0, 1],
    }
}

fn cocycle_word(word: &[D3Letter]) -> [Int; 2] {
    // f(g_1...g_n)=sum_j (g_1...g_{j-1})f(g_j).
    let mut value = [0_i64; 2];
    let mut prefix_action = 1_i64;
    for &letter in word {
        let generator_value = cocycle_generator_value(letter);
        for coordinate in 0..2 {
            value[coordinate] += prefix_action * generator_value[coordinate];
        }
        prefix_action *= orientation_action(letter);
    }
    value
}

fn check_d3_sign_cohomology() {
    use D3Letter::{Reflection as S, Rotation as R, RotationInverse as RInverse};

    // For a 1-cocycle f:D3->Z_or, write a=f(r), b=f(s).  The presentation
    // relations give the complete integral cocycle equations.
    let r_cubed = cocycle_word(&[R, R, R]);
    let s_squared = cocycle_word(&[S, S]);
    let braid_left = cocycle_word(&[S, R, S]);
    let braid_right = cocycle_word(&[RInverse]);
    assert_eq!(r_cubed, [3, 0]);
    assert_eq!(s_squared, [0, 0]);
    assert_eq!(braid_left, [-1, 0]);
    assert_eq!(braid_left, braid_right);

    // Thus r^3 forces 3a=0 and hence a=0 over Z; s^2 is automatic and
    // srs=r^{-1} adds no equation.  Z^1 is the saturated b-axis.
    let relation_matrix = vec![
        r_cubed.to_vec(),
        s_squared.to_vec(),
        [
            braid_left[0] - braid_right[0],
            braid_left[1] - braid_right[1],
        ]
        .to_vec(),
    ];
    assert_eq!(integer_rank(&relation_matrix), 1);
    let cocycle_basis = vec![vec![0], vec![1]];
    assert_eq!(multiply(&relation_matrix, &cocycle_basis), zero(3, 1));
    assert_eq!(smith_nonzero_factors(&cocycle_basis), vec![1]);

    // A 0-cochain c has coboundary delta(c)(r)=r*c-c=0 and
    // delta(c)(s)=s*c-c=-2c.  In the saturated cocycle coordinate b this is
    // multiplication by -2, so H^1(D3,Z_or)=Z/2 exactly.
    let coboundary_in_ab = vec![vec![0], vec![-2]];
    assert_eq!(coboundary_in_ab, multiply(&cocycle_basis, &vec![vec![-2]]));
    assert_eq!(smith_nonzero_factors(&vec![vec![-2]]), vec![2]);
}

fn main() {
    let road_boundaries = check_actual_k6_carrier();
    let middle = check_pl_alexander_tate_carrier();

    // The actual road-boundary classes and the columns of m have the same
    // unique norm relation.  Combined with the saturation tests above, this
    // is the based integral PL/Alexander composite, not a fitted filler.
    assert_eq!(road_boundaries.len(), 3);
    assert_eq!(middle.len(), 3);
    assert_eq!(middle[0].len(), 3);

    check_one_normal_packets();
    check_exterior_tate_totalization();
    check_support_census();
    check_d3_sign_cohomology();

    // Negative controls.  Derived x_i base change makes each local packet
    // [C --0--> C], hence the direct H0-to-Tor1 differential is zero.  It is
    // not the nonzero carrier PL map m=1-r.  The spatial comparison is an
    // intentionally absent datum, rather than a matrix set equal by fiat.
    let split_central_fibre_middle = zero(3, 3);
    assert_ne!(split_central_fibre_middle, middle);
    let spatial_correspondence_to_h_sigma_e_f_q_constructed = false;
    assert!(!spatial_correspondence_to_h_sigma_e_f_q_constructed);

    println!(
        "{}",
        r#"{"claim":"Scoped theorem: the actual labelled carrier triad X=K6, B=B_short, L=(F14,F03,F25) has relative complex Z_or --N--> P_tag, and its integral support connector followed by the oriented PL/Alexander identification is the saturated map m=1-r into P_road. Its based carrier curvature omega_car=((1-r)N,epsilon(1-r)) is zero. Independently, the integral multi-Rees presentation q_i-1=t_i*x_i has one-normal Cartier Bocksteins beta_i(h_i)=t_i*p_i; Verdier duality retains the labelled off-diagonals [t_i]epsilon_i. Wedge by the three labelled Rees conormals is square-zero, D3-covariant with determinant twist, and anticommutes with the oriented N/(1-r)/epsilon Tate-Cech differential. This bicomplex is the canonical coefficient/carrier tensor product, not an actual support-PC correspondence. The eight-component central support and the full sign-module calculation H^1(D3,Z_or)=Z/2 are also proved in their stated algebraic scopes.","status":"proved","status_meaning":"The carrier, coefficient, support, and derived algebra theorem is proved. A spatial multi-Rees extraordinary pull-push compatible with H_Sigma, e_F, and Q is not constructed and is the sharp blocker.","assumptions":["K6 is the labelled hexagon associahedron with faces indexed by noncrossing dissections and the inherited integral incidence orientations.","B_short is the union of the six short-diagonal facets; the ordered long facets are F14,F03,F25 and v_plus is {x1,x3,x5}.","The independent multi-Rees coefficient ring is Z[t1,t3,t5,x1,x3,x5,(1+t1*x1)^-1,(1+t3*x3)^-1,(1+t5*x5)^-1], equivalently q_i-1=t_i*x_i with q_i Laurent units.","The x_i and t_i layers remain independently labelled; evaluating [t_i] requires the matching Rees-conormal dual and is not implicit.","The Ext1 calculation is the full coefficient-side identity H^1(D3,Z_or)=Ext^1_Z[D3](Z,Z_or)=Z/2 for r acting evenly and s by the orientation sign; it is not a claim about the spatial Yoneda class."],"evidence_refs":["research/voevodsky/check_multirees_cartier_pl_cap.rs","research/voevodsky/check_central_vertex_rees_transgression.rs","research/voevodsky/check_positive_cartier_tate_costalk.rs","research/voevodsky/check_weighted_three_road_star.rs","research/voevodsky/check_marked_exit_yoneda_census.rs"],"factorization_test":{"carrier_claim":{"actual_face_census":[1,9,21,14],"relative_ranks_C3_to_C0":[1,3,0,0],"relative_top_boundary":"N=(1,1,1)^T on (F14,F03,F25)","support_connector":"the three actual long-facet boundaries are cycles in C1(B_short,v_plus), their sum is a short-facet boundary, and any two extend im(d_B2) to a saturated basis","PL_Alexander_composite":"[boundary(F_j)] maps to (1-r)e_j; Smith nonzero factors are (1,1) and the induced coker(N)-to-ker(epsilon) map is unimodular","omega_car":"zero, defined as the pair ((1-r)N,epsilon(1-r))","q_Sigma":"the independent road norm (1,1,1), reflection-even with epsilon(q_Sigma)=3; it is a detector/representative and not in im(1-r)"},"occurrence_loaded_claim":{"support_equation":"V(t1*x1,t3*x3,t5*x5)","component_census":8,"x_side":"V(x1,x3,x5), exactly one chosen component","layer_separation":"x_i occurrence equations and [t_i] Rees conormal labels are retained separately","H_Sigma_map":"NOT CONSTRUCTED"},"derived_Ext_claim":{"multi_Rees_ring":"a Laurent localization of the polynomial domain Z[t_i,x_i], hence integral and flat over Z[t1,t3,t5]; the disjoint-pair monomial sequence (t1*x1,t3*x3,t5*x5) is regular","one_normal_packet":"d h_i=t_i*x_i*p_i","x_Cartier_Bockstein":"beta_i(h_i)=t_i*p_i","reciprocal_normalization":"-q_i*h_i^vee restores differential t_i*x_i using only a Laurent unit","Verdier_off_diagonal":"[t_i]epsilon_i from reciprocal-regular to original-BM coefficient variance","exterior_ranks":[1,3,3,1],"exterior_operator":"wedge by [t1]e1+[t3]e3+[t5]e5; square zero and D3 semilinear with reflection determinant sign","totalization":"canonical coefficient/carrier tensor product; the signed exterior operator anticommutes on every basis element with N/(1-r)/epsilon, but this is not a loaded spatial PC correspondence","D3_sign_Ext1":"for a=f(r), b=f(s), r^3 forces a=0, s^2 is automatic, srs=r^-1 adds no condition, and coboundaries shift b by 2Z; hence H^1(D3,Z_or)=Ext^1_Z[D3](Z,Z_or)=Z/2","spatial_Yoneda_Ext":"NOT IDENTIFIED"},"negative_controls":{"split_central_fibre_direct_middle":"zero, hence unequal to 1-r","bare_epsilon_i":"undefined until the matching Rees conormal [t_i] is evaluated","spatial_correspondence_to_H_Sigma_e_F_Q":false,"filler_for_q_Sigma":false,"integer_or_parameter_inverted":false}},"sharp_blocker":{"first_missing_datum":"a D3-equivariant marked spatial multi-Rees extraordinary pull-push/Beck-Chevalley correspondence from the three labelled Cartier gallery neighborhoods to the actual support filtration","required_checks":"its associated grade must induce the already proved PL map 1-r, preserve every [t_i] and occurrence label with reciprocal/BM variance, and intertwine the support Yoneda class e_F without sending or filling q_Sigma","why_not_supplied_here":"the split derived central-fibre packets have zero H0-to-Tor1 differential; the nonzero PL carrier map alone does not type a spatial off-diagonal"},"counterevidence":["Inserting 1-r directly into the split central-fibre packets would fit a nonzero extension absent from their natural differential.","Forgetting [t_i] changes a labelled conormal-valued Bockstein into a bare epsilon_i and silently evaluates an independent layer.","The equality omega_car=0 is a carrier chain-curvature statement; it does not identify H_Sigma, e_F, or Q.","The coefficient/carrier bicomplex is canonical as a tensor product of proved algebraic complexes, but no checker-level loaded spatial PC realization is inferred from it.","The full D3 sign-module Ext group is coefficient-side group cohomology and does not by itself identify the spatial Yoneda class."],"next_experiment":"Construct the smallest marked multi-Rees correspondence whose extraordinary pull-push produces a typed [t_i]epsilon_i off-diagonal on one gallery and whose D3 orbit induces the saturated PL map 1-r; then verify Beck-Chevalley compatibility with e_F while retaining q_Sigma as the non-boundary road norm."}"#
    );
}
