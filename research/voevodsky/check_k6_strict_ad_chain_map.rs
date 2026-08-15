//! Exact ablation of a strict integral minimal Alexander-dual projection.
//!
//! The actual labelled associahedron gives
//!
//!     P = C_*(B_short) / C_*(v_+),
//!     K = ker(epsilon: Z{q_0,q_1,q_2} -> Z).
//!
//! In the physical road order (F14,F03,F25), rotation is R and the fixed
//! peripheral map is M_AD=R-R^2.  The older displayed matrix M1 uses the
//! signed reversed target basis qbar=(-q2,-q1,-q0); the checker derives that
//! basis change explicitly rather than silently calling it the physical road
//! basis.
//!
//! A degree-zero chain map P -> K[1] is a 3-by-21 matrix F on the edge
//! generators.  We impose only the chain equation, landing in K, strict D3
//! covariance, and the independently fixed saturated map on H_1.  The
//! resulting 174-by-63 integral system is rationally consistent but has an
//! explicit mod-3 inconsistency in either basis.  Thus the checker falsifies
//! only this direct minimal projection.
//!
//! By contrast, the full cone U=(Z^6 -> Z^22 -> Z^14) maps integrally to the
//! augmented target T=(Z^3 -> Z).  Its lift space is a nonempty affine lattice
//! of rank nine; an explicit ell=-1 lift is checked below.  The equation 3c=1
//! obstructs only the extra endpoint-unit framing F0(v_+)=1, not unframed
//! full-cone lifts or a derived roof/butterfly.

use std::collections::{BTreeMap, BTreeSet};

type Int = i64;
type Matrix = Vec<Vec<Int>>;

const N: u8 = 6;
const DIMENSION: usize = 3;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Dissection = BTreeSet<Diagonal>;

#[derive(Clone, Debug)]
struct Equation {
    coefficients: Vec<Int>,
    right_hand_side: Int,
    label: String,
}

#[derive(Clone, Debug)]
struct BasisDictionary {
    physical_rotation: Matrix,
    physical_reflection: Matrix,
    physical_homology: Matrix,
    target_rotation: Matrix,
    target_reflection: Matrix,
    target_homology: Matrix,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct Rational {
    numerator: i128,
    denominator: i128,
}

impl Rational {
    fn new(mut numerator: i128, mut denominator: i128) -> Self {
        assert_ne!(denominator, 0);
        if denominator < 0 {
            numerator = -numerator;
            denominator = -denominator;
        }
        let divisor = gcd_i128(numerator, denominator);
        Self {
            numerator: numerator / divisor,
            denominator: denominator / divisor,
        }
    }

    fn is_zero(&self) -> bool {
        self.numerator == 0
    }

    fn subtract(&self, other: &Self) -> Self {
        Self::new(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )
    }

    fn multiply(&self, other: &Self) -> Self {
        Self::new(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )
    }

    fn divide(&self, other: &Self) -> Self {
        assert!(!other.is_zero());
        Self::new(
            self.numerator * other.denominator,
            self.denominator * other.numerator,
        )
    }
}

fn gcd_i128(mut left: i128, mut right: i128) -> i128 {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        (left, right) = (right, left % right);
    }
    if left == 0 {
        1
    } else {
        left
    }
}

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
                let target_sign = source_sign
                    * incidence_sign(face, &target, added, vertex_gauges)
                    * incidence_sign(&image_face, &image_target, image_added, vertex_gauges);
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

fn zero(rows: usize, columns: usize) -> Matrix {
    vec![vec![0; columns]; rows]
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

fn boundary_matrix(
    source: &[Dissection],
    target: &[Dissection],
    vertex_gauges: &BTreeMap<Dissection, Int>,
) -> Matrix {
    let target_indices: BTreeMap<_, _> = target
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
            if let Some(&row) = target_indices.get(&boundary_face) {
                result[row][column] = incidence_sign(face, &boundary_face, added, vertex_gauges);
            }
        }
    }
    result
}

