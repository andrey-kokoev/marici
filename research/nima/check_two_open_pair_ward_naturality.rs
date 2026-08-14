//! Exact two-open-pair Ward/naturality audit on the marked-theta carrier.
//!
//! A spanning tree of the five-vertex marked-theta graph leaves two internal
//! edge pairs open.  This checker keeps those four state indices external,
//! contracts them with four algebraically generic transverse test vectors,
//! and works in a Gram-free polynomial chart.  It tests, before the second
//! closure:
//!
//! 1. the four tree Ward identities;
//! 2. Ward stability after either physical-projector closure;
//! 3. the one-edge Ward formula `metric + N + N'`;
//! 4. the proposed realization square from physical closure to the
//!    gauge-reduced graphical/curve-cover network;
//! 5. reference independence and both closure orders.
//!
//! No spacetime dimension, floating-point sample, or Gram determinant is
//! imposed.  The four test polarizations have independent Gram coordinates
//! modulo only their required transversality equations.

use std::collections::{BTreeMap, BTreeSet};

type Int = i128;

const VERTICES: usize = 5;
const NODES: usize = 3 * VERTICES;
const BASE_PRIMITIVES: usize = 7;
const TEST_VECTORS: usize = 4;
const PRIMITIVES: usize = BASE_PRIMITIVES + TEST_VECTORS;
const VARIABLES: usize = 64;

const VAR_A: usize = 0;
const VAR_E0P0: usize = 1;
const VAR_E0P1: usize = 2;
const VAR_E0K1: usize = 3;
const VAR_E1P0: usize = 4;
const VAR_E1P1: usize = 5;
const VAR_E1K0: usize = 6;
const VAR_E2P0: usize = 7;
const VAR_E2P1: usize = 8;
const VAR_E2K0: usize = 9;
const VAR_E0E1: usize = 10;
const VAR_E0E2: usize = 11;
const VAR_E1E2: usize = 12;
const VAR_D: usize = 13;
const FIRST_TEST_GRAM: usize = 14;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Monomial([i8; VARIABLES]);

impl Monomial {
    const ONE: Self = Self([0; VARIABLES]);

    fn variable(index: usize) -> Self {
        let mut powers = [0; VARIABLES];
        powers[index] = 1;
        Self(powers)
    }

    fn multiply(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| {
            self.0[index]
                .checked_add(other.0[index])
                .expect("monomial exponent overflow")
        }))
    }

    fn shift(mut self, index: usize, amount: i8) -> Self {
        self.0[index] = self.0[index]
            .checked_add(amount)
            .expect("monomial exponent overflow");
        self
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
                let monomial = left_monomial.multiply(right_monomial);
                *result.entry(monomial).or_default() += left_coefficient * right_coefficient;
            }
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }

    fn shift_exponent(mut self, index: usize, amount: i8) -> Self {
        self.0 = self
            .0
            .into_iter()
            .map(|(monomial, coefficient)| (monomial.shift(index, amount), coefficient))
            .collect();
        self
    }

    fn minimum_exponent(&self, index: usize) -> i8 {
        self.0
            .keys()
            .map(|monomial| monomial.0[index])
            .min()
            .unwrap_or(0)
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
        Self(std::array::from_fn(|index| self.0[index] + other.0[index]))
    }

    fn minus(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| self.0[index] - other.0[index]))
    }

    fn scale(self, scalar: Int) -> Self {
        Self(std::array::from_fn(|index| scalar * self.0[index]))
    }
}

fn p(road: usize) -> Vector {
    match road {
        0 => Vector::primitive(0),
        1 => Vector::primitive(1),
        2 => Vector::primitive(0).plus(Vector::primitive(1)).scale(-1),
        _ => unreachable!(),
    }
}

fn k(road: usize) -> Vector {
    match road {
        0 => Vector::primitive(2),
        1 => Vector::primitive(3),
        2 => Vector::primitive(2).plus(Vector::primitive(3)).scale(-1),
        _ => unreachable!(),
    }
}

fn epsilon(road: usize) -> Vector {
    Vector::primitive(4 + road)
}

fn test_vector(index: usize) -> Vector {
    Vector::primitive(BASE_PRIMITIVES + index)
}

fn variable(index: usize, coefficient: Int) -> Polynomial {
    Polynomial::variable(index).scale(coefficient)
}

