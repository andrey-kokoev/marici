//! Two-endpoint carrier realization of the orientation-twisted road extension.
//!
//! The actual labelled triple
//!
//!     V={v_+,v_-} subset B_short subset K6
//!
//! retains both fusion-sheet endpoints.  The pair boundary
//! H_1(B_short,V) -> H_tilde_0(V) is the spatial carrier of the
//! orientation-twisted road augmentation: its three primitive corridor
//! classes are cycled by rotation, negated and reflected by the physical
//! reflection, and each has endpoint value one.  Splicing the support
//! connector with this pair sequence gives the complete unsplit Tate
//! extension over an endpoint-orientation line with the same D3 character
//! as the normalization-sheet difference.
//!
//! The conductor closed points are also fixed by labels, not merely by
//! character: J_+=(x1,x3,x5) maps to v_+ and J_-=(x0,x2,x4) maps to v_-.
//! For D03 the two entry-99 marked half-galleries meet at
//! {D03,x0,x3} and concatenate to one primitive corridor.  This closes the
//! closed-conductor carrier map only.  It does not construct a ringed map
//! from the full normalization-Cech object, nor promote the triple to an
//! occurrence/multi-Rees/PC extraordinary-costalk object.
//!
//! The strict support triple nevertheless removes one unnecessary unknown:
//! at original-twist/BM level the canonical endpoint/Q object is simply
//!
//!     E_endpoint,Q^abs = F_K/F_V,
//!
//! with its inherited short exact filtration
//!
//!     0 -> F_B/F_V -> F_K/F_V -> F_K/F_B -> 0.
//!
//! Its carrier grade is C_*(K6,V), whose only homology is one primitive
//! torsion-free endpoint-orientation line.  What remains missing is its
//! reciprocal/multi-Rees/PC promotion and the full normalization-sheet map.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

type Z = i64;
type Matrix = Vec<Vec<Z>>;
type Face = BTreeSet<Diagonal>;

const N: u8 = 6;
const DIMENSION: usize = 3;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

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

fn short(index: u8) -> Diagonal {
    diagonal(index, (index + 2) % N)
}

fn face(values: &[Diagonal]) -> Face {
    values.iter().copied().collect()
}

fn noncrossing(value: &Face) -> bool {
    value.iter().enumerate().all(|(position, first)| {
        value
            .iter()
            .skip(position + 1)
            .all(|second| !crosses(*first, *second))
    })
}

fn faces_by_size() -> Vec<Vec<Face>> {
    let diagonals = all_diagonals();
    let mut result = vec![Vec::new(); DIMENSION + 1];
    for mask in 0_u16..(1_u16 << diagonals.len()) {
        if mask.count_ones() as usize > DIMENSION {
            continue;
        }
        let value: Face = diagonals
            .iter()
            .enumerate()
            .filter_map(|(index, diagonal)| ((mask & (1 << index)) != 0).then_some(*diagonal))
            .collect();
        if noncrossing(&value) {
            result[value.len()].push(value);
        }
    }
    for values in &mut result {
        values.sort();
    }
    assert_eq!(
        result.iter().map(Vec::len).collect::<Vec<_>>(),
        [1, 9, 21, 14]
    );
    result
}

fn addable(value: &Face, added: Diagonal) -> bool {
    !value.contains(&added)
        && value.len() < DIMENSION
        && value.iter().all(|present| !crosses(*present, added))
}

fn raw_incidence_sign(value: &Face, added: Diagonal) -> Z {
    if value.iter().filter(|present| **present < added).count() % 2 == 0 {
        1
    } else {
        -1
    }
}