fn select_rows_and_columns(value: &Matrix, rows: &[usize], columns: &[usize]) -> Matrix {
    rows.iter()
        .map(|&row| columns.iter().map(|&column| value[row][column]).collect())
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
    assert_eq!(left.first().map(Vec::len), right.first().map(Vec::len));
    left.iter()
        .zip(right)
        .map(|(left_row, right_row)| {
            left_row
                .iter()
                .zip(right_row)
                .map(|(left_entry, right_entry)| left_entry - right_entry)
                .collect()
        })
        .collect()
}

fn check_basis_dictionary(
    road_cycles: &Matrix,
    rotation_edges: &Matrix,
    reflection_edges: &Matrix,
) -> BasisDictionary {
    // Column convention in the physical road order (F14,F03,F25):
    // R(q_i)=q_{i+1}, while the chosen reflection fixes q_0.
    let physical_rotation = vec![vec![0, 0, 1], vec![1, 0, 0], vec![0, 1, 0]];
    let physical_reflection = vec![vec![1, 0, 0], vec![0, 0, 1], vec![0, 1, 0]];
    let rotation_squared = multiply(&physical_rotation, &physical_rotation);
    let physical_homology = subtract(&physical_rotation, &rotation_squared);

    // Entry 115''s 1-r has a cyclically shifted tag/boundary basis.  On the
    // actual ordered long-facet boundary cycles this is (1-R)R=R-R^2.
    assert_eq!(
        physical_homology,
        multiply(
            &subtract(&identity(3), &physical_rotation),
            &physical_rotation
        )
    );

    // The actual boundary cycles carry the oriented tag action: rotation R
    // and reflection -s.  This is derived from the K6 cellular action.
    assert_eq!(
        multiply(rotation_edges, road_cycles),
        multiply(road_cycles, &physical_rotation)
    );
    assert_eq!(
        multiply(reflection_edges, road_cycles),
        multiply(road_cycles, &scale(&physical_reflection, -1))
    );

    // The old target matrix was written in the signed reversed basis
    // qbar=(-q2,-q1,-q0).  If J swaps indices 0 and 2, the coordinate
    // transition is B=-J.  It conjugates the physical target actions and
    // sends M_AD to the displayed M1.
    let reversal = vec![vec![0, 0, 1], vec![0, 1, 0], vec![1, 0, 0]];
    let signed_reversal = scale(&reversal, -1);
    assert_eq!(multiply(&signed_reversal, &signed_reversal), identity(3));
    let target_rotation = multiply(
        &signed_reversal,
        &multiply(&physical_rotation, &signed_reversal),
    );
    let target_reflection = multiply(
        &signed_reversal,
        &multiply(&physical_reflection, &signed_reversal),
    );
    let target_homology = multiply(&signed_reversal, &physical_homology);

    assert_eq!(
        target_rotation,
        vec![vec![0, 1, 0], vec![0, 0, 1], vec![1, 0, 0]]
    );
    assert_eq!(
        target_reflection,
        vec![vec![0, 1, 0], vec![1, 0, 0], vec![0, 0, 1]]
    );
    assert_eq!(
        target_homology,
        vec![vec![1, -1, 0], vec![-1, 0, 1], vec![0, 1, -1]]
    );
    assert_eq!(target_homology, multiply(&physical_homology, &reversal));

    BasisDictionary {
        physical_rotation,
        physical_reflection,
        physical_homology,
        target_rotation,
        target_reflection,
        target_homology,
    }
}

fn rational_rank(value: &Matrix) -> usize {
    if value.is_empty() || value[0].is_empty() {
        return 0;
    }
    let mut work: Vec<Vec<Rational>> = value
        .iter()
        .map(|row| {
            row.iter()
                .map(|&entry| Rational::new(i128::from(entry), 1))
                .collect()
        })
        .collect();
    let columns = work[0].len();
    let mut rank = 0;
    for column in 0..columns {
        let Some(pivot) = (rank..work.len()).find(|&row| !work[row][column].is_zero()) else {
            continue;
        };
        work.swap(rank, pivot);
        let pivot_value = work[rank][column].clone();
        for row in rank + 1..work.len() {
            if work[row][column].is_zero() {
                continue;
            }
            let factor = work[row][column].divide(&pivot_value);
            for entry in column..columns {
                work[row][entry] = work[row][entry].subtract(&factor.multiply(&work[rank][entry]));
            }
        }
        rank += 1;
        if rank == work.len() {
            break;
        }
    }
    rank
}

