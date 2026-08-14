//! Exact formal origin-resolution and two-closure coherence certificate.
//!
//! This checker deliberately separates two statements which are easy to
//! conflate:
//!
//! * the polynomial residuals have integral fillers in the cellular chains of
//!   `(Delta^2)^5`; and
//! * those fillers are canonically realized by local Ward/V moves.
//!
//! Only the first statement follows from the formal filled-triangle carrier.
//! The checker constructs that filler explicitly.  It does not label a formal
//! simplex edge by a three-gluon Ward identity, so it is not a certificate of
//! the second statement.

#[allow(dead_code)]
mod ward {
    // Exact two-open-pair Ward/naturality audit on the marked-theta carrier.
    //
    // A spanning tree of the five-vertex marked-theta graph leaves two internal
    // edge pairs open.  This checker keeps those four state indices external,
    // contracts them with four algebraically generic transverse test vectors,
    // and works in a Gram-free polynomial chart.  It tests, before the second
    // closure:
    //
    // 1. the four tree Ward identities;
    // 2. Ward stability after either physical-projector closure;
    // 3. the one-edge Ward formula `metric + N + N'`;
    // 4. the proposed realization square from physical closure to the
    //    gauge-reduced graphical/curve-cover network;
    // 5. reference independence and both closure orders.
    //
    // No spacetime dimension, floating-point sample, or Gram determinant is
    // imposed.  The four test polarizations have independent Gram coordinates
    // modulo only their required transversality equations.

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
                assert_eq!(
                    result.dot(test_vector(index), first_momentum),
                    Polynomial::default()
                );
            }
            for index in 2..4 {
                assert_eq!(
                    result.dot(test_vector(index), second_momentum),
                    Polynomial::default()
                );
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

        fn divide_by_reference(
            &self,
            polynomial: Polynomial,
            momentum: Vector,
            reference: Vector,
        ) -> Polynomial {
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
        sum_patterns(
            patterns,
            tree_actions(tree_mask),
            false,
            1,
            &terminals,
            gram,
        )
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

    fn prior_audit_main() {
        let patterns = patterns();
        let trees = spanning_tree_masks();
        let mut audit = AuditCounts::default();
        let mut maximum_partial_monomials = 0;
        let mut variables_used = 0;

        for tree_mask in trees.iter().copied() {
            let closure_vec: Vec<_> = (0..6).filter(|slot| tree_mask & (1 << slot) == 0).collect();
            let closures = [closure_vec[0], closure_vec[1]];
            let momenta = [edge_momentum(closures[0]), edge_momentum(closures[1])];
            let gram = GramSpace::new(momenta[0], momenta[1]);
            variables_used = variables_used.max(gram.variables_used);
            let tests = [
                test_vector(0),
                test_vector(1),
                test_vector(2),
                test_vector(3),
            ];

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
                        [
                            momentum,
                            reference,
                            remaining_vectors[0],
                            remaining_vectors[1],
                        ]
                    } else {
                        [
                            remaining_vectors[0],
                            remaining_vectors[1],
                            momentum,
                            reference,
                        ]
                    };
                    let reduced_reverse_vectors = if pair_index == 0 {
                        [
                            reference,
                            momentum,
                            remaining_vectors[0],
                            remaining_vectors[1],
                        ]
                    } else {
                        [
                            remaining_vectors[0],
                            remaining_vectors[1],
                            reference,
                            momentum,
                        ]
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
                        audit.first_realization_defect.get_or_insert((
                            tree_mask,
                            closures[pair_index],
                            physical.clone().add(&graphical.scale(-1)).0.len(),
                        ));
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
                        .entry(minimum_free_support(
                            &patterns,
                            &partial_residuals,
                            &endpoints,
                        ))
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
        println!(
            "  generic test-polarization variables: {}",
            variables_used - FIRST_TEST_GRAM
        );
        println!("  total Gram coordinates used:         {variables_used}");
        println!("  local cubic sector words:            {}", patterns.len());
        println!("  maximum partial monomial count:      {maximum_partial_monomials}");
        println!(
            "  tree Ward failures:                  {}",
            audit.tree_ward_failures
        );
        println!(
            "  post-closure Ward failures:          {}",
            audit.stable_ward_failures
        );
        println!(
            "  one-edge Ward-formula failures:      {}",
            audit.ward_formula_failures
        );
        println!(
            "  partial realization failures:        {}",
            audit.realization_failures
        );
        println!(
            "  reference-independence failures:     {}",
            audit.reference_failures
        );
        println!(
            "  closure-order failures:              {}",
            audit.closure_order_failures
        );
        println!(
            "  final physical/graphical failures:   {}",
            audit.final_failures
        );
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
            println!(
                "  every presentation needs transport across all five vertex-sector coordinates"
            );
        } else {
            println!("VERDICT");
            println!("  physical Ward alignment and closure coherence pass");
            println!("  the candidate partial reduced-graph realization is false");
            println!("  final equality is produced only after the second physical trace");
        }
    }

    #[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
    struct EdgeCell {
        coordinate: u8,
        low: u8,
        high: u8,
        environment: [u8; VERTICES],
    }

    #[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
    enum TwoCell {
        Triangle {
            coordinate: u8,
            environment: [u8; VERTICES],
        },
        Square {
            first_coordinate: u8,
            first_low: u8,
            first_high: u8,
            second_coordinate: u8,
            second_low: u8,
            second_high: u8,
            environment: [u8; VERTICES],
        },
    }

    type ZeroChain = Vec<Polynomial>;

    #[derive(Clone, Debug, Default, Eq, PartialEq)]
    struct OneChain(BTreeMap<EdgeCell, Polynomial>);

    #[derive(Clone, Debug, Default, Eq, PartialEq)]
    struct TwoChain(BTreeMap<TwoCell, Polynomial>);

    fn add_term<K: Copy + Ord>(map: &mut BTreeMap<K, Polynomial>, key: K, value: &Polynomial) {
        if value == &Polynomial::default() {
            return;
        }
        let became_zero = {
            let entry = map.entry(key).or_default();
            entry.add_assign(value);
            *entry == Polynomial::default()
        };
        if became_zero {
            map.remove(&key);
        }
    }

    fn subtract_polynomials(first: &Polynomial, second: &Polynomial) -> Polynomial {
        first.clone().add(&second.clone().scale(-1))
    }

    fn zero_chain() -> ZeroChain {
        vec![Polynomial::default(); 3_usize.pow(VERTICES as u32)]
    }

    fn pattern_code(pattern: [usize; VERTICES]) -> usize {
        let mut place = 1;
        let mut result = 0;
        for digit in pattern {
            result += place * digit;
            place *= 3;
        }
        result
    }

    fn pattern_u8(pattern: [usize; VERTICES]) -> [u8; VERTICES] {
        pattern.map(|entry| entry as u8)
    }

    fn chain_difference(first: &ZeroChain, second: &ZeroChain) -> ZeroChain {
        first
            .iter()
            .zip(second)
            .map(|(left, right)| subtract_polynomials(left, right))
            .collect()
    }

    fn zero_add_assign(target: &mut ZeroChain, source: &ZeroChain) {
        for (left, right) in target.iter_mut().zip(source) {
            left.add_assign(right);
        }
    }

    fn augmentation(chain: &ZeroChain) -> Polynomial {
        let mut result = Polynomial::default();
        for coefficient in chain {
            result.add_assign(coefficient);
        }
        result
    }

    impl OneChain {
        fn add_assign(&mut self, other: &Self) {
            for (&cell, coefficient) in &other.0 {
                add_term(&mut self.0, cell, coefficient);
            }
        }

        fn subtract_assign(&mut self, other: &Self) {
            for (&cell, coefficient) in &other.0 {
                add_term(&mut self.0, cell, &coefficient.clone().scale(-1));
            }
        }

        fn scale(mut self, scalar: Int) -> Self {
            self.0 = self
                .0
                .into_iter()
                .filter_map(|(cell, coefficient)| {
                    let coefficient = coefficient.scale(scalar);
                    (coefficient != Polynomial::default()).then_some((cell, coefficient))
                })
                .collect();
            self
        }

        fn boundary(&self) -> ZeroChain {
            let mut result = zero_chain();
            for (cell, coefficient) in &self.0 {
                let mut low = cell.environment.map(|entry| entry as usize);
                let mut high = low;
                low[cell.coordinate as usize] = cell.low as usize;
                high[cell.coordinate as usize] = cell.high as usize;
                result[pattern_code(high)].add_assign(coefficient);
                result[pattern_code(low)].add_assign(&coefficient.clone().scale(-1));
            }
            result
        }

        fn minimum_a_exponent(&self) -> i8 {
            self.0
                .values()
                .map(|coefficient| coefficient.minimum_exponent(VAR_A))
                .min()
                .unwrap_or(0)
        }
    }

    impl TwoChain {
        fn boundary(&self) -> OneChain {
            let mut result = OneChain::default();
            for (cell, coefficient) in &self.0 {
                match *cell {
                    TwoCell::Triangle {
                        coordinate,
                        environment,
                    } => {
                        for (low, high, sign) in [(1, 2, 1), (0, 2, -1), (0, 1, 1)] {
                            let mut environment = environment;
                            environment[coordinate as usize] = 0;
                            add_term(
                                &mut result.0,
                                EdgeCell {
                                    coordinate,
                                    low,
                                    high,
                                    environment,
                                },
                                &coefficient.clone().scale(sign),
                            );
                        }
                    }
                    TwoCell::Square {
                        first_coordinate,
                        first_low,
                        first_high,
                        second_coordinate,
                        second_low,
                        second_high,
                        environment,
                    } => {
                        // d(e_first x e_second)
                        // = d(e_first) x e_second - e_first x d(e_second).
                        for (endpoint, sign) in [(first_high, 1), (first_low, -1)] {
                            let mut edge_environment = environment;
                            edge_environment[first_coordinate as usize] = endpoint;
                            edge_environment[second_coordinate as usize] = 0;
                            add_term(
                                &mut result.0,
                                EdgeCell {
                                    coordinate: second_coordinate,
                                    low: second_low,
                                    high: second_high,
                                    environment: edge_environment,
                                },
                                &coefficient.clone().scale(sign),
                            );
                        }
                        for (endpoint, sign) in [(second_high, -1), (second_low, 1)] {
                            let mut edge_environment = environment;
                            edge_environment[first_coordinate as usize] = 0;
                            edge_environment[second_coordinate as usize] = endpoint;
                            add_term(
                                &mut result.0,
                                EdgeCell {
                                    coordinate: first_coordinate,
                                    low: first_low,
                                    high: first_high,
                                    environment: edge_environment,
                                },
                                &coefficient.clone().scale(sign),
                            );
                        }
                    }
                }
            }
            result
        }

        fn cell_counts(&self) -> (usize, usize) {
            let triangles = self
                .0
                .keys()
                .filter(|cell| matches!(cell, TwoCell::Triangle { .. }))
                .count();
            (triangles, self.0.len() - triangles)
        }

        fn minimum_a_exponent(&self) -> i8 {
            self.0
                .values()
                .map(|coefficient| coefficient.minimum_exponent(VAR_A))
                .min()
                .unwrap_or(0)
        }
    }

    #[derive(Clone, Copy, Debug, Eq, PartialEq)]
    struct Contraction {
        order: [usize; VERTICES],
        base: [u8; VERTICES],
    }

    fn oriented_edge(from: u8, to: u8) -> Option<(u8, u8, Int)> {
        match from.cmp(&to) {
            std::cmp::Ordering::Less => Some((from, to, 1)),
            std::cmp::Ordering::Greater => Some((to, from, -1)),
            std::cmp::Ordering::Equal => None,
        }
    }

    fn permutation_sign(values: [u8; 3]) -> Int {
        let inversions = usize::from(values[0] > values[1])
            + usize::from(values[0] > values[2])
            + usize::from(values[1] > values[2]);
        if inversions % 2 == 0 {
            1
        } else {
            -1
        }
    }

    impl Contraction {
        fn for_slot(slot: usize) -> Self {
            let road = slot / 2;
            let central = slot % 2;
            Self {
                order: [
                    central,
                    2 + road,
                    1 - central,
                    2 + (road + 1) % 3,
                    2 + (road + 2) % 3,
                ],
                // The central singleton labels rotate with the roads.  The
                // local labels at the three road vertices do not.
                base: [road as u8, road as u8, 0, 0, 0],
            }
        }

        fn zero(&self, chain: &ZeroChain) -> OneChain {
            let mut result = OneChain::default();
            for (pattern, coefficient) in patterns().into_iter().zip(chain) {
                if coefficient == &Polynomial::default() {
                    continue;
                }
                let pattern = pattern_u8(pattern);
                for position in 0..VERTICES {
                    let coordinate = self.order[position];
                    let Some((low, high, sign)) =
                        oriented_edge(self.base[coordinate], pattern[coordinate])
                    else {
                        continue;
                    };
                    let mut environment = pattern;
                    for earlier in 0..position {
                        let earlier = self.order[earlier];
                        environment[earlier] = self.base[earlier];
                    }
                    environment[coordinate] = 0;
                    add_term(
                        &mut result.0,
                        EdgeCell {
                            coordinate: coordinate as u8,
                            low,
                            high,
                            environment,
                        },
                        &coefficient.clone().scale(sign),
                    );
                }
            }
            result
        }

        fn one(&self, chain: &OneChain) -> TwoChain {
            let mut result = TwoChain::default();
            for (edge, coefficient) in &chain.0 {
                let edge_coordinate = edge.coordinate as usize;
                let edge_position = self
                    .order
                    .iter()
                    .position(|&coordinate| coordinate == edge_coordinate)
                    .unwrap();

                for position in 0..edge_position {
                    let coordinate = self.order[position];
                    let vertex = edge.environment[coordinate];
                    let Some((low, high, edge_sign)) = oriented_edge(self.base[coordinate], vertex)
                    else {
                        continue;
                    };
                    let mut environment = edge.environment;
                    for earlier in 0..position {
                        let earlier = self.order[earlier];
                        environment[earlier] = self.base[earlier];
                    }
                    environment[coordinate] = 0;
                    environment[edge_coordinate] = 0;

                    let (cell, coordinate_sign) = if coordinate < edge_coordinate {
                        (
                            TwoCell::Square {
                                first_coordinate: coordinate as u8,
                                first_low: low,
                                first_high: high,
                                second_coordinate: edge.coordinate,
                                second_low: edge.low,
                                second_high: edge.high,
                                environment,
                            },
                            1,
                        )
                    } else {
                        (
                            TwoCell::Square {
                                first_coordinate: edge.coordinate,
                                first_low: edge.low,
                                first_high: edge.high,
                                second_coordinate: coordinate as u8,
                                second_low: low,
                                second_high: high,
                                environment,
                            },
                            -1,
                        )
                    };
                    add_term(
                        &mut result.0,
                        cell,
                        &coefficient.clone().scale(edge_sign * coordinate_sign),
                    );
                }

                let base = self.base[edge_coordinate];
                if base != edge.low && base != edge.high {
                    let mut environment = edge.environment;
                    for earlier in 0..edge_position {
                        let earlier = self.order[earlier];
                        environment[earlier] = self.base[earlier];
                    }
                    environment[edge_coordinate] = 0;
                    add_term(
                        &mut result.0,
                        TwoCell::Triangle {
                            coordinate: edge.coordinate,
                            environment,
                        },
                        &coefficient
                            .clone()
                            .scale(permutation_sign([base, edge.low, edge.high])),
                    );
                }
            }
            result
        }
    }

    fn physical_choices() -> [EdgeAction; 3] {
        [
            EdgeAction::Metric,
            EdgeAction::LongitudinalForward,
            EdgeAction::LongitudinalReverse,
        ]
    }

    fn partial_residual(
        tree_mask: u8,
        closures: [usize; 2],
        pair_index: usize,
        reference_shift: usize,
        gram: &GramSpace,
    ) -> ZeroChain {
        let tests = [
            test_vector(0),
            test_vector(1),
            test_vector(2),
            test_vector(3),
        ];
        let remaining_vectors = if pair_index == 0 {
            [tests[2], tests[3]]
        } else {
            [tests[0], tests[1]]
        };
        patterns()
            .into_iter()
            .map(|pattern| {
                let source = one_closed_pattern_value(
                    pattern,
                    tree_mask,
                    closures[pair_index],
                    closures[1 - pair_index],
                    remaining_vectors,
                    false,
                    reference_shift,
                    true,
                    gram,
                );
                let target = one_closed_pattern_value(
                    pattern,
                    tree_mask,
                    closures[pair_index],
                    closures[1 - pair_index],
                    remaining_vectors,
                    true,
                    reference_shift,
                    false,
                    gram,
                );
                subtract_polynomials(&source, &target)
            })
            .collect()
    }

    fn fully_physical_pattern(
        pattern: [usize; VERTICES],
        tree_mask: u8,
        closures: [usize; 2],
        reference_shift: usize,
        gram: &GramSpace,
    ) -> Polynomial {
        fully_closed_pattern_value(
            pattern,
            tree_mask,
            closures,
            reference_shift,
            true,
            false,
            gram,
        )
    }

    fn fully_graphical_pattern(
        pattern: [usize; VERTICES],
        tree_mask: u8,
        closures: [usize; 2],
        reference_shift: usize,
        gram: &GramSpace,
    ) -> Polynomial {
        fully_closed_pattern_value(
            pattern,
            tree_mask,
            closures,
            reference_shift,
            false,
            true,
            gram,
        )
    }

    fn intermediate_pattern(
        pattern: [usize; VERTICES],
        tree_mask: u8,
        closures: [usize; 2],
        first_index: usize,
        reference_shift: usize,
        gram: &GramSpace,
    ) -> Polynomial {
        let first = closures[first_index];
        let second = closures[1 - first_index];
        let mut result = Polynomial::default();
        for choice in physical_choices() {
            let mut actions = tree_actions(tree_mask);
            actions[first] = EdgeAction::Metric;
            actions[second] = choice;
            result.add_assign(&evaluate_sector(
                pattern,
                actions,
                true,
                reference_shift,
                &[],
                gram,
            ));
        }
        result
    }

    struct ClosureData {
        physical: ZeroChain,
        graphical: ZeroChain,
        intermediate: [ZeroChain; 2],
    }

    fn closure_data(
        tree_mask: u8,
        closures: [usize; 2],
        reference_shift: usize,
        gram: &GramSpace,
    ) -> ClosureData {
        let mut physical = ZeroChain::new();
        let mut graphical = ZeroChain::new();
        let mut first = ZeroChain::new();
        let mut second = ZeroChain::new();
        for pattern in patterns() {
            physical.push(fully_physical_pattern(
                pattern,
                tree_mask,
                closures,
                reference_shift,
                gram,
            ));
            graphical.push(fully_graphical_pattern(
                pattern,
                tree_mask,
                closures,
                reference_shift,
                gram,
            ));
            first.push(intermediate_pattern(
                pattern,
                tree_mask,
                closures,
                0,
                reference_shift,
                gram,
            ));
            second.push(intermediate_pattern(
                pattern,
                tree_mask,
                closures,
                1,
                reference_shift,
                gram,
            ));
        }
        ClosureData {
            physical,
            graphical,
            intermediate: [first, second],
        }
    }

    fn closure_homotopy(data: &ClosureData, closures: [usize; 2], first: usize) -> OneChain {
        let second = 1 - first;
        let first_leg = chain_difference(&data.physical, &data.intermediate[first]);
        let second_leg = chain_difference(&data.intermediate[first], &data.graphical);
        assert_eq!(augmentation(&first_leg), Polynomial::default());
        assert_eq!(augmentation(&second_leg), Polynomial::default());
        let mut result = Contraction::for_slot(closures[first]).zero(&first_leg);
        result.add_assign(&Contraction::for_slot(closures[second]).zero(&second_leg));
        result
    }

    fn rotate_vertex(vertex: usize) -> usize {
        match vertex {
            0 | 1 => vertex,
            2..=4 => 2 + (vertex - 2 + 1) % 3,
            _ => unreachable!(),
        }
    }

    fn rotate_label(vertex: usize, label: u8) -> u8 {
        if vertex < 2 {
            (label + 1) % 3
        } else {
            label
        }
    }

    fn rotate_pattern(pattern: [u8; VERTICES]) -> [u8; VERTICES] {
        let mut result = [0; VERTICES];
        for vertex in 0..VERTICES {
            result[rotate_vertex(vertex)] = rotate_label(vertex, pattern[vertex]);
        }
        result
    }

    fn rotate_edge(cell: EdgeCell) -> (EdgeCell, Int) {
        let coordinate = cell.coordinate as usize;
        let target_coordinate = rotate_vertex(coordinate);
        let rotated_low = rotate_label(coordinate, cell.low);
        let rotated_high = rotate_label(coordinate, cell.high);
        let (low, high, sign) = oriented_edge(rotated_low, rotated_high).unwrap();
        let mut environment = rotate_pattern(cell.environment);
        environment[target_coordinate] = 0;
        (
            EdgeCell {
                coordinate: target_coordinate as u8,
                low,
                high,
                environment,
            },
            sign,
        )
    }

    fn rotate_one(chain: &OneChain) -> OneChain {
        let mut result = OneChain::default();
        for (&cell, coefficient) in &chain.0 {
            let (cell, sign) = rotate_edge(cell);
            add_term(&mut result.0, cell, &coefficient.clone().scale(sign));
        }
        result
    }

    fn rotate_two_cell(cell: TwoCell) -> (TwoCell, Int) {
        match cell {
            TwoCell::Triangle {
                coordinate,
                environment,
            } => {
                let source = coordinate as usize;
                let target = rotate_vertex(source);
                let triangle_sign = if source < 2 {
                    permutation_sign([1, 2, 0])
                } else {
                    1
                };
                let mut environment = rotate_pattern(environment);
                environment[target] = 0;
                (
                    TwoCell::Triangle {
                        coordinate: target as u8,
                        environment,
                    },
                    triangle_sign,
                )
            }
            TwoCell::Square {
                first_coordinate,
                first_low,
                first_high,
                second_coordinate,
                second_low,
                second_high,
                environment,
            } => {
                let first_source = first_coordinate as usize;
                let second_source = second_coordinate as usize;
                let first_target = rotate_vertex(first_source);
                let second_target = rotate_vertex(second_source);
                let (first_low, first_high, first_sign) = oriented_edge(
                    rotate_label(first_source, first_low),
                    rotate_label(first_source, first_high),
                )
                .unwrap();
                let (second_low, second_high, second_sign) = oriented_edge(
                    rotate_label(second_source, second_low),
                    rotate_label(second_source, second_high),
                )
                .unwrap();
                let mut environment = rotate_pattern(environment);
                environment[first_target] = 0;
                environment[second_target] = 0;
                if first_target < second_target {
                    (
                        TwoCell::Square {
                            first_coordinate: first_target as u8,
                            first_low,
                            first_high,
                            second_coordinate: second_target as u8,
                            second_low,
                            second_high,
                            environment,
                        },
                        first_sign * second_sign,
                    )
                } else {
                    (
                        TwoCell::Square {
                            first_coordinate: second_target as u8,
                            first_low: second_low,
                            first_high: second_high,
                            second_coordinate: first_target as u8,
                            second_low: first_low,
                            second_high: first_high,
                            environment,
                        },
                        -first_sign * second_sign,
                    )
                }
            }
        }
    }

    fn rotate_two(chain: &TwoChain) -> TwoChain {
        let mut result = TwoChain::default();
        for (&cell, coefficient) in &chain.0 {
            let (cell, sign) = rotate_two_cell(cell);
            add_term(&mut result.0, cell, &coefficient.clone().scale(sign));
        }
        result
    }

    fn singleton_edge(cell: EdgeCell) -> OneChain {
        OneChain(BTreeMap::from([(cell, Polynomial::constant(1))]))
    }

    fn formal_rotation_audit() -> (usize, usize) {
        let mut zero_checks = 0;
        let mut one_checks = 0;
        for slot in 0..6 {
            let contraction = Contraction::for_slot(slot);
            let rotated_contraction = Contraction::for_slot((slot + 2) % 6);
            for pattern in patterns() {
                let mut basis = zero_chain();
                basis[pattern_code(pattern)] = Polynomial::constant(1);
                let mut rotated_basis = zero_chain();
                let rotated_pattern =
                    rotate_pattern(pattern_u8(pattern)).map(|entry| entry as usize);
                rotated_basis[pattern_code(rotated_pattern)] = Polynomial::constant(1);
                assert_eq!(
                    rotate_one(&contraction.zero(&basis)),
                    rotated_contraction.zero(&rotated_basis)
                );
                zero_checks += 1;
            }

            for coordinate in 0..VERTICES {
                for (low, high) in [(0, 1), (0, 2), (1, 2)] {
                    for pattern in patterns() {
                        if pattern[coordinate] != 0 {
                            continue;
                        }
                        let cell = EdgeCell {
                            coordinate: coordinate as u8,
                            low,
                            high,
                            environment: pattern_u8(pattern),
                        };
                        let chain = singleton_edge(cell);
                        assert_eq!(
                            rotate_two(&contraction.one(&chain)),
                            rotated_contraction.one(&rotate_one(&chain))
                        );
                        one_checks += 1;
                    }
                }
            }
        }
        (zero_checks, one_checks)
    }

    fn rotation_orbit_audit() -> (usize, usize) {
        let mut seen = [false; 243];
        let mut orbits = 0;
        for pattern in patterns() {
            let code = pattern_code(pattern);
            if seen[code] {
                continue;
            }
            let first = rotate_pattern(pattern_u8(pattern));
            let second = rotate_pattern(first);
            let third = rotate_pattern(second);
            assert_eq!(third, pattern_u8(pattern));
            let orbit = [
                code,
                pattern_code(first.map(|entry| entry as usize)),
                pattern_code(second.map(|entry| entry as usize)),
            ];
            assert_eq!(orbit.iter().copied().collect::<BTreeSet<_>>().len(), 3);
            for member in orbit {
                seen[member] = true;
            }
            orbits += 1;
        }
        assert!(seen.into_iter().all(|entry| entry));
        // An invariant integral zero-chain has one coefficient on each orbit,
        // hence its augmentation is divisible by the orbit size.  Therefore
        // an invariant augmentation splitting (and thus an unpointed
        // equivariant cone) cannot exist over Z; averaging needs 1/3.
        (orbits, 3)
    }

    fn formal_contraction_identity_audit() -> usize {
        let mut checks = 0;
        for slot in 0..6 {
            let contraction = Contraction::for_slot(slot);
            for coordinate in 0..VERTICES {
                for (low, high) in [(0, 1), (0, 2), (1, 2)] {
                    for pattern in patterns() {
                        if pattern[coordinate] != 0 {
                            continue;
                        }
                        let edge = singleton_edge(EdgeCell {
                            coordinate: coordinate as u8,
                            low,
                            high,
                            environment: pattern_u8(pattern),
                        });
                        let mut left = contraction.one(&edge).boundary();
                        left.add_assign(&contraction.zero(&edge.boundary()));
                        assert_eq!(left, edge);
                        checks += 1;
                    }
                }
            }
        }
        checks
    }

    type GraphChain = [i8; 6];

    fn graph_endpoints(slot: usize) -> (usize, usize) {
        (slot % 2, 2 + slot / 2)
    }

    fn tree_path_chain(tree_mask: u8, start: usize, finish: usize) -> GraphChain {
        fn search(
            tree_mask: u8,
            vertex: usize,
            finish: usize,
            parent: usize,
            result: &mut GraphChain,
        ) -> bool {
            if vertex == finish {
                return true;
            }
            for slot in 0..6 {
                if tree_mask & (1 << slot) == 0 {
                    continue;
                }
                let (tail, head) = graph_endpoints(slot);
                let (next, sign) = if vertex == tail {
                    (head, 1)
                } else if vertex == head {
                    (tail, -1)
                } else {
                    continue;
                };
                if next == parent {
                    continue;
                }
                result[slot] = sign;
                if search(tree_mask, next, finish, vertex, result) {
                    return true;
                }
                result[slot] = 0;
            }
            false
        }

        let mut result = [0; 6];
        assert!(search(tree_mask, start, finish, usize::MAX, &mut result));
        result
    }

    fn fundamental_cycle(tree_mask: u8, chord: usize) -> GraphChain {
        assert_eq!(tree_mask & (1 << chord), 0);
        let (tail, head) = graph_endpoints(chord);
        let path = tree_path_chain(tree_mask, tail, head);
        let mut result = path.map(|coefficient| -coefficient);
        result[chord] += 1;
        result
    }

    fn cycle_coordinates(cycle: GraphChain) -> [i8; 2] {
        // With every edge oriented from a central vertex to a road vertex, a
        // cycle has odd-road coefficient minus its even-road coefficient and
        // is determined by a=(a_0,a_1,a_2), sum a_r=0.  The fixed global
        // basis is (1,-1,0), (1,0,-1).
        let a = [cycle[0], cycle[2], cycle[4]];
        for road in 0..3 {
            assert_eq!(cycle[2 * road + 1], -a[road]);
        }
        assert_eq!(a[0] + a[1] + a[2], 0);
        [-a[1], -a[2]]
    }

    fn determinant(first: [i8; 2], second: [i8; 2]) -> i8 {
        first[0] * second[1] - first[1] * second[0]
    }

    fn graph_basis_cycle(coordinates: [i8; 2]) -> GraphChain {
        let a = [
            coordinates[0] + coordinates[1],
            -coordinates[0],
            -coordinates[1],
        ];
        std::array::from_fn(|slot| {
            let road = slot / 2;
            if slot % 2 == 0 {
                a[road]
            } else {
                -a[road]
            }
        })
    }

    fn transform_graph_cycle(cycle: GraphChain, road_map: impl Fn(usize) -> usize) -> GraphChain {
        let mut result = [0; 6];
        for slot in 0..6 {
            let target = 2 * road_map(slot / 2) + slot % 2;
            result[target] = cycle[slot];
        }
        result
    }

    fn graph_symmetry_determinant(road_map: impl Copy + Fn(usize) -> usize) -> i8 {
        let first = cycle_coordinates(transform_graph_cycle(graph_basis_cycle([1, 0]), road_map));
        let second = cycle_coordinates(transform_graph_cycle(graph_basis_cycle([0, 1]), road_map));
        determinant(first, second)
    }

    fn determinant_line_audit() -> (usize, usize, i8, i8) {
        let mut positive = 0;
        let mut negative = 0;
        for tree_mask in spanning_tree_masks() {
            let chords: Vec<_> = (0..6).filter(|slot| tree_mask & (1 << slot) == 0).collect();
            let wedge = determinant(
                cycle_coordinates(fundamental_cycle(tree_mask, chords[0])),
                cycle_coordinates(fundamental_cycle(tree_mask, chords[1])),
            );
            assert_eq!(wedge.abs(), 1);
            if wedge == 1 {
                positive += 1;
            } else {
                negative += 1;
            }
        }
        let rotation = graph_symmetry_determinant(|road| (road + 1) % 3);
        let reflection = graph_symmetry_determinant(|road| (3 - road) % 3);
        assert_eq!(rotation, 1);
        assert_eq!(reflection, -1);
        (positive, negative, rotation, reflection)
    }

    #[derive(Clone, Copy, Debug, Eq, PartialEq)]
    enum TubeObstruction {
        Intersect,
        Adjacent,
    }

    #[derive(Clone, Copy, Debug, Eq, PartialEq)]
    struct RibbonStage {
        graph: u8,
        genus: i8,
        boundaries: i8,
    }

    #[derive(Clone, Copy, Debug, Eq, PartialEq)]
    enum RibbonMove {
        BoundarySplit,
        BoundaryJoin,
    }

    #[derive(Clone, Copy, Debug, Eq, PartialEq)]
    struct GraphAdditionDiagram {
        tree: u8,
        closures: [usize; 2],
        // Fibers are J(T union S) for S=empty,{e},{f},{e,f}.
        fibers: [RibbonStage; 4],
        order_paths: [[usize; 3]; 2],
        order_moves: [[RibbonMove; 2]; 2],
        obstruction: TubeObstruction,
    }

    impl GraphAdditionDiagram {
        fn new(tree: u8, closures: [usize; 2]) -> Self {
            let [first, second] = closures;
            let first_endpoints = graph_endpoints(first);
            let second_endpoints = graph_endpoints(second);
            let intersect = first_endpoints.0 == second_endpoints.0
                || first_endpoints.0 == second_endpoints.1
                || first_endpoints.1 == second_endpoints.0
                || first_endpoints.1 == second_endpoints.1;
            let graphs = [
                tree,
                tree | (1 << first),
                tree | (1 << second),
                tree | (1 << first) | (1 << second),
            ];
            Self {
                tree,
                closures,
                fibers: [
                    RibbonStage {
                        graph: graphs[0],
                        genus: 0,
                        boundaries: 1,
                    },
                    RibbonStage {
                        graph: graphs[1],
                        genus: 0,
                        boundaries: 2,
                    },
                    RibbonStage {
                        graph: graphs[2],
                        genus: 0,
                        boundaries: 2,
                    },
                    RibbonStage {
                        graph: graphs[3],
                        genus: 1,
                        boundaries: 1,
                    },
                ],
                order_paths: [[0, 1, 3], [0, 2, 3]],
                order_moves: [
                    [RibbonMove::BoundarySplit, RibbonMove::BoundaryJoin],
                    [RibbonMove::BoundarySplit, RibbonMove::BoundaryJoin],
                ],
                obstruction: if intersect {
                    TubeObstruction::Intersect
                } else {
                    TubeObstruction::Adjacent
                },
            }
        }

        fn audit(&self) {
            assert_eq!(self.fibers[0].graph, self.tree);
            assert_eq!(self.fibers[1].graph, self.tree | (1 << self.closures[0]));
            assert_eq!(self.fibers[2].graph, self.tree | (1 << self.closures[1]));
            assert_eq!(self.fibers[3].graph, 0b11_1111);
            assert_eq!(self.order_paths, [[0, 1, 3], [0, 2, 3]]);
            for stage in self.fibers {
                // Each connected ribbon graph retracts onto its thickening.
                let graph_euler = VERTICES as i8 - stage.graph.count_ones() as i8;
                let surface_euler = 2 - 2 * stage.genus - stage.boundaries;
                assert_eq!(graph_euler, surface_euler);
            }
            assert_eq!(self.order_moves[0], self.order_moves[1]);
        }
    }

    #[derive(Clone, Debug, Eq, PartialEq)]
    struct StagedTwoChain {
        // This types the origin-chain filler over the Grothendieck
        // construction (equivalently, the double mapping cylinder) of the
        // graph-addition square.  It is intentionally not a two-cell of the
        // final multiplihedron J(K2,3): the two missing-edge tubes are never
        // compatible there.
        graph_base: GraphAdditionDiagram,
        origin_filler: TwoChain,
    }

    #[derive(Default)]
    struct Counts {
        partial_presentations: usize,
        partial_boundary_failures: usize,
        maximum_partial_edges: usize,
        closure_presentations: usize,
        closure_boundary_failures: usize,
        nonzero_coherence_cycles: usize,
        coherence_fill_failures: usize,
        coherence_triangles: usize,
        coherence_squares: usize,
        nonzero_determinant_curvatures: usize,
        intersecting_tube_diagrams: usize,
        adjacent_tube_diagrams: usize,
        reference_transports: usize,
        reference_boundary_failures: usize,
        nonzero_reference_cycles: usize,
        reference_fill_failures: usize,
        minimum_a_exponent: i8,
    }

    pub fn run() {
        let contraction_identity_checks = formal_contraction_identity_audit();
        let (rotation_zero_checks, rotation_one_checks) = formal_rotation_audit();
        let (rotation_orbits, invariant_augmentation_gcd) = rotation_orbit_audit();
        let (positive_tree_wedges, negative_tree_wedges, rotation_det, reflection_det) =
            determinant_line_audit();
        let mut counts = Counts::default();
        let mut first_minimum = true;

        for tree_mask in spanning_tree_masks() {
            let closure_vec: Vec<_> = (0..6).filter(|slot| tree_mask & (1 << slot) == 0).collect();
            let closures = [closure_vec[0], closure_vec[1]];
            let momenta = [edge_momentum(closures[0]), edge_momentum(closures[1])];
            let gram = GramSpace::new(momenta[0], momenta[1]);
            let graph_diagram = GraphAdditionDiagram::new(tree_mask, closures);
            graph_diagram.audit();
            match graph_diagram.obstruction {
                TubeObstruction::Intersect => counts.intersecting_tube_diagrams += 1,
                TubeObstruction::Adjacent => counts.adjacent_tube_diagrams += 1,
            }

            // The 48 partial presentations: 12 trees x 2 references x 2
            // choices of first closure.
            for reference_shift in [1, 2] {
                for pair_index in 0..2 {
                    let residual =
                        partial_residual(tree_mask, closures, pair_index, reference_shift, &gram);
                    assert_eq!(augmentation(&residual), Polynomial::default());
                    let homotopy = Contraction::for_slot(closures[pair_index]).zero(&residual);
                    counts.partial_presentations += 1;
                    counts.maximum_partial_edges =
                        counts.maximum_partial_edges.max(homotopy.0.len());
                    if homotopy.boundary() != residual {
                        counts.partial_boundary_failures += 1;
                    }
                    let exponent = homotopy.minimum_a_exponent();
                    if first_minimum || exponent < counts.minimum_a_exponent {
                        counts.minimum_a_exponent = exponent;
                        first_minimum = false;
                    }
                }

                // The two closure-induced homotopies are made from the same
                // three nodes A -> B_e -> D, but use the edge-pointed cones
                // associated to their successive closures.
                let data = closure_data(tree_mask, closures, reference_shift, &gram);
                let final_residual = chain_difference(&data.physical, &data.graphical);
                assert_eq!(augmentation(&final_residual), Polynomial::default());
                let first_order = closure_homotopy(&data, closures, 0);
                let second_order = closure_homotopy(&data, closures, 1);
                counts.closure_presentations += 1;
                if first_order.boundary() != final_residual
                    || second_order.boundary() != final_residual
                {
                    counts.closure_boundary_failures += 1;
                }
                let mut cycle = first_order.clone();
                cycle.subtract_assign(&second_order);
                assert_eq!(cycle.boundary(), zero_chain());
                if cycle != OneChain::default() {
                    counts.nonzero_coherence_cycles += 1;
                    // The complement fundamental cycles are a unimodular
                    // basis, so tensoring this antisymmetric curvature with
                    // their wedge cannot make a nonzero integral cycle zero.
                    counts.nonzero_determinant_curvatures += 1;
                }
                let filler = StagedTwoChain {
                    graph_base: graph_diagram,
                    origin_filler: Contraction::for_slot(closures[0]).one(&cycle),
                };
                if filler.origin_filler.boundary() != cycle {
                    counts.coherence_fill_failures += 1;
                }
                let (triangles, squares) = filler.origin_filler.cell_counts();
                counts.coherence_triangles += triangles;
                counts.coherence_squares += squares;
                let exponent = filler.origin_filler.minimum_a_exponent();
                if first_minimum || exponent < counts.minimum_a_exponent {
                    counts.minimum_a_exponent = exponent;
                    first_minimum = false;
                }
            }

            // Null-reference covariance is a comparison of two different raw
            // origin chains.  Its admitted reference transport is the same
            // integral cone on their difference.  After subtracting that
            // transport, the residual one-cycle is filled explicitly.
            for pair_index in 0..2 {
                let first = partial_residual(tree_mask, closures, pair_index, 1, &gram);
                let second = partial_residual(tree_mask, closures, pair_index, 2, &gram);
                let contraction = Contraction::for_slot(closures[pair_index]);
                let first_homotopy = contraction.zero(&first);
                let second_homotopy = contraction.zero(&second);
                let difference = chain_difference(&second, &first);
                assert_eq!(augmentation(&difference), Polynomial::default());
                let transport = contraction.zero(&difference);
                counts.reference_transports += 1;
                if transport.boundary() != difference {
                    counts.reference_boundary_failures += 1;
                }
                let mut cycle = second_homotopy;
                cycle.subtract_assign(&first_homotopy);
                cycle.subtract_assign(&transport);
                assert_eq!(cycle.boundary(), zero_chain());
                if cycle != OneChain::default() {
                    counts.nonzero_reference_cycles += 1;
                }
                let filler = contraction.one(&cycle);
                if filler.boundary() != cycle {
                    counts.reference_fill_failures += 1;
                }
            }
        }

        println!("Formal origin-resolution/coherence audit");
        println!("========================================");
        println!(
            "  partial presentations:                 {}",
            counts.partial_presentations
        );
        println!(
            "  partial boundary failures:             {}",
            counts.partial_boundary_failures
        );
        println!(
            "  maximum occupied one-cells:            {}",
            counts.maximum_partial_edges
        );
        println!(
            "  tree/reference closure presentations:  {}",
            counts.closure_presentations
        );
        println!(
            "  closure-homotopy boundary failures:    {}",
            counts.closure_boundary_failures
        );
        println!(
            "  nonzero coherence one-cycles:          {}",
            counts.nonzero_coherence_cycles
        );
        println!(
            "  coherence two-chain failures:          {}",
            counts.coherence_fill_failures
        );
        println!(
            "  occupied coherence triangles:          {}",
            counts.coherence_triangles
        );
        println!(
            "  occupied coherence product squares:    {}",
            counts.coherence_squares
        );
        println!(
            "  nonzero det(H1)-valued curvatures:     {}",
            counts.nonzero_determinant_curvatures
        );
        println!(
            "  intersecting missing-tube diagrams:    {}",
            counts.intersecting_tube_diagrams
        );
        println!(
            "  adjacent missing-tube diagrams:        {}",
            counts.adjacent_tube_diagrams
        );
        println!("  ribbon stages in either order:         disk -> annulus -> punctured torus");
        println!("  modular/BV moves in either order:      boundary split -> boundary join");
        println!(
            "  null-reference transports:             {}",
            counts.reference_transports
        );
        println!(
            "  reference-transport boundary failures: {}",
            counts.reference_boundary_failures
        );
        println!(
            "  nonzero adjusted reference cycles:     {}",
            counts.nonzero_reference_cycles
        );
        println!(
            "  reference two-chain failures:          {}",
            counts.reference_fill_failures
        );
        println!("  degree-one contraction identities:     {contraction_identity_checks}");
        println!("  road-rotation degree-zero checks:      {rotation_zero_checks}");
        println!("  road-rotation degree-one checks:       {rotation_one_checks}");
        println!("  free road-rotation origin orbits:      {rotation_orbits}");
        println!("  invariant augmentation image:         {invariant_augmentation_gcd} Z");
        println!(
            "  complement-basis wedge signs (+/-):   {positive_tree_wedges}/{negative_tree_wedges}"
        );
        println!("  road-rotation action on det(H1):       {rotation_det}");
        println!("  road-reflection action on det(H1):     {reflection_det}");
        println!(
            "  minimum Laurent exponent of a:         {}",
            counts.minimum_a_exponent
        );
        println!("  integer coefficient denominators:      none");
        println!("  invariant unpointed symmetrization:    denominator 3 / Z/3 obstruction");

        assert_eq!(counts.partial_presentations, 48);
        assert_eq!(counts.partial_boundary_failures, 0);
        assert_eq!(counts.closure_presentations, 24);
        assert_eq!(counts.closure_boundary_failures, 0);
        assert_eq!(counts.coherence_fill_failures, 0);
        assert_eq!(counts.nonzero_determinant_curvatures, 24);
        assert_eq!(counts.intersecting_tube_diagrams, 6);
        assert_eq!(counts.adjacent_tube_diagrams, 6);
        assert_eq!(counts.reference_transports, 24);
        assert_eq!(counts.reference_boundary_failures, 0);
        assert_eq!(counts.reference_fill_failures, 0);

        println!();
        println!("VERDICT");
        println!("  every audited residual has an explicit integral nearest-neighbor filler");
        println!("  every two-order coherence cycle has an integral triangle/square filler");
        println!("  all 24 antisymmetric curvatures remain nonzero over det H1");
        println!("  road reflection reverses det H1; no zero is caused by forgetting it");
        println!("  fillers live over S -> J(T union S) in a double mapping cylinder");
        println!("  no filler is asserted to be a codimension-two cell of J(K2,3)");
        println!("  the edge-pointed family is exactly covariant under order-three rotation");
        println!("  null-reference changes are connected by an integral formal transport");
        println!("  covariance here is for formal cone operators, not Gram-chart coefficients");
        println!("  these are contractible-complex fillers, not realized Ward/V generators");
        println!("  a presentation-free rotation-invariant cone needs 1/3 and is not integral");
    }
}

fn main() {
    ward::run();
}
