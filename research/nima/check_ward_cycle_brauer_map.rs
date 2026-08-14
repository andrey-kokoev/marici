//! Exact graph-homology bridge between the equal-endpoint Ward kernel and the
//! individually tagged closed circuits of the marked-theta Brauer carrier.
//!
//! This certificate deliberately stops before claiming a physical chain map.
//! It proves an integral, symmetry-compatible identification of the Ward
//! kernel with graph H1 and a canonical class map from individual oriented
//! circuit tags to H1.  It also proves that the latter map has no integral
//! D3-equivariant additive section: resolved noncrossing curves are not an
//! additive model of H1.  The earlier surface carrier records a closed circuit
//! only by the formal factor D; here we retain its K_{2,3} support as a tag,
//! but do not evaluate D -> 1 and do not manufacture scalar coefficients.

use std::collections::{BTreeMap, BTreeSet};

const VERTICES: usize = 5;
const EDGES: usize = 6;
const WARD_QUOTIENT: usize = 7;

type Chain = [i64; EDGES];
type VertexChain = [i64; VERTICES];
type WardChain = [i64; WARD_QUOTIENT];

const ROAD_PERMUTATIONS: [[usize; 3]; 6] = [
    [0, 1, 2],
    [1, 2, 0],
    [2, 0, 1],
    [0, 2, 1],
    [2, 1, 0],
    [1, 0, 2],
];

fn edge(core: usize, road: usize) -> usize {
    2 * road + core
}

fn edge_vertices(slot: usize) -> (usize, usize) {
    (slot % 2, 2 + slot / 2)
}

fn incidence(chain: Chain) -> VertexChain {
    let mut boundary = [0; VERTICES];
    for (slot, coefficient) in chain.into_iter().enumerate() {
        let (tail, head) = edge_vertices(slot);
        boundary[tail] -= coefficient;
        boundary[head] += coefficient;
    }
    boundary
}

fn chain_from_coordinates(coordinates: [i64; 2]) -> Chain {
    let [p, q] = coordinates;
    [p, -p, q, -q, -p - q, p + q]
}

fn chain_coordinates(chain: Chain) -> [i64; 2] {
    assert_eq!(incidence(chain), [0; VERTICES]);
    let coordinates = [chain[edge(0, 0)], chain[edge(0, 1)]];
    assert_eq!(chain_from_coordinates(coordinates), chain);
    coordinates
}

fn chain_add_scaled(mut target: Chain, source: Chain, coefficient: i64) -> Chain {
    for slot in 0..EDGES {
        target[slot] += coefficient * source[slot];
    }
    target
}

fn h1_basis() -> [Chain; 2] {
    [
        chain_from_coordinates([1, 0]),
        chain_from_coordinates([0, 1]),
    ]
}

// Quotient Ward coordinates are
//   (l_00,l_01,l_10,l_11,q_0,q_1,q_2),
// after eliminating l_c2 using l_c0+l_c1+l_c2=0.  The contact map is
//   l_cr |-> e_{c,r+1}-e_{c,r+2}, q_r |-> e_{0,r}-e_{1,r}.
fn ward_contact_column(column: usize) -> Chain {
    let mut result = [0; EDGES];
    match column {
        0..=3 => {
            let core = column / 2;
            let road = column % 2;
            result[edge(core, (road + 1) % 3)] += 1;
            result[edge(core, (road + 2) % 3)] -= 1;
        }
        4..=6 => {
            let road = column - 4;
            result[edge(0, road)] += 1;
            result[edge(1, road)] -= 1;
        }
        _ => unreachable!(),
    }
    result
}

fn ward_contact(chain: WardChain) -> Chain {
    let mut result = [0; EDGES];
    for (column, coefficient) in chain.into_iter().enumerate() {
        result = chain_add_scaled(result, ward_contact_column(column), coefficient);
    }
    result
}

fn combinations(size: usize, choose: usize) -> Vec<Vec<usize>> {
    fn recurse(
        next: usize,
        size: usize,
        remaining: usize,
        current: &mut Vec<usize>,
        output: &mut Vec<Vec<usize>>,
    ) {
        if remaining == 0 {
            output.push(current.clone());
            return;
        }
        for value in next..=size - remaining {
            current.push(value);
            recurse(value + 1, size, remaining - 1, current, output);
            current.pop();
        }
    }
    let mut output = Vec::new();
    recurse(0, size, choose, &mut Vec::new(), &mut output);
    output
}

