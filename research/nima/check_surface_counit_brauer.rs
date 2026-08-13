//! State-layer certificate for the all-topology transmutation counit.
//!
//! Polarization contractions form the Brauer category: composing two perfect
//! matchings can create closed circuits, and every closed circuit evaluates to
//! the formal dimension D.  The scalar counit must therefore be resolved before
//! summing contraction patterns and must send each *individual* circuit D to 1.
//!
//! This program checks three facts independently of any amplitude formula:
//!
//! 1. the number of circuits created by composition is a strict additive
//!    2-cocycle (the two parenthesizations of a triple composite create the same
//!    total number of circuits);
//! 2. the cocycle is compatible with disjoint union and cyclic relabelling;
//! 3. the published one-loop one-point surface integrand has precisely one such
//!    circuit: W_2 I_1 = (1-Delta)/X_(1,p) = D/X_(1,p) when Delta=1-D.
//!
//! Consequently base change along Z[D] -> Z, D |-> 1 is a cyclic monoidal
//! augmentation of the resolved contraction category.  The certificate does
//! not by itself construct the derived modular envelope or prove descent to a
//! chosen physical surface-function quotient; those are separated in entry 47.

use std::collections::BTreeSet;

#[derive(Clone, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Matching {
    source: usize,
    target: usize,
    pairs: Vec<(usize, usize)>,
}

impl Matching {
    fn new(source: usize, target: usize, pairs: Vec<(usize, usize)>) -> Self {
        let total = source + target;
        assert_eq!(total % 2, 0);
        assert_eq!(pairs.len() * 2, total);

        let mut normalized = Vec::with_capacity(pairs.len());
        let mut used = BTreeSet::new();
        for (a, b) in pairs {
            assert!(a < total && b < total && a != b);
            assert!(used.insert(a));
            assert!(used.insert(b));
            normalized.push(if a < b { (a, b) } else { (b, a) });
        }
        normalized.sort_unstable();
        Self {
            source,
            target,
            pairs: normalized,
        }
    }
}

