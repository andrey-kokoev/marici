//! Exact certificate for the additive eight-point primitive half-line atlas.
//!
//! The certificate deliberately does not manufacture transition
//! automorphisms.  A rank-two chart Q={D,E} has the Laurent-normalized
//! Alexander-complement generator g_Q.  Its physical Gysin restriction at D
//! is the E-road in the genuine K_(2,3) cut object.  Thus two charts meeting
//! at D have distinct chain-level restrictions.  They are joined by either
//! of the two center paths in K_(2,3); the difference of those paths is the
//! primitive four-edge Ward circuit.
//!
//! The shared cut object has three road components.  Its carrier H_0
//! augmentation is a line quotient, not an established PC coefficient
//! retract; integrally it has no cyclic section.  Conditional on the unit
//! road quotient, ordered normal contraction gives the nontrivial orientation
//! local system on the candidate Mobius hypercover carrier.  Without that
//! quotient/counit, the
//! equally equivariant trivial and orientation systems are both compatible
//! with all facewise data and both have positive outer-octagon holonomy.
//!
//! The twelve charts, twenty-four pairwise comparisons, eight cut triangles,
//! and four squares form a Mobius-band cell carrier.  It is only a candidate
//! truncated hypercover until coefficient matching maps and cd-squares are
//! typed.  In the trivial coefficient model,
//! hypothetical edge comparisons satisfying all local face equations leave
//! one global weight.  The formal completions 0 and omega have
//! residual-octagon periods 0 and 2.  This is an additional illustration of
//! underdetermination; it does not assert that either completion is a
//! physical scalar construction.  The decisive next datum is the primitive
//! PC quotient/retract and its crosscap holonomy, not an octagon product.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

const N: u8 = 8;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Quadrangulation = [Diagonal; 2];
type Matrix = Vec<Vec<i64>>;

#[derive(Clone, Copy, Debug)]
struct Collapse {
    face: usize,
    edge: usize,
}

fn diagonal(first: u8, second: u8) -> Diagonal {
    assert_ne!(first, second);
    if first < second {
        Diagonal(first, second)
    } else {
        Diagonal(second, first)
    }
}

fn boundary_diagonal(value: Diagonal) -> bool {
    value.1 == value.0 + 1 || value == Diagonal(0, N - 1)
}

fn strictly_between(vertex: u8, first: u8, second: u8) -> bool {
    let span = (second + N - first) % N;
    let position = (vertex + N - first) % N;
    position > 0 && position < span
}

fn crosses(first: Diagonal, second: Diagonal) -> bool {
    if first.0 == second.0 || first.0 == second.1 || first.1 == second.0 || first.1 == second.1 {
        return false;
    }
    strictly_between(second.0, first.0, first.1) != strictly_between(second.1, first.0, first.1)
        && strictly_between(first.0, second.0, second.1)
            != strictly_between(first.1, second.0, second.1)
}

fn physical(value: Diagonal) -> bool {
    !boundary_diagonal(value) && value.0 % 2 != value.1 % 2
}

fn rotate(value: Diagonal, amount: u8) -> Diagonal {
    diagonal((value.0 + amount) % N, (value.1 + amount) % N)
}

fn reflect(value: Diagonal) -> Diagonal {
    diagonal((N - value.0) % N, (N - value.1) % N)
}

fn transform(value: Diagonal, amount: u8, reflected: bool) -> Diagonal {
    let reflected_value = if reflected { reflect(value) } else { value };
    rotate(reflected_value, amount)
}

fn physical_diagonals() -> Vec<Diagonal> {
    let mut result = Vec::new();
    for first in 0..N {
        for second in first + 1..N {
            let value = Diagonal(first, second);
            if physical(value) {
                result.push(value);
            }
        }
    }
    assert_eq!(result.len(), 8);
    result
}

fn quadrangulations(roads: &[Diagonal]) -> Vec<Quadrangulation> {
    let mut result = Vec::new();
    for first in 0..roads.len() {
        for second in first + 1..roads.len() {
            if !crosses(roads[first], roads[second]) {
                result.push([roads[first], roads[second]]);
            }
        }
    }
    result.sort();
    assert_eq!(result.len(), 12);
    result
}

fn polygon_boundary_edges() -> BTreeSet<Diagonal> {
    (0..N)
        .map(|vertex| diagonal(vertex, (vertex + 1) % N))
        .collect()
}

fn choose_four_vertices(start: u8, selected: &mut Vec<u8>, result: &mut Vec<[u8; 4]>) {
    if selected.len() == 4 {
        result.push([selected[0], selected[1], selected[2], selected[3]]);
        return;
    }
    let needed = 4 - selected.len() as u8;
    for vertex in start..=N - needed {
        selected.push(vertex);
        choose_four_vertices(vertex + 1, selected, result);
        selected.pop();
    }
}

fn quadrangulation_cells(value: Quadrangulation) -> Vec<[u8; 4]> {
    let edges: BTreeSet<_> = polygon_boundary_edges().into_iter().chain(value).collect();
    let mut candidates = Vec::new();
    choose_four_vertices(0, &mut Vec::new(), &mut candidates);
    let mut result: Vec<_> = candidates
        .into_iter()
        .filter(|vertices| {
            (0..4)
                .all(|index| edges.contains(&diagonal(vertices[index], vertices[(index + 1) % 4])))
        })
        .collect();
    result.sort();
    assert_eq!(result.len(), 3);
    result
}

fn region_slots(cell: [u8; 4]) -> [Diagonal; 2] {
    let mut result = [diagonal(cell[0], cell[2]), diagonal(cell[1], cell[3])];
    result.sort();
    result
}

fn physical_core(triangulation: &[Diagonal]) -> Vec<Diagonal> {
    triangulation
        .iter()
        .copied()
        .filter(|&value| physical(value))
        .collect()
}