fn determinant(mut matrix: Vec<Vec<i128>>) -> i128 {
    let size = matrix.len();
    assert!(matrix.iter().all(|row| row.len() == size));
    if size == 0 {
        return 1;
    }
    let mut sign = 1_i128;
    let mut previous = 1_i128;
    for pivot_index in 0..size - 1 {
        let Some(pivot_row) = (pivot_index..size).find(|&row| matrix[row][pivot_index] != 0) else {
            return 0;
        };
        if pivot_row != pivot_index {
            matrix.swap(pivot_row, pivot_index);
            sign = -sign;
        }
        let pivot = matrix[pivot_index][pivot_index];
        for row in pivot_index + 1..size {
            for column in pivot_index + 1..size {
                let numerator = matrix[row][column] * pivot
                    - matrix[row][pivot_index] * matrix[pivot_index][column];
                assert_eq!(numerator % previous, 0);
                matrix[row][column] = numerator / previous;
            }
        }
        previous = pivot;
    }
    sign * matrix[size - 1][size - 1]
}

fn minors(matrix: &[Vec<i64>], size: usize) -> Vec<i128> {
    assert!(!matrix.is_empty());
    let columns = matrix[0].len();
    assert!(matrix.iter().all(|row| row.len() == columns));
    let mut result = Vec::new();
    for rows in combinations(matrix.len(), size) {
        for selected_columns in combinations(columns, size) {
            result.push(determinant(
                rows.iter()
                    .map(|&row| {
                        selected_columns
                            .iter()
                            .map(|&column| i128::from(matrix[row][column]))
                            .collect()
                    })
                    .collect(),
            ));
        }
    }
    result
}

fn integer_rank(matrix: &[Vec<i64>]) -> usize {
    let maximum = matrix.len().min(matrix[0].len());
    (1..=maximum)
        .rev()
        .find(|&size| minors(matrix, size).into_iter().any(|value| value != 0))
        .unwrap_or(0)
}

fn gcd(mut left: i128, mut right: i128) -> i128 {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        (left, right) = (right, left % right);
    }
    left
}

fn maximal_minor_content(matrix: &[Vec<i64>], rank: usize) -> i128 {
    minors(matrix, rank).into_iter().fold(0, gcd)
}

fn incidence_matrix() -> Vec<Vec<i64>> {
    let columns: Vec<_> = (0..EDGES)
        .map(|slot| {
            let mut unit = [0; EDGES];
            unit[slot] = 1;
            incidence(unit)
        })
        .collect();
    (0..VERTICES)
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect()
}

fn ward_contact_matrix() -> Vec<Vec<i64>> {
    let columns: Vec<_> = (0..WARD_QUOTIENT).map(ward_contact_column).collect();
    (0..EDGES)
        .map(|row| columns.iter().map(|column| column[row]).collect())
        .collect()
}

// Integral bridge in the quotient chart that eliminates l_c2.  If x has H1
// coordinates (p,q), the unimodular D3-intertwiner sends them to Ward-kernel
// parameters (a,b)=(q,-p).  Contact cancellation then uniquely fixes the
// other coordinates.  The quarter-turn chart change is essential: simply
// identifying (p,q) with (a,b) is not D3-equivariant.
fn theta(chain: Chain) -> WardChain {
    let [p, q] = chain_coordinates(chain);
    let (a, b) = (q, -p);
    [a, b, -a, -b, b, -a, a - b]
}

fn theta_inverse(ward: WardChain) -> Chain {
    assert_eq!(ward_contact(ward), [0; EDGES]);
    let chain = chain_from_coordinates([-ward[1], ward[0]]);
    assert_eq!(theta(chain), ward);
    chain
}

fn permutation_sign(permutation: [usize; 3]) -> i64 {
    let inversions = (0..3)
        .flat_map(|left| ((left + 1)..3).map(move |right| (left, right)))
        .filter(|&(left, right)| permutation[left] > permutation[right])
        .count();
    if inversions % 2 == 0 {
        1
    } else {
        -1
    }
}

fn graph_action(chain: Chain, core_swap: bool, roads: [usize; 3]) -> Chain {
    let mut result = [0; EDGES];
    for slot in 0..EDGES {
        let core = slot % 2;
        let road = slot / 2;
        let moved = edge(if core_swap { 1 - core } else { core }, roads[road]);
        result[moved] += chain[slot];
    }
    assert_eq!(incidence(result), [0; VERTICES]);
    result
}

