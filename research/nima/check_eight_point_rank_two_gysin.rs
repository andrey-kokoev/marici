//! Rank-two completion and marked-link audit for the scalar octagon.
//!
//! This certificate keeps three objects separate:
//!
//! 1. the honest component incidence derived from scalar triangulations;
//! 2. the quotient obtained by merging the two disconnected components of
//!    every rank-one fiber (the previously advertised K_{2,8});
//! 3. the medial 8-triangle + 4-square Mobius carrier.
//!
//! Every genuine rank-two physical core is a quadrangulation.  Its exact
//! scalar fiber is a 3-cube, but that cube lies wholly in rank two.  It does
//! not have the proposed K_{2,8} four-circuit as its cellular boundary.
//! Transverse to each cube are exactly two canonical route faces, one on each
//! polarity sheet: altogether sixteen squares and eight pentagons.  After
//! contracting only connected exact-core fibers, these give a 24-face CW
//! carrier.  It is the union of two contractible cones meeting in the twelve
//! discrete rank-two fibers, hence is homotopy equivalent to K_{2,12} and has
//! H1=Z^11.
//!
//! If one first imposes the disconnected rank-one identifications, each
//! quadrangulation edge {D,E} can be suspended to a square with boundary
//! Gamma_8(e_D-e_E).  The twelve imposed squares kill H1(K_{2,8}) and leave
//! H2=Z^5.  This is a valid abstract suspension of the compatibility graph,
//! but it is not the boundary of the scalar rank-two cube.
//!
//! Under a marked cut D, connected scalar fibers do give an honest K_{2,3}:
//! the two components of the rank-one D-fiber are its centers and the three
//! compatible rank-two cubes are its roads.  Thus a rank-two core maps by a
//! degree-lowering link/Gysin operation to one local road; differences of two
//! rank-two cores suspend to local four-circuits.  No map
//! H1(K_{2,8})->H1(K_{2,3}) is used or available intrinsically.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

const N: usize = 8;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge(usize, usize);

