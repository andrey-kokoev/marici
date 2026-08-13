//! Scalar-only twelve-point stress test for the directed-dual-tree rule.
//!
//! This executable deliberately does not import a twelve-point QTDS contact
//! table.  It generates scalar triangulations, parity cores, quadrangulation
//! sink slots, flip distances, and marked assignments from the dodecagon
//! alone.  The ten-point rule is used without modification.

use std::collections::{BTreeMap, BTreeSet, HashMap, VecDeque};

const N: usize = 12;
const NONE: i16 = -1;

#[derive(Clone)]
struct Geometry {
    diagonal_index: [[i16; N]; N],
    diagonals: Vec<(usize, usize)>,
    physical: Vec<usize>,
    physical_mask: u64,
    rotation: Vec<usize>,
}

fn is_boundary(first: usize, second: usize) -> bool {
    let difference = first.abs_diff(second);
    difference == 1 || difference == N - 1
}

fn geometry() -> Geometry {
    let mut diagonal_index = [[NONE; N]; N];
    let mut diagonals = Vec::new();
    for first in 0..N {
        for second in (first + 1)..N {
            if !is_boundary(first, second) {
                let index = diagonals.len();
                diagonals.push((first, second));
                diagonal_index[first][second] = index as i16;
                diagonal_index[second][first] = index as i16;
            }
        }
    }
    assert_eq!(diagonals.len(), N * (N - 3) / 2);
    let physical: Vec<_> = diagonals
        .iter()
        .enumerate()
        .filter_map(|(index, (first, second))| {
            ((first + second) % 2 == 1).then_some(index)
        })
        .collect();
    assert_eq!(physical.len(), 24);
    let physical_mask = physical
        .iter()
        .fold(0_u64, |mask, index| mask | (1_u64 << index));
    let rotation = diagonals
        .iter()
        .map(|(first, second)| {
            let mut rotated_first = (first + 1) % N;
            let mut rotated_second = (second + 1) % N;
            if rotated_first > rotated_second {
                std::mem::swap(&mut rotated_first, &mut rotated_second);
            }
            diagonal_index[rotated_first][rotated_second] as usize
        })
        .collect();
    Geometry {
        diagonal_index,
        diagonals,
        physical,
        physical_mask,
        rotation,
    }
}

fn triangulations_range(
    first: usize,
    last: usize,
    geometry: &Geometry,
    memo: &mut HashMap<(usize, usize), Vec<u64>>,
) -> Vec<u64> {
    if let Some(result) = memo.get(&(first, last)) {
        return result.clone();
    }
    if last - first + 1 <= 3 {
        return vec![0];
    }
    let mut result = Vec::new();
    for split in (first + 1)..last {
        let left = triangulations_range(first, split, geometry, memo);
        let right = triangulations_range(split, last, geometry, memo);
        for left_mask in &left {
            for right_mask in &right {
                let mut mask = left_mask | right_mask;
                if split > first + 1 {
                    let index = geometry.diagonal_index[first][split];
                    assert!(index >= 0);
                    mask |= 1_u64 << index;
                }
                if split < last - 1 {
                    let index = geometry.diagonal_index[split][last];
                    assert!(index >= 0);
                    mask |= 1_u64 << index;
                }
                result.push(mask);
            }
        }
    }
    result.sort_unstable();
    result.dedup();
    memo.insert((first, last), result.clone());
    result
}

fn triangulations(geometry: &Geometry) -> Vec<u64> {
    let mut memo = HashMap::new();
    triangulations_range(0, N - 1, geometry, &mut memo)
}

fn mask_indices(mut mask: u64) -> Vec<usize> {
    let mut result = Vec::new();
    while mask != 0 {
        let index = mask.trailing_zeros() as usize;
        result.push(index);
        mask &= mask - 1;
    }
    result
}

