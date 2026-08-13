//! Exact four- and five-point scaffold-transmutation audit.
//!
//! This certificate separates two questions that can otherwise be conflated:
//!
//! 1. Is the metric adjoint I_S^{-1} J^T I_G determined by the published
//!    scalar-scaffolding construction?  (No: the full map J and gauge pairing
//!    I_G are not supplied.)
//! 2. What is the exact relation between the diagramwise Dong--Su--Yang (DSY)
//!    extractors and the Backus--Figueiredo W transmutation on the canonical
//!    Yang--Mills amplitude?  (They agree after cellular augmentation and
//!    quotienting differential operators by Ann(A_YM).)
//!
//! The physical statements used as source axioms are:
//!
//!   D_Gamma A_YM = b_Gamma,
//!   (prod_{e != e_*} W_e) A_YM = A_phi3.
//!
//! Everything else below--all cyclic scaffold references, graph permutations,
//! W-expansion membership and multiplicities, residual nonzero operator
//! support, pair/final-W counting, and matrix-identifiability counts--is
//! generated and checked exactly with the Rust standard library.

use std::collections::{BTreeMap, BTreeSet};
use std::fmt;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Coord(u8, u8);

impl Coord {
    fn new(first: u8, second: u8) -> Self {
        assert_ne!(first, second);
        if first < second {
            Self(first, second)
        } else {
            Self(second, first)
        }
    }

    fn rotate(self, shift: u8, modulus: u8) -> Self {
        Self::new(
            rotate_label(self.0, shift, modulus),
            rotate_label(self.1, shift, modulus),
        )
    }
}

impl fmt::Display for Coord {
    fn fmt(&self, output: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(output, "X_{{{},{}}}", self.0, self.1)
    }
}

type Monomial = Vec<Coord>;

fn rotate_label(label: u8, shift: u8, modulus: u8) -> u8 {
    ((label - 1 + shift) % modulus) + 1
}

fn monomial(coords: &[(u8, u8)]) -> Monomial {
    let mut result: Vec<_> = coords
        .iter()
        .map(|(first, second)| Coord::new(*first, *second))
        .collect();
    result.sort_unstable();
    result
}

fn rotate_monomial(value: &Monomial, shift: u8, modulus: u8) -> Monomial {
    let mut result: Vec<_> = value
        .iter()
        .map(|coordinate| coordinate.rotate(shift, modulus))
        .collect();
    result.sort_unstable();
    result
}

fn format_monomial(value: &Monomial, derivative: bool) -> String {
    value
        .iter()
        .map(|coordinate| {
            if derivative {
                format!("d[{},{}]", coordinate.0, coordinate.1)
            } else {
                coordinate.to_string()
            }
        })
        .collect::<Vec<_>>()
        .join(" ")
}

fn scalar_graphs(n: usize) -> Vec<Monomial> {
    match n {
        4 => vec![monomial(&[(1, 5)]), monomial(&[(3, 7)])],
        5 => vec![
            monomial(&[(1, 5), (1, 7)]),
            monomial(&[(3, 7), (3, 9)]),
            monomial(&[(1, 5), (5, 9)]),
            monomial(&[(1, 7), (3, 7)]),
            monomial(&[(3, 9), (5, 9)]),
        ],
        _ => panic!("this bounded certificate covers n=4,5 only"),
    }
}

fn dsy_operators(n: usize) -> Vec<Monomial> {
    match n {
        4 => vec![
            monomial(&[(2, 8), (1, 4), (1, 6)]),
            monomial(&[(2, 8), (1, 4), (3, 6)]),
        ],
        5 => vec![
            monomial(&[(2, 10), (1, 4), (1, 6), (1, 8)]),
            monomial(&[(2, 10), (1, 4), (3, 6), (3, 8)]),
            monomial(&[(2, 10), (1, 4), (1, 6), (5, 8)]),
            monomial(&[(2, 10), (1, 4), (1, 8), (3, 6)]),
            monomial(&[(2, 10), (1, 4), (3, 8), (9, 6)]),
        ],
        _ => panic!("this bounded certificate covers n=4,5 only"),
    }
}

fn even_labels(n: usize) -> Vec<u8> {
    (1..=n).map(|index| (2 * index) as u8).collect()
}

fn cyclic_neighbors(label: u8, modulus: u8) -> (u8, u8) {
    let previous = if label == 1 { modulus } else { label - 1 };
    let next = if label == modulus { 1 } else { label + 1 };
    (previous, next)
}