fn twisted_graph_action(chain: Chain, core_swap: bool, roads: [usize; 3]) -> Chain {
    let sign = permutation_sign(roads);
    graph_action(chain, core_swap, roads).map(|coefficient| sign * coefficient)
}

fn ward_action(ward: WardChain, core_swap: bool, roads: [usize; 3]) -> WardChain {
    // Lift the chosen quotient representative to nine local marks.
    let full = [
        ward[0], ward[1], 0, ward[2], ward[3], 0, ward[4], ward[5], ward[6],
    ];
    let mut moved = [0; 9];
    let road_sign = permutation_sign(roads);
    for core in 0..2 {
        for road in 0..3 {
            let source = 3 * core + road;
            let target = 3 * (if core_swap { 1 - core } else { core }) + roads[road];
            moved[target] += road_sign * full[source];
        }
    }
    for road in 0..3 {
        let sign = if core_swap { -1 } else { 1 };
        moved[6 + roads[road]] += sign * full[6 + road];
    }
    // Reduce modulo each local cyclic relation.
    [
        moved[0] - moved[2],
        moved[1] - moved[2],
        moved[3] - moved[5],
        moved[4] - moved[5],
        moved[6],
        moved[7],
        moved[8],
    ]
}

fn matrix_det(matrix: [[i64; 2]; 2]) -> i64 {
    matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
}

fn action_matrix(core_swap: bool, roads: [usize; 3], twisted: bool) -> [[i64; 2]; 2] {
    let basis = h1_basis();
    let images = basis.map(|cycle| {
        chain_coordinates(if twisted {
            twisted_graph_action(cycle, core_swap, roads)
        } else {
            graph_action(cycle, core_swap, roads)
        })
    });
    [[images[0][0], images[1][0]], [images[0][1], images[1][1]]]
}

fn audit_integral_bridge() -> (usize, usize) {
    let graph_incidence = incidence_matrix();
    let incidence_rank = integer_rank(&graph_incidence);
    assert_eq!(incidence_rank, 4);
    assert_eq!(maximal_minor_content(&graph_incidence, incidence_rank), 1);
    assert_eq!(EDGES - incidence_rank, 2);

    let contact = ward_contact_matrix();
    let contact_rank = integer_rank(&contact);
    assert_eq!(contact_rank, 5);
    assert_eq!(maximal_minor_content(&contact, contact_rank), 1);
    assert_eq!(WARD_QUOTIENT - contact_rank, 2);

    let basis = h1_basis();
    for (index, cycle) in basis.into_iter().enumerate() {
        assert_eq!(incidence(cycle), [0; VERTICES]);
        assert_eq!(chain_coordinates(cycle)[index], 1);
        let ward = theta(cycle);
        assert_eq!(ward_contact(ward), [0; EDGES]);
        assert_eq!(theta_inverse(ward), cycle);
    }

    // These are the primitive kernel columns found directly from the
    // equal-endpoint quotient contact matrix.  Projection to (l_00,l_01) is
    // the identity, so theta and theta_inverse are integral and saturated.
    assert_eq!(
        h1_basis().map(theta),
        [[0, -1, 0, 1, -1, 0, 1], [1, 0, -1, 0, 0, -1, 1],]
    );

    let mut equivariant_checks = 0;
    let mut sign_twisted_failures = 0;
    for core_swap in [false, true] {
        for roads in ROAD_PERMUTATIONS {
            for cycle in h1_basis() {
                let moved_ward = ward_action(theta(cycle), core_swap, roads);
                assert_eq!(
                    moved_ward,
                    theta(graph_action(cycle, core_swap, roads)),
                    "covariance failed: core_swap={core_swap}, roads={roads:?}, cycle={cycle:?}"
                );
                if moved_ward != theta(twisted_graph_action(cycle, core_swap, roads)) {
                    sign_twisted_failures += 1;
                }
                equivariant_checks += 1;
            }
        }
    }
    assert_eq!(equivariant_checks, 24);
    assert_eq!(sign_twisted_failures, 12);
    (equivariant_checks, sign_twisted_failures)
}

