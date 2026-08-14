//! Exact finite test for an oriented Brauer-skein filler on the marked theta.
//!
//! The degree-zero state carrier is the 3^5 set of local singleton choices on
//! the five cubic vertices of K_{2,3}.  Its elementary degree-one transitions
//! change one coordinate from either local pairing to either other pairing;
//! hence its transition graph is the Hamming graph K_3 square ... square K_3.
//!
//! This file separates three objects that must not be conflated:
//!
//! * the 243 unoriented resolved pairing states;
//! * the free oriented tag module T = Z{c01,c12,c20};
//! * H1(K_{2,3};Z), to which the oriented tags map.
//!
//! The natural state transitions are only a formal carrier.  No Ward/contact
//! coefficient is assigned to them here, and no Cut compatibility is claimed.

use std::collections::{BTreeMap, BTreeSet, VecDeque};

const VERTICES: usize = 5;
const EDGES: usize = 6;
const STATES: usize = 3_usize.pow(VERTICES as u32);

type State = [usize; VERTICES];
type EdgeChain = [i64; EDGES];
type TagChain = [i64; 3];
type H1Coordinates = [i64; 2];

const ROAD_PERMUTATIONS: [[usize; 3]; 6] = [
    [0, 1, 2],
    [1, 2, 0],
    [2, 0, 1],
    [0, 2, 1],
    [2, 1, 0],
    [1, 0, 2],
];

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct GroupElement {
    core_swap: bool,
    roads: [usize; 3],
}

fn group() -> Vec<GroupElement> {
    [false, true]
        .into_iter()
        .flat_map(|core_swap| {
            ROAD_PERMUTATIONS
                .into_iter()
                .map(move |roads| GroupElement { core_swap, roads })
        })
        .collect()
}

fn permutation_sign(permutation: [usize; 3]) -> i64 {
    let inversions = (0..3)
        .flat_map(|left| ((left + 1)..3).map(move |right| (left, right)))
        .filter(|&(left, right)| permutation[left] > permutation[right])
        .count();
    if inversions % 2 == 0 { 1 } else { -1 }
}

fn relation_character(element: GroupElement) -> i64 {
    let core_orientation = if element.core_swap { -1 } else { 1 };
    core_orientation * permutation_sign(element.roads)
}

fn encode(state: State) -> usize {
    state
        .into_iter()
        .enumerate()
        .map(|(coordinate, value)| value * 3_usize.pow(coordinate as u32))
        .sum()
}

fn decode(mut code: usize) -> State {
    assert!(code < STATES);
    std::array::from_fn(|_| {
        let value = code % 3;
        code /= 3;
        value
    })
}

fn state_action(state: State, element: GroupElement) -> State {
    let mut moved = [usize::MAX; VERTICES];
    for core in 0..2 {
        let target_core = if element.core_swap { 1 - core } else { core };
        moved[target_core] = element.roads[state[core]];
    }
    for road in 0..3 {
        let target_road = element.roads[road];
        let singleton = state[2 + road];
        moved[2 + target_road] = if element.core_swap {
            match singleton {
                0 => 2,
                1 => 1,
                2 => 0,
                _ => unreachable!(),
            }
        } else {
            singleton
        };
    }
    assert!(moved.into_iter().all(|value| value < 3));
    moved
}

fn state_neighbors(code: usize) -> Vec<usize> {
    let state = decode(code);
    let mut neighbors = Vec::with_capacity(2 * VERTICES);
    for coordinate in 0..VERTICES {
        for value in 0..3 {
            if value != state[coordinate] {
                let mut next = state;
                next[coordinate] = value;
                neighbors.push(encode(next));
            }
        }
    }
    neighbors.sort_unstable();
    neighbors
}

fn transition_edges() -> Vec<(usize, usize)> {
    let mut result = BTreeSet::new();
    for state in 0..STATES {
        for next in state_neighbors(state) {
            result.insert(if state < next { (state, next) } else { (next, state) });
        }
    }
    result.into_iter().collect()
}