fn modulo_three(value: Int) -> Int {
    value.rem_euclid(3)
}

fn rank_modulo_three(value: &Matrix) -> usize {
    if value.is_empty() || value[0].is_empty() {
        return 0;
    }
    let mut work: Matrix = value
        .iter()
        .map(|row| row.iter().map(|&entry| modulo_three(entry)).collect())
        .collect();
    let columns = work[0].len();
    let mut rank = 0;
    for column in 0..columns {
        let Some(pivot) = (rank..work.len()).find(|&row| work[row][column] != 0) else {
            continue;
        };
        work.swap(rank, pivot);
        if work[rank][column] == 2 {
            for entry in &mut work[rank] {
                *entry = modulo_three(2 * *entry);
            }
        }
        for row in 0..work.len() {
            if row == rank || work[row][column] == 0 {
                continue;
            }
            let factor = work[row][column];
            for entry in column..columns {
                work[row][entry] = modulo_three(work[row][entry] - factor * work[rank][entry]);
            }
        }
        rank += 1;
        if rank == work.len() {
            break;
        }
    }
    rank
}

fn append_right_hand_side(equations: &[Equation]) -> Matrix {
    equations
        .iter()
        .map(|equation| {
            equation
                .coefficients
                .iter()
                .copied()
                .chain(std::iter::once(equation.right_hand_side))
                .collect()
        })
        .collect()
}

fn add_equation(
    equations: &mut Vec<Equation>,
    coefficients: Vec<Int>,
    right_hand_side: Int,
    label: String,
) {
    equations.push(Equation {
        coefficients,
        right_hand_side,
        label,
    });
}

fn variable(target: usize, edge: usize) -> usize {
    21 * target + edge
}

fn build_strict_map_system(
    d_b2: &Matrix,
    road_cycles: &Matrix,
    rotation_edges: &Matrix,
    reflection_edges: &Matrix,
    rotation_target: &Matrix,
    reflection_target: &Matrix,
    desired_homology: &Matrix,
) -> Vec<Equation> {
    let mut equations = Vec::new();

    // F d_2=0.
    for target in 0..3 {
        for facet in 0..6 {
            let mut coefficients = vec![0; 63];
            for edge in 0..21 {
                coefficients[variable(target, edge)] = d_b2[edge][facet];
            }
            add_equation(
                &mut equations,
                coefficients,
                0,
                format!("chain({target},{facet})"),
            );
        }
    }

    // The values land in K=ker epsilon.
    for edge in 0..21 {
        let mut coefficients = vec![0; 63];
        for target in 0..3 {
            coefficients[variable(target, edge)] = 1;
        }
        add_equation(&mut equations, coefficients, 0, format!("epsilon({edge})"));
    }

    // Strict D3 covariance A_target F = F A_edges.
    for (name, target_action, edge_action) in [
        ("r", rotation_target, rotation_edges),
        ("s", reflection_target, reflection_edges),
    ] {
        for target in 0..3 {
            for edge in 0..21 {
                let mut coefficients = vec![0; 63];
                for middle in 0..3 {
                    coefficients[variable(middle, edge)] += target_action[target][middle];
                }
                for middle in 0..21 {
                    coefficients[variable(target, middle)] -= edge_action[middle][edge];
                }
                add_equation(
                    &mut equations,
                    coefficients,
                    0,
                    format!("{name}-cov({target},{edge})"),
                );
            }
        }
    }

    // On the actual peripheral cycles, F is the independently fixed
    // saturated inverse transgression, with the established orientations.
    for target in 0..3 {
        for cycle in 0..3 {
            let mut coefficients = vec![0; 63];
            for edge in 0..21 {
                coefficients[variable(target, edge)] = road_cycles[edge][cycle];
            }
            add_equation(
                &mut equations,
                coefficients,
                desired_homology[target][cycle],
                format!("H1({target},{cycle})"),
            );
        }
    }
    equations
}