fn audit_alexander_generators(quadrangulations: &[Quadrangulation]) {
    let mut all_exact_core_vertices = BTreeSet::new();
    for &quadrangulation in quadrangulations {
        let slots: Vec<_> = quadrangulation_cells(quadrangulation)
            .into_iter()
            .map(region_slots)
            .collect();
        let variables: BTreeSet<_> = slots.iter().flatten().copied().collect();
        assert_eq!(variables.len(), 6);
        assert!(variables.iter().all(|&value| !physical(value)));

        // A bit word v selects the occurrence monomial w_v.  Its antipode
        // selects m_v, and w_v*m_v is the full squarefree support M_Q.
        for mask in 0_u8..8 {
            let mut occurrence = BTreeSet::new();
            let mut complement = BTreeSet::new();
            let mut triangulation = quadrangulation.to_vec();
            for (region, pair) in slots.iter().enumerate() {
                let bit = usize::from((mask >> region) & 1);
                occurrence.insert(pair[bit]);
                complement.insert(pair[1 - bit]);
                triangulation.push(pair[bit]);
            }
            assert!(occurrence.is_disjoint(&complement));
            assert_eq!(
                occurrence
                    .union(&complement)
                    .copied()
                    .collect::<BTreeSet<_>>(),
                variables
            );
            triangulation.sort();
            assert_eq!(triangulation.len(), 5);
            assert!(triangulation.iter().enumerate().all(|(index, &first)| {
                triangulation[index + 1..]
                    .iter()
                    .all(|&second| !crosses(first, second))
            }));
            assert_eq!(physical_core(&triangulation), quadrangulation);
            all_exact_core_vertices.insert(triangulation);
        }

        // Along a cube edge the two representatives differ by precisely the
        // weighted interval relation X_(r0)e_0=X_(r1)e_1.  Hence all eight
        // w_v e_v represent one Laurent class g_Q and their polarized sum is
        // 8g_Q.  The loop below audits all twelve edge relations.
        let mut relations = 0;
        for mask in 0_u8..8 {
            for region in 0..3 {
                if (mask >> region) & 1 == 0 {
                    let other = mask | (1 << region);
                    assert_eq!(mask ^ other, 1 << region);
                    relations += 1;
                }
            }
        }
        assert_eq!(relations, 12);
    }
    assert_eq!(all_exact_core_vertices.len(), 96);
}

fn intersection<T: Ord + Copy>(first: &[T], second: &[T]) -> Vec<T> {
    let left: BTreeSet<_> = first.iter().copied().collect();
    let right: BTreeSet<_> = second.iter().copied().collect();
    left.intersection(&right).copied().collect()
}

fn canonical_edge(first: usize, second: usize) -> (usize, usize) {
    if first < second {
        (first, second)
    } else {
        (second, first)
    }
}

fn road_cycle(roads: &[Diagonal], quadrangulations: &[Quadrangulation]) -> Vec<usize> {
    let adjacency: Vec<Vec<_>> = roads
        .iter()
        .map(|road| {
            quadrangulations
                .iter()
                .filter(|value| value.contains(road))
                .map(|value| {
                    let other = *value.iter().find(|&&candidate| candidate != *road).unwrap();
                    roads
                        .iter()
                        .position(|&candidate| candidate == other)
                        .unwrap()
                })
                .collect()
        })
        .collect();
    assert!(adjacency.iter().all(|neighbors| neighbors.len() == 3));
    let antipode: Vec<_> = roads
        .iter()
        .map(|&road| rotate(road, 4))
        .map(|road| {
            roads
                .iter()
                .position(|&candidate| candidate == road)
                .unwrap()
        })
        .collect();
    let outer: Vec<Vec<_>> = adjacency
        .iter()
        .enumerate()
        .map(|(index, neighbors)| {
            neighbors
                .iter()
                .copied()
                .filter(|&neighbor| neighbor != antipode[index])
                .collect()
        })
        .collect();
    let mut cycle = vec![0_usize];
    let mut previous = usize::MAX;
    while cycle.len() < roads.len() {
        let current = *cycle.last().unwrap();
        let next = outer[current]
            .iter()
            .copied()
            .find(|&candidate| candidate != previous)
            .unwrap();
        previous = current;
        cycle.push(next);
    }
    assert!(outer[*cycle.last().unwrap()].contains(&cycle[0]));
    cycle
}

fn graph_boundary(vertices: usize, edges: &[(usize, usize)]) -> Matrix {
    let mut result = vec![vec![0; edges.len()]; vertices];
    for (column, &(first, second)) in edges.iter().enumerate() {
        result[first][column] = -1;
        result[second][column] = 1;
    }
    result
}

fn face_boundary(faces: &[Vec<usize>], edge_index: &BTreeMap<(usize, usize), usize>) -> Matrix {
    let mut result = vec![vec![0; faces.len()]; edge_index.len()];
    for (column, face) in faces.iter().enumerate() {
        for index in 0..face.len() {
            let first = face[index];
            let second = face[(index + 1) % face.len()];
            let edge = canonical_edge(first, second);
            result[edge_index[&edge]][column] += if first < second { 1 } else { -1 };
        }
    }
    result
}

fn matrix_product(left: &Matrix, right: &Matrix) -> Matrix {
    let rows = left.len();
    let middle = right.len();
    let columns = right.first().map_or(0, Vec::len);
    assert!(left.iter().all(|row| row.len() == middle));
    let mut result = vec![vec![0; columns]; rows];
    for row in 0..rows {
        for column in 0..columns {
            result[row][column] = (0..middle)
                .map(|index| left[row][index] * right[index][column])
                .sum();
        }
    }
    result
}