fn state_orbits() -> Vec<BTreeSet<usize>> {
    let elements = group();
    let mut unseen: BTreeSet<_> = (0..STATES).collect();
    let mut orbits = Vec::new();
    while let Some(&seed) = unseen.first() {
        let orbit: BTreeSet<_> = elements
            .iter()
            .map(|&element| encode(state_action(decode(seed), element)))
            .collect();
        for state in &orbit {
            unseen.remove(state);
        }
        orbits.push(orbit);
    }
    orbits
}

fn edge_action(edge: (usize, usize), element: GroupElement) -> (usize, usize) {
    let left = encode(state_action(decode(edge.0), element));
    let right = encode(state_action(decode(edge.1), element));
    if left < right { (left, right) } else { (right, left) }
}

fn edge_orbits(edges: &BTreeSet<(usize, usize)>) -> Vec<BTreeSet<(usize, usize)>> {
    let elements = group();
    let mut unseen = edges.clone();
    let mut orbits = Vec::new();
    while let Some(&seed) = unseen.first() {
        let orbit: BTreeSet<_> = elements
            .iter()
            .map(|&element| edge_action(seed, element))
            .collect();
        assert!(orbit.iter().all(|edge| edges.contains(edge)));
        for edge in &orbit {
            unseen.remove(edge);
        }
        orbits.push(orbit);
    }
    orbits
}

#[derive(Clone)]
struct DisjointSet {
    parent: [usize; 4 * VERTICES],
}

impl DisjointSet {
    fn new() -> Self {
        Self {
            parent: std::array::from_fn(|index| index),
        }
    }

    fn find(&mut self, node: usize) -> usize {
        if self.parent[node] != node {
            self.parent[node] = self.find(self.parent[node]);
        }
        self.parent[node]
    }

    fn join(&mut self, left: usize, right: usize) {
        let left = self.find(left);
        let right = self.find(right);
        if left != right {
            self.parent[right] = left;
        }
    }
}

fn flag(vertex: usize, position: usize) -> usize {
    4 * vertex + position
}

fn auxiliary(vertex: usize) -> usize {
    4 * vertex + 3
}

fn graph_endpoints(slot: usize) -> (usize, usize) {
    let core = slot % 2;
    let road = slot / 2;
    (
        flag(core, road),
        flag(2 + road, if core == 0 { 0 } else { 2 }),
    )
}

fn resolved_circuit_support(pattern: State) -> Option<u8> {
    let mut sets = DisjointSet::new();
    for (vertex, singleton) in pattern.into_iter().enumerate() {
        sets.join(auxiliary(vertex), flag(vertex, singleton));
        let paired: Vec<_> = (0..3).filter(|&position| position != singleton).collect();
        sets.join(flag(vertex, paired[0]), flag(vertex, paired[1]));
    }
    for slot in 0..EDGES {
        let (left, right) = graph_endpoints(slot);
        sets.join(left, right);
    }

    let external: BTreeSet<_> = (0..VERTICES)
        .map(auxiliary)
        .chain((0..3).map(|road| flag(2 + road, 1)))
        .collect();
    let external_roots: BTreeSet<_> = external
        .into_iter()
        .map(|endpoint| sets.find(endpoint))
        .collect();
    let all_roots: BTreeSet<_> = (0..4 * VERTICES).map(|node| sets.find(node)).collect();
    let closed: Vec<_> = all_roots.difference(&external_roots).copied().collect();
    assert!(closed.len() <= 1);
    closed.first().map(|&root| {
        (0..EDGES).fold(0_u8, |mask, slot| {
            let (left, _) = graph_endpoints(slot);
            if sets.find(left) == root { mask | (1 << slot) } else { mask }
        })
    })
}

fn road_pair_support(first: usize, second: usize) -> u8 {
    [first, second]
        .into_iter()
        .flat_map(|road| [2 * road, 2 * road + 1])
        .fold(0_u8, |mask, slot| mask | (1 << slot))
}