fn check_explicit_mod_three_witness(equations: &[Equation]) {
    // Coefficients are in F_3; 2 denotes -1.  This fixed combination of
    // source equations has zero left hand side and right hand side 1.
    const WITNESS: &[(Int, &str)] = &[
        (1, "chain(0,1)"),
        (1, "chain(0,3)"),
        (2, "chain(0,4)"),
        (1, "chain(0,5)"),
        (2, "chain(1,2)"),
        (1, "chain(1,3)"),
        (1, "chain(1,5)"),
        (2, "epsilon(1)"),
        (1, "epsilon(3)"),
        (2, "epsilon(6)"),
        (2, "epsilon(12)"),
        (1, "r-cov(0,0)"),
        (1, "r-cov(0,1)"),
        (2, "r-cov(0,2)"),
        (2, "r-cov(0,3)"),
        (2, "r-cov(0,4)"),
        (1, "r-cov(0,6)"),
        (2, "r-cov(0,7)"),
        (1, "r-cov(0,8)"),
        (2, "r-cov(0,11)"),
        (2, "r-cov(0,12)"),
        (2, "r-cov(0,14)"),
        (1, "r-cov(0,15)"),
        (1, "r-cov(0,16)"),
        (1, "r-cov(0,17)"),
        (1, "r-cov(1,1)"),
        (2, "r-cov(1,3)"),
        (1, "r-cov(1,6)"),
        (1, "r-cov(1,12)"),
        (2, "s-cov(0,0)"),
        (1, "s-cov(0,6)"),
        (1, "H1(0,0)"),
    ];
    let mut left_hand_side = vec![0; 63];
    let mut right_hand_side = 0;
    for &(scalar, label) in WITNESS {
        let equation = equations
            .iter()
            .find(|equation| equation.label == label)
            .unwrap_or_else(|| panic!("missing witness equation {label}"));
        for (target, &coefficient) in left_hand_side.iter_mut().zip(&equation.coefficients) {
            *target = modulo_three(*target + scalar * coefficient);
        }
        right_hand_side = modulo_three(right_hand_side + scalar * equation.right_hand_side);
    }
    assert_eq!(left_hand_side, vec![0; 63]);
    assert_eq!(right_hand_side, 1);
}

fn full_degree_one_variable(target: usize, generator: usize) -> usize {
    22 * target + generator
}

fn full_degree_zero_variable(vertex: usize) -> usize {
    66 + vertex
}

#[allow(clippy::too_many_arguments)]
fn build_full_cone_system(
    d_u2: &Matrix,
    d_u1: &Matrix,
    road_cycles: &Matrix,
    rotation_u1: &Matrix,
    reflection_u1: &Matrix,
    rotation_u0: &Matrix,
    reflection_u0: &Matrix,
    basis: &BasisDictionary,
) -> Vec<Equation> {
    let mut equations = Vec::new();

    // F_1 d_{U,2}=0.
    for target in 0..3 {
        for facet in 0..6 {
            let mut coefficients = vec![0; 80];
            for generator in 0..22 {
                coefficients[full_degree_one_variable(target, generator)] = d_u2[generator][facet];
            }
            add_equation(
                &mut equations,
                coefficients,
                0,
                format!("full-chain-2({target},{facet})"),
            );
        }
    }

    // epsilon F_1=F_0 d_{U,1}; unlike the minimal projection, individual
    // edge values need not lie in ker(epsilon).
    for generator in 0..22 {
        let mut coefficients = vec![0; 80];
        for target in 0..3 {
            coefficients[full_degree_one_variable(target, generator)] = 1;
        }
        for vertex in 0..14 {
            coefficients[full_degree_zero_variable(vertex)] -= d_u1[vertex][generator];
        }
        add_equation(
            &mut equations,
            coefficients,
            0,
            format!("full-chain-1({generator})"),
        );
    }

    // Equivariance of F_1 in the physical road basis.
    for (name, target_action, source_action) in [
        ("r", &basis.physical_rotation, rotation_u1),
        ("s", &basis.physical_reflection, reflection_u1),
    ] {
        for target in 0..3 {
            for generator in 0..22 {
                let mut coefficients = vec![0; 80];
                for middle in 0..3 {
                    coefficients[full_degree_one_variable(middle, generator)] +=
                        target_action[target][middle];
                }
                for middle in 0..22 {
                    coefficients[full_degree_one_variable(target, middle)] -=
                        source_action[middle][generator];
                }
                add_equation(
                    &mut equations,
                    coefficients,
                    0,
                    format!("full-{name}-cov-1({target},{generator})"),
                );
            }
        }
    }

    // Equivariance of F_0, whose target is the trivial module Z.
    for (name, source_action) in [("r", rotation_u0), ("s", reflection_u0)] {
        for vertex in 0..14 {
            let mut coefficients = vec![0; 80];
            coefficients[full_degree_zero_variable(vertex)] += 1;
            for middle in 0..14 {
                coefficients[full_degree_zero_variable(middle)] -= source_action[middle][vertex];
            }
            add_equation(
                &mut equations,
                coefficients,
                0,
                format!("full-{name}-cov-0({vertex})"),
            );
        }
    }

    // The induced map on the three peripheral cycles is the physical
    // M_AD=R-R^2.
    for target in 0..3 {
        for cycle in 0..3 {
            let mut coefficients = vec![0; 80];
            for edge in 0..21 {
                coefficients[full_degree_one_variable(target, edge)] = road_cycles[edge][cycle];
            }
            add_equation(
                &mut equations,
                coefficients,
                basis.physical_homology[target][cycle],
                format!("full-H1({target},{cycle})"),
            );
        }
    }

    equations
}

