//! Rust stress test for mixed scalar-refinement / physical-cut naturality.
//!
//! The readable specification is check_mixed_prism_spectator_stability.py.
//! This executable independently regenerates the local K_2 x I carriers
//! without enumerating the ambient associahedron, checks every common
//! component mark, reconstructs both upper slot edges, and compares the
//! complete atlas under one-step deck rotation.
//!
//! The n=10 and n=12 counts are regression oracles from the Python audit.
//! The n=14 run is the first higher-arity spectator test.

use std::collections::{BTreeMap, BTreeSet, HashMap, HashSet, VecDeque};

const MAX_N: usize = 14;
const NONE: i16 = -1;
type Mask = u128;
type Cell = [u8; 4];
type Marks = Vec<(Cell, usize)>;

#[derive(Clone)]
struct Geometry {
    n: usize,
    diagonal_index: [[i16; MAX_N]; MAX_N],
    diagonals: Vec<(usize, usize)>,
    physical_mask: Mask,
    rotation: Vec<usize>,
}

impl Geometry {
    fn new(n: usize) -> Self {
        assert!(n >= 4 && n <= MAX_N && n % 2 == 0);
        let mut diagonal_index = [[NONE; MAX_N]; MAX_N];
        let mut diagonals = Vec::new();
        for first in 0..n {
            for second in (first + 1)..n {
                if !is_boundary_pair(first, second, n) {
                    let index = diagonals.len();
                    assert!(index < 128);
                    diagonals.push((first, second));
                    diagonal_index[first][second] = index as i16;
                    diagonal_index[second][first] = index as i16;
                }
            }
        }
        assert_eq!(diagonals.len(), n * (n - 3) / 2);
        let mut physical_mask = 0;
        for (index, (first, second)) in diagonals.iter().enumerate() {
            if (first + second) % 2 == 1 {
                physical_mask |= bit(index);
            }
        }
        let rotation = diagonals
            .iter()
            .map(|(first, second)| {
                let a = (first + 1) % n;
                let b = (second + 1) % n;
                let (a, b) = canonical_pair(a, b);
                let index = diagonal_index[a][b];
                assert!(index >= 0);
                index as usize
            })
            .collect();
        Self {
            n,
            diagonal_index,
            diagonals,
            physical_mask,
            rotation,
        }
    }

    fn diagonal_id(&self, first: usize, second: usize) -> usize {
        let (first, second) = canonical_pair(first, second);
        let index = self.diagonal_index[first][second];
        assert!(
            index >= 0,
            "requested boundary ({first},{second}) at n={}",
            self.n
        );
        index as usize
    }

    fn optional_diagonal_id(&self, first: usize, second: usize) -> Option<usize> {
        let (first, second) = canonical_pair(first, second);
        let index = self.diagonal_index[first][second];
        (index >= 0).then_some(index as usize)
    }

    fn is_physical(&self, diagonal: usize) -> bool {
        self.physical_mask & bit(diagonal) != 0
    }
}

fn bit(index: usize) -> Mask {
    1_u128 << index
}

fn canonical_pair(first: usize, second: usize) -> (usize, usize) {
    if first < second {
        (first, second)
    } else {
        (second, first)
    }
}

fn is_boundary_pair(first: usize, second: usize, n: usize) -> bool {
    let difference = first.abs_diff(second);
    difference == 1 || difference == n - 1
}

fn mask_indices(mut mask: Mask) -> Vec<usize> {
    let mut result = Vec::new();
    while mask != 0 {
        let index = mask.trailing_zeros() as usize;
        result.push(index);
        mask &= mask - 1;
    }
    result
}

fn rotate_mask(mask: Mask, geometry: &Geometry) -> Mask {
    mask_indices(mask)
        .into_iter()
        .fold(0, |result, index| result | bit(geometry.rotation[index]))
}

fn rotate_cell(cell: Cell, geometry: &Geometry) -> Cell {
    let mut result = cell.map(|vertex| ((vertex as usize + 1) % geometry.n) as u8);
    result.sort_unstable();
    result
}

fn catalan(index: usize) -> usize {
    let mut numerator = 1_u128;
    let mut denominator = 1_u128;
    for value in 1..=index {
        numerator *= (index + value) as u128;
        denominator *= value as u128;
    }
    (numerator / denominator / (index + 1) as u128) as usize
}

fn triangulations_vertices(
    vertices: &[usize],
    geometry: &Geometry,
    memo: &mut HashMap<Vec<usize>, Vec<Mask>>,
) -> Vec<Mask> {
    if let Some(value) = memo.get(vertices) {
        return value.clone();
    }
    if vertices.len() <= 3 {
        return vec![0];
    }
    let mut result = Vec::new();
    for split in 1..(vertices.len() - 1) {
        let left = triangulations_vertices(&vertices[..=split], geometry, memo);
        let right = triangulations_vertices(&vertices[split..], geometry, memo);
        for left_mask in &left {
            for right_mask in &right {
                let mut mask = left_mask | right_mask;
                if split > 1 {
                    mask |= bit(geometry.diagonal_id(vertices[0], vertices[split]));
                }
                if split < vertices.len() - 2 {
                    mask |=
                        bit(geometry.diagonal_id(vertices[split], vertices[vertices.len() - 1]));
                }
                result.push(mask);
            }
        }
    }
    result.sort_unstable();
    result.dedup();
    memo.insert(vertices.to_vec(), result.clone());
    result
}

fn zero_core_sources(geometry: &Geometry) -> Vec<Mask> {
    let half = geometry.n / 2;
    let mut result = BTreeSet::new();
    let mut memo = HashMap::new();
    for parity in [0_usize, 1_usize] {
        let vertices: Vec<_> = (parity..geometry.n).step_by(2).collect();
        assert_eq!(vertices.len(), half);
        let mut boundary = 0;
        for index in 0..half {
            boundary |= bit(geometry.diagonal_id(vertices[index], vertices[(index + 1) % half]));
        }
        for triangulation in triangulations_vertices(&vertices, geometry, &mut memo) {
            let source = triangulation | boundary;
            assert_eq!(source.count_ones() as usize, geometry.n - 3);
            assert_eq!(source & geometry.physical_mask, 0);
            result.insert(source);
        }
    }
    assert_eq!(result.len(), 2 * catalan(half - 2));
    result.into_iter().collect()
}

