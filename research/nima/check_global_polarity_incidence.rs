//! Exact census of the global alternating-polarity incidence through twelve points.
//!
//! For an even polygon, a diagonal is physical when its endpoints have
//! opposite parity.  The physical core of a triangulation is the collection
//! of its physical diagonals.  This certificate computes the flip components
//! at core ranks zero and one, without identifying disconnected fibers with
//! the same physical label.
//!
//! The result sharply distinguishes the six-point suspension carrier from
//! its naive higher-point extrapolation.  At six points, connected-fiber
//! contraction is K_{2,3}.  From eight points onward, the rank-one fiber over
//! a road is disconnected.  At ten and twelve points some connected
//! rank-one components have no rank-zero incidence at all.  Raw flip-edge
//! multiplicities also depend on the dihedral orbit of the road.  Thus a
//! global higher-point carrier needs higher core faces or a homotopy quotient;
//! it is not obtained by connected-fiber contraction alone.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Edge(usize, usize);

type Triangulation = Vec<Edge>;

fn edge(first: usize, second: usize) -> Edge {
    assert_ne!(first, second);
    if first < second {
        Edge(first, second)
    } else {
        Edge(second, first)
    }
}

fn boundary_edge(value: Edge, n: usize) -> bool {
    value.1 == value.0 + 1 || (value.0 == 0 && value.1 == n - 1)
}

fn physical(value: Edge) -> bool {
    value.0 % 2 != value.1 % 2
}

fn catalan(index: usize) -> usize {
    let mut values = vec![0_usize; index + 1];
    values[0] = 1;
    for n in 1..=index {
        values[n] = (0..n).map(|left| values[left] * values[n - 1 - left]).sum();
    }
    values[index]
}

fn interval_triangulations(
    first: usize,
    last: usize,
    memo: &mut BTreeMap<(usize, usize), Vec<Triangulation>>,
) -> Vec<Triangulation> {
    if last <= first + 1 {
        return vec![Vec::new()];
    }
    if let Some(saved) = memo.get(&(first, last)) {
        return saved.clone();
    }
    let mut result = Vec::new();
    for pivot in first + 1..last {
        let left = interval_triangulations(first, pivot, memo);
        let right = interval_triangulations(pivot, last, memo);
        for left_tri in &left {
            for right_tri in &right {
                let mut triangulation = Vec::with_capacity(last - first - 2);
                triangulation.extend(left_tri.iter().copied());
                triangulation.extend(right_tri.iter().copied());
                if pivot > first + 1 {
                    triangulation.push(edge(first, pivot));
                }
                if last > pivot + 1 {
                    triangulation.push(edge(pivot, last));
                }
                triangulation.sort();
                result.push(triangulation);
            }
        }
    }
    result.sort();
    result.dedup();
    memo.insert((first, last), result.clone());
    result
}

fn triangulations(n: usize) -> Vec<Triangulation> {
    let mut result = interval_triangulations(0, n - 1, &mut BTreeMap::new());
    result.sort();
    assert_eq!(result.len(), catalan(n - 2));
    assert!(result
        .iter()
        .all(|triangulation| triangulation.len() == n - 3));
    result
}

fn has_side(triangulation: &Triangulation, value: Edge, n: usize) -> bool {
    boundary_edge(value, n) || triangulation.binary_search(&value).is_ok()
}

fn flipped(triangulation: &Triangulation, diagonal: Edge, n: usize) -> Triangulation {
    assert!(triangulation.binary_search(&diagonal).is_ok());
    let opposite: Vec<_> = (0..n)
        .filter(|&vertex| vertex != diagonal.0 && vertex != diagonal.1)
        .filter(|&vertex| {
            has_side(triangulation, edge(diagonal.0, vertex), n)
                && has_side(triangulation, edge(diagonal.1, vertex), n)
        })
        .collect();
    assert_eq!(opposite.len(), 2);
    let replacement = edge(opposite[0], opposite[1]);
    assert!(!boundary_edge(replacement, n));
    let mut result: Vec<_> = triangulation
        .iter()
        .copied()
        .filter(|&value| value != diagonal)
        .collect();
    result.push(replacement);
    result.sort();
    result
}