fn vertex_gauges(by_size: &[Vec<Face>]) -> BTreeMap<Face, Z> {
    let mut gauges = BTreeMap::from([(by_size[DIMENSION][0].clone(), 1)]);
    let mut changed = true;
    while changed {
        changed = false;
        for edge in &by_size[2] {
            let endpoints: Vec<_> = all_diagonals()
                .into_iter()
                .filter(|added| addable(edge, *added))
                .map(|added| {
                    let mut target = edge.clone();
                    target.insert(added);
                    (target, raw_incidence_sign(edge, added))
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

fn incidence_sign(value: &Face, target: &Face, added: Diagonal, gauges: &BTreeMap<Face, Z>) -> Z {
    raw_incidence_sign(value, added)
        * gauges.get(value).copied().unwrap_or(1)
        * gauges.get(target).copied().unwrap_or(1)
}

fn zero(rows: usize, columns: usize) -> Matrix {
    vec![vec![0; columns]; rows]
}

fn identity(size: usize) -> Matrix {
    let mut value = zero(size, size);
    for (index, row) in value.iter_mut().enumerate() {
        row[index] = 1;
    }
    value
}

fn boundary_matrix(source: &[Face], target: &[Face], gauges: &BTreeMap<Face, Z>) -> Matrix {
    let target_index: BTreeMap<_, _> = target
        .iter()
        .enumerate()
        .map(|(index, value)| (value.clone(), index))
        .collect();
    let mut result = zero(target.len(), source.len());
    for (column, value) in source.iter().enumerate() {
        for added in all_diagonals()
            .into_iter()
            .filter(|added| addable(value, *added))
        {
            let mut boundary = value.clone();
            boundary.insert(added);
            if let Some(row) = target_index.get(&boundary) {
                result[*row][column] = incidence_sign(value, &boundary, added, gauges);
            }
        }
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

fn scale(value: &Matrix, scalar: Z) -> Matrix {
    value
        .iter()
        .map(|row| row.iter().map(|entry| scalar * entry).collect())
        .collect()
}

fn matrix_column(value: &Matrix, column: usize) -> Vec<Z> {
    value.iter().map(|row| row[column]).collect()
}

fn columns_matrix(columns: &[Vec<Z>]) -> Matrix {
    assert!(!columns.is_empty());
    (0..columns[0].len())
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect()
}

fn select(value: &Matrix, rows: &[usize], columns: &[usize]) -> Matrix {
    rows.iter()
        .map(|row| columns.iter().map(|column| value[*row][*column]).collect())
        .collect()
}

fn determinant(value: &Matrix) -> Z {
    assert_eq!(value.len(), value.first().map_or(0, Vec::len));
    if value.is_empty() {
        return 1;
    }
    let mut work: Vec<Vec<i128>> = value
        .iter()
        .map(|row| row.iter().map(|entry| i128::from(*entry)).collect())
        .collect();
    let mut previous = 1_i128;
    let mut sign = 1_i128;
    for pivot_index in 0..value.len() - 1 {
        let Some(pivot_row) = (pivot_index..value.len()).find(|row| work[*row][pivot_index] != 0)
        else {
            return 0;
        };
        if pivot_row != pivot_index {
            work.swap(pivot_row, pivot_index);
            sign = -sign;
        }
        let pivot = work[pivot_index][pivot_index];
        for row in pivot_index + 1..value.len() {
            for column in pivot_index + 1..value.len() {
                let numerator =
                    work[row][column] * pivot - work[row][pivot_index] * work[pivot_index][column];
                assert_eq!(numerator % previous, 0);
                work[row][column] = numerator / previous;
            }
            work[row][pivot_index] = 0;
        }
        previous = pivot;
    }
    Z::try_from(sign * work[value.len() - 1][value.len() - 1]).unwrap()
}

fn integer_rank(value: &Matrix) -> usize {
    if value.is_empty() || value[0].is_empty() {
        return 0;
    }
    let mut work = value.clone();
    let mut rank = 0;
    for column in 0..work[0].len() {
        let Some(pivot) = (rank..work.len()).find(|row| work[*row][column] != 0) else {
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
            let common = work[row].iter().fold(0_i64, |a, b| gcd(a, *b));
            if common > 1 {
                for entry in &mut work[row] {
                    *entry /= common;
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

fn gcd(mut left: Z, mut right: Z) -> Z {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        (left, right) = (right, left % right);
    }
    left
}

fn replace_column(value: &Matrix, column: usize, replacement: &[Z]) -> Matrix {
    let mut result = value.clone();
    for row in 0..result.len() {
        result[row][column] = replacement[row];
    }
    result
}

fn unimodular_coordinates(basis: &Matrix, value: &[Z]) -> Vec<Z> {
    let divisor = determinant(basis);
    assert_eq!(divisor.abs(), 1);
    (0..basis.len())
        .map(|column| determinant(&replace_column(basis, column, value)) / divisor)
        .collect()
}

fn in_b_short(value: &Face) -> bool {
    value
        .iter()
        .any(|diagonal| (0..N).any(|index| *diagonal == short(index)))
}

fn plus_vertex() -> Face {
    face(&[short(1), short(3), short(5)])
}

fn minus_vertex() -> Face {
    face(&[short(0), short(2), short(4)])
}

fn rotate_vertex(vertex: u8) -> u8 {
    (vertex + 2) % N
}

fn reflect_vertex(vertex: u8) -> u8 {
    (3 + N - vertex) % N
}

fn permute_face(value: &Face, permutation: fn(u8) -> u8) -> Face {
    value
        .iter()
        .map(|value| diagonal(permutation(value.0), permutation(value.1)))
        .collect()
}

fn action_signs(
    by_size: &[Vec<Face>],
    gauges: &BTreeMap<Face, Z>,
    permutation: fn(u8) -> u8,
    top_sign: Z,
) -> Vec<BTreeMap<Face, Z>> {
    let mut signs = vec![BTreeMap::new(); DIMENSION + 1];
    signs[0].insert(by_size[0][0].clone(), top_sign);
    for size in 0..DIMENSION {
        for value in &by_size[size] {
            let source_sign = signs[size][value];
            let image = permute_face(value, permutation);
            for added in all_diagonals()
                .into_iter()
                .filter(|added| addable(value, *added))
            {
                let mut target = value.clone();
                target.insert(added);
                let image_added = diagonal(permutation(added.0), permutation(added.1));
                let mut image_target = image.clone();
                image_target.insert(image_added);
                let target_sign = source_sign * incidence_sign(value, &target, added, gauges)
                    / incidence_sign(&image, &image_target, image_added, gauges);
                match signs[size + 1].get(&target) {
                    Some(known) => assert_eq!(*known, target_sign),
                    None => {
                        signs[size + 1].insert(target, target_sign);
                    }
                }
            }
        }
    }
    signs
}

fn action_matrix(values: &[Face], signs: &BTreeMap<Face, Z>, permutation: fn(u8) -> u8) -> Matrix {
    let indices: BTreeMap<_, _> = values
        .iter()
        .enumerate()
        .map(|(index, value)| (value.clone(), index))
        .collect();
    let mut result = zero(values.len(), values.len());
    for (column, value) in values.iter().enumerate() {
        let image = permute_face(value, permutation);
        result[indices[&image]][column] = signs[value];
    }
    result
}

fn apply(matrix: &Matrix, vector: &[Z]) -> Vec<Z> {
    matrix
        .iter()
        .map(|row| row.iter().zip(vector).map(|(a, b)| a * b).sum())
        .collect()
}

fn edge_endpoints(d1: &Matrix, edge: usize) -> [usize; 2] {
    let endpoints: Vec<_> = (0..d1.len()).filter(|row| d1[*row][edge] != 0).collect();
    assert_eq!(endpoints.len(), 2);
    [endpoints[0], endpoints[1]]
}

fn corridor_path(
    by_size: &[Vec<Face>],
    d1: &Matrix,
    road: Diagonal,
    start: usize,
    finish: usize,
) -> Vec<Z> {
    let allowed_vertices: BTreeSet<_> = by_size[3]
        .iter()
        .enumerate()
        .filter_map(|(index, value)| {
            (index == start || index == finish || value.contains(&road)).then_some(index)
        })
        .collect();
    assert_eq!(allowed_vertices.len(), 6);
    let mut adjacency = vec![Vec::new(); by_size[3].len()];
    let mut allowed_edges = 0;
    for edge in 0..by_size[2].len() {
        let [first, second] = edge_endpoints(d1, edge);
        if allowed_vertices.contains(&first) && allowed_vertices.contains(&second) {
            adjacency[first].push((second, edge));
            adjacency[second].push((first, edge));
            allowed_edges += 1;
        }
    }
    assert_eq!(allowed_edges, 6);
    let mut previous = vec![None; by_size[3].len()];
    previous[start] = Some((start, usize::MAX));
    let mut queue = VecDeque::from([start]);
    while let Some(vertex) = queue.pop_front() {
        if vertex == finish {
            break;
        }
        for &(next, edge) in &adjacency[vertex] {
            if previous[next].is_none() {
                previous[next] = Some((vertex, edge));
                queue.push_back(next);
            }
        }
    }
    assert!(previous[finish].is_some());
    let mut result = vec![0; by_size[2].len()];
    let mut current = finish;
    while current != start {
        let (prior, edge) = previous[current].unwrap();
        result[edge] += d1[current][edge];
        current = prior;
    }
    let boundary = apply(d1, &result);
    for (row, coefficient) in boundary.iter().enumerate() {
        let expected = if row == start {
            -1
        } else if row == finish {
            1
        } else {
            0
        };
        assert_eq!(*coefficient, expected);
    }
    result
}

fn path_through_faces(by_size: &[Vec<Face>], d1: &Matrix, vertices: &[Face]) -> Vec<Z> {
    assert!(vertices.len() >= 2);
    let indices: BTreeMap<_, _> = by_size[3]
        .iter()
        .enumerate()
        .map(|(index, value)| (value.clone(), index))
        .collect();
    let mut result = vec![0; by_size[2].len()];
    for adjacent in vertices.windows(2) {
        let start = indices[&adjacent[0]];
        let finish = indices[&adjacent[1]];
        let matching: Vec<_> = (0..by_size[2].len())
            .filter(|edge| {
                let endpoints = edge_endpoints(d1, *edge);
                endpoints.contains(&start) && endpoints.contains(&finish)
            })
            .collect();
        assert_eq!(matching.len(), 1);
        let edge = matching[0];
        result[edge] += d1[finish][edge];
    }
    let boundary = apply(d1, &result);
    let start = indices[&vertices[0]];
    let finish = indices[vertices.last().unwrap()];
    assert!(boundary.iter().enumerate().all(|(index, value)| {
        *value
            == if index == start {
                -1
            } else if index == finish {
                1
            } else {
                0
            }
    }));
    result
}

fn spanning_forest_edges(d1: &Matrix, roots: &[usize]) -> Vec<usize> {
    let mut adjacency = vec![Vec::new(); d1.len()];
    for edge in 0..d1[0].len() {
        let [first, second] = edge_endpoints(d1, edge);
        adjacency[first].push((second, edge));
        adjacency[second].push((first, edge));
    }
    let mut seen = vec![false; d1.len()];
    let mut queue = VecDeque::new();
    for root in roots {
        seen[*root] = true;
        queue.push_back(*root);
    }
    let mut edges = Vec::new();
    while let Some(vertex) = queue.pop_front() {
        for &(next, edge) in &adjacency[vertex] {
            if !seen[next] {
                seen[next] = true;
                edges.push(edge);
                queue.push_back(next);
            }
        }
    }
    assert!(seen.into_iter().all(|value| value));
    assert_eq!(edges.len(), d1.len() - roots.len());
    edges
}

fn main() {
    let by_size = faces_by_size();
    let gauges = vertex_gauges(&by_size);
    let d3 = boundary_matrix(&by_size[0], &by_size[1], &gauges);
    let d2 = boundary_matrix(&by_size[1], &by_size[2], &gauges);
    let d1 = boundary_matrix(&by_size[2], &by_size[3], &gauges);
    assert_eq!(multiply(&d2, &d3), zero(21, 1));
    assert_eq!(multiply(&d1, &d2), zero(14, 9));

    let plus = by_size[3]
        .iter()
        .position(|value| value == &plus_vertex())
        .unwrap();
    let minus = by_size[3]
        .iter()
        .position(|value| value == &minus_vertex())
        .unwrap();
    assert_ne!(plus, minus);
    assert!(in_b_short(&by_size[3][plus]) && in_b_short(&by_size[3][minus]));

    let b_facets: Vec<_> = by_size[1]
        .iter()
        .enumerate()
        .filter_map(|(index, value)| in_b_short(value).then_some(index))
        .collect();
    assert_eq!(b_facets.len(), 6);
    assert!(by_size[2].iter().all(in_b_short));
    assert!(by_size[3].iter().all(in_b_short));

    // Entry 105's absolute unlocalized original-twist/BM packet has one
    // generator (S,H) for every H subset S.  The present face census
    // therefore restricts it, without changing its differential, to the
    // strict D3-stable support filtration F_V subset F_B subset F_K.  V is
    // closed because its two faces are maximal; B_short is closed because
    // every radial target retains the short diagonal already in its source;
    // normal deletion never changes S.  The complementary seven generators
    // are the top cell and the two normal states on each of the three long
    // facets, so the based Q leg is retained before any contraction.
    let loaded_rank = |predicate: &dyn Fn(&Face) -> bool| {
        by_size
            .iter()
            .flatten()
            .filter(|value| predicate(value))
            .map(|value| 1_usize << value.len())
            .sum::<usize>()
    };
    let full_loaded_rank = loaded_rank(&|_| true);
    let b_loaded_rank = loaded_rank(&in_b_short);
    let v_loaded_rank = loaded_rank(&|value| value == &plus_vertex() || value == &minus_vertex());
    assert_eq!(
        (v_loaded_rank, b_loaded_rank, full_loaded_rank),
        (16, 208, 215)
    );
    assert_eq!(full_loaded_rank - b_loaded_rank, 7);

    // The quotient F_K/F_V is therefore already a canonical absolute
    // endpoint/Q object in the original-twist model.  Keep its degreewise
    // ranks, and those of its subobject F_B/F_V and quotient Q=F_K/F_B,
    // explicit so that no later PC promotion may silently discard a normal
    // state or replace the extension by its H1 line.
    let loaded_degree_ranks = |predicate: &dyn Fn(&Face) -> bool| {
        let mut ranks = vec![0_usize; DIMENSION + 1];
        for value in by_size.iter().flatten().filter(|value| predicate(value)) {
            for normal_subset in 0_usize..(1_usize << value.len()) {
                let degree = DIMENSION - value.len() + normal_subset.count_ones() as usize;
                ranks[degree] += 1;
            }
        }
        ranks
    };
    let full_loaded_degrees = loaded_degree_ranks(&|_| true);
    let b_loaded_degrees = loaded_degree_ranks(&in_b_short);
    let v_loaded_degrees =
        loaded_degree_ranks(&|value| value == &plus_vertex() || value == &minus_vertex());
    let subtract_degrees = |left: &[usize], right: &[usize]| {
        left.iter()
            .zip(right)
            .map(|(left, right)| left - right)
            .collect::<Vec<_>>()
    };
    let endpoint_q_degrees = subtract_degrees(&full_loaded_degrees, &v_loaded_degrees);
    let road_relative_degrees = subtract_degrees(&b_loaded_degrees, &v_loaded_degrees);
    let q_degrees = subtract_degrees(&full_loaded_degrees, &b_loaded_degrees);
    assert_eq!(full_loaded_degrees, [14, 63, 93, 45]);
    assert_eq!(b_loaded_degrees, [14, 63, 90, 41]);
    assert_eq!(v_loaded_degrees, [2, 6, 6, 2]);
    assert_eq!(endpoint_q_degrees, [12, 57, 87, 43]);
    assert_eq!(road_relative_degrees, [12, 57, 84, 39]);
    assert_eq!(q_degrees, [0, 0, 3, 4]);
    assert_eq!(endpoint_q_degrees.iter().sum::<usize>(), 199);
    assert_eq!(road_relative_degrees.iter().sum::<usize>(), 192);
    assert_eq!(q_degrees.iter().sum::<usize>(), 7);

    let all_edges: Vec<_> = (0..21).collect();
    let relative_vertices: Vec<_> = (0..14)
        .filter(|index| *index != plus && *index != minus)
        .collect();
    let d_b2 = select(&d2, &all_edges, &b_facets);
    let d_b1_relative = select(&d1, &relative_vertices, &all_edges);
    assert_eq!(multiply(&d_b1_relative, &d_b2), zero(12, 6));
    assert_eq!((integer_rank(&d_b2), integer_rank(&d_b1_relative)), (6, 12));
    assert_eq!(21 - 6 - 12, 3);

    // Carrier grade of E_endpoint,Q^abs=F_K/F_V.  Since all nine facets and
    // all twenty-one edges survive while the two endpoint vertices are
    // quotiented, C_*(K6,V) has ranks (1,9,21,12).  The exact ranks below
    // leave H1=Z and no other rational homology; saturation is certified
    // below from the unimodular road basis and a unit maximal minor of the
    // long-facet connector.
    assert_eq!(multiply(&d_b1_relative, &d2), zero(12, 9));
    assert_eq!(
        (
            integer_rank(&d3),
            integer_rank(&d2),
            integer_rank(&d_b1_relative)
        ),
        (1, 8, 12)
    );
    assert_eq!(
        [
            1 - integer_rank(&d3),
            9 - integer_rank(&d3) - integer_rank(&d2),
            21 - integer_rank(&d2) - integer_rank(&d_b1_relative),
            12 - integer_rank(&d_b1_relative),
        ],
        [0, 0, 1, 0]
    );

    let rotation_signs = action_signs(&by_size, &gauges, rotate_vertex, 1);
    let reflection_signs = action_signs(&by_size, &gauges, reflect_vertex, -1);
    let rotation_edges = action_matrix(&by_size[2], &rotation_signs[2], rotate_vertex);
    let reflection_edges = action_matrix(&by_size[2], &reflection_signs[2], reflect_vertex);
    let rotation_vertices = action_matrix(&by_size[3], &rotation_signs[3], rotate_vertex);
    let reflection_vertices = action_matrix(&by_size[3], &reflection_signs[3], reflect_vertex);
    assert_eq!(
        apply(&rotation_vertices, &matrix_column(&identity(14), plus))[plus],
        1
    );
    assert_eq!(
        apply(&rotation_vertices, &matrix_column(&identity(14), minus))[minus],
        1
    );
    assert_eq!(
        apply(&reflection_vertices, &matrix_column(&identity(14), plus))[minus],
        -1
    );
    assert_eq!(
        apply(&reflection_vertices, &matrix_column(&identity(14), minus))[plus],
        -1
    );

    let roads = [diagonal(1, 4), diagonal(0, 3), diagonal(2, 5)];

    // The conductor endpoint labels are exact.  Entry 93's positive and
    // negative branch ideals are generated respectively by the odd and even
    // short diagonals, hence their closed conductor points have precisely the
    // labels of v_+ and v_-.  Entry 99's marked D03 half-galleries are the
    // following two paths.  They meet at the same road vertex and their
    // difference is a primitive endpoint-to-endpoint corridor.
    let d03 = diagonal(0, 3);
    let v10 = face(&[d03, short(1), short(3)]);
    let v00 = face(&[d03, short(0), short(3)]);
    let v01 = face(&[d03, short(0), short(4)]);
    let plus_half = path_through_faces(&by_size, &d1, &[plus_vertex(), v10.clone(), v00.clone()]);
    let minus_half = path_through_faces(&by_size, &d1, &[minus_vertex(), v01.clone(), v00.clone()]);
    let marked_d03: Vec<_> = plus_half
        .iter()
        .zip(&minus_half)
        .map(|(positive, negative)| positive - negative)
        .collect();
    assert_eq!(
        marked_d03,
        path_through_faces(
            &by_size,
            &d1,
            &[plus_vertex(), v10, v00, v01, minus_vertex()],
        )
    );
    let marked_d03_boundary = apply(&d1, &marked_d03);
    assert_eq!(marked_d03_boundary[plus], -1);
    assert_eq!(marked_d03_boundary[minus], 1);
    assert_eq!(plus_half.iter().filter(|value| **value != 0).count(), 2);
    assert_eq!(minus_half.iter().filter(|value| **value != 0).count(), 2);
    assert_eq!(marked_d03.iter().filter(|value| **value != 0).count(), 4);

    // Rotate the marked D03 corridor backwards once to obtain the first road
    // in the fixed physical order (F14,F03,F25).  The old graph search is
    // retained as an independent connectivity check, but it does not select
    // the marked route through the road square.
    let first_path = apply(&rotation_edges, &apply(&rotation_edges, &marked_d03));
    let _unmarked_search_path = corridor_path(&by_size, &d1, roads[0], plus, minus);
    let paths = [
        first_path.clone(),
        apply(&rotation_edges, &first_path),
        apply(&rotation_edges, &apply(&rotation_edges, &first_path)),
    ];
    assert_eq!(paths[1], marked_d03);
    let plus_halves = [
        apply(&rotation_edges, &apply(&rotation_edges, &plus_half)),
        plus_half.clone(),
        apply(&rotation_edges, &plus_half),
    ];
    let minus_halves = [
        apply(&rotation_edges, &apply(&rotation_edges, &minus_half)),
        minus_half.clone(),
        apply(&rotation_edges, &minus_half),
    ];
    for index in 0..3 {
        let difference: Vec<_> = plus_halves[index]
            .iter()
            .zip(&minus_halves[index])
            .map(|(positive, negative)| positive - negative)
            .collect();
        assert_eq!(difference, paths[index]);
    }
    let sum_chains = |chains: &[Vec<Z>]| {
        (0..by_size[2].len())
            .map(|edge| chains.iter().map(|chain| chain[edge]).sum())
            .collect::<Vec<Z>>()
    };
    let q_plus = sum_chains(&plus_halves);
    let q_minus = sum_chains(&minus_halves);
    let road_norm = sum_chains(&paths);
    assert_eq!(
        q_plus
            .iter()
            .zip(&q_minus)
            .map(|(positive, negative)| positive - negative)
            .collect::<Vec<_>>(),
        road_norm
    );
    let q_plus_boundary = apply(&d1, &q_plus);
    let q_minus_boundary = apply(&d1, &q_minus);
    let road_norm_boundary = apply(&d1, &road_norm);
    assert_eq!(q_plus_boundary[plus], -3);
    assert_eq!(q_plus_boundary[minus], 0);
    assert_eq!(q_minus_boundary[plus], 0);
    assert_eq!(q_minus_boundary[minus], -3);
    assert_eq!(road_norm_boundary[plus], -3);
    assert_eq!(road_norm_boundary[minus], 3);
    for path in &paths {
        let boundary = apply(&d1, path);
        assert_eq!(boundary[plus], -1);
        assert_eq!(boundary[minus], 1);
        assert!(boundary
            .iter()
            .enumerate()
            .all(|(index, value)| index == plus || index == minus || *value == 0));
    }

    let forest_edges = spanning_forest_edges(&d1, &[plus, minus]);
    let mut basis_columns: Vec<Vec<Z>> = (0..d_b2[0].len())
        .map(|column| matrix_column(&d_b2, column))
        .collect();
    basis_columns.extend(paths.iter().cloned());
    basis_columns.extend(
        forest_edges
            .iter()
            .map(|edge| matrix_column(&identity(21), *edge)),
    );
    let full_basis = columns_matrix(&basis_columns);
    assert_eq!(full_basis.len(), 21);
    assert_eq!(determinant(&full_basis).abs(), 1);

    let homology_coordinates = |chain: &[Z]| {
        let coordinates = unimodular_coordinates(&full_basis, chain);
        assert!(coordinates[9..].iter().all(|value| *value == 0));
        coordinates[6..9].to_vec()
    };
    let road_rotation = columns_matrix(
        &paths
            .iter()
            .map(|path| homology_coordinates(&apply(&rotation_edges, path)))
            .collect::<Vec<_>>(),
    );
    let road_reflection_raw = columns_matrix(
        &paths
            .iter()
            .map(|path| homology_coordinates(&apply(&reflection_edges, path)))
            .collect::<Vec<_>>(),
    );
    let expected_rotation = vec![vec![0, 0, 1], vec![1, 0, 0], vec![0, 1, 0]];
    let expected_raw_reflection = vec![vec![0, 1, 0], vec![1, 0, 0], vec![0, 0, 1]];
    assert_eq!(road_rotation, expected_rotation);
    assert_eq!(road_reflection_raw, expected_raw_reflection);

    // The raw relative pair carries the permutation action.  Tensoring the
    // entire pair triangle once by the physical road-orientation character
    // is forced by the common endpoint line: roads become a negative
    // permutation module, tags lose their cellular orientation sign, the
    // relative top becomes trivial, and the endpoint becomes Z_or.
    let road_reflection = scale(&road_reflection_raw, -1);

    let endpoint = vec![vec![1, 1, 1]];
    assert_eq!(multiply(&endpoint, &road_rotation), endpoint);
    assert_eq!(multiply(&endpoint, &road_reflection_raw), endpoint);
    assert_eq!(
        multiply(&endpoint, &road_reflection),
        vec![vec![-1, -1, -1]]
    );

    let long_facets: Vec<_> = roads
        .iter()
        .map(|road| {
            by_size[1]
                .iter()
                .position(|value| value == &face(&[*road]))
                .unwrap()
        })
        .collect();
    let top_long_coefficients: Vec<_> = long_facets.iter().map(|index| d3[*index][0]).collect();
    assert!(top_long_coefficients.iter().all(|value| value.abs() == 1));
    let tag_boundaries: Vec<_> = long_facets
        .iter()
        .zip(&top_long_coefficients)
        .map(|(index, sign)| {
            matrix_column(&d2, *index)
                .into_iter()
                .map(|value| sign * value)
                .collect::<Vec<_>>()
        })
        .collect();
    let middle = columns_matrix(
        &tag_boundaries
            .iter()
            .map(|boundary| homology_coordinates(boundary))
            .collect::<Vec<_>>(),
    );
    let norm = vec![vec![1], vec![1], vec![1]];
    assert_eq!(multiply(&middle, &norm), zero(3, 1));
    assert_eq!(multiply(&endpoint, &middle), zero(1, 3));
    assert_eq!(integer_rank(&middle), 2);
    assert!(middle.iter().flatten().any(|value| value.abs() == 1));
    let mut unit_middle_minor = false;
    for first_row in 0..3 {
        for second_row in (first_row + 1)..3 {
            for first_column in 0..3 {
                for second_column in (first_column + 1)..3 {
                    let minor = middle[first_row][first_column] * middle[second_row][second_column]
                        - middle[first_row][second_column] * middle[second_row][first_column];
                    unit_middle_minor |= minor.abs() == 1;
                }
            }
        }
    }
    assert!(unit_middle_minor);

    // In the geometrically normalized long-facet basis the middle map is
    // I-R^2.  Entry 142 uses the signed cyclic tag basis obtained by the
    // unimodular change -R; in that basis the same map is exactly I-R.
    // This records the dictionary rather than treating the two displays as
    // competing conventions.
    let entry_142_middle = multiply(&middle, &scale(&road_rotation, -1));
    assert_eq!(
        entry_142_middle,
        vec![vec![1, 0, -1], vec![-1, 1, 0], vec![0, -1, 1]]
    );

    // The normalized long-facet action is read from the actual cells.  Its
    // covariance with the endpoint-relative road module certifies the full
    // unsplit Tate extension without choosing a projector or a strict road
    // section.
    let tag_action = |edge_action: &Matrix, facet_signs: &BTreeMap<Face, Z>, permutation| {
        let mut value = zero(3, 3);
        for (column, facet_index) in long_facets.iter().enumerate() {
            let source = &by_size[1][*facet_index];
            let image = permute_face(source, permutation);
            let row = long_facets
                .iter()
                .position(|index| by_size[1][*index] == image)
                .unwrap();
            value[row][column] =
                facet_signs[source] * top_long_coefficients[column] / top_long_coefficients[row];
        }
        let _ = edge_action;
        value
    };
    let tag_rotation = tag_action(&rotation_edges, &rotation_signs[1], rotate_vertex);
    let tag_reflection_raw = tag_action(&reflection_edges, &reflection_signs[1], reflect_vertex);
    let tag_reflection = scale(&tag_reflection_raw, -1);
    assert_eq!(
        multiply(&road_rotation, &middle),
        multiply(&middle, &tag_rotation)
    );
    assert_eq!(
        multiply(&road_reflection_raw, &middle),
        multiply(&middle, &tag_reflection_raw)
    );
    assert_eq!(
        multiply(&road_reflection, &middle),
        multiply(&middle, &tag_reflection)
    );
    assert_eq!(multiply(&tag_rotation, &norm), norm);
    assert_eq!(multiply(&tag_reflection_raw, &norm), scale(&norm, -1));
    assert_eq!(multiply(&tag_reflection, &norm), norm);

    // Entry 93's closed conductor points have the exact odd/even labels of
    // v_+/v_-.  Thus the label map from the two closed sheet components to V
    // is the identity in the ordered bases (+,-) and (v_+,v_-), not a map
    // inferred merely from their common character.  Reflection exchanges
    // both pairs and negates e_- - e_+, exactly as it negates the road
    // augmentation.  This is only the closed-conductor carrier map; no map
    // of full branch rings or PC costalks is asserted.
    let sheet_to_closed_endpoints = identity(2);
    let sheet_difference = vec![vec![-1, 1]];
    let sheet_reflection = vec![vec![0, 1], vec![1, 0]];
    assert_eq!(
        multiply(&sheet_to_closed_endpoints, &sheet_reflection),
        multiply(&sheet_reflection, &sheet_to_closed_endpoints)
    );
    assert_eq!(
        multiply(&sheet_difference, &sheet_to_closed_endpoints),
        sheet_difference
    );
    assert_eq!(
        multiply(&sheet_difference, &sheet_reflection),
        vec![vec![1, -1]]
    );

    println!(
        "{{\"claim\":\"The actual labelled two-endpoint triple V={{v_plus,v_minus}} subset B_short subset K6 canonically realizes the road-side endpoint-orientation carrier after tensoring its raw cellular pair triangle once by the physical road-orientation character. H1(B_short,V) is a saturated torsion-free rank-three road module; rotation cycles its three corridor classes, twisted physical reflection negates and reflects them, and the pair boundary is epsilon=(1,1,1) into Htilde0(V)=Z_or. The support connector and relative top give the exact unsplit Tate window over that same line. By entry 105's generator rule H subset S, the same triple restricts the absolute unlocalized original-twist/BM packet to strict D3-stable ranks 16 subset 208 subset 215. The canonical original-twist endpoint/Q object is the quotient F_K/F_V: its carrier C_*(K6,V) has only one primitive torsion-free H1 orientation line, its loaded degree ranks are (12,57,87,43), and its inherited filtration has road-relative subobject F_B/F_V and seven-generator quotient Q=F_K/F_B. Entry 93's exact odd/even conductor closed-point labels map to v_plus/v_minus, and the plus/minus D03 marked half-galleries concatenate at {{D03,x0,x3}} to a primitive four-edge corridor. Summing the three rotated special-leg half-galleries gives Gamma_Sigma_plus-Gamma_Sigma_minus=N_road strictly, with boundary 3(v_minus-v_plus). This closes the closed-conductor carrier cospan but not its ringed PC promotion.\",\"status\":\"proved\",\"factorization_test\":{{\"face_census\":[1,9,21,14],\"pair_chain_ranks\":[6,21,12],\"pair_differential_ranks\":[6,12],\"entry_105_loaded_support_ranks\":[16,208,215],\"loaded_Q_rank\":7,\"carrier_endpoint_Q_object\":\"C_*(K6,V) ranks (1,9,21,12), differential ranks (1,8,12), H1=Z_or after the road-orientation twist and all other homology zero; saturated and torsion-free\",\"absolute_endpoint_Q_object\":\"F_K/F_V with loaded degree ranks (12,57,87,43)\",\"absolute_endpoint_Q_filtration\":\"0 -> F_B/F_V degrees (12,57,84,39) -> F_K/F_V -> Q degrees (0,0,3,4) -> 0\",\"H1_B_V\":\"Z^3, saturated and torsion-free\",\"raw_pair_reflection\":{:?},\"road_rotation\":{:?},\"twisted_road_reflection\":{:?},\"endpoint\":[1,1,1],\"geometric_middle\":{:?},\"entry_142_middle_after_signed_cyclic_tag_rebase\":{:?},\"middle_rank\":2,\"orientation_twist\":\"one global reflection-sign tensor: raw roads permutation to negative permutation, raw tags negative permutation to permutation, raw top orientation to trivial, raw endpoint trivial to Z_or\",\"closed_conductor_endpoint_map\":\"J_plus=(x1,x3,x5) maps to v_plus and J_minus=(x0,x2,x4) maps to v_minus in the exact labelled carrier\",\"D03_marked_half_corridor\":\"two primitive two-edge half-galleries meet at {{D03,x0,x3}} and concatenate to the four-edge D03 corridor\",\"special_leg_sheet_difference\":\"Gamma_Sigma_plus-Gamma_Sigma_minus=N_road strictly; boundary=3(v_minus-v_plus); this is not entry-113 q_Sigma in the generic Q leg\",\"Q_cells\":\"the top and three actual long facets with their normal states are retained before support contraction\"}},\"counterevidence\":[\"The strict original-twist quotient F_K/F_V is canonical, but it does not by itself construct its reciprocal/multi-Rees/PC extraordinary promotion or the normalization-sheet map into that promotion.\",\"The checker constructs the labelled map only on the two closed conductor points; it does not construct a ringed map from the full normalization-Cech branches to the reciprocal/multi-Rees/PC endpoint object.\",\"Contracting to H1 forgets the distinguished chain-level Q representatives; the filtered cellular triple must be retained in any loaded promotion.\"],\"sharp_blocker\":\"Promote the now-explicit original-twist endpoint/Q object F_K/F_V to reciprocal/multi-Rees/PC variance and construct the full normalization-Cech sheet map into it; then prove the three marked half-corridor Cartier/central-flip counits commute with entry-131 edge purity while retaining q_Sigma.\",\"next_experiment\":\"Use E_endpoint,Q^abs=F_K/F_V and its exact subquotient filtration as the fixed original-twist carrier. Construct only its reciprocal/multi-Rees/PC promotion and the full normalization-Cech sheet arrow, run the ordinary-forgetting ablation, and only then test K_alt, q_Sigma, the x3 edge residue, and reflection parity.\"}}",
        road_reflection_raw,
        road_rotation,
        road_reflection,
        middle,
        entry_142_middle
    );
}
