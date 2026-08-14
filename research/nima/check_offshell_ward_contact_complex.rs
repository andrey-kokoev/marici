//! Exact off-shell certificate for the moving-Ward contact typing repair.
//!
//! Conventions are all-outgoing, `k + p + q = 0`, and
//!
//!   V(k,p,q) = -[eta (k-p) + cyclic],
//!   P_ab(k)  = k^2 eta_ab - k_a k_b,
//!   D_xi(k)  = eta/k^2 + (xi-1) k k/(k^2)^2.
//!
//! Thus `k.V = P(next)-P(previous)` and, off shell,
//!
//!   P(k) D_xi(k) = I - k k/k^2.
//!
//! The last formula gives a typed degree-zero target: an edge-contraction
//! contact state and a longitudinal exit.  The graph calculation below does
//! not identify either state with a surface cell or a 243-origin carrier.

#![allow(dead_code)]

use std::collections::{BTreeMap, BTreeSet};

type Int = i128;

const PRIMITIVES: usize = 6; // p, q, and four generic test vectors
const GRAM_VARIABLES: usize = PRIMITIVES * (PRIMITIVES + 1) / 2;
const XI_VARIABLE: usize = GRAM_VARIABLES;
const VARIABLES: usize = GRAM_VARIABLES + 1;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Monomial([u8; VARIABLES]);

impl Monomial {
    const ONE: Self = Self([0; VARIABLES]);

    fn variable(index: usize) -> Self {
        let mut powers = [0; VARIABLES];
        powers[index] = 1;
        Self(powers)
    }

    fn multiply(self, other: Self) -> Self {
        Self(std::array::from_fn(|i| {
            self.0[i]
                .checked_add(other.0[i])
                .expect("monomial exponent overflow")
        }))
    }
}

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct Polynomial(BTreeMap<Monomial, Int>);

impl Polynomial {
    fn constant(value: Int) -> Self {
        if value == 0 {
            Self::default()
        } else {
            Self(BTreeMap::from([(Monomial::ONE, value)]))
        }
    }

    fn variable(index: usize) -> Self {
        Self(BTreeMap::from([(Monomial::variable(index), 1)]))
    }

    fn add_assign(&mut self, other: &Self) {
        for (&monomial, &coefficient) in &other.0 {
            let entry = self.0.entry(monomial).or_default();
            *entry += coefficient;
            if *entry == 0 {
                self.0.remove(&monomial);
            }
        }
    }

    fn add(mut self, other: &Self) -> Self {
        self.add_assign(other);
        self
    }

