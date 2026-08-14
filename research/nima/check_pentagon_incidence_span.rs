//! Exact incidence-span certificate for the eight nontransverse octagon pentagons.
//!
//! This checker does not construct a loaded Pochhammer/Cousin current.  It
//! proves the underlying occurrence theorem which such a lift must realize:
//! the scalar edge is a constructible rank-four common-label span, its two
//! exchanged rank-one endpoint quotients are absent from every supported
//! double-Gysin source, and the supported face images satisfy exact basis
//! Cech descent.  No edge isomorphism between the endpoint modules is used.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

const N: usize = 8;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge(usize, usize);

type Cell = Vec<usize>;
type Triangulation = Vec<Edge>;

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Occurrence(Vec<(Cell, Edge)>);

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
        let kind = match vertices.len() {
            4 => FaceKind::Square,
            5 => FaceKind::Pentagon,
            _ => unreachable!(),
        };
        result.push(RouteFace {
            vertices: cyclic_order(&vertices, tris),
            common,
            core: [current[0], current[1]],
            sheet: *sheets.iter().next().unwrap(),
            kind,
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
    let mut cut = BTreeSet::new();
    for diagonal in order {
        cut.insert(diagonal);
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
    assert_eq!(cut.len(), 2);
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
    assert_eq!(result.len(), 8);
    result
}

fn supported_images(face: &RouteFace) -> Vec<BTreeSet<Occurrence>> {
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
        result.push(first);
    }
    result
}

fn scalar_exchange(face: &RouteFace, tris: &[Triangulation]) -> (Edge, Edge) {
    assert_eq!(face.kind, FaceKind::Pentagon);
    for position in 0..face.vertices.len() {
        let first = &tris[face.vertices[position]];
        let second = &tris[face.vertices[(position + 1) % face.vertices.len()]];
        if core(first).is_empty() && core(second).is_empty() {
            let removed: Vec<_> = first
                .iter()
                .copied()
                .filter(|diagonal| !second.contains(diagonal))
                .collect();
            let inserted: Vec<_> = second
                .iter()
                .copied()
                .filter(|diagonal| !first.contains(diagonal))
                .collect();
            assert_eq!((removed.len(), inserted.len()), (1, 1));
            return (removed[0], inserted[0]);
        }
    }
    panic!("pentagon has no same-core scalar edge")
}

fn scalar_endpoints<'a>(
    face: &RouteFace,
    tris: &'a [Triangulation],
) -> (&'a Triangulation, &'a Triangulation) {
    let endpoints: Vec<_> = face
        .vertices
        .iter()
        .map(|&index| &tris[index])
        .filter(|triangulation| core(triangulation).is_empty())
        .collect();
    assert_eq!(endpoints.len(), 2);
    (endpoints[0], endpoints[1])
}

fn weight_telescope(face: &RouteFace, tris: &[Triangulation]) {
    let mut total = BTreeMap::<Edge, i64>::new();
    for position in 0..face.vertices.len() {
        let first = &tris[face.vertices[position]];
        let second = &tris[face.vertices[(position + 1) % face.vertices.len()]];
        let removed = *first.iter().find(|edge| !second.contains(edge)).unwrap();
        let inserted = *second.iter().find(|edge| !first.contains(edge)).unwrap();
        // w(T)=-sum X_d, hence w(T')-w(T)=X_removed-X_inserted.
        *total.entry(removed).or_default() += 1;
        *total.entry(inserted).or_default() -= 1;
    }
    assert!(total.values().all(|coefficient| *coefficient == 0));
}

fn rotate_cell(cell: &Cell) -> Cell {
    let mut result: Vec<_> = cell.iter().map(|vertex| (vertex + 1) % N).collect();
    result.sort_unstable();
    result
}

fn rotate_occurrence(occurrence: &Occurrence) -> Occurrence {
    let mut marks: Vec<_> = occurrence
        .0
        .iter()
        .map(|(cell, mark)| (rotate_cell(cell), rotate_edge(*mark)))
        .collect();
    marks.sort();
    Occurrence(marks)
}