fn graph_is_connected(mask: u8) -> bool {
    let mut seen = BTreeSet::from([0]);
    loop {
        let before = seen.len();
        for slot in 0..EDGES {
            if mask & (1 << slot) == 0 {
                continue;
            }
            let (left, right) = edge_vertices(slot);
            if seen.contains(&left) {
                seen.insert(right);
            }
            if seen.contains(&right) {
                seen.insert(left);
            }
        }
        if seen.len() == before {
            break;
        }
    }
    seen.len() == VERTICES
}

fn spanning_trees() -> Vec<u8> {
    let trees: Vec<_> = (0_u8..(1 << EDGES))
        .filter(|mask| mask.count_ones() as usize == VERTICES - 1)
        .filter(|&mask| graph_is_connected(mask))
        .collect();
    assert_eq!(trees.len(), 12);
    trees
}

fn tree_lift(tree: u8, wanted: VertexChain) -> Chain {
    let tree_edges: Vec<_> = (0..EDGES).filter(|slot| tree & (1 << slot) != 0).collect();
    assert_eq!(tree_edges.len(), 4);
    let mut solutions = Vec::new();
    for code in 0..3_usize.pow(4) {
        let mut rest = code;
        let mut candidate = [0; EDGES];
        for &slot in &tree_edges {
            candidate[slot] = i64::try_from(rest % 3).expect("ternary digit") - 1;
            rest /= 3;
        }
        if incidence(candidate) == wanted {
            solutions.push(candidate);
        }
    }
    assert_eq!(solutions.len(), 1);
    solutions[0]
}

fn fundamental_cycle(tree: u8, chord: usize) -> Chain {
    assert_eq!(tree & (1 << chord), 0);
    let mut unit = [0; EDGES];
    unit[chord] = 1;
    let cycle = chain_add_scaled(unit, tree_lift(tree, incidence(unit)), -1);
    assert_eq!(incidence(cycle), [0; VERTICES]);
    assert_eq!(cycle.into_iter().filter(|&value| value != 0).count(), 4);
    cycle
}

fn basis_matrix(first: Chain, second: Chain) -> [[i64; 2]; 2] {
    let first = chain_coordinates(first);
    let second = chain_coordinates(second);
    [[first[0], second[0]], [first[1], second[1]]]
}

fn matrix_inverse_unimodular(matrix: [[i64; 2]; 2]) -> [[i64; 2]; 2] {
    let determinant = matrix_det(matrix);
    assert!(determinant.abs() == 1);
    [
        [matrix[1][1] / determinant, -matrix[0][1] / determinant],
        [-matrix[1][0] / determinant, matrix[0][0] / determinant],
    ]
}

fn matrix_multiply(left: [[i64; 2]; 2], right: [[i64; 2]; 2]) -> [[i64; 2]; 2] {
    std::array::from_fn(|row| {
        std::array::from_fn(|column| {
            (0..2)
                .map(|middle| left[row][middle] * right[middle][column])
                .sum()
        })
    })
}

fn audit_tree_changes() -> (usize, usize, usize) {
    let trees = spanning_trees();
    let mut bases = BTreeMap::new();
    let mut chord_generators = 0;
    for &tree in &trees {
        let chords: Vec<_> = (0..EDGES).filter(|slot| tree & (1 << slot) == 0).collect();
        assert_eq!(chords.len(), 2);
        let cycles = [
            fundamental_cycle(tree, chords[0]),
            fundamental_cycle(tree, chords[1]),
        ];
        let matrix = basis_matrix(cycles[0], cycles[1]);
        assert!(matrix_det(matrix).abs() == 1);
        for cycle in cycles {
            assert_eq!(theta_inverse(theta(cycle)), cycle);
            chord_generators += 1;
        }
        bases.insert(tree, matrix);
    }

    let mut changes = 0;
    for source in bases.values() {
        for target in bases.values() {
            let transition = matrix_multiply(matrix_inverse_unimodular(*target), *source);
            assert!(matrix_det(transition).abs() == 1);
            changes += 1;
        }
    }
    assert_eq!(changes, 144);
    (trees.len(), chord_generators, changes)
}

