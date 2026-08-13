//! Bounded support certificate for the all-arity transmutation-Cut formula.
//!
//! We use the physical channel X_(1,2l+1)=0.  The two gauge-equivalent
//! scaffold gluing kernels are
//!
//!   C0(k,m) = X_(k,m) - X_(k,2l+1) - X_(m,1),
//!   C1(k,m) = X_(k,m) - X_(k,1)    - X_(m,2l+1).
//!
//! For every pairwise counit U_(e,f), expand its B-support, let exactly one
//! derivative hit C, distribute the remaining derivatives to the two lower
//! factors, and impose lower multi-affinity.  The resulting raw support is
//! exactly:
//!
//! * one tensor product of lower U counits;
//! * for a same-side retained pair, at most one additional two-pair sector
//!   tensored with the all-odd operator Z on the opposite factor.
//!
//! Z = product_e B_e annihilates a Yang--Mills amplitude: by multi-affinity it
//! is the surviving support of product_e W_e, and product_e W_e A =
//! W_e(T_e A) = W_e A_phi3 = 0.  Therefore the extra term lies in a separable
//! lower annihilator ideal, proving the strict tensor-quotient formula.

use std::collections::{BTreeMap, BTreeSet};

const X_LEFT: u8 = 250;
const X_RIGHT: u8 = 251;

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
}

type Monomial = Vec<Coord>;
type TensorMonomial = (Monomial, Monomial);
type LinearCombination = BTreeMap<TensorMonomial, i32>;

#[derive(Clone, Copy, Debug)]
enum GaugeKernel {
    First,
    Second,
}

fn canonical_monomial(mut coordinates: Vec<Coord>) -> Monomial {
    coordinates.sort_unstable();
    assert!(coordinates.windows(2).all(|window| window[0] != window[1]));
    coordinates
}

fn cycle_even_labels(cycle: &[u8]) -> Vec<u8> {
    assert_eq!(cycle.len() % 2, 0);
    cycle.iter().skip(1).step_by(2).copied().collect()
}

fn cycle_odd_labels(cycle: &[u8]) -> Vec<u8> {
    cycle.iter().step_by(2).copied().collect()
}

fn allowed_odd_targets(cycle: &[u8], even: u8) -> Vec<u8> {
    let position = cycle.iter().position(|label| *label == even).unwrap();
    assert_eq!(position % 2, 1);
    let previous = cycle[(position + cycle.len() - 1) % cycle.len()];
    let next = cycle[(position + 1) % cycle.len()];
    cycle_odd_labels(cycle)
        .into_iter()
        .filter(|odd| *odd != previous && *odd != next)
        .collect()
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
        for value in &options[index] {
            current.push(*value);
            recurse(options, index + 1, current, visit);
            current.pop();
        }
    }
    recurse(options, 0, &mut Vec::new(), &mut visit);
}

fn b_product_support(cycle: &[u8], omitted: &BTreeSet<u8>) -> BTreeSet<Monomial> {
    let sources: Vec<_> = cycle_even_labels(cycle)
        .into_iter()
        .filter(|source| !omitted.contains(source))
        .collect();
    let options: Vec<_> = sources
        .iter()
        .map(|source| allowed_odd_targets(cycle, *source))
        .collect();
    let mut result = BTreeSet::new();
    enumerate_choices(&options, |targets| {
        let coordinates = sources
            .iter()
            .zip(targets)
            .map(|(source, target)| Coord::new(*source, *target))
            .collect();
        assert!(result.insert(canonical_monomial(coordinates)));
    });
    result
}

fn u_support(cycle: &[u8], pair: Coord) -> BTreeSet<Monomial> {
    let evens: BTreeSet<_> = cycle_even_labels(cycle).into_iter().collect();
    assert!(evens.contains(&pair.0));
    assert!(evens.contains(&pair.1));
    let omitted = BTreeSet::from([pair.0, pair.1]);
    b_product_support(cycle, &omitted)
        .into_iter()
        .map(|mut monomial| {
            monomial.push(pair);
            canonical_monomial(monomial)
        })
        .collect()
}

fn z_support(cycle: &[u8]) -> BTreeSet<Monomial> {
    b_product_support(cycle, &BTreeSet::new())
}

fn two_pair_support(cycle: &[u8], first: Coord, second: Coord) -> BTreeSet<Monomial> {
    let evens: BTreeSet<_> = cycle_even_labels(cycle).into_iter().collect();
    let endpoints = BTreeSet::from([first.0, first.1, second.0, second.1]);
    assert_eq!(endpoints.len(), 4);
    assert!(endpoints.iter().all(|endpoint| evens.contains(endpoint)));
    b_product_support(cycle, &endpoints)
        .into_iter()
        .map(|mut monomial| {
            monomial.push(first);
            monomial.push(second);
            canonical_monomial(monomial)
        })
        .collect()
}

