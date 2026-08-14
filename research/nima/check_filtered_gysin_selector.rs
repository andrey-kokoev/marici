//! Exact selector audit for the eight nontransverse octagon pentagons.
//!
//! There are three different questions which must not be conflated.
//!
//! 1. A support-compatible cellular map from an oriented pentagon disk to a
//!    square disk has 20 representatives of each relative degree.
//! 2. If the target square is additionally labelled by the Boolean core word
//!    empty,D,DE,E, the core-rank filtration and normal orientation select the
//!    quotient which contracts the unique rank-zero edge.
//! 3. That Boolean labelling is not presently part of the target occurrence
//!    facet.  Moreover, pushforward of the established extension-by-zero
//!    coefficient cosheaf through the contraction has rank six at the
//!    contracted vertex, whereas a route-square vertex has rank five.  The
//!    missing rank-one relation is the exchanged-label Cousin lower term.
//!
//! Thus the filtered contraction is a canonical bare carrier representative,
//! not yet the loaded physical Gysin map.  The nonvanishing physical-edge
//! constraint first leaves four cyclic origins per normal orientation.  The
//! weaker derived statement is intrinsic already: these representatives are
//! chain homotopic as maps of pairs and carry the same decomposable weighted
//! nine-cell facet fundamental class.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

const N: usize = 8;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge(usize, usize);

type Cell = Vec<usize>;
type Triangulation = Vec<Edge>;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
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
}

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Occurrence(Vec<(Cell, Edge)>);