fn edge_present(first: usize, second: usize, triangulation: Mask, geometry: &Geometry) -> bool {
    if is_boundary_pair(first, second, geometry.n) {
        return true;
    }
    geometry
        .optional_diagonal_id(first, second)
        .is_some_and(|index| triangulation & bit(index) != 0)
}

fn flip_diagonal(triangulation: Mask, diagonal: usize, geometry: &Geometry) -> (Mask, usize) {
    assert!(triangulation & bit(diagonal) != 0);
    let (first, second) = geometry.diagonals[diagonal];
    let opposite: Vec<_> = (0..geometry.n)
        .filter(|vertex| {
            *vertex != first
                && *vertex != second
                && edge_present(first, *vertex, triangulation, geometry)
                && edge_present(second, *vertex, triangulation, geometry)
        })
        .collect();
    assert_eq!(opposite.len(), 2);
    let replacement = geometry.diagonal_id(opposite[0], opposite[1]);
    assert_eq!(triangulation & bit(replacement), 0);
    (
        (triangulation & !bit(diagonal)) | bit(replacement),
        replacement,
    )
}

#[derive(Clone)]
struct ParityTriangle {
    vertices: [usize; 3],
    edges: [usize; 3],
}

fn parity_triangles(source: Mask, geometry: &Geometry) -> Vec<ParityTriangle> {
    let mut vertex_set = BTreeSet::new();
    for diagonal in mask_indices(source) {
        let (first, second) = geometry.diagonals[diagonal];
        vertex_set.insert(first);
        vertex_set.insert(second);
    }
    let vertices: Vec<_> = vertex_set.into_iter().collect();
    assert_eq!(vertices.len(), geometry.n / 2);
    assert!(vertices.iter().all(|vertex| vertex % 2 == vertices[0] % 2));

    let mut result = Vec::new();
    for first_index in 0..vertices.len() {
        for second_index in (first_index + 1)..vertices.len() {
            for third_index in (second_index + 1)..vertices.len() {
                let first = vertices[first_index];
                let second = vertices[second_index];
                let third = vertices[third_index];
                let edges = [
                    geometry.diagonal_id(first, second),
                    geometry.diagonal_id(second, third),
                    geometry.diagonal_id(first, third),
                ];
                if edges.iter().all(|edge| source & bit(*edge) != 0) {
                    result.push(ParityTriangle {
                        vertices: [first, second, third],
                        edges,
                    });
                }
            }
        }
    }
    assert_eq!(result.len(), geometry.n / 2 - 2);
    result
}

fn rooted_flip_chains(
    source: Mask,
    mark: usize,
    geometry: &Geometry,
    first_is_plus: bool,
) -> Vec<Vec<usize>> {
    let triangles = parity_triangles(source, geometry);
    let mut incidence = vec![Vec::<usize>::new(); geometry.diagonals.len()];
    for (triangle_index, triangle) in triangles.iter().enumerate() {
        for edge in triangle.edges {
            incidence[edge].push(triangle_index);
        }
    }
    assert!(!incidence[mark].is_empty());

    let mut parent_edge = vec![None; triangles.len()];
    let mut queue = VecDeque::new();
    for triangle in &incidence[mark] {
        parent_edge[*triangle] = Some(mark);
        queue.push_back(*triangle);
    }
    while let Some(triangle_index) = queue.pop_front() {
        let parent = parent_edge[triangle_index].unwrap();
        for edge in triangles[triangle_index].edges {
            if edge == parent {
                continue;
            }
            for neighbor in &incidence[edge] {
                if *neighbor != triangle_index && parent_edge[*neighbor].is_none() {
                    parent_edge[*neighbor] = Some(edge);
                    queue.push_back(*neighbor);
                }
            }
        }
    }
    assert!(parent_edge.iter().all(Option::is_some));

    let sheet_is_even = triangles[0].vertices[0] % 2 == 0;
    let choose_predecessor = first_is_plus == sheet_is_even;
    let mut selected = vec![0; triangles.len()];
    for (index, triangle) in triangles.iter().enumerate() {
        let parent = parent_edge[index].unwrap();
        let position = triangle
            .edges
            .iter()
            .position(|edge| *edge == parent)
            .unwrap();
        let selected_position = if choose_predecessor {
            (position + 2) % 3
        } else {
            (position + 1) % 3
        };
        selected[index] = triangle.edges[selected_position];
    }
    assert!(!selected.contains(&mark));
    let selected_set: HashSet<_> = selected.iter().copied().collect();
    assert_eq!(selected_set.len(), selected.len());

    let mut successor = HashMap::new();
    for (index, edge) in selected.iter().copied().enumerate() {
        let neighbors: Vec<_> = incidence[edge]
            .iter()
            .copied()
            .filter(|neighbor| *neighbor != index)
            .collect();
        if !neighbors.is_empty() {
            assert_eq!(neighbors.len(), 1);
            let child = neighbors[0];
            assert_eq!(parent_edge[child], Some(edge));
            successor.insert(index, child);
        }
    }
    let children: HashSet<_> = successor.values().copied().collect();
    let starts: Vec<_> = (0..triangles.len())
        .filter(|index| !children.contains(index))
        .collect();

    let mut chains = Vec::new();
    for start in starts {
        let mut forward = Vec::new();
        let mut current = start;
        loop {
            forward.push(selected[current]);
            if let Some(next) = successor.get(&current) {
                current = *next;
            } else {
                break;
            }
        }
        forward.reverse();
        chains.push(forward);
    }
    chains.sort();
    assert_eq!(chains.iter().map(Vec::len).sum::<usize>(), triangles.len());
    chains
}