fn lower_multi_affine(cycle: &[u8], monomial: &Monomial) -> bool {
    let evens: BTreeSet<_> = cycle_even_labels(cycle).into_iter().collect();
    let mut occurrences = BTreeMap::<u8, usize>::new();
    for coordinate in monomial {
        for endpoint in [coordinate.0, coordinate.1] {
            if evens.contains(&endpoint) {
                *occurrences.entry(endpoint).or_default() += 1;
            }
        }
    }
    evens
        .iter()
        .all(|even| occurrences.get(even).copied().unwrap_or(0) == 1)
}

fn bridge_terms(k: u8, m: u8, i: u8, j: u8, gauge: GaugeKernel) -> [(Coord, i32); 3] {
    match gauge {
        GaugeKernel::First => [
            (Coord::new(k, m), 1),
            (Coord::new(k, j), -1),
            (Coord::new(m, i), -1),
        ],
        GaugeKernel::Second => [
            (Coord::new(k, m), 1),
            (Coord::new(k, i), -1),
            (Coord::new(m, j), -1),
        ],
    }
}

fn add_product(
    result: &mut LinearCombination,
    left: &BTreeSet<Monomial>,
    right: &BTreeSet<Monomial>,
    coefficient: i32,
) {
    for left_monomial in left {
        for right_monomial in right {
            *result
                .entry((left_monomial.clone(), right_monomial.clone()))
                .or_default() += coefficient;
        }
    }
}

fn prune_zero(result: &mut LinearCombination) {
    result.retain(|_, coefficient| *coefficient != 0);
}

struct Channel {
    global_cycle: Vec<u8>,
    left_cycle: Vec<u8>,
    right_cycle: Vec<u8>,
    left_labels: BTreeSet<u8>,
    right_labels: BTreeSet<u8>,
    left_interior: Vec<u8>,
    right_interior: Vec<u8>,
    left_evens: BTreeSet<u8>,
    right_evens: BTreeSet<u8>,
    i: u8,
    j: u8,
    left_minus: u8,
    left_plus: u8,
    right_minus: u8,
    right_plus: u8,
}

impl Channel {
    fn new(n: usize, left_external_gluons: usize) -> Self {
        assert!(n >= 4);
        assert!(left_external_gluons >= 2);
        assert!(left_external_gluons <= n - 2);
        assert!(2 * n < X_LEFT as usize);

        let i = 1_u8;
        let j = (2 * left_external_gluons + 1) as u8;
        let global_cycle: Vec<_> = (1..=(2 * n) as u8).collect();
        let left_cycle: Vec<_> = (1..=j).chain([X_LEFT]).collect();
        let right_cycle: Vec<_> = [i, X_RIGHT]
            .into_iter()
            .chain(j..=(2 * n) as u8)
            .collect();
        let left_labels = (1..=j).collect();
        let right_labels = [i]
            .into_iter()
            .chain(j..=(2 * n) as u8)
            .collect();
        let left_interior = (2..j).collect();
        let right_interior = ((j + 1)..=(2 * n) as u8).collect();
        let left_evens = (2..j).filter(|label| label % 2 == 0).collect();
        let right_evens = ((j + 1)..=(2 * n) as u8)
            .filter(|label| label % 2 == 0)
            .collect();

        Self {
            global_cycle,
            left_cycle,
            right_cycle,
            left_labels,
            right_labels,
            left_interior,
            right_interior,
            left_evens,
            right_evens,
            i,
            j,
            left_minus: j - 1,
            left_plus: i + 1,
            right_minus: (2 * n) as u8,
            right_plus: j + 1,
        }
    }

    fn distribute(&self, coordinate: Coord) -> Option<bool> {
        let on_left = self.left_labels.contains(&coordinate.0)
            && self.left_labels.contains(&coordinate.1);
        let on_right = self.right_labels.contains(&coordinate.0)
            && self.right_labels.contains(&coordinate.1);
        match (on_left, on_right) {
            (true, false) => Some(true),
            (false, true) => Some(false),
            (false, false) => None,
            (true, true) => panic!("an even-containing coordinate cannot live on both sides"),
        }
    }
}

fn raw_cut_support(channel: &Channel, pair: Coord, gauge: GaugeKernel) -> LinearCombination {
    let mut result = LinearCombination::new();
    for global_monomial in u_support(&channel.global_cycle, pair) {
        for k in &channel.left_interior {
            for m in &channel.right_interior {
                for (bridge, sign) in bridge_terms(*k, *m, channel.i, channel.j, gauge) {
                    let Some(position) = global_monomial
                        .iter()
                        .position(|coordinate| *coordinate == bridge)
                    else {
                        continue;
                    };
                    let mut left = Vec::new();
                    let mut right = Vec::new();
                    let mut distributable = true;
                    for (index, coordinate) in global_monomial.iter().enumerate() {
                        if index == position {
                            continue;
                        }
                        match channel.distribute(*coordinate) {
                            Some(true) => left.push(*coordinate),
                            Some(false) => right.push(*coordinate),
                            None => {
                                distributable = false;
                                break;
                            }
                        }
                    }
                    if !distributable {
                        continue;
                    }
                    left.push(Coord::new(*k, X_LEFT));
                    right.push(Coord::new(*m, X_RIGHT));
                    let left = canonical_monomial(left);
                    let right = canonical_monomial(right);
                    if !lower_multi_affine(&channel.left_cycle, &left)
                        || !lower_multi_affine(&channel.right_cycle, &right)
                    {
                        continue;
                    }
                    *result.entry((left, right)).or_default() += sign;
                }
            }
        }
    }
    prune_zero(&mut result);
    result
}

