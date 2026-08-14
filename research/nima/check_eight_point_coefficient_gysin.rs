//! Exhaustive coefficient audit for the marked octagon link/Gysin question.
//!
//! This certificate deliberately separates three structures which have
//! different domains in the ledger:
//!
//! * the strict Laurent-valued physical coaction of entries 27 and 32;
//! * the normal orientation line and its Koszul signs from entry 38;
//! * the cellular square/pentagon boundaries of the scalar associahedron.
//!
//! The first two are sufficient on the sixteen transverse squares.  The
//! eight transverse pentagons contain a same-core scalar edge dependent on
//! the physicalizing chain.  It is not one of the independent-factor mixed
//! cells covered by the rooted-spine theorem (entry 37).  Consequently the
//! repository does not define the coefficient transport on that edge for the
//! full eight-dimensional rank-two occurrence fiber.  The executable records
//! this as missing data; it does not manufacture a sign from a Ward matrix.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

const N: usize = 8;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge(usize, usize);

type Triangulation = Vec<Edge>;
type Cell = Vec<usize>;

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Occurrence {
    marks: Vec<(Cell, Edge)>,
    numerators: Vec<Edge>,
    denominators: Vec<Edge>,
    coefficient: i64,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum FaceKind {
    Square,
    Pentagon,
}

#[derive(Clone, Debug)]
struct RouteFace {
    vertices: Vec<usize>,
    common: Vec<Edge>,
    core: [Edge; 2],
    sheet: usize,
    kind: FaceKind,
    boundary: BTreeMap<(usize, usize), i64>,
}

fn edge(first: usize, second: usize) -> Edge {
    assert_ne!(first, second);
    if first < second {
        Edge(first, second)
    } else {
        Edge(second, first)
    }
}

fn boundary_edge(value: Edge) -> bool {
    value.1 == value.0 + 1 || (value.0 == 0 && value.1 == N - 1)
}

fn crossing(first: Edge, second: Edge) -> bool {
    if [first.0, first.1]
        .iter()
        .any(|endpoint| *endpoint == second.0 || *endpoint == second.1)
    {
        return false;
    }
    (first.0 < second.0 && second.0 < first.1 && first.1 < second.1)
        || (second.0 < first.0 && first.0 < second.1 && second.1 < first.1)
}

fn physical(value: Edge) -> bool {
    value.0 % 2 != value.1 % 2
}

fn polygon_diagonals() -> Vec<Edge> {
    let mut result = Vec::new();
    for first in 0..N {
        for second in first + 1..N {
            let candidate = edge(first, second);
            if !boundary_edge(candidate) {
                result.push(candidate);
            }
        }
    }
    result
}

fn choose_noncrossing(
    diagonals: &[Edge],
    start: usize,
    required: usize,
    current: &mut Vec<Edge>,
    output: &mut Vec<Triangulation>,
) {
    if required == 0 {
        output.push(current.clone());
        return;
    }
    if diagonals.len() - start < required {
        return;
    }
    for index in start..=diagonals.len() - required {
        let candidate = diagonals[index];
        if current.iter().any(|&chosen| crossing(candidate, chosen)) {
            continue;
        }
        current.push(candidate);
        choose_noncrossing(diagonals, index + 1, required - 1, current, output);
        current.pop();
    }
}

fn triangulations() -> Vec<Triangulation> {
    let diagonals = polygon_diagonals();
    let mut result = Vec::new();
    choose_noncrossing(&diagonals, 0, N - 3, &mut Vec::new(), &mut result);
    for triangulation in &mut result {
        triangulation.sort();
    }
    result.sort();
    result
}

fn core(triangulation: &Triangulation) -> Vec<Edge> {
    triangulation
        .iter()
        .copied()
        .filter(|&diagonal| physical(diagonal))
        .collect()
}

fn adjacent(first: &Triangulation, second: &Triangulation) -> bool {
    first
        .iter()
        .filter(|diagonal| second.contains(diagonal))
        .count()
        + 1
        == first.len()
}

fn rotate_edge(value: Edge) -> Edge {
    edge((value.0 + 1) % N, (value.1 + 1) % N)
}

fn rotate_triangulation(value: &Triangulation) -> Triangulation {
    let mut result: Vec<_> = value.iter().copied().map(rotate_edge).collect();
    result.sort();
    result
}

fn two_faces(tris: &[Triangulation]) -> Vec<(Vec<Edge>, Vec<usize>)> {
    let diagonals = polygon_diagonals();
    let mut result = Vec::new();
    for first in 0..diagonals.len() {
        for second in first + 1..diagonals.len() {
            for third in second + 1..diagonals.len() {
                let fixed = vec![diagonals[first], diagonals[second], diagonals[third]];
                if crossing(fixed[0], fixed[1])
                    || crossing(fixed[0], fixed[2])
                    || crossing(fixed[1], fixed[2])
                {
                    continue;
                }
                let vertices: Vec<_> = tris
                    .iter()
                    .enumerate()
                    .filter(|(_, triangulation)| {
                        fixed
                            .iter()
                            .all(|diagonal| triangulation.contains(diagonal))
                    })
                    .map(|(index, _)| index)
                    .collect();
                assert!(vertices.len() == 4 || vertices.len() == 5);
                result.push((fixed, vertices));
            }
        }
    }
    result.sort();
    result.dedup();
    result
}

fn cyclic_order(vertices: &[usize], tris: &[Triangulation]) -> Vec<usize> {
    let mut result = vec![vertices[0]];
    let first_neighbors: Vec<_> = vertices
        .iter()
        .copied()
        .filter(|&candidate| {
            candidate != vertices[0] && adjacent(&tris[vertices[0]], &tris[candidate])
        })
        .collect();
    assert_eq!(first_neighbors.len(), 2);
    result.push(*first_neighbors.iter().min().unwrap());
    while result.len() < vertices.len() {
        let previous = result[result.len() - 2];
        let current = result[result.len() - 1];
        let next = vertices
            .iter()
            .copied()
            .find(|&candidate| {
                candidate != previous
                    && !result.contains(&candidate)
                    && adjacent(&tris[current], &tris[candidate])
            })
            .expect("two-face boundary continuation");
        result.push(next);
    }
    assert!(adjacent(&tris[*result.last().unwrap()], &tris[result[0]]));
    result
}

fn oriented_boundary(vertices: &[usize]) -> BTreeMap<(usize, usize), i64> {
    let mut result = BTreeMap::<(usize, usize), i64>::new();
    for index in 0..vertices.len() {
        let first = vertices[index];
        let second = vertices[(index + 1) % vertices.len()];
        let key = if first < second {
            (first, second)
        } else {
            (second, first)
        };
        *result.entry(key).or_insert(0) += if first < second { 1 } else { -1 };
    }
    assert!(result.values().all(|entry| entry.abs() == 1));
    let mut vertex_boundary = BTreeMap::<usize, i64>::new();
    for (&(first, second), &coefficient) in &result {
        *vertex_boundary.entry(first).or_insert(0) -= coefficient;
        *vertex_boundary.entry(second).or_insert(0) += coefficient;
    }
    assert!(vertex_boundary.values().all(|&entry| entry == 0));
    result
}

fn scalar_sheet(triangulation: &Triangulation) -> usize {
    assert!(core(triangulation).is_empty());
    let parities: BTreeSet<_> = triangulation
        .iter()
        .map(|diagonal| diagonal.0 % 2)
        .collect();
    assert_eq!(parities.len(), 1);
    *parities.iter().next().unwrap()
}

fn transverse_faces(tris: &[Triangulation]) -> Vec<RouteFace> {
    let mut result = Vec::new();
    for (common, vertices) in two_faces(tris) {
        let labels: Vec<_> = vertices.iter().map(|&index| core(&tris[index])).collect();
        let rank_two: BTreeSet<_> = labels
            .iter()
            .filter(|label| label.len() == 2)
            .cloned()
            .collect();
        if !labels.iter().any(Vec::is_empty) || rank_two.len() != 1 {
            continue;
        }
        let current = rank_two.iter().next().unwrap();
        if labels
            .iter()
            .any(|label| !label.iter().all(|diagonal| current.contains(diagonal)))
        {
            continue;
        }
        let sheets: BTreeSet<_> = vertices
            .iter()
            .filter(|&&index| core(&tris[index]).is_empty())
            .map(|&index| scalar_sheet(&tris[index]))
            .collect();
        assert_eq!(sheets.len(), 1);
        let ranks: Vec<_> = vertices
            .iter()
            .map(|&index| core(&tris[index]).len())
            .collect();
        let kind = match vertices.len() {
            4 => {
                assert_eq!(ranks.iter().filter(|&&rank| rank == 0).count(), 1);
                assert_eq!(ranks.iter().filter(|&&rank| rank == 1).count(), 2);
                assert_eq!(ranks.iter().filter(|&&rank| rank == 2).count(), 1);
                FaceKind::Square
            }
            5 => {
                assert_eq!(ranks.iter().filter(|&&rank| rank == 0).count(), 2);
                assert_eq!(ranks.iter().filter(|&&rank| rank == 1).count(), 2);
                assert_eq!(ranks.iter().filter(|&&rank| rank == 2).count(), 1);
                FaceKind::Pentagon
            }
            _ => unreachable!(),
        };
        let ordered = cyclic_order(&vertices, tris);
        result.push(RouteFace {
            vertices: ordered.clone(),
            common,
            core: [current[0], current[1]],
            sheet: *sheets.iter().next().unwrap(),
            kind,
            boundary: oriented_boundary(&ordered),
        });
    }
    result.sort_by_key(|face| (face.core, face.sheet));
    result
}

fn core_regions(current: &[Edge]) -> Vec<Cell> {
    let mut regions = vec![(0..N).collect::<Vec<_>>()];
    for &Edge(first, second) in current {
        let candidates: Vec<_> = regions
            .iter()
            .enumerate()
            .filter_map(|(region_index, region)| {
                let first_index = region.iter().position(|&vertex| vertex == first)?;
                let second_index = region.iter().position(|&vertex| vertex == second)?;
                let distance = (second_index + region.len() - first_index) % region.len();
                (distance != 1 && distance != region.len() - 1).then_some((
                    region_index,
                    first_index,
                    second_index,
                ))
            })
            .collect();
        assert_eq!(candidates.len(), 1);
        let (region_index, mut first_index, mut second_index) = candidates[0];
        let region = regions.remove(region_index);
        if first_index > second_index {
            std::mem::swap(&mut first_index, &mut second_index);
        }
        regions.push(region[first_index..=second_index].to_vec());
        let mut other = region[second_index..].to_vec();
        other.extend_from_slice(&region[..=first_index]);
        regions.push(other);
    }
    for region in &mut regions {
        region.sort_unstable();
    }
    regions.sort();
    result_regions_sanity(&regions, current.len());
    regions
}

fn result_regions_sanity(regions: &[Cell], cut_rank: usize) {
    assert_eq!(regions.len(), cut_rank + 1);
    assert!(regions.iter().all(|region| region.len() % 2 == 0));
}

fn cell_slots(cell: &Cell) -> [Edge; 2] {
    assert_eq!(cell.len(), 4);
    let mut result = [edge(cell[0], cell[2]), edge(cell[1], cell[3])];
    result.sort();
    result
}

fn full_occurrences(current: [Edge; 2]) -> BTreeSet<Occurrence> {
    let cells = core_regions(&current);
    assert_eq!(
        cells.iter().map(Vec::len).collect::<Vec<_>>(),
        vec![4, 4, 4]
    );
    let slots: Vec<_> = cells.iter().map(cell_slots).collect();
    let mut result = BTreeSet::new();
    for mask in 0..8 {
        let mut marks = Vec::new();
        let mut numerators = Vec::new();
        for index in 0..3 {
            let mark = slots[index][(mask >> index) & 1];
            marks.push((cells[index].clone(), mark));
            numerators.push(mark);
        }
        marks.sort();
        numerators.sort();
        result.insert(Occurrence {
            marks,
            numerators,
            denominators: current.to_vec(),
            coefficient: -1,
        });
    }
    assert_eq!(result.len(), 8);
    result
}

fn cell_side(cell: &Cell, diagonal: Edge) -> usize {
    let inside = cell
        .iter()
        .filter(|&&vertex| vertex != diagonal.0 && vertex != diagonal.1)
        .filter(|&&vertex| diagonal.0 < vertex && vertex < diagonal.1)
        .count();
    if inside == 2 {
        0
    } else {
        assert_eq!(inside, 0);
        1
    }
}

fn directed_edges(current: [Edge; 2], plus: bool) -> BTreeMap<Edge, (Cell, Cell)> {
    let cells = core_regions(&current);
    let mut result = BTreeMap::new();
    for diagonal in current {
        let adjacent: Vec<_> = cells
            .iter()
            .filter(|cell| cell.contains(&diagonal.0) && cell.contains(&diagonal.1))
            .cloned()
            .collect();
        assert_eq!(adjacent.len(), 2);
        let plus_side = if diagonal.0 % 2 == 0 { 1 } else { 0 };
        let target_side = if plus { plus_side } else { 1 - plus_side };
        let target = adjacent
            .iter()
            .find(|cell| cell_side(cell, diagonal) == target_side)
            .unwrap()
            .clone();
        let source = adjacent
            .iter()
            .find(|cell| **cell != target)
            .unwrap()
            .clone();
        result.insert(diagonal, (source, target));
    }
    result
}

fn forest_sinks(
    cells: &[Cell],
    directions: &BTreeMap<Edge, (Cell, Cell)>,
    cut: &BTreeSet<Edge>,
) -> Vec<Cell> {
    let cell_index: BTreeMap<_, _> = cells
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, cell)| (cell, index))
        .collect();
    let mut adjacency = vec![Vec::new(); cells.len()];
    let mut outgoing = vec![false; cells.len()];
    for (diagonal, (source, target)) in directions {
        if cut.contains(diagonal) {
            continue;
        }
        let source_index = cell_index[source];
        let target_index = cell_index[target];
        adjacency[source_index].push(target_index);
        adjacency[target_index].push(source_index);
        outgoing[source_index] = true;
    }
    let mut seen = vec![false; cells.len()];
    let mut result = Vec::new();
    for start in 0..cells.len() {
        if seen[start] {
            continue;
        }
        let mut component = Vec::new();
        let mut queue = VecDeque::from([start]);
        seen[start] = true;
        while let Some(index) = queue.pop_front() {
            component.push(index);
            for &neighbor in &adjacency[index] {
                if !seen[neighbor] {
                    seen[neighbor] = true;
                    queue.push_back(neighbor);
                }
            }
        }
        let sinks: Vec<_> = component
            .into_iter()
            .filter(|&index| !outgoing[index])
            .collect();
        if sinks.len() != 1 {
            return Vec::new();
        }
        result.push(cells[sinks[0]].clone());
    }
    result.sort();
    result
}