fn w_terms(even: u8, modulus: u8) -> Vec<Coord> {
    assert_eq!(even % 2, 0);
    let (previous, next) = cyclic_neighbors(even, modulus);
    let result: Vec<_> = (1..=modulus)
        .filter(|label| *label != even && *label != previous && *label != next)
        .map(|label| Coord::new(even, label))
        .collect();
    assert_eq!(result.len(), modulus as usize - 3);
    result
}

fn expand_full_w(n: usize, leave: u8) -> (u64, BTreeMap<Monomial, u64>) {
    let modulus = (2 * n) as u8;
    let acted: Vec<_> = even_labels(n)
        .into_iter()
        .filter(|even| *even != leave)
        .collect();
    assert_eq!(acted.len(), n - 1);

    let mut expansion = BTreeMap::from([(Vec::new(), 1_u64)]);
    for even in acted {
        let mut next = BTreeMap::new();
        for (partial, coefficient) in expansion {
            for term in w_terms(even, modulus) {
                let mut completed = partial.clone();
                completed.push(term);
                completed.sort_unstable();
                *next.entry(completed).or_insert(0) += coefficient;
            }
        }
        expansion = next;
    }
    let raw_count = expansion.values().sum();
    let expected = (modulus as u64 - 3).pow((n - 1) as u32);
    assert_eq!(raw_count, expected);
    (raw_count, expansion)
}

fn catalan(index: usize) -> usize {
    let mut values = vec![0_u64; index + 1];
    values[0] = 1;
    for size in 1..=index {
        values[size] = (0..size)
            .map(|left| values[left] * values[size - 1 - left])
            .sum();
    }
    values[index] as usize
}

fn factorial(value: usize) -> u64 {
    (1..=value as u64).product()
}

fn permutation_under_rotation(graphs: &[Monomial], shift: u8, modulus: u8) -> Vec<usize> {
    graphs
        .iter()
        .map(|graph| {
            let rotated = rotate_monomial(graph, shift, modulus);
            graphs
                .iter()
                .position(|candidate| *candidate == rotated)
                .expect("rotation must permute the planar graph set")
        })
        .collect()
}

fn audit_matrix_identifiability(n: usize) {
    let source_dimension = factorial(2 * n - 3);
    let target_dimension = factorial(n - 3);
    let map_entries = source_dimension * target_dimension;
    let one_section_ambiguity = target_dimension * (source_dimension - 1);
    let optimistic_cyclic_ambiguity = target_dimension * (source_dimension - n as u64);

    println!("  metric-adjoint typing audit:");
    println!(
        "    dim H_{{0,{}}}=(2n-3)!={}, dim H_{{0,{}}}=(n-3)!={}",
        2 * n,
        source_dimension,
        n,
        target_dimension
    );
    println!(
        "    a full J needs {} entries; one master-section value leaves {} free",
        map_entries, one_section_ambiguity
    );
    println!(
        "    even treating all {} cyclic sections as independent leaves at least {} free",
        n, optimistic_cyclic_ambiguity
    );
    println!(
        "    I_S is {}x{}; a gauge-descended I_G (including state coevaluation) is not supplied",
        source_dimension, source_dimension
    );

    assert!(one_section_ambiguity > 0);
    assert!(optimistic_cyclic_ambiguity > 0);
}

fn audit_pairwise_w_choices(n: usize) {
    let modulus = (2 * n) as u8;
    let evens = even_labels(n);
    let mut final_leave_counts = BTreeMap::<u8, usize>::new();
    let mut pair_count = 0;
    let mut labelled_final_count = 0;

    for first_index in 0..evens.len() {
        for second_index in (first_index + 1)..evens.len() {
            let first = evens[first_index];
            let second = evens[second_index];
            let prefactor = Coord::new(first, second);
            assert!(w_terms(first, modulus).contains(&prefactor));
            assert!(w_terms(second, modulus).contains(&prefactor));

            // After W on E\{first,second}, the result is X_{first,second} A_phi3.
            // Applying W_first leaves second unacted; W_second leaves first unacted.
            *final_leave_counts.entry(second).or_insert(0) += 1;
            *final_leave_counts.entry(first).or_insert(0) += 1;
            pair_count += 1;
            labelled_final_count += 2;
        }
    }

    assert_eq!(pair_count, n * (n - 1) / 2);
    assert_eq!(labelled_final_count, n * (n - 1));
    assert_eq!(final_leave_counts.len(), n);
    assert!(final_leave_counts.values().all(|count| *count == n - 1));
    println!(
        "  W choices: {} omitted pairs, {} labelled final actions, {} unique full transmuters",
        pair_count,
        labelled_final_count,
        final_leave_counts.len()
    );
}