fn cech_exact(
    first: &BTreeSet<Occurrence>,
    second: &BTreeSet<Occurrence>,
    intersection_rank: usize,
    union_rank: usize,
) {
    let intersection: BTreeSet<_> = first.intersection(second).cloned().collect();
    let union: BTreeSet<_> = first.union(second).cloned().collect();
    assert_eq!(intersection.len(), intersection_rank);
    assert_eq!(union.len(), union_rank);
    assert_eq!(first.len() + second.len(), intersection.len() + union.len());

    // For 0 -> R^I -> R^A + R^B -> R^U -> 0, use
    // z |-> (z,-z) and (a,b) |-> a+b.
    let first_basis: Vec<_> = first.iter().cloned().collect();
    let second_basis: Vec<_> = second.iter().cloned().collect();
    let intersection_basis: Vec<_> = intersection.iter().cloned().collect();
    let union_basis: Vec<_> = union.iter().cloned().collect();
    let first_index: BTreeMap<_, _> = first_basis
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, basis)| (basis, index))
        .collect();
    let second_index: BTreeMap<_, _> = second_basis
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, basis)| (basis, index))
        .collect();
    let union_index: BTreeMap<_, _> = union_basis
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, basis)| (basis, index))
        .collect();

    let middle_rank = first.len() + second.len();
    let mut inclusion = vec![vec![0_i64; intersection.len()]; middle_rank];
    for (column, occurrence) in intersection_basis.iter().enumerate() {
        inclusion[first_index[occurrence]][column] = 1;
        inclusion[first.len() + second_index[occurrence]][column] = -1;
    }
    let mut projection = vec![vec![0_i64; middle_rank]; union.len()];
    for (column, occurrence) in first_basis.iter().enumerate() {
        projection[union_index[occurrence]][column] = 1;
    }
    for (offset, occurrence) in second_basis.iter().enumerate() {
        projection[union_index[occurrence]][first.len() + offset] = 1;
    }

    for row in 0..union.len() {
        for column in 0..intersection.len() {
            let composite: i64 = (0..middle_rank)
                .map(|middle| projection[row][middle] * inclusion[middle][column])
                .sum();
            assert_eq!(composite, 0);
        }
    }

    // Exact unit minors certify the ranks and that every nonzero Smith
    // invariant of both incidence maps is 1.
    for (column, occurrence) in intersection_basis.iter().enumerate() {
        let pivot_row = first_index[occurrence];
        for other_column in 0..intersection.len() {
            assert_eq!(
                inclusion[pivot_row][other_column],
                i64::from(other_column == column)
            );
        }
    }
    for (row, occurrence) in union_basis.iter().enumerate() {
        let pivot_column = if let Some(&column) = first_index.get(occurrence) {
            column
        } else {
            first.len() + second_index[occurrence]
        };
        for other_row in 0..union.len() {
            assert_eq!(
                projection[other_row][pivot_column],
                i64::from(other_row == row)
            );
        }
    }
    assert_eq!(middle_rank - union.len(), intersection.len());
}