fn base_gram(first: usize, second: usize) -> Polynomial {
    let (first, second) = if first <= second {
        (first, second)
    } else {
        (second, first)
    };
    match (first, second) {
        (0, 0)
        | (0, 1)
        | (1, 1)
        | (2, 2)
        | (2, 3)
        | (3, 3)
        | (4, 4)
        | (5, 5)
        | (6, 6)
        | (0, 2)
        | (1, 3) => Polynomial::default(),
        (0, 3) => variable(VAR_A, 1),
        (1, 2) => variable(VAR_A, -1),
        (0, 4) | (2, 4) => variable(VAR_E0P0, 1),
        (1, 4) => variable(VAR_E0P1, 1),
        (3, 4) => variable(VAR_E0K1, 1),
        (0, 5) => variable(VAR_E1P0, 1),
        (1, 5) | (3, 5) => variable(VAR_E1P1, 1),
        (2, 5) => variable(VAR_E1K0, 1),
        (0, 6) => variable(VAR_E2P0, 1),
        (1, 6) => variable(VAR_E2P1, 1),
        (2, 6) => variable(VAR_E2K0, 1),
        (3, 6) => variable(VAR_E2P0, 1)
            .add(&variable(VAR_E2P1, 1))
            .add(&variable(VAR_E2K0, -1)),
        (4, 5) => variable(VAR_E0E1, 1),
        (4, 6) => variable(VAR_E0E2, 1),
        (5, 6) => variable(VAR_E1E2, 1),
        pair => panic!("missing primitive Gram entry {:?}", pair),
    }
}

struct GramSpace {
    pairings: Vec<Vec<Polynomial>>,
    variables_used: usize,
}

impl GramSpace {
    fn new(first_momentum: Vector, second_momentum: Vector) -> Self {
        let mut pairings = vec![vec![Polynomial::default(); PRIMITIVES]; PRIMITIVES];
        for first in 0..BASE_PRIMITIVES {
            for second in 0..BASE_PRIMITIVES {
                pairings[first][second] = base_gram(first, second);
            }
        }

        let transverse_momenta = [
            first_momentum,
            first_momentum,
            second_momentum,
            second_momentum,
        ];
        let mut next_variable = FIRST_TEST_GRAM;
        for (test_index, momentum) in IntoIterator::into_iter(transverse_momenta).enumerate() {
            let test_primitive = BASE_PRIMITIVES + test_index;
            let pivot = (0..BASE_PRIMITIVES)
                .find(|&index| momentum.0[index] != 0)
                .expect("transversality momentum has no base component");
            let pivot_coefficient = momentum.0[pivot];
            assert!(pivot_coefficient == 1 || pivot_coefficient == -1);

            for base in 0..BASE_PRIMITIVES {
                if base == pivot {
                    continue;
                }
                let entry = Polynomial::variable(next_variable);
                next_variable += 1;
                pairings[test_primitive][base] = entry.clone();
                pairings[base][test_primitive] = entry;
            }

            let mut pivot_entry = Polynomial::default();
            for base in 0..BASE_PRIMITIVES {
                if base == pivot || momentum.0[base] == 0 {
                    continue;
                }
                pivot_entry.add_assign(
                    &pairings[test_primitive][base]
                        .clone()
                        .scale(-momentum.0[base] / pivot_coefficient),
                );
            }
            pairings[test_primitive][pivot] = pivot_entry.clone();
            pairings[pivot][test_primitive] = pivot_entry;
        }

        for first in 0..TEST_VECTORS {
            for second in first..TEST_VECTORS {
                let entry = Polynomial::variable(next_variable);
                next_variable += 1;
                let first = BASE_PRIMITIVES + first;
                let second = BASE_PRIMITIVES + second;
                pairings[first][second] = entry.clone();
                pairings[second][first] = entry;
            }
        }
        assert!(next_variable <= VARIABLES);

        let result = Self {
            pairings,
            variables_used: next_variable,
        };
        for index in 0..2 {
            assert_eq!(result.dot(test_vector(index), first_momentum), Polynomial::default());
        }
        for index in 2..4 {
            assert_eq!(result.dot(test_vector(index), second_momentum), Polynomial::default());
        }
        result
    }

    fn dot(&self, first: Vector, second: Vector) -> Polynomial {
        let mut result = Polynomial::default();
        for left in 0..PRIMITIVES {
            for right in 0..PRIMITIVES {
                let coefficient = first.0[left] * second.0[right];
                if coefficient != 0 {
                    result.add_assign(&self.pairings[left][right].clone().scale(coefficient));
                }
            }
        }
        result
    }

    fn divide_by_reference(&self, polynomial: Polynomial, momentum: Vector, reference: Vector) -> Polynomial {
        let denominator = self.dot(momentum, reference);
        if denominator == Polynomial::variable(VAR_A) {
            polynomial.shift_exponent(VAR_A, -1)
        } else {
            assert_eq!(denominator, Polynomial::variable(VAR_A).scale(-1));
            polynomial.scale(-1).shift_exponent(VAR_A, -1)
        }
    }
}

