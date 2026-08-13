//! Symbolic physical-projector identity for the marked theta handle.
//!
//! This removes the sampled-kinematics limitation of
//! check_marked_handle_x_dictionary.rs. The five cubic Yang--Mills tensors
//! are expanded into their three metric/handle sectors. Tensor-index
//! components are never sampled: every connected index strand is evaluated
//! symbolically as either a Gram product or a formal factor D.
//!
//! The on-shell three-point kinematic variety is represented by a free Laurent
//! polynomial ring in thirteen independent Gram coordinates plus D. For each
//! of the twelve spanning-tree sewing presentations we insert
//!
//!     -g + (l r + r l)/(l.r)
//!
//! on the two loop-closing edges, choosing cyclic null references with
//! l.r = A. The result is proved equal, coefficient by coefficient, to the
//! gauge-reduced contraction-cover polynomial with every closed circuit
//! assigned the resolved carrier D = nu - Delta.
//!
//! This ring is the physical Gram specialization of the freer surface curve
//! ring.  Distinct homotopy classes X_C can have the same Gram image; the
//! companion X-dictionary certificate keeps those classes independent.

use std::collections::{BTreeMap, BTreeSet};

type Int = i128;

const VERTICES: usize = 5;
const NODES: usize = 3 * VERTICES;
const PRIMITIVES: usize = 7;
const VARIABLES: usize = 14;

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