fn ribbon_signature(mask: u8) -> (usize, usize) {
    assert!(graph_is_connected(mask));
    let mut alpha = [usize::MAX; 3 * VERTICES];
    let mut active = BTreeSet::new();
    for slot in 0..EDGES {
        if mask & (1 << slot) == 0 {
            continue;
        }
        let core = slot % 2;
        let road = slot / 2;
        let left = 3 * core + road;
        let right = 3 * (2 + road) + if core == 0 { 0 } else { 2 };
        alpha[left] = right;
        alpha[right] = left;
        active.insert(left);
        active.insert(right);
    }

    let mut sigma = [usize::MAX; 3 * VERTICES];
    for vertex in 0..VERTICES {
        let positions: Vec<_> = (0..3)
            .filter(|position| active.contains(&(3 * vertex + position)))
            .collect();
        assert!(!positions.is_empty());
        for (index, &position) in positions.iter().enumerate() {
            sigma[3 * vertex + position] = 3 * vertex + positions[(index + 1) % positions.len()];
        }
    }

    let mut seen = BTreeSet::new();
    let mut boundaries = 0;
    for &start in &active {
        if seen.contains(&start) {
            continue;
        }
        boundaries += 1;
        let mut current = start;
        while seen.insert(current) {
            current = sigma[alpha[current]];
        }
        assert_eq!(current, start);
    }
    let euler = VERTICES as i64 - i64::from(mask.count_ones());
    let twice_genus = 2 - boundaries as i64 - euler;
    assert!(twice_genus >= 0 && twice_genus % 2 == 0);
    ((twice_genus / 2) as usize, boundaries)
}

