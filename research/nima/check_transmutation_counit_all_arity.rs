//! All-arity combinatorial certificate for the scaffold transmutation counit.
//!
//! Source axioms (not re-proved here):
//!
//!   W_e = sum_{j not in {e,e+-1}} d/dX_{e,j},
//!   (prod_{g in E\{e,f}} W_g) A_YM = X_{e,f} A_phi3,
//!   A_YM is multi-affine in every even scaffold label.
//!
//! Applying d/dX_{e,f} gives a pairwise transmuter V_{e,f}.  Multi-affinity
//! kills every term of V_{e,f} in which one of the other W_g factors chooses
//! an even target.  Its universal surviving representative is therefore
//!
//!   U_{e,f} = d/dX_{e,f} prod_{g in E\{e,f}} B_g,
//!   B_g = sum_{o odd, o not adjacent to g} d/dX_{g,o}.
//!
//! There is a second universal support identity.  If
//!
//!   T_e = prod_{g in E\{e}} W_g,
//!   R_e = prod_{g in E\{e}} B_g,
//!
//! then the multi-affine support of T_e is the disjoint union of R_e and
//! all U_{e,f} incident to e.  Hence, on the canonical amplitude,
//!
//!   T_e = R_e + sum_{f != e} U_{e,f}  modulo Ann(A_YM),
//!   R_e A_YM = -(n-2) A_phi3.
//!
//! This program checks the support classification directly through n=7,
//! verifies its closed counts without overflow through n=25, checks pair-sector disjointness
//! and cyclic covariance through n=7, and locates the complete n=4,5
//! Dong--Su--Yang coframes inside the appropriate fixed reference slice.  It
//! also checks the integral equivariant obstruction: cyclically invariant
//! edge combinations have augmentation divisible by n for odd n and n/2 for
//! even n, so a unit counit representative requires rationalization or a new
//! fixed (barycentric) generator.

use std::collections::{BTreeMap, BTreeSet};

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

type Monomial = Vec<Coord>;

fn rotate_label(label: u8, shift: u8, modulus: u8) -> u8 {
    ((label - 1 + shift) % modulus) + 1
}

fn even_labels(n: usize) -> Vec<u8> {
    (1..=n).map(|index| (2 * index) as u8).collect()
}

fn odd_labels(n: usize) -> Vec<u8> {
    (0..n).map(|index| (2 * index + 1) as u8).collect()
}

fn adjacent_odds(even: u8, modulus: u8) -> [u8; 2] {
    [
        if even == 1 { modulus } else { even - 1 },
        if even == modulus { 1 } else { even + 1 },
    ]
}

fn allowed_odd_targets(even: u8, n: usize) -> Vec<u8> {
    let adjacent = adjacent_odds(even, (2 * n) as u8);
    odd_labels(n)
        .into_iter()
        .filter(|odd| !adjacent.contains(odd))
        .collect()
}

fn allowed_all_targets(even: u8, n: usize) -> Vec<u8> {
    let modulus = (2 * n) as u8;
    let adjacent = adjacent_odds(even, modulus);
    (1..=modulus)
        .filter(|target| *target != even && !adjacent.contains(target))
        .collect()
}

fn power(base: u128, exponent: usize) -> u128 {
    (0..exponent)
        .try_fold(1_u128, |result, _| result.checked_mul(base))
        .expect("closed count exceeded u128")
}

fn canonical_monomial(pair: Coord, sources: &[u8], targets: &[u8]) -> Monomial {
    assert_eq!(sources.len(), targets.len());
    let mut result = Vec::with_capacity(sources.len() + 1);
    result.push(pair);
    result.extend(
        sources
            .iter()
            .zip(targets)
            .map(|(source, target)| Coord::new(*source, *target)),
    );
    result.sort_unstable();
    result
}

