use std::cmp::{Ordering, Reverse};
use std::collections::{BTreeMap, BTreeSet, BinaryHeap, VecDeque};
use std::sync::OnceLock;
use std::time::Instant;

const VARIABLES: usize = 4;
type Monomial = [u8; VARIABLES];

fn prime() -> i64 {
    static PRIME: OnceLock<i64> = OnceLock::new();
    *PRIME.get_or_init(|| {
        std::env::var("PRIME")
            .ok()
            .map(|raw| raw.parse().expect("PRIME must be an integer"))
            .unwrap_or(32_003)
    })
}

fn add_mod(left: i64, right: i64) -> i64 {
    (left + right).rem_euclid(prime())
}
fn multiply_mod(left: i64, right: i64) -> i64 {
    ((left as i128 * right as i128) % prime() as i128) as i64
}
fn power_mod(mut base: i64, mut exponent: i64) -> i64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent & 1 == 1 {
            result = multiply_mod(result, base);
        }
        base = multiply_mod(base, base);
        exponent >>= 1;
    }
    result
}
fn inverse(value: i64) -> i64 {
    power_mod(value.rem_euclid(prime()), prime() - 2)
}

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct Polynomial(BTreeMap<Monomial, i64>);

impl Polynomial {
    fn term(monomial: Monomial, coefficient: i64) -> Self {
        let mut result = Self::default();
        let coefficient = coefficient.rem_euclid(prime());
        if coefficient != 0 {
            result.0.insert(monomial, coefficient);
        }
        result
    }
    fn constant(coefficient: i64) -> Self {
        Self::term([0; VARIABLES], coefficient)
    }
    fn variable(index: usize) -> Self {
        let mut monomial = [0; VARIABLES];
        monomial[index] = 1;
        Self::term(monomial, 1)
    }
    fn add(&self, other: &Self) -> Self {
        let mut result = self.clone();
        for (monomial, coefficient) in &other.0 {
            let next = add_mod(*result.0.get(monomial).unwrap_or(&0), *coefficient);
            if next == 0 {
                result.0.remove(monomial);
            } else {
                result.0.insert(*monomial, next);
            }
        }
        result
    }
    fn subtract(&self, other: &Self) -> Self {
        self.add(&other.scale(-1))
    }
    fn scale(&self, scalar: i64) -> Self {
        let mut result = Self::default();
        for (monomial, coefficient) in &self.0 {
            let next = multiply_mod(*coefficient, scalar.rem_euclid(prime()));
            if next != 0 {
                result.0.insert(*monomial, next);
            }
        }
        result
    }
    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::default();
        for (left_monomial, left_coefficient) in &self.0 {
            for (right_monomial, right_coefficient) in &other.0 {
                let mut monomial = [0; VARIABLES];
                for variable in 0..VARIABLES {
                    monomial[variable] =
                        left_monomial[variable] + right_monomial[variable];
                }
                let next = add_mod(
                    *result.0.get(&monomial).unwrap_or(&0),
                    multiply_mod(*left_coefficient, *right_coefficient),
                );
                if next == 0 {
                    result.0.remove(&monomial);
                } else {
                    result.0.insert(monomial, next);
                }
            }
        }
        result
    }
    fn power(&self, mut exponent: u8) -> Self {
        let mut result = Self::constant(1);
        let mut base = self.clone();
        while exponent > 0 {
            if exponent & 1 == 1 {
                result = result.multiply(&base);
            }
            exponent >>= 1;
            if exponent > 0 {
                base = base.multiply(&base);
            }
        }
        result
    }
    fn derivative(&self, variable: usize) -> Self {
        let mut result = Self::default();
        for (monomial, coefficient) in &self.0 {
            if monomial[variable] > 0 {
                let mut derived = *monomial;
                let exponent = derived[variable];
                derived[variable] -= 1;
                result = result.add(&Self::term(
                    derived,
                    multiply_mod(*coefficient, i64::from(exponent)),
                ));
            }
        }
        result
    }
    fn leading_term(&self) -> Option<(Monomial, i64)> {
        self.0
            .iter()
            .max_by(|(left, _), (right, _)| compare_monomials(left, right))
            .map(|(monomial, coefficient)| (*monomial, *coefficient))
    }
    fn monic(&self) -> Self {
        self.leading_term()
            .map_or_else(|| self.clone(), |(_, coefficient)| self.scale(inverse(coefficient)))
    }
    fn is_zero(&self) -> bool {
        self.0.is_empty()
    }
}