fn neighbor_table(tris: &[Triangulation], n: usize) -> Vec<Vec<usize>> {
    let indices: BTreeMap<_, _> = tris
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, triangulation)| (triangulation, index))
        .collect();
    tris.iter()
        .map(|triangulation| {
            let mut neighbors: Vec<_> = triangulation
                .iter()
                .copied()
                .map(|diagonal| indices[&flipped(triangulation, diagonal, n)])
                .collect();
            neighbors.sort_unstable();
            neighbors.dedup();
            assert_eq!(neighbors.len(), n - 3);
            neighbors
        })
        .collect()
}

fn parity_core(triangulation: &Triangulation) -> Vec<Edge> {
    triangulation
        .iter()
        .copied()
        .filter(|&value| physical(value))
        .collect()
}

fn core_groups(tris: &[Triangulation]) -> BTreeMap<Vec<Edge>, Vec<usize>> {
    let mut groups = BTreeMap::<Vec<Edge>, Vec<usize>>::new();
    for (index, triangulation) in tris.iter().enumerate() {
        groups
            .entry(parity_core(triangulation))
            .or_default()
            .push(index);
    }
    groups
}

fn induced_components(indices: &[usize], neighbors: &[Vec<usize>]) -> Vec<Vec<usize>> {
    let allowed: BTreeSet<_> = indices.iter().copied().collect();
    let mut unseen = allowed.clone();
    let mut result = Vec::new();
    while let Some(&start) = unseen.iter().next() {
        unseen.remove(&start);
        let mut component = Vec::new();
        let mut queue = VecDeque::from([start]);
        while let Some(current) = queue.pop_front() {
            component.push(current);
            for &neighbor in &neighbors[current] {
                if allowed.contains(&neighbor) && unseen.remove(&neighbor) {
                    queue.push_back(neighbor);
                }
            }
        }
        component.sort_unstable();
        result.push(component);
    }
    result.sort();
    result
}

fn polygon_diagonals(n: usize) -> Vec<Edge> {
    let mut result = Vec::new();
    for first in 0..n {
        for second in first + 1..n {
            let candidate = edge(first, second);
            if !boundary_edge(candidate, n) {
                result.push(candidate);
            }
        }
    }
    result
}

fn physical_roads(n: usize) -> Vec<Edge> {
    polygon_diagonals(n)
        .into_iter()
        .filter(|&value| physical(value))
        .collect()
}

fn arc(first: usize, second: usize, n: usize) -> Vec<usize> {
    let mut result = vec![first];
    let mut current = first;
    while current != second {
        current = (current + 1) % n;
        result.push(current);
    }
    result
}

fn cut_polygons(cut: Edge, n: usize) -> (Vec<usize>, Vec<usize>) {
    let mut forward = arc(cut.0, cut.1, n);
    let mut backward = arc(cut.1, cut.0, n);
    if forward.len() > backward.len()
        || (forward.len() == backward.len() && forward.as_slice() > backward.as_slice())
    {
        std::mem::swap(&mut forward, &mut backward);
    }
    assert_eq!(forward.len() + backward.len(), n + 2);
    assert_eq!(forward.len() % 2, 0);
    assert_eq!(backward.len() % 2, 0);
    (forward, backward)
}

fn restrict_to_polygon(triangulation: &Triangulation, vertices: &[usize]) -> Triangulation {
    let positions: BTreeMap<_, _> = vertices
        .iter()
        .copied()
        .enumerate()
        .map(|(position, vertex)| (vertex, position))
        .collect();
    let mut result = Vec::new();
    for &value in triangulation {
        let (Some(&first), Some(&second)) = (positions.get(&value.0), positions.get(&value.1))
        else {
            continue;
        };
        let local = edge(first, second);
        if !boundary_edge(local, vertices.len()) {
            result.push(local);
        }
    }
    result.sort();
    result
}

fn sheet_of_zero_core(triangulation: &Triangulation, n: usize) -> usize {
    assert!(n >= 6);
    assert!(!triangulation.is_empty());
    let sheet = triangulation[0].0 % 2;
    assert!(triangulation
        .iter()
        .all(|value| !physical(*value) && value.0 % 2 == sheet && value.1 % 2 == sheet));
    sheet
}

fn parity_polygon_projection(triangulation: &Triangulation, n: usize) -> Triangulation {
    let p = n / 2;
    let sheet = sheet_of_zero_core(triangulation, n);
    let mut result = Vec::new();
    for &value in triangulation {
        let first = (value.0 - sheet) / 2;
        let second = (value.1 - sheet) / 2;
        let local = edge(first, second);
        if !boundary_edge(local, p) {
            result.push(local);
        }
    }
    result.sort();
    assert_eq!(result.len(), p - 3);
    result
}

