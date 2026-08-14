//! Exact cubical-coherence audit for the scalar octagon.
//!
//! This certificate separates three statements which can otherwise be
//! conflated.  Every physical rank-two quadrangulation core cuts the octagon
//! into three quadrilaterals, so its fixed-core associahedral face is an
//! honest I^3.  The established supported double-Gysin occurrence images
//! determine coordinate facets of those cubes.  Four such images form a
//! side-facet belt only on the eight pentagon/companion-square cores; the
//! other four square/square cores have only two established images.
//!
//! On each four-chart cube the coordinate-facet inclusions extending the
//! occurrence sets are cellular chain maps.  This is a target-cube statement,
//! not a Gysin chain map from the route polygon: the established Gysin data
//! specify support on occurrences but no maps on route edges or 2-cells.  In
//! particular a pentagon cannot silently be identified with a square facet.
//! The outward-oriented target facets form an annular belt; two missing caps
//! and the cube fill its cellular coherence.  No finite-alpha-prime,
//! Pochhammer, or route-to-cube chain map is asserted here.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

const N: usize = 8;
const STAR: i8 = -1;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge(usize, usize);

type Cell = Vec<usize>;
type Triangulation = Vec<Edge>;
type Chain = BTreeMap<CubeCell, i64>;
type Matrix = Vec<Vec<i64>>;

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Occurrence(Vec<(Cell, Edge)>);

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

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct CubeCell([i8; 3]);

impl CubeCell {
    fn dimension(self) -> usize {
        self.0.iter().filter(|&&entry| entry == STAR).count()
    }

    fn boundary(self) -> Vec<(Self, i64)> {
        let mut result = Vec::new();
        let mut free_position = 0;
        for coordinate in 0..3 {
            if self.0[coordinate] != STAR {
                continue;
            }
            let sign = if free_position % 2 == 0 { 1 } else { -1 };
            let mut positive = self;
            positive.0[coordinate] = 1;
            let mut negative = self;
            negative.0[coordinate] = 0;
            result.push((positive, sign));
            result.push((negative, -sign));
            free_position += 1;
        }
        result
    }

