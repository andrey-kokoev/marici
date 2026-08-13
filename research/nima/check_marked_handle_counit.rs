//! Exact external-state test for the resolved surface counit on a handle.
//!
//! Start with the theta spine of the once-holed torus and subdivide `n`
//! distinct roads, attaching one labelled external leg at every subdivision.
//! For n = 0,1,2,3 the resulting cubic ribbon graph has
//!
//!     V = n + 2,  E_internal = n + 3,  b_1 = 2,  (g,b) = (1,1).
//!
//! Every cubic vertex carries one of the three cyclic three-point counit
//! sectors.  The program enumerates all 3^V resolved sewings, retains their
//! external Brauer matching, and counts closed polarization circuits before
//! applying D -> 1.  It also opens every subset of internal edges and checks
//! Cut naturality coefficient by coefficient after the augmentation.
//!
//! The completed graph-theoretic cycles are also checked to have mixed turn
//! words.  This is only a topological diagnostic: it does not test the
//! pre-gluing open paths that control longitudinal physical-projector terms.
//! The complete tensor-network audit in `check_marked_handle_x_dictionary.rs`
//! finds those corrections to be nonzero for some sewing histories.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Var {
    X14,
    X26,
    X36,
    X24,
    X25,
    X46,
}

const YM3: [(i64, Var, Var); 6] = [
    (1, Var::X14, Var::X26),
    (1, Var::X36, Var::X24),
    (1, Var::X25, Var::X46),
    (-1, Var::X25, Var::X36),
    (-1, Var::X14, Var::X36),
    (-1, Var::X14, Var::X25),
];

const LOCAL_SECTORS: [(Var, Var); 3] = [
    (Var::X14, Var::X26),
    (Var::X36, Var::X24),
    (Var::X25, Var::X46),
];

fn ordered_pair<T: Ord>(left: T, right: T) -> (T, T) {
    if left <= right {
        (left, right)
    } else {
        (right, left)
    }
}

fn audit_local_three_point_counit() {
    let mut polynomial = BTreeMap::new();
    for &(coefficient, left, right) in &YM3 {
        *polynomial.entry(ordered_pair(left, right)).or_insert(0) += coefficient;
    }
    for &(left, right) in &LOCAL_SECTORS {
        assert_eq!(polynomial.get(&ordered_pair(left, right)), Some(&1));
    }
}

fn flag(vertex: usize, position: usize) -> usize {
    assert!(position < 3);
    4 * vertex + position
}

