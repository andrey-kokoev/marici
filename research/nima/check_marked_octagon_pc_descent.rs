//! Exact n=8 audit of the marked octagon and its PC typing.
//!
//! Entry 24 constructs a deck-odd marked scalar one-chain from length-two
//! associahedral paths.  The coefficient of a path marked by d is -X_d.
//! The first question here is whether d survives at the middle vertex.  If
//! it does, the entire path lies in the fixed-mark associahedral facet
//! K_alpha^(d), so entry 38's A-linear undecorated facewise PC chain map can
//! be applied with -X_d as a constant coefficient.  No dependent
//! occurrence specialization is needed on that path.
//!
//! The second question is whether the residual octagon is a product of
//! transition automorphisms.  It is not.  Consecutive octagon vertices are
//! distinct rank-two cores sharing one physical diagonal; their other two
//! diagonals cross.  Hence their exact-core cubes are disjoint scalar faces.
//! The established horizontal datum is a pair of residue/Gysin maps to the
//! shared rank-one core, a noninvertible span, not an isomorphism T_i.  The
//! correctly typed obstruction is therefore the additive marked boundary
//! class.  The entry-24 transport has no support on the outer-octagon edges,
//! so its ordinary and sign-twisted circulations vanish identically.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

const N: u8 = 8;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Triangulation = Vec<Diagonal>;
type Quadrangulation = [Diagonal; 2];
type Matrix = Vec<Vec<i64>>;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Matching {
    source: usize,
    mark: Diagonal,
    target: usize,
}

fn diagonal(first: u8, second: u8) -> Diagonal {
    if first < second {
        Diagonal(first, second)
    } else {
        Diagonal(second, first)
    }
}

fn is_boundary(value: Diagonal) -> bool {
    value.1 - value.0 == 1 || value == Diagonal(0, N - 1)
}