fn expanded_occurrences(
    current: [Edge; 2],
    plus: bool,
    global_mark: Edge,
    order: [Edge; 2],
) -> BTreeSet<Occurrence> {
    let cells = core_regions(&current);
    let directions = directed_edges(current, plus);
    let sinks = forest_sinks(&cells, &directions, &BTreeSet::new());
    assert_eq!(sinks.len(), 1);
    let global_sink = sinks[0].clone();
    assert!(cell_slots(&global_sink).contains(&global_mark));

    let mut records = BTreeSet::from([Occurrence {
        marks: vec![(global_sink, global_mark)],
        numerators: vec![global_mark],
        denominators: Vec::new(),
        coefficient: -1,
    }]);
    let mut cut = BTreeSet::new();
    for diagonal in order {
        let old_sinks = forest_sinks(&cells, &directions, &cut);
        cut.insert(diagonal);
        let new_sinks = forest_sinks(&cells, &directions, &cut);
        let source = directions[&diagonal].0.clone();
        let mut expected = old_sinks;
        expected.push(source.clone());
        expected.sort();
        assert_eq!(new_sinks, expected);

        let mut next = BTreeSet::new();
        for occurrence in records {
            for slot in cell_slots(&source) {
                let mut marks = occurrence.marks.clone();
                marks.push((source.clone(), slot));
                marks.sort();
                let mut numerators = occurrence.numerators.clone();
                numerators.push(slot);
                numerators.sort();
                let mut denominators = occurrence.denominators.clone();
                denominators.push(diagonal);
                denominators.sort();
                next.insert(Occurrence {
                    marks,
                    numerators,
                    denominators,
                    coefficient: -occurrence.coefficient,
                });
            }
        }
        records = next;
    }
    assert_eq!(records.len(), 4);
    assert!(records
        .iter()
        .all(|occurrence| occurrence.coefficient == -1));
    records
}