fn canonical_source_monomial(sources: &[u8], targets: &[u8]) -> Monomial {
    assert_eq!(sources.len(), targets.len());
    let mut result: Vec<_> = sources
        .iter()
        .zip(targets)
        .map(|(source, target)| Coord::new(*source, *target))
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

fn multi_affine(value: &Monomial, n: usize) -> bool {
    let mut occurrences = vec![0_u8; n];
    for coordinate in value {
        for label in [coordinate.0, coordinate.1] {
            if label % 2 == 0 {
                occurrences[label as usize / 2 - 1] += 1;
            }
        }
    }
    occurrences.into_iter().all(|count| count <= 1)
}

fn enumerate_choices<F: FnMut(&[u8])>(options: &[Vec<u8>], mut visit: F) {
    fn recurse<F: FnMut(&[u8])>(
        options: &[Vec<u8>],
        index: usize,
        current: &mut Vec<u8>,
        visit: &mut F,
    ) {
        if index == options.len() {
            visit(current);
            return;
        }
        for choice in &options[index] {
            current.push(*choice);
            recurse(options, index + 1, current, visit);
            current.pop();
        }
    }
    recurse(options, 0, &mut Vec::new(), &mut visit);
}

fn pair_sources(n: usize, pair: Coord) -> Vec<u8> {
    even_labels(n)
        .into_iter()
        .filter(|label| *label != pair.0 && *label != pair.1)
        .collect()
}

fn u_support(n: usize, pair: Coord) -> BTreeSet<Monomial> {
    let sources = pair_sources(n, pair);
    let options: Vec<_> = sources
        .iter()
        .map(|source| allowed_odd_targets(*source, n))
        .collect();
    let mut result = BTreeSet::new();
    enumerate_choices(&options, |targets| {
        assert!(result.insert(canonical_monomial(pair, &sources, targets)));
    });
    result
}

fn r_support(n: usize, omitted: u8) -> BTreeSet<Monomial> {
    let sources: Vec<_> = even_labels(n)
        .into_iter()
        .filter(|label| *label != omitted)
        .collect();
    let options: Vec<_> = sources
        .iter()
        .map(|source| allowed_odd_targets(*source, n))
        .collect();
    let mut result = BTreeSet::new();
    enumerate_choices(&options, |targets| {
        assert!(result.insert(canonical_source_monomial(&sources, targets)));
    });
    result
}

fn t_multiaffine_support(n: usize, omitted: u8) -> BTreeSet<Monomial> {
    let sources: Vec<_> = even_labels(n)
        .into_iter()
        .filter(|label| *label != omitted)
        .collect();
    let options: Vec<_> = sources
        .iter()
        .map(|source| allowed_all_targets(*source, n))
        .collect();
    let mut result = BTreeSet::new();
    enumerate_choices(&options, |targets| {
        let value = canonical_source_monomial(&sources, targets);
        if multi_affine(&value, n) {
            assert!(result.insert(value));
        }
    });
    result
}

fn direct_multiaffine_audit(n: usize, pair: Coord) -> (u128, u128) {
    let sources = pair_sources(n, pair);
    let options: Vec<_> = sources
        .iter()
        .map(|source| allowed_all_targets(*source, n))
        .collect();
    let mut raw = 0_u128;
    let mut survivors = BTreeSet::new();
    enumerate_choices(&options, |targets| {
        raw += 1;
        let value = canonical_monomial(pair, &sources, targets);
        if multi_affine(&value, n) {
            survivors.insert(value);
            assert!(targets.iter().all(|target| target % 2 == 1));
        }
    });
    (raw, survivors.len() as u128)
}

fn monomial(coords: &[(u8, u8)]) -> Monomial {
    let mut result: Vec<_> = coords
        .iter()
        .map(|(first, second)| Coord::new(*first, *second))
        .collect();
    result.sort_unstable();
    result
}

fn low_point_dsy(n: usize) -> Vec<Monomial> {
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
        _ => Vec::new(),
    }
}

fn catalan(index: usize) -> u128 {
    let mut values = vec![0_u128; index + 1];
    values[0] = 1;
    for size in 1..=index {
        values[size] = (0..size)
            .map(|left| values[left] * values[size - 1 - left])
            .sum();
    }
    values[index]
}

fn closed_count_audit() {
    println!("closed all-arity support counts");
    // At n=25 the largest count, (2n-3)^(n-2), still fits in u128.
    // checked multiplication makes the arithmetic certificate fail loudly if
    // this bound is raised without also changing the integer representation.
    for n in 3..=25 {
        let all_target_count = 2 * n - 3;
        let odd_target_count = n - 2;
        for even in even_labels(n) {
            assert_eq!(allowed_all_targets(even, n).len(), all_target_count);
            assert_eq!(allowed_odd_targets(even, n).len(), odd_target_count);
        }
        let raw = power(all_target_count as u128, n - 2);
        let universal = power(odd_target_count as u128, n - 2);
        let fixed_trace_slice = power(odd_target_count as u128, n - 3);
        assert!(catalan(n - 2) <= fixed_trace_slice);
        if n <= 12 || n == 16 || n == 24 || n == 25 {
            println!(
                "  n={n:>2}: V raw={raw:<22} U={universal:<18} fixed=[1,4] slice={fixed_trace_slice:<15} Catalan={}",
                catalan(n - 2)
            );
        }
    }
}

fn direct_audit() {
    println!("\ndirect expansion / multi-affinity audit");
    for n in 3..=7 {
        let evens = even_labels(n);
        let expected_raw = power((2 * n - 3) as u128, n - 2);
        let expected_survivors = power((n - 2) as u128, n - 2);
        for first in 0..evens.len() {
            for second in (first + 1)..evens.len() {
                let pair = Coord::new(evens[first], evens[second]);
                let (raw, survivors) = direct_multiaffine_audit(n, pair);
                assert_eq!(raw, expected_raw);
                assert_eq!(survivors, expected_survivors);
            }
        }
        println!(
            "  n={n}: all {} pairs, raw/pair={expected_raw}, universal survivors/pair={expected_survivors}",
            n * (n - 1) / 2
        );
    }
}

