//! Exact certificate for gluing the two longitudinal Ward exits on every
//! internal edge of K_{2,3}.
//!
//! For all-outgoing endpoint momenta k and -k, the longitudinal tensor
//!
//!     Q(k) = k tensor k / k^2
//!
//! is even.  The physically motivated endpoint quotient is therefore
//! Q_{e,tail}=Q_{e,head}.  We audit it against the algebraically possible but
//! tensorially wrong opposite-sign convention.  The quotient itself is only
//! a physical chain map if sewing introduces no additional endpoint sign.

use std::collections::BTreeSet;

const VERTICES: usize = 5;
const EDGES: usize = 6;
const WARD_MARKS: usize = 9;
const EXITS: usize = 2 * EDGES;
const QUOTIENT_MARKS: [usize; 7] = [0, 1, 3, 4, 6, 7, 8];

type Chain6 = [i64; EDGES];
type ExitChain = [i64; EXITS];

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct DegreeZero {
    contacts: Chain6,
    exits: ExitChain,
}

impl DegreeZero {
    fn zero() -> Self {
        Self {
            contacts: [0; EDGES],
            exits: [0; EXITS],
        }
    }

    fn add_scaled(&mut self, other: Self, coefficient: i64) {
        for edge in 0..EDGES {
            self.contacts[edge] += coefficient * other.contacts[edge];
        }
        for exit in 0..EXITS {
            self.exits[exit] += coefficient * other.exits[exit];
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct GluedDegreeZero {
    contacts: Chain6,
    longitudinal: Chain6,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Gluing {
    Even,
    Odd,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum WardMark {
    Left { core: usize, incoming_road: usize },
    RightExternal { road: usize },
}

fn edge_slot(core: usize, road: usize) -> usize {
    2 * road + core
}

fn edge_vertices(edge: usize) -> (usize, usize) {
    (edge % 2, 2 + edge / 2)
}

fn endpoint_exit(edge: usize, vertex: usize) -> usize {
    let (tail, head) = edge_vertices(edge);
    if vertex == tail {
        2 * edge
    } else {
        assert_eq!(vertex, head);
        2 * edge + 1
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

// dW=(C_next-Q_next,vertex)-(C_previous-Q_previous,vertex).
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
        WardMark::RightExternal { road } => {
            (2 + road, edge_slot(0, road), edge_slot(1, road))
        }
    };
    let mut result = DegreeZero::zero();
    result.contacts[next] += 1;
    result.contacts[previous] -= 1;
    result.exits[endpoint_exit(next, vertex)] -= 1;
    result.exits[endpoint_exit(previous, vertex)] += 1;
    result
}

fn glue(value: DegreeZero, convention: Gluing) -> GluedDegreeZero {
    let longitudinal = std::array::from_fn(|edge| match convention {
        Gluing::Even => value.exits[2 * edge] + value.exits[2 * edge + 1],
        Gluing::Odd => value.exits[2 * edge] - value.exits[2 * edge + 1],
    });
    GluedDegreeZero {
        contacts: value.contacts,
        longitudinal,
    }
}

fn apply_raw(coefficients: [i64; WARD_MARKS]) -> DegreeZero {
    let mut result = DegreeZero::zero();
    for (coefficient, mark) in coefficients.into_iter().zip(ward_marks()) {
        result.add_scaled(ward_differential(mark), coefficient);
    }
    result
}

fn local_relations() -> [[i64; WARD_MARKS]; 2] {
    [
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
    ]
}

fn raw_columns(mode: Option<Gluing>, contact_only: bool) -> Vec<Vec<i64>> {
    ward_marks()
        .into_iter()
        .map(|mark| {
            let value = ward_differential(mark);
            if contact_only {
                value.contacts.to_vec()
            } else if let Some(convention) = mode {
                let value = glue(value, convention);
                value
                    .contacts
                    .into_iter()
                    .chain(value.longitudinal)
                    .collect()
            } else {
                value.contacts.into_iter().chain(value.exits).collect()
            }
        })
        .collect()
}

fn quotient_columns(columns: &[Vec<i64>]) -> Vec<Vec<i64>> {
    QUOTIENT_MARKS
        .iter()
        .map(|&index| columns[index].clone())
        .collect()
}

fn gcd(mut left: i128, mut right: i128) -> i128 {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        (left, right) = (right, left % right);
    }
    left
}

fn lcm(left: i128, right: i128) -> i128 {
    if left == 0 || right == 0 {
        0
    } else {
        (left / gcd(left, right)) * right
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rational {
    numerator: i128,
    denominator: i128,
}

impl Rational {
    fn new(numerator: i128, denominator: i128) -> Self {
        assert_ne!(denominator, 0);
        if numerator == 0 {
            return Self {
                numerator: 0,
                denominator: 1,
            };
        }
        let sign = if denominator < 0 { -1 } else { 1 };
        let divisor = gcd(numerator, denominator);
        Self {
            numerator: sign * numerator / divisor,
            denominator: denominator.abs() / divisor,
        }
    }

    fn zero() -> Self {
        Self::new(0, 1)
    }

    fn one() -> Self {
        Self::new(1, 1)
    }

    fn is_zero(self) -> bool {
        self.numerator == 0
    }

    fn add(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )
    }

    fn neg(self) -> Self {
        Self::new(-self.numerator, self.denominator)
    }

    fn multiply(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )
    }

    fn divide(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.denominator,
            self.denominator * other.numerator,
        )
    }
}

fn matrix_from_columns(columns: &[Vec<i64>]) -> Vec<Vec<Rational>> {
    assert!(!columns.is_empty());
    let rows = columns[0].len();
    assert!(columns.iter().all(|column| column.len() == rows));
    (0..rows)
        .map(|row| {
            columns
                .iter()
                .map(|column| Rational::new(i128::from(column[row]), 1))
                .collect()
        })
        .collect()
}

fn rref(columns: &[Vec<i64>]) -> (Vec<Vec<Rational>>, Vec<usize>) {
    let mut matrix = matrix_from_columns(columns);
    let column_count = columns.len();
    let mut pivot_row = 0;
    let mut pivots = Vec::new();
    for column in 0..column_count {
        let Some(found) = (pivot_row..matrix.len()).find(|&row| !matrix[row][column].is_zero())
        else {
            continue;
        };
        matrix.swap(pivot_row, found);
        let pivot = matrix[pivot_row][column];
        for entry in &mut matrix[pivot_row] {
            *entry = entry.divide(pivot);
        }
        let normalized = matrix[pivot_row].clone();
        for (row_index, row) in matrix.iter_mut().enumerate() {
            if row_index == pivot_row || row[column].is_zero() {
                continue;
            }
            let coefficient = row[column];
            for entry in 0..column_count {
                row[entry] = row[entry].add(normalized[entry].multiply(coefficient).neg());
            }
        }
        pivots.push(column);
        pivot_row += 1;
        if pivot_row == matrix.len() {
            break;
        }
    }
    (matrix, pivots)
}

fn rational_rank(columns: &[Vec<i64>]) -> usize {
    rref(columns).1.len()
}

fn primitive_integer_kernel(columns: &[Vec<i64>]) -> Vec<Vec<i64>> {
    let (matrix, pivots) = rref(columns);
    let pivot_set: BTreeSet<_> = pivots.iter().copied().collect();
    let mut result = Vec::new();
    for free in (0..columns.len()).filter(|column| !pivot_set.contains(column)) {
        let mut vector = vec![Rational::zero(); columns.len()];
        vector[free] = Rational::one();
        for (row, &pivot) in pivots.iter().enumerate() {
            vector[pivot] = matrix[row][free].neg();
        }
        // In every matrix audited below the RREF kernel coordinates are
        // integral.  Hence the free coordinates give a genuine Z-basis, not
        // merely primitive rational rays.
        assert!(vector.iter().all(|value| value.denominator == 1));
        let denominator = vector
            .iter()
            .fold(1_i128, |common, value| lcm(common, value.denominator));
        let mut integers: Vec<i128> = vector
            .iter()
            .map(|value| value.numerator * (denominator / value.denominator))
            .collect();
        let divisor = integers
            .iter()
            .fold(0_i128, |common, &value| gcd(common, value));
        for value in &mut integers {
            *value /= divisor;
        }
        if integers.iter().find(|&&value| value != 0).is_some_and(|&value| value < 0) {
            for value in &mut integers {
                *value = -*value;
            }
        }
        let integers: Vec<i64> = integers
            .into_iter()
            .map(|value| i64::try_from(value).expect("kernel coefficient overflow"))
            .collect();
        for row in 0..columns[0].len() {
            assert_eq!(
                columns
                    .iter()
                    .zip(&integers)
                    .map(|(column, coefficient)| column[row] * coefficient)
                    .sum::<i64>(),
                0
            );
        }
        result.push(integers);
    }
    result
}

fn columns_rank(vectors: &[Vec<i64>]) -> usize {
    if vectors.is_empty() {
        0
    } else {
        rational_rank(vectors)
    }
}

fn verify_raw_kernel_is_local(columns: &[Vec<i64>]) {
    let kernel = primitive_integer_kernel(columns);
    assert_eq!(kernel.len(), 2);
    let local: Vec<Vec<i64>> = local_relations().into_iter().map(Vec::from).collect();
    assert_eq!(columns_rank(&local), 2);
    let mut union = local;
    union.extend(kernel);
    assert_eq!(columns_rank(&union), 2);
}

fn spanning_tree_masks() -> Vec<u8> {
    let mut trees = Vec::new();
    for mask in 0_u8..(1 << EDGES) {
        if mask.count_ones() != 4 {
            continue;
        }
        let mut parent: [usize; VERTICES] = std::array::from_fn(|vertex| vertex);
        fn find(parent: &mut [usize; VERTICES], vertex: usize) -> usize {
            if parent[vertex] != vertex {
                parent[vertex] = find(parent, parent[vertex]);
            }
            parent[vertex]
        }
        for edge in 0..EDGES {
            if mask & (1 << edge) != 0 {
                let (left, right) = edge_vertices(edge);
                let left_root = find(&mut parent, left);
                let right_root = find(&mut parent, right);
                parent[right_root] = left_root;
            }
        }
        let roots: BTreeSet<_> = (0..VERTICES)
            .map(|vertex| find(&mut parent, vertex))
            .collect();
        if roots.len() == 1 {
            trees.push(mask);
        }
    }
    assert_eq!(trees.len(), 12);
    trees
}

fn incidence(chain: Chain6, orientation: u8) -> [i64; VERTICES] {
    let mut result = [0; VERTICES];
    for (edge, coefficient) in chain.into_iter().enumerate() {
        let (canonical_tail, canonical_head) = edge_vertices(edge);
        let (tail, head) = if orientation & (1 << edge) == 0 {
            (canonical_tail, canonical_head)
        } else {
            (canonical_head, canonical_tail)
        };
        result[tail] -= coefficient;
        result[head] += coefficient;
    }
    result
}

fn tree_lift(tree: u8, wanted: [i64; VERTICES], orientation: u8) -> Chain6 {
    let tree_edges: Vec<_> = (0..EDGES)
        .filter(|edge| tree & (1 << edge) != 0)
        .collect();
    let mut solutions = Vec::new();
    for code in 0..3_usize.pow(4) {
        let mut rest = code;
        let mut candidate = [0; EDGES];
        for &edge in &tree_edges {
            candidate[edge] = i64::try_from(rest % 3).expect("ternary digit") - 1;
            rest /= 3;
        }
        if incidence(candidate, orientation) == wanted {
            solutions.push(candidate);
        }
    }
    assert_eq!(solutions.len(), 1);
    solutions[0]
}

fn support(chain: Chain6) -> Vec<usize> {
    (0..EDGES).filter(|&edge| chain[edge] != 0).collect()
}

fn fundamental_relation(cycle_support: &[usize]) -> [i64; WARD_MARKS] {
    assert_eq!(cycle_support.len(), 4);
    let marks = ward_marks();
    let mut local_marks = Vec::new();
    for vertex in 0..VERTICES {
        let incident: Vec<_> = cycle_support
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
                .filter(|(_, mark)| support(ward_differential(**mark).contacts) == incident)
                .map(|(index, _)| index)
                .collect();
            assert_eq!(candidates.len(), 1);
            local_marks.push(candidates[0]);
        }
    }
    assert_eq!(local_marks.len(), 4);
    let mut solutions = Vec::new();
    for signs in 0_u8..16 {
        let mut coefficients = [0; WARD_MARKS];
        for (position, &mark) in local_marks.iter().enumerate() {
            coefficients[mark] = if signs & (1 << position) == 0 { 1 } else { -1 };
        }
        if apply_raw(coefficients).contacts == [0; EDGES] {
            solutions.push(coefficients);
        }
    }
    assert_eq!(solutions.len(), 2);
    solutions.sort();
    solutions[1]
}

fn nonzero_count<const N: usize>(value: [i64; N]) -> usize {
    value.into_iter().filter(|&entry| entry != 0).count()
}

#[derive(Default)]
struct CycleAudit {
    base_cycles: usize,
    orientation_expanded_cycles: usize,
    contact_failures: usize,
    even_failures: usize,
    odd_failures: usize,
    minimum_odd_support: usize,
}

fn audit_cycles() -> CycleAudit {
    let trees = spanning_tree_masks();
    let mut audit = CycleAudit {
        minimum_odd_support: usize::MAX,
        ..CycleAudit::default()
    };
    for orientation in 0_u8..(1 << EDGES) {
        for &tree in &trees {
            for chord in 0..EDGES {
                if tree & (1 << chord) != 0 {
                    continue;
                }
                let mut unit = [0; EDGES];
                unit[chord] = 1;
                let lifted = tree_lift(tree, incidence(unit, orientation), orientation);
                let cycle: Chain6 = std::array::from_fn(|edge| unit[edge] - lifted[edge]);
                assert_eq!(incidence(cycle, orientation), [0; VERTICES]);
                assert_eq!(support(cycle).len(), 4);
                let relation = fundamental_relation(&support(cycle));
                let raw = apply_raw(relation);
                if raw.contacts != [0; EDGES] {
                    audit.contact_failures += 1;
                }
                let even = glue(raw, Gluing::Even);
                if even.longitudinal != [0; EDGES] {
                    audit.even_failures += 1;
                }
                let odd = glue(raw, Gluing::Odd);
                let odd_support = nonzero_count(odd.longitudinal);
                if odd_support != 0 {
                    audit.odd_failures += 1;
                    audit.minimum_odd_support = audit.minimum_odd_support.min(odd_support);
                }
                audit.orientation_expanded_cycles += 1;
                if orientation == 0 {
                    audit.base_cycles += 1;
                }
            }
        }
    }
    assert_eq!(audit.base_cycles, 24);
    assert_eq!(audit.orientation_expanded_cycles, 64 * 24);
    assert_eq!(audit.contact_failures, 0);
    assert_eq!(audit.even_failures, 0);
    assert_eq!(audit.odd_failures, audit.orientation_expanded_cycles);
    audit
}

const ROAD_PERMUTATIONS: [[usize; 3]; 6] = [
    [0, 1, 2],
    [1, 2, 0],
    [2, 0, 1],
    [0, 2, 1],
    [2, 1, 0],
    [1, 0, 2],
];

fn permutation_sign(permutation: [usize; 3]) -> i64 {
    let inversions = (0..3)
        .flat_map(|left| ((left + 1)..3).map(move |right| (left, right)))
        .filter(|&(left, right)| permutation[left] > permutation[right])
        .count();
    if inversions % 2 == 0 { 1 } else { -1 }
}

fn map_edge(edge: usize, core_swap: bool, roads: [usize; 3]) -> usize {
    let core = edge % 2;
    let road = edge / 2;
    edge_slot(if core_swap { 1 - core } else { core }, roads[road])
}

fn map_mark(mark: WardMark, core_swap: bool, roads: [usize; 3]) -> (WardMark, i64) {
    match mark {
        WardMark::Left {
            core,
            incoming_road,
        } => (
            WardMark::Left {
                core: if core_swap { 1 - core } else { core },
                incoming_road: roads[incoming_road],
            },
            permutation_sign(roads),
        ),
        WardMark::RightExternal { road } => (
            WardMark::RightExternal { road: roads[road] },
            if core_swap { -1 } else { 1 },
        ),
    }
}

fn permute_raw(value: DegreeZero, core_swap: bool, roads: [usize; 3]) -> DegreeZero {
    let mut result = DegreeZero::zero();
    for edge in 0..EDGES {
        let mapped = map_edge(edge, core_swap, roads);
        result.contacts[mapped] += value.contacts[edge];
        result.exits[2 * mapped] += value.exits[2 * edge];
        result.exits[2 * mapped + 1] += value.exits[2 * edge + 1];
    }
    result
}

fn permute_glued(
    value: GluedDegreeZero,
    core_swap: bool,
    roads: [usize; 3],
) -> GluedDegreeZero {
    let mut result = GluedDegreeZero {
        contacts: [0; EDGES],
        longitudinal: [0; EDGES],
    };
    for edge in 0..EDGES {
        let mapped = map_edge(edge, core_swap, roads);
        result.contacts[mapped] += value.contacts[edge];
        result.longitudinal[mapped] += value.longitudinal[edge];
    }
    result
}

fn audit_covariance() -> (usize, usize, usize) {
    let mut raw_checks = 0;
    let mut even_checks = 0;
    let mut odd_checks = 0;
    for core_swap in [false, true] {
        for roads in ROAD_PERMUTATIONS {
            for mark in ward_marks() {
                let (mapped_mark, coefficient) = map_mark(mark, core_swap, roads);
                let mut expected = DegreeZero::zero();
                expected.add_scaled(ward_differential(mapped_mark), coefficient);
                let actual = permute_raw(ward_differential(mark), core_swap, roads);
                assert_eq!(actual, expected);
                raw_checks += 1;
                for convention in [Gluing::Even, Gluing::Odd] {
                    assert_eq!(
                        glue(actual, convention),
                        permute_glued(
                            glue(ward_differential(mark), convention),
                            core_swap,
                            roads
                        )
                    );
                    match convention {
                        Gluing::Even => even_checks += 1,
                        Gluing::Odd => odd_checks += 1,
                    }
                }
            }
        }
    }
    assert_eq!(raw_checks, 12 * WARD_MARKS);
    assert_eq!(even_checks, raw_checks);
    assert_eq!(odd_checks, raw_checks);
    (raw_checks, even_checks, odd_checks)
}

fn audit_momentum_orientation() -> (usize, usize) {
    let mut even_tensor_checks = 0;
    let mut odd_tensor_failures = 0;
    for orientation in 0_u8..(1 << EDGES) {
        for edge in 0..EDGES {
            let tail_sign: i64 = if orientation & (1 << edge) == 0 { 1 } else { -1 };
            let head_sign = -tail_sign;
            // Only the scalar parity multiplying k tensor k is needed: both
            // endpoint projectors have coefficient (+1) after k -> -k.
            let tail_projector = tail_sign * tail_sign;
            let head_projector = head_sign * head_sign;
            assert_eq!(tail_projector, head_projector);
            even_tensor_checks += 1;
            if tail_projector != -head_projector {
                odd_tensor_failures += 1;
            }
        }
    }
    assert_eq!(even_tensor_checks, 64 * EDGES);
    assert_eq!(odd_tensor_failures, even_tensor_checks);
    (even_tensor_checks, odd_tensor_failures)
}

fn minimum_nonlocal_even_kernel_support() -> (usize, [i64; WARD_MARKS]) {
    let local = local_relations();
    let mut best: Option<(usize, [i64; WARD_MARKS])> = None;
    for code in 1..3_usize.pow(WARD_MARKS as u32) {
        let mut rest = code;
        let coefficients = std::array::from_fn(|_| {
            let value = i64::try_from(rest % 3).expect("ternary digit") - 1;
            rest /= 3;
            value
        });
        let raw = apply_raw(coefficients);
        let even = glue(raw, Gluing::Even);
        if even.contacts != [0; EDGES] || even.longitudinal != [0; EDGES] {
            continue;
        }
        let only_local = (-1_i64..=1).any(|first| {
            (-1_i64..=1).any(|second| {
                std::array::from_fn::<_, WARD_MARKS, _>(|index| {
                    first * local[0][index] + second * local[1][index]
                }) == coefficients
            })
        });
        if only_local {
            continue;
        }
        let support = nonzero_count(coefficients);
        if best.as_ref().is_none_or(|current| support < current.0) {
            best = Some((support, coefficients));
        }
    }
    best.expect("no nonlocal physical kernel class")
}

fn main() {
    for relation in local_relations() {
        assert_eq!(apply_raw(relation), DegreeZero::zero());
    }

    let contact_raw = raw_columns(None, true);
    let unglued_raw = raw_columns(None, false);
    let even_raw = raw_columns(Some(Gluing::Even), false);
    let odd_raw = raw_columns(Some(Gluing::Odd), false);
    verify_raw_kernel_is_local(&unglued_raw);
    verify_raw_kernel_is_local(&odd_raw);

    let contact = quotient_columns(&contact_raw);
    let unglued = quotient_columns(&unglued_raw);
    let even = quotient_columns(&even_raw);
    let odd = quotient_columns(&odd_raw);

    let contact_rank = rational_rank(&contact);
    let unglued_rank = rational_rank(&unglued);
    let even_rank = rational_rank(&even);
    let odd_rank = rational_rank(&odd);
    let contact_kernel = primitive_integer_kernel(&contact);
    let unglued_kernel = primitive_integer_kernel(&unglued);
    let even_kernel = primitive_integer_kernel(&even);
    let odd_kernel = primitive_integer_kernel(&odd);

    assert_eq!((contact_rank, contact_kernel.len()), (5, 2));
    assert_eq!((unglued_rank, unglued_kernel.len()), (7, 0));
    assert_eq!((even_rank, even_kernel.len()), (5, 2));
    assert_eq!((odd_rank, odd_kernel.len()), (7, 0));
    assert_eq!(even_kernel, contact_kernel);

    let cycles = audit_cycles();
    let (raw_covariance, even_covariance, odd_covariance) = audit_covariance();
    let (orientation_checks, odd_tensor_failures) = audit_momentum_orientation();
    let (minimum_support, witness) = minimum_nonlocal_even_kernel_support();
    assert_eq!(minimum_support, 4);

    println!("Longitudinal internal-edge gluing certificate");
    println!("================================================");
    println!("  raw Ward marks / cyclic relations:       {WARD_MARKS}/2");
    println!("  quotient degree-one rank:                {}", QUOTIENT_MARKS.len());
    println!("  raw contact+12-exit rank/kernel:         {}/{}", rational_rank(&unglued_raw), primitive_integer_kernel(&unglued_raw).len());
    println!("  quotient contact-only Z=Q rank/kernel:   {contact_rank}/{}", contact_kernel.len());
    println!("  quotient unglued Z=Q rank/kernel:        {unglued_rank}/{}", unglued_kernel.len());
    println!("  quotient even-glued Z=Q rank/kernel:     {even_rank}/{}", even_kernel.len());
    println!("  quotient odd-glued Z=Q rank/kernel:      {odd_rank}/{}", odd_kernel.len());
    println!("  even-glued primitive Z-kernel basis:     {even_kernel:?}");
    println!("  base tree/chord cycles:                  {}", cycles.base_cycles);
    println!("  orientation-expanded cycle checks:       {}", cycles.orientation_expanded_cycles);
    println!("  contact/even telescope failures:         {}/{}", cycles.contact_failures, cycles.even_failures);
    println!("  odd-convention telescope failures:       {}", cycles.odd_failures);
    println!("  smallest odd remainder edge support:     {}", cycles.minimum_odd_support);
    println!("  S2xD3 raw/even/odd covariance checks:    {raw_covariance}/{even_covariance}/{odd_covariance}");
    println!("  k -> -k projector-even checks:           {orientation_checks}");
    println!("  opposite-sign tensor mismatches:         {odd_tensor_failures}");
    println!("  smallest surviving closed class support: {minimum_support}");
    println!("  smallest surviving closed class:         {witness:?}");
    println!();
    println!("VERDICT");
    println!("  Q(-k)=Q(k) selects equal endpoint exits; all 24 fundamental chord relations then telescope");
    println!("  the opposite endpoint sign is tensorially wrong and obstructs every chord relation");
    println!("  the equal-endpoint quotient removes the degree-zero longitudinal remainder but leaves a rank-two closed Ward kernel");
    println!("  promoting this algebraic quotient to a physical chain map still assumes sign-compatible propagator sewing");
}