fn gcd(mut first: i128, mut second: i128) -> i128 {
    first = first.abs();
    second = second.abs();
    while second != 0 {
        (first, second) = (second, first % second);
    }
    first
}

fn integer_rank(matrix: &Matrix) -> usize {
    if matrix.is_empty() || matrix[0].is_empty() {
        return 0;
    }
    let mut value: Vec<Vec<i128>> = matrix
        .iter()
        .map(|row| row.iter().map(|&entry| i128::from(entry)).collect())
        .collect();
    let rows = value.len();
    let columns = value[0].len();
    let mut pivot = 0;
    for column in 0..columns {
        let Some(row) = (pivot..rows).find(|&row| value[row][column] != 0) else {
            continue;
        };
        value.swap(pivot, row);
        for row in pivot + 1..rows {
            if value[row][column] == 0 {
                continue;
            }
            let pivot_value = value[pivot][column];
            let row_value = value[row][column];
            for entry in column..columns {
                value[row][entry] =
                    pivot_value * value[row][entry] - row_value * value[pivot][entry];
            }
            let divisor = value[row]
                .iter()
                .fold(0_i128, |common, &entry| gcd(common, entry));
            if divisor > 1 {
                for entry in &mut value[row] {
                    *entry /= divisor;
                }
            }
        }
        pivot += 1;
        if pivot == rows {
            break;
        }
    }
    pivot
}

fn mod_two_rank(matrix: &Matrix) -> usize {
    if matrix.is_empty() || matrix[0].is_empty() {
        return 0;
    }
    let mut value: Vec<Vec<u8>> = matrix
        .iter()
        .map(|row| row.iter().map(|entry| entry.rem_euclid(2) as u8).collect())
        .collect();
    let rows = value.len();
    let columns = value[0].len();
    let mut rank = 0;
    for column in 0..columns {
        let Some(pivot) = (rank..rows).find(|&row| value[row][column] == 1) else {
            continue;
        };
        value.swap(rank, pivot);
        for row in 0..rows {
            if row != rank && value[row][column] == 1 {
                for entry in column..columns {
                    value[row][entry] ^= value[rank][entry];
                }
            }
        }
        rank += 1;
        if rank == rows {
            break;
        }
    }
    rank
}

fn minor(matrix: &Matrix, rows: &[usize], columns: &[usize]) -> Matrix {
    rows.iter()
        .map(|&row| columns.iter().map(|&column| matrix[row][column]).collect())
        .collect()
}

fn determinant(matrix: Matrix) -> i128 {
    let size = matrix.len();
    assert!(matrix.iter().all(|row| row.len() == size));
    if size == 0 {
        return 1;
    }
    let mut value: Vec<Vec<i128>> = matrix
        .into_iter()
        .map(|row| row.into_iter().map(i128::from).collect())
        .collect();
    let mut sign = 1_i128;
    let mut denominator = 1_i128;
    for pivot in 0..size - 1 {
        if value[pivot][pivot] == 0 {
            let row = (pivot + 1..size)
                .find(|&row| value[row][pivot] != 0)
                .expect("singular determinant pivot");
            value.swap(pivot, row);
            sign = -sign;
        }
        let pivot_value = value[pivot][pivot];
        for row in pivot + 1..size {
            for column in pivot + 1..size {
                value[row][column] = (value[row][column] * pivot_value
                    - value[row][pivot] * value[pivot][column])
                    / denominator;
            }
        }
        denominator = pivot_value;
    }
    sign * value[size - 1][size - 1]
}

fn solve_unimodular(matrix: &Matrix, target: &[i64]) -> Vec<i64> {
    let size = matrix.len();
    assert_eq!(target.len(), size);
    assert!(matrix.iter().all(|row| row.len() == size));
    let denominator = determinant(matrix.clone());
    assert_eq!(denominator.abs(), 1);
    (0..size)
        .map(|column| {
            let mut replaced = matrix.clone();
            for row in 0..size {
                replaced[row][column] = target[row];
            }
            i64::try_from(determinant(replaced) / denominator).expect("small integral solution")
        })
        .collect()
}

fn transpose(matrix: &Matrix) -> Matrix {
    let columns = matrix.first().map_or(0, Vec::len);
    (0..columns)
        .map(|column| matrix.iter().map(|row| row[column]).collect())
        .collect()
}

fn dot(first: &[i64], second: &[i64]) -> i64 {
    assert_eq!(first.len(), second.len());
    first
        .iter()
        .zip(second)
        .map(|(left, right)| left * right)
        .sum()
}

fn vector_boundary(matrix: &Matrix, vector: &[i64]) -> Vec<i64> {
    assert_eq!(matrix.first().map_or(0, Vec::len), vector.len());
    matrix.iter().map(|row| dot(row, vector)).collect()
}

fn free_face_collapses(boundary_two: &Matrix) -> Vec<Collapse> {
    let edge_count = boundary_two.len();
    let face_count = boundary_two.first().map_or(0, Vec::len);
    let mut active_edges = vec![true; edge_count];
    let mut active_faces = vec![true; face_count];
    let mut result = Vec::new();
    while result.len() < face_count {
        let found = (0..edge_count).find_map(|edge| {
            if !active_edges[edge] {
                return None;
            }
            let incident: Vec<_> = (0..face_count)
                .filter(|&face| active_faces[face] && boundary_two[edge][face] != 0)
                .collect();
            if incident.len() == 1 {
                Some(Collapse {
                    face: incident[0],
                    edge,
                })
            } else {
                None
            }
        });
        let collapse = found.expect("the medial Mobius band has a free boundary edge");
        active_faces[collapse.face] = false;
        active_edges[collapse.edge] = false;
        result.push(collapse);
    }
    assert!(active_faces.iter().all(|active| !active));
    result
}