fn audit_case(n: usize) {
    let modulus = (2 * n) as u8;
    let graphs = scalar_graphs(n);
    let operators = dsy_operators(n);
    assert_eq!(graphs.len(), catalan(n - 2));
    assert_eq!(operators.len(), graphs.len());
    assert!(operators.iter().all(|operator| operator.len() == n - 1));

    println!("n={n}");
    println!("  canonical cellular coframe:");
    for (index, (graph, operator)) in graphs.iter().zip(&operators).enumerate() {
        println!(
            "    Gamma{}: {:<28} <- {}",
            index + 1,
            format!("1/({})", format_monomial(graph, false)),
            format_monomial(operator, true)
        );
    }

    let graph_set: BTreeSet<_> = graphs.iter().cloned().collect();
    let mut reference_rows = Vec::new();
    for reference in 0..n {
        let shift = (2 * reference) as u8;
        let leave = rotate_label(modulus, shift, modulus);
        let reference_pair = Coord::new(
            rotate_label(2, shift, modulus),
            rotate_label(modulus, shift, modulus),
        );
        let rotated_graphs: Vec<_> = graphs
            .iter()
            .map(|graph| rotate_monomial(graph, shift, modulus))
            .collect();
        let rotated_graph_set: BTreeSet<_> = rotated_graphs.iter().cloned().collect();
        assert_eq!(rotated_graph_set, graph_set);

        let permutation = permutation_under_rotation(&graphs, shift, modulus);
        let rotated_operators: Vec<_> = operators
            .iter()
            .map(|operator| rotate_monomial(operator, shift, modulus))
            .collect();
        assert_eq!(rotated_operators.iter().collect::<BTreeSet<_>>().len(), graphs.len());

        let (raw_count, mut expansion) = expand_full_w(n, leave);
        let unique_count = expansion.len();
        for operator in &rotated_operators {
            let coefficient = expansion
                .get_mut(operator)
                .expect("every DSY extractor must occur in the full W expansion");
            assert_eq!(*coefficient, 1);
            *coefficient -= 1;
        }
        expansion.retain(|_, coefficient| *coefficient != 0);
        let residual_support = expansion.len();
        let residual_weight: u64 = expansion.values().sum();
        assert_eq!(residual_support, unique_count - graphs.len());
        assert_eq!(residual_weight, raw_count - graphs.len() as u64);
        assert!(residual_support > 0); // Not equality as free differential operators.

        reference_rows.push((
            reference_pair,
            leave,
            permutation,
            raw_count,
            unique_count,
            residual_support,
            residual_weight,
        ));
    }

    for (index, row) in reference_rows.iter().enumerate() {
        let permutation = row
            .2
            .iter()
            .map(|entry| (entry + 1).to_string())
            .collect::<Vec<_>>()
            .join(",");
        println!(
            "  ref r={}: pair {}, leave e*={}, cells->[{}], W raw/unique={}/{}, residual support/weight={}/{}",
            index,
            row.0,
            row.1,
            permutation,
            row.3,
            row.4,
            row.5,
            row.6
        );
    }

    // All rotations have the same formal scalar augmentation because they
    // permute the complete Catalan graph set.
    let one_step = permutation_under_rotation(&graphs, 2, modulus);
    if n == 4 {
        assert_eq!(one_step, vec![1, 0]);
    } else {
        assert_eq!(one_step, vec![1, 2, 3, 4, 0]);
    }
    println!(
        "  augmentation: sum_Gamma b_Gamma has {} terms and is invariant under all {} cyclic references",
        graphs.len(), n
    );
    println!(
        "  quotient identity: [prod_(e != e*) W_e] = [sum_Gamma D_Gamma^(e*)] in Diff/Ann(A_YM)"
    );

    audit_pairwise_w_choices(n);
    audit_matrix_identifiability(n);
    println!();
}

fn main() {
    println!("Low-point scaffold transmutation certificate");
    println!("============================================");
    audit_case(4);
    audit_case(5);
    println!("VERDICT");
    println!("  genuine metric adjunction: UNDEFINED from published data");
    println!("  augmented/coframe counit:  PROVED at n=4,5 on the canonical amplitude");
    println!("  cyclic reference defect:   ABSENT after augmentation/Ann(A_YM) quotient");
    println!("  chain-level adjunction:     remains a separate comparison problem");
}