fn local_component_key(local_zero: &Triangulation, local_n: usize) -> usize {
    if local_n == 4 {
        0
    } else {
        sheet_of_zero_core(local_zero, local_n)
    }
}

fn incidence_count(source: &[usize], target: &[usize], neighbors: &[Vec<usize>]) -> usize {
    let target_set: BTreeSet<_> = target.iter().copied().collect();
    source
        .iter()
        .flat_map(|&index| neighbors[index].iter().copied())
        .filter(|neighbor| target_set.contains(neighbor))
        .count()
}

fn road_orbits(roads: &[Edge], n: usize) -> BTreeMap<usize, Vec<Edge>> {
    let mut result = BTreeMap::<usize, Vec<Edge>>::new();
    for &road in roads {
        let forward = road.1 - road.0;
        let distance = forward.min(n - forward);
        assert_eq!(distance % 2, 1);
        result.entry(distance + 1).or_default().push(road);
    }
    result
}

fn assert_zero_component_associahedra(
    n: usize,
    tris: &[Triangulation],
    neighbors: &[Vec<usize>],
    zero_components: &[Vec<usize>],
) {
    let p = n / 2;
    let parity_tris = triangulations(p);
    let parity_neighbors = neighbor_table(&parity_tris, p);
    let parity_indices: BTreeMap<_, _> = parity_tris
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, triangulation)| (triangulation, index))
        .collect();
    assert_eq!(zero_components.len(), 2);
    for component in zero_components {
        assert_eq!(component.len(), catalan(p - 2));
        let mut images = BTreeSet::new();
        for &index in component {
            let projected = parity_polygon_projection(&tris[index], n);
            let projected_index = parity_indices[&projected];
            assert!(images.insert(projected.clone()));
            let global_neighbors: BTreeSet<_> = neighbors[index]
                .iter()
                .copied()
                .filter(|neighbor| component.binary_search(neighbor).is_ok())
                .map(|neighbor| parity_polygon_projection(&tris[neighbor], n))
                .collect();
            let local_neighbors: BTreeSet<_> = parity_neighbors[projected_index]
                .iter()
                .map(|&neighbor| parity_tris[neighbor].clone())
                .collect();
            assert_eq!(global_neighbors, local_neighbors);
        }
        assert_eq!(images, parity_tris.iter().cloned().collect());
    }
}

fn assert_marked_link(
    n: usize,
    cut: Edge,
    tris: &[Triangulation],
    neighbors: &[Vec<usize>],
) -> usize {
    let (first_polygon, second_polygon) = cut_polygons(cut, n);
    let first_tris = triangulations(first_polygon.len());
    let second_tris = triangulations(second_polygon.len());
    let first_set: BTreeSet<_> = first_tris.iter().cloned().collect();
    let second_set: BTreeSet<_> = second_tris.iter().cloned().collect();
    let first_neighbors = neighbor_table(&first_tris, first_polygon.len());
    let second_neighbors = neighbor_table(&second_tris, second_polygon.len());
    let first_indices: BTreeMap<_, _> = first_tris
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, triangulation)| (triangulation, index))
        .collect();
    let second_indices: BTreeMap<_, _> = second_tris
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, triangulation)| (triangulation, index))
        .collect();

    let boundary: Vec<_> = tris
        .iter()
        .enumerate()
        .filter(|(_, triangulation)| triangulation.binary_search(&cut).is_ok())
        .map(|(index, _)| index)
        .collect();
    assert_eq!(boundary.len(), first_tris.len() * second_tris.len());
    let boundary_set: BTreeSet<_> = boundary.iter().copied().collect();
    let mut images = BTreeSet::new();
    let mut image_of = BTreeMap::new();
    for &index in &boundary {
        let first = restrict_to_polygon(&tris[index], &first_polygon);
        let second = restrict_to_polygon(&tris[index], &second_polygon);
        assert!(first_set.contains(&first));
        assert!(second_set.contains(&second));
        assert!(images.insert((first.clone(), second.clone())));
        image_of.insert(index, (first, second));
    }
    assert_eq!(images.len(), first_tris.len() * second_tris.len());

    for &index in &boundary {
        let (first, second) = &image_of[&index];
        let first_index = first_indices[first];
        let second_index = second_indices[second];
        let expected: BTreeSet<_> = first_neighbors[first_index]
            .iter()
            .map(|&neighbor| (first_tris[neighbor].clone(), second.clone()))
            .chain(
                second_neighbors[second_index]
                    .iter()
                    .map(|&neighbor| (first.clone(), second_tris[neighbor].clone())),
            )
            .collect();
        let actual: BTreeSet<_> = neighbors[index]
            .iter()
            .copied()
            .filter(|neighbor| boundary_set.contains(neighbor))
            .map(|neighbor| image_of[&neighbor].clone())
            .collect();
        assert_eq!(actual, expected);
    }
    boundary.len()
}