fn factorization_occurrences(current: [Edge; 2], marked: Edge) -> BTreeSet<Occurrence> {
    let other = *current
        .iter()
        .find(|&&diagonal| diagonal != marked)
        .unwrap();
    let cut_regions = core_regions(&[marked]);
    let spectator = cut_regions.iter().find(|region| region.len() == 4).unwrap();
    let local = cut_regions.iter().find(|region| region.len() == 6).unwrap();
    assert!(local.contains(&other.0) && local.contains(&other.1));
    let cells = core_regions(&current);
    let spectator_cell = cells.iter().find(|cell| *cell == spectator).unwrap();
    let local_cells: Vec<_> = cells
        .iter()
        .filter(|cell| cell.iter().all(|vertex| local.contains(vertex)))
        .collect();
    assert_eq!(local_cells.len(), 2);

    let mut result = BTreeSet::new();
    for spectator_slot in cell_slots(spectator_cell) {
        for local_mask in 0..4 {
            let mut marks = vec![(spectator_cell.clone(), spectator_slot)];
            let mut numerators = vec![spectator_slot];
            for (index, cell) in local_cells.iter().enumerate() {
                let slot = cell_slots(cell)[(local_mask >> index) & 1];
                marks.push(((*cell).clone(), slot));
                numerators.push(slot);
            }
            marks.sort();
            numerators.sort();
            // L_4(empty) has sign -1 and L_6(q_E) has sign +1.
            result.insert(Occurrence {
                marks,
                numerators,
                denominators: current.to_vec(),
                coefficient: -1,
            });
        }
    }
    assert_eq!(result.len(), 2 * 4);
    result
}