fn pair_partition_and_cyclic_audit() {
    println!("\npair-sector partition and cyclic covariance");
    for n in 3..=7 {
        let evens = even_labels(n);
        let modulus = (2 * n) as u8;
        let mut union = BTreeSet::new();
        let mut pair_count = 0;
        for first in 0..evens.len() {
            for second in (first + 1)..evens.len() {
                let pair = Coord::new(evens[first], evens[second]);
                let support = u_support(n, pair);
                assert_eq!(support.len() as u128, power((n - 2) as u128, n - 2));
                for value in &support {
                    assert_eq!(
                        value.iter().filter(|coordinate| coordinate.0 % 2 == 0 && coordinate.1 % 2 == 0).count(),
                        1
                    );
                    assert!(union.insert(value.clone()));
                }
                let rotated_pair = pair.rotate(2, modulus);
                let rotated_support: BTreeSet<_> = support
                    .iter()
                    .map(|value| rotate_monomial(value, 2, modulus))
                    .collect();
                assert_eq!(rotated_support, u_support(n, rotated_pair));
                pair_count += 1;
            }
        }
        assert_eq!(pair_count, n * (n - 1) / 2);
        assert_eq!(
            union.len() as u128,
            pair_count as u128 * power((n - 2) as u128, n - 2)
        );
        println!(
            "  n={n}: {} disjoint edge sectors, union={}, rotation by two exact",
            pair_count,
            union.len()
        );
    }
}

fn vertex_edge_incidence_audit() {
    println!("\nfull W support as vertex plus incident edge sectors");
    for n in 3..=7 {
        let edge_size = power((n - 2) as u128, n - 2);
        let vertex_size = power((n - 2) as u128, n - 1);
        let expected_size = vertex_size + (n as u128 - 1) * edge_size;
        for omitted in even_labels(n) {
            let actual = t_multiaffine_support(n, omitted);
            let vertex = r_support(n, omitted);
            assert_eq!(vertex.len() as u128, vertex_size);

            let mut expected = vertex;
            for other in even_labels(n) {
                if other != omitted {
                    let edge = u_support(n, Coord::new(omitted, other));
                    for value in edge {
                        assert!(expected.insert(value));
                    }
                }
            }
            assert_eq!(expected.len() as u128, expected_size);
            assert_eq!(actual, expected);
        }
        println!(
            "  n={n}: each T_e has vertex={vertex_size} plus {} incident edges x {edge_size}, total={expected_size}",
            n - 1
        );
    }
}

fn low_point_coframe_audit() {
    println!("\nlow-point DSY coframes inside U_(2,2n)");
    for n in [4_usize, 5_usize] {
        let pair = Coord::new(2, (2 * n) as u8);
        let support = u_support(n, pair);
        let dsy = low_point_dsy(n);
        assert_eq!(dsy.len() as u128, catalan(n - 2));
        for operator in &dsy {
            assert!(support.contains(operator));
            assert!(operator.contains(&Coord::new(1, 4)));
        }
        let fixed_slice = support
            .iter()
            .filter(|operator| operator.contains(&Coord::new(1, 4)))
            .count();
        assert_eq!(fixed_slice as u128, power((n - 2) as u128, n - 3));
        println!(
            "  n={n}: U support={}, fixed slice={}, Catalan coframe={}",
            support.len(),
            fixed_slice,
            dsy.len()
        );
    }
}

fn oriented_boundary(mask: u64, n: usize) -> Vec<(u64, i32)> {
    let mut result = Vec::new();
    let mut position = 0;
    for vertex in 0..n {
        let bit = 1_u64 << vertex;
        if mask & bit != 0 {
            let sign = if position % 2 == 0 { 1 } else { -1 };
            result.push((mask ^ bit, sign));
            position += 1;
        }
    }
    result
}

