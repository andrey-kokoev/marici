//! Countercertificate for the naive n=8 -> K_{2,4} polarity carrier.
//!
//! The certificate derives incidence from polygon triangulations only.  A
//! diagonal is physical when its endpoints have opposite parity.  The parity
//! core of a triangulation is its set of physical diagonals.
//!
//! At n=6 the familiar construction has two zero-core vertices and three
//! one-core strata.  Contracting each one-core fiber gives K_{2,3}.
//!
//! At n=8 the literal analogue behaves differently:
//!
//! * the four zero-core triangulations form two connected components under
//!   zero-core flips, so they do give an unordered pair of polarity cores;
//! * there are eight, not four, rank-one parity-core strata;
//! * after contracting the two zero-core components and the eight one-core
//!   fibers, every polarity core meets every rank-one stratum once.  The
//!   derived incidence is K_{2,8}.
//!
//! Pairing antipodal roads produces a graph quotient K_{2,4}, but it is not a
//! contraction of the scalar parity-core presentation.  Every antipodal pair
//! occurs as a genuine rank-two core with eight scalar refinements, so the
//! quotient collapses a two-channel stratum to rank one and merges distinct
//! factorization labels.
//!
//! The correct six-point restriction is nevertheless present.  Marking any
//! one of the eight physical channels cuts the octagon into a quadrilateral
//! and a hexagon.  Quotienting the inessential two choices of quadrilateral
//! triangulation leaves exactly the fourteen hexagon triangulations, its two
//! zero-core centers, its three physical roads, and the K_{2,3} incidence.
//!
//! Thus this file falsifies only the proposed global four-road carrier.  It
//! does not obstruct the all-m abstract suspension theorem or the family of
//! marked six-point boundary carriers.

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