fn orientation_sign(ordered: [Edge; 2], canonical: [Edge; 2]) -> i64 {
    if ordered == canonical {
        1
    } else {
        assert_eq!(ordered, [canonical[1], canonical[0]]);
        -1
    }
}

fn rotate_core_orientation_sign(current: [Edge; 2]) -> i64 {
    let transported = [rotate_edge(current[0]), rotate_edge(current[1])];
    let mut target = transported;
    target.sort();
    orientation_sign(transported, target)
}

fn rotate_boundary(
    boundary: &BTreeMap<(usize, usize), i64>,
    rotation: &[usize],
) -> BTreeMap<(usize, usize), i64> {
    let mut result = BTreeMap::new();
    for (&(first, second), &coefficient) in boundary {
        let rotated_first = rotation[first];
        let rotated_second = rotation[second];
        let (key, sign) = if rotated_first < rotated_second {
            ((rotated_first, rotated_second), 1)
        } else {
            ((rotated_second, rotated_first), -1)
        };
        *result.entry(key).or_insert(0) += coefficient * sign;
    }
    result
}

fn boundary_transport_sign(face: &RouteFace, target: &RouteFace, rotation: &[usize]) -> i64 {
    let transported = rotate_boundary(&face.boundary, rotation);
    if transported == target.boundary {
        1
    } else {
        let negative: BTreeMap<_, _> = target
            .boundary
            .iter()
            .map(|(&key, &coefficient)| (key, -coefficient))
            .collect();
        assert_eq!(transported, negative);
        -1
    }
}