#[derive(Clone, Debug, Eq, PartialEq)]
struct Lift {
    vertices: Vec<usize>,
    degree: i64,
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

fn scalar_sheet(triangulation: &Triangulation) -> usize {
    assert!(core(triangulation).is_empty());
    let parities: BTreeSet<_> = triangulation
        .iter()
        .map(|diagonal| diagonal.0 % 2)
        .collect();
    assert_eq!(parities.len(), 1);
    *parities.iter().next().unwrap()
}

fn two_faces(tris: &[Triangulation]) -> Vec<(Vec<Edge>, Vec<usize>)> {
    let diagonals = polygon_diagonals();
    let mut result = Vec::new();
    for first in 0..diagonals.len() {
        for second in first + 1..diagonals.len() {
            for third in second + 1..diagonals.len() {
                let common = vec![diagonals[first], diagonals[second], diagonals[third]];
                if crossing(common[0], common[1])
                    || crossing(common[0], common[2])
                    || crossing(common[1], common[2])
                {
                    continue;
                }
                let vertices: Vec<_> = tris
                    .iter()
                    .enumerate()
                    .filter(|(_, triangulation)| {
                        common
                            .iter()
                            .all(|diagonal| triangulation.contains(diagonal))
                    })
                    .map(|(index, _)| index)
                    .collect();
                assert!(vertices.len() == 4 || vertices.len() == 5);
                result.push((common, vertices));
            }
        }
    }
    result.sort();
    result.dedup();
    result
}

fn cyclic_order(vertices: &[usize], tris: &[Triangulation]) -> Vec<usize> {
    let mut result = vec![vertices[0]];
    let second = vertices
        .iter()
        .copied()
        .filter(|&candidate| {
            candidate != vertices[0] && adjacent(&tris[vertices[0]], &tris[candidate])
        })
        .min()
        .unwrap();
    result.push(second);
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

fn route_faces(tris: &[Triangulation]) -> Vec<RouteFace> {
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
        result.push(RouteFace {
            vertices: cyclic_order(&vertices, tris),
            common,
            core: [current[0], current[1]],
            sheet: *sheets.iter().next().unwrap(),
            kind: if vertices.len() == 4 {
                FaceKind::Square
            } else {
                FaceKind::Pentagon
            },
        });
    }
    result.sort_by_key(|face| (face.core, face.sheet, face.kind));
    result
}

fn dihedral_orders(vertices: &[usize]) -> Vec<Vec<usize>> {
    let mut result = Vec::new();
    for reflected in [false, true] {
        let base: Vec<_> = if reflected {
            vertices.iter().copied().rev().collect()
        } else {
            vertices.to_vec()
        };
        for rotation in 0..vertices.len() {
            result.push(
                (0..vertices.len())
                    .map(|index| base[(index + rotation) % vertices.len()])
                    .collect(),
            );
        }
    }
    result.sort();
    result.dedup();
    result
}

fn wanted_core_word(current: [Edge; 2], kind: FaceKind) -> Vec<Vec<Edge>> {
    let d = current[0];
    let e = current[1];
    match kind {
        FaceKind::Pentagon => vec![vec![], vec![], vec![d], vec![d, e], vec![e]],
        FaceKind::Square => vec![vec![], vec![d], vec![d, e], vec![e]],
    }
}

fn normalized_vertices(face: &RouteFace, tris: &[Triangulation]) -> Vec<usize> {
    let wanted = wanted_core_word(face.core, face.kind);
    let candidates: Vec<_> = dihedral_orders(&face.vertices)
        .into_iter()
        .filter(|order| {
            order
                .iter()
                .map(|&index| core(&tris[index]))
                .collect::<Vec<_>>()
                == wanted
        })
        .collect();
    assert_eq!(candidates.len(), 1);
    candidates[0].clone()
}

fn intersection(first: &Triangulation, second: &Triangulation) -> Vec<Edge> {
    first
        .iter()
        .copied()
        .filter(|diagonal| second.contains(diagonal))
        .collect()
}

fn facet_labels(face: &RouteFace, normalized: &[usize], tris: &[Triangulation]) -> Vec<Edge> {
    let mut result = Vec::new();
    for index in 0..normalized.len() {
        let shared = intersection(
            &tris[normalized[index]],
            &tris[normalized[(index + 1) % normalized.len()]],
        );
        let extras: Vec<_> = shared
            .into_iter()
            .filter(|diagonal| !face.common.contains(diagonal))
            .collect();
        assert_eq!(extras.len(), 1);
        result.push(extras[0]);
    }
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
    regions
}

fn cell_slots(cell: &Cell) -> [Edge; 2] {
    assert_eq!(cell.len(), 4);
    let mut result = [edge(cell[0], cell[2]), edge(cell[1], cell[3])];
    result.sort();
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

fn forest_sinks(cells: &[Cell], directions: &BTreeMap<Edge, (Cell, Cell)>) -> Vec<Cell> {
    let indices: BTreeMap<_, _> = cells
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, cell)| (cell, index))
        .collect();
    let mut adjacency = vec![Vec::new(); cells.len()];
    let mut outgoing = vec![false; cells.len()];
    for (source, target) in directions.values() {
        let source_index = indices[source];
        let target_index = indices[target];
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

fn occurrence_from_mask(current: [Edge; 2], mask: usize) -> Occurrence {
    let cells = core_regions(&current);
    let mut marks = Vec::new();
    for (coordinate, cell) in cells.iter().enumerate() {
        marks.push((cell.clone(), cell_slots(cell)[(mask >> coordinate) & 1]));
    }
    marks.sort();
    Occurrence(marks)
}

fn full_tensor(current: [Edge; 2]) -> BTreeMap<Occurrence, Vec<Edge>> {
    (0..8)
        .map(|mask| {
            let occurrence = occurrence_from_mask(current, mask);
            let mut monomial: Vec<_> = occurrence.0.iter().map(|(_, mark)| *mark).collect();
            monomial.sort();
            (occurrence, monomial)
        })
        .collect()
}

fn chart_terms(face: &RouteFace, plus: bool) -> (BTreeMap<Occurrence, Vec<Edge>>, (usize, usize)) {
    let cells = core_regions(&face.core);
    let directions = directed_edges(face.core, plus);
    let sinks = forest_sinks(&cells, &directions);
    assert_eq!(sinks.len(), 1);
    let sink = &sinks[0];
    let marks: Vec<_> = cell_slots(sink)
        .into_iter()
        .filter(|mark| face.common.contains(mark))
        .collect();
    assert_eq!(marks.len(), 1);
    let coordinate = cells.iter().position(|cell| cell == sink).unwrap();
    let value = cell_slots(sink)
        .iter()
        .position(|candidate| *candidate == marks[0])
        .unwrap();
    let full = full_tensor(face.core);
    let restricted = full
        .into_iter()
        .filter(|(occurrence, _)| {
            occurrence
                .0
                .iter()
                .find(|(cell, _)| cell == sink)
                .map(|(_, mark)| *mark == marks[0])
                .unwrap()
        })
        .collect::<BTreeMap<_, _>>();
    assert_eq!(restricted.len(), 4);
    (restricted, (coordinate, value))
}

fn rotate_edge(value: Edge) -> Edge {
    edge((value.0 + 1) % N, (value.1 + 1) % N)
}

fn rotate_triangulation(value: &Triangulation) -> Triangulation {
    let mut result: Vec<_> = value.iter().copied().map(rotate_edge).collect();
    result.sort();
    result
}

fn rotate_cell(cell: &Cell) -> Cell {
    let mut result: Vec<_> = cell.iter().map(|vertex| (vertex + 1) % N).collect();
    result.sort_unstable();
    result
}

fn rotate_occurrence(value: &Occurrence) -> Occurrence {
    let mut marks: Vec<_> = value
        .0
        .iter()
        .map(|(cell, mark)| (rotate_cell(cell), rotate_edge(*mark)))
        .collect();
    marks.sort();
    Occurrence(marks)
}

fn rotate_chart(chart: &BTreeMap<Occurrence, Vec<Edge>>) -> BTreeMap<Occurrence, Vec<Edge>> {
    chart
        .iter()
        .map(|(occurrence, monomial)| {
            let mut rotated_monomial: Vec<_> = monomial.iter().copied().map(rotate_edge).collect();
            rotated_monomial.sort();
            (rotate_occurrence(occurrence), rotated_monomial)
        })
        .collect()
}

fn occurrence_mask(current: [Edge; 2], occurrence: &Occurrence) -> usize {
    let cells = core_regions(&current);
    let mut result = 0;
    for (coordinate, cell) in cells.iter().enumerate() {
        let mark = occurrence
            .0
            .iter()
            .find(|(marked_cell, _)| marked_cell == cell)
            .map(|(_, mark)| *mark)
            .unwrap();
        let slot = cell_slots(cell)
            .iter()
            .position(|candidate| *candidate == mark)
            .unwrap();
        result |= slot << coordinate;
    }
    result
}

fn chart_cycle(current: [Edge; 2], chart: &BTreeMap<Occurrence, Vec<Edge>>) -> Vec<Occurrence> {
    let by_mask: BTreeMap<_, _> = chart
        .keys()
        .cloned()
        .map(|occurrence| (occurrence_mask(current, &occurrence), occurrence))
        .collect();
    assert_eq!(by_mask.len(), 4);
    let start = *by_mask.keys().next().unwrap();
    let second = *by_mask
        .keys()
        .filter(|&&mask| (mask ^ start).count_ones() == 1)
        .next()
        .unwrap();
    let mut masks = vec![start, second];
    while masks.len() < 4 {
        let previous = masks[masks.len() - 2];
        let current_mask = masks[masks.len() - 1];
        let next = *by_mask
            .keys()
            .find(|&&mask| {
                mask != previous
                    && !masks.contains(&mask)
                    && (mask ^ current_mask).count_ones() == 1
            })
            .unwrap();
        masks.push(next);
    }
    assert_eq!((masks[3] ^ masks[0]).count_ones(), 1);
    masks
        .into_iter()
        .map(|mask| by_mask[&mask].clone())
        .collect()
}

fn enumerate_lifts(vertex_count: usize) -> Vec<Lift> {
    let mut result = Vec::new();
    for code in 0..4_usize.pow(vertex_count as u32) {
        let mut work = code;
        let mut vertices = Vec::new();
        for _ in 0..vertex_count {
            vertices.push(work % 4);
            work /= 4;
        }
        if vertices.iter().copied().collect::<BTreeSet<_>>().len() != 4 {
            continue;
        }
        let mut signed_steps = 0_i64;
        let mut cellular = true;
        for index in 0..vertex_count {
            let first = vertices[index];
            let second = vertices[(index + 1) % vertex_count];
            match (second + 4 - first) % 4 {
                0 => {}
                1 => signed_steps += 1,
                3 => signed_steps -= 1,
                2 => {
                    cellular = false;
                    break;
                }
                _ => unreachable!(),
            }
        }
        if cellular {
            assert_eq!(signed_steps % 4, 0);
            let degree = signed_steps / 4;
            assert!(degree == 1 || degree == -1);
            result.push(Lift { vertices, degree });
        }
    }
    result.sort_by_key(|lift| (lift.degree, lift.vertices.clone()));
    result
}

fn target_edge_chain(first: usize, second: usize) -> [i64; 4] {
    let mut result = [0; 4];
    match (second + 4 - first) % 4 {
        0 => {}
        1 => result[first] = 1,
        3 => result[second] = -1,
        _ => panic!("noncellular edge"),
    }
    result
}

fn forward_path(first: usize, second: usize) -> [i64; 4] {
    let mut result = [0; 4];
    let mut current = first;
    while current != second {
        result[current] += 1;
        current = (current + 1) % 4;
    }
    result
}

fn subtract(first: [i64; 4], second: [i64; 4]) -> [i64; 4] {
    std::array::from_fn(|index| first[index] - second[index])
}

fn add_scaled(mut value: [i64; 4], cycle_coefficient: i64) -> [i64; 4] {
    for entry in &mut value {
        *entry += cycle_coefficient;
    }
    value
}

/// Verify a chain homotopy of boundary circles.  The homotopy sends source
/// vertices to target one-chains and stays inside the target boundary.  Equal
/// degrees are exactly the closure condition.  Since the two disk 2-cells
/// have the same coefficient, this extends to a chain homotopy of pairs.
fn pair_chain_homotopic(first: &Lift, second: &Lift) -> bool {
    if first.degree != second.degree || first.vertices.len() != second.vertices.len() {
        return false;
    }
    let count = first.vertices.len();
    let base: Vec<_> = (0..count)
        .map(|index| forward_path(second.vertices[index], first.vertices[index]))
        .collect();
    let mut winding = vec![0_i64; count + 1];
    for index in 0..count {
        let following = (index + 1) % count;
        let delta = subtract(
            target_edge_chain(first.vertices[index], first.vertices[following]),
            target_edge_chain(second.vertices[index], second.vertices[following]),
        );
        let base_difference = subtract(base[following], base[index]);
        let residual = subtract(delta, base_difference);
        if !residual.iter().all(|entry| *entry == residual[0]) {
            return false;
        }
        winding[index + 1] = winding[index] + residual[0];
    }
    if winding[count] != 0 {
        return false;
    }
    for index in 0..count {
        let following = (index + 1) % count;
        let h_current = add_scaled(base[index], winding[index]);
        let h_following = add_scaled(base[following], winding[following]);
        let right = subtract(h_following, h_current);
        let left = subtract(
            target_edge_chain(first.vertices[index], first.vertices[following]),
            target_edge_chain(second.vertices[index], second.vertices[following]),
        );
        if left != right {
            return false;
        }
    }
    true
}

fn symmetric_difference(first: usize, second: usize) -> usize {
    first ^ second
}

fn collapsed_edge(lift: &Lift) -> usize {
    let collapsed: Vec<_> = (0..lift.vertices.len())
        .filter(|&index| lift.vertices[index] == lift.vertices[(index + 1) % lift.vertices.len()])
        .collect();
    assert_eq!(collapsed.len(), 1);
    collapsed[0]
}

fn facet_cell_support(lift: &Lift) -> [usize; 3] {
    let vertices: BTreeSet<_> = lift.vertices.iter().copied().collect();
    let edges: BTreeSet<_> = (0..lift.vertices.len())
        .filter_map(|index| {
            let first = lift.vertices[index];
            let second = lift.vertices[(index + 1) % lift.vertices.len()];
            (first != second).then_some(if (second + 4 - first) % 4 == 1 {
                first
            } else {
                second
            })
        })
        .collect();
    [vertices.len(), edges.len(), usize::from(lift.degree != 0)]
}

fn main() {
    let tris = triangulations();
    assert_eq!(tris.len(), 132);
    let faces = route_faces(&tris);
    assert_eq!(faces.len(), 24);

    let mut grouped = BTreeMap::<[Edge; 2], Vec<&RouteFace>>::new();
    for face in &faces {
        grouped.entry(face.core).or_default().push(face);
    }
    assert_eq!(grouped.len(), 12);
    let four_chart_groups: BTreeMap<_, _> = grouped
        .into_iter()
        .filter(|(_, group)| group.iter().any(|face| face.kind == FaceKind::Pentagon))
        .collect();
    assert_eq!(four_chart_groups.len(), 8);

    let lifts = enumerate_lifts(5);
    assert_eq!(lifts.len(), 40);
    assert_eq!(lifts.iter().filter(|lift| lift.degree == 1).count(), 20);
    assert_eq!(lifts.iter().filter(|lift| lift.degree == -1).count(), 20);
    let collapse_profile: BTreeMap<_, _> = (0..5)
        .map(|edge_index| {
            (
                edge_index,
                lifts
                    .iter()
                    .filter(|lift| collapsed_edge(lift) == edge_index)
                    .count(),
            )
        })
        .collect();
    assert_eq!(collapse_profile, (0..5).map(|index| (index, 8)).collect());
    assert!(lifts
        .iter()
        .all(|lift| facet_cell_support(lift) == [4, 4, 1]));

    // A realization of the already nonzero physical coaction cannot collapse
    // a core-changing edge.  The unique same-core edge is edge zero, so this
    // necessary support constraint leaves four cyclic target origins in each
    // normal orientation.
    let physical_support_compatible: Vec<_> = lifts
        .iter()
        .filter(|lift| collapsed_edge(lift) == 0)
        .collect();
    assert_eq!(physical_support_compatible.len(), 8);
    assert_eq!(
        physical_support_compatible
            .iter()
            .filter(|lift| lift.degree == 1)
            .count(),
        4
    );
    assert_eq!(
        physical_support_compatible
            .iter()
            .filter(|lift| lift.degree == -1)
            .count(),
        4
    );

    // The proposed Boolean target labels are 0,D,DE,E.  Rank compatibility
    // leaves the two orientations; the ordered exact-core word leaves one.
    let source_ranks = [0, 0, 1, 2, 1];
    let target_ranks = [0, 1, 2, 1];
    let rank_filtered: Vec<_> = lifts
        .iter()
        .filter(|lift| {
            lift.vertices
                .iter()
                .enumerate()
                .all(|(index, &target)| source_ranks[index] == target_ranks[target])
        })
        .collect();
    assert_eq!(rank_filtered.len(), 2);
    assert_eq!(
        rank_filtered
            .iter()
            .map(|lift| lift.degree)
            .collect::<BTreeSet<_>>(),
        BTreeSet::from([-1, 1])
    );
    let oriented_rank_filtered: Vec<_> = rank_filtered
        .iter()
        .copied()
        .filter(|lift| lift.degree == 1)
        .collect();
    assert_eq!(oriented_rank_filtered.len(), 1);

    // Bit labels: 0=empty, 1=D, 3=DE, 2=E.
    let source_core_word = [0_usize, 0, 1, 3, 2];
    let target_core_word = [0_usize, 1, 3, 2];
    let exact_core_filtered: Vec<_> = lifts
        .iter()
        .filter(|lift| {
            lift.vertices
                .iter()
                .enumerate()
                .all(|(index, &target)| source_core_word[index] == target_core_word[target])
        })
        .collect();
    assert_eq!(exact_core_filtered.len(), 1);
    assert_eq!(exact_core_filtered[0].degree, 1);
    assert_eq!(exact_core_filtered[0].vertices, vec![0, 0, 1, 2, 3]);

    // Requiring the four already-labelled physical toggles to map to their
    // namesake Boolean edges leaves four choices of Boolean origin.  Anchoring
    // the rank-two vertex at DE gives the same singleton as the exact-core
    // word.  Both are conditional counts: the physical coaction is typed on
    // occurrence modules, but its realization as a route-edge cellular map
    // and a Boolean origin on the occurrence facet are precisely what is open.
    let toggles = [0_usize, 1, 2, 1, 2];
    let physical_edge_filtered: Vec<_> = lifts
        .iter()
        .filter(|lift| {
            (1..5).all(|index| {
                let first = target_core_word[lift.vertices[index]];
                let second = target_core_word[lift.vertices[(index + 1) % 5]];
                symmetric_difference(first, second) == toggles[index]
            })
        })
        .collect();
    assert_eq!(physical_edge_filtered.len(), 4);
    assert!(physical_edge_filtered
        .iter()
        .all(|lift| collapsed_edge(lift) == 0));
    assert_eq!(
        physical_edge_filtered
            .iter()
            .filter(|lift| lift.degree == 1)
            .count(),
        2
    );
    assert_eq!(
        physical_edge_filtered
            .iter()
            .filter(|lift| lift.degree == -1)
            .count(),
        2
    );
    let anchored_physical_edge_filtered: Vec<_> = physical_edge_filtered
        .into_iter()
        .filter(|lift| lift.vertices[3] == 2)
        .collect();
    assert_eq!(anchored_physical_edge_filtered.len(), 1);
    let oriented_anchored: Vec<_> = anchored_physical_edge_filtered
        .into_iter()
        .filter(|lift| lift.degree == 1)
        .collect();
    assert_eq!(oriented_anchored.len(), 1);
    assert_eq!(oriented_anchored[0], exact_core_filtered[0]);

    // All fixed-degree representatives define one relative cellular
    // homotopy class.  The two degrees are distinguished on H_2(D^2,S^1).
    let mut homotopy_checks = 0;
    for degree in [-1, 1] {
        let family: Vec<_> = lifts.iter().filter(|lift| lift.degree == degree).collect();
        for first in &family {
            for second in &family {
                assert!(pair_chain_homotopic(first, second));
                homotopy_checks += 1;
            }
        }
    }
    assert_eq!(homotopy_checks, 2 * 20 * 20);
    assert!(!pair_chain_homotopic(
        lifts.iter().find(|lift| lift.degree == 1).unwrap(),
        lifts.iter().find(|lift| lift.degree == -1).unwrap()
    ));

    let tri_index: BTreeMap<_, _> = tris
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, triangulation)| (triangulation, index))
        .collect();
    let face_index: BTreeMap<_, _> = faces
        .iter()
        .enumerate()
        .map(|(index, face)| {
            let mut vertices = face.vertices.clone();
            vertices.sort_unstable();
            ((face.kind, vertices), index)
        })
        .collect();