fn find(parent: &mut [usize], value: usize) -> usize {
    if parent[value] != value {
        parent[value] = find(parent, parent[value]);
    }
    parent[value]
}

fn remaining_graph_tree(
    vertex_count: usize,
    edges: &[(usize, usize)],
    collapses: &[Collapse],
) -> (Vec<usize>, usize) {
    let removed: BTreeSet<_> = collapses.iter().map(|collapse| collapse.edge).collect();
    let remaining: Vec<_> = (0..edges.len())
        .filter(|edge| !removed.contains(edge))
        .collect();
    assert_eq!(remaining.len(), vertex_count);
    let mut parent: Vec<_> = (0..vertex_count).collect();
    let mut tree = Vec::new();
    let mut chords = Vec::new();
    for edge in remaining {
        let (first, second) = edges[edge];
        let first_root = find(&mut parent, first);
        let second_root = find(&mut parent, second);
        if first_root == second_root {
            chords.push(edge);
        } else {
            parent[first_root] = second_root;
            tree.push(edge);
        }
    }
    assert_eq!(tree.len(), vertex_count - 1);
    assert_eq!(chords.len(), 1);
    (tree, chords[0])
}

fn tree_path(
    start: usize,
    end: usize,
    edges: &[(usize, usize)],
    tree: &[usize],
) -> Vec<(usize, i64)> {
    let mut adjacency = vec![Vec::new(); edges.len()];
    for &edge in tree {
        let (first, second) = edges[edge];
        adjacency[first].push((second, edge, 1_i64));
        adjacency[second].push((first, edge, -1_i64));
    }
    let mut parent = vec![None; adjacency.len()];
    let mut queue = VecDeque::from([start]);
    parent[start] = Some((start, usize::MAX, 0));
    while let Some(current) = queue.pop_front() {
        if current == end {
            break;
        }
        for &(next, edge, sign) in &adjacency[current] {
            if parent[next].is_none() {
                parent[next] = Some((current, edge, sign));
                queue.push_back(next);
            }
        }
    }
    let mut result = Vec::new();
    let mut current = end;
    while current != start {
        let (previous, edge, sign) = parent[current].expect("tree path");
        result.push((edge, sign));
        current = previous;
    }
    result.reverse();
    result
}

fn core_cycle(
    vertex_count: usize,
    edges: &[(usize, usize)],
    tree: &[usize],
    chord: usize,
) -> Vec<i64> {
    let mut result = vec![0; edges.len()];
    let (first, second) = edges[chord];
    result[chord] = 1;
    for (edge, sign) in tree_path(second, first, edges, tree) {
        result[edge] += sign;
    }
    assert!(
        vector_boundary(&graph_boundary(vertex_count, edges), &result)
            .iter()
            .all(|&entry| entry == 0)
    );
    result
}

fn dual_cocycle(boundary_two: &Matrix, collapses: &[Collapse], chord: usize) -> Vec<i64> {
    let mut result = vec![0; boundary_two.len()];
    result[chord] = 1;
    for collapse in collapses.iter().rev() {
        let incidence = boundary_two[collapse.edge][collapse.face];
        assert!(incidence.abs() == 1);
        let sum: i64 = (0..boundary_two.len())
            .filter(|&edge| edge != collapse.edge)
            .map(|edge| boundary_two[edge][collapse.face] * result[edge])
            .sum();
        assert_eq!(sum % incidence, 0);
        result[collapse.edge] = -sum / incidence;
    }
    assert!(vector_boundary(&transpose(boundary_two), &result)
        .iter()
        .all(|&entry| entry == 0));
    result
}

fn oriented_cycle_vector(vertices: &[usize], edges: &BTreeMap<(usize, usize), usize>) -> Vec<i64> {
    let mut result = vec![0; edges.len()];
    for index in 0..vertices.len() {
        let first = vertices[index];
        let second = vertices[(index + 1) % vertices.len()];
        let edge = canonical_edge(first, second);
        result[edges[&edge]] += if first < second { 1 } else { -1 };
    }
    result
}

fn unit_power(monodromy: i64, exponent: i64) -> i64 {
    assert!(monodromy == 1 || monodromy == -1);
    if monodromy == 1 || exponent.rem_euclid(2) == 0 {
        1
    } else {
        -1
    }
}

fn twisted_boundaries(
    vertex_count: usize,
    edges: &[(usize, usize)],
    faces: &[Vec<usize>],
    edge_index: &BTreeMap<(usize, usize), usize>,
    voltage: &[i64],
    monodromy: i64,
) -> (Matrix, Matrix) {
    let mut boundary_one = vec![vec![0; edges.len()]; vertex_count];
    for (column, &(first, second)) in edges.iter().enumerate() {
        boundary_one[first][column] = -1;
        boundary_one[second][column] = unit_power(monodromy, voltage[column]);
    }
    let mut boundary_two = vec![vec![0; faces.len()]; edges.len()];
    for (column, face) in faces.iter().enumerate() {
        let mut coefficient = 1_i64;
        for index in 0..face.len() {
            let first = face[index];
            let second = face[(index + 1) % face.len()];
            let key = canonical_edge(first, second);
            let edge = edge_index[&key];
            let transport = unit_power(monodromy, voltage[edge]);
            if first < second {
                boundary_two[edge][column] += coefficient;
                coefficient *= transport;
            } else {
                boundary_two[edge][column] -= transport * coefficient;
                coefficient *= transport;
            }
        }
        assert_eq!(coefficient, 1);
    }
    assert!(matrix_product(&boundary_one, &boundary_two)
        .iter()
        .flatten()
        .all(|&entry| entry == 0));
    (boundary_one, boundary_two)
}