fn boundary_word(face: &RouteFace) -> String {
    face.boundary
        .values()
        .map(|&coefficient| if coefficient == 1 { '+' } else { '-' })
        .collect()
}

fn compatibility_graph(roads: &[Edge]) -> Vec<(usize, usize)> {
    let mut result = Vec::new();
    for first in 0..roads.len() {
        for second in first + 1..roads.len() {
            if !crossing(roads[first], roads[second]) {
                result.push((first, second));
            }
        }
    }
    result
}

fn local_suspension_audit(roads: &[Edge], cores: &[[Edge; 2]]) -> usize {
    let mut checks = 0;
    for &marked in roads {
        let local: Vec<_> = cores
            .iter()
            .filter_map(|current| {
                if current.contains(&marked) {
                    Some(*current.iter().find(|&&road| road != marked).unwrap())
                } else {
                    None
                }
            })
            .collect();
        assert_eq!(local.len(), 3);
        assert_eq!(local.iter().copied().collect::<BTreeSet<_>>().len(), 3);
        for first in 0..3 {
            for second in first + 1..3 {
                // The reduced local source is formed only after the three
                // distinct coefficient fibers have factored to three direct
                // summands.  No occurrence bases are identified here.
                let mut source = [0_i64; 3];
                source[first] = 1;
                source[second] = -1;
                assert_eq!(source.iter().sum::<i64>(), 0);

                // Edges are ordered (center, road).  Gamma sends a road
                // difference to the four-edge K_(2,3) circuit.
                let mut circuit = [0_i64; 6];
                circuit[2 * first] = 1;
                circuit[2 * first + 1] = -1;
                circuit[2 * second] = -1;
                circuit[2 * second + 1] = 1;
                let mut vertex_boundary = [0_i64; 5];
                for road in 0..3 {
                    for center in 0..2 {
                        let coefficient = circuit[2 * road + center];
                        vertex_boundary[center] -= coefficient;
                        vertex_boundary[2 + road] += coefficient;
                    }
                }
                assert_eq!(vertex_boundary, [0; 5]);
                assert_eq!(circuit.iter().filter(|&&entry| entry != 0).count(), 4);
                checks += 1;
            }
        }
    }
    checks
}

fn determinant(mut matrix: Vec<Vec<i128>>) -> i128 {
    assert!(matrix.iter().all(|row| row.len() == matrix.len()));
    let size = matrix.len();
    let mut previous = 1_i128;
    let mut sign = 1_i128;
    for column in 0..size - 1 {
        let row = (column..size)
            .find(|&row| matrix[row][column] != 0)
            .expect("nonsingular matrix");
        if row != column {
            matrix.swap(row, column);
            sign = -sign;
        }
        let pivot = matrix[column][column];
        for row in column + 1..size {
            for next in column + 1..size {
                let numerator =
                    matrix[row][next] * pivot - matrix[row][column] * matrix[column][next];
                assert_eq!(numerator % previous, 0);
                matrix[row][next] = numerator / previous;
            }
        }
        previous = pivot;
    }
    sign * matrix[size - 1][size - 1]
}

fn oriented_graph_cycle(
    vertices: &[usize],
    edge_index: &BTreeMap<(usize, usize), usize>,
) -> Vec<i128> {
    let mut result = vec![0; edge_index.len()];
    for index in 0..vertices.len() {
        let first = vertices[index];
        let second = vertices[(index + 1) % vertices.len()];
        let key = if first < second {
            (first, second)
        } else {
            (second, first)
        };
        result[edge_index[&key]] += if first < second { 1 } else { -1 };
    }
    result
}