fn deletion_simplex_audit() {
    println!("\ndeleting even labels forms an oriented simplex/Koszul complex");
    for n in 3..=12 {
        let limit = 1_u64 << n;
        for mask in 1_u64..limit {
            let mut boundary_squared = BTreeMap::<u64, i32>::new();
            for (face, first_sign) in oriented_boundary(mask, n) {
                for (subface, second_sign) in oriented_boundary(face, n) {
                    *boundary_squared.entry(subface).or_default() +=
                        first_sign * second_sign;
                }
            }
            assert!(boundary_squared.values().all(|coefficient| *coefficient == 0));
        }

        let edges = (0_u64..limit)
            .filter(|mask| mask.count_ones() == 2)
            .count();
        let star_edges = (1..n)
            .map(|vertex| (1_u64 << 0) | (1_u64 << vertex))
            .collect::<BTreeSet<_>>();
        assert_eq!(edges, n * (n - 1) / 2);
        assert_eq!(star_edges.len(), n - 1);
        for edge in star_edges {
            let boundary = oriented_boundary(edge, n);
            assert_eq!(boundary.len(), 2);
            assert_eq!(boundary[0].1, 1);
            assert_eq!(boundary[1].1, -1);
        }
        println!(
            "  n={n}: d^2=0 on all {} nonempty faces; a connected n-1-edge star spans vertex differences",
            limit - 1
        );
    }
}

fn gcd(mut left: usize, mut right: usize) -> usize {
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left
}

fn vertex_edge(first: usize, second: usize) -> (usize, usize) {
    assert_ne!(first, second);
    if first < second {
        (first, second)
    } else {
        (second, first)
    }
}

fn rotate_vertex_edge(edge: (usize, usize), shift: usize, n: usize) -> (usize, usize) {
    vertex_edge((edge.0 + shift) % n, (edge.1 + shift) % n)
}

fn cyclic_edge_orbits(n: usize) -> Vec<BTreeSet<(usize, usize)>> {
    let all_edges: BTreeSet<_> = (0..n)
        .flat_map(|first| ((first + 1)..n).map(move |second| (first, second)))
        .collect();
    let mut unseen = all_edges.clone();
    let mut orbits = Vec::new();
    while let Some(seed) = unseen.iter().next().copied() {
        let orbit: BTreeSet<_> = (0..n)
            .map(|shift| rotate_vertex_edge(seed, shift, n))
            .collect();
        for edge in &orbit {
            assert!(unseen.remove(edge));
        }
        orbits.push(orbit);
    }
    assert_eq!(orbits.iter().map(BTreeSet::len).sum::<usize>(), all_edges.len());
    orbits
}

fn equivariant_augmentation_audit() {
    println!("\ncyclic equivariant obstruction in the edge/vertex counit lattice");
    for n in 3..=25 {
        let orbits = cyclic_edge_orbits(n);
        assert_eq!(orbits.len(), n / 2);
        let orbit_sizes: Vec<_> = orbits.iter().map(BTreeSet::len).collect();
        let edge_augmentation_gcd = orbit_sizes.iter().copied().reduce(gcd).unwrap();
        let expected_gcd = if n % 2 == 0 { n / 2 } else { n };
        assert_eq!(edge_augmentation_gcd, expected_gcd);

        let expected_shortest_orbit = if n % 2 == 0 { n / 2 } else { n };
        assert_eq!(orbit_sizes.iter().copied().min().unwrap(), expected_shortest_orbit);
        assert!(orbit_sizes.iter().all(|size| *size == n || (n % 2 == 0 && *size == n / 2)));

        // Adding the cyclic vertex sectors T_e (augmentation +1) or R_e
        // (augmentation -(n-2)) contributes only multiples of n and cannot
        // reduce the edge obstruction.
        let combined_gcd = gcd(edge_augmentation_gcd, gcd(n, n * (n - 2)));
        assert_eq!(combined_gcd, expected_gcd);
        assert_ne!(combined_gcd, 1);

        if n <= 12 || n == 16 || n == 24 || n == 25 {
            println!(
                "  n={n:>2}: edge-orbit sizes={orbit_sizes:?}, invariant augmentation ideal={}Z",
                combined_gcd
            );
        }
    }
}

fn main() {
    println!("All-arity scaffold transmutation counit certificate");
    println!("=================================================");
    closed_count_audit();
    direct_audit();
    pair_partition_and_cyclic_audit();
    vertex_edge_incidence_audit();
    low_point_coframe_audit();
    deletion_simplex_audit();
    equivariant_augmentation_audit();
    println!("\nVERDICT");
    println!("  V_(e,f) reduces universally to U_(e,f) by multi-affinity");
    println!("  |supp U_(e,f)|=(n-2)^(n-2), with disjoint pair sectors");
    println!("  cyclic rotation permutes the pair sectors exactly");
    println!("  T_e support = R_e disjoint-union all incident U_(e,f) supports");
    println!("  therefore R_e A_YM=-(n-2) A_phi3");
    println!("  the complete n=4,5 DSY coframes lie in the fixed reference slice");
    println!("  alternating W faces totalize to a deletion-simplex differential d^2=0");
    println!("  integral cyclic edge/vertex representatives augment only to g_n Z");
    println!("    g_n=n for odd n and g_n=n/2 for even n");
    println!("  U_(e,f) A_YM=A_phi3 follows from the pair transmutation theorem");
}