fn audit_addition_orders() -> (usize, usize) {
    let full = (1_u8 << EDGES) - 1;
    assert_eq!(ribbon_signature(full), (1, 1));
    let mut paths = 0;
    let mut determinant_swaps = 0;
    for tree in spanning_trees() {
        assert_eq!(ribbon_signature(tree), (0, 1));
        let chords: Vec<_> = (0..EDGES).filter(|slot| tree & (1 << slot) == 0).collect();
        let first_cycle = fundamental_cycle(tree, chords[0]);
        let second_cycle = fundamental_cycle(tree, chords[1]);
        let forward = basis_matrix(first_cycle, second_cycle);
        let reverse = basis_matrix(second_cycle, first_cycle);
        assert_eq!(matrix_det(reverse), -matrix_det(forward));
        determinant_swaps += 1;
        for first in chords {
            assert_eq!(ribbon_signature(tree | (1 << first)), (0, 2));
            assert_eq!(ribbon_signature(full), (1, 1));
            paths += 1;
        }
    }
    assert_eq!((paths, determinant_swaps), (24, 12));
    (paths, determinant_swaps)
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct CircuitTag {
    support: u8,
    primitive_cycle: Chain,
}

fn canonical_orientation(mut cycle: Chain) -> (i64, Chain) {
    let first = cycle
        .into_iter()
        .find(|&coefficient| coefficient != 0)
        .unwrap();
    if first < 0 {
        cycle = cycle.map(|coefficient| -coefficient);
        (-1, cycle)
    } else {
        (1, cycle)
    }
}

fn circuit_tag(cycle: Chain) -> (i64, CircuitTag) {
    let (sign, primitive_cycle) = canonical_orientation(cycle);
    let support = primitive_cycle
        .iter()
        .enumerate()
        .fold(0_u8, |mask, (slot, coefficient)| {
            if *coefficient == 0 {
                mask
            } else {
                mask | (1 << slot)
            }
        });
    (
        sign,
        CircuitTag {
            support,
            primitive_cycle,
        },
    )
}

fn road_cycle(first: usize, second: usize) -> Chain {
    let mut cycle = [0; EDGES];
    cycle[edge(0, first)] += 1;
    cycle[edge(1, first)] -= 1;
    cycle[edge(0, second)] -= 1;
    cycle[edge(1, second)] += 1;
    assert_eq!(incidence(cycle), [0; VERTICES]);
    cycle
}

fn oriented_tag_cycles() -> [Chain; 3] {
    [road_cycle(0, 1), road_cycle(1, 2), road_cycle(2, 0)]
}

fn oriented_tag_class(coefficients: [i64; 3]) -> Chain {
    coefficients
        .into_iter()
        .zip(oriented_tag_cycles())
        .fold([0; EDGES], |sum, (coefficient, cycle)| {
            chain_add_scaled(sum, cycle, coefficient)
        })
}

fn oriented_tag_action(coefficients: [i64; 3], core_swap: bool, roads: [usize; 3]) -> [i64; 3] {
    let tags = oriented_tag_cycles();
    let mut result = [0; 3];
    for (source, coefficient) in coefficients.into_iter().enumerate() {
        let moved = graph_action(tags[source], core_swap, roads);
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
        let (target, sign) = matches[0];
        result[target] += sign * coefficient;
    }
    result
}

fn rational_section_numerator(chain: Chain) -> [i64; 3] {
    // The canonical D3-equivariant rational section has coefficient sum zero.
    // This returns three times that section.
    let [p, q] = chain_coordinates(chain);
    [p - q, p + 2 * q, -2 * p - q]
}

fn audit_tag_class_map() -> (usize, usize, usize) {
    let tags = oriented_tag_cycles();
    assert_eq!(
        tags.into_iter()
            .fold([0; EDGES], |sum, tag| chain_add_scaled(sum, tag, 1)),
        [0; EDGES]
    );
    assert_eq!(oriented_tag_class([1, 1, 1]), [0; EDGES]);

    let class_matrix: Vec<Vec<_>> = (0..EDGES)
        .map(|row| tags.iter().map(|tag| tag[row]).collect())
        .collect();
    assert_eq!(integer_rank(&class_matrix), 2);
    assert_eq!(maximal_minor_content(&class_matrix, 2), 1);

    // Rotation forces the lifts of the three cyclic tags to sum to zero.  A
    // lift of c0 is e0+n(1,1,1); its orbit sum is
    // (1+3n)(1,1,1), requiring n=-1/3.  Equivalently, the invariant diagonal
    // plus the sum-zero lattice has index three in Z^3.
    let splitting_lattice = vec![vec![1, 1, 0], vec![1, -1, 1], vec![1, 0, -1]];
    let splitting_index = determinant(splitting_lattice).abs() as usize;
    assert_eq!(splitting_index, 3);

    let mut rational_equivariance_checks = 0;
    for core_swap in [false, true] {
        for roads in ROAD_PERMUTATIONS {
            for cycle in h1_basis() {
                assert_eq!(
                    rational_section_numerator(graph_action(cycle, core_swap, roads)),
                    oriented_tag_action(rational_section_numerator(cycle), core_swap, roads)
                );
                rational_equivariance_checks += 1;
            }
        }
    }
    assert_eq!(rational_equivariance_checks, 24);
    assert!(h1_basis()
        .into_iter()
        .flat_map(rational_section_numerator)
        .any(|coefficient| coefficient % 3 != 0));

    // Forgetting orientation is worse: reflection 1<->2 fixes the support of
    // c1 but sends its H1 class to -c1.  Thus the free unoriented tag cannot
    // carry a nonzero equivariant class lift with the ordinary permutation
    // action; an orientation/determinant local system is required.
    let reflection = [0, 2, 1];
    assert_eq!(
        graph_action(tags[1], false, reflection),
        tags[1].map(|coefficient| -coefficient)
    );

    let pairwise_intersections: Vec<_> = (0..3)
        .flat_map(|left| ((left + 1)..3).map(move |right| (left, right)))
        .map(|(left, right)| matrix_det(basis_matrix(tags[left], tags[right])))
        .collect();
    assert_eq!(pairwise_intersections.len(), 3);
    assert!(pairwise_intersections
        .iter()
        .all(|intersection| intersection.abs() == 1));

    (
        rational_equivariance_checks,
        splitting_index,
        pairwise_intersections.len(),
    )
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

fn resolved_circuit_support(pattern: [usize; VERTICES]) -> Option<u8> {
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
            if sets.find(left) == root {
                mask | (1 << slot)
            } else {
                mask
            }
        })
    })
}

fn audit_resolved_circuit_tags() -> BTreeMap<CircuitTag, usize> {
    let oriented = oriented_tag_cycles();
    let relation = oriented
        .into_iter()
        .fold([0; EDGES], |sum, cycle| chain_add_scaled(sum, cycle, 1));
    assert_eq!(relation, [0; EDGES]);
    let tags_by_support: BTreeMap<_, _> = oriented
        .into_iter()
        .map(|cycle| {
            let (_, tag) = circuit_tag(cycle);
            (tag.support, tag)
        })
        .collect();
    assert_eq!(tags_by_support.len(), 3);

    let mut support_histogram = BTreeMap::new();
    for mut code in 0..3_usize.pow(VERTICES as u32) {
        let pattern = std::array::from_fn(|_| {
            let digit = code % 3;
            code /= 3;
            digit
        });
        if let Some(support) = resolved_circuit_support(pattern) {
            *support_histogram.entry(support).or_insert(0) += 1;
        }
    }
    assert_eq!(support_histogram.len(), 3);
    assert_eq!(support_histogram.values().sum::<usize>(), 9);
    assert!(support_histogram
        .values()
        .all(|&multiplicity| multiplicity == 3));
    assert_eq!(
        support_histogram.keys().copied().collect::<BTreeSet<_>>(),
        tags_by_support.keys().copied().collect()
    );

    // Every tree/chord generator lands, up to orientation, on one of the three
    // tags that is actually populated by a D-bearing resolved state.
    for tree in spanning_trees() {
        for chord in (0..EDGES).filter(|slot| tree & (1 << slot) == 0) {
            let (_, tag) = circuit_tag(fundamental_cycle(tree, chord));
            assert_eq!(tags_by_support.get(&tag.support), Some(&tag));
        }
    }

    support_histogram
        .into_iter()
        .map(|(support, multiplicity)| (tags_by_support[&support], multiplicity))
        .collect()
}

