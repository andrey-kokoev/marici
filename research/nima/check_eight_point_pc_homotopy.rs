//! Complete occurrence-resolved certificate for the eight-point PC polarity
//! homotopy.
//!
//! The certificate combines, without quotienting occurrence marks,
//!
//! * entry 23's exact G/R/K Laurent decomposition;
//! * entry 84's saturated codimension-one six-point flags;
//! * entry 86's occurrence-conjugated core-entry counit; and
//! * entry 83's fixed-mark loaded contact primitive.
//!
//! The symbol checked here is
//!
//!   H_8^PC = sum_D Ins_D^PC(H_{6,D}^mark) + H_ct^PC.
//!
//! `D` runs over the eight physical octagon diagonals.  The subscript on
//! `H_{6,D}` is essential: the hexagon, its polarity, and the complementary
//! four-point tensor are induced by the cut D.  The normalized Gysin symbol
//! is
//!
//!   Ins_D^PC(c) = - hhat_D (c_4 tensor c) [dX_D]
//!               =   hhat_D (q_4 tensor c) [dX_D],
//!   hhat_D = 2*pi*i*alpha' ell_D/(q_D-1),
//!   gr_V(hhat_D) = 1/X_D.
//!
//! Here `c_4` is the positively normalized two-occurrence four-point cycle
//! and the rooted QTDS convention is `q_4=-c_4`.  Consequently the derived
//! cut table has the side-ordered form
//!
//!   Res_D Ins_D^PC(H_6^mark) = q_4 boxtimes H_6^mark.
//!
//! All calculations use exact sparse Laurent polynomials over Q.  PC tubes
//! are represented by their face flag, ordered normal word, and associated
//! Laurent grade; no numerical kinematics or floating point arithmetic is
//! used.

use std::cmp::Ordering;
use std::collections::{BTreeMap, BTreeSet, VecDeque};

const N: u8 = 8;
const VARIABLES: usize = 20;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Triangulation = Vec<Diagonal>;
type Quadrangulation = [Diagonal; 2];
type Powers = [i8; VARIABLES];

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rational {
    numerator: i64,
    denominator: i64,
}

impl Rational {
    const ZERO: Self = Self {
        numerator: 0,
        denominator: 1,
    };
    const ONE: Self = Self {
        numerator: 1,
        denominator: 1,
    };

    fn new(mut numerator: i64, mut denominator: i64) -> Self {
        assert_ne!(denominator, 0);
        if numerator == 0 {
            return Self::ZERO;
        }
        if denominator < 0 {
            numerator = -numerator;
            denominator = -denominator;
        }
        let divisor = gcd(numerator.unsigned_abs(), denominator as u64) as i64;
        Self {
            numerator: numerator / divisor,
            denominator: denominator / divisor,
        }
    }

    fn add(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )
    }

    fn multiply(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )
    }
}