fn edge_present(first: usize, second: usize, core: u64, geometry: &Geometry) -> bool {
    if is_boundary(first, second) {
        return true;
    }
    let index = geometry.diagonal_index[first][second];
    index >= 0 && core & (1_u64 << index) != 0
}

fn quadrangulation_cells(core: u64, geometry: &Geometry) -> Vec<[usize; 4]> {
    let mut result = Vec::new();
    for first in 0..N {
        for second in (first + 1)..N {
            for third in (second + 1)..N {
                for fourth in (third + 1)..N {
                    let cell = [first, second, third, fourth];
                    if (0..4).all(|index| {
                        edge_present(
                            cell[index],
                            cell[(index + 1) % 4],
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
    assert_eq!(result.len(), 5);
    result
}

fn cell_contains(cell: &[usize; 4], first: usize, second: usize) -> bool {
    cell.contains(&first) && cell.contains(&second)
}

fn cell_side(cell: &[usize; 4], first: usize, second: usize) -> u8 {
    let mut inside = 0;
    let mut outside = 0;
    for vertex in cell {
        if *vertex == first || *vertex == second {
            continue;
        }
        if first < *vertex && *vertex < second {
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

fn alternating_side(first: usize, plus: bool) -> u8 {
    let plus_side = if first % 2 == 0 { 1 } else { 0 };
    if plus { plus_side } else { 1 - plus_side }
}

fn cell_slots(cell: &[usize; 4], geometry: &Geometry) -> [usize; 2] {
    let first = geometry.diagonal_index[cell[0]][cell[2]];
    let second = geometry.diagonal_index[cell[1]][cell[3]];
    assert!(first >= 0 && second >= 0);
    [first as usize, second as usize]
}

fn sink_slots(core: u64, sides: &[u8], geometry: &Geometry) -> Option<[usize; 2]> {
    let cells = quadrangulation_cells(core, geometry);
    let mut outdegree = [0_u8; 5];
    for diagonal_index in mask_indices(core) {
        let (first, second) = geometry.diagonals[diagonal_index];
        let adjacent: Vec<_> = cells
            .iter()
            .enumerate()
            .filter_map(|(index, cell)| {
                cell_contains(cell, first, second).then_some(index)
            })
            .collect();
        assert_eq!(adjacent.len(), 2);
        let target = adjacent
            .iter()
            .copied()
            .find(|index| cell_side(&cells[*index], first, second) == sides[diagonal_index])
            .unwrap();
        let source = *adjacent.iter().find(|index| **index != target).unwrap();
        outdegree[source] += 1;
    }
    let sinks: Vec<_> = (0..5).filter(|index| outdegree[*index] == 0).collect();
    (sinks.len() == 1).then(|| cell_slots(&cells[sinks[0]], geometry))
}

fn alternating_sides(geometry: &Geometry, plus: bool) -> Vec<u8> {
    let mut sides = vec![0; geometry.diagonals.len()];
    for index in &geometry.physical {
        let (first, _) = geometry.diagonals[*index];
        sides[*index] = alternating_side(first, plus);
    }
    sides
}

fn chord_class(diagonal: (usize, usize)) -> usize {
    let distance = diagonal.1 - diagonal.0;
    distance.min(N - distance)
}

fn source_multiplicities(zero_cells: &[usize], triangulations: &[u64], diagonal_count: usize) -> Vec<usize> {
    let mut result = vec![0; diagonal_count];
    for index in zero_cells {
        for diagonal in mask_indices(triangulations[*index]) {
            result[diagonal] += 1;
        }
    }
    result
}

fn slot_data(
    quadrangulations: &[u64],
    sides: &[u8],
    geometry: &Geometry,
) -> (Vec<Option<[usize; 2]>>, Vec<usize>) {
    let mut slots = Vec::new();
    let mut multiplicities = vec![0; geometry.diagonals.len()];
    for core in quadrangulations {
        let value = sink_slots(*core, sides, geometry);
        if let Some(pair) = value {
            multiplicities[pair[0]] += 1;
            multiplicities[pair[1]] += 1;
        }
        slots.push(value);
    }
    (slots, multiplicities)
}

fn flip_adjacency(triangulations: &[u64]) -> Vec<Vec<usize>> {
    let mut adjacency = vec![Vec::new(); triangulations.len()];
    let mut first_incidence: HashMap<u64, usize> = HashMap::new();
    for (index, triangulation) in triangulations.iter().enumerate() {
        for diagonal in mask_indices(*triangulation) {
            let face = triangulation & !(1_u64 << diagonal);
            if let Some(other) = first_incidence.remove(&face) {
                adjacency[index].push(other);
                adjacency[other].push(index);
            } else {
                first_incidence.insert(face, index);
            }
        }
    }
    assert!(first_incidence.is_empty());
    assert!(adjacency.iter().all(|neighbors| neighbors.len() == N - 3));
    adjacency
}

fn bfs(source: usize, adjacency: &[Vec<usize>]) -> Vec<u16> {
    let mut distances = vec![u16::MAX; adjacency.len()];
    distances[source] = 0;
    let mut queue = VecDeque::from([source]);
    while let Some(vertex) = queue.pop_front() {
        for neighbor in &adjacency[vertex] {
            if distances[*neighbor] == u16::MAX {
                distances[*neighbor] = distances[vertex] + 1;
                queue.push_back(*neighbor);
            }
        }
    }
    assert!(distances.iter().all(|distance| *distance != u16::MAX));
    distances
}

fn assignment(
    sources: &[usize],
    targets: &[usize],
    mark: usize,
    distances_by_source: &HashMap<usize, Vec<u16>>,
    fibers: &[Vec<usize>],
    triangulations: &[u64],
) -> (u16, u8, Vec<(usize, usize, u16)>) {
    assert_eq!(sources.len(), targets.len());
    let size = sources.len();
    assert!(size < usize::BITS as usize);
    let mut costs = vec![vec![u16::MAX; size]; size];
    for (source_position, source) in sources.iter().enumerate() {
        let distances = &distances_by_source[source];
        for (target_position, target) in targets.iter().enumerate() {
            costs[source_position][target_position] = fibers[*target]
                .iter()
                .filter(|endpoint| triangulations[**endpoint] & (1_u64 << mark) != 0)
                .map(|endpoint| distances[*endpoint])
                .min()
                .unwrap();
        }
    }

    let state_count = 1_usize << size;
    let mut best = vec![u16::MAX; state_count];
    let mut ways = vec![0_u8; state_count];
    let mut parent = vec![usize::MAX; state_count];
    best[0] = 0;
    ways[0] = 1;
    for mask in 0..state_count {
        if ways[mask] == 0 {
            continue;
        }
        let source_position = mask.count_ones() as usize;
        if source_position == size {
            continue;
        }
        for target_position in 0..size {
            if mask & (1_usize << target_position) != 0 {
                continue;
            }
            let next = mask | (1_usize << target_position);
            let candidate = best[mask] + costs[source_position][target_position];
            if candidate < best[next] {
                best[next] = candidate;
                ways[next] = ways[mask];
                parent[next] = target_position;
            } else if candidate == best[next] {
                ways[next] = (ways[next] + ways[mask]).min(2);
            }
        }
    }
    let full = state_count - 1;
    let mut pairs = Vec::new();
    let mut mask = full;
    for source_position in (0..size).rev() {
        let target_position = parent[mask];
        assert_ne!(target_position, usize::MAX);
        pairs.push((
            sources[source_position],
            targets[target_position],
            costs[source_position][target_position],
        ));
        mask &= !(1_usize << target_position);
    }
    pairs.reverse();
    (best[full], ways[full], pairs)
}

fn rotate_mask(mask: u64, geometry: &Geometry) -> u64 {
    mask_indices(mask).iter().fold(0_u64, |result, index| {
        result | (1_u64 << geometry.rotation[*index])
    })
}

fn path_count(
    source: usize,
    endpoint: usize,
    distance: u16,
    distances: &[u16],
    adjacency: &[Vec<usize>],
) -> u64 {
    let mut counts = vec![0_u64; adjacency.len()];
    counts[source] = 1;
    for layer in 0..distance {
        for vertex in 0..adjacency.len() {
            if distances[vertex] != layer || counts[vertex] == 0 {
                continue;
            }
            for neighbor in &adjacency[vertex] {
                if distances[*neighbor] == layer + 1 {
                    counts[*neighbor] += counts[vertex];
                }
            }
        }
    }
    counts[endpoint]
}

fn shortest_paths(
    source: usize,
    endpoint: usize,
    distance: u16,
    distances: &[u16],
    adjacency: &[Vec<usize>],
) -> Vec<Vec<usize>> {
    fn visit(
        vertex: usize,
        endpoint: usize,
        distance: u16,
        distances: &[u16],
        adjacency: &[Vec<usize>],
        path: &mut Vec<usize>,
        result: &mut Vec<Vec<usize>>,
    ) {
        if path.len() == distance as usize + 1 {
            if vertex == endpoint {
                result.push(path.clone());
            }
            return;
        }
        for neighbor in &adjacency[vertex] {
            if distances[*neighbor] == distances[vertex] + 1 {
                path.push(*neighbor);
                visit(
                    *neighbor,
                    endpoint,
                    distance,
                    distances,
                    adjacency,
                    path,
                    result,
                );
                path.pop();
            }
        }
    }

    let mut result = Vec::new();
    visit(
        source,
        endpoint,
        distance,
        distances,
        adjacency,
        &mut vec![source],
        &mut result,
    );
    result.sort();
    result
}

fn route_square_edges(paths: &[Vec<usize>]) -> usize {
    let mut adjacency = vec![Vec::new(); paths.len()];
    for first in 0..paths.len() {
        for second in (first + 1)..paths.len() {
            let differences: Vec<_> = paths[first]
                .iter()
                .zip(paths[second].iter())
                .enumerate()
                .filter_map(|(index, (left, right))| (left != right).then_some(index))
                .collect();
            if differences.len() == 1 {
                assert!(differences[0] > 0 && differences[0] + 1 < paths[first].len());
                adjacency[first].push(second);
                adjacency[second].push(first);
            }
        }
    }
    let mut found = vec![false; paths.len()];
    found[0] = true;
    let mut queue = VecDeque::from([0]);
    while let Some(path) = queue.pop_front() {
        for neighbor in &adjacency[path] {
            if !found[*neighbor] {
                found[*neighbor] = true;
                queue.push_back(*neighbor);
            }
        }
    }
    assert!(found.into_iter().all(|value| value));
    adjacency.iter().map(Vec::len).sum::<usize>() / 2
}

fn marked_matching(
    slots: &[Option<[usize; 2]>],
    zero_cells: &[usize],
    quadrangulations: &[u64],
    fibers: &[Vec<usize>],
    triangulations: &[u64],
    distances_by_source: &HashMap<usize, Vec<u16>>,
) -> (
    BTreeSet<(u64, usize, u64)>,
    BTreeMap<u8, usize>,
    BTreeMap<u16, usize>,
) {
    let diagonal_count = 54;
    let mut sources_by_mark = vec![Vec::new(); diagonal_count];
    for source in zero_cells {
        for mark in mask_indices(triangulations[*source]) {
            sources_by_mark[mark].push(*source);
        }
    }
    let mut targets_by_mark = vec![Vec::new(); diagonal_count];
    for (target, value) in slots.iter().enumerate() {
        if let Some(pair) = value {
            targets_by_mark[pair[0]].push(target);
            targets_by_mark[pair[1]].push(target);
        }
    }
    let mut result = BTreeSet::new();
    let mut optimal_way_counts = BTreeMap::new();
    let mut transfer_distances = BTreeMap::new();
    for mark in 0..diagonal_count {
        if sources_by_mark[mark].is_empty() {
            assert!(targets_by_mark[mark].is_empty());
            continue;
        }
        sources_by_mark[mark].sort_unstable();
        targets_by_mark[mark].sort_unstable();
        let (_, ways, pairs) = assignment(
            &sources_by_mark[mark],
            &targets_by_mark[mark],
            mark,
            distances_by_source,
            fibers,
            triangulations,
        );
        *optimal_way_counts.entry(ways).or_insert(0) += 1;
        for (source, target, distance) in pairs {
            *transfer_distances.entry(distance).or_insert(0) += 1;
            result.insert((triangulations[source], mark, quadrangulations[target]));
        }
    }
    (result, optimal_way_counts, transfer_distances)
}

fn endpoint_diagnostics(
    matching: &BTreeSet<(u64, usize, u64)>,
    triangulation_index: &HashMap<u64, usize>,
    quadrangulation_index: &HashMap<u64, usize>,
    fibers: &[Vec<usize>],
    triangulations: &[u64],
    distances_by_source: &HashMap<usize, Vec<u16>>,
    adjacency: &[Vec<usize>],
) -> (
    BTreeMap<usize, usize>,
    BTreeMap<u64, usize>,
    BTreeMap<(usize, usize), usize>,
) {
    let mut endpoint_counts = BTreeMap::new();
    let mut path_counts = BTreeMap::new();
    let mut square_profiles = BTreeMap::new();
    for (source_mask, mark, core) in matching {
        let source = triangulation_index[source_mask];
        let target = quadrangulation_index[core];
        let distances = &distances_by_source[&source];
        let minimum = fibers[target]
            .iter()
            .filter(|endpoint| triangulations[**endpoint] & (1_u64 << mark) != 0)
            .map(|endpoint| distances[*endpoint])
            .min()
            .unwrap();
        let endpoints: Vec<_> = fibers[target]
            .iter()
            .copied()
            .filter(|endpoint| {
                triangulations[*endpoint] & (1_u64 << mark) != 0
                    && distances[*endpoint] == minimum
            })
            .collect();
        *endpoint_counts.entry(endpoints.len()).or_insert(0) += 1;
        let counted_paths: u64 = endpoints
            .iter()
            .map(|endpoint| path_count(source, *endpoint, minimum, distances, adjacency))
            .sum();
        *path_counts.entry(counted_paths).or_insert(0) += 1;
        assert_eq!(endpoints.len(), 1);
        let paths = shortest_paths(
            source,
            endpoints[0],
            minimum,
            distances,
            adjacency,
        );
        assert_eq!(paths.len() as u64, counted_paths);
        let square_edges = route_square_edges(&paths);
        *square_profiles
            .entry((paths.len(), square_edges))
            .or_insert(0) += 1;
    }
    (endpoint_counts, path_counts, square_profiles)
}

fn marked_endpoint_paths(
    source_mask: u64,
    mark: usize,
    core: u64,
    triangulation_index: &HashMap<u64, usize>,
    quadrangulation_index: &HashMap<u64, usize>,
    fibers: &[Vec<usize>],
    triangulations: &[u64],
    distances_by_source: &HashMap<usize, Vec<u16>>,
    adjacency: &[Vec<usize>],
) -> (u64, Vec<Vec<usize>>) {
    let source = triangulation_index[&source_mask];
    let target = quadrangulation_index[&core];
    let distances = &distances_by_source[&source];
    let minimum = fibers[target]
        .iter()
        .filter(|endpoint| triangulations[**endpoint] & (1_u64 << mark) != 0)
        .map(|endpoint| distances[*endpoint])
        .min()
        .unwrap();
    let endpoints: Vec<_> = fibers[target]
        .iter()
        .copied()
        .filter(|endpoint| {
            triangulations[*endpoint] & (1_u64 << mark) != 0
                && distances[*endpoint] == minimum
        })
        .collect();
    assert_eq!(endpoints.len(), 1);
    (
        triangulations[endpoints[0]],
        shortest_paths(
            source,
            endpoints[0],
            minimum,
            distances,
            adjacency,
        ),
    )
}

fn add_scaled_path(
    transport: &mut BTreeMap<(u64, u64, usize), i64>,
    path: &[usize],
    mark: usize,
    coefficient: i64,
    triangulations: &[u64],
) {
    for pair in path.windows(2) {
        let first = triangulations[pair[0]];
        let second = triangulations[pair[1]];
        let (left, right, orientation) = if first < second {
            (first, second, 1)
        } else {
            (second, first, -1)
        };
        *transport.entry((left, right, mark)).or_insert(0) += orientation * coefficient;
    }
}

fn averaged_scalar_transport(
    plus_matching: &BTreeSet<(u64, usize, u64)>,
    minus_matching: &BTreeSet<(u64, usize, u64)>,
    triangulation_index: &HashMap<u64, usize>,
    quadrangulation_index: &HashMap<u64, usize>,
    fibers: &[Vec<usize>],
    triangulations: &[u64],
    distances_by_source: &HashMap<usize, Vec<u16>>,
    adjacency: &[Vec<usize>],
    geometry: &Geometry,
) -> BTreeMap<usize, usize> {
    const SCALE: i64 = 24;
    let plus: BTreeMap<_, _> = plus_matching
        .iter()
        .map(|(source, mark, target)| ((*source, *mark), *target))
        .collect();
    let minus: BTreeMap<_, _> = minus_matching
        .iter()
        .map(|(source, mark, target)| ((*source, *mark), *target))
        .collect();
    assert_eq!(plus.keys().collect::<Vec<_>>(), minus.keys().collect::<Vec<_>>());
    let mut transport = BTreeMap::new();
    let mut expected_boundary: BTreeMap<(u64, usize), i64> = BTreeMap::new();
    for ((source, mark), plus_target) in &plus {
        let (plus_endpoint, plus_paths) = marked_endpoint_paths(
            *source,
            *mark,
            *plus_target,
            triangulation_index,
            quadrangulation_index,
            fibers,
            triangulations,
            distances_by_source,
            adjacency,
        );
        let (minus_endpoint, minus_paths) = marked_endpoint_paths(
            *source,
            *mark,
            minus[&(*source, *mark)],
            triangulation_index,
            quadrangulation_index,
            fibers,
            triangulations,
            distances_by_source,
            adjacency,
        );
        assert_eq!(SCALE % plus_paths.len() as i64, 0);
        assert_eq!(SCALE % minus_paths.len() as i64, 0);
        for path in &plus_paths {
            add_scaled_path(
                &mut transport,
                path,
                *mark,
                -SCALE / plus_paths.len() as i64,
                triangulations,
            );
        }
        for path in &minus_paths {
            add_scaled_path(
                &mut transport,
                path,
                *mark,
                SCALE / minus_paths.len() as i64,
                triangulations,
            );
        }
        *expected_boundary.entry((minus_endpoint, *mark)).or_insert(0) += SCALE;
        *expected_boundary.entry((plus_endpoint, *mark)).or_insert(0) -= SCALE;
    }
    transport.retain(|_, coefficient| *coefficient != 0);
    expected_boundary.retain(|_, coefficient| *coefficient != 0);

    let mut boundary: BTreeMap<(u64, usize), i64> = BTreeMap::new();
    for ((first, second, mark), coefficient) in &transport {
        *boundary.entry((*first, *mark)).or_insert(0) -= coefficient;
        *boundary.entry((*second, *mark)).or_insert(0) += coefficient;
    }
    boundary.retain(|_, coefficient| *coefficient != 0);
    assert_eq!(boundary, expected_boundary);

    let mut rotated = BTreeMap::new();
    for ((first, second, mark), coefficient) in &transport {
        let rotated_first = rotate_mask(*first, geometry);
        let rotated_second = rotate_mask(*second, geometry);
        let (left, right, orientation) = if rotated_first < rotated_second {
            (rotated_first, rotated_second, 1)
        } else {
            (rotated_second, rotated_first, -1)
        };
        *rotated
            .entry((left, right, geometry.rotation[*mark]))
            .or_insert(0) += orientation * coefficient;
    }
    rotated.retain(|_, coefficient| *coefficient != 0);
    assert_eq!(
        rotated,
        transport
            .iter()
            .map(|(edge, coefficient)| (*edge, -*coefficient))
            .collect()
    );

    fn gcd(mut first: i64, mut second: i64) -> i64 {
        while second != 0 {
            let remainder = first % second;
            first = second;
            second = remainder;
        }
        first.abs()
    }
    let mut denominators = BTreeMap::new();
    for coefficient in transport.values() {
        let denominator = (SCALE / gcd(coefficient.abs(), SCALE)) as usize;
        *denominators.entry(denominator).or_insert(0) += 1;
    }
    denominators
}

fn main() {
    let geometry = geometry();
    let triangulations = triangulations(&geometry);
    assert_eq!(triangulations.len(), 16_796);
    assert!(triangulations
        .iter()
        .all(|triangulation| triangulation.count_ones() as usize == N - 3));

    let zero_cells: Vec<_> = triangulations
        .iter()
        .enumerate()
        .filter_map(|(index, triangulation)| {
            (triangulation & geometry.physical_mask == 0).then_some(index)
        })
        .collect();
    let source_counts = source_multiplicities(
        &zero_cells,
        &triangulations,
        geometry.diagonals.len(),
    );

    let mut fiber_map: BTreeMap<u64, Vec<usize>> = BTreeMap::new();
    for (index, triangulation) in triangulations.iter().enumerate() {
        let core = triangulation & geometry.physical_mask;
        if core.count_ones() == 4 {
            fiber_map.entry(core).or_default().push(index);
        }
    }
    let quadrangulations: Vec<_> = fiber_map.keys().copied().collect();
    let fibers: Vec<_> = quadrangulations
        .iter()
        .map(|core| fiber_map[core].clone())
        .collect();
    assert_eq!(quadrangulations.len(), 273);
    assert!(fibers.iter().all(|fiber| fiber.len() == 32));

    let plus_sides = alternating_sides(&geometry, true);
    let minus_sides = alternating_sides(&geometry, false);
    let (plus_slots, plus_counts) = slot_data(&quadrangulations, &plus_sides, &geometry);
    let (minus_slots, minus_counts) = slot_data(&quadrangulations, &minus_sides, &geometry);
    assert_eq!(plus_counts, source_counts);
    assert_eq!(minus_counts, source_counts);

    // Rotation reversal has one independent seed on each physical chord
    // class (length 3 and length 5).  Test all four such patterns; scalar
    // contact conservation must correlate the seeds.
    let mut rotation_candidates = Vec::new();
    let mut conservative_candidates = Vec::new();
    for choice in 0..4 {
        let mut sides = plus_sides.clone();
        for diagonal_index in &geometry.physical {
            let class = chord_class(geometry.diagonals[*diagonal_index]);
            let class_bit = match class {
                3 => 0,
                5 => 1,
                _ => panic!("unexpected physical chord class"),
            };
            if choice & (1 << class_bit) != 0 {
                sides[*diagonal_index] ^= 1;
            }
        }
        rotation_candidates.push(sides.clone());
        let (_, counts) = slot_data(&quadrangulations, &sides, &geometry);
        if counts == source_counts {
            conservative_candidates.push(choice);
        }
    }
    assert_eq!(rotation_candidates.len(), 4);
    assert_eq!(conservative_candidates, vec![0, 3]);

    let adjacency = flip_adjacency(&triangulations);
    let mut distances_by_source = HashMap::new();
    for source in &zero_cells {
        distances_by_source.insert(*source, bfs(*source, &adjacency));
    }

    let (plus_matching, plus_ways, plus_distances) = marked_matching(
        &plus_slots,
        &zero_cells,
        &quadrangulations,
        &fibers,
        &triangulations,
        &distances_by_source,
    );
    let (minus_matching, minus_ways, minus_distances) = marked_matching(
        &minus_slots,
        &zero_cells,
        &quadrangulations,
        &fibers,
        &triangulations,
        &distances_by_source,
    );

    let rotated_plus: BTreeSet<_> = plus_matching
        .iter()
        .map(|(source, mark, target)| {
            (
                rotate_mask(*source, &geometry),
                geometry.rotation[*mark],
                rotate_mask(*target, &geometry),
            )
        })
        .collect();
    assert_eq!(rotated_plus, minus_matching);

    let triangulation_index: HashMap<_, _> = triangulations
        .iter()
        .enumerate()
        .map(|(index, mask)| (*mask, index))
        .collect();
    let quadrangulation_index: HashMap<_, _> = quadrangulations
        .iter()
        .enumerate()
        .map(|(index, mask)| (*mask, index))
        .collect();
    let plus_endpoint_data = endpoint_diagnostics(
        &plus_matching,
        &triangulation_index,
        &quadrangulation_index,
        &fibers,
        &triangulations,
        &distances_by_source,
        &adjacency,
    );
    let minus_endpoint_data = endpoint_diagnostics(
        &minus_matching,
        &triangulation_index,
        &quadrangulation_index,
        &fibers,
        &triangulations,
        &distances_by_source,
        &adjacency,
    );
    let transport_denominators = averaged_scalar_transport(
        &plus_matching,
        &minus_matching,
        &triangulation_index,
        &quadrangulation_index,
        &fibers,
        &triangulations,
        &distances_by_source,
        &adjacency,
        &geometry,
    );

    let unique_sink_count = plus_slots.iter().filter(|value| value.is_some()).count();
    let marked_source_count: usize = zero_cells
        .iter()
        .map(|index| triangulations[*index].count_ones() as usize)
        .sum();
    assert_eq!(2 * unique_sink_count, marked_source_count);
    assert_eq!(plus_ways, BTreeMap::from([(1, 30)]));
    assert_eq!(minus_ways, BTreeMap::from([(1, 30)]));
    assert_eq!(plus_distances, BTreeMap::from([(4, marked_source_count)]));
    assert_eq!(minus_distances, plus_distances);
    assert_eq!(plus_endpoint_data.0, BTreeMap::from([(1, marked_source_count)]));
    assert_eq!(minus_endpoint_data, plus_endpoint_data);

    println!(
        "n=12 scalar cores: {} triangulations, {} zero-core cells, {} marked sources, {} quadrangulations, 32 refinements per full core",
        triangulations.len(),
        zero_cells.len(),
        marked_source_count,
        quadrangulations.len(),
    );
    println!(
        "n=12 scalar coorientation: alternating flows give {} unique sinks and conserve every marked scalar diagonal; among the four rotation-reversing chord-orbit patterns only the opposite alternating pair conserves contacts",
        unique_sink_count,
    );
    println!(
        "n=12 scalar matching: plus ways={:?}, distances={:?}; minus ways={:?}, distances={:?}; one-step rotation exchanges the matchings",
        plus_ways, plus_distances, minus_ways, minus_distances,
    );
    println!(
        "n=12 marked lift diagnostics: endpoints={:?}, shortest-path multiplicities={:?}, square-move profiles={:?}",
        plus_endpoint_data.0, plus_endpoint_data.1, plus_endpoint_data.2,
    );
    println!(
        "n=12 scalar lift: the all-geodesic average has exact contact boundary, is deck odd, and has reduced coefficient denominators {:?}",
        transport_denominators,
    );
    println!("all scalar-only twelve-point checks passed");
}
