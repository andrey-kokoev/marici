//! Exact occurrence-support cosheaf and four-chart geometry audit at eight points.
//!
//! The combinatorial engine mirrors `check_pentagon_incidence_span.rs`.
//! This certificate adds two tests: the diagonal-occurrence module on every
//! route face is the direct sum of extension-by-zero rank-one cosheaves, and
//! the four physical images are coordinate facets of the full-core cube but
//! do not geometrically cover that cube.

#[allow(dead_code)]
mod incidence {
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
            let second =
                expanded_occurrences(face.core, plus, marks[0], [face.core[1], face.core[0]]);
            assert_eq!(first, second);
            result.push(first);
        }
        result
    }

    fn difference(first: &[Edge], second: &[Edge]) -> Vec<Edge> {
        first
            .iter()
            .copied()
            .filter(|edge| !second.contains(edge))
            .collect()
    }

    fn cyclic_equal(first: &[Edge], second: &[Edge]) -> bool {
        if first.len() != second.len() {
            return false;
        }
        (0..first.len()).any(|shift| {
            (0..first.len()).all(|index| first[index] == second[(index + shift) % second.len()])
        })
    }

    fn cyclic_equal_up_to_reversal(first: &[Edge], second: &[Edge]) -> bool {
        if cyclic_equal(first, second) {
            return true;
        }
        let mut reversed = second.to_vec();
        reversed.reverse();
        cyclic_equal(first, &reversed)
    }

    fn edge_dissection(face: &RouteFace, position: usize, tris: &[Triangulation]) -> Vec<Edge> {
        let first = &tris[face.vertices[position]];
        let second = &tris[face.vertices[(position + 1) % face.vertices.len()]];
        let mut result: Vec<_> = first
            .iter()
            .copied()
            .filter(|edge| second.contains(edge))
            .collect();
        result.sort();
        result
    }

    fn audit_face_cosheaf(face: &RouteFace, tris: &[Triangulation]) -> (usize, usize) {
        let face_fiber = face.common.clone();
        assert_eq!(face_fiber.len(), 3);
        let edge_fibers: Vec<_> = (0..face.vertices.len())
            .map(|position| edge_dissection(face, position, tris))
            .collect();
        let vertex_fibers: Vec<_> = face
            .vertices
            .iter()
            .map(|&index| tris[index].clone())
            .collect();
        assert!(edge_fibers.iter().all(|fiber| fiber.len() == 4));
        assert!(vertex_fibers.iter().all(|fiber| fiber.len() == 5));

        // These are all generating specializations of the cellular cosheaf:
        // 2-cell -> boundary edge -> boundary vertex.  Each is the canonical
        // coordinate inclusion on labels, and the two composites from the
        // face to any vertex agree.
        let mut specialization_maps = 0;
        for position in 0..face.vertices.len() {
            let next = (position + 1) % face.vertices.len();
            assert!(face_fiber
                .iter()
                .all(|label| edge_fibers[position].contains(label)));
            assert!(edge_fibers[position]
                .iter()
                .all(|label| vertex_fibers[position].contains(label)));
            assert!(edge_fibers[position]
                .iter()
                .all(|label| vertex_fibers[next].contains(label)));
            let previous = (position + face.vertices.len() - 1) % face.vertices.len();
            for label in &face_fiber {
                assert!(edge_fibers[previous].contains(label));
                assert!(edge_fibers[position].contains(label));
                assert!(vertex_fibers[position].contains(label));
            }
            specialization_maps += 3;
        }

        // Decompose the complete module as a direct sum over diagonal labels.
        // A common label is supported on the whole polygonal face.  Every
        // other label is supported on exactly one closed boundary edge.
        let universe: BTreeSet<_> = vertex_fibers.iter().flatten().copied().collect();
        assert_eq!(universe.len(), 3 + face.vertices.len());
        let mut whole_face_supports = 0;
        let mut closed_edge_supports = 0;
        for label in universe {
            let on_face = face_fiber.contains(&label);
            let supported_edges: Vec<_> = edge_fibers
                .iter()
                .enumerate()
                .filter_map(|(index, fiber)| fiber.contains(&label).then_some(index))
                .collect();
            let supported_vertices: Vec<_> = vertex_fibers
                .iter()
                .enumerate()
                .filter_map(|(index, fiber)| fiber.contains(&label).then_some(index))
                .collect();
            if on_face {
                assert_eq!(supported_edges.len(), face.vertices.len());
                assert_eq!(supported_vertices.len(), face.vertices.len());
                whole_face_supports += 1;
            } else {
                assert_eq!(supported_edges.len(), 1);
                let edge_index = supported_edges[0];
                let mut expected = vec![edge_index, (edge_index + 1) % face.vertices.len()];
                expected.sort_unstable();
                assert_eq!(supported_vertices, expected);
                closed_edge_supports += 1;
            }
        }
        assert_eq!(whole_face_supports, 3);
        assert_eq!(closed_edge_supports, face.vertices.len());
        (
            specialization_maps,
            whole_face_supports + closed_edge_supports,
        )
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
            let slots = cell_slots(cell);
            let slot = slots
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
        panic!("rank-four physical image is not a coordinate facet")
    }

    fn cube_cell_census(charts: &[(usize, usize)]) -> (usize, usize, usize, usize) {
        assert_eq!(charts.len(), 4);
        let selected: BTreeSet<_> = charts.iter().copied().collect();
        assert_eq!(selected.len(), 4);

        // Cubical cells are words in {0,1,*}^3.  A cell belongs to the union
        // of selected facets iff at least one fixed coordinate matches one of
        // the selected coordinate/value pairs.
        let mut covered = [0_usize; 4];
        let mut total = [0_usize; 4];
        for code in 0..27 {
            let mut work = code;
            let mut word = [0_usize; 3];
            let mut dimension = 0;
            for entry in &mut word {
                *entry = work % 3;
                work /= 3;
                dimension += usize::from(*entry == 2);
            }
            total[dimension] += 1;
            let belongs = charts
                .iter()
                .any(|&(coordinate, value)| word[coordinate] == value);
            covered[dimension] += usize::from(belongs);
        }
        assert_eq!(total, [8, 12, 6, 1]);
        assert_eq!(covered, [8, 12, 4, 0]);
        (covered[0], covered[1], covered[2], covered[3])
    }

    pub(super) fn run() {
        let tris = triangulations();
        assert_eq!(tris.len(), 132);
        let faces = route_faces(&tris);
        assert_eq!(faces.len(), 24);

        let representative_common = vec![edge(1, 3), edge(3, 5), edge(5, 7)];
        let representative_facets =
            vec![edge(1, 7), edge(3, 7), edge(0, 3), edge(0, 5), edge(1, 5)];
        let mut representative_seen = false;
        let mut pentagons = 0;
        let mut squares = 0;
        let mut specialization_maps = 0;
        let mut support_summands = 0;
        for face in &faces {
            let (maps, summands) = audit_face_cosheaf(face, &tris);
            specialization_maps += maps;
            support_summands += summands;
            match face.kind {
                FaceKind::Pentagon => pentagons += 1,
                FaceKind::Square => squares += 1,
            }
            if face.common == representative_common {
                assert_eq!(face.kind, FaceKind::Pentagon);
                let facets: Vec<_> = (0..face.vertices.len())
                    .map(|position| {
                        let current = edge_dissection(face, position, &tris);
                        let extra = difference(&current, &face.common);
                        assert_eq!(extra.len(), 1);
                        extra[0]
                    })
                    .collect();
                assert!(cyclic_equal_up_to_reversal(&facets, &representative_facets));
                let actual_vertices: BTreeSet<_> = face
                    .vertices
                    .iter()
                    .map(|&index| tris[index].clone())
                    .collect();
                let expected_vertices: BTreeSet<_> = [
                    vec![edge(1, 3), edge(1, 5), edge(1, 7), edge(3, 5), edge(5, 7)],
                    vec![edge(1, 3), edge(1, 7), edge(3, 5), edge(3, 7), edge(5, 7)],
                    vec![edge(0, 3), edge(1, 3), edge(3, 5), edge(3, 7), edge(5, 7)],
                    vec![edge(0, 3), edge(0, 5), edge(1, 3), edge(3, 5), edge(5, 7)],
                    vec![edge(0, 5), edge(1, 3), edge(1, 5), edge(3, 5), edge(5, 7)],
                ]
                .into_iter()
                .map(|mut vertex| {
                    vertex.sort();
                    vertex
                })
                .collect();
                assert_eq!(actual_vertices, expected_vertices);
                representative_seen = true;
            }
        }
        assert!(representative_seen);
        assert_eq!((pentagons, squares), (8, 16));
        assert_eq!(specialization_maps, 8 * 15 + 16 * 12);
        assert_eq!(support_summands, 8 * 8 + 16 * 7);

        let mut images = BTreeMap::<([Edge; 2], usize), [BTreeSet<Occurrence>; 2]>::new();
        for face in &faces {
            let supported = supported_images(face);
            if supported.len() == 2 {
                images.insert((face.core, face.sheet), supported.try_into().unwrap());
            }
        }
        assert_eq!(images.len(), 16);

        let mut cube_audits = 0;
        for pentagon in faces.iter().filter(|face| face.kind == FaceKind::Pentagon) {
            let square = faces
                .iter()
                .find(|face| {
                    face.core == pentagon.core
                        && face.sheet != pentagon.sheet
                        && face.kind == FaceKind::Square
                })
                .expect("opposite-sheet companion square");
            let pentagon_images = &images[&(pentagon.core, pentagon.sheet)];
            let square_images = &images[&(square.core, square.sheet)];
            let charts = [
                coordinate_facet(pentagon.core, &pentagon_images[0]),
                coordinate_facet(pentagon.core, &pentagon_images[1]),
                coordinate_facet(pentagon.core, &square_images[0]),
                coordinate_facet(pentagon.core, &square_images[1]),
            ];
            assert_eq!(cube_cell_census(&charts), (8, 12, 4, 0));

            let missing: BTreeSet<_> = (0..3)
                .flat_map(|coordinate| (0..2).map(move |value| (coordinate, value)))
                .filter(|facet| !charts.contains(facet))
                .collect();
            assert_eq!(missing.len(), 2);
            let missing: Vec<_> = missing.into_iter().collect();
            assert_eq!(missing[0].0, missing[1].0);
            assert_ne!(missing[0].1, missing[1].1);
            cube_audits += 1;
        }
        assert_eq!(cube_audits, 8);

        println!("eight-point occurrence-support cosheaf certificate");
        println!("  route faces: {pentagons} pentagons + {squares} squares");
        println!("  fibers on every face/edge/vertex: ranks 3/4/5");
        println!("  generating cellular specialization maps checked: {specialization_maps}");
        println!("  extension-by-zero diagonal summands checked: {support_summands}");
        println!("  representative C={{13,35,57}}, facets cyclically {{17,37,03,05,15}}");
        println!("  four physical charts: four literal coordinate square facets on {cube_audits}/8 cubes");
        println!("  chart union cell census (C0,C1,C2,C3)=(8,12,4,0), not (8,12,6,1)");
        println!("  missing geometry: two opposite cap squares and the cube 3-cell");
        println!("  belt homotopy: S^1 x I; caps give two null-homotopies, cube compares them");
        println!();
        println!("VERDICT: PROVED WITH GEOMETRIC QUALIFICATION");
        println!("  the diagonal coefficient system is the claimed constructible cosheaf");
        println!("  the four-chart Cech sequence covers the rank-eight vertex module only");
    }
}

fn main() {
    incidence::run();
}