fn residual_octagon_audit(roads: &[Edge], compatibility: &[(usize, usize)]) -> (i64, i64, i64) {
    let road_index: BTreeMap<_, _> = roads
        .iter()
        .copied()
        .enumerate()
        .map(|(index, road)| (road, index))
        .collect();
    let mut orbit = vec![roads[0]];
    while orbit.len() < 8 {
        orbit.push(rotate_edge(*orbit.last().unwrap()));
    }
    assert_eq!(orbit.iter().copied().collect::<BTreeSet<_>>().len(), 8);

    // This is the transport which the repository actually defines: eight
    // successive one-step rotations.  It is not yet a transport along the
    // edges of the compatibility octagon.
    let mut deck_scalar_holonomy = 1;
    let mut deck_polarity_holonomy = 1;
    for index in 0..8 {
        let mut current = [orbit[index], orbit[(index + 1) % 8]];
        current.sort();
        deck_scalar_holonomy *= rotate_core_orientation_sign(current);
        deck_polarity_holonomy *= -1;
    }
    let deck_tensor_holonomy = deck_scalar_holonomy * deck_polarity_holonomy;
    assert_eq!(
        (
            deck_scalar_holonomy,
            deck_polarity_holonomy,
            deck_tensor_holonomy
        ),
        (1, 1, 1)
    );

    // Derive the residual compatibility octagon by deleting the four Mobius
    // rungs.  The raw deck orbit above is not this cyclic order: its closing
    // pair crosses.
    let adjacency: Vec<Vec<usize>> = (0..roads.len())
        .map(|vertex| {
            compatibility
                .iter()
                .filter_map(|&(first, second)| {
                    if first == vertex {
                        Some(second)
                    } else if second == vertex {
                        Some(first)
                    } else {
                        None
                    }
                })
                .collect()
        })
        .collect();
    let antipode: Vec<_> = roads
        .iter()
        .map(|&road| edge((road.0 + 4) % N, (road.1 + 4) % N))
        .map(|road| road_index[&road])
        .collect();
    let outer_neighbors: Vec<Vec<_>> = adjacency
        .iter()
        .enumerate()
        .map(|(vertex, neighbors)| {
            neighbors
                .iter()
                .copied()
                .filter(|&neighbor| neighbor != antipode[vertex])
                .collect()
        })
        .collect();
    assert!(outer_neighbors.iter().all(|neighbors| neighbors.len() == 2));
    let mut cycle = vec![0];
    let mut previous = usize::MAX;
    while cycle.len() < roads.len() {
        let current = *cycle.last().unwrap();
        let next = outer_neighbors[current]
            .iter()
            .copied()
            .find(|&candidate| candidate != previous)
            .unwrap();
        previous = current;
        cycle.push(next);
    }
    assert!(outer_neighbors[*cycle.last().unwrap()].contains(&cycle[0]));

    // Two admissible deck-equivariant edge-sign extensions are (+,+) and
    // (-,+) on the (outer,rung) rotation orbits.  They differ on every outer
    // edge, but both have +1 holonomy on the residual octagon and on every
    // ladder square.  Thus established deck constraints do not select a
    // pointwise edge transport, while they do rule out a sign twist capable
    // of removing the index-two obstruction.
    let is_outer = |first: usize, second: usize| outer_neighbors[first].contains(&second);
    for &(first, second) in compatibility {
        let mut rotated = [
            road_index[&rotate_edge(roads[first])],
            road_index[&rotate_edge(roads[second])],
        ];
        rotated.sort_unstable();
        assert!(compatibility.contains(&(rotated[0], rotated[1])));
        assert_eq!(is_outer(first, second), is_outer(rotated[0], rotated[1]));
    }
    let assignment_a = |_first: usize, _second: usize| 1_i64;
    let assignment_b = |first: usize, second: usize| {
        if is_outer(first, second) {
            -1_i64
        } else {
            1_i64
        }
    };
    let cycle_holonomy = |vertices: &[usize], assignment: &dyn Fn(usize, usize) -> i64| {
        (0..vertices.len())
            .map(|index| assignment(vertices[index], vertices[(index + 1) % vertices.len()]))
            .product::<i64>()
    };
    assert_eq!(cycle_holonomy(&cycle, &assignment_a), 1);
    assert_eq!(cycle_holonomy(&cycle, &assignment_b), 1);

    // The actual physical-normal comparison is available without choosing a
    // pentagon coefficient map.  At Q={D,E}, factoring first by D and first
    // by E gives opposite identifications with or(N_Q): their ratio is -1.
    // Every residual-octagon edge therefore has scalar-normal transition -1.
    // Each transverse route face remains on one regional-polarity sheet, so
    // its polarity transition is +1.  All three eight-edge holonomies are +1.
    let mut scalar_holonomy = 1_i64;
    let mut polarity_holonomy = 1_i64;
    for index in 0..cycle.len() {
        let first = roads[cycle[index]];
        let second = roads[cycle[(index + 1) % cycle.len()]];
        let mut current = [first, second];
        current.sort();
        let through_first = orientation_sign([first, second], current);
        let through_second = orientation_sign([second, first], current);
        scalar_holonomy *= through_second * through_first;
        polarity_holonomy *= 1;
    }
    let tensor_holonomy = scalar_holonomy * polarity_holonomy;
    assert_eq!(
        (scalar_holonomy, polarity_holonomy, tensor_holonomy),
        (1, 1, 1)
    );

    // Reproduce the five-cycle index calculation.  Four ladder squares plus
    // the residual octagon span an index-two sublattice of H1(G_8).
    let edge_index: BTreeMap<_, _> = compatibility
        .iter()
        .copied()
        .enumerate()
        .map(|(index, pair)| (pair, index))
        .collect();
    let outer = oriented_graph_cycle(&cycle, &edge_index);
    let mut faces = Vec::new();
    for index in 0..4 {
        let square = [
            cycle[index],
            cycle[(index + 1) % 8],
            cycle[(index + 5) % 8],
            cycle[(index + 4) % 8],
        ];
        assert_eq!(cycle_holonomy(&square, &assignment_a), 1);
        assert_eq!(cycle_holonomy(&square, &assignment_b), 1);
        faces.push(oriented_graph_cycle(&square, &edge_index));
    }
    faces.push(outer);

    let mut parent: Vec<_> = (0..roads.len()).collect();
    fn find(parent: &mut [usize], value: usize) -> usize {
        if parent[value] != value {
            parent[value] = find(parent, parent[value]);
        }
        parent[value]
    }
    let mut tree = BTreeSet::new();
    for (index, &(first, second)) in compatibility.iter().enumerate() {
        let first_root = find(&mut parent, first);
        let second_root = find(&mut parent, second);
        if first_root != second_root {
            parent[first_root] = second_root;
            tree.insert(index);
        }
    }
    let chords: Vec<_> = (0..compatibility.len())
        .filter(|index| !tree.contains(index))
        .collect();
    assert_eq!(chords.len(), 5);
    let coordinates: Vec<Vec<_>> = chords
        .iter()
        .map(|&row| faces.iter().map(|face| face[row]).collect())
        .collect();
    assert_eq!(determinant(coordinates).abs(), 2);
    (scalar_holonomy, polarity_holonomy, tensor_holonomy)
}