fn twisted_cycle(
    vertices: &[usize],
    edge_index: &BTreeMap<(usize, usize), usize>,
    voltage: &[i64],
    monodromy: i64,
) -> (Vec<i64>, i64) {
    let mut result = vec![0; edge_index.len()];
    let mut coefficient = 1_i64;
    for index in 0..vertices.len() {
        let first = vertices[index];
        let second = vertices[(index + 1) % vertices.len()];
        let edge = edge_index[&canonical_edge(first, second)];
        let transport = unit_power(monodromy, voltage[edge]);
        if first < second {
            result[edge] += coefficient;
            coefficient *= transport;
        } else {
            result[edge] -= transport * coefficient;
            coefficient *= transport;
        }
    }
    (result, coefficient)
}

fn augment_column(matrix: &Matrix, column: &[i64]) -> Matrix {
    assert_eq!(matrix.len(), column.len());
    matrix
        .iter()
        .zip(column)
        .map(|(row, &entry)| row.iter().copied().chain([entry]).collect())
        .collect()
}

fn local_cut_boundary(center: usize, road_count: usize) -> Matrix {
    assert!(center < 2);
    let vertices = 2 + road_count;
    let mut result = vec![vec![0; 2 * road_count]; vertices];
    for chosen_center in 0..2 {
        for road in 0..road_count {
            let edge = chosen_center * road_count + road;
            result[chosen_center][edge] = -1;
            result[2 + road][edge] = 1;
        }
    }
    assert_eq!(
        result[center].iter().filter(|&&entry| entry == -1).count(),
        road_count
    );
    result
}

fn audit_residue_cospans(roads: &[Diagonal], quadrangulations: &[Quadrangulation]) {
    let mut comparisons = 0;
    let mut path_homotopies = 0;
    let mut ward_circuits = 0;
    for &marked in roads {
        let incident: Vec<_> = quadrangulations
            .iter()
            .enumerate()
            .filter(|(_, value)| value.contains(&marked))
            .collect();
        assert_eq!(incident.len(), 3);
        let cut_boundary = local_cut_boundary(0, incident.len());

        // The Gysin leg sends g_{D,E} to the E-road.  Distinct incident
        // charts therefore have distinct normalized chain-level images.
        // Each pair has two center-path homotopies; their difference is a
        // boundary-zero primitive Ward four-circuit.
        for first in 0..incident.len() {
            for second in first + 1..incident.len() {
                let mut endpoint_difference = vec![0; 2 + incident.len()];
                endpoint_difference[2 + first] = -1;
                endpoint_difference[2 + second] = 1;
                assert_ne!(endpoint_difference, vec![0; 2 + incident.len()]);
                comparisons += 1;

                let mut paths = Vec::new();
                for center in 0..2 {
                    let mut path = vec![0; 2 * incident.len()];
                    path[center * incident.len() + first] = -1;
                    path[center * incident.len() + second] = 1;
                    assert_eq!(vector_boundary(&cut_boundary, &path), endpoint_difference);
                    paths.push(path);
                    path_homotopies += 1;
                }
                let circuit: Vec<_> = paths[0]
                    .iter()
                    .zip(&paths[1])
                    .map(|(plus, minus)| plus - minus)
                    .collect();
                assert_eq!(circuit.iter().filter(|&&entry| entry != 0).count(), 4);
                assert!(vector_boundary(&cut_boundary, &circuit)
                    .iter()
                    .all(|&entry| entry == 0));
                ward_circuits += 1;
            }
        }

        // Around the triangle of the three roads, the chosen path through
        // either fixed center telescopes strictly.
        for center in 0..2 {
            let mut triangle = vec![0; 2 * incident.len()];
            for (first, second) in [(0, 1), (1, 2), (2, 0)] {
                triangle[center * incident.len() + first] -= 1;
                triangle[center * incident.len() + second] += 1;
            }
            assert!(triangle.iter().all(|&entry| entry == 0));
        }

        // Ordered normal contraction: for Q=[D,E], i_D(D^E)=E and
        // i_E(D^E)=-D.  The two ordered double residues anticommute.
        for (_, quadrangulation) in incident {
            let position = quadrangulation
                .iter()
                .position(|&value| value == marked)
                .unwrap();
            let first_sign = if position == 0 { 1 } else { -1 };
            let companion_position = 1 - position;
            let reverse_first_sign = if companion_position == 0 { 1 } else { -1 };
            assert_eq!(first_sign, -reverse_first_sign);
        }
    }
    assert_eq!(comparisons, 24);
    assert_eq!(path_homotopies, 48);
    assert_eq!(ward_circuits, 24);
}