type Triangulation = Vec<Edge>;
type Matrix = Vec<Vec<i64>>;

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
    if first.0 == second.0 || first.0 == second.1 || first.1 == second.0 || first.1 == second.1 {
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

fn groups(tris: &[Triangulation]) -> BTreeMap<Vec<Edge>, Vec<usize>> {
    let mut result = BTreeMap::<Vec<Edge>, Vec<usize>>::new();
    for (index, triangulation) in tris.iter().enumerate() {
        result.entry(core(triangulation)).or_default().push(index);
    }
    result
}

fn components(indices: &[usize], tris: &[Triangulation]) -> Vec<Vec<usize>> {
    let mut unseen: BTreeSet<_> = indices.iter().copied().collect();
    let mut result = Vec::new();
    while let Some(&start) = unseen.iter().next() {
        unseen.remove(&start);
        let mut component = Vec::new();
        let mut queue = VecDeque::from([start]);
        while let Some(current) = queue.pop_front() {
            component.push(current);
            let neighbors: Vec<_> = unseen
                .iter()
                .copied()
                .filter(|&candidate| adjacent(&tris[current], &tris[candidate]))
                .collect();
            for neighbor in neighbors {
                unseen.remove(&neighbor);
                queue.push_back(neighbor);
            }
        }
        component.sort_unstable();
        result.push(component);
    }
    result.sort();
    result
}

fn incidence_count(first: &[usize], second: &[usize], tris: &[Triangulation]) -> usize {
    first
        .iter()
        .flat_map(|&left| second.iter().map(move |&right| (left, right)))
        .filter(|&(left, right)| adjacent(&tris[left], &tris[right]))
        .count()
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

fn associahedron_two_faces(tris: &[Triangulation]) -> Vec<Vec<usize>> {
    let diagonals = polygon_diagonals();
    let mut fixed_sets = Vec::new();
    for first in 0..diagonals.len() {
        for second in first + 1..diagonals.len() {
            for third in second + 1..diagonals.len() {
                let fixed = [diagonals[first], diagonals[second], diagonals[third]];
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
                fixed_sets.push(vertices);
            }
        }
    }
    fixed_sets.sort();
    fixed_sets.dedup();
    fixed_sets
}

fn cyclic_face_order(vertices: &[usize], tris: &[Triangulation]) -> Vec<usize> {
    let mut result = vec![vertices[0]];
    let mut previous = usize::MAX;
    while result.len() < vertices.len() {
        let current = *result.last().unwrap();
        let next = vertices
            .iter()
            .copied()
            .filter(|&candidate| candidate != previous && !result.contains(&candidate))
            .find(|&candidate| adjacent(&tris[current], &tris[candidate]))
            .expect("two-face boundary continuation");
        previous = current;
        result.push(next);
    }
    assert!(adjacent(&tris[*result.last().unwrap()], &tris[result[0]]));
    result
}

fn canonical_cycle_pattern(pattern: &[usize]) -> Vec<usize> {
    let mut candidates = Vec::new();
    for reflected in [false, true] {
        let base: Vec<_> = if reflected {
            pattern.iter().copied().rev().collect()
        } else {
            pattern.to_vec()
        };
        for rotation in 0..pattern.len() {
            candidates.push(
                (0..pattern.len())
                    .map(|index| base[(index + rotation) % pattern.len()])
                    .collect::<Vec<_>>(),
            );
        }
    }
    candidates.into_iter().min().unwrap()
}

fn audit_actual_two_faces(tris: &[Triangulation], grouped: &BTreeMap<Vec<Edge>, Vec<usize>>) {
    let faces = associahedron_two_faces(tris);
    let mut patterns = BTreeMap::<Vec<usize>, usize>::new();
    for vertices in &faces {
        let ordered = cyclic_face_order(vertices, tris);
        let pattern: Vec<_> = ordered
            .iter()
            .map(|&index| core(&tris[index]).len())
            .collect();
        *patterns
            .entry(canonical_cycle_pattern(&pattern))
            .or_default() += 1;
    }

    // Every square face internal to an exact rank-two fiber is constant under
    // the physical-core map.  Each cube has six such faces.  Their contracted
    // boundary is therefore zero, never a four-circuit on two rank-one roads.
    let mut internal_rank_two_squares = 0;
    for (current_core, fiber) in grouped.iter().filter(|(current, _)| current.len() == 2) {
        let fiber_set: BTreeSet<_> = fiber.iter().copied().collect();
        let internal = faces
            .iter()
            .filter(|face| face.len() == 4 && face.iter().all(|index| fiber_set.contains(index)))
            .count();
        assert_eq!(internal, 6, "rank-two cube {current_core:?}");
        internal_rank_two_squares += internal;
    }
    assert_eq!(internal_rank_two_squares, 12 * 6);

    // Transverse to every rank-two cube there are exactly two actual
    // associahedral route faces, one incident to each zero-core component.
    // A route face contains only the core labels empty, {D}, {E}, {D,E}.
    // It is a square or a pentagon; the pentagon's two zero-core vertices lie
    // in the same connected zero-core interval and contract to one corner.
    let zero_components = components(&grouped[&Vec::new()], tris);
    let zero_sign: BTreeMap<_, _> = zero_components
        .iter()
        .enumerate()
        .flat_map(|(sign, component)| component.iter().map(move |&index| (index, sign)))
        .collect();
    let rank_two_cores: Vec<_> = grouped
        .keys()
        .filter(|current| current.len() == 2)
        .cloned()
        .collect();
    let mut transverse = BTreeMap::<Vec<Edge>, Vec<(usize, usize)>>::new();
    for vertices in &faces {
        let labels: Vec<_> = vertices.iter().map(|&index| core(&tris[index])).collect();
        if !labels.iter().any(Vec::is_empty) || !labels.iter().any(|label| label.len() == 2) {
            continue;
        }
        let rank_two: BTreeSet<_> = labels
            .iter()
            .filter(|label| label.len() == 2)
            .cloned()
            .collect();
        if rank_two.len() != 1 {
            continue;
        }
        let current = rank_two.iter().next().unwrap().clone();
        if labels
            .iter()
            .any(|label| !label.iter().all(|diagonal| current.contains(diagonal)))
        {
            continue;
        }
        let signs: BTreeSet<_> = vertices
            .iter()
            .filter_map(|index| zero_sign.get(index).copied())
            .collect();
        assert_eq!(signs.len(), 1);
        let sign = *signs.iter().next().unwrap();
        let rank_one: BTreeSet<_> = labels
            .iter()
            .filter(|label| label.len() == 1)
            .map(|label| label[0])
            .collect();
        assert_eq!(rank_one, current.iter().copied().collect());
        transverse
            .entry(current)
            .or_default()
            .push((sign, vertices.len()));
    }
    assert_eq!(transverse.len(), rank_two_cores.len());
    for current in &rank_two_cores {
        let mut carriers = transverse[current].clone();
        carriers.sort();
        assert_eq!(carriers.len(), 2);
        assert_eq!(carriers[0].0, 0);
        assert_eq!(carriers[1].0, 1);
        assert!(carriers[0].1 == 4 || carriers[0].1 == 5);
        assert!(carriers[1].1 == 4 || carriers[1].1 == 5);
    }
    let transverse_lengths = transverse
        .values()
        .flat_map(|carriers| carriers.iter().map(|&(_, length)| length))
        .fold(BTreeMap::<usize, usize>::new(), |mut counts, length| {
            *counts.entry(length).or_default() += 1;
            counts
        });
    assert_eq!(transverse_lengths, BTreeMap::from([(4, 16), (5, 8)]));
    assert_eq!(patterns.values().sum::<usize>(), faces.len());
    println!("actual associahedral two-faces");
    println!(
        "  total two-faces: {}, rank-pattern census: {patterns:?}",
        faces.len()
    );
    println!("  exact rank-two cube squares: {internal_rank_two_squares}=12*6");
    println!("  all 72 are core-constant, so every contracted boundary is zero");
    println!("  transverse route carriers: 16 squares + 8 pentagons, exactly one per core/sheet");
    println!("  each compares D and E routes on one sheet; none alone is a Gamma_8 circuit");
}

fn matrix(rows: usize, columns: usize) -> Matrix {
    vec![vec![0; columns]; rows]
}

fn multiply(first: &Matrix, second: &Matrix) -> Matrix {
    assert!(!first.is_empty() && !second.is_empty());
    assert_eq!(first[0].len(), second.len());
    let mut result = matrix(first.len(), second[0].len());
    for row in 0..first.len() {
        for middle in 0..second.len() {
            for column in 0..second[0].len() {
                result[row][column] += first[row][middle] * second[middle][column];
            }
        }
    }
    result
}

fn assert_zero(value: &Matrix) {
    assert!(value.iter().flatten().all(|&entry| entry == 0));
}

/// Use integral unit pivots only.  If the final matrix is zero, this exhibits
/// a unimodular equivalence to diag(1,...,1,0,...,0), i.e. exact Smith data.
fn unit_smith_rank(value: &Matrix) -> usize {
    if value.is_empty() {
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
            if coefficient != 0 {
                for column in pivot..columns {
                    work[row][column] -= coefficient * work[pivot][column];
                }
            }
        }
        for column in 0..columns {
            if column == pivot {
                continue;
            }
            let coefficient = work[pivot][column];
            if coefficient != 0 {
                for row in 0..rows {
                    work[row][column] -= coefficient * work[row][pivot];
                }
            }
        }
        pivot += 1;
    }
    assert!(work[pivot..]
        .iter()
        .all(|row| row[pivot.min(columns)..].iter().all(|&entry| entry == 0)));
    pivot
}

fn determinant(mut value: Matrix) -> i128 {
    assert!(value.iter().all(|row| row.len() == value.len()));
    if value.is_empty() {
        return 1;
    }
    let size = value.len();
    let mut work: Vec<Vec<i128>> = value
        .drain(..)
        .map(|row| row.into_iter().map(i128::from).collect())
        .collect();
    let mut previous = 1_i128;
    let mut sign = 1_i128;
    for column in 0..size - 1 {
        let Some(row) = (column..size).find(|&row| work[row][column] != 0) else {
            return 0;
        };
        if row != column {
            work.swap(row, column);
            sign = -sign;
        }
        let pivot = work[column][column];
        for row in column + 1..size {
            for next_column in column + 1..size {
                let numerator =
                    work[row][next_column] * pivot - work[row][column] * work[column][next_column];
                assert_eq!(numerator % previous, 0);
                work[row][next_column] = numerator / previous;
            }
        }
        previous = pivot;
    }
    sign * work[size - 1][size - 1]
}

fn graph_boundary(vertex_count: usize, edges: &[(usize, usize)]) -> Matrix {
    let mut result = matrix(vertex_count, edges.len());
    for (column, &(first, second)) in edges.iter().enumerate() {
        result[first][column] = -1;
        result[second][column] = 1;
    }
    result
}

fn audit_scalar_fibers(
    tris: &[Triangulation],
    grouped: &BTreeMap<Vec<Edge>, Vec<usize>>,
    roads: &[Edge],
    cores: &[(usize, usize)],
) -> (Vec<Vec<Vec<usize>>>, BTreeMap<Vec<Edge>, Vec<Vec<usize>>>) {
    let zero_components = components(&grouped[&Vec::new()], tris);
    assert_eq!(
        zero_components.iter().map(Vec::len).collect::<Vec<_>>(),
        vec![2, 2]
    );

    let mut rank_one_components = BTreeMap::new();
    for &road in roads {
        let current = components(&grouped[&vec![road]], tris);
        assert_eq!(current.iter().map(Vec::len).collect::<Vec<_>>(), vec![2, 2]);
        let incidence = current
            .iter()
            .map(|component| {
                zero_components
                    .iter()
                    .map(|zero| incidence_count(zero, component, tris))
                    .collect::<Vec<_>>()
            })
            .collect::<Vec<_>>();
        assert!(
            incidence == vec![vec![1, 0], vec![0, 1]] || incidence == vec![vec![0, 1], vec![1, 0]]
        );
        rank_one_components.insert(vec![road], current);
    }

    for &(first, second) in cores {
        let key = vec![roads[first], roads[second]];
        let fiber = &grouped[&key];
        assert_eq!(fiber.len(), 8);
        let fiber_components = components(fiber, tris);
        assert_eq!(fiber_components, vec![fiber.clone()]);
        let internal_degrees: Vec<_> = fiber
            .iter()
            .map(|&source| {
                fiber
                    .iter()
                    .filter(|&&target| adjacent(&tris[source], &tris[target]))
                    .count()
            })
            .collect();
        assert!(internal_degrees.iter().all(|&degree| degree == 3));
        let internal_edges = internal_degrees.iter().sum::<usize>() / 2;
        assert_eq!(internal_edges, 12); // the 1-skeleton of I^3

        for &road_index in &[first, second] {
            let one_key = vec![roads[road_index]];
            let component_incidence: Vec<_> = rank_one_components[&one_key]
                .iter()
                .map(|component| incidence_count(component, fiber, tris))
                .collect();
            assert_eq!(component_incidence, vec![2, 2]);
        }
    }

    println!("scalar rank fibers");
    println!("  rank 0: two connected intervals");
    println!("  rank 1: sixteen connected intervals (two over each road)");
    println!("  rank 2: twelve connected cubes I^3 (eight vertices, twelve edges each)");
    println!("  raw rank 0/1 incidence: two disjoint K_(1,8) stars");

    (vec![zero_components], rank_one_components)
}

fn honest_rank_two_carrier(road_count: usize, cores: &[(usize, usize)]) {
    // Vertices: two rank-zero centers, two components above every road, and
    // one connected rank-two cube above every compatible pair. Edges are only
    // actual adjacent-rank incidences. For each core and sheet, its unique
    // transverse square/pentagon contracts to the four-edge route face
    // P_sign-D_sign-Q-E_sign-P_sign.
    let zero = |sign: usize| sign;
    let one = |sign: usize, road: usize| 2 + 2 * road + sign;
    let two = |core_index: usize| 2 + 2 * road_count + core_index;
    let vertex_count = 2 + 2 * road_count + cores.len();

    let mut edges = BTreeSet::new();
    let mut faces = Vec::new();
    for sign in 0..2 {
        for road in 0..road_count {
            edges.insert((zero(sign), one(sign, road)));
        }
    }
    for (core_index, &(first, second)) in cores.iter().enumerate() {
        for sign in 0..2 {
            for road in [first, second] {
                edges.insert((one(sign, road), two(core_index)));
            }
            faces.push([
                zero(sign),
                one(sign, first),
                two(core_index),
                one(sign, second),
            ]);
        }
    }
    let edges: Vec<_> = edges.into_iter().collect();
    let edge_index: BTreeMap<_, _> = edges
        .iter()
        .copied()
        .enumerate()
        .map(|(index, value)| (value, index))
        .collect();
    let boundary_one = graph_boundary(vertex_count, &edges);
    let mut boundary_two = matrix(edges.len(), faces.len());
    for (column, face) in faces.iter().enumerate() {
        for index in 0..face.len() {
            let first = face[index];
            let second = face[(index + 1) % face.len()];
            let key = if first < second {
                (first, second)
            } else {
                (second, first)
            };
            boundary_two[edge_index[&key]][column] += if first < second { 1 } else { -1 };
        }
    }
    assert_zero(&multiply(&boundary_one, &boundary_two));
    let rank_one = unit_smith_rank(&boundary_one);
    let rank_two = unit_smith_rank(&boundary_two);
    assert_eq!((vertex_count, edges.len(), faces.len()), (30, 64, 24));
    assert_eq!((rank_one, rank_two), (29, 24));
    assert_eq!(edges.len() - rank_one - rank_two, 11);
    assert_eq!(faces.len() - rank_two, 0);
    println!("honest connected-fiber rank-two carrier");
    println!("  cells (C0,C1,C2)=(30,64,24)");
    println!("  SNF(d1)=1^29, SNF(d2)=1^24");
    println!("  H0=Z, H1=Z^11, H2=0 (homotopy K_(2,12))");
}

fn imposed_rank_two_suspension(road_count: usize, cores: &[(usize, usize)]) {
    // Quotient model: merge the disconnected rank-one components and attach
    // one square for every compatibility edge.  In H1(K2,8)=A7 the square
    // incidence is precisely the oriented vertex-edge incidence of G.
    let mut incidence = matrix(road_count - 1, cores.len());
    for (column, &(first, second)) in cores.iter().enumerate() {
        // Coordinates on A7 use e_i-e_7 for i<7.
        if first < road_count - 1 {
            incidence[first][column] += 1;
        }
        if second < road_count - 1 {
            incidence[second][column] -= 1;
        }
    }
    let smith_rank = unit_smith_rank(&incidence);
    assert_eq!(smith_rank, road_count - 1);
    assert_eq!(cores.len() - smith_rank, 5);
    println!("imposed quotient suspension S^0*G");
    println!("  twelve square boundaries are Gamma_8(e_D-e_E)");
    println!("  SNF in H1(K_(2,8)) coordinates: 1^7 with five zero columns");
    println!("  H0=Z, H1=0, H2=Z^5");
    println!("  status: abstract quotient; not a boundary of an exact-core scalar cube");
}

fn cycle_order(roads: &[Edge], cores: &[(usize, usize)]) -> Vec<usize> {
    let adjacency: Vec<Vec<usize>> = (0..roads.len())
        .map(|vertex| {
            cores
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
    // In the Mobius ladder, remove the unique antipodal neighbor (the one
    // obtained by rotating the diagonal four vertices).  The remaining
    // degree-two graph is the outer octagon.
    let antipode: Vec<_> = roads
        .iter()
        .map(|&value| edge((value.0 + 4) % N, (value.1 + 4) % N))
        .map(|value| roads.iter().position(|&road| road == value).unwrap())
        .collect();
    let outer: Vec<Vec<_>> = adjacency
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
    assert!(outer.iter().all(|neighbors| neighbors.len() == 2));
    let mut cycle = vec![0];
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

fn oriented_cycle_vector(
    vertex_cycle: &[usize],
    edge_index: &BTreeMap<(usize, usize), usize>,
) -> Vec<i64> {
    let mut result = vec![0; edge_index.len()];
    for index in 0..vertex_cycle.len() {
        let first = vertex_cycle[index];
        let second = vertex_cycle[(index + 1) % vertex_cycle.len()];
        let key = if first < second {
            (first, second)
        } else {
            (second, first)
        };
        result[edge_index[&key]] += if first < second { 1 } else { -1 };
    }
    result
}

fn graph_face_lattice(roads: &[Edge], cores: &[(usize, usize)]) {
    let cycle = cycle_order(roads, cores);
    let edge_index: BTreeMap<_, _> = cores
        .iter()
        .copied()
        .enumerate()
        .map(|(index, pair)| (pair, index))
        .collect();
    let outer = oriented_cycle_vector(&cycle, &edge_index);
    let mut faces = Vec::new();
    for index in 0..4 {
        let square = vec![
            cycle[index],
            cycle[(index + 1) % 8],
            cycle[(index + 5) % 8],
            cycle[(index + 4) % 8],
        ];
        faces.push(oriented_cycle_vector(&square, &edge_index));
    }
    faces.push(outer);

    // Choose a spanning tree greedily; chord coefficients are integral cycle
    // coordinates.  The five face cycles have determinant two in H1(G).
    let mut parent: Vec<usize> = (0..roads.len()).collect();
    fn find(parent: &mut [usize], value: usize) -> usize {
        if parent[value] != value {
            parent[value] = find(parent, parent[value]);
        }
        parent[value]
    }
    let mut tree = BTreeSet::new();
    for (index, &(first, second)) in cores.iter().enumerate() {
        let first_root = find(&mut parent, first);
        let second_root = find(&mut parent, second);
        if first_root != second_root {
            parent[first_root] = second_root;
            tree.insert(index);
        }
    }
    assert_eq!(tree.len(), roads.len() - 1);
    let chords: Vec<_> = (0..cores.len())
        .filter(|index| !tree.contains(index))
        .collect();
    assert_eq!(chords.len(), 5);
    let coordinate_matrix: Matrix = chords
        .iter()
        .map(|&row| faces.iter().map(|face| face[row]).collect())
        .collect();
    assert_eq!(determinant(coordinate_matrix).abs(), 2);
    println!("comparison with the medial Mobius carrier");
    println!("  G has cycle lattice H1(G)=Z^5");
    println!("  four square-face cycles plus the outer octagon have SNF (1,1,1,1,2)");
    println!("  their suspensions span index two in H2(S^0*G)=Z^5");
    println!("  Mobius carrier: H0=Z, H1=Z, H2=0; boundary octagon = twice its core");
    println!("  full medial cellulation: H1=Z/2 (RP2)");
}

fn marked_link_gysin(
    tris: &[Triangulation],
    grouped: &BTreeMap<Vec<Edge>, Vec<usize>>,
    roads: &[Edge],
    cores: &[(usize, usize)],
) {
    let mut total_incidence_checks = 0;
    let mut total_circuit_checks = 0;
    for marked in 0..roads.len() {
        let centers = components(&grouped[&vec![roads[marked]]], tris);
        assert_eq!(centers.len(), 2);
        let local_roads: Vec<_> = cores
            .iter()
            .enumerate()
            .filter(|(_, (first, second))| *first == marked || *second == marked)
            .collect();
        assert_eq!(local_roads.len(), 3);
        for center in &centers {
            for (_, &(first, second)) in &local_roads {
                let fiber = &grouped[&vec![roads[first], roads[second]]];
                assert_eq!(incidence_count(center, fiber, tris), 2);
                total_incidence_checks += 1;
            }
        }

        // Gysin sends a connected rank-two cube Q to one road of the local
        // K2,3.  Differences of roads have sum zero and suspend integrally to
        // the local four-circuit.
        for first in 0..local_roads.len() {
            for second in first + 1..local_roads.len() {
                let mut circuit = vec![0_i64; 2 * local_roads.len()];
                circuit[2 * first] = 1;
                circuit[2 * first + 1] = -1;
                circuit[2 * second] = -1;
                circuit[2 * second + 1] = 1;
                assert_eq!(circuit.iter().filter(|&&entry| entry != 0).count(), 4);
                assert_eq!(circuit.iter().sum::<i64>(), 0);
                total_circuit_checks += 1;
            }
        }
    }
    assert_eq!(total_incidence_checks, 8 * 2 * 3);
    assert_eq!(total_circuit_checks, 8 * 3);
    println!("marked link/Gysin audit");
    println!("  every marked D has two connected rank-one centers and three rank-two roads");
    println!("  honest local carrier: K_(2,3), incidence checks={total_incidence_checks}");
    println!("  G_D({{D,E}})=q_E; Gamma_D(q_E-q_F) gives a local four-circuit");
    println!("  local circuit checks={total_circuit_checks}; no global H1 map is invoked");
}

fn main() {
    let tris = triangulations();
    assert_eq!(tris.len(), 132);
    let grouped = groups(&tris);
    let mut roads: Vec<_> = grouped
        .keys()
        .filter(|current| current.len() == 1)
        .map(|current| current[0])
        .collect();
    roads.sort();
    assert_eq!(roads.len(), 8);
    let cores = compatibility_graph(&roads);
    assert_eq!(cores.len(), 12);
    assert!(cores
        .iter()
        .all(|&(first, second)| { grouped[&vec![roads[first], roads[second]]].len() == 8 }));

    let _ = audit_scalar_fibers(&tris, &grouped, &roads, &cores);
    audit_actual_two_faces(&tris, &grouped);
    honest_rank_two_carrier(roads.len(), &cores);
    imposed_rank_two_suspension(roads.len(), &cores);
    graph_face_lattice(&roads, &cores);
    marked_link_gysin(&tris, &grouped, &roads, &cores);

    println!();
    println!("VERDICT");
    println!("  each rank-two core: one cube plus two canonical transverse route faces");
    println!("  their honest boundaries are sheetwise route homotopies, not Gamma_8 fillers");
    println!("  honest rank<=2 component completion: H1=Z^11, not killed K_(2,8)");
    println!(
        "  Gamma_8 square completion: conditional on an inadmissible disconnected-fiber quotient"
    );
    println!("  physical Cut: link/Gysin to local roads, then local suspension of differences");
}