fn check_forced_mod_three_value(
    equations: &[Equation],
    coefficients: Vec<Int>,
    expected: Int,
    label: &str,
) {
    let coefficient_matrix: Matrix = equations
        .iter()
        .map(|equation| equation.coefficients.clone())
        .collect();
    let augmented_matrix = append_right_hand_side(equations);
    let coefficient_rank = rank_modulo_three(&coefficient_matrix);
    let augmented_rank = rank_modulo_three(&augmented_matrix);
    assert_eq!(coefficient_rank, augmented_rank);

    let mut compatible = equations.to_vec();
    add_equation(
        &mut compatible,
        coefficients.clone(),
        expected,
        format!("{label}-compatible"),
    );
    let compatible_coefficients: Matrix = compatible
        .iter()
        .map(|equation| equation.coefficients.clone())
        .collect();
    assert_eq!(
        rank_modulo_three(&compatible_coefficients),
        coefficient_rank
    );
    assert_eq!(
        rank_modulo_three(&append_right_hand_side(&compatible)),
        augmented_rank
    );

    let mut incompatible = equations.to_vec();
    add_equation(
        &mut incompatible,
        coefficients,
        expected + 1,
        format!("{label}-incompatible"),
    );
    let incompatible_coefficients: Matrix = incompatible
        .iter()
        .map(|equation| equation.coefficients.clone())
        .collect();
    assert_eq!(
        rank_modulo_three(&incompatible_coefficients),
        coefficient_rank
    );
    assert_eq!(
        rank_modulo_three(&append_right_hand_side(&incompatible)),
        augmented_rank + 1
    );
}