fn audit_determinant_characters() -> (usize, usize, usize) {
    let mut rotations = 0;
    let mut reflections = 0;
    let mut core_swaps = 0;
    for roads in ROAD_PERMUTATIONS {
        for core_swap in [false, true] {
            let determinant = matrix_det(action_matrix(core_swap, roads, false));
            assert_eq!(determinant, permutation_sign(roads));
            if core_swap {
                core_swaps += 1;
            }
            if permutation_sign(roads) == 1 {
                rotations += 1;
            } else {
                reflections += 1;
            }
        }
    }
    assert_eq!((rotations, reflections, core_swaps), (6, 6, 6));
    (rotations, reflections, core_swaps)
}

fn main() {
    let (equivariant_checks, sign_twisted_failures) = audit_integral_bridge();
    let (trees, chord_generators, tree_changes) = audit_tree_changes();
    let (addition_paths, determinant_swaps) = audit_addition_orders();
    let (rational_section_checks, splitting_index, intersecting_tag_pairs) = audit_tag_class_map();
    let circuit_histogram = audit_resolved_circuit_tags();
    let (rotation_checks, reflection_checks, core_swap_checks) = audit_determinant_characters();

    println!("Ward-cycle / resolved-Brauer bridge certificate");
    println!("================================================");
    println!("  H1(K2,3;Z) rank / primitive basis:        2/2");
    println!("  equal-endpoint Ward kernel rank/basis:    2/2");
    println!("  S2xD3 integral equivariance checks:       {equivariant_checks}");
    println!("  unnecessary sign-twist failures:          {sign_twisted_failures}");
    println!("  spanning trees / chord generators:        {trees}/{chord_generators}");
    println!("  unimodular tree-change matrices:          {tree_changes}");
    println!("  disk-annulus-punctured-torus paths:        {addition_paths}");
    println!("  reversed-order determinant signs:         {determinant_swaps}");
    println!("  rational tag-section equivariance:        {rational_section_checks}");
    println!("  integral equivariant splitting index:     {splitting_index}");
    println!("  pairwise intersection-one tag pairs:      {intersecting_tag_pairs}");
    println!("  simultaneous resolved closed pairs:       0/243");
    println!("  tagged D-bearing circuit histogram:       {circuit_histogram:?}");
    println!("  rotation/reflection/core-swap det checks: {rotation_checks}/{reflection_checks}/{core_swap_checks}");
    println!();
    println!("VERDICT");
    println!("  the Ward kernel is integrally and S2xD3-equivariantly H1(K2,3)");
    println!("  the required chart change is the unimodular quarter-turn (p,q)->(q,-p)");
    println!(
        "  all tree bases differ unimodularly and both edge-addition orders reach the same handle"
    );
    println!(
        "  addition-order exchange and road reflection act by -1 on det H1; rotation acts by +1"
    );
    println!("  the canonical direction is oriented circuit tag -> H1, not additive H1 -> resolved curves");
    println!("  an integral D3-equivariant section is obstructed at index 3; the rational section needs 1/3");
    println!("  all three tag pairs intersect once and no resolved noncrossing state contains two circuits");
    println!("  the 9 formal-D sectors refine to 3 individual circuit supports of multiplicity 3");
    println!(
        "  a two-generator lift therefore needs an oriented crossing/smoothing degree-one cell"
    );
    println!(
        "  missing: Brauer-skein filler, signed scalar/curve coefficients, and Cut compatibility"
    );
}