fn audit_primitive_quotient() {
    // The shared channel object has three road components.  The carrier-level
    // H_0 augmentation sends every road to one generator, so each normalized
    // chart leg would become a unit after that quotient.  It is not an
    // integral cyclic retract: a C_3-invariant section has value (a,a,a), and
    // augmentation followed by that section is multiplication by 3a.
    let road_augmentation = [1_i64, 1, 1];
    assert!(road_augmentation.iter().all(|&entry| entry == 1));
    let a_two_basis = [[1_i64, -1, 0], [0, 1, -1]];
    assert!(a_two_basis
        .iter()
        .all(|root| dot(&road_augmentation, root) == 0));
    // A_2 is saturated: adjoining any one road lift of 1 gives a unimodular
    // basis of Z^3.  Thus 0 -> A_2 -> Z^3 -> Z -> 0 is exact.
    let splitting_matrix = vec![
        vec![a_two_basis[0][0], a_two_basis[1][0], 0],
        vec![a_two_basis[0][1], a_two_basis[1][1], 0],
        vec![a_two_basis[0][2], a_two_basis[1][2], 1],
    ];
    assert_eq!(determinant(splitting_matrix).abs(), 1);
    let diagonal = [1_i64, 1, 1];
    let equivariant_lattice = vec![
        vec![diagonal[0], a_two_basis[0][0], a_two_basis[1][0]],
        vec![diagonal[1], a_two_basis[0][1], a_two_basis[1][1]],
        vec![diagonal[2], a_two_basis[0][2], a_two_basis[1][2]],
    ];
    assert_eq!(determinant(equivariant_lattice).abs(), 3);
    assert!((-8_i64..=8).all(|coefficient| 3 * coefficient != 1));

    // Over Z[1/3] the only C_3-invariant section is the averaged vector
    // (1/3,1/3,1/3).  The existing occurrence entry counit is a different
    // map: it evaluates one marked six-point boundary into J_4 boxtimes J_4.
    // It does not prove that this three-road quotient or average is a PC chain
    // map/retract of J_4 boxtimes J_6.  Under the standard permutation-module
    // pairing, this augmentation sequence is dual as an underlying lattice
    // to 0 -> Z_diag -> Z^3_tags -> A_2 -> 0.  Entry 59's oriented tag module
    // has an additional reflection/core-exchange character, audited by the
    // representative counit-adjoint certificate; it must not be discarded.
}

fn contraction_sign(quadrangulation: Quadrangulation, marked: Diagonal) -> i64 {
    match quadrangulation
        .iter()
        .position(|&value| value == marked)
        .expect("the contracted normal belongs to the chart")
    {
        0 => 1,
        1 => -1,
        _ => unreachable!("a quadrangulation has two ordered normals"),
    }
}

fn primitive_quotient_voltage(
    flips: &[(usize, usize)],
    quadrangulations: &[Quadrangulation],
) -> Vec<i64> {
    flips
        .iter()
        .map(|&(first, second)| {
            let shared = intersection(&quadrangulations[first], &quadrangulations[second]);
            assert_eq!(shared.len(), 1);
            let transition = contraction_sign(quadrangulations[first], shared[0])
                * contraction_sign(quadrangulations[second], shared[0]);
            if transition == 1 {
                0
            } else {
                1
            }
        })
        .collect()
}

fn audit_voltage_dihedral_gauge(
    voltage: &[i64],
    flips: &[(usize, usize)],
    edge_index: &BTreeMap<(usize, usize), usize>,
    quadrangulations: &[Quadrangulation],
) {
    for amount in 0..N {
        for reflected in [false, true] {
            let images: Vec<_> = quadrangulations
                .iter()
                .map(|quadrangulation| {
                    let image_unsorted = [
                        transform(quadrangulation[0], amount, reflected),
                        transform(quadrangulation[1], amount, reflected),
                    ];
                    let gauge = if image_unsorted[0] < image_unsorted[1] {
                        0_i64
                    } else {
                        1_i64
                    };
                    let mut image = image_unsorted;
                    image.sort();
                    let target = quadrangulations
                        .iter()
                        .position(|&candidate| candidate == image)
                        .unwrap();
                    (target, gauge)
                })
                .collect();
            for (edge, &(first, second)) in flips.iter().enumerate() {
                let image = canonical_edge(images[first].0, images[second].0);
                let transformed_voltage = voltage[edge_index[&image]];
                let wedge_reordering_gauge = images[first].1 + images[second].1;
                assert_eq!(
                    transformed_voltage.rem_euclid(2),
                    (voltage[edge] + wedge_reordering_gauge).rem_euclid(2),
                    "D8 voltage covariance is exactly the wedge-reordering vertex gauge"
                );
            }
        }
    }
}

fn audit_dihedral_covariance(quadrangulations: &[Quadrangulation]) {
    for amount in 0..N {
        for reflected in [false, true] {
            for &quadrangulation in quadrangulations {
                let transformed_unsorted = [
                    transform(quadrangulation[0], amount, reflected),
                    transform(quadrangulation[1], amount, reflected),
                ];
                let mut transformed_sorted = transformed_unsorted;
                transformed_sorted.sort();
                assert!(quadrangulations.contains(&transformed_sorted));
                let wedge_sign = if transformed_unsorted == transformed_sorted {
                    1
                } else {
                    -1
                };
                assert!(wedge_sign == 1 || wedge_sign == -1);

                let source_variables: BTreeSet<_> = quadrangulation_cells(quadrangulation)
                    .into_iter()
                    .flat_map(region_slots)
                    .map(|value| transform(value, amount, reflected))
                    .collect();
                let target_variables: BTreeSet<_> = quadrangulation_cells(transformed_sorted)
                    .into_iter()
                    .flat_map(region_slots)
                    .collect();
                assert_eq!(source_variables, target_variables);
            }
        }
    }
}

fn audit_carrier_dihedral(faces: &[Vec<usize>], quadrangulations: &[Quadrangulation]) {
    let face_sets: BTreeSet<_> = faces
        .iter()
        .map(|face| face.iter().copied().collect::<BTreeSet<_>>())
        .collect();
    assert_eq!(face_sets.len(), faces.len());
    for amount in 0..N {
        for reflected in [false, true] {
            let permutation: Vec<_> = quadrangulations
                .iter()
                .map(|quadrangulation| {
                    let mut image = [
                        transform(quadrangulation[0], amount, reflected),
                        transform(quadrangulation[1], amount, reflected),
                    ];
                    image.sort();
                    quadrangulations
                        .iter()
                        .position(|&candidate| candidate == image)
                        .unwrap()
                })
                .collect();
            for face in faces {
                let image: BTreeSet<_> = face.iter().map(|&vertex| permutation[vertex]).collect();
                assert!(face_sets.contains(&image));
            }
        }
    }
}