fn main() {
    let tris = triangulations();
    assert_eq!(tris.len(), 132);
    assert_eq!(two_faces(&tris).len(), 300);
    let faces = route_faces(&tris);
    assert_eq!(faces.len(), 24);
    assert_eq!(
        faces
            .iter()
            .filter(|face| face.kind == FaceKind::Pentagon)
            .count(),
        8
    );
    assert_eq!(
        faces
            .iter()
            .filter(|face| face.kind == FaceKind::Square)
            .count(),
        16
    );

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
            (vertices, index)
        })
        .collect();

    let mut images = BTreeMap::<([Edge; 2], usize), [BTreeSet<Occurrence>; 2]>::new();
    let mut two_polarity_faces = 0;
    for face in &faces {
        let supported = supported_images(face);
        if supported.len() == 2 {
            cech_exact(&supported[0], &supported[1], 2, 6);
            assert!(supported[0]
                .union(&supported[1])
                .all(|occurrence| full_occurrences(face.core).contains(occurrence)));
            images.insert((face.core, face.sheet), supported.try_into().unwrap());
            two_polarity_faces += 1;
        }
    }
    assert_eq!(two_polarity_faces, 16);

    let pentagons: Vec<_> = faces
        .iter()
        .filter(|face| face.kind == FaceKind::Pentagon)
        .collect();
    let mut endpoint_lines = 0;
    let mut unsupported_exchanged_sources = 0;
    let mut deck_orbit = BTreeSet::new();
    let mut current_face = {
        let face = pentagons[0];
        let mut vertices = face.vertices.clone();
        vertices.sort_unstable();
        face_index[&vertices]
    };

    for _ in 0..8 {
        assert!(deck_orbit.insert(current_face));
        let face = &faces[current_face];
        assert_eq!(face.kind, FaceKind::Pentagon);
        weight_telescope(face, &tris);
        let (removed, inserted) = scalar_exchange(face, &tris);
        let (left, right) = scalar_endpoints(face, &tris);
        let common: BTreeSet<_> = left
            .iter()
            .copied()
            .filter(|diagonal| right.contains(diagonal))
            .collect();
        assert_eq!((left.len(), right.len(), common.len()), (5, 5, 4));
        assert!(!common.contains(&removed) && !common.contains(&inserted));
        endpoint_lines += left.len() + right.len();

        for plus in [true, false] {
            let directions = directed_edges(face.core, plus);
            let cells = core_regions(&face.core);
            let sinks = forest_sinks(&cells, &directions, &BTreeSet::new());
            assert_eq!(sinks.len(), 1);
            let sink_slots = cell_slots(&sinks[0]);
            assert!(!sink_slots.contains(&removed));
            assert!(!sink_slots.contains(&inserted));
            let supported: Vec<_> = sink_slots
                .into_iter()
                .filter(|mark| face.common.contains(mark))
                .collect();
            assert_eq!(supported.len(), 1);
            assert!(common.contains(&supported[0]));
            unsupported_exchanged_sources += 1;
        }

        let rotated_vertices = {
            let mut vertices: Vec<_> = face
                .vertices
                .iter()
                .map(|&index| tri_index[&rotate_triangulation(&tris[index])])
                .collect();
            vertices.sort_unstable();
            vertices
        };
        let next_face = face_index[&rotated_vertices];
        let next = &faces[next_face];
        assert_eq!(next.kind, FaceKind::Pentagon);
        assert_eq!(next.sheet, 1 - face.sheet);
        assert_eq!(
            (rotate_edge(removed), rotate_edge(inserted)),
            scalar_exchange(next, &tris)
        );
        let rotated_images: [BTreeSet<_>; 2] = images[&(face.core, face.sheet)]
            .iter()
            .map(|set| set.iter().map(rotate_occurrence).collect())
            .collect::<Vec<_>>()
            .try_into()
            .unwrap();
        let next_images = &images[&(next.core, next.sheet)];
        assert_eq!(
            rotated_images,
            [next_images[1].clone(), next_images[0].clone()]
        );
        current_face = next_face;
    }
    assert_eq!(deck_orbit.len(), 8);
    assert_eq!(endpoint_lines, 8 * 2 * 5);
    assert_eq!(unsupported_exchanged_sources, 8 * 2);

    let mut assembly_checks = 0;
    for pentagon in pentagons {
        let companion = faces
            .iter()
            .find(|face| {
                face.core == pentagon.core
                    && face.sheet != pentagon.sheet
                    && face.kind == FaceKind::Square
            })
            .expect("opposite-sheet companion square");
        let pentagon_sets = &images[&(pentagon.core, pentagon.sheet)];
        let square_sets = &images[&(companion.core, companion.sheet)];
        let pentagon_union: BTreeSet<_> =
            pentagon_sets[0].union(&pentagon_sets[1]).cloned().collect();
        let square_union: BTreeSet<_> = square_sets[0].union(&square_sets[1]).cloned().collect();
        cech_exact(&pentagon_union, &square_union, 4, 8);
        let cross = [
            pentagon_sets[0].intersection(&square_sets[0]).count(),
            pentagon_sets[0].intersection(&square_sets[1]).count(),
            pentagon_sets[1].intersection(&square_sets[0]).count(),
            pentagon_sets[1].intersection(&square_sets[1]).count(),
        ];
        assert_eq!(cross, [0, 2, 2, 0]);
        assert_eq!(
            pentagon_union
                .union(&square_union)
                .cloned()
                .collect::<BTreeSet<_>>(),
            full_occurrences(pentagon.core)
        );
        assembly_checks += 1;
    }
    assert_eq!(assembly_checks, 8);

    println!("eight-point pentagon incidence-span certificate");
    println!("  associahedron: 132 triangulations, 300 two-faces");
    println!("  route faces: 16 squares + 8 pentagons; pentagons form one deck orbit");
    println!(
        "  scalar endpoints: rank 5 <- rank 4 common span -> rank 5; exchanged quotients rank 1+1"
    );
    println!("  flip differential: d h_s = X_x-X_y with w(T)=-sum_d X_d; deck covariant and 8/8 facewise telescoping");
    println!("  exchanged x,y absent from all {unsupported_exchanged_sources} supported double-Gysin sources");
    println!("  D/E and E/D occurrence expansions agree on every supported source");
    println!("  within-face Cech: 0 -> R^2 -> R^4+R^4 -> R^6 -> 0, {two_polarity_faces}/16 supported two-polarity faces");
    println!("  pentagon/square Cech: 0 -> R^4 -> R^6+R^6 -> R^8 -> 0, {assembly_checks}/8 cores");
    println!("  all displayed incidence maps are saturated with nonzero Smith factors equal to 1");
    println!();
    println!("VERDICT: PROVED (COMBINATORIAL/OCCURRENCE SCOPE)");
    println!("  no endpoint isomorphism tau and no QTDS sign fitting is used");
    println!("  a loaded Pochhammer/Cousin realization is not claimed");
}