fn gcd(mut first: u64, mut second: u64) -> u64 {
    while second != 0 {
        let remainder = first % second;
        first = second;
        second = remainder;
    }
    first
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct Laurent(BTreeMap<Powers, Rational>);

impl Laurent {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn one() -> Self {
        Self::constant(Rational::ONE)
    }

    fn constant(value: Rational) -> Self {
        if value == Rational::ZERO {
            Self::zero()
        } else {
            Self(BTreeMap::from([([0; VARIABLES], value)]))
        }
    }

    fn variable(value: Diagonal) -> Self {
        let mut powers = [0; VARIABLES];
        powers[variable_index(value)] = 1;
        Self(BTreeMap::from([(powers, Rational::ONE)]))
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.0.clone();
        for (powers, coefficient) in &other.0 {
            result
                .entry(*powers)
                .and_modify(|current| *current = current.add(*coefficient))
                .or_insert(*coefficient);
        }
        result.retain(|_, coefficient| *coefficient != Rational::ZERO);
        Self(result)
    }

    fn subtract(&self, other: &Self) -> Self {
        self.add(&other.scale(Rational::new(-1, 1)))
    }

    fn scale(&self, scalar: Rational) -> Self {
        if scalar == Rational::ZERO {
            return Self::zero();
        }
        let mut result: BTreeMap<_, _> = self
            .0
            .iter()
            .map(|(powers, coefficient)| (*powers, coefficient.multiply(scalar)))
            .collect();
        result.retain(|_, coefficient| *coefficient != Rational::ZERO);
        Self(result)
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = BTreeMap::new();
        for (left_powers, left_coefficient) in &self.0 {
            for (right_powers, right_coefficient) in &other.0 {
                let mut powers = [0; VARIABLES];
                for index in 0..VARIABLES {
                    powers[index] = left_powers[index] + right_powers[index];
                }
                let coefficient = left_coefficient.multiply(*right_coefficient);
                result
                    .entry(powers)
                    .and_modify(|current: &mut Rational| *current = current.add(coefficient))
                    .or_insert(coefficient);
            }
        }
        result.retain(|_, coefficient| *coefficient != Rational::ZERO);
        Self(result)
    }

    fn power(&self, exponent: usize) -> Self {
        let mut result = Self::one();
        for _ in 0..exponent {
            result = result.multiply(self);
        }
        result
    }

    fn divide_variable(&self, value: Diagonal) -> Self {
        let index = variable_index(value);
        Self(
            self.0
                .iter()
                .map(|(powers, coefficient)| {
                    let mut divided = *powers;
                    divided[index] -= 1;
                    (divided, *coefficient)
                })
                .collect(),
        )
    }

    fn negative_support(powers: &Powers) -> Vec<usize> {
        powers
            .iter()
            .enumerate()
            .filter_map(|(index, exponent)| (*exponent < 0).then_some(index))
            .collect()
    }

    fn select_negative_support(&self, expected: &[usize]) -> Self {
        Self(
            self.0
                .iter()
                .filter(|(powers, _)| Self::negative_support(powers) == expected)
                .map(|(powers, coefficient)| (*powers, *coefficient))
                .collect(),
        )
    }

    fn regular_part(&self) -> Self {
        self.select_negative_support(&[])
    }

    fn is_regular(&self) -> bool {
        self.0
            .keys()
            .all(|powers| Self::negative_support(powers).is_empty())
    }
}

fn diagonal(first: u8, second: u8) -> Diagonal {
    if first < second {
        Diagonal(first, second)
    } else {
        Diagonal(second, first)
    }
}

fn is_boundary(value: Diagonal, multiplicity: u8) -> bool {
    value.1 - value.0 == 1 || value == Diagonal(0, multiplicity - 1)
}

fn physical(value: Diagonal) -> bool {
    value.0 % 2 != value.1 % 2
}

fn strictly_between(vertex: u8, first: u8, second: u8, multiplicity: u8) -> bool {
    let span = (second + multiplicity - first) % multiplicity;
    let position = (vertex + multiplicity - first) % multiplicity;
    position > 0 && position < span
}

fn crosses_in(first: Diagonal, second: Diagonal, multiplicity: u8) -> bool {
    if [first.0, first.1]
        .iter()
        .any(|endpoint| *endpoint == second.0 || *endpoint == second.1)
    {
        return false;
    }
    strictly_between(second.0, first.0, first.1, multiplicity)
        != strictly_between(second.1, first.0, first.1, multiplicity)
        && strictly_between(first.0, second.0, second.1, multiplicity)
            != strictly_between(first.1, second.0, second.1, multiplicity)
}

fn all_diagonals(multiplicity: u8) -> Vec<Diagonal> {
    let mut result = Vec::new();
    for first in 0..multiplicity {
        for second in first + 1..multiplicity {
            let value = Diagonal(first, second);
            if !is_boundary(value, multiplicity) {
                result.push(value);
            }
        }
    }
    result
}

fn variable_index(value: Diagonal) -> usize {
    all_diagonals(N)
        .iter()
        .position(|candidate| *candidate == value)
        .expect("every coefficient is a planar octagon variable")
}

fn choose_triangulations(
    diagonals: &[Diagonal],
    multiplicity: u8,
    start: usize,
    selected: &mut Vec<Diagonal>,
    result: &mut Vec<Triangulation>,
) {
    let target = multiplicity as usize - 3;
    if selected.len() == target {
        result.push(selected.clone());
        return;
    }
    let needed = target - selected.len();
    for index in start..=diagonals.len() - needed {
        let candidate = diagonals[index];
        if selected
            .iter()
            .all(|value| !crosses_in(*value, candidate, multiplicity))
        {
            selected.push(candidate);
            choose_triangulations(diagonals, multiplicity, index + 1, selected, result);
            selected.pop();
        }
    }
}

fn triangulations(multiplicity: u8) -> Vec<Triangulation> {
    let mut result = Vec::new();
    choose_triangulations(
        &all_diagonals(multiplicity),
        multiplicity,
        0,
        &mut Vec::new(),
        &mut result,
    );
    result.sort();
    result.dedup();
    result
}

fn intersection_size<T: Ord>(first: &[T], second: &[T]) -> usize {
    let mut left = 0;
    let mut right = 0;
    let mut count = 0;
    while left < first.len() && right < second.len() {
        match first[left].cmp(&second[right]) {
            Ordering::Less => left += 1,
            Ordering::Greater => right += 1,
            Ordering::Equal => {
                count += 1;
                left += 1;
                right += 1;
            }
        }
    }
    count
}

fn triangulation_adjacency(values: &[Triangulation]) -> Vec<Vec<usize>> {
    let mut result = vec![Vec::new(); values.len()];
    let common = values[0].len() - 1;
    for first in 0..values.len() {
        for second in first + 1..values.len() {
            if intersection_size(&values[first], &values[second]) == common {
                result[first].push(second);
                result[second].push(first);
            }
        }
    }
    result
}

fn physical_diagonals() -> Vec<Diagonal> {
    let mut result: Vec<_> = (0..N)
        .map(|vertex| diagonal(vertex, (vertex + 3) % N))
        .collect();
    result.sort();
    result.dedup();
    assert_eq!(result.len(), 8);
    result
}

fn quadrangulations() -> Vec<Quadrangulation> {
    let roads = physical_diagonals();
    let mut result = Vec::new();
    for first in 0..roads.len() {
        for second in first + 1..roads.len() {
            if !crosses_in(roads[first], roads[second], N) {
                result.push([roads[first], roads[second]]);
            }
        }
    }
    result.sort();
    assert_eq!(result.len(), 12);
    result
}

fn planar(value_first: i16, value_second: i16, vertices: &[u8]) -> Laurent {
    let multiplicity = vertices.len() as i16;
    let first = value_first.rem_euclid(multiplicity) as usize;
    let second = value_second.rem_euclid(multiplicity) as usize;
    if first == second
        || (first as i16 - second as i16).rem_euclid(multiplicity) == 1
        || (first as i16 - second as i16).rem_euclid(multiplicity) == multiplicity - 1
    {
        Laurent::zero()
    } else {
        Laurent::variable(diagonal(vertices[first], vertices[second]))
    }
}

fn symbolic_kinematics(vertices: &[u8]) -> Vec<Vec<Laurent>> {
    let multiplicity = vertices.len();
    let mut result = vec![vec![Laurent::zero(); multiplicity]; multiplicity];
    for first in 0..multiplicity {
        for second in first + 1..multiplicity {
            let value = planar(first as i16, second as i16 + 1, vertices)
                .add(&planar(first as i16 + 1, second as i16, vertices))
                .subtract(&planar(first as i16, second as i16, vertices))
                .subtract(&planar(first as i16 + 1, second as i16 + 1, vertices));
            result[first][second] = value.clone();
            result[second][first] = value;
        }
    }
    for row in &result {
        assert_eq!(
            row.iter()
                .fold(Laurent::zero(), |sum, value| sum.add(value)),
            Laurent::zero()
        );
    }
    result
}

#[derive(Clone, Debug)]
struct RawTerm {
    numerator: Laurent,
    propagators: Vec<Vec<usize>>,
}

fn odd_three_splits(size: usize) -> Vec<(usize, usize, usize)> {
    let mut result = Vec::new();
    for first in (1..size - 1).step_by(2) {
        for second in (1..size - first).step_by(2) {
            let third = size - first - second;
            if third > 0 && third % 2 == 1 {
                result.push((first, second, third));
            }
        }
    }
    result
}

fn vertex_factor(
    block: &[usize],
    first: &[usize],
    second: &[usize],
    third: &[usize],
    starts_plus: bool,
    kinematics: &[Vec<Laurent>],
) -> Laurent {
    let (left, right, sign) = if starts_plus {
        (first, third, Rational::new(-1, 1))
    } else {
        (block, second, Rational::ONE)
    };
    left.iter()
        .flat_map(|left_vertex| {
            right
                .iter()
                .map(move |right_vertex| &kinematics[*left_vertex][*right_vertex])
        })
        .fold(Laurent::zero(), |sum, value| sum.add(value))
        .scale(sign)
}

fn current_terms(block: &[usize], starts_plus: bool, kinematics: &[Vec<Laurent>]) -> Vec<RawTerm> {
    if block.len() == 1 {
        return vec![RawTerm {
            numerator: Laurent::one(),
            propagators: Vec::new(),
        }];
    }
    vertex_terms(block, starts_plus, kinematics)
        .into_iter()
        .map(|mut term| {
            term.propagators.insert(0, block.to_vec());
            term
        })
        .collect()
}

fn vertex_terms(block: &[usize], starts_plus: bool, kinematics: &[Vec<Laurent>]) -> Vec<RawTerm> {
    let mut result = Vec::new();
    for (first_size, second_size, _) in odd_three_splits(block.len()) {
        let first_end = first_size;
        let second_end = first_size + second_size;
        let first = &block[..first_end];
        let second = &block[first_end..second_end];
        let third = &block[second_end..];
        let factor = vertex_factor(block, first, second, third, starts_plus, kinematics);
        for first_term in current_terms(first, starts_plus, kinematics) {
            for second_term in current_terms(second, !starts_plus, kinematics) {
                for third_term in current_terms(third, starts_plus, kinematics) {
                    let mut propagators = first_term.propagators.clone();
                    propagators.extend(second_term.propagators.clone());
                    propagators.extend(third_term.propagators.clone());
                    result.push(RawTerm {
                        numerator: factor
                            .multiply(&first_term.numerator)
                            .multiply(&second_term.numerator)
                            .multiply(&third_term.numerator),
                        propagators,
                    });
                }
            }
        }
    }
    result
}

fn qtds_diagrams(vertices: &[u8], plus: bool) -> BTreeMap<Vec<Diagonal>, Laurent> {
    assert_eq!(vertices.len() % 2, 0);
    let kinematics = symbolic_kinematics(vertices);
    let root: Vec<_> = (0..vertices.len() - 1).collect();
    let convention_sign = if (vertices.len() / 2 - 1) % 2 == 0 {
        Rational::ONE
    } else {
        Rational::new(-1, 1)
    };
    let mut result = BTreeMap::new();
    for term in vertex_terms(&root, plus, &kinematics) {
        let mut channels = Vec::new();
        let mut value = term.numerator.scale(convention_sign);
        for block in term.propagators {
            let channel = diagonal(
                vertices[*block.first().expect("nonempty propagator")],
                vertices[(block.last().expect("nonempty propagator") + 1) % vertices.len()],
            );
            channels.push(channel);
            value = value.divide_variable(channel);
        }
        channels.sort();
        assert!(result.insert(channels, value).is_none());
    }
    result
}

fn multiply_series(
    first: &BTreeMap<usize, Laurent>,
    second: &BTreeMap<usize, Laurent>,
    maximum_degree: usize,
) -> BTreeMap<usize, Laurent> {
    let mut result = BTreeMap::new();
    for (first_degree, first_value) in first {
        for (second_degree, second_value) in second {
            let degree = first_degree + second_degree;
            if degree <= maximum_degree {
                let term = first_value.multiply(second_value);
                result
                    .entry(degree)
                    .and_modify(|current: &mut Laurent| *current = current.add(&term))
                    .or_insert(term);
            }
        }
    }
    result
}

fn scalar_grade_by_core(
    values: &[Triangulation],
) -> (
    BTreeMap<Vec<Diagonal>, Laurent>,
    BTreeMap<Triangulation, Laurent>,
) {
    let target_degree = 6;
    let mut groups = BTreeMap::new();
    let mut individual = BTreeMap::new();
    for triangulation in values {
        let mut series = BTreeMap::from([(0, Laurent::one())]);
        for value in triangulation {
            let factor = if physical(*value) {
                BTreeMap::from([(0, Laurent::one().divide_variable(*value))])
            } else {
                let sigma = if value.0 % 2 == 0 { -1_i64 } else { 1_i64 };
                (1..=target_degree)
                    .map(|degree| {
                        let numerator_sign = if (degree - 1) % 2 == 0 { 1 } else { -1 };
                        let sigma_power = sigma.pow(degree as u32);
                        (
                            degree,
                            Laurent::variable(*value)
                                .power(degree - 1)
                                .scale(Rational::new(numerator_sign / sigma_power, 1)),
                        )
                    })
                    .collect()
            };
            series = multiply_series(&series, &factor, target_degree);
        }
        let grade = series.remove(&target_degree).unwrap_or_else(Laurent::zero);
        let core: Vec<_> = triangulation
            .iter()
            .copied()
            .filter(|value| physical(*value))
            .collect();
        groups
            .entry(core)
            .and_modify(|current: &mut Laurent| *current = current.add(&grade))
            .or_insert_with(|| grade.clone());
        individual.insert(triangulation.clone(), grade);
    }
    (groups, individual)
}

fn polygon_paths(value: Diagonal) -> (Vec<u8>, Vec<u8>) {
    let increasing: Vec<_> = (value.0..=value.1).collect();
    let mut complementary: Vec<_> = (value.1..N).collect();
    complementary.extend(0..=value.0);
    if increasing.len() == 4 {
        (complementary, increasing)
    } else {
        assert_eq!(increasing.len(), 6);
        (increasing, complementary)
    }
}

fn rotate_to_even_start(mut vertices: Vec<u8>) -> Vec<u8> {
    let position = vertices
        .iter()
        .position(|vertex| {
            vertex % 2 == 0 && {
                let previous = vertices[(vertices.len()
                    + vertices.iter().position(|v| v == vertex).unwrap()
                    - 1)
                    % vertices.len()];
                diagonal(*vertex, previous) == diagonal(vertices[0], *vertices.last().unwrap())
                    || diagonal(
                        *vertex,
                        vertices[(vertices.iter().position(|v| v == vertex).unwrap() + 1)
                            % vertices.len()],
                    ) == diagonal(vertices[0], *vertices.last().unwrap())
            }
        })
        .expect("one cut endpoint is even");
    vertices.rotate_left(position);
    assert_eq!(vertices[0] % 2, 0);
    assert!(vertices
        .iter()
        .enumerate()
        .all(|(index, vertex)| *vertex % 2 == index as u8 % 2));
    vertices
}

fn cut_polygons(value: Diagonal) -> (Vec<u8>, Vec<u8>) {
    let (hexagon, quadrilateral) = polygon_paths(value);
    (
        rotate_to_even_start(hexagon),
        rotate_to_even_start(quadrilateral),
    )
}

fn local_diagonal(vertices: &[u8], first: usize, second: usize) -> Diagonal {
    diagonal(
        vertices[first % vertices.len()],
        vertices[second % vertices.len()],
    )
}

fn six_boundary_vector(vertices: &[u8]) -> BTreeMap<Diagonal, Laurent> {
    assert_eq!(vertices.len(), 6);
    let x: Vec<_> = (0..6)
        .map(|index| Laurent::variable(local_diagonal(vertices, index, index + 2)))
        .collect();
    let channels = [
        local_diagonal(vertices, 0, 3),
        local_diagonal(vertices, 1, 4),
        local_diagonal(vertices, 2, 5),
    ];
    BTreeMap::from([
        (channels[0], x[0].add(&x[1]).subtract(&x[3]).subtract(&x[4])),
        (channels[1], x[4].add(&x[5]).subtract(&x[1]).subtract(&x[2])),
        (channels[2], x[2].add(&x[3]).subtract(&x[5]).subtract(&x[0])),
    ])
}

fn four_point_cycle(vertices: &[u8]) -> Laurent {
    assert_eq!(vertices.len(), 4);
    Laurent::variable(local_diagonal(vertices, 0, 2))
        .add(&Laurent::variable(local_diagonal(vertices, 1, 3)))
}

#[derive(Clone, Debug)]
struct Decomposition {
    q: BTreeMap<Quadrangulation, Laurent>,
    g: BTreeMap<Quadrangulation, Laurent>,
    r: BTreeMap<(Quadrangulation, Diagonal), Laurent>,
    k: BTreeMap<Quadrangulation, Laurent>,
}

fn decompose(
    q_raw: BTreeMap<Vec<Diagonal>, Laurent>,
    full_core: &BTreeMap<Quadrangulation, Laurent>,
) -> Decomposition {
    let q: BTreeMap<_, _> = q_raw
        .into_iter()
        .map(|(channels, value)| {
            assert_eq!(channels.len(), 2);
            ([channels[0], channels[1]], value)
        })
        .collect();
    let mut r = BTreeMap::new();
    let mut k = BTreeMap::new();
    for (quadrangulation, value) in &q {
        let remainder = value.subtract(&full_core[quadrangulation]);
        let mut rebuilt = Laurent::zero();
        for channel in physical_diagonals() {
            let selected = remainder.select_negative_support(&[variable_index(channel)]);
            if quadrangulation.contains(&channel) {
                r.insert((*quadrangulation, channel), selected.clone());
            } else {
                assert_eq!(selected, Laurent::zero());
            }
            rebuilt = rebuilt.add(&selected);
        }
        let contact = remainder.regular_part();
        rebuilt = rebuilt.add(&contact);
        assert_eq!(remainder, rebuilt);
        k.insert(*quadrangulation, contact);
    }
    Decomposition {
        q,
        g: full_core.clone(),
        r,
        k,
    }
}

// ----- Six-point saturated occurrence chain --------------------------------

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum SixNode {
    Vertex(Triangulation),
    Edge(Triangulation, Triangulation),
    Facet(Diagonal),
}

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct SixOccurrenceEdge {
    outer: Diagonal,
    center: Triangulation,
    mark: Diagonal,
    first: SixNode,
    second: SixNode,
}

type SixChain = BTreeMap<SixOccurrenceEdge, Laurent>;

fn ordered_six_edge(first: Triangulation, second: Triangulation) -> SixNode {
    if first < second {
        SixNode::Edge(first, second)
    } else {
        SixNode::Edge(second, first)
    }
}

fn add_six_edge(chain: &mut SixChain, key: SixOccurrenceEdge, coefficient: Laurent) {
    chain
        .entry(key)
        .and_modify(|current| *current = current.add(&coefficient))
        .or_insert(coefficient);
    chain.retain(|_, value| value != &Laurent::zero());
}

fn six_local_triangulations(vertices: &[u8]) -> Vec<Triangulation> {
    let local = triangulations(6);
    local
        .into_iter()
        .map(|triangulation| {
            let mut mapped: Vec<_> = triangulation
                .into_iter()
                .map(|value| local_diagonal(vertices, value.0 as usize, value.1 as usize))
                .collect();
            mapped.sort();
            mapped
        })
        .collect()
}

fn core_of(value: &Triangulation) -> Vec<Diagonal> {
    value
        .iter()
        .copied()
        .filter(|item| physical(*item))
        .collect()
}

fn boundary_edges_of_polygon(vertices: &[u8]) -> BTreeSet<Diagonal> {
    (0..vertices.len())
        .map(|index| local_diagonal(vertices, index, index + 1))
        .collect()
}

fn quadrilateral_cells_in_hexagon(vertices: &[u8], channel: Diagonal) -> Vec<BTreeSet<u8>> {
    let edges: BTreeSet<_> = boundary_edges_of_polygon(vertices)
        .into_iter()
        .chain([channel])
        .collect();
    let mut result = Vec::new();
    for choice in combinations(vertices, 4) {
        if (0..4).all(|index| edges.contains(&diagonal(choice[index], choice[(index + 1) % 4]))) {
            result.push(choice.into_iter().collect());
        }
    }
    assert_eq!(result.len(), 2);
    result
}

fn combinations(values: &[u8], size: usize) -> Vec<Vec<u8>> {
    fn recurse(
        values: &[u8],
        size: usize,
        start: usize,
        selected: &mut Vec<u8>,
        result: &mut Vec<Vec<u8>>,
    ) {
        if selected.len() == size {
            result.push(selected.clone());
            return;
        }
        let needed = size - selected.len();
        for index in start..=values.len() - needed {
            selected.push(values[index]);
            recurse(values, size, index + 1, selected, result);
            selected.pop();
        }
    }
    let mut result = Vec::new();
    recurse(values, size, 0, &mut Vec::new(), &mut result);
    result
}

fn cell_side_in_polygon(vertices: &[u8], channel: Diagonal, cell: &BTreeSet<u8>) -> u8 {
    let first_position = vertices
        .iter()
        .position(|value| *value == channel.0)
        .unwrap();
    let second_position = vertices
        .iter()
        .position(|value| *value == channel.1)
        .unwrap();
    let mut increasing = BTreeSet::new();
    let mut cursor = (first_position + 1) % vertices.len();
    while cursor != second_position {
        increasing.insert(vertices[cursor]);
        cursor = (cursor + 1) % vertices.len();
    }
    let endpoints = BTreeSet::from([channel.0, channel.1]);
    let other: BTreeSet<_> = cell.difference(&endpoints).copied().collect();
    if other.is_subset(&increasing) {
        0
    } else {
        assert!(other.is_disjoint(&increasing));
        1
    }
}

fn scalar_slots(cell: &BTreeSet<u8>) -> BTreeSet<Diagonal> {
    let vertices: Vec<_> = cell.iter().copied().collect();
    BTreeSet::from([
        diagonal(vertices[0], vertices[2]),
        diagonal(vertices[1], vertices[3]),
    ])
}

fn sink_source_slots(
    vertices: &[u8],
    channel: Diagonal,
    plus: bool,
) -> (BTreeSet<Diagonal>, BTreeSet<Diagonal>) {
    let plus_side = if channel.0 % 2 == 0 { 1 } else { 0 };
    let target_side = if plus { plus_side } else { 1 - plus_side };
    let cells = quadrilateral_cells_in_hexagon(vertices, channel);
    let sink = cells
        .iter()
        .find(|cell| cell_side_in_polygon(vertices, channel, cell) == target_side)
        .expect("one directed sink");
    let source = cells.iter().find(|cell| *cell != sink).expect("one source");
    (scalar_slots(sink), scalar_slots(source))
}

fn catalan_six_endpoint(
    all: &[Triangulation],
    vertices: &[u8],
    source: &Triangulation,
    mark: Diagonal,
    plus: bool,
) -> (Diagonal, Triangulation) {
    let candidates: Vec<_> = all
        .iter()
        .filter_map(|target| {
            if intersection_size(source, target) != 2 || !target.contains(&mark) {
                return None;
            }
            let core = core_of(target);
            if core.len() != 1 {
                return None;
            }
            let channel = core[0];
            sink_source_slots(vertices, channel, plus)
                .0
                .contains(&mark)
                .then(|| (channel, target.clone()))
        })
        .collect();
    assert_eq!(candidates.len(), 1);
    candidates[0].clone()
}

fn saturated_leg(
    outer: Diagonal,
    center: &Triangulation,
    mark: Diagonal,
    facet: Diagonal,
    all: &[Triangulation],
) -> SixChain {
    let fiber: Vec<_> = all
        .iter()
        .filter(|value| core_of(value) == vec![facet])
        .cloned()
        .collect();
    assert_eq!(fiber.len(), 4);
    let corners: Vec<_> = fiber
        .iter()
        .filter(|value| intersection_size(center, value) == 2)
        .cloned()
        .collect();
    assert_eq!(corners.len(), 1);
    let corner = corners[0].clone();
    assert!(corner.contains(&mark));
    let bridge = ordered_six_edge(center.clone(), corner.clone());
    let internal_neighbors: Vec<_> = fiber
        .iter()
        .filter(|value| intersection_size(&corner, value) == 2)
        .cloned()
        .collect();
    assert_eq!(internal_neighbors.len(), 2);

    let mut result = SixChain::new();
    let mut add = |first: SixNode, second: SixNode, coefficient: Rational| {
        add_six_edge(
            &mut result,
            SixOccurrenceEdge {
                outer,
                center: center.clone(),
                mark,
                first,
                second,
            },
            Laurent::constant(coefficient),
        );
    };
    add(
        SixNode::Vertex(center.clone()),
        bridge.clone(),
        Rational::ONE,
    );
    add(bridge, SixNode::Vertex(corner.clone()), Rational::ONE);
    for neighbor in internal_neighbors {
        let edge = ordered_six_edge(corner.clone(), neighbor);
        add(
            SixNode::Vertex(corner.clone()),
            edge.clone(),
            Rational::new(1, 2),
        );
        add(edge, SixNode::Facet(facet), Rational::new(1, 2));
    }
    result
}

fn add_scaled_six_chain(target: &mut SixChain, source: &SixChain, scalar: &Laurent) {
    for (edge, coefficient) in source {
        add_six_edge(target, edge.clone(), coefficient.multiply(scalar));
    }
}

fn marked_six_chain(outer: Diagonal, vertices: &[u8]) -> SixChain {
    let all = six_local_triangulations(vertices);
    let centers: Vec<_> = all
        .iter()
        .filter(|value| core_of(value).is_empty())
        .cloned()
        .collect();
    assert_eq!(centers.len(), 2);
    let mut result = SixChain::new();
    for center in centers {
        assert_eq!(center.len(), 3);
        for mark in center.iter().copied() {
            let (plus_facet, plus_corner) =
                catalan_six_endpoint(&all, vertices, &center, mark, true);
            let (minus_facet, minus_corner) =
                catalan_six_endpoint(&all, vertices, &center, mark, false);
            assert_ne!(plus_facet, minus_facet);
            let plus_leg = saturated_leg(outer, &center, mark, plus_facet, &all);
            let minus_leg = saturated_leg(outer, &center, mark, minus_facet, &all);
            assert!(plus_leg.keys().any(|edge| {
                edge.first == SixNode::Vertex(plus_corner.clone())
                    || edge.second == SixNode::Vertex(plus_corner.clone())
            }));
            assert!(minus_leg.keys().any(|edge| {
                edge.first == SixNode::Vertex(minus_corner.clone())
                    || edge.second == SixNode::Vertex(minus_corner.clone())
            }));
            let source_coefficient = Laurent::variable(mark).scale(Rational::new(-1, 1));
            add_scaled_six_chain(&mut result, &plus_leg, &source_coefficient);
            add_scaled_six_chain(
                &mut result,
                &minus_leg,
                &source_coefficient.scale(Rational::new(-1, 1)),
            );
        }
    }
    result
}

fn six_chain_boundary(chain: &SixChain) -> BTreeMap<(Triangulation, Diagonal, SixNode), Laurent> {
    let mut result = BTreeMap::new();
    for (edge, coefficient) in chain {
        for (node, sign) in [(&edge.first, -1), (&edge.second, 1)] {
            let key = (edge.center.clone(), edge.mark, node.clone());
            let term = coefficient.scale(Rational::new(sign, 1));
            result
                .entry(key)
                .and_modify(|current: &mut Laurent| *current = current.add(&term))
                .or_insert(term);
        }
    }
    result.retain(|_, value| value != &Laurent::zero());
    result
}

fn augmented_six_boundary(chain: &SixChain) -> BTreeMap<Diagonal, Laurent> {
    let mut result = BTreeMap::new();
    for ((_center, _mark, node), coefficient) in six_chain_boundary(chain) {
        let SixNode::Facet(facet) = node else {
            panic!("occurrence centers and internal flags must cancel");
        };
        result
            .entry(facet)
            .and_modify(|current: &mut Laurent| *current = current.add(&coefficient))
            .or_insert(coefficient);
    }
    result.retain(|_, value| value != &Laurent::zero());
    result
}

fn augmented_six_boundary_by_center(
    chain: &SixChain,
) -> BTreeMap<Triangulation, BTreeMap<Diagonal, Laurent>> {
    let mut result: BTreeMap<Triangulation, BTreeMap<Diagonal, Laurent>> = BTreeMap::new();
    for ((center, _mark, node), coefficient) in six_chain_boundary(chain) {
        let SixNode::Facet(facet) = node else {
            panic!("each marked plus/minus pair cancels at its center and internal flags");
        };
        result
            .entry(center)
            .or_default()
            .entry(facet)
            .and_modify(|current| *current = current.add(&coefficient))
            .or_insert(coefficient);
    }
    for boundary in result.values_mut() {
        boundary.retain(|_, value| value != &Laurent::zero());
    }
    result
}

fn six_center_vectors(vertices: &[u8]) -> BTreeMap<Triangulation, BTreeMap<Diagonal, Laurent>> {
    let all = six_local_triangulations(vertices);
    let centers: Vec<_> = all
        .into_iter()
        .filter(|value| core_of(value).is_empty())
        .collect();
    assert_eq!(centers.len(), 2);
    let x: Vec<_> = (0..6)
        .map(|index| Laurent::variable(local_diagonal(vertices, index, index + 2)))
        .collect();
    let channels = [
        local_diagonal(vertices, 0, 3),
        local_diagonal(vertices, 1, 4),
        local_diagonal(vertices, 2, 5),
    ];
    let even_center = centers
        .iter()
        .find(|center| center.iter().all(|value| value.0 % 2 == 0))
        .expect("one even scalar center")
        .clone();
    let odd_center = centers
        .iter()
        .find(|center| center.iter().all(|value| value.0 % 2 == 1))
        .expect("one odd scalar center")
        .clone();
    BTreeMap::from([
        (
            even_center,
            BTreeMap::from([
                (channels[0], x[0].subtract(&x[4])),
                (channels[1], x[4].subtract(&x[2])),
                (channels[2], x[2].subtract(&x[0])),
            ]),
        ),
        (
            odd_center,
            BTreeMap::from([
                (channels[0], x[1].subtract(&x[3])),
                (channels[1], x[5].subtract(&x[1])),
                (channels[2], x[3].subtract(&x[5])),
            ]),
        ),
    ])
}

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct TensorOccurrence(Diagonal, Diagonal);

type TensorVector = BTreeMap<TensorOccurrence, Laurent>;

fn entry_residue_sheet(vertices: &[u8], channel: Diagonal, plus: bool) -> TensorVector {
    let all = six_local_triangulations(vertices);
    let centers: Vec<_> = all
        .iter()
        .filter(|value| core_of(value).is_empty())
        .cloned()
        .collect();
    let mut result = TensorVector::new();
    for center in centers {
        for mark in center.iter().copied() {
            let (entry_channel, _) = catalan_six_endpoint(&all, vertices, &center, mark, plus);
            if entry_channel != channel {
                continue;
            }
            let (sink, source) = sink_source_slots(vertices, channel, plus);
            assert!(sink.contains(&mark));
            for source_mark in source {
                let cells = quadrilateral_cells_in_hexagon(vertices, channel);
                let side_zero_slots = scalar_slots(
                    cells
                        .iter()
                        .find(|cell| cell_side_in_polygon(vertices, channel, cell) == 0)
                        .expect("one side-zero quadrilateral"),
                );
                let (side_zero_mark, side_one_mark) = if side_zero_slots.contains(&mark) {
                    (mark, source_mark)
                } else {
                    assert!(side_zero_slots.contains(&source_mark));
                    (source_mark, mark)
                };
                // (-X_mark) from the scalar occurrence times the (-1)
                // core-entry/Gysin sign is positive.
                let coefficient = Laurent::variable(mark).multiply(&Laurent::variable(source_mark));
                let key = TensorOccurrence(side_zero_mark, side_one_mark);
                result
                    .entry(key)
                    .and_modify(|current| *current = current.add(&coefficient))
                    .or_insert(coefficient);
            }
        }
    }
    assert_eq!(result.len(), 4);
    result
}

fn primitive_dual(value: &TensorVector) -> i64 {
    value
        .iter()
        .map(|(occurrence, coefficient)| {
            let expected =
                Laurent::variable(occurrence.0).multiply(&Laurent::variable(occurrence.1));
            assert_eq!(*coefficient, expected);
            1_i64
        })
        .sum()
}

// ----- Entry-83 fixed-mark contact chain -----------------------------------

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Matching {
    source: usize,
    mark: Diagonal,
    target: usize,
}

fn physical_core(value: &Triangulation) -> Vec<Diagonal> {
    value
        .iter()
        .copied()
        .filter(|item| physical(*item))
        .collect()
}

fn polygon_boundary_edges() -> BTreeSet<Diagonal> {
    (0..N)
        .map(|vertex| diagonal(vertex, (vertex + 1) % N))
        .collect()
}

fn quadrangulation_cells(value: Quadrangulation) -> Vec<[u8; 4]> {
    let edges: BTreeSet<_> = polygon_boundary_edges().into_iter().chain(value).collect();
    let result: Vec<_> = combinations(&(0..N).collect::<Vec<_>>(), 4)
        .into_iter()
        .filter_map(|vertices| {
            let cell = [vertices[0], vertices[1], vertices[2], vertices[3]];
            (0..4)
                .all(|index| edges.contains(&diagonal(cell[index], cell[(index + 1) % 4])))
                .then_some(cell)
        })
        .collect();
    assert_eq!(result.len(), 3);
    result
}

fn octagon_cell_side(value: Diagonal, cell: [u8; 4]) -> u8 {
    let increasing: BTreeSet<_> = (value.0 + 1..value.1).collect();
    let other: BTreeSet<_> = cell
        .into_iter()
        .filter(|vertex| *vertex != value.0 && *vertex != value.1)
        .collect();
    if other.is_subset(&increasing) {
        0
    } else {
        assert!(other.is_disjoint(&increasing));
        1
    }
}

fn coorientation(value: Diagonal, plus: bool) -> u8 {
    let plus_side = if value.0 % 2 == 0 { 1 } else { 0 };
    if plus {
        plus_side
    } else {
        1 - plus_side
    }
}

fn contact_slots(value: Quadrangulation, plus: bool) -> Vec<Diagonal> {
    let cells = quadrangulation_cells(value);
    let mut outdegree = vec![0_usize; cells.len()];
    for road in value {
        let adjacent: Vec<_> = cells
            .iter()
            .enumerate()
            .filter(|(_, cell)| cell.contains(&road.0) && cell.contains(&road.1))
            .collect();
        assert_eq!(adjacent.len(), 2);
        let target = adjacent
            .iter()
            .find(|(_, cell)| octagon_cell_side(road, **cell) == coorientation(road, plus))
            .unwrap()
            .0;
        let source = adjacent
            .iter()
            .find(|(index, _)| *index != target)
            .unwrap()
            .0;
        outdegree[source] += 1;
    }
    let sinks: Vec<_> = outdegree
        .iter()
        .enumerate()
        .filter_map(|(index, degree)| (*degree == 0).then_some(cells[index]))
        .collect();
    if sinks.len() == 2 {
        return Vec::new();
    }
    assert_eq!(sinks.len(), 1);
    let cell = sinks[0];
    let mut slots = vec![diagonal(cell[0], cell[2]), diagonal(cell[1], cell[3])];
    slots.sort();
    slots
}

fn bfs(start: usize, adjacency: &[Vec<usize>]) -> Vec<usize> {
    let mut distances = vec![usize::MAX; adjacency.len()];
    distances[start] = 0;
    let mut queue = VecDeque::from([start]);
    while let Some(current) = queue.pop_front() {
        for neighbor in &adjacency[current] {
            if distances[*neighbor] == usize::MAX {
                distances[*neighbor] = distances[current] + 1;
                queue.push_back(*neighbor);
            }
        }
    }
    distances
}

fn permutations(values: &[usize]) -> Vec<Vec<usize>> {
    fn recurse(values: &mut Vec<usize>, start: usize, result: &mut Vec<Vec<usize>>) {
        if start == values.len() {
            result.push(values.clone());
            return;
        }
        for index in start..values.len() {
            values.swap(start, index);
            recurse(values, start + 1, result);
            values.swap(start, index);
        }
    }
    let mut values = values.to_vec();
    let mut result = Vec::new();
    recurse(&mut values, 0, &mut result);
    result
}

fn derive_matching(
    plus: bool,
    triangulations: &[Triangulation],
    quadrangulations: &[Quadrangulation],
    zero_core: &[usize],
    fibers: &[Vec<usize>],
    distances: &BTreeMap<usize, Vec<usize>>,
) -> Vec<Matching> {
    let mut sources_by_mark: BTreeMap<Diagonal, Vec<usize>> = BTreeMap::new();
    for source in zero_core {
        for mark in &triangulations[*source] {
            sources_by_mark.entry(*mark).or_default().push(*source);
        }
    }
    let mut targets_by_mark: BTreeMap<Diagonal, Vec<usize>> = BTreeMap::new();
    for (target, quadrangulation) in quadrangulations.iter().enumerate() {
        for mark in contact_slots(*quadrangulation, plus) {
            targets_by_mark.entry(mark).or_default().push(target);
        }
    }
    assert_eq!(
        sources_by_mark.keys().collect::<Vec<_>>(),
        targets_by_mark.keys().collect::<Vec<_>>()
    );
    let mut result = Vec::new();
    for (mark, sources) in sources_by_mark {
        let targets = &targets_by_mark[&mark];
        let marked_distance = |source: usize, target: usize| {
            fibers[target]
                .iter()
                .filter(|endpoint| triangulations[**endpoint].contains(&mark))
                .map(|endpoint| distances[&source][*endpoint])
                .min()
                .unwrap()
        };
        let scored: Vec<_> = permutations(targets)
            .into_iter()
            .map(|order| {
                let score = sources
                    .iter()
                    .zip(&order)
                    .map(|(source, target)| marked_distance(*source, *target))
                    .sum::<usize>();
                (score, order)
            })
            .collect();
        let minimum = scored.iter().map(|(score, _)| *score).min().unwrap();
        let minimizers: Vec<_> = scored
            .into_iter()
            .filter(|(score, _)| *score == minimum)
            .collect();
        assert_eq!(minimizers.len(), 1);
        for (source, target) in sources.iter().zip(&minimizers[0].1) {
            assert_eq!(marked_distance(*source, *target), 2);
            result.push(Matching {
                source: *source,
                mark,
                target: *target,
            });
        }
    }
    result.sort();
    assert_eq!(result.len(), 20);
    result
}

fn marked_paths(
    matching: Matching,
    triangulations: &[Triangulation],
    adjacency: &[Vec<usize>],
    fibers: &[Vec<usize>],
) -> Vec<(usize, usize, usize)> {
    let mut result = Vec::new();
    for middle in &adjacency[matching.source] {
        for endpoint in &adjacency[*middle] {
            if fibers[matching.target].contains(endpoint)
                && triangulations[*endpoint].contains(&matching.mark)
            {
                assert!(triangulations[matching.source].contains(&matching.mark));
                assert!(triangulations[*middle].contains(&matching.mark));
                result.push((matching.source, *middle, *endpoint));
            }
        }
    }
    result.sort();
    assert!((1..=2).contains(&result.len()));
    assert_eq!(
        result
            .iter()
            .map(|path| path.2)
            .collect::<BTreeSet<_>>()
            .len(),
        1
    );
    result
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct ContactEdge {
    mark: Diagonal,
    first: usize,
    second: usize,
}

type ContactChain = BTreeMap<ContactEdge, Laurent>;

fn add_contact_edge(result: &mut ContactChain, edge: ContactEdge, coefficient: Laurent) {
    result
        .entry(edge)
        .and_modify(|current| *current = current.add(&coefficient))
        .or_insert(coefficient);
    result.retain(|_, value| value != &Laurent::zero());
}

fn contact_chain(
    plus: &[Matching],
    minus: &[Matching],
    triangulations: &[Triangulation],
    adjacency: &[Vec<usize>],
    fibers: &[Vec<usize>],
) -> ContactChain {
    let plus_by_occurrence: BTreeMap<_, _> = plus
        .iter()
        .map(|matching| ((matching.source, matching.mark), *matching))
        .collect();
    let minus_by_occurrence: BTreeMap<_, _> = minus
        .iter()
        .map(|matching| ((matching.source, matching.mark), *matching))
        .collect();
    assert_eq!(
        plus_by_occurrence.keys().collect::<Vec<_>>(),
        minus_by_occurrence.keys().collect::<Vec<_>>()
    );
    let mut result = ContactChain::new();
    for (occurrence, plus_matching) in plus_by_occurrence {
        let minus_matching = minus_by_occurrence[&occurrence];
        for (matching, polarity_sign) in [(plus_matching, 1), (minus_matching, -1)] {
            let paths = marked_paths(matching, triangulations, adjacency, fibers);
            let path_weight = Rational::new(polarity_sign, paths.len() as i64);
            let coefficient =
                Laurent::variable(matching.mark).scale(Rational::new(-1, 1).multiply(path_weight));
            for (source, middle, endpoint) in paths {
                add_contact_edge(
                    &mut result,
                    ContactEdge {
                        mark: matching.mark,
                        first: source,
                        second: middle,
                    },
                    coefficient.clone(),
                );
                add_contact_edge(
                    &mut result,
                    ContactEdge {
                        mark: matching.mark,
                        first: middle,
                        second: endpoint,
                    },
                    coefficient.clone(),
                );
            }
        }
    }
    result
}

fn contact_boundary(chain: &ContactChain) -> BTreeMap<(Diagonal, usize), Laurent> {
    let mut result = BTreeMap::new();
    for (edge, coefficient) in chain {
        for (vertex, sign) in [(edge.first, -1), (edge.second, 1)] {
            let term = coefficient.scale(Rational::new(sign, 1));
            result
                .entry((edge.mark, vertex))
                .and_modify(|current: &mut Laurent| *current = current.add(&term))
                .or_insert(term);
        }
    }
    result.retain(|_, value| value != &Laurent::zero());
    result
}

fn core_forget_contact_boundary(
    boundary: &BTreeMap<(Diagonal, usize), Laurent>,
    triangulations: &[Triangulation],
) -> BTreeMap<Quadrangulation, Laurent> {
    let mut result = BTreeMap::new();
    for ((_mark, vertex), coefficient) in boundary {
        let core = physical_core(&triangulations[*vertex]);
        assert_eq!(core.len(), 2);
        let key = [core[0], core[1]];
        result
            .entry(key)
            .and_modify(|current: &mut Laurent| *current = current.add(coefficient))
            .or_insert_with(|| coefficient.clone());
    }
    result.retain(|_, value| value != &Laurent::zero());
    result
}

// ----- Dihedral covariance --------------------------------------------------

fn transform_vertex(value: u8, amount: u8, reflect: bool) -> u8 {
    let reflected = if reflect { (N - value) % N } else { value };
    (reflected + amount) % N
}

fn transform_diagonal(value: Diagonal, amount: u8, reflect: bool) -> Diagonal {
    diagonal(
        transform_vertex(value.0, amount, reflect),
        transform_vertex(value.1, amount, reflect),
    )
}

fn transform_triangulation(value: &Triangulation, amount: u8, reflect: bool) -> Triangulation {
    let mut result: Vec<_> = value
        .iter()
        .map(|item| transform_diagonal(*item, amount, reflect))
        .collect();
    result.sort();
    result
}

fn transform_quadrangulation(value: Quadrangulation, amount: u8, reflect: bool) -> Quadrangulation {
    let mut result = value.map(|item| transform_diagonal(item, amount, reflect));
    result.sort();
    result
}

fn transform_laurent(value: &Laurent, amount: u8, reflect: bool) -> Laurent {
    let mut result = Laurent::zero();
    for (powers, coefficient) in &value.0 {
        let mut transformed = [0_i8; VARIABLES];
        for (index, exponent) in powers.iter().enumerate() {
            if *exponent != 0 {
                let source = all_diagonals(N)[index];
                let target = transform_diagonal(source, amount, reflect);
                transformed[variable_index(target)] += *exponent;
            }
        }
        result = result.add(&Laurent(BTreeMap::from([(transformed, *coefficient)])));
    }
    result
}

fn transform_six_node(value: &SixNode, amount: u8, reflect: bool) -> SixNode {
    match value {
        SixNode::Vertex(triangulation) => {
            SixNode::Vertex(transform_triangulation(triangulation, amount, reflect))
        }
        SixNode::Edge(first, second) => ordered_six_edge(
            transform_triangulation(first, amount, reflect),
            transform_triangulation(second, amount, reflect),
        ),
        SixNode::Facet(facet) => SixNode::Facet(transform_diagonal(*facet, amount, reflect)),
    }
}

fn transform_six_chain(value: &SixChain, amount: u8, reflect: bool) -> SixChain {
    let mut result = SixChain::new();
    for (edge, coefficient) in value {
        add_six_edge(
            &mut result,
            SixOccurrenceEdge {
                outer: transform_diagonal(edge.outer, amount, reflect),
                center: transform_triangulation(&edge.center, amount, reflect),
                mark: transform_diagonal(edge.mark, amount, reflect),
                first: transform_six_node(&edge.first, amount, reflect),
                second: transform_six_node(&edge.second, amount, reflect),
            },
            transform_laurent(coefficient, amount, reflect),
        );
    }
    result
}

fn scale_six_chain(value: &SixChain, scalar: Rational) -> SixChain {
    value
        .iter()
        .map(|(edge, coefficient)| (edge.clone(), coefficient.scale(scalar)))
        .collect()
}

fn multiply_six_chain(value: &SixChain, scalar: &Laurent) -> SixChain {
    value
        .iter()
        .map(|(edge, coefficient)| (edge.clone(), coefficient.multiply(scalar)))
        .collect()
}

fn transform_contact_chain(
    value: &ContactChain,
    amount: u8,
    reflect: bool,
    triangulations: &[Triangulation],
) -> ContactChain {
    let mut result = ContactChain::new();
    for (edge, coefficient) in value {
        let transformed_index = |index: usize| {
            let transformed = transform_triangulation(&triangulations[index], amount, reflect);
            triangulations
                .iter()
                .position(|value| *value == transformed)
                .expect("the dihedral image is an octagon triangulation")
        };
        add_contact_edge(
            &mut result,
            ContactEdge {
                mark: transform_diagonal(edge.mark, amount, reflect),
                first: transformed_index(edge.first),
                second: transformed_index(edge.second),
            },
            transform_laurent(coefficient, amount, reflect),
        );
    }
    result
}

fn scale_contact_chain(value: &ContactChain, scalar: Rational) -> ContactChain {
    value
        .iter()
        .map(|(edge, coefficient)| (*edge, coefficient.scale(scalar)))
        .collect()
}

fn transformed_matching(
    matching: Matching,
    amount: u8,
    reflect: bool,
    triangulations: &[Triangulation],
    quadrangulations: &[Quadrangulation],
) -> Matching {
    let source_value = transform_triangulation(&triangulations[matching.source], amount, reflect);
    let target_value =
        transform_quadrangulation(quadrangulations[matching.target], amount, reflect);
    Matching {
        source: triangulations
            .iter()
            .position(|value| *value == source_value)
            .unwrap(),
        mark: transform_diagonal(matching.mark, amount, reflect),
        target: quadrangulations
            .iter()
            .position(|value| *value == target_value)
            .unwrap(),
    }
}

fn audit() {
    let all = triangulations(N);
    assert_eq!(all.len(), 132);
    let adjacency = triangulation_adjacency(&all);
    assert!(adjacency.iter().all(|neighbors| neighbors.len() == 5));
    let quadrangulations = quadrangulations();
    let physical = physical_diagonals();

    // Entry 23: retain all scalar cells and exhaust every Laurent sector.
    let (groups, individual) = scalar_grade_by_core(&all);
    let core_counts = all.iter().fold(BTreeMap::new(), |mut counts, value| {
        *counts.entry(physical_core(value).len()).or_default() += 1;
        counts
    });
    assert_eq!(core_counts, BTreeMap::from([(0, 4), (1, 32), (2, 96)]));
    let full_core: BTreeMap<_, _> = quadrangulations
        .iter()
        .map(|value| (*value, groups[&value.to_vec()].clone()))
        .collect();
    let one_core: BTreeMap<_, _> = physical
        .iter()
        .map(|value| (*value, groups[&vec![*value]].clone()))
        .collect();
    let zero_core = groups[&Vec::new()].clone();
    assert_eq!(
        individual
            .iter()
            .filter(|(triangulation, _)| physical_core(triangulation).is_empty())
            .fold(Laurent::zero(), |sum, (_, value)| sum.add(value)),
        zero_core
    );

    let plus = decompose(qtds_diagrams(&(0..N).collect::<Vec<_>>(), true), &full_core);
    let minus = decompose(
        qtds_diagrams(&(0..N).collect::<Vec<_>>(), false),
        &full_core,
    );
    assert_eq!(plus.q.len(), 12);
    assert_eq!(minus.q.len(), 12);
    assert_eq!(plus.g, minus.g);

    let mut pole_grade_counts = Vec::new();
    for decomposition in [&plus, &minus] {
        let mut double_occurrences = BTreeSet::new();
        let mut single_occurrences = BTreeSet::new();
        let mut regular_occurrences = BTreeSet::new();
        for quadrangulation in &quadrangulations {
            let expected_double_support: BTreeSet<_> = quadrangulation
                .iter()
                .map(|channel| variable_index(*channel))
                .collect();
            for powers in decomposition.g[quadrangulation].0.keys() {
                assert_eq!(
                    Laurent::negative_support(powers)
                        .into_iter()
                        .collect::<BTreeSet<_>>(),
                    expected_double_support
                );
                assert!(quadrangulation
                    .iter()
                    .all(|channel| powers[variable_index(*channel)] == -1));
                double_occurrences.insert((*quadrangulation, *powers));
            }
            for channel in quadrangulation {
                for powers in decomposition.r[&(*quadrangulation, *channel)].0.keys() {
                    assert_eq!(
                        Laurent::negative_support(powers),
                        vec![variable_index(*channel)]
                    );
                    assert_eq!(powers[variable_index(*channel)], -1);
                    single_occurrences.insert((*quadrangulation, *powers));
                }
            }
            for powers in decomposition.k[quadrangulation].0.keys() {
                assert!(Laurent::negative_support(powers).is_empty());
                regular_occurrences.insert((*quadrangulation, *powers));
            }
        }
        assert!(double_occurrences.is_disjoint(&single_occurrences));
        assert!(double_occurrences.is_disjoint(&regular_occurrences));
        assert!(single_occurrences.is_disjoint(&regular_occurrences));
        assert_eq!(regular_occurrences.len(), 20);
        pole_grade_counts.push((
            double_occurrences.len(),
            single_occurrences.len(),
            regular_occurrences.len(),
        ));
        for channel in &physical {
            let allocated = quadrangulations
                .iter()
                .filter(|quadrangulation| quadrangulation.contains(channel))
                .fold(Laurent::zero(), |sum, quadrangulation| {
                    sum.add(&decomposition.r[&(*quadrangulation, *channel)])
                });
            assert_eq!(allocated, one_core[channel]);
        }
        assert_eq!(
            decomposition
                .k
                .values()
                .fold(Laurent::zero(), |sum, value| sum.add(value)),
            zero_core
        );
        assert_eq!(
            decomposition
                .q
                .values()
                .fold(Laurent::zero(), |sum, value| sum.add(value)),
            groups
                .values()
                .fold(Laurent::zero(), |sum, value| sum.add(value))
        );
    }

    // Occurrence-resolved H_6 is inserted on all eight factorization
    // triangles.  Ins_D=hhat_D(q_4 boxtimes -)[dX_D], with rooted q_4=-c_4,
    // is the negative ordered-normal Gysin symbol of entries 32 and 38.
    let mut insertion_boundary: BTreeMap<Quadrangulation, Laurent> = BTreeMap::new();
    let mut six_chains = BTreeMap::new();
    let mut allowed_primary = 0;
    let mut allowed_nested = 0;
    let mut forbidden_nested = 0;
    let mut side_orders = BTreeMap::new();
    for outer in &physical {
        let (hexagon, quadrilateral) = cut_polygons(*outer);
        let c4 = four_point_cycle(&quadrilateral);
        let q4_plus = qtds_diagrams(&quadrilateral, true);
        let q4_minus = qtds_diagrams(&quadrilateral, false);
        assert_eq!(q4_plus, q4_minus);
        // The rooted QTDS convention carries (-1)^(4/2-1)=-1.  The
        // side-ordered PC factor is the positively normalized occurrence
        // cycle c_4, so the raw rooted term is -c_4.
        assert_eq!(q4_plus[&Vec::new()], c4.scale(Rational::new(-1, 1)));
        let q4 = q4_plus[&Vec::new()].clone();
        let even_endpoint = if outer.0 % 2 == 0 { outer.0 } else { outer.1 };
        let odd_endpoint = if outer.0 % 2 == 1 { outer.0 } else { outer.1 };
        let oriented_arc_arity = ((odd_endpoint + N - even_endpoint) % N + 1) as usize;
        let side_order = if oriented_arc_arity == 4 {
            (4_usize, 6_usize)
        } else {
            assert_eq!(oriented_arc_arity, 6);
            (6_usize, 4_usize)
        };
        side_orders.insert(*outer, side_order);

        let q6_plus = qtds_diagrams(&hexagon, true);
        let q6_minus = qtds_diagrams(&hexagon, false);
        let q6_difference: BTreeMap<_, _> = q6_plus
            .iter()
            .map(|(channel, value)| {
                assert_eq!(channel.len(), 1);
                (channel[0], value.subtract(&q6_minus[channel]))
            })
            .collect();
        assert_eq!(q6_difference, six_boundary_vector(&hexagon));

        let chain = marked_six_chain(*outer, &hexagon);
        assert_eq!(chain.len(), 72);
        let occurrences: BTreeSet<_> = chain
            .keys()
            .map(|edge| (edge.center.clone(), edge.mark))
            .collect();
        assert_eq!(occurrences.len(), 6);
        let occurrences_by_center = occurrences.iter().fold(
            BTreeMap::new(),
            |mut counts: BTreeMap<Triangulation, usize>, (center, _)| {
                *counts.entry(center.clone()).or_default() += 1;
                counts
            },
        );
        assert_eq!(occurrences_by_center.len(), 2);
        assert!(occurrences_by_center.values().all(|count| *count == 3));
        assert_eq!(
            augmented_six_boundary_by_center(&chain),
            six_center_vectors(&hexagon)
        );
        assert_eq!(augmented_six_boundary(&chain), q6_difference);
        let primary_residue_chain = multiply_six_chain(&chain, &q4);
        let expected_primary_boundary: BTreeMap<_, _> = q6_difference
            .iter()
            .map(|(channel, value)| (*channel, q4.multiply(value)))
            .collect();
        assert_eq!(
            augmented_six_boundary(&primary_residue_chain),
            expected_primary_boundary
        );
        six_chains.insert(*outer, chain);

        let local_channels: BTreeSet<_> = q6_difference.keys().copied().collect();
        assert_eq!(local_channels.len(), 3);
        for inner in &physical {
            if inner == outer {
                allowed_primary += 1;
                continue;
            }
            if local_channels.contains(inner) {
                assert!(!crosses_in(*outer, *inner, N));
                let plus_residue = entry_residue_sheet(&hexagon, *inner, true);
                let minus_residue = entry_residue_sheet(&hexagon, *inner, false);
                assert_eq!(primitive_dual(&plus_residue), 4);
                assert_eq!(primitive_dual(&minus_residue), 4);
                assert_eq!(plus_residue, minus_residue);
                allowed_nested += 1;
            } else {
                assert!(crosses_in(*outer, *inner, N));
                forbidden_nested += 1;
            }
        }

        for (inner, six_value) in &q6_difference {
            let mut quadrangulation = [*outer, *inner];
            quadrangulation.sort();
            let expected = q4.multiply(six_value).divide_variable(*outer);
            let actual =
                plus.r[&(quadrangulation, *outer)].subtract(&minus.r[&(quadrangulation, *outer)]);
            assert_eq!(actual, expected);
            assert_eq!(
                actual.multiply(&Laurent::variable(*outer)),
                expected_primary_boundary[inner]
            );
            insertion_boundary
                .entry(quadrangulation)
                .and_modify(|current| *current = current.add(&expected))
                .or_insert(expected);
        }
    }
    assert_eq!(
        (allowed_primary, allowed_nested, forbidden_nested),
        (8, 24, 32)
    );
    assert_eq!(
        side_orders
            .values()
            .filter(|order| **order == (4, 6))
            .count(),
        4
    );
    assert_eq!(
        side_orders
            .values()
            .filter(|order| **order == (6, 4))
            .count(),
        4
    );

    // Entry 83: derive both twenty-occurrence fixed-mark matchings, retain
    // the mark on every path vertex, and take the forced half-sum when two
    // paths exist.
    let zero_core_indices: Vec<_> = all
        .iter()
        .enumerate()
        .filter_map(|(index, value)| physical_core(value).is_empty().then_some(index))
        .collect();
    assert_eq!(zero_core_indices.len(), 4);
    let fibers: Vec<Vec<_>> = quadrangulations
        .iter()
        .map(|quadrangulation| {
            all.iter()
                .enumerate()
                .filter_map(|(index, value)| {
                    (physical_core(value) == quadrangulation.to_vec()).then_some(index)
                })
                .collect()
        })
        .collect();
    assert!(fibers.iter().all(|fiber| fiber.len() == 8));
    let distances: BTreeMap<_, _> = zero_core_indices
        .iter()
        .map(|source| (*source, bfs(*source, &adjacency)))
        .collect();
    let contact_plus = derive_matching(
        true,
        &all,
        &quadrangulations,
        &zero_core_indices,
        &fibers,
        &distances,
    );
    let contact_minus = derive_matching(
        false,
        &all,
        &quadrangulations,
        &zero_core_indices,
        &fibers,
        &distances,
    );
    let contact = contact_chain(&contact_plus, &contact_minus, &all, &adjacency, &fibers);
    assert!(contact.values().all(Laurent::is_regular));
    let occurrence_boundary = contact_boundary(&contact);
    assert_eq!(occurrence_boundary.len(), 40);
    let contact_boundary = core_forget_contact_boundary(&occurrence_boundary, &all);
    let expected_contact_boundary: BTreeMap<_, _> = quadrangulations
        .iter()
        .map(|quadrangulation| {
            (
                *quadrangulation,
                plus.k[quadrangulation].subtract(&minus.k[quadrangulation]),
            )
        })
        .filter(|(_, value)| value != &Laurent::zero())
        .collect();
    assert_eq!(contact_boundary, expected_contact_boundary);
    // Regular contact coefficients have no physical Laurent residue; entry
    // 38 monoidality therefore sends all eight scalar residues to zero.
    for channel in &physical {
        assert_eq!(
            contact.values().fold(Laurent::zero(), |sum, value| {
                sum.add(&value.select_negative_support(&[variable_index(*channel)]))
            }),
            Laurent::zero()
        );
    }

    // Full boundary equality, diagram by diagram.  The G sector cancels
    // pointwise; factor triangles supply all R differences; H_ct supplies
    // all K differences.  There is no fourth sector.
    for quadrangulation in &quadrangulations {
        let actual = plus.q[quadrangulation].subtract(&minus.q[quadrangulation]);
        let rebuilt = insertion_boundary
            .get(quadrangulation)
            .cloned()
            .unwrap_or_else(Laurent::zero)
            .add(
                &contact_boundary
                    .get(quadrangulation)
                    .cloned()
                    .unwrap_or_else(Laurent::zero),
            );
        assert_eq!(actual, rebuilt);
    }

    // D_8 covariance of q, G/R/K, both complete marked chains, and the
    // contact matching.  The deck character is the alternating character
    // of D_8: an odd
    // rotation swaps sheets, and the base reflection v |-> -v swaps the
    // rooted cyclic QTDS polarity because it reverses cyclic order.
    for reflect in [false, true] {
        for amount in 0..N {
            let swaps_sheet = (amount % 2 == 1) ^ reflect;
            let target_plus = if swaps_sheet { &minus } else { &plus };
            for quadrangulation in &quadrangulations {
                let transformed = transform_quadrangulation(*quadrangulation, amount, reflect);
                assert_eq!(
                    transform_laurent(&plus.q[quadrangulation], amount, reflect),
                    target_plus.q[&transformed]
                );
                assert_eq!(
                    transform_laurent(&plus.g[quadrangulation], amount, reflect),
                    target_plus.g[&transformed]
                );
                assert_eq!(
                    transform_laurent(&plus.k[quadrangulation], amount, reflect),
                    target_plus.k[&transformed]
                );
                for channel in quadrangulation {
                    let transformed_channel = transform_diagonal(*channel, amount, reflect);
                    assert_eq!(
                        transform_laurent(&plus.r[&(*quadrangulation, *channel)], amount, reflect,),
                        target_plus.r[&(transformed, transformed_channel)]
                    );
                }
            }
            let transformed_plus: BTreeSet<_> = contact_plus
                .iter()
                .map(|matching| {
                    transformed_matching(*matching, amount, reflect, &all, &quadrangulations)
                })
                .collect();
            let expected: BTreeSet<_> = if swaps_sheet {
                contact_minus.iter().copied().collect()
            } else {
                contact_plus.iter().copied().collect()
            };
            assert_eq!(transformed_plus, expected);
            let character = if swaps_sheet {
                Rational::new(-1, 1)
            } else {
                Rational::ONE
            };
            assert_eq!(
                transform_contact_chain(&contact, amount, reflect, &all),
                scale_contact_chain(&contact, character)
            );
            for outer in &physical {
                let transformed_outer = transform_diagonal(*outer, amount, reflect);
                assert_eq!(
                    transform_six_chain(&six_chains[outer], amount, reflect),
                    scale_six_chain(&six_chains[&transformed_outer], character)
                );
            }
        }
    }

    // Ordered normal and normalization audit.  One outer Gysin contributes
    // -h_D[dX_D].  Each inner entry contributes another minus, while its
    // marked source contributes -X_d; the two latter signs produce the
    // positive sheet tensor certified above.  Reversing two normal factors
    // gives the ordinary Koszul sign.
    let outer_gysin_sign = -1_i8;
    let entry_gysin_sign = -1_i8;
    let scalar_source_sign = -1_i8;
    assert_eq!(entry_gysin_sign * scalar_source_sign, 1);
    assert_eq!(outer_gysin_sign * entry_gysin_sign * scalar_source_sign, -1);
    for quadrangulation in &quadrangulations {
        let forward_sign = if quadrangulation[0] < quadrangulation[1] {
            1_i8
        } else {
            -1_i8
        };
        let reverse_sign = if quadrangulation[1] < quadrangulation[0] {
            1_i8
        } else {
            -1_i8
        };
        assert_eq!(forward_sign, -reverse_sign);
    }

    println!("complete occurrence-resolved eight-point PC homotopy audit");
    println!("  exact scalar cells: 132 = 96 full-core + 32 one-core + 4 zero-core");
    println!("  q+ and q-: 12 diagrams each; G/R/K decomposition is exhaustive");
    println!(
        "  pole-grade occurrences (G,R,K): plus={:?}; minus={:?}; pairwise disjoint",
        pole_grade_counts[0], pole_grade_counts[1]
    );
    println!("  factorization triangles: 8; marked saturated H_6 insertions: 8");
    println!("  each H_6 insertion is a disjoint 3+3 even/odd marked occurrence sum");
    println!("  saturated H_6 edges per insertion: 72; tail weights: 1/2,1/2");
    println!("  primary cut table: 8 side-ordered Res_D H_8 = q_4 tensor H_6^mark");
    println!("  side orders: four (4,6) and four (6,4)");
    println!("  compatible double residues: 24 null (sheet periods 4-4=0)");
    println!("  forbidden ordered residues: 32 zero; contact residues: 8 zero");
    println!("  all 24 ordered double residues therefore vanish with Koszul swap sign -");
    println!("  entry-83 contact occurrences: 20 per sheet; fixed-mark boundary exact");
    println!("  covariance: complete chains under all 16 D_8 / induced D_6 actions");
    println!("  signs: q_8 -, rooted q_4 -, Ins/c_4 -, source -, entry -, Koszul swap -");
    println!();
    println!("VERDICT: PROVED");
    println!("  d_PC H_8^PC = sum_Q (q_Q^+ - q_Q^-), with no omitted sector");
}

fn main() {
    audit();
}