fn main() {
    let tris = triangulations();
    assert_eq!(tris.len(), 132);
    assert_eq!(two_faces(&tris).len(), 300);
    let faces = transverse_faces(&tris);
    assert_eq!(faces.len(), 24);
    assert_eq!(
        faces
            .iter()
            .filter(|face| face.kind == FaceKind::Square)
            .count(),
        16
    );
    assert_eq!(
        faces
            .iter()
            .filter(|face| face.kind == FaceKind::Pentagon)
            .count(),
        8
    );

    let tri_index: BTreeMap<_, _> = tris
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, triangulation)| (triangulation, index))
        .collect();
    let rotation: Vec<_> = tris
        .iter()
        .map(|triangulation| tri_index[&rotate_triangulation(triangulation)])
        .collect();
    let face_index: BTreeMap<_, _> = faces
        .iter()
        .enumerate()
        .map(|(index, face)| {
            let mut vertices = face.vertices.clone();
            vertices.sort_unstable();
            (vertices, index)
        })
        .collect();

    let mut cores: Vec<_> = faces.iter().map(|face| face.core).collect();
    cores.sort();
    cores.dedup();
    assert_eq!(cores.len(), 12);
    assert!(cores
        .iter()
        .all(|current| full_occurrences(*current).len() == 8));

    let mut factorization_checks = 0;
    let mut incidence_checks = 0;
    let mut factor_orientation_profile = BTreeMap::<i64, usize>::new();
    for &current in &cores {
        let full = full_occurrences(current);
        for marked in current {
            assert_eq!(factorization_occurrences(current, marked), full);
            let other = *current
                .iter()
                .find(|&&diagonal| diagonal != marked)
                .unwrap();
            let line_sign = orientation_sign([marked, other], current);
            *factor_orientation_profile.entry(line_sign).or_insert(0) += 1;
            factorization_checks += full.len();
            // Two regional-polarity centers meet every local coefficient road.
            incidence_checks += 2;
        }
    }
    assert_eq!(factorization_checks, 12 * 2 * 8);
    assert_eq!(incidence_checks, 48);
    assert_eq!(
        factor_orientation_profile,
        BTreeMap::from([(-1, 12), (1, 12)])
    );

    let mut support_profile = BTreeMap::<(bool, bool), usize>::new();
    let mut supported_kind_profile = BTreeMap::<&str, usize>::new();
    let mut expanded_terms = 0;
    let mut deck_face_signs = BTreeMap::<i64, usize>::new();
    let mut deck_normal_signs = BTreeMap::<i64, usize>::new();
    for (face_number, face) in faces.iter().enumerate() {
        let rotated_vertices = {
            let mut value: Vec<_> = face.vertices.iter().map(|&index| rotation[index]).collect();
            value.sort_unstable();
            value
        };
        let target = &faces[face_index[&rotated_vertices]];
        assert_eq!(target.sheet, 1 - face.sheet);
        assert_eq!(target.kind, face.kind);
        let face_sign = boundary_transport_sign(face, target, &rotation);
        let normal_sign = rotate_core_orientation_sign(face.core);
        *deck_face_signs.entry(face_sign).or_insert(0) += 1;
        *deck_normal_signs.entry(normal_sign).or_insert(0) += 1;

        let mut supported = [false; 2];
        for (polarity, plus) in [true, false].into_iter().enumerate() {
            let cells = core_regions(&face.core);
            let directions = directed_edges(face.core, plus);
            let sinks = forest_sinks(&cells, &directions, &BTreeSet::new());
            if sinks.len() == 1 {
                supported[polarity] = true;
                let key = match face.kind {
                    FaceKind::Square => "square",
                    FaceKind::Pentagon => "pentagon",
                };
                *supported_kind_profile.entry(key).or_insert(0) += 1;
                let sink_slots = cell_slots(&sinks[0]);
                let marks: Vec<_> = sink_slots
                    .iter()
                    .copied()
                    .filter(|mark| face.common.contains(mark))
                    .collect();
                assert_eq!(marks.len(), 1);
                let first =
                    expanded_occurrences(face.core, plus, marks[0], [face.core[0], face.core[1]]);
                let second =
                    expanded_occurrences(face.core, plus, marks[0], [face.core[1], face.core[0]]);
                // Entry 32: exact Laurent/occurrence equality, before any
                // normal-orientation identification.
                assert_eq!(first, second);
                assert!(first.is_subset(&full_occurrences(face.core)));
                expanded_terms += first.len();
            }
        }
        *support_profile
            .entry((supported[0], supported[1]))
            .or_insert(0) += 1;

        let kind = match face.kind {
            FaceKind::Square => "square",
            FaceKind::Pentagon => "pentagon/nontransverse-missing",
        };
        println!(
            "face {:02}: Q={:?}, sheet={}, {}, boundary={}, deck(face,normal,polarity,tensor)=({:+},{:+},-1,{:+}), supported(+,-)=({},{})",
            face_number + 1,
            face.core,
            face.sheet,
            kind,
            boundary_word(face),
            face_sign,
            normal_sign,
            -normal_sign,
            supported[0],
            supported[1]
        );
    }
    assert_eq!(support_profile.values().sum::<usize>(), 24);
    assert_eq!(support_profile.get(&(true, true)), Some(&16));
    assert_eq!(support_profile.get(&(true, false)), Some(&4));
    assert_eq!(support_profile.get(&(false, true)), Some(&4));
    assert_eq!(supported_kind_profile.get("square"), Some(&24));
    assert_eq!(supported_kind_profile.get("pentagon"), Some(&16));
    assert_eq!(expanded_terms, 40 * 4);
    let mut roads: Vec<_> = cores
        .iter()
        .flat_map(|current| current.iter().copied())
        .collect();
    roads.sort();
    roads.dedup();
    assert_eq!(roads.len(), 8);
    let indexed_compatibility = compatibility_graph(&roads);
    assert_eq!(indexed_compatibility.len(), 12);
    let suspension_checks = local_suspension_audit(&roads, &cores);
    assert_eq!(suspension_checks, 24);
    let holonomy = residual_octagon_audit(&roads, &indexed_compatibility);

    println!();
    println!("coefficient fiber and marked-Cut audit");
    println!("  full fibers: 12 copies of rank 8; L8({{D,E}})=L4(empty)[2] tensor L6(q_E)[4]");
    println!("  marked factorization basis checks: {factorization_checks}; center-road incidences: {incidence_checks}");
    println!(
        "  factor orientation signs for or(N_D) wedge or(N_E): {factor_orientation_profile:?}"
    );
    println!("  supported marked face occurrences: {supported_kind_profile:?}; 40 source records -> {expanded_terms} rank-two records");
    println!("  strict two-cut occurrence equality holds on every supported record");
    println!(
        "  deck face signs: {deck_face_signs:?}; deck normal-line signs: {deck_normal_signs:?}"
    );
    println!("  local reduced-road differences and K_(2,3) circuits: {suspension_checks}");
    println!("  residual-octagon holonomy (normal, polarity, tensor): {holonomy:?}");
    println!("  two deck-equivariant edge-sign extensions differ pointwise but are trivial on all five cycle generators");
    println!("  four squares plus octagon still have index 2; no allowed sign twist removes it");
    println!();
    println!("VERDICT: INCONCLUSIVE");
    println!("  16 square carriers are covered by strict physical coaction with Koszul orientation lines");
    println!(
        "  8 pentagons have rank pattern [0,0,1,2,1] and are nontransverse dependent-chain faces"
    );
    println!("  missing datum: coefficient/residue-line transport on each pentagon's initial same-core scalar edge");
    println!("  until that map is defined on the full rank-eight Q fiber, d_occ G_D = Gamma_D G_D d_occ is not a typed test");
}