#[derive(Debug)]
struct OrbitAudit {
    small_region: usize,
    large_region: usize,
    road_count: usize,
    raw_multiplicity: usize,
    fiber_components: usize,
    fiber_component_size: usize,
    incident_components: usize,
    orphan_components: usize,
    link_size: usize,
}

fn local_fiber_factor(region_size: usize) -> String {
    if region_size == 4 {
        "Q=K_3(interval; merged sheets)".to_owned()
    } else {
        format!("K_{}", region_size / 2 - 1)
    }
}

fn audit_n(n: usize) -> Vec<OrbitAudit> {
    assert!(matches!(n, 6 | 8 | 10 | 12));
    let p = n / 2;
    let tris = triangulations(n);
    let neighbors = neighbor_table(&tris, n);
    let groups = core_groups(&tris);
    let roads = physical_roads(n);
    assert_eq!(roads.len(), p * (p - 2));
    assert_eq!(
        groups.keys().filter(|core| core.len() == 1).count(),
        roads.len()
    );

    let zero_indices = &groups[&Vec::new()];
    let zero_components = induced_components(zero_indices, &neighbors);
    assert_eq!(zero_indices.len(), 2 * catalan(p - 2));
    assert_zero_component_associahedra(n, &tris, &neighbors, &zero_components);

    let mut audits = Vec::new();
    for (small_region, orbit_roads) in road_orbits(&roads, n) {
        let representative = orbit_roads[0];
        let (first_polygon, second_polygon) = cut_polygons(representative, n);
        assert_eq!(first_polygon.len(), small_region);
        let large_region = second_polygon.len();
        let first_half = small_region / 2;
        let second_half = large_region / 2;
        let expected_multiplicity = catalan(first_half - 2) * catalan(second_half - 2);
        let local_component_counts = [
            if small_region == 4 { 1 } else { 2 },
            if large_region == 4 { 1 } else { 2 },
        ];
        let expected_fiber_components = local_component_counts[0] * local_component_counts[1];
        let expected_component_size = (if small_region == 4 {
            2
        } else {
            catalan(first_half - 2)
        }) * (if large_region == 4 {
            2
        } else {
            catalan(second_half - 2)
        });

        for &road in &orbit_roads {
            let group = &groups[&vec![road]];
            assert_eq!(group.len(), 4 * expected_multiplicity);
            let components = induced_components(group, &neighbors);
            assert_eq!(components.len(), expected_fiber_components);
            assert!(components
                .iter()
                .all(|component| component.len() == expected_component_size));

            let (first_vertices, second_vertices) = cut_polygons(road, n);
            let mut coordinate_classes = BTreeMap::<(usize, usize), BTreeSet<usize>>::new();
            for &index in group {
                let first = restrict_to_polygon(&tris[index], &first_vertices);
                let second = restrict_to_polygon(&tris[index], &second_vertices);
                assert!(parity_core(&first).is_empty());
                assert!(parity_core(&second).is_empty());
                coordinate_classes
                    .entry((
                        local_component_key(&first, first_vertices.len()),
                        local_component_key(&second, second_vertices.len()),
                    ))
                    .or_default()
                    .insert(index);
            }
            let component_sets: BTreeSet<_> = components
                .iter()
                .map(|component| component.iter().copied().collect::<BTreeSet<_>>())
                .collect();
            assert_eq!(
                coordinate_classes
                    .values()
                    .cloned()
                    .collect::<BTreeSet<_>>(),
                component_sets
            );

            let mut incident_rank_components = BTreeSet::new();
            for (polarity, zero_component) in zero_components.iter().enumerate() {
                let total = incidence_count(zero_component, group, &neighbors);
                assert_eq!(total, expected_multiplicity);
                let nonzero: Vec<_> = components
                    .iter()
                    .enumerate()
                    .filter_map(|(component_index, component)| {
                        let count = incidence_count(zero_component, component, &neighbors);
                        (count > 0).then_some((component_index, count))
                    })
                    .collect();
                assert_eq!(nonzero.len(), 1);
                assert_eq!(nonzero[0].1, expected_multiplicity);
                incident_rank_components.insert(nonzero[0].0);

                // Each zero component is a genuine polarity sheet.
                let sheet = sheet_of_zero_core(&tris[zero_component[0]], n);
                assert_eq!(sheet, polarity);
            }
            let expected_incident = if small_region == 4 && large_region == 4 {
                1
            } else {
                2
            };
            assert_eq!(incident_rank_components.len(), expected_incident);
        }

        let link_size = assert_marked_link(n, representative, &tris, &neighbors);
        let incident_components = if small_region == 4 && large_region == 4 {
            1
        } else {
            2
        };
        audits.push(OrbitAudit {
            small_region,
            large_region,
            road_count: orbit_roads.len(),
            raw_multiplicity: expected_multiplicity,
            fiber_components: expected_fiber_components,
            fiber_component_size: expected_component_size,
            incident_components,
            orphan_components: expected_fiber_components - incident_components,
            link_size,
        });
    }

    let expected_orbit_count = (p - 1) / 2;
    assert_eq!(audits.len(), expected_orbit_count);
    assert_eq!(
        audits.iter().map(|audit| audit.road_count).sum::<usize>(),
        roads.len()
    );

    println!(
        "n={n}: {} triangulations, {} roads",
        tris.len(),
        roads.len()
    );
    println!(
        "  zero core: 2 components, each K_{}=Assoc({p}-gon) with {} vertices",
        p - 1,
        catalan(p - 2)
    );
    for audit in &audits {
        println!(
            "  orbit {}+{}: roads={}, mu={}, fiber={}x{} [{} x {}], incident={}, orphan={}, link={}",
            audit.small_region,
            audit.large_region,
            audit.road_count,
            audit.raw_multiplicity,
            audit.fiber_components,
            audit.fiber_component_size,
            local_fiber_factor(audit.small_region),
            local_fiber_factor(audit.large_region),
            audit.incident_components,
            audit.orphan_components,
            audit.link_size
        );
    }
    match n {
        6 => println!("  connected-fiber contraction: simple K_(2,3)"),
        8 => println!(
            "  connected-fiber contraction: two disjoint K_(1,8) stars; fiber-label quotient gives K_(2,8)"
        ),
        10 | 12 => println!(
            "  connected-fiber contraction: orbit-dependent bipartite multigraph with orphan rank-one components"
        ),
        _ => unreachable!(),
    }
    println!();
    audits
}