fn compare_monomials(left: &Monomial, right: &Monomial) -> Ordering {
    let left_degree: u16 = left.iter().map(|value| u16::from(*value)).sum();
    let right_degree: u16 = right.iter().map(|value| u16::from(*value)).sum();
    left_degree.cmp(&right_degree).then_with(|| {
        for variable in (0..VARIABLES).rev() {
            if left[variable] != right[variable] {
                return right[variable].cmp(&left[variable]);
            }
        }
        Ordering::Equal
    })
}
fn divides(divisor: &Monomial, dividend: &Monomial) -> bool {
    (0..VARIABLES).all(|variable| divisor[variable] <= dividend[variable])
}
fn quotient(dividend: &Monomial, divisor: &Monomial) -> Monomial {
    let mut result = [0; VARIABLES];
    for variable in 0..VARIABLES {
        result[variable] = dividend[variable] - divisor[variable];
    }
    result
}
fn least_common_multiple(left: &Monomial, right: &Monomial) -> Monomial {
    let mut result = [0; VARIABLES];
    for variable in 0..VARIABLES {
        result[variable] = left[variable].max(right[variable]);
    }
    result
}
fn total_degree(monomial: &Monomial) -> u16 {
    monomial.iter().map(|value| u16::from(*value)).sum()
}
fn relatively_prime(left: &Monomial, right: &Monomial) -> bool {
    (0..VARIABLES).all(|variable| left[variable] == 0 || right[variable] == 0)
}

fn normal_form(mut polynomial: Polynomial, basis: &[Polynomial]) -> Polynomial {
    let mut remainder = Polynomial::default();
    while let Some((leading_monomial, leading_coefficient)) = polynomial.leading_term() {
        let mut reduced = false;
        for divisor in basis {
            let (divisor_monomial, divisor_coefficient) =
                divisor.leading_term().expect("zero basis polynomial");
            if divides(&divisor_monomial, &leading_monomial) {
                let multiplier = Polynomial::term(
                    quotient(&leading_monomial, &divisor_monomial),
                    multiply_mod(leading_coefficient, inverse(divisor_coefficient)),
                );
                polynomial = polynomial.subtract(&divisor.multiply(&multiplier));
                reduced = true;
                break;
            }
        }
        if !reduced {
            let leading = Polynomial::term(leading_monomial, leading_coefficient);
            remainder = remainder.add(&leading);
            polynomial = polynomial.subtract(&leading);
        }
    }
    remainder
}

fn s_polynomial(left: &Polynomial, right: &Polynomial) -> Polynomial {
    let (left_monomial, left_coefficient) = left.leading_term().unwrap();
    let (right_monomial, right_coefficient) = right.leading_term().unwrap();
    let common = least_common_multiple(&left_monomial, &right_monomial);
    left.multiply(&Polynomial::term(
        quotient(&common, &left_monomial),
        inverse(left_coefficient),
    ))
    .subtract(&right.multiply(&Polynomial::term(
        quotient(&common, &right_monomial),
        inverse(right_coefficient),
    )))
}