fn crossing(first: Edge, second: Edge) -> bool {
    if first.0 == second.0 || first.0 == second.1 || first.1 == second.0 || first.1 == second.1 {
        return false;
    }
    (first.0 < second.0 && second.0 < first.1 && first.1 < second.1)
        || (second.0 < first.0 && first.0 < second.1 && second.1 < first.1)
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

fn triangulations(n: usize) -> Vec<Triangulation> {
    let diagonals = polygon_diagonals(n);
    let mut result = Vec::new();
    choose_noncrossing(&diagonals, 0, n - 3, &mut Vec::new(), &mut result);
    result.sort();
    result
}

fn physical(value: Edge) -> bool {
    value.0 % 2 != value.1 % 2
}

fn parity_core(triangulation: &Triangulation) -> Vec<Edge> {
    triangulation
        .iter()
        .copied()
        .filter(|&diagonal| physical(diagonal))
        .collect()
}

fn common_count(first: &Triangulation, second: &Triangulation) -> usize {
    first.iter().filter(|edge| second.contains(edge)).count()
}

fn adjacent(first: &Triangulation, second: &Triangulation) -> bool {
    first.len() == second.len() && common_count(first, second) + 1 == first.len()
}

fn core_groups(tris: &[Triangulation]) -> BTreeMap<Vec<Edge>, Vec<usize>> {
    let mut result = BTreeMap::<Vec<Edge>, Vec<usize>>::new();
    for (index, triangulation) in tris.iter().enumerate() {
        result
            .entry(parity_core(triangulation))
            .or_default()
            .push(index);
    }
    result
}

fn induced_components(indices: &[usize], tris: &[Triangulation]) -> Vec<Vec<usize>> {
    let allowed: BTreeSet<_> = indices.iter().copied().collect();
    let mut unseen = allowed.clone();
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

fn transform_vertex(vertex: usize, n: usize, rotation: usize, reflected: bool) -> usize {
    let reflected_vertex = if reflected { (n - vertex) % n } else { vertex };
    (reflected_vertex + rotation) % n
}

fn transform_edge(value: Edge, n: usize, rotation: usize, reflected: bool) -> Edge {
    edge(
        transform_vertex(value.0, n, rotation, reflected),
        transform_vertex(value.1, n, rotation, reflected),
    )
}

fn transform_triangulation(
    triangulation: &Triangulation,
    n: usize,
    rotation: usize,
    reflected: bool,
) -> Triangulation {
    let mut result: Vec<_> = triangulation
        .iter()
        .copied()
        .map(|value| transform_edge(value, n, rotation, reflected))
        .collect();
    result.sort();
    result
}

fn incidence_count(component: &[usize], target: &[usize], tris: &[Triangulation]) -> usize {
    component
        .iter()
        .flat_map(|&source| target.iter().map(move |&destination| (source, destination)))
        .filter(|&(source, destination)| adjacent(&tris[source], &tris[destination]))
        .count()
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
    let forward = arc(cut.0, cut.1, n);
    let backward = arc(cut.1, cut.0, n);
    if forward.len() < backward.len() {
        (forward, backward)
    } else {
        (backward, forward)
    }
}

fn quadrilateral_diagonals(cut: Edge, n: usize) -> [Edge; 2] {
    let (quadrilateral, hexagon) = cut_polygons(cut, n);
    assert_eq!(quadrilateral.len(), 4);
    assert_eq!(hexagon.len(), 6);
    [
        edge(quadrilateral[0], quadrilateral[2]),
        edge(quadrilateral[1], quadrilateral[3]),
    ]
}

fn flip_quadrilateral_factor(triangulation: &Triangulation, cut: Edge, n: usize) -> Triangulation {
    let [first, second] = quadrilateral_diagonals(cut, n);
    assert_ne!(
        triangulation.contains(&first),
        triangulation.contains(&second)
    );
    let mut result: Vec<_> = triangulation
        .iter()
        .copied()
        .filter(|&value| value != first && value != second)
        .collect();
    result.push(if triangulation.contains(&first) {
        second
    } else {
        first
    });
    result.sort();
    result
}

fn hexagon_restriction(triangulation: &Triangulation, cut: Edge, n: usize) -> Triangulation {
    let (quadrilateral, hexagon) = cut_polygons(cut, n);
    assert_eq!(quadrilateral.len(), 4);
    assert_eq!(hexagon.len(), 6);
    let quadrilateral_diagonals = [
        edge(quadrilateral[0], quadrilateral[2]),
        edge(quadrilateral[1], quadrilateral[3]),
    ];
    let positions: BTreeMap<_, _> = hexagon
        .iter()
        .copied()
        .enumerate()
        .map(|(position, vertex)| (vertex, position))
        .collect();
    let mut result = Vec::new();
    for &value in triangulation {
        if value == cut || quadrilateral_diagonals.contains(&value) {
            continue;
        }
        let local = edge(positions[&value.0], positions[&value.1]);
        assert!(!boundary_edge(local, 6));
        result.push(local);
    }
    result.sort();
    assert_eq!(result.len(), 3);
    result
}

fn audit_six_point_reference() -> (Vec<Triangulation>, Vec<Vec<usize>>, Vec<Edge>) {
    let tris = triangulations(6);
    assert_eq!(tris.len(), 14);
    let groups = core_groups(&tris);
    let zero = &groups[&Vec::new()];
    assert_eq!(zero.len(), 2);
    let components = induced_components(zero, &tris);
    assert_eq!(
        components.iter().map(Vec::len).collect::<Vec<_>>(),
        vec![1, 1]
    );
    let roads: Vec<_> = groups
        .keys()
        .filter(|core| core.len() == 1)
        .map(|core| core[0])
        .collect();
    assert_eq!(roads.len(), 3);
    for component in &components {
        for &road in &roads {
            assert_eq!(incidence_count(component, &groups[&vec![road]], &tris), 1);
        }
    }
    (tris, components, roads)
}

fn audit_eight_point_global() -> (
    Vec<Triangulation>,
    BTreeMap<Vec<Edge>, Vec<usize>>,
    Vec<Vec<usize>>,
    Vec<Edge>,
) {
    let tris = triangulations(8);
    assert_eq!(tris.len(), 132);
    let groups = core_groups(&tris);
    let counts = groups.values().fold([0_usize; 3], |mut result, group| {
        let rank = parity_core(&tris[group[0]]).len();
        result[rank] += group.len();
        result
    });
    assert_eq!(counts, [4, 32, 96]);

    let zero = &groups[&Vec::new()];
    assert_eq!(zero.len(), 4);
    let components = induced_components(zero, &tris);
    assert_eq!(
        components.iter().map(Vec::len).collect::<Vec<_>>(),
        vec![2, 2]
    );

    let roads: Vec<_> = groups
        .keys()
        .filter(|core| core.len() == 1)
        .map(|core| core[0])
        .collect();
    assert_eq!(roads.len(), 8);
    assert!(roads.iter().all(|&road| physical(road)));
    for component in &components {
        for &road in &roads {
            assert_eq!(incidence_count(component, &groups[&vec![road]], &tris), 1);
        }
    }

    // The full dihedral action preserves the derived incidence and acts on
    // the two zero-core components as the polarity S^0.
    let tri_index: BTreeMap<_, _> = tris
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, triangulation)| (triangulation, index))
        .collect();
    let component_sets: Vec<BTreeSet<_>> = components
        .iter()
        .map(|component| component.iter().copied().collect())
        .collect();
    let mut symmetry_checks = 0;
    for reflected in [false, true] {
        for rotation in 0..8 {
            let moved_components: Vec<_> = components
                .iter()
                .map(|component| {
                    component
                        .iter()
                        .map(|&index| {
                            tri_index
                                [&transform_triangulation(&tris[index], 8, rotation, reflected)]
                        })
                        .collect::<BTreeSet<_>>()
                })
                .collect();
            assert!(moved_components
                .iter()
                .all(|component| component_sets.contains(component)));
            for component in &components {
                for &road in &roads {
                    let moved_component: BTreeSet<_> = component
                        .iter()
                        .map(|&index| {
                            tri_index
                                [&transform_triangulation(&tris[index], 8, rotation, reflected)]
                        })
                        .collect();
                    let target_component = components
                        .iter()
                        .find(|candidate| {
                            candidate.iter().copied().collect::<BTreeSet<_>>() == moved_component
                        })
                        .expect("dihedral image of a polarity component");
                    let moved_road = transform_edge(road, 8, rotation, reflected);
                    assert_eq!(
                        incidence_count(target_component, &groups[&vec![moved_road]], &tris,),
                        1,
                    );
                    symmetry_checks += 1;
                }
            }
        }
    }
    assert_eq!(symmetry_checks, 16 * 2 * 8);

    // The only tempting four-road quotient pairs antipodal physical
    // diagonals.  Each pair is itself a genuine rank-two parity core.  Thus
    // the quotient destroys core rank and cannot represent scalar cuts.
    let mut antipodal_orbits = BTreeSet::new();
    for &road in &roads {
        let opposite = transform_edge(road, 8, 4, false);
        let orbit = if road < opposite {
            [road, opposite]
        } else {
            [opposite, road]
        };
        antipodal_orbits.insert(orbit);
    }
    assert_eq!(antipodal_orbits.len(), 4);
    for orbit in antipodal_orbits {
        let core = vec![orbit[0], orbit[1]];
        assert_eq!(groups[&core].len(), 8);
        assert_ne!(orbit[0], orbit[1]);
    }

    println!("n=8 global scalar incidence");
    println!("  triangulations/core counts: 132 = 4 + 32 + 96");
    println!("  zero-core flip components: 2 components of size 2");
    println!("  rank-one parity-core roads: 8 distinct physical channels");
    println!("  contracted incidence: K_(2,8), with 16 simple edges");
    println!("  D8 incidence covariance checks: {symmetry_checks}");
    println!("  antipodal four-road quotient: rejected (collapses four genuine rank-two cores)");

    (tris, groups, components, roads)
}