fn direct_endpoint(
    source: Mask,
    mark: usize,
    geometry: &Geometry,
    first_is_plus: bool,
) -> (Mask, Mask, Vec<Vec<usize>>) {
    assert!(source & bit(mark) != 0);
    assert_eq!(source & geometry.physical_mask, 0);
    let chains = rooted_flip_chains(source, mark, geometry, first_is_plus);
    let mut endpoint = source;
    for chain in &chains {
        for diagonal in chain {
            let (next, replacement) = flip_diagonal(endpoint, *diagonal, geometry);
            assert!(geometry.is_physical(replacement));
            endpoint = next;
        }
    }
    let core = endpoint & geometry.physical_mask;
    assert_eq!(core.count_ones() as usize, geometry.n / 2 - 2);
    assert!(endpoint & bit(mark) != 0);
    (endpoint, core, chains)
}

fn state_at_prefixes(
    source: Mask,
    chains: &[Vec<usize>],
    positions: &[usize],
    geometry: &Geometry,
) -> Mask {
    assert_eq!(chains.len(), positions.len());
    let mut result = source;
    for (chain, position) in chains.iter().zip(positions) {
        for diagonal in &chain[..*position] {
            let (next, replacement) = flip_diagonal(result, *diagonal, geometry);
            assert!(geometry.is_physical(replacement));
            result = next;
        }
    }
    assert_eq!(
        (result & geometry.physical_mask).count_ones() as usize,
        positions.iter().sum()
    );
    result
}

fn all_positions(chains: &[Vec<usize>]) -> Vec<Vec<usize>> {
    fn visit(
        chains: &[Vec<usize>],
        index: usize,
        current: &mut Vec<usize>,
        result: &mut Vec<Vec<usize>>,
    ) {
        if index == chains.len() {
            result.push(current.clone());
            return;
        }
        for position in 0..=chains[index].len() {
            current.push(position);
            visit(chains, index + 1, current, result);
            current.pop();
        }
    }
    let mut result = Vec::new();
    visit(chains, 0, &mut Vec::new(), &mut result);
    result
}

#[derive(Clone, Copy, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
struct MixedSquare {
    lower: [Mask; 2],
    upper: [Mask; 2],
    base_core: Mask,
    cut_edge: usize,
}

fn sorted_pair(first: Mask, second: Mask) -> [Mask; 2] {
    if first < second {
        [first, second]
    } else {
        [second, first]
    }
}

fn mixed_squares(geometry: &Geometry, first_is_plus: bool) -> (BTreeSet<MixedSquare>, usize) {
    let mut squares = BTreeSet::new();
    let mut occurrence_count = 0;
    for source in zero_core_sources(geometry) {
        for mark in mask_indices(source) {
            let (_, _, chains) = direct_endpoint(source, mark, geometry, first_is_plus);
            for positions in all_positions(&chains) {
                let active: Vec<_> = chains
                    .iter()
                    .enumerate()
                    .filter_map(|(index, chain)| (positions[index] < chain.len()).then_some(index))
                    .collect();
                for repeated in &active {
                    if positions[*repeated] + 2 > chains[*repeated].len() {
                        continue;
                    }
                    for independent in &active {
                        if repeated == independent {
                            continue;
                        }
                        let current = state_at_prefixes(source, &chains, &positions, geometry);
                        let (alternate, scalar_replacement) = flip_diagonal(
                            current,
                            chains[*repeated][positions[*repeated] + 1],
                            geometry,
                        );
                        assert!(!geometry.is_physical(scalar_replacement));
                        let (upper_current, cut_edge) = flip_diagonal(
                            current,
                            chains[*independent][positions[*independent]],
                            geometry,
                        );
                        let (upper_alternate, other_cut_edge) = flip_diagonal(
                            alternate,
                            chains[*independent][positions[*independent]],
                            geometry,
                        );
                        assert_eq!(cut_edge, other_cut_edge);
                        assert!(geometry.is_physical(cut_edge));
                        let base_core = current & geometry.physical_mask;
                        assert_eq!(alternate & geometry.physical_mask, base_core);
                        let new_core = base_core | bit(cut_edge);
                        assert_eq!(upper_current & geometry.physical_mask, new_core);
                        assert_eq!(upper_alternate & geometry.physical_mask, new_core);
                        assert_eq!((current ^ alternate).count_ones(), 2);
                        assert_eq!((upper_current ^ upper_alternate).count_ones(), 2);
                        squares.insert(MixedSquare {
                            lower: sorted_pair(current, alternate),
                            upper: sorted_pair(upper_current, upper_alternate),
                            base_core,
                            cut_edge,
                        });
                        occurrence_count += 1;
                    }
                }
            }
        }
    }
    (squares, occurrence_count)
}

fn core_regions(core: Mask, geometry: &Geometry) -> Vec<Vec<usize>> {
    let mut regions = vec![(0..geometry.n).collect::<Vec<_>>()];
    for diagonal in mask_indices(core) {
        let (first, second) = geometry.diagonals[diagonal];
        let mut candidate = None;
        for (region_index, region) in regions.iter().enumerate() {
            let Some(first_index) = region.iter().position(|vertex| *vertex == first) else {
                continue;
            };
            let Some(second_index) = region.iter().position(|vertex| *vertex == second) else {
                continue;
            };
            let cyclic_distance = (second_index + region.len() - first_index) % region.len();
            if cyclic_distance != 1 && cyclic_distance != region.len() - 1 {
                assert!(candidate.is_none());
                candidate = Some((region_index, first_index, second_index));
            }
        }
        let (region_index, mut first_index, mut second_index) =
            candidate.expect("cut diagonal must split one region");
        let region = regions.remove(region_index);
        if first_index > second_index {
            std::mem::swap(&mut first_index, &mut second_index);
        }
        let first_region = region[first_index..=second_index].to_vec();
        let mut second_region = region[second_index..].to_vec();
        second_region.extend_from_slice(&region[..=first_index]);
        regions.push(first_region);
        regions.push(second_region);
    }
    regions.sort();
    assert_eq!(regions.len(), core.count_ones() as usize + 1);
    assert!(regions.iter().all(|region| region.len() % 2 == 0));
    regions
}

fn localize_diagonal(
    global_diagonal: usize,
    region: &[usize],
    global_geometry: &Geometry,
    local_geometry: &Geometry,
) -> Option<usize> {
    let (first, second) = global_geometry.diagonals[global_diagonal];
    let first_position = region.iter().position(|vertex| *vertex == first)?;
    let second_position = region.iter().position(|vertex| *vertex == second)?;
    local_geometry.optional_diagonal_id(first_position, second_position)
}