    let mut scalar_edge_checks = 0;
    let mut coefficient_pushout_checks = 0;
    let mut weighted_restriction_checks = 0;
    let mut deck_chart_checks = 0;
    let mut representative_quotients = BTreeSet::new();

    for (current, group) in &four_chart_groups {
        assert_eq!(group.len(), 2);
        let pentagon = *group
            .iter()
            .find(|face| face.kind == FaceKind::Pentagon)
            .unwrap();
        let square = *group
            .iter()
            .find(|face| face.kind == FaceKind::Square)
            .unwrap();
        let p_order = normalized_vertices(pentagon, &tris);
        let s_order = normalized_vertices(square, &tris);
        assert_eq!(
            p_order
                .iter()
                .map(|&index| core(&tris[index]).len())
                .collect::<Vec<_>>(),
            vec![0, 0, 1, 2, 1]
        );
        assert_eq!(
            s_order
                .iter()
                .map(|&index| core(&tris[index]).len())
                .collect::<Vec<_>>(),
            vec![0, 1, 2, 1]
        );

        let same_core_edges: Vec<_> = (0..5)
            .filter(|&index| core(&tris[p_order[index]]) == core(&tris[p_order[(index + 1) % 5]]))
            .collect();
        assert_eq!(same_core_edges, vec![0]);
        for index in 1..5 {
            let first: BTreeSet<_> = core(&tris[p_order[index]]).into_iter().collect();
            let second: BTreeSet<_> = core(&tris[p_order[(index + 1) % 5]]).into_iter().collect();
            assert_eq!(first.symmetric_difference(&second).count(), 1);
        }
        scalar_edge_checks += 5;

        // On the scalar edge the stalk diagram is Z^5 <- Z^4 -> Z^5.
        // Its cosheaf pushout has rank 5+5-4=6.  The two outer facet labels
        // are distinct extension-by-zero lines, so reaching a rank-five
        // square stalk requires one new lower-face relation.
        let labels = facet_labels(pentagon, &p_order, &tris);
        assert_eq!(labels.len(), 5);
        let edge_labels: BTreeSet<_> = pentagon.common.iter().copied().chain([labels[0]]).collect();
        let left_labels: BTreeSet<_> = edge_labels.iter().copied().chain([labels[4]]).collect();
        let right_labels: BTreeSet<_> = edge_labels.iter().copied().chain([labels[1]]).collect();
        let pushout_labels: BTreeSet<_> = left_labels.union(&right_labels).copied().collect();
        assert_eq!(edge_labels.len(), 4);
        assert_eq!(left_labels.len(), 5);
        assert_eq!(right_labels.len(), 5);
        assert_eq!(left_labels.intersection(&right_labels).count(), 4);
        assert_eq!(pushout_labels.len(), 6);
        assert_ne!(labels[4], labels[1]);
        assert!(!edge_labels.contains(&labels[4]));
        assert!(!edge_labels.contains(&labels[1]));
        coefficient_pushout_checks += 1;

        // Each of P+,P-,S+,S- is a weighted restriction of one decomposable
        // rank-eight tensor.  Hence the canonical data see the oriented
        // facet class, not a choice of its polygonal parametrization.
        let full = full_tensor(*current);
        assert_eq!(full.len(), 8);
        let mut facets = BTreeSet::new();
        for face in [pentagon, square] {
            for plus in [true, false] {
                let (chart, facet) = chart_terms(face, plus);
                assert_eq!(chart.len(), 4);
                assert!(chart
                    .iter()
                    .all(|(occurrence, monomial)| full.get(occurrence) == Some(monomial)));
                facets.insert(facet);
                weighted_restriction_checks += chart.len();

                let rotated_vertices = {
                    let mut value: Vec<_> = face
                        .vertices
                        .iter()
                        .map(|&index| tri_index[&rotate_triangulation(&tris[index])])
                        .collect();
                    value.sort_unstable();
                    value
                };
                let next_face = &faces[face_index[&(face.kind, rotated_vertices)]];
                let (next_chart, _) = chart_terms(next_face, !plus);
                assert_eq!(rotate_chart(&chart), next_chart);
                deck_chart_checks += 1;
            }
        }
        assert_eq!(facets.len(), 4);
        let missing: Vec<_> = (0..3)
            .flat_map(|coordinate| (0..2).map(move |value| (coordinate, value)))
            .filter(|facet| !facets.contains(facet))
            .collect();
        assert_eq!(missing.len(), 2);
        assert_eq!(missing[0].0, missing[1].0);

        representative_quotients.insert((
            current,
            exact_core_filtered[0].vertices.clone(),
            labels[4],
            labels[1],
        ));
    }