fn oriented_supports() -> [u8; 3] {
    [
        road_pair_support(0, 1),
        road_pair_support(1, 2),
        road_pair_support(2, 0),
    ]
}

fn edge(core: usize, road: usize) -> usize {
    2 * road + core
}

fn road_cycle(first: usize, second: usize) -> EdgeChain {
    let mut result = [0; EDGES];
    result[edge(0, first)] += 1;
    result[edge(1, first)] -= 1;
    result[edge(0, second)] -= 1;
    result[edge(1, second)] += 1;
    result
}

fn tag_cycles() -> [EdgeChain; 3] {
    [road_cycle(0, 1), road_cycle(1, 2), road_cycle(2, 0)]
}

fn graph_action(chain: EdgeChain, element: GroupElement) -> EdgeChain {
    let mut result = [0; EDGES];
    for slot in 0..EDGES {
        let core = slot % 2;
        let road = slot / 2;
        let target = edge(
            if element.core_swap { 1 - core } else { core },
            element.roads[road],
        );
        result[target] += chain[slot];
    }
    result
}

fn tag_action(chain: TagChain, element: GroupElement) -> TagChain {
    let tags = tag_cycles();
    let mut result = [0; 3];
    for (source, coefficient) in chain.into_iter().enumerate() {
        let moved = graph_action(tags[source], element);
        let matches: Vec<_> = tags
            .iter()
            .enumerate()
            .filter_map(|(target, &tag)| {
                if moved == tag {
                    Some((target, 1))
                } else if moved == tag.map(|entry| -entry) {
                    Some((target, -1))
                } else {
                    None
                }
            })
            .collect();
        assert_eq!(matches.len(), 1);
        result[matches[0].0] += matches[0].1 * coefficient;
    }
    result
}

fn tag_class(tags: TagChain) -> H1Coordinates {
    // c01=(1,-1), c12=(0,1), c20=(-1,0).
    [tags[0] - tags[2], -tags[0] + tags[1]]
}

fn h1_action(coordinates: H1Coordinates, element: GroupElement) -> H1Coordinates {
    let [p, q] = coordinates;
    let chain = [p, -p, q, -q, -p - q, p + q];
    let moved = graph_action(chain, element);
    assert_eq!(moved[1], -moved[0]);
    assert_eq!(moved[3], -moved[2]);
    assert_eq!(moved[4], -moved[0] - moved[2]);
    assert_eq!(moved[5], moved[0] + moved[2]);
    [moved[0], moved[2]]
}

fn h1_action_matrix(element: GroupElement) -> [[i64; 2]; 2] {
    let first = h1_action([1, 0], element);
    let second = h1_action([0, 1], element);
    [[first[0], second[0]], [first[1], second[1]]]
}

fn determinant_2(matrix: [[i64; 2]; 2]) -> i64 {
    matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
}

fn multiply_tag_matrix(matrix: [[i64; 2]; 3], vector: H1Coordinates) -> TagChain {
    std::array::from_fn(|row| matrix[row][0] * vector[0] + matrix[row][1] * vector[1])
}

fn rational_section_numerator(coordinates: H1Coordinates) -> TagChain {
    let [p, q] = coordinates;
    [p - q, p + 2 * q, -2 * p - q]
}