fn audit_marked_cuts(
    tris: &[Triangulation],
    groups: &BTreeMap<Vec<Edge>, Vec<usize>>,
    roads: &[Edge],
    six_tris: &[Triangulation],
) {
    let all_six: BTreeSet<_> = six_tris.iter().cloned().collect();
    let tri_index: BTreeMap<_, _> = tris
        .iter()
        .cloned()
        .enumerate()
        .map(|(index, triangulation)| (triangulation, index))
        .collect();
    let mut cut_incidence_checks = 0;
    for &cut in roads {
        let boundary: Vec<_> = tris
            .iter()
            .enumerate()
            .filter(|(_, triangulation)| triangulation.contains(&cut))
            .map(|(index, _)| index)
            .collect();
        assert_eq!(boundary.len(), 28); // Catalan(2) * Catalan(4) = 2 * 14.

        let mut restriction_fibers = BTreeMap::<Triangulation, Vec<usize>>::new();
        for &index in &boundary {
            let restricted = hexagon_restriction(&tris[index], cut, 8);
            restriction_fibers
                .entry(restricted)
                .or_default()
                .push(index);
            let flipped = flip_quadrilateral_factor(&tris[index], cut, 8);
            assert!(tri_index.contains_key(&flipped));
            assert_eq!(
                hexagon_restriction(&flipped, cut, 8),
                hexagon_restriction(&tris[index], cut, 8)
            );

            let mut mapped_global_core = Vec::new();
            for &global_road in &parity_core(&tris[index]) {
                if global_road == cut {
                    continue;
                }
                let singleton = vec![global_road];
                // Reuse the restriction routine on a completion is
                // unnecessary: positions on the six-vertex side determine
                // the local edge directly.
                let (_, hexagon) = cut_polygons(cut, 8);
                let positions: BTreeMap<_, _> = hexagon
                    .iter()
                    .copied()
                    .enumerate()
                    .map(|(position, vertex)| (vertex, position))
                    .collect();
                assert!(positions.contains_key(&global_road.0));
                assert!(positions.contains_key(&global_road.1));
                let local = edge(positions[&global_road.0], positions[&global_road.1]);
                assert!(physical(local));
                mapped_global_core.push(local);
                assert_eq!(singleton.len(), 1);
            }
            mapped_global_core.sort();
            assert_eq!(
                mapped_global_core,
                parity_core(&hexagon_restriction(&tris[index], cut, 8))
            );
        }
        assert_eq!(restriction_fibers.len(), 14);
        assert_eq!(
            restriction_fibers.keys().cloned().collect::<BTreeSet<_>>(),
            all_six
        );
        assert!(restriction_fibers.values().all(|fiber| fiber.len() == 2));

        let source_core = vec![cut];
        let source = &groups[&source_core];
        assert_eq!(source.len(), 4);
        let source_components = induced_components(source, tris);
        assert_eq!(
            source_components.iter().map(Vec::len).collect::<Vec<_>>(),
            vec![2, 2]
        );
        for component in &source_components {
            let flipped_component: BTreeSet<_> = component
                .iter()
                .map(|&index| tri_index[&flip_quadrilateral_factor(&tris[index], cut, 8)])
                .collect();
            assert_eq!(flipped_component, component.iter().copied().collect());
        }

        let compatible: Vec<_> = roads
            .iter()
            .copied()
            .filter(|&road| {
                if road == cut {
                    return false;
                }
                let mut core = vec![cut, road];
                core.sort();
                groups.contains_key(&core)
            })
            .collect();
        assert_eq!(compatible.len(), 3);

        for component in &source_components {
            for &road in &compatible {
                let mut target_core = vec![cut, road];
                target_core.sort();
                let target = &groups[&target_core];
                assert_eq!(target.len(), 8);
                let pairs: Vec<_> = component
                    .iter()
                    .flat_map(|&source_index| {
                        target
                            .iter()
                            .copied()
                            .map(move |target_index| (source_index, target_index))
                    })
                    .filter(|&(source_index, target_index)| {
                        adjacent(&tris[source_index], &tris[target_index])
                    })
                    .collect();
                assert_eq!(pairs.len(), 2);
                let moved_pairs: BTreeSet<_> = pairs
                    .iter()
                    .map(|&(source_index, target_index)| {
                        (
                            tri_index[&flip_quadrilateral_factor(&tris[source_index], cut, 8)],
                            tri_index[&flip_quadrilateral_factor(&tris[target_index], cut, 8)],
                        )
                    })
                    .collect();
                assert_eq!(moved_pairs, pairs.iter().copied().collect());
                cut_incidence_checks += 1;
            }
        }
    }
    assert_eq!(cut_incidence_checks, 8 * 2 * 3);
    println!("n=8 marked-channel restrictions");
    println!("  8 cuts: each boundary is Tri(4) x Tri(6), with 28 scalar cells");
    println!("  quotient by the quadrilateral flip gives all 14 hexagon cells");
    println!("  each cut recovers 2 polarity centers, 3 roads, and K_(2,3)");
    println!("  quotient incidence checks: {cut_incidence_checks}");
}

fn main() {
    let (six_tris, _, _) = audit_six_point_reference();
    let (eight_tris, groups, _, roads) = audit_eight_point_global();
    audit_marked_cuts(&eight_tris, &groups, &roads, &six_tris);
    println!();
    println!("VERDICT");
    println!("  canonical global n=8 K_(2,4) scalar carrier: FALSIFIED");
    println!("  canonical global carrier from the same contractions: K_(2,8)");
    println!("  marked physical-cut carrier: K_(2,3), recovered on every boundary");
}