fn is_physical(value: Diagonal) -> bool {
    value.0 % 2 != value.1 % 2
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

fn rotate(value: Diagonal, amount: u8) -> Diagonal {
    diagonal((value.0 + amount) % N, (value.1 + amount) % N)
}

fn all_diagonals() -> Vec<Diagonal> {
    let mut result = Vec::new();
    for first in 0..N {
        for second in first + 1..N {
            let value = Diagonal(first, second);
            if !is_boundary(value) {
                result.push(value);
            }
        }
    }
    result
}

fn choose_five(
    diagonals: &[Diagonal],
    start: usize,
    selected: &mut Vec<Diagonal>,
    result: &mut Vec<Triangulation>,
) {
    if selected.len() == 5 {
        if selected.iter().enumerate().all(|(index, &first)| {
            selected[index + 1..]
                .iter()
                .all(|&second| !crosses(first, second))
        }) {
            result.push(selected.clone());
        }
        return;
    }
    let needed = 5 - selected.len();
    for index in start..=diagonals.len() - needed {
        let candidate = diagonals[index];
        if selected.iter().all(|&value| !crosses(value, candidate)) {
            selected.push(candidate);
            choose_five(diagonals, index + 1, selected, result);
            selected.pop();
        }
    }
}

fn triangulations() -> Vec<Triangulation> {
    let mut result = Vec::new();
    choose_five(&all_diagonals(), 0, &mut Vec::new(), &mut result);
    result.sort();
    result.dedup();
    assert_eq!(result.len(), 132);
    result
}

fn intersection_size<T: Ord>(first: &[T], second: &[T]) -> usize {
    let mut left = 0;
    let mut right = 0;
    let mut count = 0;
    while left < first.len() && right < second.len() {
        match first[left].cmp(&second[right]) {
            std::cmp::Ordering::Less => left += 1,
            std::cmp::Ordering::Greater => right += 1,
            std::cmp::Ordering::Equal => {
                count += 1;
                left += 1;
                right += 1;
            }
        }
    }
    count
}

fn triangulation_adjacency(triangulations: &[Triangulation]) -> Vec<Vec<usize>> {
    let mut result = vec![Vec::new(); triangulations.len()];
    for first in 0..triangulations.len() {
        for second in first + 1..triangulations.len() {
            if intersection_size(&triangulations[first], &triangulations[second]) == 4 {
                result[first].push(second);
                result[second].push(first);
            }
        }
    }
    assert!(result.iter().all(|neighbors| neighbors.len() == 5));
    result
}

fn physical_core(triangulation: &Triangulation) -> Vec<Diagonal> {
    triangulation
        .iter()
        .copied()
        .filter(|&value| is_physical(value))
        .collect()
}

fn physical_diagonals() -> Vec<Diagonal> {
    let mut result: Vec<_> = (0..N)
        .map(|vertex| diagonal(vertex, (vertex + 3) % N))
        .collect();
    result.sort();
    result.dedup();
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

fn quadrangulation_adjacency(quadrangulations: &[Quadrangulation]) -> Vec<Vec<usize>> {
    (0..quadrangulations.len())
        .map(|index| {
            (0..quadrangulations.len())
                .filter(|&other| {
                    other != index
                        && intersection_size(&quadrangulations[index], &quadrangulations[other])
                            == 1
                })
                .collect()
        })
        .collect()
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
    let result: Vec<_> = candidates
        .into_iter()
        .filter(|vertices| {
            (0..4)
                .all(|index| edges.contains(&diagonal(vertices[index], vertices[(index + 1) % 4])))
        })
        .collect();
    assert_eq!(result.len(), 3);
    result
}

fn cell_side(value: Diagonal, cell: [u8; 4]) -> u8 {
    let increasing: BTreeSet<_> = (value.0 + 1..value.1).collect();
    let other: BTreeSet<_> = cell
        .into_iter()
        .filter(|&vertex| vertex != value.0 && vertex != value.1)
        .collect();
    if other.is_subset(&increasing) {
        0
    } else {
        assert!(other.is_disjoint(&increasing));
        1
    }
}

fn coorientation(value: Diagonal, plus: bool) -> u8 {
    let plus_side = if value.0 % 2 == 0 { 1 } else { 0 };
    if plus {
        plus_side
    } else {
        1 - plus_side
    }
}

fn contact_slots(value: Quadrangulation, plus: bool) -> Vec<Diagonal> {
    let cells = quadrangulation_cells(value);
    let mut outdegree = vec![0_usize; cells.len()];
    for road in value {
        let adjacent: Vec<_> = cells
            .iter()
            .enumerate()
            .filter_map(|(index, cell)| cell.contains(&road.0).then_some((index, cell)))
            .filter(|(_, cell)| cell.contains(&road.1))
            .collect();
        assert_eq!(adjacent.len(), 2);
        let target = adjacent
            .iter()
            .find(|(_, cell)| cell_side(road, **cell) == coorientation(road, plus))
            .unwrap()
            .0;
        let source = adjacent
            .iter()
            .find(|(index, _)| *index != target)
            .unwrap()
            .0;
        outdegree[source] += 1;
    }
    let sinks: Vec<_> = outdegree
        .iter()
        .enumerate()
        .filter_map(|(index, &degree)| (degree == 0).then_some(cells[index]))
        .collect();
    if sinks.len() == 2 {
        return Vec::new();
    }
    assert_eq!(sinks.len(), 1);
    let cell = sinks[0];
    let mut result = vec![diagonal(cell[0], cell[2]), diagonal(cell[1], cell[3])];
    result.sort();
    result
}

fn bfs_distances(start: usize, adjacency: &[Vec<usize>]) -> Vec<usize> {
    let mut distances = vec![usize::MAX; adjacency.len()];
    distances[start] = 0;
    let mut queue = VecDeque::from([start]);
    while let Some(current) = queue.pop_front() {
        for &neighbor in &adjacency[current] {
            if distances[neighbor] == usize::MAX {
                distances[neighbor] = distances[current] + 1;
                queue.push_back(neighbor);
            }
        }
    }
    distances
}

fn permutations(values: &[usize]) -> Vec<Vec<usize>> {
    fn recurse(values: &mut Vec<usize>, start: usize, result: &mut Vec<Vec<usize>>) {
        if start == values.len() {
            result.push(values.clone());
            return;
        }
        for index in start..values.len() {
            values.swap(start, index);
            recurse(values, start + 1, result);
            values.swap(start, index);
        }
    }
    let mut work = values.to_vec();
    let mut result = Vec::new();
    recurse(&mut work, 0, &mut result);
    result
}

fn derive_matching(
    plus: bool,
    triangulations: &[Triangulation],
    quadrangulations: &[Quadrangulation],
    zero_core: &[usize],
    fibers: &[Vec<usize>],
    distances: &BTreeMap<usize, Vec<usize>>,
) -> Vec<Matching> {
    let mut sources_by_mark: BTreeMap<Diagonal, Vec<usize>> = BTreeMap::new();
    for &source in zero_core {
        for &mark in &triangulations[source] {
            sources_by_mark.entry(mark).or_default().push(source);
        }
    }
    let mut targets_by_mark: BTreeMap<Diagonal, Vec<usize>> = BTreeMap::new();
    for (target, &value) in quadrangulations.iter().enumerate() {
        for mark in contact_slots(value, plus) {
            targets_by_mark.entry(mark).or_default().push(target);
        }
    }
    assert_eq!(
        sources_by_mark.keys().collect::<Vec<_>>(),
        targets_by_mark.keys().collect::<Vec<_>>()
    );

    let mut result = Vec::new();
    for (&mark, sources) in &sources_by_mark {
        let targets = &targets_by_mark[&mark];
        assert_eq!(sources.len(), targets.len());
        let marked_distance = |source: usize, target: usize| {
            fibers[target]
                .iter()
                .copied()
                .filter(|&endpoint| triangulations[endpoint].contains(&mark))
                .map(|endpoint| distances[&source][endpoint])
                .min()
                .unwrap()
        };
        let scored: Vec<_> = permutations(targets)
            .into_iter()
            .map(|order| {
                let score = sources
                    .iter()
                    .copied()
                    .zip(order.iter().copied())
                    .map(|(source, target)| marked_distance(source, target))
                    .sum::<usize>();
                (score, order)
            })
            .collect();
        let minimum = scored.iter().map(|(score, _)| *score).min().unwrap();
        let minimizers: Vec<_> = scored
            .into_iter()
            .filter(|(score, _)| *score == minimum)
            .collect();
        assert_eq!(minimizers.len(), 1);
        for (&source, &target) in sources.iter().zip(&minimizers[0].1) {
            assert_eq!(marked_distance(source, target), 2);
            result.push(Matching {
                source,
                mark,
                target,
            });
        }
    }
    result.sort();
    assert_eq!(result.len(), 20);
    result
}

fn marked_scalar_paths(
    matching: Matching,
    triangulations: &[Triangulation],
    adjacency: &[Vec<usize>],
    fibers: &[Vec<usize>],
) -> Vec<(usize, usize, usize)> {
    let mut result = Vec::new();
    for &middle in &adjacency[matching.source] {
        for &endpoint in &adjacency[middle] {
            if fibers[matching.target].contains(&endpoint)
                && triangulations[endpoint].contains(&matching.mark)
            {
                result.push((matching.source, middle, endpoint));
            }
        }
    }
    result.sort();
    assert!((1..=2).contains(&result.len()));
    assert_eq!(
        result
            .iter()
            .map(|path| path.2)
            .collect::<BTreeSet<_>>()
            .len(),
        1
    );
    result
}

fn road_cycle(roads: &[Diagonal], quadrangulations: &[Quadrangulation]) -> Vec<usize> {
    let adjacency: Vec<Vec<_>> = (0..roads.len())
        .map(|road| {
            quadrangulations
                .iter()
                .filter(|value| value.contains(&roads[road]))
                .map(|value| {
                    let other = *value
                        .iter()
                        .find(|&&candidate| candidate != roads[road])
                        .unwrap();
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
    while cycle.len() < 8 {
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

fn canonical_pair(first: usize, second: usize) -> (usize, usize) {
    if first < second {
        (first, second)
    } else {
        (second, first)
    }
}

fn graph_boundary(vertices: usize, edges: &[(usize, usize)]) -> Matrix {
    let mut result = vec![vec![0_i64; edges.len()]; vertices];
    for (column, &(first, second)) in edges.iter().enumerate() {
        result[first][column] = -1;
        result[second][column] = 1;
    }
    result
}

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    let rows = left.len();
    let columns = right.first().map_or(0, Vec::len);
    let middle = right.len();
    let mut result = vec![vec![0_i64; columns]; rows];
    for row in 0..rows {
        for column in 0..columns {
            result[row][column] = (0..middle)
                .map(|index| left[row][index] * right[index][column])
                .sum();
        }
    }
    result
}

fn unit_smith_rank(matrix: &Matrix) -> usize {
    let mut value = matrix.clone();
    let rows = value.len();
    let columns = value.first().map_or(0, Vec::len);
    let mut pivot = 0;
    while pivot < rows.min(columns) {
        let found = (pivot..rows).find_map(|row| {
            (pivot..columns)
                .find(|&column| value[row][column].abs() == 1)
                .map(|column| (row, column))
        });
        let Some((row, column)) = found else {
            break;
        };
        value.swap(pivot, row);
        for row_value in &mut value {
            row_value.swap(pivot, column);
        }
        if value[pivot][pivot] == -1 {
            for entry in &mut value[pivot] {
                *entry = -*entry;
            }
        }
        for row in 0..rows {
            if row != pivot {
                let multiple = value[row][pivot];
                for column in pivot..columns {
                    value[row][column] -= multiple * value[pivot][column];
                }
            }
        }
        for column in 0..columns {
            if column != pivot {
                let multiple = value[pivot][column];
                for row in 0..rows {
                    value[row][column] -= multiple * value[row][pivot];
                }
            }
        }
        pivot += 1;
    }
    assert!(value[pivot..]
        .iter()
        .all(|row| row[pivot..].iter().all(|&entry| entry == 0)));
    pivot
}

fn check_marked_paths_and_pc_typing(
    triangulations: &[Triangulation],
    adjacency: &[Vec<usize>],
    fibers: &[Vec<usize>],
    plus: &[Matching],
    minus: &[Matching],
) {
    let mut path_count = 0;
    let mut two_route_count = 0;
    for matching in plus.iter().chain(minus) {
        let paths = marked_scalar_paths(*matching, triangulations, adjacency, fibers);
        path_count += paths.len();
        two_route_count += usize::from(paths.len() == 2);
        for (source, middle, endpoint) in paths {
            assert!(triangulations[source].contains(&matching.mark));
            assert!(triangulations[middle].contains(&matching.mark));
            assert!(triangulations[endpoint].contains(&matching.mark));
            assert_ne!(source, endpoint);
        }
    }
    assert!(path_count >= 40);
    assert!(two_route_count > 0);

    // Structural proof behind the exhaustive check: if the first flip
    // removed d, the only second flip that could restore d is the inverse
    // flip, returning to the source.  Every matched endpoint has rank-two
    // physical core while every source has rank zero, so backtracking is
    // impossible.  Hence -X_d is constant on each complete path.
}

fn check_octagon_and_transition_typing(
    roads: &[Diagonal],
    quadrangulations: &[Quadrangulation],
    plus: &[Matching],
    minus: &[Matching],
) {
    let cycle = road_cycle(roads, quadrangulations);
    let outer_vertices: Vec<_> = (0..8)
        .map(|index| {
            let mut value = [roads[cycle[index]], roads[cycle[(index + 1) % 8]]];
            value.sort();
            quadrangulations
                .iter()
                .position(|candidate| *candidate == value)
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
    let outer_edges: BTreeSet<_> = (0..8)
        .map(|index| canonical_pair(outer_vertices[index], outer_vertices[(index + 1) % 8]))
        .collect();

    // Adjacent regional cubes share one core road, but the two companions
    // cross.  Thus no scalar triangulation belongs to both exact-core cubes.
    for index in 0..8 {
        let first = quadrangulations[outer_vertices[index]];
        let second = quadrangulations[outer_vertices[(index + 1) % 8]];
        assert_eq!(intersection_size(&first, &second), 1);
        let first_only = *first.iter().find(|value| !second.contains(value)).unwrap();
        let second_only = *second.iter().find(|value| !first.contains(value)).unwrap();
        assert!(crosses(first_only, second_only));
    }

    // Core-forgotten contact transport: pair the scalar-derived minus and
    // plus targets and enumerate every length-two geodesic in the line graph.
    let plus_map: BTreeMap<_, _> = plus
        .iter()
        .map(|matching| ((matching.source, matching.mark), matching.target))
        .collect();
    let minus_map: BTreeMap<_, _> = minus
        .iter()
        .map(|matching| ((matching.source, matching.mark), matching.target))
        .collect();
    assert_eq!(
        plus_map.keys().collect::<Vec<_>>(),
        minus_map.keys().collect::<Vec<_>>()
    );
    let q_adjacency = quadrangulation_adjacency(quadrangulations);
    let mut support = BTreeSet::new();
    let mut unique = 0;
    let mut ambiguous = 0;
    for key in plus_map.keys() {
        let start = minus_map[key];
        let end = plus_map[key];
        let middles: Vec<_> = q_adjacency[start]
            .iter()
            .copied()
            .filter(|middle| q_adjacency[*middle].contains(&end))
            .collect();
        assert!((1..=2).contains(&middles.len()));
        unique += usize::from(middles.len() == 1);
        ambiguous += usize::from(middles.len() == 2);
        for middle in middles {
            support.insert(canonical_pair(start, middle));
            support.insert(canonical_pair(middle, end));
        }
    }
    assert_eq!((unique, ambiguous), (16, 4));
    assert!(support.is_disjoint(&outer_edges));

    // The 12 filled local faces form a Mobius band.  Its additive boundary
    // is the outer octagon, but no multiplicative transition maps are part
    // of this incidence complex.
    let flips: Vec<_> = (0..quadrangulations.len())
        .flat_map(|first| {
            (first + 1..quadrangulations.len())
                .filter(move |&second| {
                    intersection_size(&quadrangulations[first], &quadrangulations[second]) == 1
                })
                .map(move |second| (first, second))
        })
        .collect();
    assert_eq!(flips.len(), 24);
    let edge_index: BTreeMap<_, _> = flips
        .iter()
        .copied()
        .enumerate()
        .map(|(index, edge)| (edge, index))
        .collect();
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
            let mut value = [roads[cycle[index]], roads[cycle[index + 4]]];
            value.sort();
            quadrangulations
                .iter()
                .position(|candidate| *candidate == value)
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
    let d1 = graph_boundary(quadrangulations.len(), &flips);
    let mut d2 = vec![vec![0_i64; faces.len()]; flips.len()];
    for (column, face) in faces.iter().enumerate() {
        for index in 0..face.len() {
            let first = face[index];
            let second = face[(index + 1) % face.len()];
            let edge = canonical_pair(first, second);
            d2[edge_index[&edge]][column] += if first < second { 1 } else { -1 };
        }
    }
    assert!(multiply(&d1, &d2).iter().flatten().all(|&entry| entry == 0));
    assert_eq!((unit_smith_rank(&d1), unit_smith_rank(&d2)), (11, 12));
    assert_eq!(flips.len() - 11 - 12, 1);

    println!(
        "  physical-road outer cycle: {:?}",
        cycle.iter().map(|&i| roads[i]).collect::<Vec<_>>()
    );
    println!(
        "  residual quadrangulation octagon: {:?}",
        outer_vertices
            .iter()
            .map(|&i| quadrangulations[i])
            .collect::<Vec<_>>()
    );
}

fn main() {
    let triangulations = triangulations();
    let adjacency = triangulation_adjacency(&triangulations);
    let roads = physical_diagonals();
    let quadrangulations = quadrangulations(&roads);
    let zero_core: Vec<_> = triangulations
        .iter()
        .enumerate()
        .filter_map(|(index, value)| physical_core(value).is_empty().then_some(index))
        .collect();
    assert_eq!(zero_core.len(), 4);
    let fibers: Vec<Vec<_>> = quadrangulations
        .iter()
        .map(|value| {
            triangulations
                .iter()
                .enumerate()
                .filter_map(|(index, triangulation)| {
                    (physical_core(triangulation) == value.to_vec()).then_some(index)
                })
                .collect()
        })
        .collect();
    assert!(fibers.iter().all(|fiber| fiber.len() == 8));
    let distances: BTreeMap<_, _> = zero_core
        .iter()
        .copied()
        .map(|source| (source, bfs_distances(source, &adjacency)))
        .collect();
    let plus = derive_matching(
        true,
        &triangulations,
        &quadrangulations,
        &zero_core,
        &fibers,
        &distances,
    );
    let minus = derive_matching(
        false,
        &triangulations,
        &quadrangulations,
        &zero_core,
        &fibers,
        &distances,
    );

    // One-step deck rotation exchanges the two marked matchings.
    let rotated_plus: BTreeSet<_> = plus
        .iter()
        .map(|matching| {
            let mut rotated_triangulation: Triangulation = triangulations[matching.source]
                .iter()
                .copied()
                .map(|value| rotate(value, 1))
                .collect();
            rotated_triangulation.sort();
            let source = triangulations
                .iter()
                .position(|candidate| *candidate == rotated_triangulation)
                .unwrap();
            let mut rotated_quadrangulation =
                quadrangulations[matching.target].map(|value| rotate(value, 1));
            rotated_quadrangulation.sort();
            let target = quadrangulations
                .iter()
                .position(|candidate| *candidate == rotated_quadrangulation)
                .unwrap();
            Matching {
                source,
                mark: rotate(matching.mark, 1),
                target,
            }
        })
        .collect();
    assert_eq!(rotated_plus, minus.iter().copied().collect());

    check_marked_paths_and_pc_typing(&triangulations, &adjacency, &fibers, &plus, &minus);
    check_octagon_and_transition_typing(&roads, &quadrangulations, &plus, &minus);

    println!("marked octagon target-first PC audit");
    println!("  scalar triangulations: 132; quadrangulations: 12; zero-core sources: 4");
    println!("  both scalar-derived marked matchings contain 20 occurrences");
    println!("  every matched length-two scalar path retains its mark at the middle vertex");
    println!("  each -X_d coefficient is constant on one fixed-mark associahedral face");
    println!("  the A-linear facewise PC map therefore acts on the global marked chain");
    println!("  contact transport support is disjoint from all eight outer-octagon edges");
    println!("  ordinary and sign-twisted additive octagon circulation are exactly zero");
    println!("  adjacent regional cubes are disjoint and meet only through a Gysin span");
    println!("  H_oct=T7...T0 is not typed by the established noninvertible data");
    println!("  the correct marked obstruction is additive, and it vanishes before loading");
    println!();
    println!("VERDICT: PROVED FOR THE MARKED CONTACT SECTOR");
    println!("  global PC descent follows without horizontal transition automorphisms");
    println!("  unmarked/full-symbol horizontal correspondence remains open");
}