fn vertex_momenta(vertex: usize) -> [Vector; 3] {
    match vertex {
        0 => [p(0), p(1), p(2)],
        1 => [k(0).scale(-1), k(1).scale(-1), k(2).scale(-1)],
        2..=4 => {
            let road = vertex - 2;
            [p(road).scale(-1), p(road).minus(k(road)), k(road)]
        }
        _ => unreachable!(),
    }
}

fn full_handle(vertex: usize, singleton: usize) -> Vector {
    let momenta = vertex_momenta(vertex);
    momenta[(singleton + 1) % 3].minus(momenta[(singleton + 2) % 3])
}

fn reduced_handle(vertex: usize, singleton: usize) -> Vector {
    vertex_momenta(vertex)[(singleton + 1) % 3].scale(2)
}

fn edge_endpoints(slot: usize) -> (usize, usize) {
    let road = slot / 2;
    let middle = 2 + road;
    if slot % 2 == 0 {
        (road, 3 * middle)
    } else {
        (3 + road, 3 * middle + 2)
    }
}

fn edge_momentum(slot: usize) -> Vector {
    let road = slot / 2;
    if slot % 2 == 0 {
        p(road)
    } else {
        k(road).scale(-1)
    }
}

fn edge_reference(slot: usize, shift: usize) -> Vector {
    assert!(shift == 1 || shift == 2);
    let road = slot / 2;
    if slot % 2 == 0 {
        k((road + shift) % 3)
    } else {
        p((road + shift) % 3)
    }
}

#[derive(Clone, Debug)]
struct DisjointSet {
    parent: [usize; NODES],
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