fn groebner_basis(seed: Vec<Polynomial>) -> Vec<Polynomial> {
    let mut basis: Vec<_> = seed
        .into_iter()
        .filter(|polynomial| !polynomial.is_zero())
        .map(|polynomial| polynomial.monic())
        .collect();
    let mut pairs = BinaryHeap::new();
    for left in 0..basis.len() {
        for right in left + 1..basis.len() {
            let lcm = least_common_multiple(
                &basis[left].leading_term().unwrap().0,
                &basis[right].leading_term().unwrap().0,
            );
            pairs.push(Reverse((total_degree(&lcm), left, right)));
        }
    }
    while let Some(Reverse((_, left, right))) = pairs.pop() {
        let left_lead = basis[left].leading_term().unwrap().0;
        let right_lead = basis[right].leading_term().unwrap().0;
        if relatively_prime(&left_lead, &right_lead) {
            continue;
        }
        let remainder = normal_form(s_polynomial(&basis[left], &basis[right]), &basis);
        if !remainder.is_zero() {
            let new_index = basis.len();
            basis.push(remainder.monic());
            for old_index in 0..new_index {
                let lcm = least_common_multiple(
                    &basis[old_index].leading_term().unwrap().0,
                    &basis[new_index].leading_term().unwrap().0,
                );
                pairs.push(Reverse((total_degree(&lcm), old_index, new_index)));
            }
            assert!(basis.len() <= 10_000, "Groebner safety cap exceeded");
        }
    }
    basis
}

fn standard_monomial_count(basis: &[Polynomial]) -> usize {
    let leading: Vec<_> = basis
        .iter()
        .map(|polynomial| polynomial.leading_term().unwrap().0)
        .collect();
    let mut standard = BTreeSet::new();
    let mut frontier = VecDeque::new();
    standard.insert([0; VARIABLES]);
    frontier.push_back([0; VARIABLES]);
    while let Some(monomial) = frontier.pop_front() {
        for variable in 0..VARIABLES {
            let mut next = monomial;
            next[variable] += 1;
            if leading.iter().any(|candidate| divides(candidate, &next)) {
                continue;
            }
            if standard.insert(next) {
                assert!(standard.len() <= 100_000, "standard monomial cap exceeded");
                frontier.push_back(next);
            }
        }
    }
    standard.len()
}

fn sum(polynomials: &[Polynomial]) -> Polynomial {
    polynomials
        .iter()
        .fold(Polynomial::default(), |left, right| left.add(right))
}
fn product(polynomials: &[Polynomial]) -> Polynomial {
    polynomials
        .iter()
        .fold(Polynomial::constant(1), |left, right| left.multiply(right))
}

#[derive(Clone)]
struct Factor {
    name: &'static str,
    polynomial: Polynomial,
    exponent: i64,
}

fn deletion_closed_rank(k: &Polynomial, selected: &[Factor]) -> (usize, usize, u128) {
    let mut factors = vec![Factor {
        name: "K",
        polynomial: k.clone(),
        exponent: 5,
    }];
    factors.extend_from_slice(selected);
    let divisor = product(
        &factors
            .iter()
            .map(|factor| factor.polynomial.clone())
            .collect::<Vec<_>>(),
    );
    let mut equations = Vec::new();
    for variable in 0..3 {
        let mut terms = Vec::new();
        for (index, factor) in factors.iter().enumerate() {
            let complement = product(
                &factors
                    .iter()
                    .enumerate()
                    .filter(|(other, _)| *other != index)
                    .map(|(_, other)| other.polynomial.clone())
                    .collect::<Vec<_>>(),
            );
            terms.push(
                complement
                    .multiply(&factor.polynomial.derivative(variable))
                    .scale(factor.exponent),
            );
        }
        equations.push(sum(&terms));
    }
    equations.push(
        Polynomial::variable(3)
            .multiply(&divisor)
            .subtract(&Polynomial::constant(1)),
    );
    let started = Instant::now();
    let basis = groebner_basis(equations);
    let elapsed = started.elapsed().as_millis();
    let rank = standard_monomial_count(&basis);
    (rank, basis.len(), elapsed)
}