fn audit_tag_resolution() -> (usize, usize, usize) {
    let relation = [1, 1, 1];
    assert_eq!(tag_class(relation), [0, 0]);

    // The 2x2 minor on c01,c12 is one, so the class map is saturated.
    let class_minors = [1_i64, -1, 1];
    assert_eq!(class_minors.into_iter().fold(0_i64, gcd).abs(), 1);

    // A pointed integral (non-equivariant) section: (p,q) |-> (p,p+q,0).
    let pointed_section = [[1, 0], [1, 1], [0, 0]];
    for basis in [[1, 0], [0, 1]] {
        assert_eq!(tag_class(multiply_tag_matrix(pointed_section, basis)), basis);
    }

    let mut covariance_checks = 0;
    let mut relation_character_checks = 0;
    let mut determinant_checks = 0;
    for element in group() {
        assert_eq!(tag_action(relation, element), relation.map(|x| relation_character(element) * x));
        relation_character_checks += 1;

        let h1_matrix = h1_action_matrix(element);
        assert_eq!(determinant_2(h1_matrix), permutation_sign(element.roads));
        if element.core_swap && element.roads == [0, 1, 2] {
            // Core swap is -I on H1, hence +1 on det H1, but -1 on K_rel.
            assert_eq!(h1_matrix, [[-1, 0], [0, -1]]);
            assert_eq!(determinant_2(h1_matrix), 1);
            assert_eq!(relation_character(element), -1);
        }
        determinant_checks += 1;

        for basis in [[1, 0], [0, 1]] {
            let moved_numerator = rational_section_numerator(h1_action(basis, element));
            let numerator_moved = tag_action(rational_section_numerator(basis), element);
            assert_eq!(moved_numerator, numerator_moved);
            assert_eq!(tag_class(rational_section_numerator(basis)), basis.map(|x| 3 * x));
            covariance_checks += 1;
        }
    }
    assert_eq!((covariance_checks, relation_character_checks, determinant_checks), (24, 12, 12));

    // The unique equivariant rational section has the displayed numerator /3.
    // Uniqueness follows because an equivariant difference lands in K_rel;
    // rotation (012) forces the two coefficients of H1 -> K_rel to vanish.
    let rotation = GroupElement { core_swap: false, roads: [1, 2, 0] };
    let rotation_matrix = h1_action_matrix(rotation);
    let chi = relation_character(rotation);
    let difference_constraints = [
        [rotation_matrix[0][0] - chi, rotation_matrix[1][0]],
        [rotation_matrix[0][1], rotation_matrix[1][1] - chi],
    ];
    assert_ne!(determinant_2(difference_constraints), 0);
    assert!(rational_section_numerator([1, 0]).into_iter().any(|x| x % 3 != 0));

    // The equivariant complement T_0={sum coefficients=0}, together with the
    // relation line, has index 3 in T.  Thus no integral equivariant splitting
    // exists, although the rational one does.
    let complement_and_relation = [[1_i64, 1, 0], [1, -1, 1], [1, 0, -1]];
    let splitting_index = determinant_3(complement_and_relation).abs() as usize;
    assert_eq!(splitting_index, 3);

    (covariance_checks, splitting_index, determinant_checks)
}

fn gcd(mut left: i64, mut right: i64) -> i64 {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        (left, right) = (right, left % right);
    }
    left
}

fn determinant_3(matrix: [[i64; 3]; 3]) -> i64 {
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
}

fn orbit_histogram<T>(orbits: &[BTreeSet<T>]) -> BTreeMap<usize, usize> {
    let mut result = BTreeMap::new();
    for orbit in orbits {
        *result.entry(orbit.len()).or_insert(0) += 1;
    }
    result
}

fn audit_state_graph() -> (usize, usize, BTreeMap<usize, usize>, BTreeMap<usize, usize>) {
    let edges = transition_edges();
    assert_eq!(edges.len(), 1215);
    let edge_set: BTreeSet<_> = edges.iter().copied().collect();

    let mut distance = vec![usize::MAX; STATES];
    let mut parent = vec![usize::MAX; STATES];
    let mut queue = VecDeque::from([0]);
    distance[0] = 0;
    let mut discovery_order = vec![0];
    while let Some(state) = queue.pop_front() {
        for next in state_neighbors(state) {
            if distance[next] == usize::MAX {
                distance[next] = distance[state] + 1;
                parent[next] = state;
                discovery_order.push(next);
                queue.push_back(next);
            }
        }
    }
    assert_eq!(discovery_order.len(), STATES);
    assert_eq!(parent.iter().filter(|&&value| value != usize::MAX).count(), STATES - 1);

    // Order the reduced incidence rows and tree columns by discovery time.
    // Every parent precedes its child, so the reduced tree incidence is
    // triangular with diagonal +1.  This constructively proves rank 242 and
    // Smith invariants all one: im(d1) is the saturated augmentation lattice.
    let discovery_index: BTreeMap<_, _> = discovery_order
        .iter()
        .enumerate()
        .map(|(index, &state)| (state, index))
        .collect();
    for &child in discovery_order.iter().skip(1) {
        assert!(discovery_index[&parent[child]] < discovery_index[&child]);
        let tree_edge = if parent[child] < child {
            (parent[child], child)
        } else {
            (child, parent[child])
        };
        assert!(edge_set.contains(&tree_edge));
    }

    let state_orbits = state_orbits();
    let edge_orbits = edge_orbits(&edge_set);
    assert_eq!(state_orbits.iter().map(BTreeSet::len).sum::<usize>(), STATES);
    assert_eq!(edge_orbits.iter().map(BTreeSet::len).sum::<usize>(), edges.len());
    (
        STATES - 1,
        edges.len() - (STATES - 1),
        orbit_histogram(&state_orbits),
        orbit_histogram(&edge_orbits),
    )
}