fn expected_cut_support(channel: &Channel, pair: Coord, gauge: GaugeKernel) -> LinearCombination {
    let left_anchor = match gauge {
        GaugeKernel::First => channel.left_minus,
        GaugeKernel::Second => channel.left_plus,
    };
    let right_anchor = match gauge {
        GaugeKernel::First => channel.right_minus,
        GaugeKernel::Second => channel.right_plus,
    };

    let pair_left = channel.left_evens.contains(&pair.0) && channel.left_evens.contains(&pair.1);
    let pair_right =
        channel.right_evens.contains(&pair.0) && channel.right_evens.contains(&pair.1);
    let mut result = LinearCombination::new();

    if pair_left {
        add_product(
            &mut result,
            &u_support(&channel.left_cycle, pair),
            &u_support(&channel.right_cycle, Coord::new(X_RIGHT, right_anchor)),
            1,
        );
        if pair.0 != left_anchor && pair.1 != left_anchor {
            add_product(
                &mut result,
                &two_pair_support(
                    &channel.left_cycle,
                    pair,
                    Coord::new(left_anchor, X_LEFT),
                ),
                &z_support(&channel.right_cycle),
                1,
            );
        }
    } else if pair_right {
        add_product(
            &mut result,
            &u_support(&channel.left_cycle, Coord::new(left_anchor, X_LEFT)),
            &u_support(&channel.right_cycle, pair),
            1,
        );
        if pair.0 != right_anchor && pair.1 != right_anchor {
            add_product(
                &mut result,
                &z_support(&channel.left_cycle),
                &two_pair_support(
                    &channel.right_cycle,
                    pair,
                    Coord::new(right_anchor, X_RIGHT),
                ),
                1,
            );
        }
    } else {
        let left_endpoint = if channel.left_evens.contains(&pair.0) {
            pair.0
        } else {
            pair.1
        };
        let right_endpoint = if channel.right_evens.contains(&pair.0) {
            pair.0
        } else {
            pair.1
        };
        assert!(channel.left_evens.contains(&left_endpoint));
        assert!(channel.right_evens.contains(&right_endpoint));
        add_product(
            &mut result,
            &u_support(
                &channel.left_cycle,
                Coord::new(left_endpoint, X_LEFT),
            ),
            &u_support(
                &channel.right_cycle,
                Coord::new(X_RIGHT, right_endpoint),
            ),
            1,
        );
    }

    prune_zero(&mut result);
    result
}

fn audit() {
    println!("Transmutation counit / physical-Cut support certificate");
    println!("=======================================================");
    for n in 4..=7 {
        for left_external_gluons in 2..=(n - 2) {
            let channel = Channel::new(n, left_external_gluons);
            let evens = cycle_even_labels(&channel.global_cycle);
            let mut tested_pairs = 0;
            let mut largest_raw_support = 0;
            for first in 0..evens.len() {
                for second in (first + 1)..evens.len() {
                    let pair = Coord::new(evens[first], evens[second]);
                    for gauge in [GaugeKernel::First, GaugeKernel::Second] {
                        let raw = raw_cut_support(&channel, pair, gauge);
                        let expected = expected_cut_support(&channel, pair, gauge);
                        assert_eq!(
                            raw, expected,
                            "failed at n={n}, split={left_external_gluons}|{}, pair={pair:?}, gauge={gauge:?}",
                            n - left_external_gluons
                        );
                        largest_raw_support = largest_raw_support.max(raw.len());
                    }
                    tested_pairs += 1;
                }
            }
            println!(
                "  n={n}, split={left_external_gluons}|{}: {tested_pairs} pairs x 2 gauges; largest raw tensor support={largest_raw_support}",
                n - left_external_gluons
            );
        }
    }
}

fn main() {
    audit();
    println!("\nVERDICT");
    println!("  every non-anchor bridge choice cancels between the cross and boundary terms");
    println!("  crossing U edges map exactly to U_L tensor U_R");
    println!("  same-side U edges map to U_L tensor U_R plus a two-pair tensor Z term");
    println!("  Z=product B_e lies in the separate lower Yang--Mills annihilator");
    println!("  both gauge kernels therefore induce the same group-like counit in Q_L tensor Q_R");
}