fn main() {
    let c = Polynomial::variable(0);
    let a = Polynomial::variable(1);
    let b = Polynomial::variable(2);
    let c2 = c.power(2);
    let a2 = a.power(2);
    let b2 = b.power(2);
    let point = std::env::var("KINEMATIC_POINT").unwrap_or_else(|_| "A".to_owned());
    let (x1, x2, x3, p1, p2, p3) = match point.as_str() {
        "A" => (2_i64, 3_i64, 4_i64, 5_i64, 7_i64, 11_i64),
        "B" => (3_i64, 5_i64, 6_i64, 7_i64, 11_i64, 13_i64),
        _ => panic!("KINEMATIC_POINT must be A or B"),
    };
    let p1s = p1 * p1;
    let p2s = p2 * p2;
    let p3s = p3 * p3;
    let h = p1s + p2s - p3s;
    let g_a_constant = p1s * (p1s - p2s - p3s);
    let g_a_c2 = -p1s + p2s - p3s;
    let g_b_constant = p2s * (p2s - p1s - p3s);
    let g_b_c2 = -p2s + p1s - p3s;
    let h_c2 = -p1s - p2s + p3s;
    let k = sum(&[
        a.power(4).scale(p1s),
        a2.multiply(&b2).scale(-h),
        b.power(4).scale(p2s),
        a2.scale(g_a_constant),
        c2.multiply(&a2).scale(g_a_c2),
        b2.scale(g_b_constant),
        c2.multiply(&b2).scale(g_b_c2),
        c.power(4).scale(p3s),
        c2.scale(p3s * h_c2),
        Polynomial::constant(p3s * p1s * p2s),
    ]);
    let denominators = [
        Factor {
            name: "q_g1",
            polynomial: sum(&[c.clone(), b.clone(), Polynomial::constant(x1)]),
            exponent: 17,
        },
        Factor {
            name: "q_g2",
            polynomial: sum(&[c.clone(), a.clone(), Polynomial::constant(x2)]),
            exponent: 19,
        },
        Factor {
            name: "q_g3",
            polynomial: sum(&[a, b.clone(), Polynomial::constant(x3)]),
            exponent: 23,
        },
        Factor {
            name: "q_g23",
            polynomial: sum(&[c, b, Polynomial::constant(x2 + x3)]),
            exponent: 29,
        },
    ];
    let only = std::env::var("ONLY_MASK")
        .ok()
        .map(|raw| u8::from_str_radix(&raw, 2).expect("ONLY_MASK must be binary"));
    let masks: Vec<u8> = only.map_or_else(|| (0..16).collect(), |mask| vec![mask]);
    let mut closed_ranks = [None; 16];
    for mask in masks {
        let selected: Vec<_> = denominators
            .iter()
            .enumerate()
            .filter(|(index, _)| mask & (1 << index) != 0)
            .map(|(_, factor)| factor.clone())
            .collect();
        let names = selected.iter().map(|factor| factor.name).collect::<Vec<_>>();
        let (rank, basis_size, elapsed_ms) = deletion_closed_rank(&k, &selected);
        closed_ranks[usize::from(mask)] = Some(rank);
        println!(
            "prime={} point={point} X=({x1},{x2},{x3}) P=({p1},{p2},{p3}) mask={mask:04b} factors={names:?} deletion_closed_rank={rank} basis_size={basis_size} elapsed_ms={elapsed_ms}",
            prime()
        );
    }
    if only.is_none() {
        let closed = closed_ranks.map(|rank| rank.expect("complete cube rank"));
        let mut proper = [0_usize; 16];
        for mask in 0..16_usize {
            let inherited: usize = (0..mask)
                .filter(|submask| submask & mask == *submask)
                .map(|submask| proper[submask])
                .sum();
            proper[mask] = closed[mask]
                .checked_sub(inherited)
                .expect("nonnegative support grade");
        }
        assert_eq!(
            closed,
            [7, 12, 12, 18, 12, 18, 18, 26, 12, 17, 18, 24, 18, 24, 26, 34]
        );
        assert_eq!(
            proper,
            [7, 5, 5, 1, 5, 1, 1, 1, 5, 0, 1, 0, 1, 0, 1, 0]
        );
        println!("DELETION_CLOSED={closed:?}");
        println!("PROPER_SUPPORT_GRADES={proper:?}");
    }
}