fn perfect_matchings(source: usize, target: usize) -> Vec<Matching> {
    let total = source + target;
    if total % 2 == 1 {
        return Vec::new();
    }

    fn recurse(
        remaining: &mut Vec<usize>,
        pairs: &mut Vec<(usize, usize)>,
        out: &mut Vec<Vec<(usize, usize)>>,
    ) {
        if remaining.is_empty() {
            out.push(pairs.clone());
            return;
        }
        let first = remaining.remove(0);
        for index in 0..remaining.len() {
            let second = remaining.remove(index);
            pairs.push((first, second));
            recurse(remaining, pairs, out);
            pairs.pop();
            remaining.insert(index, second);
        }
        remaining.insert(0, first);
    }

    let mut raw = Vec::new();
    recurse(&mut (0..total).collect(), &mut Vec::new(), &mut raw);
    raw.into_iter()
        .map(|pairs| Matching::new(source, target, pairs))
        .collect()
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct Composite {
    matching: Matching,
    new_circuits: usize,
}

/// Compose `first : m -> n` followed by `second : n -> p`.
fn compose(first: &Matching, second: &Matching) -> Composite {
    assert_eq!(first.target, second.source);
    let m = first.source;
    let n = first.target;
    let p = second.target;
    let total = m + n + p;
    let mut adjacency = vec![Vec::<usize>::new(); total];

    let map_first = |vertex: usize| {
        if vertex < m {
            vertex
        } else {
            m + vertex - m
        }
    };
    let map_second = |vertex: usize| {
        if vertex < n {
            m + vertex
        } else {
            m + n + vertex - n
        }
    };
    let mut add_edge = |a: usize, b: usize| {
        adjacency[a].push(b);
        adjacency[b].push(a);
    };
    for &(a, b) in &first.pairs {
        add_edge(map_first(a), map_first(b));
    }
    for &(a, b) in &second.pairs {
        add_edge(map_second(a), map_second(b));
    }

    let is_external = |vertex: usize| vertex < m || vertex >= m + n;
    let to_result = |vertex: usize| {
        if vertex < m {
            vertex
        } else {
            m + vertex - (m + n)
        }
    };

    let mut seen = vec![false; total];
    let mut result_pairs = Vec::new();
    let mut new_circuits = 0;
    for start in 0..total {
        if seen[start] || adjacency[start].is_empty() {
            continue;
        }
        let mut stack = vec![start];
        seen[start] = true;
        let mut external = Vec::new();
        while let Some(vertex) = stack.pop() {
            if is_external(vertex) {
                external.push(vertex);
            }
            for &next in &adjacency[vertex] {
                if !seen[next] {
                    seen[next] = true;
                    stack.push(next);
                }
            }
        }
        match external.len() {
            0 => new_circuits += 1,
            2 => result_pairs.push((to_result(external[0]), to_result(external[1]))),
            count => panic!("Brauer component has {count} external endpoints"),
        }
    }

    Composite {
        matching: Matching::new(m, p, result_pairs),
        new_circuits,
    }
}

fn tensor(first: &Matching, second: &Matching) -> Matching {
    let source = first.source + second.source;
    let target = first.target + second.target;
    let mut pairs = Vec::new();

    let map_first = |vertex: usize| {
        if vertex < first.source {
            vertex
        } else {
            source + vertex - first.source
        }
    };
    let map_second = |vertex: usize| {
        if vertex < second.source {
            first.source + vertex
        } else {
            source + first.target + vertex - second.source
        }
    };
    pairs.extend(
        first
            .pairs
            .iter()
            .map(|&(a, b)| (map_first(a), map_first(b))),
    );
    pairs.extend(
        second
            .pairs
            .iter()
            .map(|&(a, b)| (map_second(a), map_second(b))),
    );
    Matching::new(source, target, pairs)
}

fn cyclic_relabel(matching: &Matching, source_shift: usize, target_shift: usize) -> Matching {
    let map = |vertex: usize| {
        if vertex < matching.source {
            if matching.source == 0 {
                vertex
            } else {
                (vertex + source_shift) % matching.source
            }
        } else if matching.target == 0 {
            vertex
        } else {
            matching.source + (vertex - matching.source + target_shift) % matching.target
        }
    };
    Matching::new(
        matching.source,
        matching.target,
        matching
            .pairs
            .iter()
            .map(|&(a, b)| (map(a), map(b)))
            .collect(),
    )
}

fn audit_associativity_and_cocycle() -> usize {
    let mut triples = 0;
    for m in 0..=3 {
        for n in 0..=3 {
            for p in 0..=3 {
                for q in 0..=3 {
                    let fs = perfect_matchings(m, n);
                    let gs = perfect_matchings(n, p);
                    let hs = perfect_matchings(p, q);
                    for f in &fs {
                        for g in &gs {
                            for h in &hs {
                                let fg = compose(f, g);
                                let left = compose(&fg.matching, h);
                                let gh = compose(g, h);
                                let right = compose(f, &gh.matching);
                                assert_eq!(left.matching, right.matching);
                                assert_eq!(
                                    fg.new_circuits + left.new_circuits,
                                    gh.new_circuits + right.new_circuits
                                );
                                triples += 1;
                            }
                        }
                    }
                }
            }
        }
    }
    triples
}

fn audit_cyclic_equivariance() -> usize {
    let mut squares = 0;
    for m in 0..=3 {
        for n in 0..=3 {
            for p in 0..=3 {
                for f in perfect_matchings(m, n) {
                    for g in perfect_matchings(n, p) {
                        let composite = compose(&f, &g);
                        let source_shifts = 0..m.max(1);
                        let middle_shifts = 0..n.max(1);
                        let target_shifts = 0..p.max(1);
                        for source_shift in source_shifts.clone() {
                            for middle_shift in middle_shifts.clone() {
                                for target_shift in target_shifts.clone() {
                                    let moved = compose(
                                        &cyclic_relabel(&f, source_shift, middle_shift),
                                        &cyclic_relabel(&g, middle_shift, target_shift),
                                    );
                                    assert_eq!(moved.new_circuits, composite.new_circuits);
                                    assert_eq!(
                                        moved.matching,
                                        cyclic_relabel(
                                            &composite.matching,
                                            source_shift,
                                            target_shift
                                        )
                                    );
                                    squares += 1;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    squares
}

fn audit_tensor_interchange() -> usize {
    let mut squares = 0;
    for m1 in 0..=2 {
        for n1 in 0..=2 {
            for p1 in 0..=2 {
                for m2 in 0..=2 {
                    for n2 in 0..=2 {
                        for p2 in 0..=2 {
                            for f1 in perfect_matchings(m1, n1) {
                                for g1 in perfect_matchings(n1, p1) {
                                    for f2 in perfect_matchings(m2, n2) {
                                        for g2 in perfect_matchings(n2, p2) {
                                            let left =
                                                compose(&tensor(&f1, &f2), &tensor(&g1, &g2));
                                            let first = compose(&f1, &g1);
                                            let second = compose(&f2, &g2);
                                            assert_eq!(
                                                left.matching,
                                                tensor(&first.matching, &second.matching)
                                            );
                                            assert_eq!(
                                                left.new_circuits,
                                                first.new_circuits + second.new_circuits
                                            );
                                            squares += 1;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    squares
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LinearD {
    constant: i32,
    d: i32,
}

impl LinearD {
    fn minus(self, other: Self) -> Self {
        Self {
            constant: self.constant - other.constant,
            d: self.d - other.d,
        }
    }
}

fn audit_one_loop_surface_cell() {
    let one = LinearD { constant: 1, d: 0 };
    let two = LinearD { constant: 2, d: 0 };
    let dimension = LinearD { constant: 0, d: 1 };

    // Carrôlo--Figueiredo: Delta_gamma = nu_gamma - D for both curve types.
    for nu in [0, 1] {
        let nu_poly = LinearD { constant: nu, d: 0 };
        let delta = LinearD {
            constant: nu,
            d: -1,
        };
        assert_eq!(nu_poly.minus(delta), dimension);
    }

    // Backus--Figueiredo Eq. (15):
    // I_1 = [2 X_12 - (1+Delta)(X_2p-X_1p)] / X_1p.
    // W_2 = d/dX_12 + d/dX_21 + d/dX_2p, so its numerator is
    // 2 - (1+Delta) = 1-Delta.  For the planar puncture nu=1.
    let planar_delta = LinearD { constant: 1, d: -1 };
    let derivative_numerator = two.minus(LinearD {
        constant: one.constant + planar_delta.constant,
        d: one.d + planar_delta.d,
    });
    assert_eq!(derivative_numerator, dimension);

    // The elementary cup followed by cap is exactly one Brauer circuit.
    let cup = Matching::new(0, 2, vec![(0, 1)]);
    let cap = Matching::new(2, 0, vec![(0, 1)]);
    let trace = compose(&cup, &cap);
    assert_eq!(trace.matching, Matching::new(0, 0, Vec::new()));
    assert_eq!(trace.new_circuits, 1);
}

fn main() {
    audit_one_loop_surface_cell();
    let triples = audit_associativity_and_cocycle();
    let cyclic_squares = audit_cyclic_equivariance();
    let tensor_squares = audit_tensor_interchange();

    println!("Resolved surface counit / Brauer-state certificate");
    println!("===================================================");
    println!("  exact one-loop one-point cell: W_2 I_1 = D I_scalar");
    println!("  both closed-curve types obey nu-Delta = D");
    println!("  associative triple composites checked: {triples}");
    println!("  cyclic base-change squares checked: {cyclic_squares}");
    println!("  tensor/interchange squares checked: {tensor_squares}");
    println!();
    println!("VERDICT");
    println!("  closed-circuit number is an additive composition cocycle");
    println!("  D -> 1 is a cyclic monoidal augmentation after resolving circuits");
    println!("  a single D^(-L) normalization is not the all-topology definition");
    println!("  this layer reduces physical descent to the surface-function kernel test");
}