fn path_chain(start: usize, target: usize) -> BTreeMap<(usize, usize), i64> {
    let mut current = decode(start);
    let target_state = decode(target);
    let mut chain = BTreeMap::new();
    for coordinate in 0..VERTICES {
        if current[coordinate] == target_state[coordinate] {
            continue;
        }
        let source_code = encode(current);
        current[coordinate] = target_state[coordinate];
        let target_code = encode(current);
        let (edge, coefficient) = if source_code < target_code {
            ((source_code, target_code), 1)
        } else {
            ((target_code, source_code), -1)
        };
        *chain.entry(edge).or_insert(0) += coefficient;
    }
    assert_eq!(encode(current), target);
    chain.retain(|_, coefficient| *coefficient != 0);
    chain
}

fn add_chain(target: &mut BTreeMap<(usize, usize), i64>, source: BTreeMap<(usize, usize), i64>) {
    for (edge, coefficient) in source {
        *target.entry(edge).or_insert(0) += coefficient;
    }
    target.retain(|_, coefficient| *coefficient != 0);
}

fn boundary(chain: &BTreeMap<(usize, usize), i64>) -> BTreeMap<usize, i64> {
    let mut result = BTreeMap::new();
    for (&(left, right), &coefficient) in chain {
        *result.entry(left).or_insert(0) -= coefficient;
        *result.entry(right).or_insert(0) += coefficient;
    }
    result.retain(|_, coefficient| *coefficient != 0);
    result
}