fn check_full_cone_lifts(
    equations: &[Equation],
    plus_vertex_index: usize,
    minus_vertex_index: usize,
) {
    assert_eq!(equations.len(), 209);
    assert!(equations
        .iter()
        .all(|equation| equation.coefficients.len() == 80));

    let coefficient_matrix: Matrix = equations
        .iter()
        .map(|equation| equation.coefficients.clone())
        .collect();
    let augmented_matrix = append_right_hand_side(equations);
    assert_eq!(rational_rank(&coefficient_matrix), 71);
    assert_eq!(rational_rank(&augmented_matrix), 71);
    assert_eq!(80 - rational_rank(&coefficient_matrix), 9);

    // One integral full-cone lift.  The last entry in each F_1 row is the
    // cone generator over v_+.  This representative has k=0 and ell=-1.
    let f1 = vec![
        vec![
            -6, -3, 3, 6, 0, 9, -6, -8, 2, -2, 6, -2, -2, 0, -2, -2, 2, -6, 0, 9, 8, 0,
        ],
        vec![
            -2, 6, 3, -9, 2, -2, -2, 2, -2, 9, -3, -6, 0, 2, 8, -6, 0, 8, 0, -6, -6, 0,
        ],
        vec![
            9, -3, -6, 2, -2, -6, 8, 6, 0, -6, -3, 8, 0, 0, -6, 9, -2, -2, -2, -2, -2, 0,
        ],
    ];
    let f0 = vec![-1, -2, -1, -1, -2, -2, -2, -2, -1, -2, 0, -2, -2, -2];
    let point: Vec<_> = f1.iter().flatten().chain(f0.iter()).copied().collect();
    assert_eq!(point.len(), 80);
    for equation in equations {
        let value: Int = equation
            .coefficients
            .iter()
            .zip(&point)
            .map(|(coefficient, entry)| coefficient * entry)
            .sum();
        assert_eq!(value, equation.right_hand_side, "{}", equation.label);
    }

    assert_eq!(plus_vertex_index, 10);
    assert_eq!(minus_vertex_index, 2);
    assert_eq!(f0[plus_vertex_index], 0);
    assert_eq!(f0[minus_vertex_index] - f0[plus_vertex_index], -1);
    assert_eq!(-1, 2 + 3 * (-1));
    assert_eq!([f1[0][21], f1[1][21], f1[2][21]], [0, 0, 0]);

    // Universally, equivariance makes the cone-generator value k(1,1,1),
    // hence F_0(v_+)=3k.  The full system also forces
    // F_0(v_-)-F_0(v_+)=2 (mod 3).
    let mut plus_value = vec![0; 80];
    plus_value[full_degree_zero_variable(plus_vertex_index)] = 1;
    check_forced_mod_three_value(equations, plus_value, 0, "endpoint-plus");

    let mut endpoint_difference = vec![0; 80];
    endpoint_difference[full_degree_zero_variable(minus_vertex_index)] = 1;
    endpoint_difference[full_degree_zero_variable(plus_vertex_index)] = -1;
    check_forced_mod_three_value(equations, endpoint_difference, 2, "endpoint-difference");
}