    fn join(&mut self, first: usize, second: usize) {
        let first = self.find(first);
        let second = self.find(second);
        if first != second {
            self.parent[second] = first;
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum EdgeAction {
    Open,
    Metric,
    LongitudinalForward,
    LongitudinalReverse,
}

fn evaluate_sector(
    pattern: [usize; VERTICES],
    actions: [EdgeAction; 6],
    reduced: bool,
    reference_shift: usize,
    extra_terminals: &[(usize, Vector)],
    gram: &GramSpace,
) -> Polynomial {
    let mut sets = DisjointSet::new();
    let mut terminals = Vec::<(usize, Vector)>::new();
    let mut coefficient: Int = 1;
    let mut inverse_a_power = 0;

    for vertex in 0..VERTICES {
        let singleton = pattern[vertex];
        sets.join(
            3 * vertex + (singleton + 1) % 3,
            3 * vertex + (singleton + 2) % 3,
        );
        let handle = if reduced {
            reduced_handle(vertex, singleton)
        } else {
            full_handle(vertex, singleton)
        };
        terminals.push((3 * vertex + singleton, handle));
    }
    for road in 0..3 {
        terminals.push((3 * (2 + road) + 1, epsilon(road)));
    }

    for (slot, action) in IntoIterator::into_iter(actions).enumerate() {
        let (first, second) = edge_endpoints(slot);
        match action {
            EdgeAction::Open => {}
            EdgeAction::Metric => {
                sets.join(first, second);
                coefficient = -coefficient;
            }
            EdgeAction::LongitudinalForward | EdgeAction::LongitudinalReverse => {
                let momentum = edge_momentum(slot);
                let reference = edge_reference(slot, reference_shift);
                let denominator = gram.dot(momentum, reference);
                if denominator == Polynomial::variable(VAR_A).scale(-1) {
                    coefficient = -coefficient;
                } else {
                    assert_eq!(denominator, Polynomial::variable(VAR_A));
                }
                let (left, right) = match action {
                    EdgeAction::LongitudinalForward => (momentum, reference),
                    EdgeAction::LongitudinalReverse => (reference, momentum),
                    _ => unreachable!(),
                };
                terminals.push((first, left));
                terminals.push((second, right));
                inverse_a_power += 1;
            }
        }
    }
    terminals.extend_from_slice(extra_terminals);

    let mut nodes_by_root = BTreeMap::<usize, usize>::new();
    for node in 0..NODES {
        let root = sets.find(node);
        *nodes_by_root.entry(root).or_default() += 1;
    }
    let mut terminals_by_root = BTreeMap::<usize, Vec<Vector>>::new();
    for (node, vector) in terminals {
        let root = sets.find(node);
        terminals_by_root.entry(root).or_default().push(vector);
    }

    let mut result = Polynomial::constant(coefficient);
    for root in nodes_by_root.keys() {
        match terminals_by_root.get(root).map_or(0, Vec::len) {
            0 => result = result.multiply(&Polynomial::variable(VAR_D)),
            2 => {
                let vectors = &terminals_by_root[root];
                result = result.multiply(&gram.dot(vectors[0], vectors[1]));
            }
            count => panic!("index strand has {} terminals", count),
        }
    }
    result.shift_exponent(VAR_A, -inverse_a_power)
}

fn patterns() -> Vec<[usize; VERTICES]> {
    (0..3_usize.pow(VERTICES as u32))
        .map(|mut code| {
            std::array::from_fn(|_| {
                let digit = code % 3;
                code /= 3;
                digit
            })
        })
        .collect()
}

fn spanning_tree_masks() -> Vec<u8> {
    let mut result = Vec::new();
    for mask in 0_u8..(1 << 6) {
        if mask.count_ones() != 4 {
            continue;
        }
        let mut parent: [usize; VERTICES] = std::array::from_fn(|index| index);
        fn find(parent: &mut [usize; VERTICES], node: usize) -> usize {
            if parent[node] != node {
                parent[node] = find(parent, parent[node]);
            }
            parent[node]
        }
        for slot in 0..6 {
            if mask & (1 << slot) != 0 {
                let (first, second) = edge_endpoints(slot);
                let first = find(&mut parent, first / 3);
                let second = find(&mut parent, second / 3);
                parent[second] = first;
            }
        }
        let roots: BTreeSet<_> = (0..VERTICES)
            .map(|vertex| find(&mut parent, vertex))
            .collect();
        if roots.len() == 1 {
            result.push(mask);
        }
    }
    assert_eq!(result.len(), 12);
    result
}

fn sum_patterns(
    patterns: &[[usize; VERTICES]],
    actions: [EdgeAction; 6],
    reduced: bool,
    reference_shift: usize,
    terminals: &[(usize, Vector)],
    gram: &GramSpace,
) -> Polynomial {
    let mut result = Polynomial::default();
    for &pattern in patterns {
        result.add_assign(&evaluate_sector(
            pattern,
            actions,
            reduced,
            reference_shift,
            terminals,
            gram,
        ));
    }
    result
}

fn tree_actions(tree_mask: u8) -> [EdgeAction; 6] {
    std::array::from_fn(|slot| {
        if tree_mask & (1 << slot) != 0 {
            EdgeAction::Metric
        } else {
            EdgeAction::Open
        }
    })
}

fn open_terminals(slot: usize, left: Vector, right: Vector) -> [(usize, Vector); 2] {
    let (first, second) = edge_endpoints(slot);
    [(first, left), (second, right)]
}

fn four_open_value(
    tree_mask: u8,
    closures: [usize; 2],
    vectors: [Vector; 4],
    gram: &GramSpace,
    patterns: &[[usize; VERTICES]],
) -> Polynomial {
    let mut terminals = Vec::new();
    terminals.extend(open_terminals(closures[0], vectors[0], vectors[1]));
    terminals.extend(open_terminals(closures[1], vectors[2], vectors[3]));
    sum_patterns(patterns, tree_actions(tree_mask), false, 1, &terminals, gram)
}

fn four_open_reduced_value(
    tree_mask: u8,
    closures: [usize; 2],
    vectors: [Vector; 4],
    gram: &GramSpace,
    patterns: &[[usize; VERTICES]],
) -> Polynomial {
    let mut terminals = Vec::new();
    terminals.extend(open_terminals(closures[0], vectors[0], vectors[1]));
    terminals.extend(open_terminals(closures[1], vectors[2], vectors[3]));
    sum_patterns(patterns, tree_actions(tree_mask), true, 1, &terminals, gram)
}

fn one_closed_value(
    tree_mask: u8,
    closed_slot: usize,
    open_slot: usize,
    open_vectors: [Vector; 2],
    reduced: bool,
    reference_shift: usize,
    physical: bool,
    gram: &GramSpace,
    patterns: &[[usize; VERTICES]],
) -> Polynomial {
    let terminals = open_terminals(open_slot, open_vectors[0], open_vectors[1]);
    let choices: &[EdgeAction] = if physical {
        &[
            EdgeAction::Metric,
            EdgeAction::LongitudinalForward,
            EdgeAction::LongitudinalReverse,
        ]
    } else {
        &[EdgeAction::Metric]
    };
    let mut result = Polynomial::default();
    for &choice in choices {
        let mut actions = tree_actions(tree_mask);
        actions[closed_slot] = choice;
        result.add_assign(&sum_patterns(
            patterns,
            actions,
            reduced,
            reference_shift,
            &terminals,
            gram,
        ));
    }
    result
}

fn one_closed_pattern_value(
    pattern: [usize; VERTICES],
    tree_mask: u8,
    closed_slot: usize,
    open_slot: usize,
    open_vectors: [Vector; 2],
    reduced: bool,
    reference_shift: usize,
    physical: bool,
    gram: &GramSpace,
) -> Polynomial {
    let terminals = open_terminals(open_slot, open_vectors[0], open_vectors[1]);
    let choices: &[EdgeAction] = if physical {
        &[
            EdgeAction::Metric,
            EdgeAction::LongitudinalForward,
            EdgeAction::LongitudinalReverse,
        ]
    } else {
        &[EdgeAction::Metric]
    };
    let mut result = Polynomial::default();
    for &choice in choices {
        let mut actions = tree_actions(tree_mask);
        actions[closed_slot] = choice;
        result.add_assign(&evaluate_sector(
            pattern,
            actions,
            reduced,
            reference_shift,
            &terminals,
            gram,
        ));
    }
    result
}

fn ward_coefficient(
    tree_mask: u8,
    closures: [usize; 2],
    pair_index: usize,
    reverse: bool,
    remaining_vectors: [Vector; 2],
    reference_shift: usize,
    gram: &GramSpace,
    patterns: &[[usize; VERTICES]],
) -> Polynomial {
    let slot = closures[pair_index];
    let momentum = edge_momentum(slot);
    let reference = edge_reference(slot, reference_shift);
    let (left, right) = if reverse {
        (reference, momentum)
    } else {
        (momentum, reference)
    };
    let vectors = if pair_index == 0 {
        [left, right, remaining_vectors[0], remaining_vectors[1]]
    } else {
        [remaining_vectors[0], remaining_vectors[1], left, right]
    };
    gram.divide_by_reference(
        four_open_value(tree_mask, closures, vectors, gram, patterns),
        momentum,
        reference,
    )
}

fn fully_closed_value(
    tree_mask: u8,
    closures: [usize; 2],
    reference_shift: usize,
    physical: bool,
    reduced: bool,
    reverse_choice_order: bool,
    gram: &GramSpace,
    patterns: &[[usize; VERTICES]],
) -> Polynomial {
    let choices: &[EdgeAction] = if physical {
        &[
            EdgeAction::Metric,
            EdgeAction::LongitudinalForward,
            EdgeAction::LongitudinalReverse,
        ]
    } else {
        &[EdgeAction::Metric]
    };
    let mut result = Polynomial::default();
    if reverse_choice_order {
        for &second in choices {
            for &first in choices {
                let mut actions = tree_actions(tree_mask);
                actions[closures[0]] = first;
                actions[closures[1]] = second;
                result.add_assign(&sum_patterns(
                    patterns,
                    actions,
                    reduced,
                    reference_shift,
                    &[],
                    gram,
                ));
            }
        }
    } else {
        for &first in choices {
            for &second in choices {
                let mut actions = tree_actions(tree_mask);
                actions[closures[0]] = first;
                actions[closures[1]] = second;
                result.add_assign(&sum_patterns(
                    patterns,
                    actions,
                    reduced,
                    reference_shift,
                    &[],
                    gram,
                ));
            }
        }
    }
    result
}

fn fully_closed_pattern_value(
    pattern: [usize; VERTICES],
    tree_mask: u8,
    closures: [usize; 2],
    reference_shift: usize,
    physical: bool,
    reduced: bool,
    gram: &GramSpace,
) -> Polynomial {
    let choices: &[EdgeAction] = if physical {
        &[
            EdgeAction::Metric,
            EdgeAction::LongitudinalForward,
            EdgeAction::LongitudinalReverse,
        ]
    } else {
        &[EdgeAction::Metric]
    };
    let mut result = Polynomial::default();
    for &first in choices {
        for &second in choices {
            let mut actions = tree_actions(tree_mask);
            actions[closures[0]] = first;
            actions[closures[1]] = second;
            result.add_assign(&evaluate_sector(
                pattern,
                actions,
                reduced,
                reference_shift,
                &[],
                gram,
            ));
        }
    }
    result
}

fn closure_vertices(slots: &[usize]) -> BTreeSet<usize> {
    slots
        .iter()
        .flat_map(|&slot| {
            let (first, second) = edge_endpoints(slot);
            [first / 3, second / 3]
        })
        .collect()
}

fn quotient_defect_count(
    patterns: &[[usize; VERTICES]],
    residuals: &[Polynomial],
    free_vertices: &BTreeSet<usize>,
) -> usize {
    assert_eq!(patterns.len(), residuals.len());
    let mut by_environment = BTreeMap::<Vec<usize>, Polynomial>::new();
    for (&pattern, residual) in patterns.iter().zip(residuals) {
        let environment: Vec<_> = (0..VERTICES)
            .filter(|vertex| !free_vertices.contains(vertex))
            .map(|vertex| pattern[vertex])
            .collect();
        by_environment
            .entry(environment)
            .or_default()
            .add_assign(residual);
    }
    by_environment
        .values()
        .filter(|polynomial| **polynomial != Polynomial::default())
        .count()
}

fn minimum_free_support(
    patterns: &[[usize; VERTICES]],
    residuals: &[Polynomial],
    mandatory_vertices: &BTreeSet<usize>,
) -> usize {
    let mandatory_mask = mandatory_vertices
        .iter()
        .fold(0_u8, |mask, &vertex| mask | (1 << vertex));
    for size in mandatory_vertices.len()..=VERTICES {
        for mask in 0_u8..(1 << VERTICES) {
            if mask.count_ones() as usize != size || mask & mandatory_mask != mandatory_mask {
                continue;
            }
            let free_vertices: BTreeSet<_> = (0..VERTICES)
                .filter(|vertex| mask & (1 << vertex) != 0)
                .collect();
            if quotient_defect_count(patterns, residuals, &free_vertices) == 0 {
                return size;
            }
        }
    }
    unreachable!("the fully summed realization identity is known to close")
}

#[derive(Default)]
struct AuditCounts {
    tree_ward_failures: usize,
    stable_ward_failures: usize,
    ward_formula_failures: usize,
    realization_failures: usize,
    reference_failures: usize,
    closure_order_failures: usize,
    final_failures: usize,
    reduced_ward_coefficient_failures: usize,
    nonzero_full_ward_coefficients: usize,
    ward_coefficient_reference_failures: usize,
    patternwise_partial_defects: usize,
    one_endpoint_quotient_defects: usize,
    edge_endpoint_quotient_defects: usize,
    patternwise_full_defects: usize,
    closure_union_quotient_defects: usize,
    partial_minimum_support: BTreeMap<usize, usize>,
    full_minimum_support: BTreeMap<usize, usize>,
    first_realization_defect: Option<(u8, usize, usize)>,
}

fn main() {
    let patterns = patterns();
    let trees = spanning_tree_masks();
    let mut audit = AuditCounts::default();
    let mut maximum_partial_monomials = 0;
    let mut variables_used = 0;

    for tree_mask in trees.iter().copied() {
        let closure_vec: Vec<_> = (0..6)
            .filter(|slot| tree_mask & (1 << slot) == 0)
            .collect();
        let closures = [closure_vec[0], closure_vec[1]];
        let momenta = [edge_momentum(closures[0]), edge_momentum(closures[1])];
        let gram = GramSpace::new(momenta[0], momenta[1]);
        variables_used = variables_used.max(gram.variables_used);
        let tests = [test_vector(0), test_vector(1), test_vector(2), test_vector(3)];

        for ward_vectors in [
            [momenta[0], tests[1], tests[2], tests[3]],
            [tests[0], momenta[0], tests[2], tests[3]],
            [tests[0], tests[1], momenta[1], tests[3]],
            [tests[0], tests[1], tests[2], momenta[1]],
        ] {
            if four_open_value(tree_mask, closures, ward_vectors, &gram, &patterns)
                != Polynomial::default()
            {
                audit.tree_ward_failures += 1;
            }
        }

        for reference_shift in [1, 2] {
            for pair_index in 0..2 {
                let other = 1 - pair_index;
                let (remaining_vectors, remaining_momentum) = if pair_index == 0 {
                    ([tests[2], tests[3]], momenta[1])
                } else {
                    ([tests[0], tests[1]], momenta[0])
                };
                let physical = one_closed_value(
                    tree_mask,
                    closures[pair_index],
                    closures[other],
                    remaining_vectors,
                    false,
                    reference_shift,
                    true,
                    &gram,
                    &patterns,
                );
                maximum_partial_monomials = maximum_partial_monomials.max(physical.0.len());
                let metric = one_closed_value(
                    tree_mask,
                    closures[pair_index],
                    closures[other],
                    remaining_vectors,
                    false,
                    reference_shift,
                    false,
                    &gram,
                    &patterns,
                );
                let graphical = one_closed_value(
                    tree_mask,
                    closures[pair_index],
                    closures[other],
                    remaining_vectors,
                    true,
                    reference_shift,
                    false,
                    &gram,
                    &patterns,
                );
                let n = ward_coefficient(
                    tree_mask,
                    closures,
                    pair_index,
                    false,
                    remaining_vectors,
                    reference_shift,
                    &gram,
                    &patterns,
                );
                let n_prime = ward_coefficient(
                    tree_mask,
                    closures,
                    pair_index,
                    true,
                    remaining_vectors,
                    reference_shift,
                    &gram,
                    &patterns,
                );
                if n != Polynomial::default() {
                    audit.nonzero_full_ward_coefficients += 1;
                }
                if n_prime != Polynomial::default() {
                    audit.nonzero_full_ward_coefficients += 1;
                }

                let momentum = momenta[pair_index];
                let reference = edge_reference(closures[pair_index], reference_shift);
                let reduced_forward_vectors = if pair_index == 0 {
                    [momentum, reference, remaining_vectors[0], remaining_vectors[1]]
                } else {
                    [remaining_vectors[0], remaining_vectors[1], momentum, reference]
                };
                let reduced_reverse_vectors = if pair_index == 0 {
                    [reference, momentum, remaining_vectors[0], remaining_vectors[1]]
                } else {
                    [remaining_vectors[0], remaining_vectors[1], reference, momentum]
                };
                for vectors in [reduced_forward_vectors, reduced_reverse_vectors] {
                    let coefficient = gram.divide_by_reference(
                        four_open_reduced_value(tree_mask, closures, vectors, &gram, &patterns),
                        momentum,
                        reference,
                    );
                    if coefficient != Polynomial::default() {
                        audit.reduced_ward_coefficient_failures += 1;
                    }
                }
                if physical != metric.clone().add(&n).add(&n_prime) {
                    audit.ward_formula_failures += 1;
                }
                if physical != graphical {
                    audit.realization_failures += 1;
                    audit
                        .first_realization_defect
                        .get_or_insert((tree_mask, closures[pair_index], physical.clone().add(&graphical.scale(-1)).0.len()));
                }

                // Resolve the same equality by the five local cubic-sector
                // origins.  This tests whether the cancellation is already
                // supported on the two endpoint vertices of the closed edge,
                // uniformly in every fixed choice of the other three vertex
                // sectors.
                let partial_residuals: Vec<_> = patterns
                    .iter()
                    .map(|&pattern| {
                        let source = one_closed_pattern_value(
                            pattern,
                            tree_mask,
                            closures[pair_index],
                            closures[other],
                            remaining_vectors,
                            false,
                            reference_shift,
                            true,
                            &gram,
                        );
                        let target = one_closed_pattern_value(
                            pattern,
                            tree_mask,
                            closures[pair_index],
                            closures[other],
                            remaining_vectors,
                            true,
                            reference_shift,
                            false,
                            &gram,
                        );
                        source.add(&target.scale(-1))
                    })
                    .collect();
                audit.patternwise_partial_defects += partial_residuals
                    .iter()
                    .filter(|polynomial| **polynomial != Polynomial::default())
                    .count();
                let endpoints = closure_vertices(&[closures[pair_index]]);
                assert_eq!(endpoints.len(), 2);
                for &vertex in &endpoints {
                    audit.one_endpoint_quotient_defects += quotient_defect_count(
                        &patterns,
                        &partial_residuals,
                        &BTreeSet::from([vertex]),
                    );
                }
                audit.edge_endpoint_quotient_defects +=
                    quotient_defect_count(&patterns, &partial_residuals, &endpoints);
                *audit
                    .partial_minimum_support
                    .entry(minimum_free_support(&patterns, &partial_residuals, &endpoints))
                    .or_default() += 1;

                let stable_left = if pair_index == 0 {
                    [remaining_momentum, tests[3]]
                } else {
                    [remaining_momentum, tests[1]]
                };
                let stable_right = if pair_index == 0 {
                    [tests[2], remaining_momentum]
                } else {
                    [tests[0], remaining_momentum]
                };
                for remaining in [stable_left, stable_right] {
                    if one_closed_value(
                        tree_mask,
                        closures[pair_index],
                        closures[other],
                        remaining,
                        false,
                        reference_shift,
                        true,
                        &gram,
                        &patterns,
                    ) != Polynomial::default()
                    {
                        audit.stable_ward_failures += 1;
                    }
                }

                if reference_shift == 2 {
                    let first_reference = one_closed_value(
                        tree_mask,
                        closures[pair_index],
                        closures[other],
                        remaining_vectors,
                        false,
                        1,
                        true,
                        &gram,
                        &patterns,
                    );
                    if first_reference != physical {
                        audit.reference_failures += 1;
                    }
                    let first_n = ward_coefficient(
                        tree_mask,
                        closures,
                        pair_index,
                        false,
                        remaining_vectors,
                        1,
                        &gram,
                        &patterns,
                    );
                    let first_n_prime = ward_coefficient(
                        tree_mask,
                        closures,
                        pair_index,
                        true,
                        remaining_vectors,
                        1,
                        &gram,
                        &patterns,
                    );
                    if first_n != n || first_n_prime != n_prime {
                        audit.ward_coefficient_reference_failures += 1;
                    }
                }
            }

            let first_order = fully_closed_value(
                tree_mask,
                closures,
                reference_shift,
                true,
                false,
                false,
                &gram,
                &patterns,
            );
            let second_order = fully_closed_value(
                tree_mask,
                closures,
                reference_shift,
                true,
                false,
                true,
                &gram,
                &patterns,
            );
            if first_order != second_order {
                audit.closure_order_failures += 1;
            }
            let graphical = fully_closed_value(
                tree_mask,
                closures,
                reference_shift,
                false,
                true,
                false,
                &gram,
                &patterns,
            );
            if first_order != graphical {
                audit.final_failures += 1;
            }
            let full_residuals: Vec<_> = patterns
                .iter()
                .map(|&pattern| {
                    let source = fully_closed_pattern_value(
                        pattern,
                        tree_mask,
                        closures,
                        reference_shift,
                        true,
                        false,
                        &gram,
                    );
                    let target = fully_closed_pattern_value(
                        pattern,
                        tree_mask,
                        closures,
                        reference_shift,
                        false,
                        true,
                        &gram,
                    );
                    source.add(&target.scale(-1))
                })
                .collect();
            audit.patternwise_full_defects += full_residuals
                .iter()
                .filter(|polynomial| **polynomial != Polynomial::default())
                .count();
            let union = closure_vertices(&closures);
            audit.closure_union_quotient_defects +=
                quotient_defect_count(&patterns, &full_residuals, &union);
            *audit
                .full_minimum_support
                .entry(minimum_free_support(&patterns, &full_residuals, &union))
                .or_default() += 1;
            assert!(first_order.minimum_exponent(VAR_A) >= 0);
        }
    }

    println!("Two-open-pair Ward/naturality audit");
    println!("===================================");
    println!("  spanning-tree carriers:              {}", trees.len());
    println!("  generic test-polarization variables: {}", variables_used - FIRST_TEST_GRAM);
    println!("  total Gram coordinates used:         {variables_used}");
    println!("  local cubic sector words:            {}", patterns.len());
    println!("  maximum partial monomial count:      {maximum_partial_monomials}");
    println!("  tree Ward failures:                  {}", audit.tree_ward_failures);
    println!("  post-closure Ward failures:          {}", audit.stable_ward_failures);
    println!("  one-edge Ward-formula failures:      {}", audit.ward_formula_failures);
    println!("  partial realization failures:        {}", audit.realization_failures);
    println!("  reference-independence failures:     {}", audit.reference_failures);
    println!("  closure-order failures:              {}", audit.closure_order_failures);
    println!("  final physical/graphical failures:   {}", audit.final_failures);
    println!(
        "  reduced Ward-coefficient failures:   {}",
        audit.reduced_ward_coefficient_failures
    );
    println!(
        "  nonzero full Ward coefficients:       {}",
        audit.nonzero_full_ward_coefficients
    );
    println!(
        "  Ward-coefficient reference failures:  {}",
        audit.ward_coefficient_reference_failures
    );
    println!(
        "  nonzero patternwise partial defects:   {}",
        audit.patternwise_partial_defects
    );
    println!(
        "  one-endpoint quotient defects:         {}",
        audit.one_endpoint_quotient_defects
    );
    println!(
        "  two-endpoint quotient defects:         {}",
        audit.edge_endpoint_quotient_defects
    );
    println!(
        "  nonzero patternwise full defects:      {}",
        audit.patternwise_full_defects
    );
    println!(
        "  closure-union quotient defects:        {}",
        audit.closure_union_quotient_defects
    );
    println!(
        "  minimum partial origin support:        {:?}",
        audit.partial_minimum_support
    );
    println!(
        "  minimum full origin support:           {:?}",
        audit.full_minimum_support
    );
    if let Some((tree, slot, terms)) = audit.first_realization_defect {
        println!("  first realization defect: tree={tree:06b}, slot={slot}, terms={terms}");
    }

    assert_eq!(audit.tree_ward_failures, 0);
    assert_eq!(audit.stable_ward_failures, 0);
    assert_eq!(audit.ward_formula_failures, 0);
    assert_eq!(audit.reference_failures, 0);
    assert_eq!(audit.closure_order_failures, 0);
    assert_eq!(audit.final_failures, 0);
    assert_eq!(audit.reduced_ward_coefficient_failures, 0);
    assert_eq!(audit.ward_coefficient_reference_failures, 0);
    assert_eq!(audit.edge_endpoint_quotient_defects, 1200);
    assert_eq!(audit.closure_union_quotient_defects, 144);
    assert_eq!(audit.partial_minimum_support, BTreeMap::from([(5, 48)]));
    assert_eq!(audit.full_minimum_support, BTreeMap::from([(5, 24)]));

    println!();
    if audit.realization_failures == 0 {
        println!("VERDICT");
        println!("  Ward alignment is stable in every marked-theta two-open-pair carrier");
        println!("  each one-edge physical closure equals the reduced graphical carrier");
        println!("  both realization squares commute before the second closure");
        println!("  the equality is not strict on the raw cubic-sector origin basis");
        println!("  every presentation needs transport across all five vertex-sector coordinates");
    } else {
        println!("VERDICT");
        println!("  physical Ward alignment and closure coherence pass");
        println!("  the candidate partial reduced-graph realization is false");
        println!("  final equality is produced only after the second physical trace");
    }
}