fn auxiliary(vertex: usize) -> usize {
    4 * vertex + 3
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct InternalEdge {
    left: usize,
    right: usize,
    road: usize,
}

#[derive(Clone, Debug)]
struct MarkedTheta {
    inserted_roads: usize,
    vertices: usize,
    edges: Vec<InternalEdge>,
    physical_external: BTreeSet<usize>,
}

impl MarkedTheta {
    fn new(inserted_roads: usize) -> Self {
        assert!(inserted_roads <= 3);
        let vertices = 2 + inserted_roads;
        let mut edges = Vec::new();
        let mut physical_external = BTreeSet::new();

        for road in 0..3 {
            if road < inserted_roads {
                let middle = 2 + road;
                // The cyclic order at a marked middle vertex is
                // (towards left core, external leg, towards right core).
                edges.push(InternalEdge {
                    left: flag(0, road),
                    right: flag(middle, 0),
                    road,
                });
                edges.push(InternalEdge {
                    left: flag(1, road),
                    right: flag(middle, 2),
                    road,
                });
                physical_external.insert(flag(middle, 1));
            } else {
                edges.push(InternalEdge {
                    left: flag(0, road),
                    right: flag(1, road),
                    road,
                });
            }
        }

        let graph = Self {
            inserted_roads,
            vertices,
            edges,
            physical_external,
        };
        assert_eq!(graph.edges.len(), inserted_roads + 3);
        assert_eq!(graph.edges.len() + 1 - graph.vertices, 2);
        graph
    }

    fn all_external(&self, cut_mask: u64) -> BTreeSet<usize> {
        let mut external = self.physical_external.clone();
        external.extend((0..self.vertices).map(auxiliary));
        for (index, edge) in self.edges.iter().enumerate() {
            if cut_mask & (1 << index) != 0 {
                external.insert(edge.left);
                external.insert(edge.right);
            }
        }
        external
    }

    /// Boundary cycles of the ribbon graph.  Internal edges are paired by
    /// alpha; an external marked flag is fixed.  The vertex permutation sigma
    /// uses the displayed cyclic orders, and boundaries are cycles of sigma alpha.
    fn ribbon_signature(&self) -> (usize, usize) {
        let half_edges = 3 * self.vertices;
        let mut alpha: Vec<_> = (0..half_edges).collect();
        let ribbon_id = |endpoint: usize| 3 * (endpoint / 4) + endpoint % 4;
        for edge in &self.edges {
            let left = ribbon_id(edge.left);
            let right = ribbon_id(edge.right);
            alpha[left] = right;
            alpha[right] = left;
        }

        let sigma = |half_edge: usize| {
            let vertex = half_edge / 3;
            let position = half_edge % 3;
            3 * vertex + (position + 1) % 3
        };
        let phi: Vec<_> = (0..half_edges).map(|h| sigma(alpha[h])).collect();
        let mut seen = vec![false; half_edges];
        let mut boundaries = 0;
        for start in 0..half_edges {
            if seen[start] {
                continue;
            }
            boundaries += 1;
            let mut current = start;
            while !seen[current] {
                seen[current] = true;
                current = phi[current];
            }
            assert_eq!(current, start);
        }

        // External tails do not change the Euler characteristic of the spine.
        let twice_genus =
            2_i64 - boundaries as i64 - (self.vertices as i64 - self.edges.len() as i64);
        assert!(twice_genus >= 0 && twice_genus % 2 == 0);
        ((twice_genus / 2) as usize, boundaries)
    }
}

fn patterns(vertices: usize) -> Vec<Vec<usize>> {
    let total = 3_usize.pow(vertices as u32);
    (0..total)
        .map(|mut code| {
            let mut pattern = Vec::with_capacity(vertices);
            for _ in 0..vertices {
                pattern.push(code % 3);
                code /= 3;
            }
            pattern
        })
        .collect()
}

fn add_edge(adjacency: &mut [Vec<usize>], left: usize, right: usize) {
    adjacency[left].push(right);
    adjacency[right].push(left);
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct ResolvedState {
    circuits: usize,
    external_matching: Vec<(usize, usize)>,
}

fn resolved_state(graph: &MarkedTheta, pattern: &[usize], cut_mask: u64) -> ResolvedState {
    assert_eq!(pattern.len(), graph.vertices);
    let endpoint_count = 4 * graph.vertices;
    let mut adjacency = vec![Vec::new(); endpoint_count];

    for (vertex, &singleton) in pattern.iter().enumerate() {
        assert!(singleton < 3);
        add_edge(&mut adjacency, auxiliary(vertex), flag(vertex, singleton));
        let paired: Vec<_> = (0..3).filter(|&position| position != singleton).collect();
        add_edge(
            &mut adjacency,
            flag(vertex, paired[0]),
            flag(vertex, paired[1]),
        );
    }

    for (index, edge) in graph.edges.iter().enumerate() {
        if cut_mask & (1 << index) == 0 {
            add_edge(&mut adjacency, edge.left, edge.right);
        }
    }

    let external = graph.all_external(cut_mask);
    let mut seen = vec![false; endpoint_count];
    let mut circuits = 0;
    let mut external_matching = Vec::new();
    for start in 0..endpoint_count {
        if seen[start] {
            continue;
        }
        let mut queue = VecDeque::from([start]);
        seen[start] = true;
        let mut component_external = Vec::new();
        while let Some(endpoint) = queue.pop_front() {
            if external.contains(&endpoint) {
                component_external.push(endpoint);
            }
            for &next in &adjacency[endpoint] {
                if !seen[next] {
                    seen[next] = true;
                    queue.push_back(next);
                }
            }
        }
        match component_external.len() {
            0 => circuits += 1,
            2 => external_matching.push(ordered_pair(component_external[0], component_external[1])),
            count => panic!("resolved component has {} external endpoints", count),
        }
    }
    external_matching.sort_unstable();
    ResolvedState {
        circuits,
        external_matching,
    }
}

fn circuit_histogram(graph: &MarkedTheta, cut_mask: u64) -> BTreeMap<usize, usize> {
    let mut histogram = BTreeMap::new();
    for pattern in patterns(graph.vertices) {
        *histogram
            .entry(resolved_state(graph, &pattern, cut_mask).circuits)
            .or_insert(0) += 1;
    }
    histogram
}

fn road_weight(graph: &MarkedTheta, road: usize) -> usize {
    if road < graph.inserted_roads {
        3
    } else {
        1
    }
}

fn predicted_circuit_sectors(graph: &MarkedTheta, cut_mask: u64) -> usize {
    let cut_roads: BTreeSet<_> = graph
        .edges
        .iter()
        .enumerate()
        .filter_map(|(index, edge)| (cut_mask & (1 << index) != 0).then_some(edge.road))
        .collect();
    match cut_roads.len() {
        0 => (0..3).map(|road| road_weight(graph, road)).sum(),
        1 => road_weight(graph, *cut_roads.first().unwrap()),
        _ => 0,
    }
}

fn audit_family() -> usize {
    let mut cut_squares = 0;
    for inserted_roads in 0..=3 {
        let graph = MarkedTheta::new(inserted_roads);
        assert_eq!(graph.ribbon_signature(), (1, 1));
        let total = 3_usize.pow(graph.vertices as u32);
        let closed_circuits = 2 * inserted_roads + 3;
        assert_eq!(
            circuit_histogram(&graph, 0),
            BTreeMap::from([(0, total - closed_circuits), (1, closed_circuits)])
        );

        for cut_mask in 0..(1_u64 << graph.edges.len()) {
            let surviving = predicted_circuit_sectors(&graph, cut_mask);
            let expected = if surviving == 0 {
                BTreeMap::from([(0, total)])
            } else {
                BTreeMap::from([(0, total - surviving), (1, surviving)])
            };
            assert_eq!(circuit_histogram(&graph, cut_mask), expected);

            // The resolved augmentation evaluates every one of the 3^V
            // sectors to the scalar line, before and after every iterated Cut.
            assert_eq!(expected.values().sum::<usize>(), total);
            cut_squares += 1;
        }
    }
    cut_squares
}

fn cut_topology(graph: &MarkedTheta, cut_mask: u64) -> (usize, usize, usize) {
    let mut adjacency = vec![Vec::new(); graph.vertices];
    let mut remaining_edges = 0;
    for (index, edge) in graph.edges.iter().enumerate() {
        if cut_mask & (1 << index) != 0 {
            continue;
        }
        let left = edge.left / 4;
        let right = edge.right / 4;
        adjacency[left].push(right);
        adjacency[right].push(left);
        remaining_edges += 1;
    }

    let mut seen = vec![false; graph.vertices];
    let mut components = 0;
    for start in 0..graph.vertices {
        if seen[start] {
            continue;
        }
        components += 1;
        let mut queue = VecDeque::from([start]);
        seen[start] = true;
        while let Some(vertex) = queue.pop_front() {
            for &next in &adjacency[vertex] {
                if !seen[next] {
                    seen[next] = true;
                    queue.push_back(next);
                }
            }
        }
    }
    let betti = remaining_edges + components - graph.vertices;
    (cut_mask.count_ones() as usize, components, betti)
}

fn graph_is_connected(graph: &MarkedTheta, edge_mask: u64) -> bool {
    let mut adjacency = vec![Vec::new(); graph.vertices];
    for (index, edge) in graph.edges.iter().enumerate() {
        if edge_mask & (1 << index) == 0 {
            continue;
        }
        let left = edge.left / 4;
        let right = edge.right / 4;
        adjacency[left].push(right);
        adjacency[right].push(left);
    }
    let mut seen = BTreeSet::from([0]);
    let mut queue = VecDeque::from([0]);
    while let Some(vertex) = queue.pop_front() {
        for &next in &adjacency[vertex] {
            if seen.insert(next) {
                queue.push_back(next);
            }
        }
    }
    seen.len() == graph.vertices
}

fn simple_cycle_masks(graph: &MarkedTheta) -> Vec<u64> {
    let mut cycles = Vec::new();
    for edge_mask in 1..(1_u64 << graph.edges.len()) {
        let mut degree = vec![0; graph.vertices];
        for (index, edge) in graph.edges.iter().enumerate() {
            if edge_mask & (1 << index) != 0 {
                degree[edge.left / 4] += 1;
                degree[edge.right / 4] += 1;
            }
        }
        let support: Vec<_> = degree
            .iter()
            .enumerate()
            .filter_map(|(vertex, &value)| (value != 0).then_some(vertex))
            .collect();
        if support.is_empty() || support.iter().any(|&vertex| degree[vertex] != 2) {
            continue;
        }

        let mut adjacency = vec![Vec::new(); graph.vertices];
        for (index, edge) in graph.edges.iter().enumerate() {
            if edge_mask & (1 << index) != 0 {
                let left = edge.left / 4;
                let right = edge.right / 4;
                adjacency[left].push(right);
                adjacency[right].push(left);
            }
        }
        let mut seen = BTreeSet::from([support[0]]);
        let mut queue = VecDeque::from([support[0]]);
        while let Some(vertex) = queue.pop_front() {
            for &next in &adjacency[vertex] {
                if seen.insert(next) {
                    queue.push_back(next);
                }
            }
        }
        if seen.len() == support.len() {
            cycles.push(edge_mask);
        }
    }
    cycles
}

fn turn_word(graph: &MarkedTheta, cycle_mask: u64) -> Vec<char> {
    let mut incidence = vec![Vec::<(usize, usize)>::new(); graph.vertices];
    for (index, edge) in graph.edges.iter().enumerate() {
        if cycle_mask & (1 << index) == 0 {
            continue;
        }
        incidence[edge.left / 4].push((index, edge.left));
        incidence[edge.right / 4].push((index, edge.right));
    }
    for entries in &incidence {
        assert!(entries.is_empty() || entries.len() == 2);
    }

    let start = incidence
        .iter()
        .position(|entries| !entries.is_empty())
        .unwrap();
    let first_edge = incidence[start][0].0;
    let mut current_vertex = start;
    let mut outgoing_edge = first_edge;
    let mut turns = Vec::new();
    loop {
        let edge = graph.edges[outgoing_edge];
        let next_vertex = if edge.left / 4 == current_vertex {
            edge.right / 4
        } else {
            edge.left / 4
        };
        let incoming_endpoint = if edge.left / 4 == next_vertex {
            edge.left
        } else {
            edge.right
        };
        let next_edge = incidence[next_vertex]
            .iter()
            .find_map(|&(index, _)| (index != outgoing_edge).then_some(index))
            .unwrap();
        let next = graph.edges[next_edge];
        let outgoing_endpoint = if next.left / 4 == next_vertex {
            next.left
        } else {
            next.right
        };
        let incoming_position = incoming_endpoint % 4;
        let outgoing_position = outgoing_endpoint % 4;
        assert!(incoming_position < 3 && outgoing_position < 3);
        turns.push(if outgoing_position == (incoming_position + 1) % 3 {
            'L'
        } else {
            assert_eq!(outgoing_position, (incoming_position + 2) % 3);
            'R'
        });

        current_vertex = next_vertex;
        outgoing_edge = next_edge;
        if current_vertex == start && outgoing_edge == first_edge {
            break;
        }
    }
    turns
}

fn audit_completed_cycle_turn_words() -> (usize, usize) {
    let mut simple_cycles = 0;
    let mut closure_channels = 0;
    for inserted_roads in 0..=3 {
        let graph = MarkedTheta::new(inserted_roads);
        let cycles = simple_cycle_masks(&graph);
        assert_eq!(cycles.len(), 3);
        for &cycle in &cycles {
            let turns = turn_word(&graph, cycle);
            assert!(turns.contains(&'L'));
            assert!(turns.contains(&'R'));
            simple_cycles += 1;
        }

        let mut spanning_trees = 0;
        for tree_mask in 0..(1_u64 << graph.edges.len()) {
            if tree_mask.count_ones() as usize != graph.vertices - 1
                || !graph_is_connected(&graph, tree_mask)
            {
                continue;
            }
            spanning_trees += 1;
            for closing_edge in 0..graph.edges.len() {
                if tree_mask & (1 << closing_edge) != 0 {
                    continue;
                }
                let fundamental: Vec<_> = cycles
                    .iter()
                    .copied()
                    .filter(|cycle| {
                        cycle & (1 << closing_edge) != 0
                            && cycle & !(tree_mask | (1 << closing_edge)) == 0
                    })
                    .collect();
                assert_eq!(fundamental.len(), 1);
                let turns = turn_word(&graph, fundamental[0]);
                assert!(turns.contains(&'L') && turns.contains(&'R'));
                closure_channels += 1;
            }
        }
        let lengths: Vec<_> = (0..3)
            .map(|road| if road < inserted_roads { 2 } else { 1 })
            .collect();
        let predicted_trees =
            lengths[0] * lengths[1] + lengths[0] * lengths[2] + lengths[1] * lengths[2];
        assert_eq!(spanning_trees, predicted_trees);
    }
    (simple_cycles, closure_channels)
}

fn audit_three_leg_cut_atlas() -> BTreeMap<(usize, usize, usize, usize), usize> {
    let graph = MarkedTheta::new(3);
    let mut atlas = BTreeMap::new();
    for cut_mask in 0..(1_u64 << graph.edges.len()) {
        let (removed, components, betti) = cut_topology(&graph, cut_mask);
        let d_sectors = predicted_circuit_sectors(&graph, cut_mask);
        *atlas
            .entry((removed, components, betti, d_sectors))
            .or_insert(0) += 1;
    }
    let expected = BTreeMap::from([
        ((0, 1, 2, 9), 1),
        ((1, 1, 1, 3), 6),
        ((2, 2, 1, 3), 3),
        ((2, 1, 0, 0), 12),
        ((3, 2, 0, 0), 20),
        ((4, 3, 0, 0), 15),
        ((5, 4, 0, 0), 6),
        ((6, 5, 0, 0), 1),
    ]);
    assert_eq!(atlas, expected);
    atlas
}

fn physical_pair(graph: &MarkedTheta, matching: &[(usize, usize)]) -> Vec<(usize, usize)> {
    let mut pairs = Vec::new();
    for &(left, right) in matching {
        if graph.physical_external.contains(&left) && graph.physical_external.contains(&right) {
            let road_of = |endpoint: usize| endpoint / 4 - 2;
            pairs.push(ordered_pair(road_of(left), road_of(right)));
        }
    }
    pairs.sort_unstable();
    pairs
}

fn audit_external_support() -> BTreeMap<(usize, usize), usize> {
    let graph = MarkedTheta::new(3);
    let mut support = BTreeMap::new();
    let mut pair_support = BTreeMap::new();
    for pattern in patterns(graph.vertices) {
        let state = resolved_state(&graph, &pattern, 0);
        let physical_pairs = physical_pair(&graph, &state.external_matching);
        *support
            .entry((state.circuits, physical_pairs.len()))
            .or_insert(0) += 1;
        for pair in physical_pairs {
            *pair_support.entry(pair).or_insert(0) += 1;
        }
    }
    assert_eq!(
        support,
        BTreeMap::from([((0, 0), 174), ((0, 1), 60), ((1, 0), 9)])
    );
    assert_eq!(
        pair_support,
        BTreeMap::from([((0, 1), 20), ((0, 2), 20), ((1, 2), 20)])
    );
    support
}

fn rotate_pattern(pattern: &[usize]) -> Vec<usize> {
    assert_eq!(pattern.len(), 5);
    let mut rotated = vec![0; 5];
    rotated[0] = (pattern[0] + 1) % 3;
    rotated[1] = (pattern[1] + 1) % 3;
    for road in 0..3 {
        rotated[2 + (road + 1) % 3] = pattern[2 + road];
    }
    rotated
}

fn rotate_cut_mask(cut_mask: u64) -> u64 {
    let mut rotated = 0;
    for road in 0..3 {
        for half in 0..2 {
            let old = 2 * road + half;
            let new = 2 * ((road + 1) % 3) + half;
            if cut_mask & (1 << old) != 0 {
                rotated |= 1 << new;
            }
        }
    }
    rotated
}

fn rotate_endpoint(endpoint: usize) -> usize {
    let vertex = endpoint / 4;
    let position = endpoint % 4;
    match vertex {
        0 | 1 => {
            if position == 3 {
                endpoint
            } else {
                flag(vertex, (position + 1) % 3)
            }
        }
        2..=4 => {
            let road = vertex - 2;
            let moved_vertex = 2 + (road + 1) % 3;
            4 * moved_vertex + position
        }
        _ => unreachable!(),
    }
}

fn rotate_matching(matching: &[(usize, usize)]) -> Vec<(usize, usize)> {
    let mut rotated: Vec<_> = matching
        .iter()
        .map(|&(left, right)| ordered_pair(rotate_endpoint(left), rotate_endpoint(right)))
        .collect();
    rotated.sort_unstable();
    rotated
}

fn audit_cyclic_covariance() -> usize {
    let graph = MarkedTheta::new(3);
    let mut squares = 0;
    for pattern in patterns(graph.vertices) {
        let once = rotate_pattern(&pattern);
        let twice = rotate_pattern(&once);
        assert_eq!(rotate_pattern(&twice), pattern);
        for cut_mask in 0..(1_u64 << graph.edges.len()) {
            let state = resolved_state(&graph, &pattern, cut_mask);
            let moved = resolved_state(&graph, &once, rotate_cut_mask(cut_mask));
            assert_eq!(moved.circuits, state.circuits);
            assert_eq!(
                moved.external_matching,
                rotate_matching(&state.external_matching)
            );
            squares += 1;
        }
    }
    squares
}

fn main() {
    audit_local_three_point_counit();
    let cut_squares = audit_family();
    let cut_atlas = audit_three_leg_cut_atlas();
    let external_support = audit_external_support();
    let cyclic_squares = audit_cyclic_covariance();
    let (simple_cycles, closure_channels) = audit_completed_cycle_turn_words();

    // Backus--Figueiredo's first two-loop units obstruction is the one-leg
    // member: four post-scaffolding graph propagators plus its scaffolding pole.
    let one_leg = MarkedTheta::new(1);
    assert_eq!(one_leg.edges.len() + 1, 5);

    println!("Marked-handle resolved counit certificate");
    println!("===========================================");
    for inserted_roads in 0..=3 {
        let graph = MarkedTheta::new(inserted_roads);
        let total = 3_usize.pow(graph.vertices as u32);
        let d_sectors = 2 * inserted_roads + 3;
        println!(
            "  n={inserted_roads}: V={}, E={}, sectors={total}, P(D)={}+{}D",
            graph.vertices,
            graph.edges.len(),
            total - d_sectors,
            d_sectors
        );
    }
    println!("  all family Cut squares: {cut_squares}");
    println!(
        "  three-leg iterated-Cut topology classes: {}",
        cut_atlas.len()
    );
    println!(
        "  three-leg external-support classes: {}",
        external_support.len()
    );
    println!("  populated cyclic covariance squares: {cyclic_squares}");
    println!("  mixed-turn completed simple cycles: {simple_cycles}");
    println!("  mixed-turn completed closure cycles: {closure_channels}");
    println!();
    println!("THREE-LEG FORMULAS");
    println!("  raw closed coefficient: (234+9D)/243 = (26+D)/27");
    println!("  raw one-edge Cut coefficient: (240+3D)/243 = (80+D)/81");
    println!("  raw one-edge Cut defect: 2(D-1)/81");
    println!("  resolved coefficient after D -> 1: 243/243 = 1");
    println!();
    println!("VERDICT");
    println!("  the first three-external-leg handle cell transmutes to its scalar cell");
    println!("  every separating and nonseparating iterated Cut commutes after resolution");
    println!("  raw state evaluation has a nonzero Cut curvature proportional to D-1");
    println!("  external matching support is nonuniform but exactly cyclically balanced");
    println!("  completed theta cycles are mixed-turn (a topology-only diagnostic)");
    println!("  the separate physical-projector audit finds nonzero longitudinal terms");
}