fn globalize_diagonal(
    local_diagonal: usize,
    region: &[usize],
    local_geometry: &Geometry,
    global_geometry: &Geometry,
) -> usize {
    let (first, second) = local_geometry.diagonals[local_diagonal];
    global_geometry.diagonal_id(region[first], region[second])
}

fn globalize_mask(
    local_mask: Mask,
    region: &[usize],
    local_geometry: &Geometry,
    global_geometry: &Geometry,
) -> Mask {
    mask_indices(local_mask)
        .into_iter()
        .fold(0, |result, diagonal| {
            result
                | bit(globalize_diagonal(
                    diagonal,
                    region,
                    local_geometry,
                    global_geometry,
                ))
        })
}

fn globalize_cell(cell: Cell, region: &[usize]) -> Cell {
    let mut result = cell.map(|vertex| region[vertex as usize] as u8);
    result.sort_unstable();
    result
}

fn edge_present_cell(first: usize, second: usize, core: Mask, geometry: &Geometry) -> bool {
    edge_present(first, second, core, geometry)
}

fn quadrangulation_cells(core: Mask, geometry: &Geometry) -> Vec<Cell> {
    let mut result = Vec::new();
    for first in 0..geometry.n {
        for second in (first + 1)..geometry.n {
            for third in (second + 1)..geometry.n {
                for fourth in (third + 1)..geometry.n {
                    let cell = [first as u8, second as u8, third as u8, fourth as u8];
                    let vertices = [first, second, third, fourth];
                    if (0..4).all(|index| {
                        edge_present_cell(
                            vertices[index],
                            vertices[(index + 1) % 4],
                            core,
                            geometry,
                        )
                    }) {
                        result.push(cell);
                    }
                }
            }
        }
    }
    assert_eq!(result.len(), geometry.n / 2 - 1);
    result
}

fn cell_contains_edge(cell: Cell, first: usize, second: usize) -> bool {
    cell.contains(&(first as u8)) && cell.contains(&(second as u8))
}

fn cell_side(cell: Cell, first: usize, second: usize) -> u8 {
    let mut inside = 0;
    let mut outside = 0;
    for vertex in cell {
        let vertex = vertex as usize;
        if vertex == first || vertex == second {
            continue;
        }
        if first < vertex && vertex < second {
            inside += 1;
        } else {
            outside += 1;
        }
    }
    if inside == 2 {
        0
    } else {
        assert_eq!(outside, 2);
        1
    }
}

fn alternating_coorientation(diagonal: usize, geometry: &Geometry, first_is_plus: bool) -> u8 {
    let (first, _) = geometry.diagonals[diagonal];
    let plus_side = if first % 2 == 0 { 1 } else { 0 };
    if first_is_plus {
        plus_side
    } else {
        1 - plus_side
    }
}

#[derive(Clone)]
struct Flow {
    cells: Vec<Cell>,
    sink: Cell,
    outgoing: BTreeMap<Cell, usize>,
    directions: BTreeMap<usize, (Cell, Cell)>,
}

fn directed_edges(
    core: Mask,
    geometry: &Geometry,
    first_is_plus: bool,
) -> (Vec<Cell>, BTreeMap<usize, (Cell, Cell)>) {
    assert_eq!(core.count_ones() as usize, geometry.n / 2 - 2);
    assert_eq!(core & !geometry.physical_mask, 0);
    let cells = quadrangulation_cells(core, geometry);
    let mut directions = BTreeMap::new();
    for diagonal in mask_indices(core) {
        let (first, second) = geometry.diagonals[diagonal];
        let adjacent: Vec<_> = cells
            .iter()
            .copied()
            .filter(|cell| cell_contains_edge(*cell, first, second))
            .collect();
        assert_eq!(adjacent.len(), 2);
        let target_side = alternating_coorientation(diagonal, geometry, first_is_plus);
        let target = adjacent
            .iter()
            .copied()
            .find(|cell| cell_side(*cell, first, second) == target_side)
            .unwrap();
        let source = adjacent
            .iter()
            .copied()
            .find(|cell| *cell != target)
            .unwrap();
        directions.insert(diagonal, (source, target));
    }
    (cells, directions)
}

fn try_directed_sink_flow(core: Mask, geometry: &Geometry, first_is_plus: bool) -> Option<Flow> {
    let (cells, directions) = directed_edges(core, geometry, first_is_plus);
    let mut outgoing = BTreeMap::new();
    for (diagonal, (source, _)) in &directions {
        if outgoing.insert(*source, *diagonal).is_some() {
            return None;
        }
    }
    let sinks: Vec<_> = cells
        .iter()
        .copied()
        .filter(|cell| !outgoing.contains_key(cell))
        .collect();
    if sinks.len() != 1 {
        return None;
    }
    Some(Flow {
        cells,
        sink: sinks[0],
        outgoing,
        directions,
    })
}

fn directed_sink_flow(core: Mask, geometry: &Geometry, first_is_plus: bool) -> Flow {
    try_directed_sink_flow(core, geometry, first_is_plus)
        .expect("expected a unique-sink directed quadrangulation")
}

fn sink_slots(cell: Cell, geometry: &Geometry) -> [usize; 2] {
    let mut result = [
        geometry.diagonal_id(cell[0] as usize, cell[2] as usize),
        geometry.diagonal_id(cell[1] as usize, cell[3] as usize),
    ];
    result.sort_unstable();
    result
}