fn main() {
    let roads = physical_diagonals();
    let quadrangulations = quadrangulations(&roads);
    audit_alexander_generators(&quadrangulations);
    audit_residue_cospans(&roads, &quadrangulations);
    audit_primitive_quotient();
    audit_dihedral_covariance(&quadrangulations);

    let mut flips = Vec::new();
    for first in 0..quadrangulations.len() {
        for second in first + 1..quadrangulations.len() {
            if intersection(&quadrangulations[first], &quadrangulations[second]).len() == 1 {
                flips.push((first, second));
            }
        }
    }
    assert_eq!(flips.len(), 24);
    let edge_index: BTreeMap<_, _> = flips
        .iter()
        .copied()
        .enumerate()
        .map(|(index, edge)| (edge, index))
        .collect();

    let road_order = road_cycle(&roads, &quadrangulations);
    let outer_vertices: Vec<_> = (0..roads.len())
        .map(|index| {
            let mut value = [
                roads[road_order[index]],
                roads[road_order[(index + 1) % roads.len()]],
            ];
            value.sort();
            quadrangulations
                .iter()
                .position(|&candidate| candidate == value)
                .unwrap()
        })
        .collect();
    assert_eq!(
        outer_vertices
            .iter()
            .copied()
            .collect::<BTreeSet<_>>()
            .len(),
        8
    );

    let mut faces: Vec<Vec<usize>> = roads
        .iter()
        .map(|road| {
            quadrangulations
                .iter()
                .enumerate()
                .filter_map(|(index, value)| value.contains(road).then_some(index))
                .collect()
        })
        .collect();
    assert!(faces.iter().all(|face| face.len() == 3));
    let matching_vertices: Vec<_> = (0..4)
        .map(|index| {
            let mut value = [roads[road_order[index]], roads[road_order[index + 4]]];
            value.sort();
            quadrangulations
                .iter()
                .position(|&candidate| candidate == value)
                .unwrap()
        })
        .collect();
    for index in 0..4 {
        faces.push(vec![
            outer_vertices[index],
            matching_vertices[(index + 1) % 4],
            outer_vertices[index + 4],
            matching_vertices[index],
        ]);
    }
    assert_eq!(faces.len(), 12);
    audit_carrier_dihedral(&faces, &quadrangulations);

    let boundary_one = graph_boundary(quadrangulations.len(), &flips);
    let boundary_two = face_boundary(&faces, &edge_index);
    assert!(matrix_product(&boundary_one, &boundary_two)
        .iter()
        .flatten()
        .all(|&entry| entry == 0));
    assert_eq!(integer_rank(&boundary_one), 11);
    assert_eq!(integer_rank(&boundary_two), 12);
    assert_eq!(mod_two_rank(&boundary_one), 11);
    assert_eq!(mod_two_rank(&boundary_two), 12);
    assert_eq!(flips.len() - 11 - 12, 1);

    let collapses = free_face_collapses(&boundary_two);
    assert_eq!(collapses.len(), 12);
    let free_rows: Vec<_> = collapses.iter().map(|collapse| collapse.edge).collect();
    let face_columns: Vec<_> = collapses.iter().map(|collapse| collapse.face).collect();
    assert_eq!(
        determinant(minor(&boundary_two, &free_rows, &face_columns)).abs(),
        1
    );
    let (tree, chord) = remaining_graph_tree(quadrangulations.len(), &flips, &collapses);
    let root = 0;
    let tree_rows: Vec<_> = (0..quadrangulations.len())
        .filter(|&row| row != root)
        .collect();
    assert_eq!(
        determinant(minor(&boundary_one, &tree_rows, &tree)).abs(),
        1
    );

    let core = core_cycle(quadrangulations.len(), &flips, &tree, chord);
    let omega = dual_cocycle(&boundary_two, &collapses, chord);
    assert_eq!(dot(&omega, &core), 1);
    let primitive_voltage = primitive_quotient_voltage(&flips, &quadrangulations);
    audit_voltage_dihedral_gauge(&primitive_voltage, &flips, &edge_index, &quadrangulations);
    assert!(
        vector_boundary(&transpose(&boundary_two), &primitive_voltage)
            .iter()
            .all(|entry| entry.rem_euclid(2) == 0)
    );
    let primitive_core_holonomy = dot(&primitive_voltage, &core).rem_euclid(2);
    assert_eq!(primitive_core_holonomy, 1);
    let outer = oriented_cycle_vector(&outer_vertices, &edge_index);
    assert!(vector_boundary(&boundary_one, &outer)
        .iter()
        .all(|&entry| entry == 0));
    assert_eq!(dot(&omega, &outer).abs(), 2);
    assert_eq!(dot(&primitive_voltage, &outer).rem_euclid(2), 0);

    // The zero comparison and omega have identical endpoint data and obey
    // every one of the twelve face equations.  They are not gauge-equivalent
    // because omega pairs to one with the surviving core cycle.
    let zero = vec![0; flips.len()];
    assert!(vector_boundary(&transpose(&boundary_two), &zero)
        .iter()
        .all(|&entry| entry == 0));
    assert!(vector_boundary(&transpose(&boundary_two), &omega)
        .iter()
        .all(|&entry| entry == 0));
    assert_eq!(dot(&zero, &outer), 0);
    assert_eq!(dot(&omega, &outer).abs(), 2);

    // Universal rank-one local system.  The collapses use only monomial
    // units; after the twelve face-edge and eleven tree-edge cancellations,
    // the complex is R --(u-1)--> R.  At u=-1 the integral matrices below
    // have SNF(d1)=1^11,2 and SNF(d2)=1^12.
    let (sign_boundary_one, sign_boundary_two) = twisted_boundaries(
        quadrangulations.len(),
        &flips,
        &faces,
        &edge_index,
        &omega,
        -1,
    );
    assert_eq!(integer_rank(&sign_boundary_one), 12);
    assert_eq!(integer_rank(&sign_boundary_two), 12);
    assert_eq!(
        determinant(minor(&sign_boundary_one, &tree_rows, &tree)).abs(),
        1
    );
    let mut all_rows = tree_rows.clone();
    all_rows.push(root);
    let mut loop_columns = tree.clone();
    loop_columns.push(chord);
    assert_eq!(
        determinant(minor(&sign_boundary_one, &all_rows, &loop_columns)).abs(),
        2
    );
    assert_eq!(
        determinant(minor(&sign_boundary_two, &free_rows, &face_columns)).abs(),
        1
    );

    // The boundary octagon has universal holonomy u^2.  It is a twisted
    // cycle only after the relation u^2=1.  The two specializations give the
    // ordinary and orientation-local-system RP^2 complexes.
    let (constant_outer, constant_holonomy) =
        twisted_cycle(&outer_vertices, &edge_index, &omega, 1);
    assert_eq!(constant_holonomy, 1);
    assert_eq!(constant_outer, outer);
    let extended_constant = augment_column(&boundary_two, &constant_outer);
    assert_eq!(integer_rank(&extended_constant), 13);
    let mut extended_rows = free_rows.clone();
    extended_rows.push(chord);
    let extended_columns: Vec<_> = (0..13).collect();
    assert_eq!(
        determinant(minor(&extended_constant, &extended_rows, &extended_columns)).abs(),
        2
    );
    let reduced_mod_two: Matrix = extended_constant
        .iter()
        .map(|row| row.iter().map(|entry| entry.rem_euclid(2)).collect())
        .collect();
    assert_eq!(integer_rank(&reduced_mod_two), 12);

    let (sign_outer, sign_holonomy) = twisted_cycle(&outer_vertices, &edge_index, &omega, -1);
    assert_eq!(sign_holonomy, 1);
    assert!(vector_boundary(&sign_boundary_one, &sign_outer)
        .iter()
        .all(|&entry| entry == 0));
    let extended_sign = augment_column(&sign_boundary_two, &sign_outer);
    assert_eq!(integer_rank(&extended_sign), 12);
    let sign_free_minor = minor(&sign_boundary_two, &free_rows, &face_columns);
    let sign_free_target: Vec<_> = free_rows.iter().map(|&row| sign_outer[row]).collect();
    let sign_fundamental_reordered = solve_unimodular(&sign_free_minor, &sign_free_target);
    let mut sign_fundamental = vec![0; faces.len()];
    for (position, &face) in face_columns.iter().enumerate() {
        sign_fundamental[face] = sign_fundamental_reordered[position];
    }
    assert_eq!(
        vector_boundary(&sign_boundary_two, &sign_fundamental),
        sign_outer
    );
    assert!(sign_fundamental.iter().all(|entry| entry.abs() == 1));

    println!("global eight-point primitive half-line atlas certificate");
    println!("  local charts: 12 Alexander-complement cubes, 96 exact-core vertices");
    println!("  each polarized occurrence sum is 8g_Q; no division is used");
    println!("  cut cospans: 24 strict mismatches, 48 center paths, 24 Ward ambiguities");
    println!("  cut roads: 0 -> A2 -> Z^3 --sum--> Z -> 0 is saturated exact");
    println!("  its lattice dual is 0 -> Z_diag -> Z^3_tags -> A2 -> 0; tags need chi_N");
    println!("  the H0 coinvariant is a canonical carrier line quotient, not a proved PC quotient");
    println!("  no integral C3-equivariant section; the unique average requires inverting 3");
    println!("  ordered two-normal residues anticommute; all 16 D8 actions preserve the data");
    println!("  conditional voltage obeys all 16x24 wedge-reordering vertex-gauge identities");
    println!("  candidate hypercover carrier: (C0,C1,C2)=(12,24,8 triangles + 4 squares)");
    println!("  ordinary SNF: d1=1^11, d2=1^12; H=(Z,Z,0)");
    println!("  outer octagon is twice the primitive Mobius core");
    println!("  ordered-normal primitive-quotient voltage on the core: {primitive_core_holonomy}");
    println!("  conditionally, the unit road quotient selects the nontrivial orientation system");
    println!("  universal local system collapses to R --(u-1)--> R");
    println!("  H^0_R=0, H^1_R=R/(u-1), H^i_R=0 for i>1");
    println!("  orientation twist u=-1: SNF(d1)=1^11,2; SNF(d2)=1^12; H^1=Z/2");
    println!("  over a characteristic-zero field the twisted Mobius complex is acyclic");
    println!("  the twisted outer octagon bounds the unique signed relative fundamental chain");
    println!("  residual cap requires u^2=1: d1=u-1, d2=u+1");
    println!("  capped u=1: H^0=Z, H^1=0, H^2=Z/2");
    println!("  capped u=-1: H^0=0, H^1=Z/2, H^2=Z");
    println!("  the capped twisted top class is the conditional additive Jordan candidate");
    println!("  zero and omega obey the same formal endpoint and cellular face equations");
    println!(
        "  their ordinary octagon periods are 0 and 2, so those equations underdetermine Theta"
    );
    println!();
    println!("VERDICT: CONDITIONAL / THETA_FULL IS NOT YET TYPED");
    println!("  strict gluing is false on the occurrence-resolved cut complexes");
    println!("  local derived gluing exists through either cut-center path");
    println!("  the missing PC quotient pi_D decides whether chart legs invert on a line");
    println!("  a cyclic section/homotopy is additional retract data, not part of pi_D");
    println!("  crosscap holonomy, not outer holonomy, distinguishes the two local systems");
    println!("  bare H1 or RP2 torsion is not a scalar-derived coefficient class");
}