    assert_eq!(scalar_edge_checks, 8 * 5);
    assert_eq!(coefficient_pushout_checks, 8);
    assert_eq!(weighted_restriction_checks, 8 * 4 * 4);
    assert_eq!(deck_chart_checks, 8 * 4);
    assert_eq!(representative_quotients.len(), 8);

    // Deck covariance does not choose one of the four cyclic origins.  Any
    // of the four physical-support-compatible, degree +1 maps propagates
    // around the actual occurrence bases and closes after eight rotations.
    let representative_group = four_chart_groups.values().next().unwrap();
    let representative_pentagon = *representative_group
        .iter()
        .find(|face| face.kind == FaceKind::Pentagon)
        .unwrap();
    let source_cycle = normalized_vertices(representative_pentagon, &tris);
    let (representative_chart, _) = chart_terms(representative_pentagon, true);
    let target_cycle = chart_cycle(representative_pentagon.core, &representative_chart);
    let origin_lifts: Vec<_> = physical_support_compatible
        .iter()
        .copied()
        .filter(|lift| lift.degree == 1)
        .collect();
    assert_eq!(origin_lifts.len(), 4);
    let mut deck_origin_checks = 0;
    for lift in origin_lifts {
        let initial: BTreeMap<_, _> = source_cycle
            .iter()
            .copied()
            .enumerate()
            .map(|(index, source)| (source, target_cycle[lift.vertices[index]].clone()))
            .collect();
        let mut transported = initial.clone();
        for _ in 0..8 {
            transported = transported
                .into_iter()
                .map(|(source, target)| {
                    (
                        tri_index[&rotate_triangulation(&tris[source])],
                        rotate_occurrence(&target),
                    )
                })
                .collect();
        }
        assert_eq!(transported, initial);
        deck_origin_checks += 1;
    }
    assert_eq!(deck_origin_checks, 4);