fn audit_circuit_states_and_pointed_filler() -> (
    BTreeMap<u8, usize>,
    BTreeMap<usize, usize>,
    usize,
    usize,
) {
    let supports = oriented_supports();
    let mut histogram = BTreeMap::new();
    let mut states_by_support = BTreeMap::<u8, Vec<usize>>::new();
    for code in 0..STATES {
        if let Some(support) = resolved_circuit_support(decode(code)) {
            *histogram.entry(support).or_insert(0) += 1;
            states_by_support.entry(support).or_default().push(code);
        }
    }
    assert_eq!(histogram.len(), 3);
    assert_eq!(histogram.values().sum::<usize>(), 9);
    assert!(supports.into_iter().all(|support| histogram[&support] == 3));

    let circuit_states: BTreeSet<_> = states_by_support
        .values()
        .flat_map(|states| states.iter().copied())
        .collect();
    let mut unseen = circuit_states.clone();
    let elements = group();
    let mut circuit_orbits = Vec::new();
    while let Some(&seed) = unseen.first() {
        let orbit: BTreeSet<_> = elements
            .iter()
            .map(|&element| encode(state_action(decode(seed), element)))
            .collect();
        assert!(orbit.iter().all(|state| circuit_states.contains(state)));
        for state in &orbit {
            unseen.remove(state);
        }
        circuit_orbits.push(orbit);
    }

    // The support carrier is unoriented: a road reflection can fix a support
    // while negating the corresponding oriented tag class.
    let reflection = GroupElement { core_swap: false, roads: [0, 2, 1] };
    let fixed_support = road_pair_support(1, 2);
    let moved_fixed_support = road_pair_support(reflection.roads[1], reflection.roads[2]);
    assert_eq!(fixed_support, moved_fixed_support);
    assert_eq!(tag_action([0, 1, 0], reflection), [0, -1, 0]);

    // A pointed reduced model can fill the tag relation integrally.  Choose a
    // non-circuit base and one state over each support.  The boundary is
    // sum_i [representative_i] - 3[base], not the unpointed diagonal itself.
    let base = (0..STATES)
        .find(|&code| resolved_circuit_support(decode(code)).is_none())
        .expect("non-circuit base state");
    let representatives: Vec<_> = oriented_supports()
        .into_iter()
        .map(|support| states_by_support[&support][0])
        .collect();
    let mut filler = BTreeMap::new();
    for &representative in &representatives {
        add_chain(&mut filler, path_chain(base, representative));
    }
    let expected_boundary: BTreeMap<_, _> = representatives
        .iter()
        .copied()
        .map(|state| (state, 1))
        .chain(std::iter::once((base, -3)))
        .fold(BTreeMap::new(), |mut map, (state, coefficient)| {
            *map.entry(state).or_insert(0) += coefficient;
            map
        });
    assert_eq!(boundary(&filler), expected_boundary);
    assert_eq!(expected_boundary.values().sum::<i64>(), 0);

    // The raw positive diagonal has augmentation 3 and therefore cannot be a
    // boundary in the ordinary state transition complex.
    assert_eq!(representatives.len(), 3);
    let raw_diagonal_augmentation = representatives.len();
    assert_ne!(raw_diagonal_augmentation, 0);

    (
        histogram,
        orbit_histogram(&circuit_orbits),
        filler.values().map(|value| value.unsigned_abs() as usize).sum(),
        raw_diagonal_augmentation,
    )
}

fn main() {
    let (boundary_rank, cycle_rank, state_orbits, edge_orbits) = audit_state_graph();
    let (tag_covariance, splitting_index, determinant_checks) = audit_tag_resolution();
    let (circuit_histogram, circuit_orbits, pointed_filler_size, raw_augmentation) =
        audit_circuit_states_and_pointed_filler();

    println!("Oriented Brauer-skein filler certificate");
    println!("=========================================");
    println!("  resolved states / elementary edges:       {STATES}/1215");
    println!("  boundary rank / graph-cycle rank:          {boundary_rank}/{cycle_rank}");
    println!("  boundary lattice saturation index:         1");
    println!("  S2xD3 state orbit histogram:                {state_orbits:?}");
    println!("  S2xD3 transition-edge orbit histogram:      {edge_orbits:?}");
    println!("  resolved circuit support histogram:         {circuit_histogram:?}");
    println!("  resolved circuit-state orbit histogram:     {circuit_orbits:?}");
    println!("  pointed integral filler l1-size:             {pointed_filler_size}");
    println!("  raw oriented-tag diagonal augmentation:     {raw_augmentation}");
    println!("  tag-section equivariance checks over Q:      {tag_covariance}");
    println!("  integral equivariant complement index:       {splitting_index}");
    println!("  det(H1)/relation-character checks:           {determinant_checks}");
    println!();
    println!("VERDICT");
    println!("  0 -> K_rel -> Z^3_tags -> H1(K2,3;Z) -> 0 is saturated and S2xD3-equivariant");
    println!("  K_rel has character (-1)^core_swap det(road), not det(H1) alone");
    println!("  a pointed integral section/filler exists, but no integral equivariant section exists");
    println!("  the unique equivariant section exists over Q and has denominator 3");
    println!("  the two-term resolution already models additive H1 without choosing a section");
    println!("  the ordinary 243-state transition graph cannot bound the unpointed positive diagonal");
    println!("  a crossing/smoothing cell remains relevant only for multiplicative/two-cycle coherence");
    println!("  transitions are formal state-carrier edges, not derived Ward/contact generators");
}