    fn belongs_to_facet(self, facet: (usize, usize)) -> bool {
        self.0[facet.0] == facet.1 as i8
    }
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct SquareCell([i8; 2]);

impl SquareCell {
    fn boundary(self) -> Vec<(Self, i64)> {
        let mut result = Vec::new();
        let mut free_position = 0;
        for coordinate in 0..2 {
            if self.0[coordinate] != STAR {
                continue;
            }
            let sign = if free_position % 2 == 0 { 1 } else { -1 };
            let mut positive = self;
            positive.0[coordinate] = 1;
            let mut negative = self;
            negative.0[coordinate] = 0;
            result.push((positive, sign));
            result.push((negative, -sign));
            free_position += 1;
        }
        result
    }
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

fn forest_sinks(
    cells: &[Cell],
    directions: &BTreeMap<Edge, (Cell, Cell)>,
    cut: &BTreeSet<Edge>,
) -> Vec<Cell> {
    let indices: BTreeMap<_, _> = cells
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
    let mut records = BTreeSet::from([Occurrence(vec![(global_sink, global_mark)])]);
    for diagonal in order {
        let source = directions[&diagonal].0.clone();
        let mut next = BTreeSet::new();
        for occurrence in records {
            for slot in cell_slots(&source) {
                let mut marks = occurrence.0.clone();
                marks.push((source.clone(), slot));
                marks.sort();
                next.insert(Occurrence(marks));
            }
        }
        records = next;
    }
    assert_eq!(records.len(), 4);
    records
}

fn full_occurrences(current: [Edge; 2]) -> BTreeSet<Occurrence> {
    let cells = core_regions(&current);
    assert_eq!(
        cells.iter().map(Vec::len).collect::<Vec<_>>(),
        vec![4, 4, 4]
    );
    let mut result = BTreeSet::new();
    for mask in 0..8 {
        let mut marks = Vec::new();
        for (index, cell) in cells.iter().enumerate() {
            marks.push((cell.clone(), cell_slots(cell)[(mask >> index) & 1]));
        }
        marks.sort();
        result.insert(Occurrence(marks));
    }
    result
}

fn supported_images(face: &RouteFace) -> Vec<(bool, BTreeSet<Occurrence>)> {
    let mut result = Vec::new();
    for plus in [true, false] {
        let cells = core_regions(&face.core);
        let directions = directed_edges(face.core, plus);
        let sinks = forest_sinks(&cells, &directions, &BTreeSet::new());
        if sinks.len() != 1 {
            continue;
        }
        let marks: Vec<_> = cell_slots(&sinks[0])
            .into_iter()
            .filter(|mark| face.common.contains(mark))
            .collect();
        assert_eq!(marks.len(), 1);
        let first = expanded_occurrences(face.core, plus, marks[0], face.core);
        let second = expanded_occurrences(face.core, plus, marks[0], [face.core[1], face.core[0]]);
        assert_eq!(first, second);
        result.push((plus, first));
    }
    result
}

fn occurrence_mask(current: [Edge; 2], occurrence: &Occurrence) -> usize {
    let cells = core_regions(&current);
    assert_eq!(occurrence.0.len(), cells.len());
    let mut result = 0;
    for (cell_index, cell) in cells.iter().enumerate() {
        let (_, mark) = occurrence
            .0
            .iter()
            .find(|(marked_cell, _)| marked_cell == cell)
            .expect("one marked diagonal in every quadrilateral");
        let slot = cell_slots(cell)
            .iter()
            .position(|candidate| candidate == mark)
            .unwrap();
        result |= slot << cell_index;
    }
    result
}

fn coordinate_facet(current: [Edge; 2], chart: &BTreeSet<Occurrence>) -> (usize, usize) {
    assert_eq!(chart.len(), 4);
    let masks: BTreeSet<_> = chart
        .iter()
        .map(|occurrence| occurrence_mask(current, occurrence))
        .collect();
    for coordinate in 0..3 {
        for value in 0..2 {
            let expected: BTreeSet<_> = (0..8)
                .filter(|mask| ((mask >> coordinate) & 1) == value)
                .collect();
            if masks == expected {
                return (coordinate, value);
            }
        }
    }
    panic!("supported occurrence image is not a coordinate facet")
}

fn triangulation_mask(current: [Edge; 2], triangulation: &Triangulation) -> usize {
    let cells = core_regions(&current);
    let mut result = 0;
    for (coordinate, cell) in cells.iter().enumerate() {
        let slots = cell_slots(cell);
        let chosen: Vec<_> = slots
            .iter()
            .enumerate()
            .filter_map(|(slot, diagonal)| triangulation.contains(diagonal).then_some(slot))
            .collect();
        assert_eq!(chosen.len(), 1);
        result |= chosen[0] << coordinate;
    }
    result
}

fn all_cube_cells() -> Vec<CubeCell> {
    let mut result = Vec::new();
    for code in 0..27 {
        let mut work = code;
        let mut word = [0_i8; 3];
        for entry in &mut word {
            *entry = match work % 3 {
                0 => 0,
                1 => 1,
                2 => STAR,
                _ => unreachable!(),
            };
            work /= 3;
        }
        result.push(CubeCell(word));
    }
    result.sort_by_key(|cell| (cell.dimension(), *cell));
    result
}

fn all_square_cells() -> Vec<SquareCell> {
    let mut result = Vec::new();
    for code in 0..9 {
        let mut work = code;
        let mut word = [0_i8; 2];
        for entry in &mut word {
            *entry = match work % 3 {
                0 => 0,
                1 => 1,
                2 => STAR,
                _ => unreachable!(),
            };
            work /= 3;
        }
        result.push(SquareCell(word));
    }
    result.sort_by_key(|cell| (cell.0.iter().filter(|&&x| x == STAR).count(), *cell));
    result
}

fn embed_square(cell: SquareCell, facet: (usize, usize)) -> CubeCell {
    let mut result = [STAR; 3];
    result[facet.0] = facet.1 as i8;
    let mut source = 0;
    for (coordinate, entry) in result.iter_mut().enumerate() {
        if coordinate != facet.0 {
            *entry = cell.0[source];
            source += 1;
        }
    }
    CubeCell(result)
}

fn add_term(chain: &mut Chain, cell: CubeCell, coefficient: i64) {
    if coefficient == 0 {
        return;
    }
    let entry = chain.entry(cell).or_default();
    *entry += coefficient;
    if *entry == 0 {
        chain.remove(&cell);
    }
}

fn chain_boundary(chain: &Chain) -> Chain {
    let mut result = Chain::new();
    for (&cell, &coefficient) in chain {
        for (face, face_coefficient) in cell.boundary() {
            add_term(&mut result, face, coefficient * face_coefficient);
        }
    }
    result
}

fn outward_facet(facet: (usize, usize)) -> (CubeCell, i64) {
    let mut word = [STAR; 3];
    word[facet.0] = facet.1 as i8;
    let coefficient = if facet.0 % 2 == 0 { 1 } else { -1 } * if facet.1 == 1 { 1 } else { -1 };
    (CubeCell(word), coefficient)
}

fn selected_complex(facets: &[(usize, usize)], filled: bool) -> Vec<CubeCell> {
    all_cube_cells()
        .into_iter()
        .filter(|cell| {
            (filled && cell.dimension() == 3)
                || facets.iter().any(|&facet| cell.belongs_to_facet(facet))
        })
        .collect()
}

fn matrix(rows: usize, columns: usize) -> Matrix {
    vec![vec![0; columns]; rows]
}

fn multiply(first: &Matrix, second: &Matrix) -> Matrix {
    if first.is_empty() {
        return Vec::new();
    }
    assert!(!second.is_empty());
    assert_eq!(first[0].len(), second.len());
    let columns = second[0].len();
    let mut result = matrix(first.len(), columns);
    for row in 0..first.len() {
        for middle in 0..second.len() {
            for column in 0..columns {
                result[row][column] += first[row][middle] * second[middle][column];
            }
        }
    }
    result
}

fn boundary_matrix(cells: &[CubeCell], degree: usize) -> Matrix {
    let lower: Vec<_> = cells
        .iter()
        .copied()
        .filter(|cell| cell.dimension() + 1 == degree)
        .collect();
    let upper: Vec<_> = cells
        .iter()
        .copied()
        .filter(|cell| cell.dimension() == degree)
        .collect();
    let row_index: BTreeMap<_, _> = lower
        .iter()
        .copied()
        .enumerate()
        .map(|(index, cell)| (cell, index))
        .collect();
    let mut result = matrix(lower.len(), upper.len());
    for (column, cell) in upper.iter().copied().enumerate() {
        for (face, coefficient) in cell.boundary() {
            result[row_index[&face]][column] = coefficient;
        }
    }
    result
}

/// Integral elimination using only unit pivots.  Reaching a zero remainder
/// certifies that every nonzero Smith factor is one.
fn unit_smith_rank(value: &Matrix) -> usize {
    if value.is_empty() || value[0].is_empty() {
        return 0;
    }
    let mut work = value.clone();
    let rows = work.len();
    let columns = work[0].len();
    let mut pivot = 0;
    while pivot < rows && pivot < columns {
        let found = (pivot..rows).find_map(|row| {
            (pivot..columns)
                .find(|&column| work[row][column].abs() == 1)
                .map(|column| (row, column))
        });
        let Some((pivot_row, pivot_column)) = found else {
            break;
        };
        work.swap(pivot, pivot_row);
        for row in &mut work {
            row.swap(pivot, pivot_column);
        }
        if work[pivot][pivot] == -1 {
            for entry in &mut work[pivot] {
                *entry = -*entry;
            }
        }
        for row in 0..rows {
            if row == pivot {
                continue;
            }
            let coefficient = work[row][pivot];
            for column in pivot..columns {
                work[row][column] -= coefficient * work[pivot][column];
            }
        }
        for column in 0..columns {
            if column == pivot {
                continue;
            }
            let coefficient = work[pivot][column];
            for row in 0..rows {
                work[row][column] -= coefficient * work[row][pivot];
            }
        }
        pivot += 1;
    }
    assert!(work[pivot..]
        .iter()
        .all(|row| row[pivot.min(columns)..].iter().all(|&entry| entry == 0)));
    pivot
}

fn homology(cells: &[CubeCell]) -> ([usize; 4], [usize; 4]) {
    let mut counts = [0; 4];
    for cell in cells {
        counts[cell.dimension()] += 1;
    }
    let mut ranks = [0; 4];
    let mut boundaries = Vec::new();
    boundaries.push(Vec::new());
    for degree in 1..=3 {
        let boundary = boundary_matrix(cells, degree);
        ranks[degree] = unit_smith_rank(&boundary);
        boundaries.push(boundary);
    }
    for degree in 2..=3 {
        let square = multiply(&boundaries[degree - 1], &boundaries[degree]);
        assert!(square.iter().flatten().all(|&entry| entry == 0));
    }
    let mut betti = [0; 4];
    for degree in 0..=3 {
        betti[degree] =
            counts[degree] - ranks[degree] - if degree < 3 { ranks[degree + 1] } else { 0 };
    }
    (counts, betti)
}

fn check_facet_chain_map(facet: (usize, usize)) -> usize {
    let mut checks = 0;
    for source in all_square_cells() {
        let mut mapped_boundary = Chain::new();
        for (face, coefficient) in source.boundary() {
            add_term(&mut mapped_boundary, embed_square(face, facet), coefficient);
        }
        let image = BTreeMap::from([(embed_square(source, facet), 1)]);
        assert_eq!(mapped_boundary, chain_boundary(&image));
        checks += 1;
    }
    checks
}

/// Count cellular polygon-to-square lifts compatible with only the setwise
/// statement that all four square vertices occur. Consecutive source
/// vertices may map to equal or adjacent target vertices. The signed step
/// sum is four times the degree of the induced boundary map, so sending the
/// source 2-cell to that degree times the target 2-cell gives a chain map.
fn support_only_polygon_lifts(vertex_count: usize) -> BTreeMap<i64, usize> {
    let mut profile = BTreeMap::new();
    for code in 0..4_usize.pow(vertex_count as u32) {
        let mut work = code;
        let mut values = Vec::new();
        for _ in 0..vertex_count {
            values.push(work % 4);
            work /= 4;
        }
        if values.iter().copied().collect::<BTreeSet<_>>().len() != 4 {
            continue;
        }
        let mut signed_steps = 0_i64;
        let mut cellular = true;
        for index in 0..vertex_count {
            let first = values[index];
            let second = values[(index + 1) % vertex_count];
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
            *profile.entry(signed_steps / 4).or_default() += 1;
        }
    }
    profile
}

fn main() {
    let tris = triangulations();
    assert_eq!(tris.len(), 132);
    let faces = route_faces(&tris);
    assert_eq!(faces.len(), 24);

    let mut grouped = BTreeMap::<Vec<Edge>, Vec<&Triangulation>>::new();
    for triangulation in &tris {
        grouped
            .entry(core(triangulation))
            .or_default()
            .push(triangulation);
    }
    let cores: Vec<[Edge; 2]> = grouped
        .keys()
        .filter(|current| current.len() == 2)
        .map(|current| [current[0], current[1]])
        .collect();
    assert_eq!(cores.len(), 12);

    let all_cells = all_cube_cells();
    assert_eq!(
        (0..=3)
            .map(|degree| all_cells
                .iter()
                .filter(|cell| cell.dimension() == degree)
                .count())
            .collect::<Vec<_>>(),
        vec![8, 12, 6, 1]
    );

    let mut fixed_core_vertices = 0;
    let mut face_poset_cells = 0;
    let mut four_chart_cores = 0;
    let mut two_chart_cores = 0;
    let mut cellular_map_checks = 0;
    let mut chart_type_profile = BTreeMap::<(usize, usize), usize>::new();
    let mut chart_facets_on_four_core = BTreeMap::<(usize, usize), usize>::new();
    let mut representative_charts = Vec::new();
    let mut representative_caps = Vec::new();

    for current in cores {
        let regions = core_regions(&current);
        assert_eq!(regions.len(), 3);
        assert!(regions.iter().all(|region| region.len() == 4));

        let fixed: Vec<_> = tris
            .iter()
            .filter(|triangulation| current.iter().all(|edge| triangulation.contains(edge)))
            .collect();
        assert_eq!(fixed.len(), 8);
        assert!(fixed
            .iter()
            .all(|triangulation| core(triangulation) == current));
        let masks: BTreeSet<_> = fixed
            .iter()
            .map(|triangulation| triangulation_mask(current, triangulation))
            .collect();
        assert_eq!(masks, (0..8).collect());
        for first in 0..fixed.len() {
            for second in first + 1..fixed.len() {
                let hamming = (triangulation_mask(current, fixed[first])
                    ^ triangulation_mask(current, fixed[second]))
                .count_ones();
                assert_eq!(adjacent(fixed[first], fixed[second]), hamming == 1);
            }
        }
        fixed_core_vertices += fixed.len();

        // Every word in {0,1,*}^3 is the fixed-core dissection obtained by
        // resolving the indicated quadrilateral slots.  Its completions are
        // precisely the 2^(number of stars) vertices above it.
        for cell in &all_cells {
            let completions = fixed
                .iter()
                .filter(|triangulation| {
                    let mask = triangulation_mask(current, triangulation);
                    (0..3).all(|coordinate| {
                        cell.0[coordinate] == STAR
                            || cell.0[coordinate] as usize == ((mask >> coordinate) & 1)
                    })
                })
                .count();
            assert_eq!(completions, 1 << cell.dimension());
            face_poset_cells += 1;
        }

        let core_faces: Vec<_> = faces.iter().filter(|face| face.core == current).collect();
        assert_eq!(core_faces.len(), 2);
        assert_eq!(
            core_faces
                .iter()
                .map(|face| face.sheet)
                .collect::<BTreeSet<_>>(),
            BTreeSet::from([0, 1])
        );

        let mut charts = Vec::new();
        let mut kinds = BTreeMap::<FaceKind, usize>::new();
        for face in core_faces {
            assert_eq!(
                face.vertices.len(),
                match face.kind {
                    FaceKind::Square => 4,
                    FaceKind::Pentagon => 5,
                }
            );
            *kinds.entry(face.kind).or_default() += 1;
            for (plus, image) in supported_images(face) {
                assert!(image.is_subset(&full_occurrences(current)));
                let facet = coordinate_facet(current, &image);
                charts.push((face.kind, plus, facet));
            }
        }
        let distinct_facets: BTreeSet<_> = charts.iter().map(|entry| entry.2).collect();
        if charts.len() == 4 {
            assert_eq!(
                kinds,
                BTreeMap::from([(FaceKind::Square, 1), (FaceKind::Pentagon, 1)])
            );
            assert_eq!(distinct_facets.len(), 4);
            let missing: Vec<_> = (0..3)
                .flat_map(|coordinate| (0..2).map(move |value| (coordinate, value)))
                .filter(|facet| !distinct_facets.contains(facet))
                .collect();
            assert_eq!(missing.len(), 2);
            assert_eq!(missing[0].0, missing[1].0);
            assert_ne!(missing[0].1, missing[1].1);

            if current == [edge(0, 3), edge(0, 5)] {
                representative_charts = charts
                    .iter()
                    .map(|&(kind, plus, facet)| (kind, plus, facet, outward_facet(facet).1))
                    .collect();
                representative_caps = missing.clone();
            }

            for &(_, _, facet) in &charts {
                cellular_map_checks += check_facet_chain_map(facet);
                *chart_facets_on_four_core.entry(facet).or_default() += 1;
            }

            let belt_facets: Vec<_> = distinct_facets.iter().copied().collect();
            let cap_facets = missing;
            let belt = selected_complex(&belt_facets, false);
            let one_cap = selected_complex(
                &belt_facets
                    .iter()
                    .copied()
                    .chain([cap_facets[0]])
                    .collect::<Vec<_>>(),
                false,
            );
            let sphere = selected_complex(
                &belt_facets
                    .iter()
                    .copied()
                    .chain(cap_facets.iter().copied())
                    .collect::<Vec<_>>(),
                false,
            );
            let cube = selected_complex(
                &belt_facets
                    .iter()
                    .copied()
                    .chain(cap_facets.iter().copied())
                    .collect::<Vec<_>>(),
                true,
            );
            assert_eq!(homology(&belt), ([8, 12, 4, 0], [1, 1, 0, 0]));
            assert_eq!(homology(&one_cap), ([8, 12, 5, 0], [1, 0, 0, 0]));
            assert_eq!(homology(&sphere), ([8, 12, 6, 0], [1, 0, 1, 0]));
            assert_eq!(homology(&cube), ([8, 12, 6, 1], [1, 0, 0, 0]));

            let mut belt_chain = Chain::new();
            for facet in &belt_facets {
                let (cell, coefficient) = outward_facet(*facet);
                add_term(&mut belt_chain, cell, coefficient);
            }
            let mut cap_chain = Chain::new();
            for facet in &cap_facets {
                let (cell, coefficient) = outward_facet(*facet);
                add_term(&mut cap_chain, cell, coefficient);
            }
            let sphere_chain: Chain = belt_chain
                .iter()
                .chain(cap_chain.iter())
                .map(|(&cell, &coefficient)| (cell, coefficient))
                .collect();
            let cube_cell = CubeCell([STAR; 3]);
            let cube_boundary = chain_boundary(&BTreeMap::from([(cube_cell, 1)]));
            assert_eq!(sphere_chain, cube_boundary);
            assert_eq!(chain_boundary(&belt_chain), {
                let mut value = chain_boundary(&cap_chain);
                for coefficient in value.values_mut() {
                    *coefficient = -*coefficient;
                }
                value
            });
            assert!(chain_boundary(&belt_chain).len() == 8);
            assert!(chain_boundary(&sphere_chain).is_empty());
            four_chart_cores += 1;
        } else {
            assert_eq!(charts.len(), 2);
            assert_eq!(kinds, BTreeMap::from([(FaceKind::Square, 2)]));
            two_chart_cores += 1;
        }
        *chart_type_profile
            .entry((charts.len(), distinct_facets.len()))
            .or_default() += 1;
    }

    assert_eq!(fixed_core_vertices, 12 * 8);
    assert_eq!(face_poset_cells, 12 * 27);
    assert_eq!((four_chart_cores, two_chart_cores), (8, 4));
    assert_eq!(
        chart_type_profile,
        BTreeMap::from([((2, 2), 4), ((4, 4), 8)])
    );
    assert_eq!(cellular_map_checks, 8 * 4 * 9);
    assert_eq!(chart_facets_on_four_core.values().sum::<usize>(), 32);

    // Support alone does not select the route-to-facet chain map. Even after
    // requiring a surjective cellular map on vertices, an oriented pentagon
    // has twenty degree +1 and twenty degree -1 lifts to a square, while a
    // square has four of each. They differ by the collapsed pentagon edge
    // and/or the cyclic target identification.
    let square_lifts = support_only_polygon_lifts(4);
    let pentagon_lifts = support_only_polygon_lifts(5);
    assert_eq!(square_lifts, BTreeMap::from([(-1, 4), (1, 4)]));
    assert_eq!(pentagon_lifts, BTreeMap::from([(-1, 20), (1, 20)]));
    assert_eq!(representative_charts.len(), 4);
    assert_eq!(representative_caps.len(), 2);

    println!("eight-point cubical Gysin-coherence certificate");
    println!("  all 12 physical rank-two cores are quadrangulations");
    println!(
        "  fixed-core associahedral fibers: 12 honest I^3 faces, 96 vertices, 324 face-poset cells"
    );
    println!("  supported chart profile (images, distinct facets): {chart_type_profile:?}");
    println!("  8 pentagon/square cores: P+,P-,S+,S- are four distinct side facets");
    println!(
        "  4 square/square cores: only two established supported facets, not a four-chart belt"
    );
    println!(
        "  representative Q={{03,05}} charts (kind,plus,facet,outward sign): {representative_charts:?}"
    );
    println!("  representative missing opposite caps: {representative_caps:?}; cube cell=(*,*,*)");
    println!("  target-facet inclusion checks on the eight belts: {cellular_map_checks}");
    println!(
        "  support-only route-to-square chain lifts: square {square_lifts:?}, pentagon {pentagon_lifts:?}"
    );
    println!("  belt: cells (8,12,4), H=(Z,Z,0,0)");
    println!("  one-capped belt: cells (8,12,5), H=(Z,0,0,0)");
    println!("  boundary sphere: cells (8,12,6), H=(Z,0,Z,0)");
    println!("  filled cube: cells (8,12,6,1), H=(Z,0,0,0)");
    println!("  signed identity: d(belt)=-d(two caps), belt+caps=d(cube)");
    println!();
    println!("VERDICT: CONDITIONAL / CHAIN-MAP QUESTION REMAINS UNTYPED");
    println!("  every core has an exact cube, but only 8/12 carry the four-chart belt");
    println!("  occurrence supports extend to cellular target-facet inclusions");
    println!("  no route-edge/2-cell Gysin map is supplied, so pentagon-to-square chain naturality is untested");
    println!(
        "  caps/cube make the target boundary discrepancy exact, conditionally on such a lift"
    );
    println!("  no finite-alpha-prime residue or Pochhammer chain map is certified");
}