    // The eight pentagons form one deck orbit.  Rotation preserves the
    // unique minimal-rank edge and rotates its two exchanged quotient labels.
    let pentagons: Vec<_> = four_chart_groups
        .values()
        .map(|group| {
            *group
                .iter()
                .find(|face| face.kind == FaceKind::Pentagon)
                .unwrap()
        })
        .collect();
    let pentagon_lookup: BTreeMap<_, _> = pentagons
        .iter()
        .enumerate()
        .map(|(index, face)| {
            let mut vertices = face.vertices.clone();
            vertices.sort_unstable();
            (vertices, index)
        })
        .collect();
    let mut orbit = Vec::new();
    let mut current_index = 0;
    for _ in 0..8 {
        assert!(!orbit.contains(&current_index));
        orbit.push(current_index);
        let face = pentagons[current_index];
        let mut rotated_vertices: Vec<_> = face
            .vertices
            .iter()
            .map(|&index| tri_index[&rotate_triangulation(&tris[index])])
            .collect();
        rotated_vertices.sort_unstable();
        current_index = pentagon_lookup[&rotated_vertices];
    }
    assert_eq!(current_index, 0);
    assert_eq!(orbit.len(), 8);

    println!("filtered Gysin-selector certificate");
    println!("  route faces: 24; nontransverse pentagon/square cores: 8 in one deck orbit");
    println!("  raw cellular pentagon lifts: 40 = 20 degree +1 + 20 degree -1");
    println!("  nonzero support on all 4 physical edges leaves 4 cyclic origins per orientation");
    println!("  every lift uses the complete target facet complex: cells (4,4,1), not a constant rank-8 stalk");
    println!("  target Boolean rank labels reduce 40 -> 2; normal orientation reduces 2 -> 1");
    println!("  exact core/toggle labels give the same quotient map [0,0,1,2,3]");
    println!("  the contraction is derived, not assumed: every pentagon has one rank-zero edge and four physical edges");
    println!("  coefficient pushforward at the contracted edge: rank 5 + rank 5 - rank 4 = rank 6");
    println!(
        "  desired route-square vertex rank: 5; missing Cousin relation rank: 1 on all 8 cores"
    );
    println!("  weighted chart restrictions checked: {weighted_restriction_checks}; deck checks: {deck_chart_checks}");
    println!("  four cyclic origins each close on the eight-step deck orbit: {deck_origin_checks} checks");
    println!("  all 20 lifts of either fixed degree are pair-chain-homotopic: {homotopy_checks} ordered checks");
    println!();
    println!("VERDICT: CONDITIONAL STRICT SELECTOR / PROVED DERIVED CLASS");
    println!("  physical edge support, normal orientation, deck covariance, and factorized weights leave 4 strict origins");
    println!("  they represent one relative fundamental class for the selected normal orientation");
    println!("  a Boolean-labelled Rees/core-rank cofiber selects the scalar-edge contraction uniquely as a bare carrier");
    println!("  it is not yet the loaded Gysin map: the extension-by-zero pushforward has one excess quotient line");
    println!("  minimal missing datum: a loaded Cousin counit relating the two exchanged endpoint labels");
}