fn main() {
    let by_size = faces_by_size();
    let vertex_gauges = vertex_orientation_gauges(&by_size);
    let d_x2 = boundary_matrix(&by_size[1], &by_size[2], &vertex_gauges);
    let d_x1 = boundary_matrix(&by_size[2], &by_size[3], &vertex_gauges);
    let in_b = |face: &Dissection| face.iter().any(|&value| short_index(value).is_some());
    let b_facet_indices: Vec<_> = by_size[1]
        .iter()
        .enumerate()
        .filter(|(_, face)| in_b(face))
        .map(|(index, _)| index)
        .collect();
    let plus_vertex: Dissection = [1_usize, 3, 5]
        .into_iter()
        .map(|index| diagonal(index as u8, (index as u8 + 2) % N))
        .collect();
    let b_vertex_indices: Vec<_> = by_size[3]
        .iter()
        .enumerate()
        .filter(|(_, face)| **face != plus_vertex)
        .map(|(index, _)| index)
        .collect();
    let edge_indices: Vec<_> = (0..21).collect();
    let d_b2 = select_rows_and_columns(&d_x2, &edge_indices, &b_facet_indices);
    let d_b1 = select_rows_and_columns(&d_x1, &b_vertex_indices, &edge_indices);
    assert_eq!((d_b2.len(), d_b2[0].len()), (21, 6));
    assert_eq!((d_b1.len(), d_b1[0].len()), (13, 21));
    assert_eq!(multiply(&d_b1, &d_b2), zero(13, 6));
    assert_eq!(rational_rank(&d_b2), 6);
    assert_eq!(rational_rank(&d_b1), 13);
    assert_eq!(21 - rational_rank(&d_b2) - rational_rank(&d_b1), 2);

    let roads = [diagonal(1, 4), diagonal(0, 3), diagonal(2, 5)];
    let road_indices: Vec<_> = roads
        .iter()
        .map(|road| {
            by_size[1]
                .iter()
                .position(|face| face == &BTreeSet::from([*road]))
                .expect("road facet")
        })
        .collect();
    assert_eq!(road_indices, [4, 1, 7]);
    let road_cycles = select_rows_and_columns(&d_x2, &edge_indices, &road_indices);
    assert_eq!(multiply(&d_b1, &road_cycles), zero(13, 3));

    let rotation_signs = cellular_action_signs(&by_size, &vertex_gauges, rotate_vertex, 1);
    let reflection_signs = cellular_action_signs(&by_size, &vertex_gauges, reflect_vertex, -1);
    let rotation_edges = cellular_action_matrix(&by_size[2], &rotation_signs[2], rotate_vertex);
    let reflection_edges =
        cellular_action_matrix(&by_size[2], &reflection_signs[2], reflect_vertex);
    let rotation_vertices = cellular_action_matrix(&by_size[3], &rotation_signs[3], rotate_vertex);
    let reflection_vertices =
        cellular_action_matrix(&by_size[3], &reflection_signs[3], reflect_vertex);
    let basis = check_basis_dictionary(&road_cycles, &rotation_edges, &reflection_edges);

    // Keep the historical signed-reversed target basis so that the frozen
    // 32-row witness remains byte-for-byte checkable.
    let equations = build_strict_map_system(
        &d_b2,
        &road_cycles,
        &rotation_edges,
        &reflection_edges,
        &basis.target_rotation,
        &basis.target_reflection,
        &basis.target_homology,
    );
    assert_eq!(equations.len(), 174);
    assert!(equations
        .iter()
        .all(|equation| equation.coefficients.len() == 63));
    let coefficient_matrix: Matrix = equations
        .iter()
        .map(|equation| equation.coefficients.clone())
        .collect();
    let augmented_matrix = append_right_hand_side(&equations);

    assert_eq!(rational_rank(&coefficient_matrix), 59);
    assert_eq!(rational_rank(&augmented_matrix), 59);
    assert_eq!(63 - rational_rank(&coefficient_matrix), 4);
    assert_eq!(rank_modulo_three(&coefficient_matrix), 58);
    assert_eq!(rank_modulo_three(&augmented_matrix), 59);
    check_explicit_mod_three_witness(&equations);

    // Rebuild the same direct system in the physical road basis.  The signed
    // reversal is unimodular, so all four ranks, including the mod-three
    // inconsistency, agree.
    let physical_equations = build_strict_map_system(
        &d_b2,
        &road_cycles,
        &rotation_edges,
        &reflection_edges,
        &basis.physical_rotation,
        &basis.physical_reflection,
        &basis.physical_homology,
    );
    assert_eq!(physical_equations.len(), 174);
    let physical_coefficients: Matrix = physical_equations
        .iter()
        .map(|equation| equation.coefficients.clone())
        .collect();
    let physical_augmented = append_right_hand_side(&physical_equations);
    assert_eq!(rational_rank(&physical_coefficients), 59);
    assert_eq!(rational_rank(&physical_augmented), 59);
    assert_eq!(rank_modulo_three(&physical_coefficients), 58);
    assert_eq!(rank_modulo_three(&physical_augmented), 59);

    // Full mapping cone U=Cone(C(v_+)->C(B_short)).
    let plus_vertex_index = by_size[3]
        .iter()
        .position(|vertex| vertex == &plus_vertex)
        .expect("v_+ occurs");
    let minus_vertex: Dissection = [0_usize, 2, 4]
        .into_iter()
        .map(|index| diagonal(index as u8, (index as u8 + 2) % N))
        .collect();
    let minus_vertex_index = by_size[3]
        .iter()
        .position(|vertex| vertex == &minus_vertex)
        .expect("v_- occurs");

    let mut d_u2 = zero(22, 6);
    for row in 0..21 {
        d_u2[row].clone_from_slice(&d_b2[row]);
    }
    let mut d_u1 = zero(14, 22);
    for row in 0..14 {
        d_u1[row][..21].clone_from_slice(&d_x1[row]);
    }
    d_u1[plus_vertex_index][21] = 1;
    assert_eq!(multiply(&d_u1, &d_u2), zero(14, 6));

    let mut rotation_u1 = zero(22, 22);
    let mut reflection_u1 = zero(22, 22);
    for row in 0..21 {
        rotation_u1[row][..21].clone_from_slice(&rotation_edges[row]);
        reflection_u1[row][..21].clone_from_slice(&reflection_edges[row]);
    }
    rotation_u1[21][21] = 1;
    reflection_u1[21][21] = 1;

    let full_equations = build_full_cone_system(
        &d_u2,
        &d_u1,
        &road_cycles,
        &rotation_u1,
        &reflection_u1,
        &rotation_vertices,
        &reflection_vertices,
        &basis,
    );
    check_full_cone_lifts(&full_equations, plus_vertex_index, minus_vertex_index);

    println!(
        "{}",
        concat!(
            r#"{"claim":"For the actual labelled K6 cellular quotient P=C_*(B_short)/C_*(v_+), no integral strict D3-equivariant chain map P->ker(epsilon)[1] induces the fixed primitive Alexander-dual map. This direct-minimal no-go holds in the physical road basis with M_AD=R-R^2 and, equivalently, in the signed reversed target basis used by the frozen witness. In contrast, integral D3-equivariant maps from the full cone U to the augmented target T do exist.","status":"falsified","assumptions":["K6 incidence signs and D3 actions are reconstructed from the labelled face poset with the established ambient orientation","physical road order is F14,F03,F25, with R(q_i)=q_(i+1), physical reflection fixing q0, and M_AD=R-R^2","the historical matrix [[1,-1,0],[-1,0,1],[0,1,-1]] is expressed in qbar=(-q2,-q1,-q0), not in the physical road basis","D3 covariance is strict over Z and no 1/3 localization is allowed","the endpoint-unit equation F0(v_+)=1 is not part of either the minimal or unframed full-cone system"],"factorization_test":{"basis_dictionary":"J swaps 0 and 2; qbar=-Jq; Rbar=JRJ=R^-1; sbar=JsJ; M1=-J(R-R^2)=(R-R^2)J","entry115_reconciliation":"on the actual ordered long-facet boundary cycles, (1-R)R=R-R^2","P_chain_ranks":"C2/C1/C0 = 6/21/13","P_differential_ranks":"rank d2=6, rank d1=13, H1 rank=2","direct_strict_system":"174 equations in 63 variables","direct_rational_system":"coefficient rank=augmented rank=59; affine dimension=4","direct_mod3_system":"coefficient rank=58, augmented rank=59 in both physical and signed-reversed bases","explicit_witness":"32 frozen source equations sum over F3 to left side 0 and right side 1 in the signed-reversed basis","strict_integral_minimal_projection":"empty","full_cone_system":"209 equations in 80 variables; coefficient rank=augmented rank=71; nonempty integral affine lattice of rank 9","full_cone_example":"explicit integral lift with ell=-1, F0(v_+)=0, and F0(v_-)-F0(v_+)=-1","full_cone_endpoint_formulas":"F0(v_+)=3k and F0(v_-)-F0(v_+)=2+3ell","endpoint_unit_framing_ablation":"only the extra demand F0(v_+)=1 gives 3k=1; it does not obstruct unframed U->T lifts","derived_roof_or_butterfly":"not tested and not falsified"},"counterevidence":["The full augmented cone admits integral equivariant lifts; therefore the direct-minimal obstruction must not be promoted to a full-cone nonexistence claim.","The homological complementary-boundary Alexander duality and saturated first transgression remain integral isomorphisms.","The direct rational system is nonempty, so its failure is 3-primary rather than a rank obstruction.","Forgetting F0 and requiring every edge value to lie in ker(epsilon) is exactly the extra strict projection condition that distinguishes P->K[1] from U->T."],"sharp_blocker":"Select and compare a pointed relative AW/cap framing inside the nonempty rank-nine full-cone lift lattice; existence of an unframed full-cone lift is no longer a blocker.","next_experiment":"Construct the pointed D3-equivariant relative AW/cap roof or butterfly, identify its endpoint framing and cone-connector coherences inside the full-cone lift lattice, and only then compute the residual reflection parity."}"#
        )
    );
}