    fn scale(mut self, scalar: Int) -> Self {
        if scalar == 0 {
            return Self::default();
        }
        for coefficient in self.0.values_mut() {
            *coefficient *= scalar;
        }
        self
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = BTreeMap::new();
        for (&left_monomial, &left_coefficient) in &self.0 {
            for (&right_monomial, &right_coefficient) in &other.0 {
                *result
                    .entry(left_monomial.multiply(right_monomial))
                    .or_default() += left_coefficient * right_coefficient;
            }
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Vector([Int; PRIMITIVES]);

impl Vector {
    fn primitive(index: usize) -> Self {
        let mut coefficients = [0; PRIMITIVES];
        coefficients[index] = 1;
        Self(coefficients)
    }

    fn plus(self, other: Self) -> Self {
        Self(std::array::from_fn(|i| self.0[i] + other.0[i]))
    }

    fn minus(self, other: Self) -> Self {
        Self(std::array::from_fn(|i| self.0[i] - other.0[i]))
    }

    fn scale(self, scalar: Int) -> Self {
        Self(std::array::from_fn(|i| scalar * self.0[i]))
    }
}

fn gram_index(first: usize, second: usize) -> usize {
    let (first, second) = if first <= second {
        (first, second)
    } else {
        (second, first)
    };
    let before = first * PRIMITIVES - first * first.saturating_sub(1) / 2;
    before + second - first
}

fn dot(first: Vector, second: Vector) -> Polynomial {
    let mut result = Polynomial::default();
    for i in 0..PRIMITIVES {
        for j in 0..PRIMITIVES {
            let coefficient = first.0[i] * second.0[j];
            if coefficient != 0 {
                result.add_assign(&Polynomial::variable(gram_index(i, j)).scale(coefficient));
            }
        }
    }
    result
}

fn momenta() -> [Vector; 3] {
    let p = Vector::primitive(0);
    let q = Vector::primitive(1);
    [p, q, p.plus(q).scale(-1)]
}

fn test_vector(index: usize) -> Vector {
    Vector::primitive(2 + index)
}

fn projector(momentum: Vector, first: Vector, second: Vector) -> Polynomial {
    dot(momentum, momentum).multiply(&dot(first, second)).add(
        &dot(first, momentum)
            .multiply(&dot(second, momentum))
            .scale(-1),
    )
}

// The sign is selected so that contraction at slot i is
// P(slot i+1)-P(slot i+2), with cyclic indices.
fn three_gluon_vertex(momenta: [Vector; 3], tests: [Vector; 3]) -> Polynomial {
    let mut result = Polynomial::default();
    result.add_assign(
        &dot(tests[0], tests[1]).multiply(&dot(momenta[1].minus(momenta[0]), tests[2])),
    );
    result.add_assign(
        &dot(tests[1], tests[2]).multiply(&dot(momenta[2].minus(momenta[1]), tests[0])),
    );
    result.add_assign(
        &dot(tests[2], tests[0]).multiply(&dot(momenta[0].minus(momenta[2]), tests[1])),
    );
    result
}

fn check_local_ward_identity() -> usize {
    let momenta = momenta();
    assert_eq!(
        momenta[0].plus(momenta[1]).plus(momenta[2]),
        Vector([0; PRIMITIVES])
    );
    let mut checks = 0;
    for incoming in 0..3 {
        let next = (incoming + 1) % 3;
        let previous = (incoming + 2) % 3;
        for first in 0..4 {
            for second in 0..4 {
                let mut tests = [Vector([0; PRIMITIVES]); 3];
                tests[incoming] = momenta[incoming];
                tests[next] = test_vector(first);
                tests[previous] = test_vector(second);
                let left = three_gluon_vertex(momenta, tests);
                let right = projector(momenta[next], tests[next], tests[previous])
                    .add(&projector(momenta[previous], tests[next], tests[previous]).scale(-1));
                assert_eq!(left, right);
                checks += 1;
            }
        }
    }
    checks
}

// Compare rational tensors over the common denominator (k^2)^2.  This avoids
// specializing any Gram variable and keeps p^2, q^2, and r^2 generic.
fn check_propagator_composition() -> usize {
    let xi_minus_one = Polynomial::variable(XI_VARIABLE).add(&Polynomial::constant(-1));
    let mut checks = 0;
    for momentum in momenta() {
        let square = dot(momentum, momentum);
        for first in 0..4 {
            for second in 0..4 {
                let first = test_vector(first);
                let second = test_vector(second);
                let first_k = dot(first, momentum);
                let second_k = dot(second, momentum);
                let metric = dot(first, second);

                // a.P.k is the factor multiplying the covariant-gauge tail.
                let p_k = square
                    .multiply(&first_k)
                    .add(&first_k.multiply(&square).scale(-1));
                assert_eq!(p_k, Polynomial::default());

                let feynman_numerator = square.multiply(
                    &square
                        .multiply(&metric)
                        .add(&first_k.multiply(&second_k).scale(-1)),
                );
                let covariant_numerator = feynman_numerator
                    .clone()
                    .add(&xi_minus_one.multiply(&p_k).multiply(&second_k));
                let contact_numerator = square.multiply(&square).multiply(&metric);
                let longitudinal_numerator =
                    square.multiply(&first_k).multiply(&second_k).scale(-1);
                let split = contact_numerator.add(&longitudinal_numerator);

                assert_eq!(covariant_numerator, feynman_numerator);
                assert_eq!(covariant_numerator, split);
                checks += 1;
            }
        }
    }
    // Each of the 48 Ward identities has two P insertions; the 3*16 unique
    // propagator checks above cover both occurrences, giving 96 compositions.
    2 * checks
}

const VERTICES: usize = 5;
const EDGES: usize = 6;
// Nine symmetry-visible physical marks modulo the two local cyclic sums give
// the smallest degree-one module used by the complex, of rank seven.
const WARD_MARKS: usize = 9;
const LOCAL_CYCLIC_RELATIONS: usize = 2;
const MOVING_WARD_RANK: usize = WARD_MARKS - LOCAL_CYCLIC_RELATIONS;
const LONGITUDINAL_EXITS: usize = 2 * EDGES;

type ContactChain = [i8; EDGES];
type VertexBoundary = [i8; VERTICES];
type LongitudinalChain = [i8; LONGITUDINAL_EXITS];

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct DegreeZero {
    contacts: ContactChain,
    longitudinal: LongitudinalChain,
}

impl DegreeZero {
    fn zero() -> Self {
        Self {
            contacts: [0; EDGES],
            longitudinal: [0; LONGITUDINAL_EXITS],
        }
    }

    fn add_scaled(&mut self, other: Self, coefficient: i8) {
        for i in 0..EDGES {
            self.contacts[i] += coefficient * other.contacts[i];
        }
        for i in 0..LONGITUDINAL_EXITS {
            self.longitudinal[i] += coefficient * other.longitudinal[i];
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum WardMark {
    // At L_core, the incoming road is contracted; next and previous roads exit.
    Left { core: usize, incoming_road: usize },
    // At R_road, the external leg is contracted; the two internal edges exit.
    RightExternal { road: usize },
}

fn edge_slot(core: usize, road: usize) -> usize {
    2 * road + core
}

fn edge_vertices(slot: usize) -> (usize, usize) {
    (slot % 2, 2 + slot / 2)
}

fn endpoint_exit(slot: usize, vertex: usize) -> usize {
    let (tail, head) = edge_vertices(slot);
    if vertex == tail {
        2 * slot
    } else {
        assert_eq!(vertex, head);
        2 * slot + 1
    }
}

fn ward_marks() -> [WardMark; WARD_MARKS] {
    std::array::from_fn(|index| {
        if index < 6 {
            WardMark::Left {
                core: index / 3,
                incoming_road: index % 3,
            }
        } else {
            WardMark::RightExternal { road: index - 6 }
        }
    })
}

// d W = (C_next-Q_next) - (C_previous-Q_previous).
fn ward_differential(mark: WardMark) -> DegreeZero {
    let (vertex, next, previous) = match mark {
        WardMark::Left {
            core,
            incoming_road,
        } => (
            core,
            edge_slot(core, (incoming_road + 1) % 3),
            edge_slot(core, (incoming_road + 2) % 3),
        ),
        WardMark::RightExternal { road } => (2 + road, edge_slot(0, road), edge_slot(1, road)),
    };
    let mut result = DegreeZero::zero();
    result.contacts[next] += 1;
    result.contacts[previous] -= 1;
    result.longitudinal[endpoint_exit(next, vertex)] -= 1;
    result.longitudinal[endpoint_exit(previous, vertex)] += 1;
    result
}

fn incidence(chain: ContactChain) -> VertexBoundary {
    let mut result = [0_i8; VERTICES];
    for (slot, coefficient) in IntoIterator::into_iter(chain).enumerate() {
        let (tail, head) = edge_vertices(slot);
        result[tail] -= coefficient;
        result[head] += coefficient;
    }
    result
}

fn contact_unit(slot: usize) -> ContactChain {
    let mut result = [0; EDGES];
    result[slot] = 1;
    result
}

fn subtract(left: ContactChain, right: ContactChain) -> ContactChain {
    std::array::from_fn(|i| left[i] - right[i])
}

fn spanning_tree_masks() -> Vec<u8> {
    let mut trees = Vec::new();
    for mask in 0_u8..(1 << EDGES) {
        if mask.count_ones() != 4 {
            continue;
        }
        let mut parent: [usize; VERTICES] = std::array::from_fn(|i| i);
        fn find(parent: &mut [usize; VERTICES], vertex: usize) -> usize {
            if parent[vertex] != vertex {
                parent[vertex] = find(parent, parent[vertex]);
            }
            parent[vertex]
        }
        for slot in 0..EDGES {
            if mask & (1 << slot) != 0 {
                let (left, right) = edge_vertices(slot);
                let left = find(&mut parent, left);
                let right = find(&mut parent, right);
                parent[right] = left;
            }
        }
        let roots: BTreeSet<_> = (0..VERTICES).map(|v| find(&mut parent, v)).collect();
        if roots.len() == 1 {
            trees.push(mask);
        }
    }
    assert_eq!(trees.len(), 12);
    trees
}

fn tree_lift_boundary(tree_mask: u8, wanted: VertexBoundary) -> ContactChain {
    let edges: Vec<_> = (0..EDGES)
        .filter(|slot| tree_mask & (1 << slot) != 0)
        .collect();
    assert_eq!(edges.len(), 4);
    let mut solutions = Vec::new();
    for code in 0..3_usize.pow(4) {
        let mut rest = code;
        let mut candidate = [0_i8; EDGES];
        for &slot in &edges {
            candidate[slot] = (rest % 3) as i8 - 1;
            rest /= 3;
        }
        if incidence(candidate) == wanted {
            solutions.push(candidate);
        }
    }
    assert_eq!(solutions.len(), 1);
    solutions[0]
}

fn gcd(mut first: i64, mut second: i64) -> i64 {
    first = first.abs();
    second = second.abs();
    while second != 0 {
        (first, second) = (second, first % second);
    }
    first
}

fn integer_rank(mut rows: Vec<Vec<i64>>) -> usize {
    if rows.is_empty() {
        return 0;
    }
    let columns = rows[0].len();
    let mut rank = 0;
    for column in 0..columns {
        let Some(pivot) = (rank..rows.len()).find(|&row| rows[row][column] != 0) else {
            continue;
        };
        rows.swap(rank, pivot);
        for row in 0..rows.len() {
            if row == rank || rows[row][column] == 0 {
                continue;
            }
            let pivot_value = rows[rank][column];
            let row_value = rows[row][column];
            for entry in column..columns {
                rows[row][entry] = pivot_value * rows[row][entry] - row_value * rows[rank][entry];
            }
            let divisor = rows[row]
                .iter()
                .fold(0_i64, |common, &value| gcd(common, value));
            if divisor > 1 {
                for value in &mut rows[row] {
                    *value /= divisor;
                }
            }
        }
        rank += 1;
        if rank == rows.len() {
            break;
        }
    }
    rank
}

fn contact_rank(vectors: &[ContactChain]) -> usize {
    integer_rank(
        vectors
            .iter()
            .map(|vector| vector.iter().map(|&x| i64::from(x)).collect())
            .collect(),
    )
}

fn full_rank(vectors: &[DegreeZero]) -> usize {
    integer_rank(
        vectors
            .iter()
            .map(|vector| {
                vector
                    .contacts
                    .iter()
                    .chain(vector.longitudinal.iter())
                    .map(|&x| i64::from(x))
                    .collect()
            })
            .collect(),
    )
}

fn nonzero_count<const N: usize>(vector: [i8; N]) -> usize {
    vector.iter().filter(|&&x| x != 0).count()
}

fn fundamental_relation(cycle: ContactChain) -> [i8; WARD_MARKS] {
    assert_eq!(incidence(cycle), [0; VERTICES]);
    assert_eq!(nonzero_count(cycle), 4);
    let marks = ward_marks();
    let cycle_edges: Vec<_> = (0..EDGES).filter(|&edge| cycle[edge] != 0).collect();
    let mut at_vertices = Vec::new();
    for vertex in 0..VERTICES {
        let incident: Vec<_> = cycle_edges
            .iter()
            .copied()
            .filter(|&edge| {
                let (left, right) = edge_vertices(edge);
                vertex == left || vertex == right
            })
            .collect();
        if incident.len() == 2 {
            let candidates: Vec<_> = marks
                .iter()
                .enumerate()
                .filter(|(_, mark)| {
                    let differential = ward_differential(**mark).contacts;
                    let support: Vec<_> =
                        (0..EDGES).filter(|&edge| differential[edge] != 0).collect();
                    support == incident
                })
                .map(|(index, _)| index)
                .collect();
            assert_eq!(candidates.len(), 1);
            at_vertices.push(candidates[0]);
        }
    }
    assert_eq!(at_vertices.len(), 4);

    let mut solutions = Vec::new();
    for signs in 0_u8..16 {
        let mut coefficients = [0_i8; WARD_MARKS];
        let mut image = DegreeZero::zero();
        for (position, &mark) in at_vertices.iter().enumerate() {
            let coefficient = if signs & (1 << position) == 0 { 1 } else { -1 };
            coefficients[mark] = coefficient;
            image.add_scaled(ward_differential(marks[mark]), coefficient);
        }
        if image.contacts == [0; EDGES] {
            solutions.push((coefficients, image.longitudinal));
        }
    }
    assert_eq!(solutions.len(), 2); // a relation and its negative
    let (coefficients, longitudinal) = solutions[0];
    assert_eq!(nonzero_count(longitudinal), 8);
    coefficients
}

fn apply_ward_chain(coefficients: [i8; WARD_MARKS]) -> DegreeZero {
    let mut result = DegreeZero::zero();
    for (coefficient, mark) in IntoIterator::into_iter(coefficients).zip(ward_marks()) {
        result.add_scaled(ward_differential(mark), coefficient);
    }
    result
}

fn minimum_longitudinal_obstruction() -> (usize, [i8; WARD_MARKS], usize) {
    let marks = ward_marks();
    // First determine the minimum support over Q exactly, by comparing the
    // contact and full column ranks on every subset.  This excludes smaller
    // witnesses with coefficients outside {-1,0,1}.
    let exact_minimum = (1_u16..(1 << WARD_MARKS))
        .filter_map(|mask| {
            let subset: Vec<_> = (0..WARD_MARKS)
                .filter(|&index| mask & (1 << index) != 0)
                .map(|index| ward_differential(marks[index]))
                .collect();
            let contacts: Vec<_> = subset.iter().map(|value| value.contacts).collect();
            (full_rank(&subset) > contact_rank(&contacts)).then_some(mask.count_ones() as usize)
        })
        .min()
        .expect("no rank-detected longitudinal obstruction");

    // Then retain a small integral witness for the minimum-rank obstruction.
    let mut best: Option<(usize, [i8; WARD_MARKS], usize)> = None;
    for code in 1..3_usize.pow(WARD_MARKS as u32) {
        let mut rest = code;
        let coefficients = std::array::from_fn(|_| {
            let coefficient = (rest % 3) as i8 - 1;
            rest /= 3;
            coefficient
        });
        let support = nonzero_count(coefficients);
        if best.as_ref().is_some_and(|best| support >= best.0) {
            continue;
        }
        let mut image = DegreeZero::zero();
        for i in 0..WARD_MARKS {
            image.add_scaled(ward_differential(marks[i]), coefficients[i]);
        }
        if image.contacts == [0; EDGES] && image.longitudinal != [0; LONGITUDINAL_EXITS] {
            best = Some((support, coefficients, nonzero_count(image.longitudinal)));
        }
    }
    let best = best.expect("no longitudinal obstruction");
    assert_eq!(best.0, exact_minimum);
    best
}

fn permute_contact(chain: ContactChain, reflection: bool) -> ContactChain {
    let mut result = [0; EDGES];
    for slot in 0..EDGES {
        let core = slot % 2;
        let road = slot / 2;
        let (new_core, new_road) = if reflection {
            (1 - core, (3 - road) % 3)
        } else {
            (core, (road + 1) % 3)
        };
        result[edge_slot(new_core, new_road)] += chain[slot];
    }
    result
}

fn permute_longitudinal(chain: LongitudinalChain, reflection: bool) -> LongitudinalChain {
    let mut result = [0; LONGITUDINAL_EXITS];
    for slot in 0..EDGES {
        let mapped = permute_contact(contact_unit(slot), reflection)
            .iter()
            .position(|&x| x != 0)
            .unwrap();
        result[2 * mapped] += chain[2 * slot];
        result[2 * mapped + 1] += chain[2 * slot + 1];
    }
    result
}

fn permute_degree_zero(value: DegreeZero, reflection: bool) -> DegreeZero {
    DegreeZero {
        contacts: permute_contact(value.contacts, reflection),
        longitudinal: permute_longitudinal(value.longitudinal, reflection),
    }
}

fn permute_mark(mark: WardMark, reflection: bool) -> (WardMark, i8) {
    if reflection {
        match mark {
            WardMark::Left {
                core,
                incoming_road,
            } => (
                WardMark::Left {
                    core: 1 - core,
                    incoming_road: (3 - incoming_road) % 3,
                },
                -1,
            ),
            WardMark::RightExternal { road } => (
                WardMark::RightExternal {
                    road: (3 - road) % 3,
                },
                -1,
            ),
        }
    } else {
        match mark {
            WardMark::Left {
                core,
                incoming_road,
            } => (
                WardMark::Left {
                    core,
                    incoming_road: (incoming_road + 1) % 3,
                },
                1,
            ),
            WardMark::RightExternal { road } => (
                WardMark::RightExternal {
                    road: (road + 1) % 3,
                },
                1,
            ),
        }
    }
}

fn check_symmetries(trees: &[u8]) -> (usize, usize, usize) {
    let tree_set: BTreeSet<_> = trees.iter().copied().collect();
    let mut rotation_checks = 0;
    let mut reflection_checks = 0;
    for mark in ward_marks() {
        for reflection in [false, true] {
            let (mapped, coefficient) = permute_mark(mark, reflection);
            let mut expected = DegreeZero::zero();
            expected.add_scaled(ward_differential(mapped), coefficient);
            assert_eq!(
                permute_degree_zero(ward_differential(mark), reflection),
                expected
            );
            if reflection {
                reflection_checks += 1;
            } else {
                rotation_checks += 1;
            }
        }
    }
    for &tree in trees {
        for reflection in [false, true] {
            let mut chain = [0_i8; EDGES];
            for edge in 0..EDGES {
                if tree & (1 << edge) != 0 {
                    chain[edge] = 1;
                }
            }
            let mapped = permute_contact(chain, reflection);
            let mapped_mask = (0..EDGES).fold(0_u8, |mask, edge| {
                mask | if mapped[edge] != 0 { 1 << edge } else { 0 }
            });
            assert!(tree_set.contains(&mapped_mask));
        }
    }

    // All 2^6 edge-orientation presentations encode the same unoriented
    // contact chain after multiplying a coordinate by its orientation sign.
    let mut orientation_checks = 0;
    for orientation in 0_u8..(1 << EDGES) {
        let signs: ContactChain = std::array::from_fn(|edge| {
            if orientation & (1 << edge) == 0 {
                1
            } else {
                -1
            }
        });
        for mark in ward_marks() {
            let canonical_value = ward_differential(mark);
            let canonical = canonical_value.contacts;
            let presented: ContactChain = std::array::from_fn(|edge| canonical[edge] * signs[edge]);
            let recovered: ContactChain = std::array::from_fn(|edge| presented[edge] * signs[edge]);
            let presented_longitudinal: LongitudinalChain =
                std::array::from_fn(|exit| canonical_value.longitudinal[exit] * signs[exit / 2]);
            let recovered_longitudinal: LongitudinalChain =
                std::array::from_fn(|exit| presented_longitudinal[exit] * signs[exit / 2]);
            assert_eq!(recovered, canonical);
            assert_eq!(recovered_longitudinal, canonical_value.longitudinal);
            assert_eq!(incidence(recovered), incidence(canonical));
            orientation_checks += 1;
        }
    }
    (orientation_checks, rotation_checks, reflection_checks)
}

#[derive(Default)]
struct GraphAudit {
    tree_presentations: usize,
    tree_exact_contacts: usize,
    harmonic_chords: usize,
    harmonic_rank_failures: usize,
    ward_tree_propagations: usize,
    harmonic_telescoping_failures: usize,
    orientation_checks: usize,
    rotation_checks: usize,
    reflection_checks: usize,
}

fn check_graph_complex() -> (GraphAudit, usize, usize, usize, [i8; WARD_MARKS], usize) {
    let trees = spanning_tree_masks();
    let marks = ward_marks();
    let differentials: Vec<_> = marks.iter().copied().map(ward_differential).collect();
    let contact_vectors: Vec<_> = differentials.iter().map(|d| d.contacts).collect();
    let contact_map_rank = contact_rank(&contact_vectors);
    let full_map_rank = full_rank(&differentials);
    assert_eq!(contact_map_rank, 5);
    assert_eq!(full_map_rank, 7);
    assert_eq!(WARD_MARKS - contact_map_rank, 4);
    assert_eq!(WARD_MARKS - full_map_rank, 2);
    assert_eq!(MOVING_WARD_RANK - contact_map_rank, 2);
    assert_eq!(MOVING_WARD_RANK - full_map_rank, 0);

    // The two surviving full-kernel relations are the local cyclic sums at
    // L0 and L1.  Degree zero is terminal, so d^2=0 exactly in this two-term
    // complex; the nontrivial test is harmonic telescoping below.
    for core in 0..2 {
        let mut relation = [0_i8; WARD_MARKS];
        for road in 0..3 {
            relation[3 * core + road] = 1;
        }
        assert_eq!(apply_ward_chain(relation), DegreeZero::zero());
    }

    let mut audit = GraphAudit::default();
    for tree in trees.iter().copied() {
        audit.tree_presentations += 1;
        let mut cycles = Vec::new();
        for edge in 0..EDGES {
            let unit = contact_unit(edge);
            let tree_part = tree_lift_boundary(tree, incidence(unit));
            assert_eq!(incidence(tree_part), incidence(unit));
            let harmonic = subtract(unit, tree_part);
            assert_eq!(incidence(harmonic), [0; VERTICES]);
            if tree & (1 << edge) != 0 {
                assert_eq!(harmonic, [0; EDGES]);
                audit.tree_exact_contacts += 1;
            } else {
                assert_eq!(harmonic[edge], 1);
                assert_eq!(nonzero_count(harmonic), 4);
                let relation = fundamental_relation(harmonic);
                let image = apply_ward_chain(relation);
                assert_eq!(image.contacts, [0; EDGES]);
                assert_eq!(nonzero_count(image.longitudinal), 8);
                audit.harmonic_telescoping_failures += 1;
                cycles.push(harmonic);
                audit.harmonic_chords += 1;
            }
        }
        if contact_rank(&cycles) != 2 {
            audit.harmonic_rank_failures += 1;
        }

        // Every physical local contact difference has a unique tree
        // propagation plus a retained harmonic remainder.
        for differential in &differentials {
            let tree_part = tree_lift_boundary(tree, incidence(differential.contacts));
            let harmonic = subtract(differential.contacts, tree_part);
            assert_eq!(incidence(harmonic), [0; VERTICES]);
            assert_eq!(
                std::array::from_fn::<_, EDGES, _>(|edge| tree_part[edge] + harmonic[edge]),
                differential.contacts
            );
            audit.ward_tree_propagations += 1;
        }
    }
    assert_eq!(audit.tree_presentations, 12);
    assert_eq!(audit.tree_exact_contacts, 48);
    assert_eq!(audit.harmonic_chords, 24);
    assert_eq!(audit.harmonic_rank_failures, 0);
    assert_eq!(audit.ward_tree_propagations, 108);
    assert_eq!(audit.harmonic_telescoping_failures, 24);

    let (minimum_support, witness, exit_support) = minimum_longitudinal_obstruction();
    assert_eq!(minimum_support, 4);
    assert_eq!(exit_support, 8);
    let (orientation_checks, rotation_checks, reflection_checks) = check_symmetries(&trees);
    assert_eq!(orientation_checks, 64 * WARD_MARKS);
    assert_eq!(rotation_checks, WARD_MARKS);
    assert_eq!(reflection_checks, WARD_MARKS);
    audit.orientation_checks = orientation_checks;
    audit.rotation_checks = rotation_checks;
    audit.reflection_checks = reflection_checks;

    (
        audit,
        contact_map_rank,
        full_map_rank,
        minimum_support,
        witness,
        exit_support,
    )
}

fn main() {
    let ward_checks = check_local_ward_identity();
    let propagator_compositions = check_propagator_composition();
    let (audit, contact_rank, full_rank, minimum_support, witness, exit_support) =
        check_graph_complex();

    println!("Off-shell moving-Ward contact-complex certificate");
    println!("=================================================");
    println!("  generic Gram variables:                 {GRAM_VARIABLES}");
    println!("  cyclic three-gluon Ward checks:         {ward_checks}");
    println!("  P*D contact/longitudinal compositions:  {propagator_compositions}");
    println!(
        "  K2,3 spanning-tree presentations:       {}",
        audit.tree_presentations
    );
    println!(
        "  tree-exact contact generators:          {}",
        audit.tree_exact_contacts
    );
    println!(
        "  retained harmonic chords:               {}",
        audit.harmonic_chords
    );
    println!(
        "  harmonic rank failures:                 {}",
        audit.harmonic_rank_failures
    );
    println!(
        "  local Ward tree propagations:           {}",
        audit.ward_tree_propagations
    );
    println!(
        "  orientation convention checks:          {}",
        audit.orientation_checks
    );
    println!(
        "  road-rotation chain-map checks:          {}",
        audit.rotation_checks
    );
    println!(
        "  reflection chain-map checks:             {}",
        audit.reflection_checks
    );
    println!(
        "  degree-one quotient rank:                {MOVING_WARD_RANK} ({} marks / {LOCAL_CYCLIC_RELATIONS} local cyclic relations)",
        WARD_MARKS
    );
    println!(
        "  contact-only map rank/kernel:            {contact_rank}/{}",
        MOVING_WARD_RANK - contact_rank
    );
    println!(
        "  contact+exit map rank/kernel:            {full_rank}/{}",
        MOVING_WARD_RANK - full_rank
    );
    println!(
        "  obstructed harmonic telescope checks:   {}",
        audit.harmonic_telescoping_failures
    );
    println!("  smallest obstruction mark support:      {minimum_support}");
    println!("  smallest obstruction exit support:      {exit_support}");
    println!("  smallest obstruction coefficients:      {witness:?}");
    println!();
    println!("VERDICT");
    println!("  P(k)D_xi(k) canonically types every Ward exit as contact minus longitudinal");
    println!(
        "  the contact projection propagates by tree incidence and retains H1(K2,3) of rank two"
    );
    println!("  the two-term differential has d^2=0 because degree zero is terminal");
    println!(
        "  full harmonic telescoping is obstructed by an xi-independent longitudinal remainder"
    );
    println!("  the smallest obstruction is a four-mark K2,3 square with eight longitudinal exits");
    println!("  no map to a surface or 243-origin carrier is constructed here");
}