fn forest_sinks(
    quadrangulation: Mask,
    cut_core: Mask,
    geometry: &Geometry,
    first_is_plus: bool,
) -> Vec<Cell> {
    let (cells, directions) = directed_edges(quadrangulation, geometry, first_is_plus);
    let cell_index: BTreeMap<_, _> = cells
        .iter()
        .copied()
        .enumerate()
        .map(|(index, cell)| (cell, index))
        .collect();
    let mut adjacency = vec![Vec::<usize>::new(); cells.len()];
    let mut has_outgoing = vec![false; cells.len()];
    for (edge, (source, target)) in &directions {
        if cut_core & bit(*edge) != 0 {
            continue;
        }
        let source_index = cell_index[source];
        let target_index = cell_index[target];
        adjacency[source_index].push(target_index);
        adjacency[target_index].push(source_index);
        has_outgoing[source_index] = true;
    }

    let mut seen = vec![false; cells.len()];
    let mut sinks = Vec::new();
    for start in 0..cells.len() {
        if seen[start] {
            continue;
        }
        let mut component = vec![start];
        let mut queue = VecDeque::from([start]);
        seen[start] = true;
        while let Some(current) = queue.pop_front() {
            for neighbor in &adjacency[current] {
                if !seen[*neighbor] {
                    seen[*neighbor] = true;
                    component.push(*neighbor);
                    queue.push_back(*neighbor);
                }
            }
        }
        let component_sinks: Vec<_> = component
            .into_iter()
            .filter(|index| !has_outgoing[*index])
            .collect();
        assert_eq!(component_sinks.len(), 1);
        sinks.push(cells[component_sinks[0]]);
    }
    sinks.sort_unstable();
    assert_eq!(sinks.len(), cut_core.count_ones() as usize + 1);
    sinks
}

fn inverse_source(core: Mask, mark: usize, geometry: &Geometry, first_is_plus: bool) -> Mask {
    let flow = directed_sink_flow(core, geometry, first_is_plus);
    assert!(sink_slots(flow.sink, geometry).contains(&mark));
    let sheet_parity = geometry.diagonals[mark].0 % 2;

    let mut endpoint = core;
    for cell in &flow.cells {
        let scalar_diagonals = [
            geometry.diagonal_id(cell[0] as usize, cell[2] as usize),
            geometry.diagonal_id(cell[1] as usize, cell[3] as usize),
        ];
        let chosen: Vec<_> = scalar_diagonals
            .into_iter()
            .filter(|diagonal| geometry.diagonals[*diagonal].0 % 2 == sheet_parity)
            .collect();
        assert_eq!(chosen.len(), 1);
        endpoint |= bit(chosen[0]);
    }
    assert_eq!(endpoint.count_ones() as usize, geometry.n - 3);
    assert!(endpoint & bit(mark) != 0);

    let choose_predecessor = first_is_plus == (sheet_parity == 0);
    let mut successor = BTreeMap::new();
    for (cell, parent) in &flow.outgoing {
        let boundary = [
            canonical_pair(cell[0] as usize, cell[1] as usize),
            canonical_pair(cell[1] as usize, cell[2] as usize),
            canonical_pair(cell[2] as usize, cell[3] as usize),
            canonical_pair(cell[0] as usize, cell[3] as usize),
        ];
        let parent_pair = geometry.diagonals[*parent];
        let parent_position = boundary
            .iter()
            .position(|pair| *pair == parent_pair)
            .unwrap();
        let selected_position = if choose_predecessor {
            (parent_position + 3) % 4
        } else {
            (parent_position + 1) % 4
        };
        let selected_pair = boundary[selected_position];
        if let Some(selected) = geometry.optional_diagonal_id(selected_pair.0, selected_pair.1) {
            if core & bit(selected) != 0 {
                assert_ne!(selected, *parent);
                assert!(successor.insert(*parent, selected).is_none());
            }
        }
    }

    let children: HashSet<_> = successor.values().copied().collect();
    let starts: Vec<_> = mask_indices(core)
        .into_iter()
        .filter(|edge| !children.contains(edge))
        .collect();
    let mut source = endpoint;
    for start in starts {
        let mut diagonal = start;
        loop {
            let (next, replacement) = flip_diagonal(source, diagonal, geometry);
            assert!(!geometry.is_physical(replacement));
            source = next;
            if let Some(next_edge) = successor.get(&diagonal) {
                diagonal = *next_edge;
            } else {
                break;
            }
        }
    }
    assert_eq!(source & geometry.physical_mask, 0);
    assert!(source & bit(mark) != 0);
    source
}

fn direction_matches_global_sheet(
    local_core: Mask,
    region: &[usize],
    local_geometry: &Geometry,
    global_geometry: &Geometry,
    local_polarity: bool,
    global_polarity: bool,
) -> bool {
    let Some(flow) = try_directed_sink_flow(local_core, local_geometry, local_polarity) else {
        return false;
    };
    flow.directions
        .iter()
        .all(|(local_edge, (local_source, local_target))| {
            let global_edge =
                globalize_diagonal(*local_edge, region, local_geometry, global_geometry);
            let global_source = globalize_cell(*local_source, region);
            let global_target = globalize_cell(*local_target, region);
            let (first, second) = global_geometry.diagonals[global_edge];
            let target_side =
                alternating_coorientation(global_edge, global_geometry, global_polarity);
            cell_side(global_target, first, second) == target_side
                && cell_side(global_source, first, second) != target_side
        })
}