fn main() {
    let six = audit_n(6);
    let eight = audit_n(8);
    let ten = audit_n(10);
    let twelve = audit_n(12);

    assert_eq!(six.len(), 1);
    assert_eq!(six[0].raw_multiplicity, 1);
    assert_eq!(six[0].fiber_components, 1);

    assert_eq!(eight.len(), 1);
    assert_eq!(eight[0].raw_multiplicity, 1);
    assert_eq!(eight[0].fiber_components, 2);

    assert_eq!(
        ten.iter()
            .map(|audit| (
                audit.small_region,
                audit.raw_multiplicity,
                audit.fiber_components
            ))
            .collect::<Vec<_>>(),
        vec![(4, 2, 2), (6, 1, 4)]
    );
    assert_eq!(
        twelve
            .iter()
            .map(|audit| (
                audit.small_region,
                audit.raw_multiplicity,
                audit.fiber_components
            ))
            .collect::<Vec<_>>(),
        vec![(4, 5, 2), (6, 2, 4)]
    );

    println!("VERDICT");
    println!("  road count p(p-2): VERIFIED for n=6,8,10,12");
    println!("  zero-core components: two parity associahedra at every tested n");
    println!("  only n=6 contracts connected core fibers to a simple K_(2,r)");
    println!(
        "  n>=8 requires disconnected-fiber descent; n>=10 also has orphan rank-one components"
    );
    println!("  marked links are exact products of the two cut-polygon associahedra");
}