const VARIABLE_NAMES: [&str; VARIABLES] = [
    "A", "e0p0", "e0p1", "e0k1", "e1p0", "e1p1", "e1k0", "e2p0", "e2p1", "e2k0", "e0e1", "e0e2",
    "e1e2", "D",
];

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
        let mut terms = BTreeMap::new();
        if value != 0 {
            terms.insert(Monomial::ONE, value);
        }
        Self(terms)
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

    fn power(&self, exponent: u8) -> Self {
        (0..exponent).fold(Self::constant(1), |result, _| result.multiply(self))
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

    fn coefficient_content(&self) -> Int {
        fn gcd(mut a: Int, mut b: Int) -> Int {
            a = a.abs();
            b = b.abs();
            while b != 0 {
                (a, b) = (b, a % b);
            }
            a
        }
        self.0.values().copied().fold(0, gcd)
    }

    fn degree_range(&self) -> (i16, i16) {
        self.0
            .keys()
            .map(|monomial| monomial.0.iter().map(|&power| i16::from(power)).sum())
            .fold((i16::MAX, i16::MIN), |(minimum, maximum), degree| {
                (minimum.min(degree), maximum.max(degree))
            })
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

fn variable(index: usize, coefficient: Int) -> Polynomial {
    Polynomial::variable(index).scale(coefficient)
}

fn primitive_gram(first: usize, second: usize) -> Polynomial {
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
        pair => panic!("missing primitive Gram entry {pair:?}"),
    }
}

fn dot(first: Vector, second: Vector) -> Polynomial {
    let mut result = Polynomial::default();
    for left in 0..PRIMITIVES {
        for right in 0..PRIMITIVES {
            let coefficient = first.0[left] * second.0[right];
            if coefficient != 0 {
                result.add_assign(&primitive_gram(left, right).scale(coefficient));
            }
        }
    }
    result
}

fn rotate_vector(vector: Vector) -> Vector {
    // Simultaneous road rotation p_r,k_r,e_r -> p_{r+1},k_{r+1},e_{r+1}.
    let images = [p(1), p(2), k(1), k(2), epsilon(1), epsilon(2), epsilon(0)];
    vector
        .0
        .iter()
        .zip(images)
        .fold(Vector([0; PRIMITIVES]), |result, (&coefficient, image)| {
            result.plus(image.scale(coefficient))
        })
}

fn rotation_images() -> [Polynomial; VARIABLES] {
    let representatives = [
        (p(0), k(1)),
        (epsilon(0), p(0)),
        (epsilon(0), p(1)),
        (epsilon(0), k(1)),
        (epsilon(1), p(0)),
        (epsilon(1), p(1)),
        (epsilon(1), k(0)),
        (epsilon(2), p(0)),
        (epsilon(2), p(1)),
        (epsilon(2), k(0)),
        (epsilon(0), epsilon(1)),
        (epsilon(0), epsilon(2)),
        (epsilon(1), epsilon(2)),
    ];
    std::array::from_fn(|index| {
        if index == VAR_D {
            Polynomial::variable(VAR_D)
        } else {
            let (first, second) = representatives[index];
            dot(rotate_vector(first), rotate_vector(second))
        }
    })
}

fn substitute(polynomial: &Polynomial, images: &[Polynomial; VARIABLES]) -> Polynomial {
    let mut result = Polynomial::default();
    for (&monomial, &coefficient) in &polynomial.0 {
        let mut term = Polynomial::constant(coefficient);
        for (index, &exponent) in monomial.0.iter().enumerate() {
            assert!(exponent >= 0, "substitution received a Laurent monomial");
            term = term.multiply(&images[index].power(exponent as u8));
        }
        result.add_assign(&term);
    }
    result
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

#[derive(Clone, Copy, Debug)]
enum Sewing {
    Metric,
    LongitudinalForward,
    LongitudinalReverse,
}

fn evaluate_sector(
    pattern: [usize; VERTICES],
    sewings: [Sewing; 6],
    reduced: bool,
    reference_shift: usize,
) -> Polynomial {
    let mut sets = DisjointSet::new();
    let mut terminals = Vec::<(usize, Vector)>::new();
    let mut coefficient: Int = 1;
    let mut inverse_a_power = 0;

    for vertex in 0..VERTICES {
        let singleton = pattern[vertex];
        let first_paired = (singleton + 1) % 3;
        let second_paired = (singleton + 2) % 3;
        sets.join(3 * vertex + first_paired, 3 * vertex + second_paired);
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

    for (slot, sewing) in sewings.into_iter().enumerate() {
        let (first, second) = edge_endpoints(slot);
        match sewing {
            Sewing::Metric => {
                sets.join(first, second);
                coefficient = -coefficient;
            }
            Sewing::LongitudinalForward | Sewing::LongitudinalReverse => {
                let momentum = edge_momentum(slot);
                let reference = edge_reference(slot, reference_shift);
                let denominator = dot(momentum, reference);
                let denominator_sign = if denominator == Polynomial::variable(VAR_A) {
                    1
                } else {
                    assert_eq!(denominator, Polynomial::variable(VAR_A).scale(-1));
                    -1
                };
                coefficient *= denominator_sign;
                let (left, right) = match sewing {
                    Sewing::LongitudinalForward => (momentum, reference),
                    Sewing::LongitudinalReverse => (reference, momentum),
                    Sewing::Metric => unreachable!(),
                };
                terminals.push((first, left));
                terminals.push((second, right));
                inverse_a_power += 1;
            }
        }
    }

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
                result = result.multiply(&dot(vectors[0], vectors[1]));
            }
            count => panic!("index strand has {count} terminals"),
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

fn graphical_polynomial() -> Polynomial {
    let mut result = Polynomial::default();
    for pattern in patterns() {
        result.add_assign(&evaluate_sector(pattern, [Sewing::Metric; 6], true, 1));
    }
    result
}

fn naive_metric_polynomial() -> Polynomial {
    let mut result = Polynomial::default();
    for pattern in patterns() {
        result.add_assign(&evaluate_sector(pattern, [Sewing::Metric; 6], false, 1));
    }
    result
}

fn physical_polynomial(tree_mask: u8, reference_shift: usize) -> Polynomial {
    let closures: Vec<_> = (0..6).filter(|slot| tree_mask & (1 << slot) == 0).collect();
    assert_eq!(closures.len(), 2);
    let mut result = Polynomial::default();
    for choices in 0..9 {
        let mut code = choices;
        let mut sewings = [Sewing::Metric; 6];
        for &slot in &closures {
            sewings[slot] = match code % 3 {
                0 => Sewing::Metric,
                1 => Sewing::LongitudinalForward,
                2 => Sewing::LongitudinalReverse,
                _ => unreachable!(),
            };
            code /= 3;
        }
        for pattern in patterns() {
            result.add_assign(&evaluate_sector(pattern, sewings, false, reference_shift));
        }
    }
    result
}

fn format_monomial(monomial: Monomial) -> String {
    let factors: Vec<_> = monomial
        .0
        .iter()
        .enumerate()
        .filter_map(|(index, &power)| {
            if power == 0 {
                None
            } else if power == 1 {
                Some(VARIABLE_NAMES[index].to_string())
            } else {
                Some(format!("{}^{power}", VARIABLE_NAMES[index]))
            }
        })
        .collect();
    if factors.is_empty() {
        "1".to_string()
    } else {
        factors.join("*")
    }
}

fn polynomial_preview(polynomial: &Polynomial, limit: usize) -> String {
    polynomial
        .0
        .iter()
        .take(limit)
        .map(|(&monomial, &coefficient)| format!("{coefficient:+} {}", format_monomial(monomial)))
        .collect::<Vec<_>>()
        .join("\n    ")
}

fn audit_endpoint_polarization_identity() {
    let mut left = BTreeMap::<(usize, usize), Int>::new();
    let mut right = BTreeMap::<(usize, usize), Int>::new();
    let pair = |x: usize, y: usize| if x <= y { (x, y) } else { (y, x) };
    let add_square = |target: &mut BTreeMap<(usize, usize), Int>, x: usize, y: usize, sign: Int| {
        *target.entry(pair(x, x)).or_default() += sign;
        *target.entry(pair(y, y)).or_default() += sign;
        *target.entry(pair(x, y)).or_default() -= 2 * sign;
    };
    add_square(&mut left, 1, 3, 1);
    add_square(&mut left, 0, 2, 1);
    add_square(&mut left, 1, 2, -1);
    add_square(&mut left, 0, 3, -1);
    for (x, x_sign) in [(1, 1), (0, -1)] {
        for (y, y_sign) in [(2, 1), (3, -1)] {
            *right.entry(pair(x, y)).or_default() += 2 * x_sign * y_sign;
        }
    }
    left.retain(|_, coefficient| *coefficient != 0);
    right.retain(|_, coefficient| *coefficient != 0);
    assert_eq!(left, right);
}

fn main() {
    audit_endpoint_polarization_identity();

    let graphical = graphical_polynomial();
    let naive = naive_metric_polynomial();
    assert_ne!(naive, graphical);
    assert!(graphical.minimum_exponent(VAR_A) >= 0);

    let trees = spanning_tree_masks();
    let mut physical_sizes = BTreeMap::new();
    for reference_shift in [1, 2] {
        for &tree in &trees {
            let physical = physical_polynomial(tree, reference_shift);
            assert_eq!(
                physical, graphical,
                "symbolic physical/graphical mismatch for tree {tree:06b}, reference shift {reference_shift}"
            );
            assert!(physical.minimum_exponent(VAR_A) >= 0);
            physical_sizes.insert((reference_shift, tree), physical.0.len());
        }
    }

    let correction = graphical.clone().add(&naive.clone().scale(-1));
    assert!(!correction.0.is_empty());

    let rotation = rotation_images();
    assert_eq!(substitute(&graphical, &rotation), graphical);
    assert_eq!(substitute(&naive, &rotation), naive);
    let rotated_twice: [Polynomial; VARIABLES] =
        std::array::from_fn(|index| substitute(&rotation[index], &rotation));
    let rotated_thrice: [Polynomial; VARIABLES] =
        std::array::from_fn(|index| substitute(&rotated_twice[index], &rotation));
    for index in 0..VARIABLES {
        assert_eq!(rotated_thrice[index], Polynomial::variable(index));
    }

    println!("Marked-handle symbolic identity certificate");
    println!("===========================================");
    println!("  independent Gram variables (including A): 13");
    println!("  formal state-trace variable: D");
    println!("  local sector words: {}", patterns().len());
    println!(
        "  spanning-tree/reference presentations: {}",
        2 * trees.len()
    );
    println!("  physical projector terms per sector/tree: 9");
    println!("  graphical polynomial monomials: {}", graphical.0.len());
    println!("  naive metric polynomial monomials: {}", naive.0.len());
    println!(
        "  longitudinal correction monomials: {}",
        correction.0.len()
    );
    println!(
        "  graphical coefficient content: {}",
        graphical.coefficient_content()
    );
    println!("  graphical degree range: {:?}", graphical.degree_range());
    println!(
        "  minimum A exponent after cancellation: {}",
        graphical.minimum_exponent(VAR_A)
    );
    println!("  physical monomial counts by (reference,tree): {physical_sizes:?}");
    println!("  exact cyclic road covariance: rho(P)=P and rho^3=1");
    println!("  symbolic level: physical Gram specialization of the free surface curve ring");
    println!("  first graphical terms:");
    println!("    {}", polynomial_preview(&graphical, 8));
    println!();
    println!("VERDICT");
    println!("  the four-extension identity holds in the free endpoint Gram ring");
    println!("  every physical-projector denominator cancels symbolically");
    println!("  all 24 sewing-tree/reference choices give one polynomial over Z[Gram,D]");
    println!("  the symbolic polynomial is covariant under the order-three handle rotation");
    println!("  it is the physical specialization of the resolved contraction-cover polynomial");
    println!("  the naive all-metric network differs by a nonzero symbolic correction");
}