fn regional_internal_edges(
    source: Mask,
    cut_core: Mask,
    region: &[usize],
    global_geometry: &Geometry,
    local_geometry: &Geometry,
) -> Mask {
    let region_set: HashSet<_> = region.iter().copied().collect();
    let mut result = 0;
    for diagonal in mask_indices(source & !cut_core) {
        let (first, second) = global_geometry.diagonals[diagonal];
        if region_set.contains(&first) && region_set.contains(&second) {
            if let Some(local_diagonal) =
                localize_diagonal(diagonal, region, global_geometry, local_geometry)
            {
                result |= bit(local_diagonal);
            }
        }
    }
    assert_eq!(result.count_ones() as usize, region.len() - 3);
    assert_eq!(result & local_geometry.physical_mask, 0);
    result
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct Forward {
    quadrangulation: Mask,
    marks: Marks,
}

#[derive(Clone, Debug, Eq, Hash, PartialEq)]
struct ForwardKey {
    source: Mask,
    cut_core: Mask,
    component_marks: Vec<usize>,
    first_is_plus: bool,
}

fn regional_forward(
    source: Mask,
    cut_core: Mask,
    component_marks: &[usize],
    global_geometry: &Geometry,
    geometries: &BTreeMap<usize, Geometry>,
    first_is_plus: bool,
    cache: &mut HashMap<ForwardKey, Forward>,
) -> Forward {
    let key = ForwardKey {
        source,
        cut_core,
        component_marks: component_marks.to_vec(),
        first_is_plus,
    };
    if let Some(value) = cache.get(&key) {
        return value.clone();
    }

    let regions = core_regions(cut_core, global_geometry);
    assert_eq!(regions.len(), component_marks.len());
    let mut quadrangulation = cut_core;
    let mut marks = Vec::new();

    for (region, global_mark) in regions.iter().zip(component_marks) {
        let local_geometry = &geometries[&region.len()];
        let local_source =
            regional_internal_edges(source, cut_core, region, global_geometry, local_geometry);
        let local_mark =
            localize_diagonal(*global_mark, region, global_geometry, local_geometry).unwrap();
        assert!(local_source & bit(local_mark) != 0);

        let mut candidates = BTreeSet::new();
        if region.len() == 4 {
            candidates.insert((0, {
                let mut cell = [
                    region[0] as u8,
                    region[1] as u8,
                    region[2] as u8,
                    region[3] as u8,
                ];
                cell.sort_unstable();
                cell
            }));
        } else {
            for local_polarity in [true, false] {
                let (_, local_core, _) =
                    direct_endpoint(local_source, local_mark, local_geometry, local_polarity);
                if !direction_matches_global_sheet(
                    local_core,
                    region,
                    local_geometry,
                    global_geometry,
                    local_polarity,
                    first_is_plus,
                ) {
                    continue;
                }
                let local_flow = directed_sink_flow(local_core, local_geometry, local_polarity);
                candidates.insert((
                    globalize_mask(local_core, region, local_geometry, global_geometry),
                    globalize_cell(local_flow.sink, region),
                ));
            }
        }
        assert_eq!(candidates.len(), 1);
        let (regional_core, global_sink) = candidates.into_iter().next().unwrap();
        quadrangulation |= regional_core;
        marks.push((global_sink, *global_mark));
    }

    marks.sort_unstable();
    assert_eq!(
        quadrangulation.count_ones() as usize,
        global_geometry.n / 2 - 2
    );
    let sinks = forest_sinks(quadrangulation, cut_core, global_geometry, first_is_plus);
    let marked_sinks: Vec<_> = marks.iter().map(|(cell, _)| *cell).collect();
    assert_eq!(sinks, marked_sinks);
    for (sink, mark) in &marks {
        assert!(sink_slots(*sink, global_geometry).contains(mark));
    }

    let result = Forward {
        quadrangulation,
        marks,
    };
    cache.insert(key, result.clone());
    result
}

fn cell_is_inside_region(cell: Cell, region: &[usize]) -> bool {
    cell.iter()
        .all(|vertex| region.contains(&(*vertex as usize)))
}

fn regional_inverse(
    quadrangulation: Mask,
    cut_core: Mask,
    marks: &Marks,
    global_geometry: &Geometry,
    geometries: &BTreeMap<usize, Geometry>,
    _first_is_plus: bool,
) -> Mask {
    let mut result = cut_core;
    for region in core_regions(cut_core, global_geometry) {
        let local_geometry = &geometries[&region.len()];
        let mut local_core = 0;
        for diagonal in mask_indices(quadrangulation & !cut_core) {
            if let Some(local_diagonal) =
                localize_diagonal(diagonal, &region, global_geometry, local_geometry)
            {
                local_core |= bit(local_diagonal);
            }
        }
        assert_eq!(local_core.count_ones() as usize, region.len() / 2 - 2);

        let component_marks: Vec<_> = marks
            .iter()
            .filter(|(cell, _)| cell_is_inside_region(*cell, &region))
            .collect();
        assert_eq!(component_marks.len(), 1);
        let (global_sink, global_mark) = component_marks[0];
        let local_mark =
            localize_diagonal(*global_mark, &region, global_geometry, local_geometry).unwrap();

        let mut candidates = BTreeSet::new();
        for local_polarity in [true, false] {
            let Some(local_flow) =
                try_directed_sink_flow(local_core, local_geometry, local_polarity)
            else {
                continue;
            };
            if globalize_cell(local_flow.sink, &region) != *global_sink {
                continue;
            }
            let local_source =
                inverse_source(local_core, local_mark, local_geometry, local_polarity);
            candidates.insert(globalize_mask(
                local_source,
                &region,
                local_geometry,
                global_geometry,
            ));
        }
        assert_eq!(candidates.len(), 1);
        result |= candidates.into_iter().next().unwrap();
    }
    assert_eq!(result.count_ones() as usize, global_geometry.n - 3);
    assert_eq!(result & global_geometry.physical_mask, cut_core);
    for (_, mark) in marks {
        assert!(result & bit(*mark) != 0);
    }
    result
}

fn common_component_marks(
    square: MixedSquare,
    geometry: &Geometry,
    geometries: &BTreeMap<usize, Geometry>,
) -> Vec<Vec<usize>> {
    let common = square.lower[0] & square.lower[1];
    let regions = core_regions(square.base_core, geometry);
    let mut choices = Vec::new();
    for region in &regions {
        let local_geometry = &geometries[&region.len()];
        let mut candidates = Vec::new();
        for diagonal in mask_indices(common & !square.base_core) {
            if localize_diagonal(diagonal, region, geometry, local_geometry).is_some() {
                candidates.push(diagonal);
            }
        }
        candidates.sort_unstable();
        candidates.dedup();
        assert!(!candidates.is_empty());
        choices.push(candidates);
    }

    fn visit(
        choices: &[Vec<usize>],
        index: usize,
        current: &mut Vec<usize>,
        result: &mut Vec<Vec<usize>>,
    ) {
        if index == choices.len() {
            result.push(current.clone());
            return;
        }
        for choice in &choices[index] {
            current.push(*choice);
            visit(choices, index + 1, current, result);
            current.pop();
        }
    }
    let mut result = Vec::new();
    visit(&choices, 0, &mut Vec::new(), &mut result);
    result
}

#[derive(Clone, Copy, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
enum TargetBehavior {
    Absent,
    Fixed,
    Sliding,
}

#[derive(Clone, Copy, Debug, Eq, Hash, Ord, PartialEq, PartialOrd)]
struct SlotTransport {
    slot: usize,
    upper: [Mask; 2],
    forced: bool,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct TransportOutcome {
    behavior: TargetBehavior,
    cut_source: Option<Cell>,
    terms: Vec<SlotTransport>,
}

#[derive(Clone, Debug, Eq, Hash, PartialEq)]
struct InverseKey {
    quadrangulation: Mask,
    cut_core: Mask,
    marks: Marks,
    first_is_plus: bool,
}

fn cached_regional_inverse(
    quadrangulation: Mask,
    cut_core: Mask,
    marks: &Marks,
    global_geometry: &Geometry,
    geometries: &BTreeMap<usize, Geometry>,
    first_is_plus: bool,
    cache: &mut HashMap<InverseKey, Mask>,
) -> Mask {
    let key = InverseKey {
        quadrangulation,
        cut_core,
        marks: marks.clone(),
        first_is_plus,
    };
    if let Some(value) = cache.get(&key) {
        return *value;
    }
    let result = regional_inverse(
        quadrangulation,
        cut_core,
        marks,
        global_geometry,
        geometries,
        first_is_plus,
    );
    cache.insert(key, result);
    result
}

fn audit_transport(
    square: MixedSquare,
    component_marks: &[usize],
    geometry: &Geometry,
    geometries: &BTreeMap<usize, Geometry>,
    first_is_plus: bool,
    forward_cache: &mut HashMap<ForwardKey, Forward>,
    inverse_cache: &mut HashMap<InverseKey, Mask>,
) -> TransportOutcome {
    let left = regional_forward(
        square.lower[0],
        square.base_core,
        component_marks,
        geometry,
        geometries,
        first_is_plus,
        forward_cache,
    );
    let right = regional_forward(
        square.lower[1],
        square.base_core,
        component_marks,
        geometry,
        geometries,
        first_is_plus,
        forward_cache,
    );
    assert_ne!(left.quadrangulation, right.quadrangulation);
    assert_eq!(left.marks, right.marks);

    let left_supported = left.quadrangulation & bit(square.cut_edge) != 0;
    let right_supported = right.quadrangulation & bit(square.cut_edge) != 0;
    assert_eq!(
        left_supported, right_supported,
        "asymmetric mixed-cut support"
    );
    if !left_supported {
        return TransportOutcome {
            behavior: TargetBehavior::Absent,
            cut_source: None,
            terms: Vec::new(),
        };
    }

    let (_, left_directions) = directed_edges(left.quadrangulation, geometry, first_is_plus);
    let (_, right_directions) = directed_edges(right.quadrangulation, geometry, first_is_plus);
    let left_direction = left_directions[&square.cut_edge];
    let right_direction = right_directions[&square.cut_edge];
    assert_eq!(
        left_direction.0, right_direction.0,
        "cut source cell must be scalar-refinement invariant"
    );
    let slots = sink_slots(left_direction.0, geometry);
    assert_eq!(slots, sink_slots(right_direction.0, geometry));
    assert!(!left.marks.iter().any(|(cell, _)| *cell == left_direction.0));

    let new_core = square.base_core | bit(square.cut_edge);
    let mut terms = Vec::new();
    for slot in slots {
        let mut new_marks = left.marks.clone();
        new_marks.push((left_direction.0, slot));
        new_marks.sort_unstable();

        let left_source = cached_regional_inverse(
            left.quadrangulation,
            new_core,
            &new_marks,
            geometry,
            geometries,
            first_is_plus,
            inverse_cache,
        );
        let right_source = cached_regional_inverse(
            right.quadrangulation,
            new_core,
            &new_marks,
            geometry,
            geometries,
            first_is_plus,
            inverse_cache,
        );
        assert_eq!(left_source & geometry.physical_mask, new_core);
        assert_eq!(right_source & geometry.physical_mask, new_core);
        assert_eq!((left_source ^ right_source).count_ones(), 2);
        let difference = left_source ^ right_source;
        for diagonal in mask_indices(difference) {
            assert!(!geometry.is_physical(diagonal));
        }
        for (_, mark) in &new_marks {
            assert!(left_source & bit(*mark) != 0);
            assert!(right_source & bit(*mark) != 0);
        }

        let upper = sorted_pair(left_source, right_source);
        terms.push(SlotTransport {
            slot,
            upper,
            forced: upper == square.upper,
        });
    }
    terms.sort_unstable();
    assert_eq!(terms.iter().filter(|term| term.forced).count(), 1);
    assert_eq!(terms.iter().filter(|term| !term.forced).count(), 1);

    TransportOutcome {
        behavior: if left_direction.1 == right_direction.1 {
            TargetBehavior::Fixed
        } else {
            TargetBehavior::Sliding
        },
        cut_source: Some(left_direction.0),
        terms,
    }
}

fn rotate_square(square: MixedSquare, geometry: &Geometry) -> MixedSquare {
    MixedSquare {
        lower: sorted_pair(
            rotate_mask(square.lower[0], geometry),
            rotate_mask(square.lower[1], geometry),
        ),
        upper: sorted_pair(
            rotate_mask(square.upper[0], geometry),
            rotate_mask(square.upper[1], geometry),
        ),
        base_core: rotate_mask(square.base_core, geometry),
        cut_edge: geometry.rotation[square.cut_edge],
    }
}

fn rotate_marks_for_core(
    component_marks: &[usize],
    rotated_core: Mask,
    geometry: &Geometry,
    geometries: &BTreeMap<usize, Geometry>,
) -> Vec<usize> {
    let rotated_marks: Vec<_> = component_marks
        .iter()
        .map(|mark| geometry.rotation[*mark])
        .collect();
    let mut result = Vec::new();
    for region in core_regions(rotated_core, geometry) {
        let local_geometry = &geometries[&region.len()];
        let candidates: Vec<_> = rotated_marks
            .iter()
            .copied()
            .filter(|mark| localize_diagonal(*mark, &region, geometry, local_geometry).is_some())
            .collect();
        assert_eq!(candidates.len(), 1);
        result.push(candidates[0]);
    }
    result
}

fn rotate_outcome(outcome: &TransportOutcome, geometry: &Geometry) -> TransportOutcome {
    let mut terms: Vec<_> = outcome
        .terms
        .iter()
        .map(|term| SlotTransport {
            slot: geometry.rotation[term.slot],
            upper: sorted_pair(
                rotate_mask(term.upper[0], geometry),
                rotate_mask(term.upper[1], geometry),
            ),
            forced: term.forced,
        })
        .collect();
    terms.sort_unstable();
    TransportOutcome {
        behavior: outcome.behavior,
        cut_source: outcome.cut_source.map(|cell| rotate_cell(cell, geometry)),
        terms,
    }
}

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Profile {
    base_degree: usize,
    region_sizes: Vec<usize>,
    behavior: TargetBehavior,
    term_count: usize,
    forced_count: usize,
    parallel_count: usize,
    curvature_support: usize,
}

#[derive(Debug)]
struct AuditSummary {
    zero_sources: usize,
    square_count: usize,
    occurrence_count: usize,
    decorated_count: usize,
    supported_count: usize,
    absent_count: usize,
    profiles: BTreeMap<Profile, usize>,
}

fn audit_multiplicity(n: usize, geometries: &BTreeMap<usize, Geometry>) -> AuditSummary {
    let geometry = &geometries[&n];
    let zero_sources = zero_core_sources(geometry).len();
    let (plus_squares, plus_occurrences) = mixed_squares(geometry, true);
    let (minus_squares, minus_occurrences) = mixed_squares(geometry, false);
    assert_eq!(plus_squares.len(), minus_squares.len());
    assert_eq!(plus_occurrences, minus_occurrences);
    let rotated_square_set: BTreeSet<_> = plus_squares
        .iter()
        .copied()
        .map(|square| rotate_square(square, geometry))
        .collect();
    assert_eq!(rotated_square_set, minus_squares);

    let mut plus_forward_cache = HashMap::new();
    let mut plus_inverse_cache = HashMap::new();
    let mut minus_forward_cache = HashMap::new();
    let mut minus_inverse_cache = HashMap::new();
    let mut decorated_count = 0;
    let mut supported_count = 0;
    let mut absent_count = 0;
    let mut profiles = BTreeMap::new();

    for square in plus_squares.iter().copied() {
        let rotated_square = rotate_square(square, geometry);
        assert!(minus_squares.contains(&rotated_square));
        for component_marks in common_component_marks(square, geometry, geometries) {
            let plus_outcome = audit_transport(
                square,
                &component_marks,
                geometry,
                geometries,
                true,
                &mut plus_forward_cache,
                &mut plus_inverse_cache,
            );
            let rotated_marks = rotate_marks_for_core(
                &component_marks,
                rotated_square.base_core,
                geometry,
                geometries,
            );
            let minus_outcome = audit_transport(
                rotated_square,
                &rotated_marks,
                geometry,
                geometries,
                false,
                &mut minus_forward_cache,
                &mut minus_inverse_cache,
            );
            assert_eq!(rotate_outcome(&plus_outcome, geometry), minus_outcome);

            decorated_count += 1;
            match plus_outcome.behavior {
                TargetBehavior::Absent => absent_count += 1,
                TargetBehavior::Fixed | TargetBehavior::Sliding => supported_count += 1,
            }
            let region_sizes = core_regions(square.base_core, geometry)
                .into_iter()
                .map(|region| region.len())
                .collect();
            let forced_count = plus_outcome.terms.iter().filter(|term| term.forced).count();
            let parallel_count = plus_outcome.terms.len() - forced_count;
            let profile = Profile {
                base_degree: square.base_core.count_ones() as usize,
                region_sizes,
                behavior: plus_outcome.behavior,
                term_count: plus_outcome.terms.len(),
                forced_count,
                parallel_count,
                curvature_support: 0,
            };
            *profiles.entry(profile).or_insert(0) += 1;
        }
    }
    assert_eq!(decorated_count, supported_count + absent_count);

    let summary = AuditSummary {
        zero_sources,
        square_count: plus_squares.len(),
        occurrence_count: plus_occurrences,
        decorated_count,
        supported_count,
        absent_count,
        profiles,
    };

    match n {
        10 => {
            assert_eq!(summary.zero_sources, 10);
            assert_eq!(summary.square_count, 20);
            assert_eq!(summary.occurrence_count, 40);
            assert_eq!(summary.decorated_count, 120);
            assert_eq!(summary.supported_count, 50);
            assert_eq!(summary.absent_count, 70);
        }
        12 => {
            assert_eq!(summary.zero_sources, 28);
            assert_eq!(summary.square_count, 336);
            assert_eq!(summary.occurrence_count, 720);
            assert_eq!(summary.decorated_count, 2568);
            assert_eq!(summary.supported_count, 1092);
            assert_eq!(summary.absent_count, 1476);
        }
        14 => {
            assert_eq!(summary.zero_sources, 84);
            assert_eq!(summary.square_count, 3920);
            assert_eq!(summary.occurrence_count, 8820);
        }
        _ => unreachable!(),
    }
    summary
}

fn main() {
    let geometries: BTreeMap<_, _> = (4..=MAX_N)
        .step_by(2)
        .map(|n| (n, Geometry::new(n)))
        .collect();

    for n in [10_usize, 12_usize, 14_usize] {
        let started = std::time::Instant::now();
        let summary = audit_multiplicity(n, &geometries);
        println!(
            "n={n}: {} zero sources; {} mixed squares from {} occurrences; \
             {} decorated transports = {} supported + {} common-zero",
            summary.zero_sources,
            summary.square_count,
            summary.occurrence_count,
            summary.decorated_count,
            summary.supported_count,
            summary.absent_count,
        );
        for (profile, count) in &summary.profiles {
            println!("  {profile:?}: {count}");
        }
        println!("  elapsed: {:.3?}", started.elapsed());
    }
    println!(
        "all independent Rust mixed-naturalness, upper-edge, spectator, \
         and exact deck-covariance checks through fourteen points passed"
    );
}
