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
                    monomial[variable] = left_monomial[variable] + right_monomial[variable];
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
        self.leading_term().map_or_else(
            || self.clone(),
            |(_, coefficient)| self.scale(inverse(coefficient)),
        )
    }
    fn is_zero(&self) -> bool {
        self.0.is_empty()
    }
}

#[derive(Clone, Copy, Debug, Default, Eq, PartialEq)]
struct DualScalar {
    value: i64,
    tangent: i64,
}

impl DualScalar {
    fn new(value: i64, tangent: i64) -> Self {
        Self {
            value: value.rem_euclid(prime()),
            tangent: tangent.rem_euclid(prime()),
        }
    }
    fn add(self, other: Self) -> Self {
        Self::new(add_mod(self.value, other.value), add_mod(self.tangent, other.tangent))
    }
    fn multiply(self, other: Self) -> Self {
        Self::new(
            multiply_mod(self.value, other.value),
            add_mod(
                multiply_mod(self.value, other.tangent),
                multiply_mod(self.tangent, other.value),
            ),
        )
    }
    fn inverse(self) -> Self {
        let inverse_value = inverse(self.value);
        Self::new(
            inverse_value,
            -multiply_mod(self.tangent, multiply_mod(inverse_value, inverse_value)),
        )
    }
}

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct DualPolynomial(BTreeMap<Monomial, DualScalar>);

impl DualPolynomial {
    fn from_pair(value: &Polynomial, tangent: &Polynomial) -> Self {
        let monomials = value
            .0
            .keys()
            .chain(tangent.0.keys())
            .copied()
            .collect::<BTreeSet<_>>();
        let mut result = Self::default();
        for monomial in monomials {
            let coefficient = DualScalar::new(
                *value.0.get(&monomial).unwrap_or(&0),
                *tangent.0.get(&monomial).unwrap_or(&0),
            );
            if coefficient != DualScalar::default() {
                result.0.insert(monomial, coefficient);
            }
        }
        result
    }
    fn term(monomial: Monomial, coefficient: DualScalar) -> Self {
        let mut result = Self::default();
        if coefficient != DualScalar::default() {
            result.0.insert(monomial, coefficient);
        }
        result
    }
    fn add(&self, other: &Self) -> Self {
        let mut result = self.clone();
        for (monomial, coefficient) in &other.0 {
            let next = result
                .0
                .get(monomial)
                .copied()
                .unwrap_or_default()
                .add(*coefficient);
            if next == DualScalar::default() {
                result.0.remove(monomial);
            } else {
                result.0.insert(*monomial, next);
            }
        }
        result
    }
    fn subtract(&self, other: &Self) -> Self {
        self.add(&other.scale(DualScalar::new(-1, 0)))
    }
    fn scale(&self, scalar: DualScalar) -> Self {
        let mut result = Self::default();
        for (monomial, coefficient) in &self.0 {
            let next = coefficient.multiply(scalar);
            if next != DualScalar::default() {
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
                    monomial[variable] = left_monomial[variable] + right_monomial[variable];
                }
                let next = result
                    .0
                    .get(&monomial)
                    .copied()
                    .unwrap_or_default()
                    .add(left_coefficient.multiply(*right_coefficient));
                if next == DualScalar::default() {
                    result.0.remove(&monomial);
                } else {
                    result.0.insert(monomial, next);
                }
            }
        }
        result
    }
    fn leading_term(&self) -> Option<(Monomial, DualScalar)> {
        self.0
            .iter()
            .max_by(|(left, _), (right, _)| compare_monomials(left, right))
            .map(|(monomial, coefficient)| (*monomial, *coefficient))
    }
    fn is_zero(&self) -> bool {
        self.0.is_empty()
    }
    fn split(&self) -> (Polynomial, Polynomial) {
        let mut value = Polynomial::default();
        let mut tangent = Polynomial::default();
        for (monomial, coefficient) in &self.0 {
            if coefficient.value != 0 {
                value.0.insert(*monomial, coefficient.value);
            }
            if coefficient.tangent != 0 {
                tangent.0.insert(*monomial, coefficient.tangent);
            }
        }
        (value, tangent)
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

#[derive(Clone)]
struct TrackedPolynomial {
    polynomial: Polynomial,
    provenance: Vec<Polynomial>,
}

#[derive(Clone)]
struct DualTrackedPolynomial {
    polynomial: DualPolynomial,
    provenance: Vec<DualPolynomial>,
}

fn dual_subtract_provenance(
    left: &[DualPolynomial],
    right: &[DualPolynomial],
    multiplier: &DualPolynomial,
) -> Vec<DualPolynomial> {
    left.iter()
        .zip(right)
        .map(|(left_entry, right_entry)| left_entry.subtract(&right_entry.multiply(multiplier)))
        .collect()
}

fn dual_tracked_normal_form(
    mut tracked: DualTrackedPolynomial,
    basis: &[DualTrackedPolynomial],
) -> DualTrackedPolynomial {
    let mut remainder = DualPolynomial::default();
    while let Some((leading_monomial, leading_coefficient)) = tracked.polynomial.leading_term() {
        let mut reduced = false;
        for divisor in basis {
            let (divisor_monomial, divisor_coefficient) = divisor
                .polynomial
                .leading_term()
                .expect("zero dual tracked basis polynomial");
            if divides(&divisor_monomial, &leading_monomial) {
                let multiplier = DualPolynomial::term(
                    quotient(&leading_monomial, &divisor_monomial),
                    leading_coefficient.multiply(divisor_coefficient.inverse()),
                );
                tracked.polynomial = tracked
                    .polynomial
                    .subtract(&divisor.polynomial.multiply(&multiplier));
                tracked.provenance = dual_subtract_provenance(
                    &tracked.provenance,
                    &divisor.provenance,
                    &multiplier,
                );
                reduced = true;
                break;
            }
        }
        if !reduced {
            let leading = DualPolynomial::term(leading_monomial, leading_coefficient);
            remainder = remainder.add(&leading);
            tracked.polynomial = tracked.polynomial.subtract(&leading);
        }
    }
    DualTrackedPolynomial {
        polynomial: remainder,
        provenance: tracked.provenance,
    }
}

fn dual_tracked_s_polynomial(
    left: &DualTrackedPolynomial,
    right: &DualTrackedPolynomial,
) -> DualTrackedPolynomial {
    let (left_monomial, left_coefficient) = left.polynomial.leading_term().unwrap();
    let (right_monomial, right_coefficient) = right.polynomial.leading_term().unwrap();
    let common = least_common_multiple(&left_monomial, &right_monomial);
    let left_multiplier = DualPolynomial::term(
        quotient(&common, &left_monomial),
        left_coefficient.inverse(),
    );
    let right_multiplier = DualPolynomial::term(
        quotient(&common, &right_monomial),
        right_coefficient.inverse(),
    );
    DualTrackedPolynomial {
        polynomial: left
            .polynomial
            .multiply(&left_multiplier)
            .subtract(&right.polynomial.multiply(&right_multiplier)),
        provenance: left
            .provenance
            .iter()
            .zip(&right.provenance)
            .map(|(left_entry, right_entry)| {
                left_entry
                    .multiply(&left_multiplier)
                    .subtract(&right_entry.multiply(&right_multiplier))
            })
            .collect(),
    }
}

fn dual_tracked_groebner_basis(seed: &[DualPolynomial]) -> Vec<DualTrackedPolynomial> {
    let seed_count = seed.len();
    let mut basis = Vec::new();
    for (index, polynomial) in seed.iter().enumerate() {
        if polynomial.is_zero() {
            continue;
        }
        let inverse_lead = polynomial.leading_term().unwrap().1.inverse();
        let mut provenance = vec![DualPolynomial::default(); seed_count];
        provenance[index] = DualPolynomial::term([0; VARIABLES], inverse_lead);
        basis.push(DualTrackedPolynomial {
            polynomial: polynomial.scale(inverse_lead),
            provenance,
        });
    }
    let mut pairs = BinaryHeap::new();
    for left in 0..basis.len() {
        for right in left + 1..basis.len() {
            let common = least_common_multiple(
                &basis[left].polynomial.leading_term().unwrap().0,
                &basis[right].polynomial.leading_term().unwrap().0,
            );
            pairs.push(Reverse((total_degree(&common), left, right)));
        }
    }
    while let Some(Reverse((_, left, right))) = pairs.pop() {
        let left_lead = basis[left].polynomial.leading_term().unwrap().0;
        let right_lead = basis[right].polynomial.leading_term().unwrap().0;
        if relatively_prime(&left_lead, &right_lead) {
            continue;
        }
        let remainder = dual_tracked_normal_form(
            dual_tracked_s_polynomial(&basis[left], &basis[right]),
            &basis,
        );
        if !remainder.polynomial.is_zero() {
            let inverse_lead = remainder.polynomial.leading_term().unwrap().1.inverse();
            let new = DualTrackedPolynomial {
                polynomial: remainder.polynomial.scale(inverse_lead),
                provenance: remainder
                    .provenance
                    .iter()
                    .map(|entry| entry.scale(inverse_lead))
                    .collect(),
            };
            let new_index = basis.len();
            basis.push(new);
            for old_index in 0..new_index {
                let common = least_common_multiple(
                    &basis[old_index].polynomial.leading_term().unwrap().0,
                    &basis[new_index].polynomial.leading_term().unwrap().0,
                );
                pairs.push(Reverse((total_degree(&common), old_index, new_index)));
            }
            assert!(basis.len() <= 10_000, "dual tracked Groebner safety cap exceeded");
        }
    }
    basis
}

fn dual_normal_form_with_exact_trace(
    mut polynomial: DualPolynomial,
    basis: &[DualTrackedPolynomial],
    seed_count: usize,
) -> (DualPolynomial, Vec<DualPolynomial>) {
    let mut remainder = DualPolynomial::default();
    let mut trace = vec![DualPolynomial::default(); seed_count];
    while let Some((leading_monomial, leading_coefficient)) = polynomial.leading_term() {
        let mut reduced = false;
        for divisor in basis {
            let (divisor_monomial, divisor_coefficient) = divisor
                .polynomial
                .leading_term()
                .expect("zero dual basis polynomial");
            if divides(&divisor_monomial, &leading_monomial) {
                let multiplier = DualPolynomial::term(
                    quotient(&leading_monomial, &divisor_monomial),
                    leading_coefficient.multiply(divisor_coefficient.inverse()),
                );
                polynomial = polynomial.subtract(&divisor.polynomial.multiply(&multiplier));
                for (entry, provenance) in trace.iter_mut().zip(&divisor.provenance) {
                    *entry = entry.add(&provenance.multiply(&multiplier));
                }
                reduced = true;
                break;
            }
        }
        if !reduced {
            let leading = DualPolynomial::term(leading_monomial, leading_coefficient);
            remainder = remainder.add(&leading);
            polynomial = polynomial.subtract(&leading);
        }
    }
    (remainder, trace)
}

fn dual_reconstruct_from_exact_trace(
    remainder: &DualPolynomial,
    trace: &[DualPolynomial],
    seed: &[DualPolynomial],
) -> DualPolynomial {
    trace
        .iter()
        .zip(seed)
        .fold(remainder.clone(), |result, (coefficient, generator)| {
            result.add(&coefficient.multiply(generator))
        })
}

fn dual_solve_square(
    matrix: &[Vec<DualScalar>],
    right: &[DualScalar],
) -> (Vec<DualScalar>, Vec<usize>) {
    let dimension = matrix.len();
    assert_eq!(right.len(), dimension, "dual solve right-hand dimension");
    let mut augmented = matrix
        .iter()
        .zip(right)
        .map(|(row, value)| {
            let mut result = row.clone();
            result.push(*value);
            result
        })
        .collect::<Vec<_>>();
    let mut pivots = Vec::new();
    for column in 0..dimension {
        let pivot = (column..dimension)
            .find(|row| augmented[*row][column].value != 0)
            .expect("singular dual frame matrix");
        augmented.swap(column, pivot);
        pivots.push(pivot);
        let inverse_pivot = augmented[column][column].inverse();
        for entry in column..=dimension {
            augmented[column][entry] = augmented[column][entry].multiply(inverse_pivot);
        }
        for row in 0..dimension {
            if row == column {
                continue;
            }
            let multiplier = augmented[row][column];
            if multiplier == DualScalar::default() {
                continue;
            }
            for entry in column..=dimension {
                let subtraction = multiplier.multiply(augmented[column][entry]);
                augmented[row][entry] = augmented[row][entry]
                    .add(DualScalar::new(-subtraction.value, -subtraction.tangent));
            }
        }
    }
    (
        augmented.into_iter().map(|row| row[dimension]).collect(),
        pivots,
    )
}

fn subtract_provenance(
    left: &[Polynomial],
    right: &[Polynomial],
    multiplier: &Polynomial,
) -> Vec<Polynomial> {
    left.iter()
        .zip(right)
        .map(|(left_entry, right_entry)| {
            left_entry.subtract(&right_entry.multiply(multiplier))
        })
        .collect()
}

fn tracked_normal_form(
    mut tracked: TrackedPolynomial,
    basis: &[TrackedPolynomial],
) -> TrackedPolynomial {
    let mut remainder = Polynomial::default();
    while let Some((leading_monomial, leading_coefficient)) = tracked.polynomial.leading_term() {
        let mut reduced = false;
        for divisor in basis {
            let (divisor_monomial, divisor_coefficient) = divisor
                .polynomial
                .leading_term()
                .expect("zero tracked basis polynomial");
            if divides(&divisor_monomial, &leading_monomial) {
                let multiplier = Polynomial::term(
                    quotient(&leading_monomial, &divisor_monomial),
                    multiply_mod(leading_coefficient, inverse(divisor_coefficient)),
                );
                tracked.polynomial = tracked
                    .polynomial
                    .subtract(&divisor.polynomial.multiply(&multiplier));
                tracked.provenance = subtract_provenance(
                    &tracked.provenance,
                    &divisor.provenance,
                    &multiplier,
                );
                reduced = true;
                break;
            }
        }
        if !reduced {
            let leading = Polynomial::term(leading_monomial, leading_coefficient);
            remainder = remainder.add(&leading);
            tracked.polynomial = tracked.polynomial.subtract(&leading);
        }
    }
    TrackedPolynomial {
        polynomial: remainder,
        provenance: tracked.provenance,
    }
}

fn tracked_s_polynomial(
    left: &TrackedPolynomial,
    right: &TrackedPolynomial,
) -> TrackedPolynomial {
    let (left_monomial, left_coefficient) = left.polynomial.leading_term().unwrap();
    let (right_monomial, right_coefficient) = right.polynomial.leading_term().unwrap();
    let common = least_common_multiple(&left_monomial, &right_monomial);
    let left_multiplier = Polynomial::term(
        quotient(&common, &left_monomial),
        inverse(left_coefficient),
    );
    let right_multiplier = Polynomial::term(
        quotient(&common, &right_monomial),
        inverse(right_coefficient),
    );
    TrackedPolynomial {
        polynomial: left
            .polynomial
            .multiply(&left_multiplier)
            .subtract(&right.polynomial.multiply(&right_multiplier)),
        provenance: left
            .provenance
            .iter()
            .zip(&right.provenance)
            .map(|(left_entry, right_entry)| {
                left_entry
                    .multiply(&left_multiplier)
                    .subtract(&right_entry.multiply(&right_multiplier))
            })
            .collect(),
    }
}

fn tracked_groebner_basis(seed: &[Polynomial]) -> Vec<TrackedPolynomial> {
    let seed_count = seed.len();
    let mut basis = Vec::new();
    for (index, polynomial) in seed.iter().enumerate() {
        if polynomial.is_zero() {
            continue;
        }
        let inverse_lead = inverse(polynomial.leading_term().unwrap().1);
        let mut provenance = vec![Polynomial::default(); seed_count];
        provenance[index] = Polynomial::constant(inverse_lead);
        basis.push(TrackedPolynomial {
            polynomial: polynomial.scale(inverse_lead),
            provenance,
        });
    }
    let mut pairs = BinaryHeap::new();
    for left in 0..basis.len() {
        for right in left + 1..basis.len() {
            let common = least_common_multiple(
                &basis[left].polynomial.leading_term().unwrap().0,
                &basis[right].polynomial.leading_term().unwrap().0,
            );
            pairs.push(Reverse((total_degree(&common), left, right)));
        }
    }
    while let Some(Reverse((_, left, right))) = pairs.pop() {
        let left_lead = basis[left].polynomial.leading_term().unwrap().0;
        let right_lead = basis[right].polynomial.leading_term().unwrap().0;
        if relatively_prime(&left_lead, &right_lead) {
            continue;
        }
        let remainder = tracked_normal_form(
            tracked_s_polynomial(&basis[left], &basis[right]),
            &basis,
        );
        if !remainder.polynomial.is_zero() {
            let inverse_lead = inverse(remainder.polynomial.leading_term().unwrap().1);
            let new = TrackedPolynomial {
                polynomial: remainder.polynomial.scale(inverse_lead),
                provenance: remainder
                    .provenance
                    .iter()
                    .map(|entry| entry.scale(inverse_lead))
                    .collect(),
            };
            let new_index = basis.len();
            basis.push(new);
            for old_index in 0..new_index {
                let common = least_common_multiple(
                    &basis[old_index].polynomial.leading_term().unwrap().0,
                    &basis[new_index].polynomial.leading_term().unwrap().0,
                );
                pairs.push(Reverse((total_degree(&common), old_index, new_index)));
            }
            assert!(basis.len() <= 10_000, "tracked Groebner safety cap exceeded");
        }
    }
    basis
}

fn normal_form_with_exact_trace(
    mut polynomial: Polynomial,
    basis: &[TrackedPolynomial],
    seed_count: usize,
) -> (Polynomial, Vec<Polynomial>) {
    let mut remainder = Polynomial::default();
    let mut trace = vec![Polynomial::default(); seed_count];
    while let Some((leading_monomial, leading_coefficient)) = polynomial.leading_term() {
        let mut reduced = false;
        for divisor in basis {
            let (divisor_monomial, divisor_coefficient) = divisor
                .polynomial
                .leading_term()
                .expect("zero tracked basis polynomial");
            if divides(&divisor_monomial, &leading_monomial) {
                let multiplier = Polynomial::term(
                    quotient(&leading_monomial, &divisor_monomial),
                    multiply_mod(leading_coefficient, inverse(divisor_coefficient)),
                );
                polynomial = polynomial.subtract(&divisor.polynomial.multiply(&multiplier));
                for (entry, provenance) in trace.iter_mut().zip(&divisor.provenance) {
                    *entry = entry.add(&provenance.multiply(&multiplier));
                }
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
    (remainder, trace)
}

fn reconstruct_from_exact_trace(
    remainder: &Polynomial,
    trace: &[Polynomial],
    seed: &[Polynomial],
) -> Polynomial {
    trace
        .iter()
        .zip(seed)
        .fold(remainder.clone(), |result, (coefficient, generator)| {
            result.add(&coefficient.multiply(generator))
        })
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
    let started = Instant::now();
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
            if basis.len() <= 20 || basis.len() % 25 == 0 {
                eprintln!(
                    "GB_PROGRESS basis={} pending_pairs={} elapsed_ms={}",
                    basis.len(),
                    pairs.len(),
                    started.elapsed().as_millis()
                );
            }
        }
    }
    eprintln!(
        "GB_COMPLETE basis={} elapsed_ms={}",
        basis.len(),
        started.elapsed().as_millis()
    );
    basis
}

fn standard_monomials(basis: &[Polynomial]) -> BTreeSet<Monomial> {
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
    standard
}

fn standard_monomial_count(basis: &[Polynomial]) -> usize {
    standard_monomials(basis).len()
}

fn matrix_rank(mut rows: Vec<Vec<i64>>) -> usize {
    if rows.is_empty() {
        return 0;
    }
    let column_count = rows[0].len();
    let mut pivot_row = 0;
    for column in 0..column_count {
        let Some(found) = (pivot_row..rows.len()).find(|row| rows[*row][column] != 0) else {
            continue;
        };
        rows.swap(pivot_row, found);
        let scale = inverse(rows[pivot_row][column]);
        for value in &mut rows[pivot_row] {
            *value = multiply_mod(*value, scale);
        }
        for row in 0..rows.len() {
            if row == pivot_row || rows[row][column] == 0 {
                continue;
            }
            let coefficient = rows[row][column];
            for entry in column..column_count {
                rows[row][entry] = add_mod(
                    rows[row][entry],
                    -multiply_mod(coefficient, rows[pivot_row][entry]),
                );
            }
        }
        pivot_row += 1;
        if pivot_row == rows.len() {
            break;
        }
    }
    pivot_row
}

fn matrix_nullspace(mut rows: Vec<Vec<i64>>) -> Vec<Vec<i64>> {
    if rows.is_empty() {
        return Vec::new();
    }
    let column_count = rows[0].len();
    let mut pivot_row = 0;
    let mut pivot_columns = Vec::new();
    for column in 0..column_count {
        let Some(found) = (pivot_row..rows.len()).find(|row| rows[*row][column] != 0) else {
            continue;
        };
        rows.swap(pivot_row, found);
        let scale = inverse(rows[pivot_row][column]);
        for value in &mut rows[pivot_row] {
            *value = multiply_mod(*value, scale);
        }
        for row in 0..rows.len() {
            if row == pivot_row || rows[row][column] == 0 {
                continue;
            }
            let coefficient = rows[row][column];
            for entry in column..column_count {
                rows[row][entry] = add_mod(
                    rows[row][entry],
                    -multiply_mod(coefficient, rows[pivot_row][entry]),
                );
            }
        }
        pivot_columns.push(column);
        pivot_row += 1;
        if pivot_row == rows.len() {
            break;
        }
    }
    let pivot_set: BTreeSet<_> = pivot_columns.iter().copied().collect();
    let free_columns: Vec<_> = (0..column_count)
        .filter(|column| !pivot_set.contains(column))
        .collect();
    free_columns
        .into_iter()
        .map(|free| {
            let mut vector = vec![0_i64; column_count];
            vector[free] = 1;
            for (row, pivot) in pivot_columns.iter().enumerate() {
                vector[*pivot] = (-rows[row][free]).rem_euclid(prime());
            }
            vector
        })
        .collect()
}

fn signed_residue(value: i64) -> i64 {
    let reduced = value.rem_euclid(prime());
    if reduced > prime() / 2 {
        reduced - prime()
    } else {
        reduced
    }
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

fn cm_k_and_linears(p1s: i64, p2s: i64, p3s: i64) -> (Polynomial, [Polynomial; 3]) {
    let c = Polynomial::variable(0);
    let a = Polynomial::variable(1);
    let b = Polynomial::variable(2);
    let c2 = c.power(2);
    let a2 = a.power(2);
    let b2 = b.power(2);
    let h = p1s + p2s - p3s;
    let k = sum(&[
        a.power(4).scale(p1s),
        a2.multiply(&b2).scale(-h),
        b.power(4).scale(p2s),
        a2.scale(p1s * (p1s - p2s - p3s)),
        c2.multiply(&a2).scale(-p1s + p2s - p3s),
        b2.scale(p2s * (p2s - p1s - p3s)),
        c2.multiply(&b2).scale(-p2s + p1s - p3s),
        c.power(4).scale(p3s),
        c2.scale(p3s * (-p1s - p2s + p3s)),
        Polynomial::constant(p3s * p1s * p2s),
    ]);
    let linear_1 = sum(&[
        a2.power(2),
        a2.multiply(&b2).scale(-1),
        a2.scale(2 * p1s - p2s - p3s),
        c2.multiply(&a2).scale(-1),
        b2.scale(-p2s),
        c2.multiply(&b2),
        c2.scale(-p3s),
        Polynomial::constant(p2s * p3s),
    ]);
    let linear_2 = sum(&[
        b2.power(2),
        a2.multiply(&b2).scale(-1),
        b2.scale(2 * p2s - p1s - p3s),
        c2.multiply(&b2).scale(-1),
        a2.scale(-p1s),
        c2.multiply(&a2),
        c2.scale(-p3s),
        Polynomial::constant(p1s * p3s),
    ]);
    let linear_3 = sum(&[
        c2.power(2),
        a2.multiply(&b2),
        a2.scale(-p1s),
        c2.multiply(&a2).scale(-1),
        b2.scale(-p2s),
        c2.multiply(&b2).scale(-1),
        c2.scale(-p1s - p2s + 2 * p3s),
        Polynomial::constant(p1s * p2s),
    ]);
    (k, [linear_1, linear_2, linear_3])
}

fn cubic_parameter_derivative(values: &[Polynomial; 4]) -> Polynomial {
    // Exact derivative at zero for every polynomial of degree at most three.
    sum(&[
        values[0].scale(-11),
        values[1].scale(18),
        values[2].scale(-9),
        values[3].scale(2),
    ])
    .scale(inverse(6))
}

fn cm_parameter_derivative(momenta: [i64; 3], direction: usize) -> Polynomial {
    let values: Vec<_> = (0..4)
        .map(|step| {
            let mut shifted = momenta;
            shifted[direction] += step;
            cm_k_and_linears(shifted[0], shifted[1], shifted[2]).0
        })
        .collect();
    cubic_parameter_derivative(&[
        values[0].clone(),
        values[1].clone(),
        values[2].clone(),
        values[3].clone(),
    ])
}

fn cm_second_parameter_derivative(
    momenta: [i64; 3],
    first_direction: usize,
    second_direction: usize,
) -> Polynomial {
    let values: Vec<_> = (0..4)
        .map(|step| {
            let mut shifted = momenta;
            shifted[second_direction] += step;
            cm_parameter_derivative(shifted, first_direction)
        })
        .collect();
    cubic_parameter_derivative(&[
        values[0].clone(),
        values[1].clone(),
        values[2].clone(),
        values[3].clone(),
    ])
}

fn parameter_derivative_of<F>(momenta: [i64; 3], direction: usize, evaluate: &F) -> Polynomial
where
    F: Fn([i64; 3]) -> Polynomial,
{
    let values = [
        evaluate(momenta),
        {
            let mut shifted = momenta;
            shifted[direction] += 1;
            evaluate(shifted)
        },
        {
            let mut shifted = momenta;
            shifted[direction] += 2;
            evaluate(shifted)
        },
        {
            let mut shifted = momenta;
            shifted[direction] += 3;
            evaluate(shifted)
        },
    ];
    cubic_parameter_derivative(&values)
}

fn second_parameter_derivative_of<F>(
    momenta: [i64; 3],
    first: usize,
    second: usize,
    evaluate: &F,
) -> Polynomial
where
    F: Fn([i64; 3]) -> Polynomial,
{
    parameter_derivative_of(momenta, second, &|shifted| {
        parameter_derivative_of(shifted, first, evaluate)
    })
}

fn cyclic_trace_target(momenta: [i64; 3]) -> Polynomial {
    let z = Polynomial::variable(3);
    let (_, linears) = cm_k_and_linears(momenta[0], momenta[1], momenta[2]);
    sum(
        &(0..3)
            .map(|occurrence| {
                linears[occurrence]
                    .multiply(&z)
                    .scale(-1)
                    .add(
                        &linears[occurrence]
                            .multiply(&linears[occurrence])
                            .multiply(&z.power(2))
                            .scale(3 * momenta[occurrence]),
                    )
            })
            .collect::<Vec<_>>(),
    )
}

fn physical_naive_derivative(
    momenta: [i64; 3],
    direction: usize,
    occurrence: usize,
) -> Polynomial {
    let z = Polynomial::variable(3);
    let (k, linears) = cm_k_and_linears(momenta[0], momenta[1], momenta[2]);
    let dk = parameter_derivative_of(momenta, direction, &|shifted| {
        cm_k_and_linears(shifted[0], shifted[1], shifted[2]).0
    });
    let dl = parameter_derivative_of(momenta, direction, &|shifted| {
        cm_k_and_linears(shifted[0], shifted[1], shifted[2]).1[occurrence].clone()
    });
    let _ = k;
    dl.multiply(&z).subtract(
        &linears[occurrence]
            .multiply(&dk)
            .multiply(&z.power(2))
            .scale(3 * inverse(2)),
    )
}

fn cyclic_naive_derivative(momenta: [i64; 3], direction: usize) -> Polynomial {
    let z = Polynomial::variable(3);
    let target = cyclic_trace_target(momenta);
    let explicit = parameter_derivative_of(momenta, direction, &cyclic_trace_target);
    let dk = parameter_derivative_of(momenta, direction, &|shifted| {
        cm_k_and_linears(shifted[0], shifted[1], shifted[2]).0
    });
    explicit.subtract(&target.multiply(&dk).multiply(&z).scale(inverse(2)))
}

fn dual_groebner_audit(k: &Polynomial, dk: &Polynomial) {
    let z = Polynomial::variable(3);
    let seed = (0..3)
        .map(|variable| k.derivative(variable).scale(5))
        .chain(std::iter::once(
            z.multiply(k).subtract(&Polynomial::constant(1)),
        ))
        .collect::<Vec<_>>();
    let tangent_seed = (0..3)
        .map(|variable| dk.derivative(variable).scale(5))
        .chain(std::iter::once(z.multiply(dk)))
        .collect::<Vec<_>>();
    let dual_seed = seed
        .iter()
        .zip(&tangent_seed)
        .map(|(value, tangent)| DualPolynomial::from_pair(value, tangent))
        .collect::<Vec<_>>();
    let ordinary = tracked_groebner_basis(&seed);
    let dual = dual_tracked_groebner_basis(&dual_seed);
    assert_eq!(ordinary.len(), dual.len(), "dual basis length mismatch");
    let mut tangent_terms = 0_usize;
    for (ordinary_entry, dual_entry) in ordinary.iter().zip(&dual) {
        let (value, tangent) = dual_entry.polynomial.split();
        assert_eq!(ordinary_entry.polynomial, value, "dual basis value mismatch");
        tangent_terms += tangent.0.len();
        assert_eq!(
            dual_reconstruct_from_exact_trace(
                &DualPolynomial::default(),
                &dual_entry.provenance,
                &dual_seed,
            ),
            dual_entry.polynomial,
            "dual basis provenance mismatch",
        );
    }
    let ordinary_basis = ordinary
        .iter()
        .map(|entry| entry.polynomial.clone())
        .collect::<Vec<_>>();
    let targets = [
        (Polynomial::constant(1), Polynomial::default()),
        (Polynomial::variable(0), Polynomial::default()),
        (Polynomial::variable(1), Polynomial::default()),
        (Polynomial::variable(2), Polynomial::default()),
        (Polynomial::variable(3), Polynomial::default()),
        (k.clone(), dk.clone()),
        (k.multiply(&Polynomial::variable(3)), dk.multiply(&Polynomial::variable(3))),
    ];
    let mut target_tangent_terms = 0_usize;
    for (value, tangent) in &targets {
        let dual_target = DualPolynomial::from_pair(value, tangent);
        let (dual_remainder, trace) =
            dual_normal_form_with_exact_trace(dual_target.clone(), &dual, dual_seed.len());
        let (remainder_value, remainder_tangent) = dual_remainder.split();
        assert_eq!(
            normal_form(value.clone(), &ordinary_basis),
            remainder_value,
            "dual target remainder value mismatch",
        );
        target_tangent_terms += remainder_tangent.0.len();
        assert_eq!(
            dual_reconstruct_from_exact_trace(&dual_remainder, &trace, &dual_seed),
            dual_target,
            "dual target trace reconstruction mismatch",
        );
    }
    eprintln!(
        "DUAL_GROEBNER_AUDIT seed_count={} basis_count={} tangent_term_count={} target_count={} target_tangent_term_count={}",
        dual_seed.len(),
        dual.len(),
        tangent_terms,
        targets.len(),
        target_tangent_terms,
    );
}

fn dual_pair_from_evaluator<F>(
    momenta: [i64; 3],
    variation: usize,
    evaluate: &F,
) -> DualPolynomial
where
    F: Fn([i64; 3]) -> Polynomial,
{
    DualPolynomial::from_pair(
        &evaluate(momenta),
        &parameter_derivative_of(momenta, variation, evaluate),
    )
}

fn dual_rank_seven_matrices(
    momenta: [i64; 3],
    variation: usize,
) -> (Vec<Vec<Vec<DualScalar>>>, Vec<Vec<usize>>) {
    let z = Polynomial::variable(3);
    let (k, linears) = cm_k_and_linears(momenta[0], momenta[1], momenta[2]);
    let dk_variation = parameter_derivative_of(momenta, variation, &|shifted| {
        cm_k_and_linears(shifted[0], shifted[1], shifted[2]).0
    });
    let seed = (0..3)
        .map(|variable| k.derivative(variable).scale(5))
        .chain(std::iter::once(
            z.multiply(&k).subtract(&Polynomial::constant(1)),
        ))
        .collect::<Vec<_>>();
    let tangent_seed = (0..3)
        .map(|variable| dk_variation.derivative(variable).scale(5))
        .chain(std::iter::once(z.multiply(&dk_variation)))
        .collect::<Vec<_>>();
    let dual_seed = seed
        .iter()
        .zip(&tangent_seed)
        .map(|(value, tangent)| DualPolynomial::from_pair(value, tangent))
        .collect::<Vec<_>>();
    let dual_basis = dual_tracked_groebner_basis(&dual_seed);
    let ordinary_basis = dual_basis
        .iter()
        .map(|entry| entry.polynomial.split().0)
        .collect::<Vec<_>>();
    let monomials = standard_monomials(&ordinary_basis)
        .into_iter()
        .collect::<Vec<_>>();
    assert_eq!(monomials.len(), 7, "rank-seven standard monomial count");

    let mut frame_targets = Vec::new();
    for occurrence in 0..3 {
        let value = linears[occurrence].multiply(&z);
        let tangent = parameter_derivative_of(momenta, variation, &|shifted| {
            cm_k_and_linears(shifted[0], shifted[1], shifted[2]).1[occurrence]
                .multiply(&z)
        });
        frame_targets.push(DualPolynomial::from_pair(&value, &tangent));
    }
    frame_targets.push(dual_pair_from_evaluator(
        momenta,
        variation,
        &cyclic_trace_target,
    ));
    for fiber_variable in 0..3 {
        frame_targets.push(dual_pair_from_evaluator(
            momenta,
            variation,
            &|shifted| {
                parameter_derivative_of(shifted, 0, &|inner| {
                    cm_k_and_linears(inner[0], inner[1], inner[2]).0
                })
                .derivative(fiber_variable)
                .scale(5)
            },
        ));
    }

    let frame_reductions = frame_targets
        .iter()
        .map(|target| {
            dual_normal_form_with_exact_trace(target.clone(), &dual_basis, dual_seed.len())
        })
        .collect::<Vec<_>>();
    let frame_matrix = monomials
        .iter()
        .map(|monomial| {
            frame_reductions
                .iter()
                .map(|(remainder, _)| remainder.0.get(monomial).copied().unwrap_or_default())
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();

    let mut matrices = Vec::new();
    let mut pivot_packets = Vec::new();
    let retain_cross_grade = std::env::var("CM_RETAIN_EXACT_CROSS_GRADE")
        .ok()
        .as_deref()
        == Some("1");
    for direction in 0..3 {
        let di_k = parameter_derivative_of(momenta, direction, &|shifted| {
            cm_k_and_linears(shifted[0], shifted[1], shifted[2]).0
        });
        let dvariation_di_k = second_parameter_derivative_of(
            momenta,
            direction,
            variation,
            &|shifted| cm_k_and_linears(shifted[0], shifted[1], shifted[2]).0,
        );
        let mut exact_derivatives = (0..3)
            .map(|fiber_variable| {
                DualPolynomial::from_pair(
                    &di_k.derivative(fiber_variable).scale(5),
                    &dvariation_di_k.derivative(fiber_variable).scale(5),
                )
            })
            .collect::<Vec<_>>();
        exact_derivatives.push(DualPolynomial::from_pair(
            &z.multiply(&di_k),
            &z.multiply(&dvariation_di_k),
        ));

        let mut columns = Vec::new();
        let mut direction_pivots = Vec::new();
        for frame_index in 0..7 {
            let naive = if frame_index < 3 {
                dual_pair_from_evaluator(momenta, variation, &|shifted| {
                    physical_naive_derivative(shifted, direction, frame_index)
                })
            } else if frame_index == 3 {
                dual_pair_from_evaluator(momenta, variation, &|shifted| {
                    cyclic_naive_derivative(shifted, direction)
                })
            } else {
                let fiber_variable = frame_index - 4;
                dual_pair_from_evaluator(momenta, variation, &|shifted| {
                    second_parameter_derivative_of(
                        shifted,
                        0,
                        direction,
                        &|inner| cm_k_and_linears(inner[0], inner[1], inner[2]).0,
                    )
                    .derivative(fiber_variable)
                    .scale(5)
                })
            };
            let correction = frame_reductions[frame_index]
                .1
                .iter()
                .zip(&exact_derivatives)
                .fold(DualPolynomial::default(), |result, (primitive, derivative)| {
                    result.add(&primitive.multiply(derivative))
                });
            let lifted = if retain_cross_grade {
                naive
            } else {
                naive.subtract(&correction)
            };
            let (remainder, _) =
                dual_normal_form_with_exact_trace(lifted, &dual_basis, dual_seed.len());
            let right = monomials
                .iter()
                .map(|monomial| remainder.0.get(monomial).copied().unwrap_or_default())
                .collect::<Vec<_>>();
            let (coordinates, pivots) = dual_solve_square(&frame_matrix, &right);
            columns.push(coordinates);
            direction_pivots.push(pivots);
        }
        matrices.push(
            (0..7)
                .map(|row| (0..7).map(|column| columns[column][row]).collect())
                .collect(),
        );
        pivot_packets.push(direction_pivots.into_iter().next().unwrap());
    }
    (matrices, pivot_packets)
}

fn determinant_three(matrix: &[[Polynomial; 3]; 3]) -> Polynomial {
    sum(&[
        matrix[0][0].multiply(&matrix[1][1]).multiply(&matrix[2][2]),
        matrix[0][1].multiply(&matrix[1][2]).multiply(&matrix[2][0]),
        matrix[0][2].multiply(&matrix[1][0]).multiply(&matrix[2][1]),
        matrix[0][2]
            .multiply(&matrix[1][1])
            .multiply(&matrix[2][0])
            .scale(-1),
        matrix[0][1]
            .multiply(&matrix[1][0])
            .multiply(&matrix[2][2])
            .scale(-1),
        matrix[0][0]
            .multiply(&matrix[1][2])
            .multiply(&matrix[2][1])
            .scale(-1),
    ])
}

fn conormal_kodaira_spencer_packet(
    k: &Polynomial,
    momenta: [i64; 3],
) -> (Vec<Vec<Vec<i64>>>, Vec<Vec<Vec<i64>>>, Vec<Vec<i64>>, [usize; 3]) {
    let z = Polynomial::variable(3);
    let seed = (0..3)
        .map(|variable| k.derivative(variable).scale(5))
        .chain(std::iter::once(
            z.multiply(k).subtract(&Polynomial::constant(1)),
        ))
        .collect::<Vec<_>>();
    let basis = groebner_basis(seed.clone());
    let monomials = standard_monomials(&basis).into_iter().collect::<Vec<_>>();
    assert_eq!(monomials.len(), 7, "Kodaira--Spencer quotient length");
    let quotient_generator_nonzero = seed
        .iter()
        .filter(|generator| !normal_form((*generator).clone(), &basis).is_zero())
        .count();
    println!(
        "CONORMAL_KOSZUL_QUOTIENT_GENERATOR_NONZERO={quotient_generator_nonzero}"
    );
    let mixed_parameter_commutator_nonzero = [(0_usize, 1_usize), (0, 2), (1, 2)]
        .iter()
        .filter(|(left, right)| {
            !cm_second_parameter_derivative(momenta, *left, *right)
                .subtract(&cm_second_parameter_derivative(momenta, *right, *left))
                .is_zero()
        })
        .count();
    println!(
        "CONORMAL_MIXED_PARAMETER_COMMUTATOR_NONZERO={mixed_parameter_commutator_nonzero}"
    );
    let index = monomials
        .iter()
        .enumerate()
        .map(|(position, monomial)| (*monomial, position))
        .collect::<BTreeMap<_, _>>();
    let vector = |polynomial: Polynomial| {
        let reduced = normal_form(polynomial, &basis);
        let mut coordinates = vec![0_i64; monomials.len()];
        for (monomial, coefficient) in reduced.0 {
            coordinates[*index.get(&monomial).expect("KS standard monomial")] = coefficient;
        }
        coordinates
    };
    let sections = (0..3)
        .map(|direction| {
            let dk = cm_parameter_derivative(momenta, direction);
            let mut components = (0..3)
                .map(|fiber_variable| dk.derivative(fiber_variable).scale(5))
                .collect::<Vec<_>>();
            components.push(z.multiply(&dk));
            components
        })
        .collect::<Vec<_>>();
    let generator_pairs = [(0_usize, 1_usize), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)];
    let primitive_koszul_gauge_nonzero = sections
        .iter()
        .flat_map(|section| {
            generator_pairs.iter().map(|(left, right)| {
                normal_form(
                    seed[*right]
                        .multiply(&section[*left])
                        .subtract(&seed[*left].multiply(&section[*right])),
                    &basis,
                )
            })
        })
        .filter(|remainder| !remainder.is_zero())
        .count();
    println!(
        "CONORMAL_PRIMITIVE_KOSZUL_GAUGE_NONZERO={primitive_koszul_gauge_nonzero}"
    );
    let section_coordinates = sections
        .iter()
        .map(|section| section.iter().cloned().map(&vector).collect::<Vec<_>>())
        .collect::<Vec<_>>();
    let transitivity_columns = sections
        .iter()
        .flat_map(|section| {
            monomials.iter().map(|monomial| {
                let scalar = Polynomial::term(*monomial, 1);
                section
                    .iter()
                    .flat_map(|component| vector(component.multiply(&scalar)))
                    .collect::<Vec<_>>()
            })
        })
        .collect::<Vec<_>>();
    let transitivity_rows = (0..(4 * monomials.len()))
        .map(|row| {
            transitivity_columns
                .iter()
                .map(|column| column[row])
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();
    let transitivity_map_rank = matrix_rank(transitivity_rows.clone());
    let transitivity_kernel = matrix_nullspace(transitivity_rows.clone());
    let transitivity_cokernel_dual = matrix_nullspace(transitivity_columns.clone());
    println!("CONORMAL_TRANSITIVITY_MAP_RANK={transitivity_map_rank}");
    println!("CONORMAL_TRANSITIVITY_MATRIX={transitivity_rows:?}");
    println!("CONORMAL_TRANSITIVITY_KERNEL={transitivity_kernel:?}");
    println!("CONORMAL_TRANSITIVITY_COKERNEL_DUAL={transitivity_cokernel_dual:?}");
    let direction_pairs = [(0_usize, 1_usize), (0, 2), (1, 2)];
    let pair_coordinates = direction_pairs
        .iter()
        .map(|(left, right)| {
            generator_pairs
                .iter()
                .map(|(first, second)| {
                    vector(
                        sections[*left][*first]
                            .multiply(&sections[*right][*second])
                            .subtract(
                                &sections[*left][*second]
                                    .multiply(&sections[*right][*first]),
                            ),
                    )
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();
    let generator_triples = [(0_usize, 1_usize, 2_usize), (0, 1, 3), (0, 2, 3), (1, 2, 3)];
    let triple_coordinates = generator_triples
        .iter()
        .map(|(first, second, third)| {
            let matrix = [
                [
                    sections[0][*first].clone(),
                    sections[0][*second].clone(),
                    sections[0][*third].clone(),
                ],
                [
                    sections[1][*first].clone(),
                    sections[1][*second].clone(),
                    sections[1][*third].clone(),
                ],
                [
                    sections[2][*first].clone(),
                    sections[2][*second].clone(),
                    sections[2][*third].clone(),
                ],
            ];
            vector(determinant_three(&matrix))
        })
        .collect::<Vec<_>>();
    let rank_from_columns = |columns: Vec<Vec<i64>>| {
        let width = columns.len();
        let height = columns[0].len();
        matrix_rank(
            (0..height)
                .map(|row| (0..width).map(|column| columns[column][row]).collect())
                .collect(),
        )
    };
    let section_rank = rank_from_columns(
        section_coordinates
            .iter()
            .map(|section| section.iter().flatten().copied().collect())
            .collect(),
    );
    let pair_rank = rank_from_columns(
        pair_coordinates
            .iter()
            .map(|section| section.iter().flatten().copied().collect())
            .collect(),
    );
    let triple_rank = rank_from_columns(vec![triple_coordinates.iter().flatten().copied().collect()]);
    (
        section_coordinates,
        pair_coordinates,
        triple_coordinates,
        [section_rank, pair_rank, triple_rank],
    )
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

fn normal_tower_class_rank(
    k: &Polynomial,
    selected: &[Factor],
    labelled_coefficients: &[(&'static str, Polynomial)],
    direct_localized_classes: &[(&'static str, Polynomial)],
) -> (usize, usize, Vec<&'static str>, Vec<Vec<i64>>, u128) {
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
    let exact_seed = equations.clone();
    let basis = groebner_basis(equations);
    let provenance_corrected = std::env::var("CM_PROVENANCE_CORRECTED_DERIVATIVES")
        .ok()
        .as_deref()
        == Some("1");
    let tracked_basis = if std::env::var("CM_EXACT_LIFT_AUDIT").ok().as_deref()
        == Some("1") || provenance_corrected
    {
        let tracked = tracked_groebner_basis(&exact_seed);
        assert_eq!(tracked.len(), basis.len(), "tracked basis length mismatch");
        for (plain, tracked_entry) in basis.iter().zip(&tracked) {
            assert_eq!(plain, &tracked_entry.polynomial, "tracked basis order mismatch");
            assert_eq!(
                reconstruct_from_exact_trace(
                    &Polynomial::default(),
                    &tracked_entry.provenance,
                    &exact_seed,
                ),
                tracked_entry.polynomial,
                "tracked basis provenance mismatch",
            );
        }
        Some(tracked)
    } else {
        None
    };
    let monomials: Vec<_> = standard_monomials(&basis).into_iter().collect();
    let index: BTreeMap<_, _> = monomials
        .iter()
        .enumerate()
        .map(|(position, monomial)| (*monomial, position))
        .collect();

    // In the localized quotient z*(K*marks)=1, hence K^{-1}=z*marks.
    let mark_product = product(
        &selected
            .iter()
            .map(|factor| factor.polynomial.clone())
            .collect::<Vec<_>>(),
    );
    let inverse_k = Polynomial::variable(3).multiply(&mark_product);
    let mut all_direct = direct_localized_classes.to_vec();
    if provenance_corrected {
        let tracked = tracked_basis.as_ref().expect("provenance basis");
        let frame = [
            "physical_nu1",
            "physical_nu2",
            "physical_nu3",
            "cyclic_trace_2*K^-1/2",
            "d1_exact_gradient_a",
            "d1_exact_gradient_b",
            "d1_exact_gradient_c",
        ];
        let corrected_labels = [
            [
                "lifted_nabla_1_physical_nu1",
                "lifted_nabla_1_physical_nu2",
                "lifted_nabla_1_physical_nu3",
                "lifted_nabla_1_cyclic_trace",
                "lifted_nabla_1_d1_exact_gradient_a",
                "lifted_nabla_1_d1_exact_gradient_b",
                "lifted_nabla_1_d1_exact_gradient_c",
            ],
            [
                "lifted_nabla_2_physical_nu1",
                "lifted_nabla_2_physical_nu2",
                "lifted_nabla_2_physical_nu3",
                "lifted_nabla_2_cyclic_trace",
                "lifted_nabla_2_d1_exact_gradient_a",
                "lifted_nabla_2_d1_exact_gradient_b",
                "lifted_nabla_2_d1_exact_gradient_c",
            ],
            [
                "lifted_nabla_3_physical_nu1",
                "lifted_nabla_3_physical_nu2",
                "lifted_nabla_3_physical_nu3",
                "lifted_nabla_3_cyclic_trace",
                "lifted_nabla_3_d1_exact_gradient_a",
                "lifted_nabla_3_d1_exact_gradient_b",
                "lifted_nabla_3_d1_exact_gradient_c",
            ],
        ];
        for (frame_index, frame_name) in frame.iter().enumerate() {
            let frame_target = if let Some((_, coefficient)) = labelled_coefficients
                .iter()
                .find(|(name, _)| name == frame_name)
            {
                coefficient.multiply(&inverse_k)
            } else {
                all_direct
                    .iter()
                    .find(|(name, _)| name == frame_name)
                    .expect("missing provenance frame class")
                    .1
                    .clone()
            };
            let (_, trace) =
                normal_form_with_exact_trace(frame_target, tracked, exact_seed.len());
            for direction in 0..3 {
                let naive_name = if frame_index < 3 {
                    match direction {
                        0 => ["nabla_1_physical_nu1", "nabla_1_physical_nu2", "nabla_1_physical_nu3"][frame_index],
                        1 => ["nabla_2_physical_nu1", "nabla_2_physical_nu2", "nabla_2_physical_nu3"][frame_index],
                        _ => ["nabla_3_physical_nu1", "nabla_3_physical_nu2", "nabla_3_physical_nu3"][frame_index],
                    }
                } else if frame_index == 3 {
                    ["nabla_1_cyclic_trace", "nabla_2_cyclic_trace", "nabla_3_cyclic_trace"][direction]
                } else {
                    let fiber = frame_index - 4;
                    match direction {
                        0 => ["d1_d1_exact_gradient_a", "d1_d1_exact_gradient_b", "d1_d1_exact_gradient_c"][fiber],
                        1 => ["d2_d1_exact_gradient_a", "d2_d1_exact_gradient_b", "d2_d1_exact_gradient_c"][fiber],
                        _ => ["d3_d1_exact_gradient_a", "d3_d1_exact_gradient_b", "d3_d1_exact_gradient_c"][fiber],
                    }
                };
                let naive = all_direct
                    .iter()
                    .find(|(name, _)| *name == naive_name)
                    .expect("missing naive derivative class")
                    .1
                    .clone();
                let derivative_names = match direction {
                    0 => ["d1_exact_gradient_a", "d1_exact_gradient_b", "d1_exact_gradient_c", "d1_exact_localization"],
                    1 => ["d2_exact_gradient_a", "d2_exact_gradient_b", "d2_exact_gradient_c", "d2_exact_localization"],
                    _ => ["d3_exact_gradient_a", "d3_exact_gradient_b", "d3_exact_gradient_c", "d3_exact_localization"],
                };
                let correction = sum(
                    &trace
                        .iter()
                        .zip(derivative_names)
                        .map(|(primitive, derivative_name)| {
                            let derivative = all_direct
                                .iter()
                                .find(|(name, _)| *name == derivative_name)
                                .expect("missing exact-generator derivative")
                                .1
                                .clone();
                            primitive.multiply(&derivative)
                        })
                        .collect::<Vec<_>>(),
                );
                all_direct.push((corrected_labels[direction][frame_index], naive.subtract(&correction)));
            }
        }
    }
    let class_count = labelled_coefficients.len() + all_direct.len();
    let mut rows = vec![vec![0_i64; class_count]; monomials.len()];
    let mut exact_trace_term_count = 0_usize;
    let mut exact_trace_nonzero_components = 0_usize;
    for (column, (_, coefficient)) in labelled_coefficients.iter().enumerate() {
        let target = coefficient.multiply(&inverse_k);
        let reduced = normal_form(target.clone(), &basis);
        if let Some(tracked) = &tracked_basis {
            let (tracked_remainder, trace) =
                normal_form_with_exact_trace(target.clone(), tracked, exact_seed.len());
            assert_eq!(tracked_remainder, reduced, "labelled tracked remainder mismatch");
            assert_eq!(
                reconstruct_from_exact_trace(&tracked_remainder, &trace, &exact_seed),
                target,
                "labelled exact trace reconstruction mismatch",
            );
            exact_trace_term_count += trace.iter().map(|entry| entry.0.len()).sum::<usize>();
            exact_trace_nonzero_components += trace.iter().filter(|entry| !entry.is_zero()).count();
        }
        for (monomial, value) in reduced.0 {
            rows[*index.get(&monomial).expect("standard remainder monomial")][column] = value;
        }
    }
    for (offset, (_, class)) in all_direct.iter().enumerate() {
        let column = labelled_coefficients.len() + offset;
        let reduced = normal_form(class.clone(), &basis);
        if let Some(tracked) = &tracked_basis {
            let (tracked_remainder, trace) =
                normal_form_with_exact_trace(class.clone(), tracked, exact_seed.len());
            assert_eq!(tracked_remainder, reduced, "direct tracked remainder mismatch");
            assert_eq!(
                reconstruct_from_exact_trace(&tracked_remainder, &trace, &exact_seed),
                class.clone(),
                "direct exact trace reconstruction mismatch",
            );
            exact_trace_term_count += trace.iter().map(|entry| entry.0.len()).sum::<usize>();
            exact_trace_nonzero_components += trace.iter().filter(|entry| !entry.is_zero()).count();
        }
        for (monomial, value) in reduced.0 {
            rows[*index.get(&monomial).expect("standard remainder monomial")][column] = value;
        }
    }
    let class_rank = matrix_rank(rows.clone());
    if tracked_basis.is_some() {
        eprintln!(
            "EXACT_LIFT_AUDIT seed_count={} basis_count={} class_count={} trace_nonzero_components={} trace_term_count={}",
            exact_seed.len(),
            basis.len(),
            class_count,
            exact_trace_nonzero_components,
            exact_trace_term_count,
        );
    }
    let kernel = matrix_nullspace(rows)
        .into_iter()
        .map(|vector| vector.into_iter().map(signed_residue).collect())
        .collect();
    (
        monomials.len(),
        class_rank,
        labelled_coefficients
            .iter()
            .chain(all_direct.iter())
            .map(|(name, _)| *name)
            .collect(),
        kernel,
        started.elapsed().as_millis(),
    )
}

fn restricted_normal_tower_class_rank(
    k: &Polynomial,
    wall: &Polynomial,
    selected: &[Factor],
    labelled_coefficients: &[(&'static str, Polynomial)],
) -> (usize, usize, Vec<Vec<i64>>, u128) {
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
    let mut equations = vec![wall.clone()];
    for direction in [[0_i64, 1, 0], [0_i64, 0, 1]] {
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
                    .multiply(&directional_derivative(&factor.polynomial, direction))
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
    let wall_basis = vec![wall.monic()];
    let mut eliminated = vec![wall.monic()];
    eliminated.extend(
        equations
            .into_iter()
            .skip(1)
            .map(|equation| normal_form(equation, &wall_basis)),
    );
    let started = Instant::now();
    let basis = groebner_basis(eliminated);
    let monomials: Vec<_> = standard_monomials(&basis).into_iter().collect();
    let index: BTreeMap<_, _> = monomials
        .iter()
        .enumerate()
        .map(|(position, monomial)| (*monomial, position))
        .collect();
    let mark_product = product(
        &selected
            .iter()
            .map(|factor| factor.polynomial.clone())
            .collect::<Vec<_>>(),
    );
    let inverse_k = normal_form(Polynomial::variable(3).multiply(&mark_product), &wall_basis);
    let mut rows = vec![vec![0_i64; labelled_coefficients.len()]; monomials.len()];
    for (column, (_, coefficient)) in labelled_coefficients.iter().enumerate() {
        let restricted = normal_form(coefficient.clone(), &wall_basis);
        let reduced = normal_form(restricted.multiply(&inverse_k), &basis);
        for (monomial, value) in reduced.0 {
            rows[*index.get(&monomial).expect("standard remainder monomial")][column] = value;
        }
    }
    let class_rank = matrix_rank(rows.clone());
    let kernel = matrix_nullspace(rows)
        .into_iter()
        .map(|vector| vector.into_iter().map(signed_residue).collect())
        .collect();
    (
        monomials.len(),
        class_rank,
        kernel,
        started.elapsed().as_millis(),
    )
}

fn directional_derivative(polynomial: &Polynomial, direction: [i64; 3]) -> Polynomial {
    (0..3).fold(Polynomial::default(), |sum, variable| {
        sum.add(&polynomial.derivative(variable).scale(direction[variable]))
    })
}

fn tangential_wall_basis(
    k: &Polynomial,
    k_exponent: i64,
    wall: &Polynomial,
    selected: &[Factor],
) -> (BTreeSet<Monomial>, usize, u128) {
    let mut factors = vec![Factor {
        name: "K",
        polynomial: k.clone(),
        exponent: k_exponent,
    }];
    factors.extend_from_slice(selected);
    let divisor = product(
        &factors
            .iter()
            .map(|factor| factor.polynomial.clone())
            .collect::<Vec<_>>(),
    );
    let mut equations = vec![wall.clone()];
    // q_g1=c+b+X1.  Tangent directions are d/da and d/db-d/dc.
    for direction in [[0_i64, 1, 0], [-1_i64, 0, 1]] {
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
                    .multiply(&directional_derivative(&factor.polynomial, direction))
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
    // Eliminate the redundant wall-normal coordinate before Buchberger.
    // Keeping q_g1 as the first basis element preserves the quotient while
    // preventing avoidable c-bearing S-polynomial growth.
    let wall_basis = vec![wall.monic()];
    let mut eliminated = vec![wall.monic()];
    eliminated.extend(
        equations
            .into_iter()
            .skip(1)
            .map(|equation| normal_form(equation, &wall_basis)),
    );
    let started = Instant::now();
    let basis = groebner_basis(eliminated);
    let elapsed = started.elapsed().as_millis();
    (standard_monomials(&basis), basis.len(), elapsed)
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
        "HOMA" => (2_i64, 3_i64, 4_i64, 2_i64, 3_i64, 4_i64),
        "HOMB" => (3_i64, 5_i64, 6_i64, 3_i64, 5_i64, 6_i64),
        "SOFT1" => (0_i64, 3_i64, 4_i64, 5_i64, 7_i64, 11_i64),
        _ => panic!("KINEMATIC_POINT must be A, B, HOMA, HOMB, or SOFT1"),
    };
    let (p1s, p2s, p3s) = if let Ok(raw) = std::env::var("CM_P_SQUARES") {
        let values = raw
            .split(',')
            .map(|value| value.trim().parse::<i64>().expect("CM_P_SQUARES integer"))
            .collect::<Vec<_>>();
        assert_eq!(values.len(), 3, "CM_P_SQUARES requires three integers");
        (values[0], values[1], values[2])
    } else {
        (p1 * p1, p2 * p2, p3 * p3)
    };
    let (k, normal_linears) = cm_k_and_linears(p1s, p2s, p3s);
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
            polynomial: sum(&[c.clone(), b, Polynomial::constant(x2 + x3)]),
            exponent: 29,
        },
    ];
    if matches!(
        std::env::var("NORMAL_TOWER").ok().as_deref(),
        Some("1") | Some("restricted")
    ) {
        let [linear_1, linear_2, linear_3] = normal_linears;
        let first_normal_horizontality =
            std::env::var("CM_FIRST_NORMAL_HORIZONTAL").ok().as_deref() == Some("1");
        let z = Polynomial::variable(3);
        let labelled_coefficients = if first_normal_horizontality {
            vec![
                // normal_tower_class_rank multiplies every labelled
                // coefficient by inverse_k before reduction. Supplying bare
                // L_i here therefore represents the physical L_i/K class.
                ("physical_nu1", linear_1.clone()),
                ("physical_nu2", linear_2.clone()),
                ("physical_nu3", linear_3.clone()),
            ]
        } else {
            vec![
            ("nu1", linear_1.clone()),
            ("nu2", linear_2.clone()),
            ("nu3", linear_3.clone()),
            ("nu1^2", a2.clone()),
            ("nu2^2", b2.clone()),
            ("nu3^2", c2.clone()),
            (
                "nu1*nu2",
                sum(&[Polynomial::constant(p3s), a2.scale(-1), b2.scale(-1)]),
            ),
            (
                "nu1*nu3",
                sum(&[Polynomial::constant(p2s), a2.scale(-1), c2.scale(-1)]),
            ),
            (
                "nu2*nu3",
                sum(&[Polynomial::constant(p1s), b2.scale(-1), c2.scale(-1)]),
            ),
            ("nu1*nu2*nu3", Polynomial::constant(1)),
            ]
        };
        let direct_localized_classes =
            if first_normal_horizontality {
                let momenta = [p1s, p2s, p3s];
                let linears = [&linear_1, &linear_2, &linear_3];
                let mut classes = Vec::new();
                for direction in 0..3 {
                    let samples: Vec<_> = (0..4)
                        .map(|step| {
                            let mut shifted = momenta;
                            shifted[direction] += step;
                            cm_k_and_linears(shifted[0], shifted[1], shifted[2])
                        })
                        .collect();
                    let k_values = [
                        samples[0].0.clone(),
                        samples[1].0.clone(),
                        samples[2].0.clone(),
                        samples[3].0.clone(),
                    ];
                    let dk = cubic_parameter_derivative(&k_values);
                    for occurrence in 0..3 {
                        let line_values = [
                            samples[0].1[occurrence].clone(),
                            samples[1].1[occurrence].clone(),
                            samples[2].1[occurrence].clone(),
                            samples[3].1[occurrence].clone(),
                        ];
                        let dl = cubic_parameter_derivative(&line_values);
                        let derivative = dl
                            .multiply(&z)
                            .subtract(
                                &linears[occurrence]
                                    .multiply(&dk)
                                    .multiply(&z.power(2))
                                    .scale(3 * inverse(2)),
                            );
                        let name = match (direction, occurrence) {
                            (0, 0) => "nabla_1_physical_nu1",
                            (0, 1) => "nabla_1_physical_nu2",
                            (0, _) => "nabla_1_physical_nu3",
                            (1, 0) => "nabla_2_physical_nu1",
                            (1, 1) => "nabla_2_physical_nu2",
                            (1, _) => "nabla_2_physical_nu3",
                            (2, 0) => "nabla_3_physical_nu1",
                            (2, 1) => "nabla_3_physical_nu2",
                            _ => "nabla_3_physical_nu3",
                        };
                        classes.push((name, derivative));
                    }
                }
                let derivative_count = std::env::var("CM_FIRST_NORMAL_DERIVATIVE_COUNT")
                    .ok()
                    .and_then(|value| value.parse::<usize>().ok())
                    .unwrap_or(classes.len());
                classes.truncate(derivative_count.min(classes.len()));
                let include_cyclic =
                    std::env::var("CM_FIRST_NORMAL_INCLUDE_CYCLIC").ok().as_deref()
                        == Some("1");
                let include_cyclic_derivatives =
                    std::env::var("CM_FIRST_NORMAL_INCLUDE_CYCLIC_DERIVATIVES")
                        .ok()
                        .as_deref()
                        == Some("1");
                if include_cyclic || include_cyclic_derivatives {
                    let physical_second = |linear: &Polynomial, momentum_squared: i64| {
                        linear
                            .multiply(&z)
                            .scale(-1)
                            .add(
                                &linear
                                    .multiply(linear)
                                    .multiply(&z.power(2))
                                    .scale(3 * momentum_squared),
                            )
                    };
                    let cyclic_trace = sum(&[
                        physical_second(&linear_1, p1s),
                        physical_second(&linear_2, p2s),
                        physical_second(&linear_3, p3s),
                    ]);
                    classes.push(("cyclic_trace_2*K^-1/2", cyclic_trace.clone()));
                    if include_cyclic_derivatives {
                        let momenta = [p1s, p2s, p3s];
                        for direction in 0..3 {
                            let samples: Vec<_> = (0..4)
                                .map(|step| {
                                    let mut shifted = momenta;
                                    shifted[direction] += step;
                                    cm_k_and_linears(shifted[0], shifted[1], shifted[2])
                                })
                                .collect();
                            let k_values = [
                                samples[0].0.clone(),
                                samples[1].0.clone(),
                                samples[2].0.clone(),
                                samples[3].0.clone(),
                            ];
                            let dk = cubic_parameter_derivative(&k_values);
                            let mut da = Polynomial::constant(0);
                            for occurrence in 0..3 {
                                let line_values = [
                                    samples[0].1[occurrence].clone(),
                                    samples[1].1[occurrence].clone(),
                                    samples[2].1[occurrence].clone(),
                                    samples[3].1[occurrence].clone(),
                                ];
                                let dl = cubic_parameter_derivative(&line_values);
                                let l = &samples[0].1[occurrence];
                                let delta_p = if occurrence == direction { 1 } else { 0 };
                                da = da.add(&dl.multiply(&z).scale(-1));
                                da = da.add(&l.multiply(&dk).multiply(&z.power(2)));
                                da = da.add(
                                    &l.multiply(l)
                                        .multiply(&z.power(2))
                                        .scale(3 * delta_p),
                                );
                                da = da.add(
                                    &l.multiply(&dl)
                                        .multiply(&z.power(2))
                                        .scale(6 * momenta[occurrence]),
                                );
                                da = da.add(
                                    &l.multiply(l)
                                        .multiply(&dk)
                                        .multiply(&z.power(3))
                                        .scale(-6 * momenta[occurrence]),
                                );
                            }
                            let covariant = da.subtract(
                                &cyclic_trace
                                    .multiply(&dk)
                                    .multiply(&z)
                                    .scale(inverse(2)),
                            );
                            let name = match direction {
                                0 => "nabla_1_cyclic_trace",
                                1 => "nabla_2_cyclic_trace",
                                _ => "nabla_3_cyclic_trace",
                            };
                            classes.push((name, covariant));
                        }
                    }
                }
                if std::env::var("CM_EXACT_GENERATOR_DERIVATIVES")
                    .ok()
                    .as_deref()
                    == Some("1")
                {
                    let momenta = [p1s, p2s, p3s];
                    let mut exact_derivative_classes = Vec::new();
                    for direction in 0..3 {
                        let samples: Vec<_> = (0..4)
                            .map(|step| {
                                let mut shifted = momenta;
                                shifted[direction] += step;
                                cm_k_and_linears(shifted[0], shifted[1], shifted[2]).0
                            })
                            .collect();
                        let k_values = [
                            samples[0].clone(),
                            samples[1].clone(),
                            samples[2].clone(),
                            samples[3].clone(),
                        ];
                        let dk = cubic_parameter_derivative(&k_values);
                        for fiber_variable in 0..3 {
                            let gradient_values = [
                                samples[0].derivative(fiber_variable).scale(5),
                                samples[1].derivative(fiber_variable).scale(5),
                                samples[2].derivative(fiber_variable).scale(5),
                                samples[3].derivative(fiber_variable).scale(5),
                            ];
                            let derivative = cubic_parameter_derivative(&gradient_values);
                            let name = match (direction, fiber_variable) {
                                (0, 0) => "d1_exact_gradient_a",
                                (0, 1) => "d1_exact_gradient_b",
                                (0, _) => "d1_exact_gradient_c",
                                (1, 0) => "d2_exact_gradient_a",
                                (1, 1) => "d2_exact_gradient_b",
                                (1, _) => "d2_exact_gradient_c",
                                (2, 0) => "d3_exact_gradient_a",
                                (2, 1) => "d3_exact_gradient_b",
                                _ => "d3_exact_gradient_c",
                            };
                            exact_derivative_classes.push((name, derivative));
                        }
                        let localization_name = match direction {
                            0 => "d1_exact_localization",
                            1 => "d2_exact_localization",
                            _ => "d3_exact_localization",
                        };
                        exact_derivative_classes.push((localization_name, dk.multiply(&z)));
                    }
                    if std::env::var("CM_EXACT_GENERATOR_SECOND_DERIVATIVES")
                        .ok()
                        .as_deref()
                        == Some("1")
                    {
                        let second_labels = [
                            [
                                "d1_d1_exact_gradient_a",
                                "d1_d1_exact_gradient_b",
                                "d1_d1_exact_gradient_c",
                            ],
                            [
                                "d2_d1_exact_gradient_a",
                                "d2_d1_exact_gradient_b",
                                "d2_d1_exact_gradient_c",
                            ],
                            [
                                "d3_d1_exact_gradient_a",
                                "d3_d1_exact_gradient_b",
                                "d3_d1_exact_gradient_c",
                            ],
                        ];
                        for direction in 0..3 {
                            let second = cm_second_parameter_derivative(momenta, 0, direction);
                            for fiber_variable in 0..3 {
                                exact_derivative_classes.push((
                                    second_labels[direction][fiber_variable],
                                    second.derivative(fiber_variable).scale(5),
                                ));
                            }
                        }
                    }
                    let requested = std::env::var("CM_EXACT_GENERATOR_DERIVATIVE_COUNT")
                        .ok()
                        .and_then(|value| value.parse::<usize>().ok())
                        .unwrap_or(exact_derivative_classes.len())
                        .min(exact_derivative_classes.len());
                    classes.extend(exact_derivative_classes.into_iter().take(requested));
                }
                classes
            } else if std::env::var("CM_TOTAL_ENERGY_SECOND").ok().as_deref() == Some("1") {
                let l3_over_k = linear_3.multiply(&z);
                let p3_l3_squared_over_k_squared = linear_3
                    .multiply(&linear_3)
                    .multiply(&z.power(2))
                    .scale(p3s);
                vec![
                    (
                        "E_T^2_period_K^-5",
                        l3_over_k
                            .scale(-5)
                            .add(&p3_l3_squared_over_k_squared.scale(60)),
                    ),
                    (
                        // Twice the physical K^(-1/2) coefficient, avoiding a
                        // modular inverse of two without changing its line.
                        "2*E_T^2_period_K^-1/2",
                        l3_over_k
                            .scale(-1)
                            .add(&p3_l3_squared_over_k_squared.scale(3)),
                    ),
                ]
            } else if matches!(
                std::env::var("CM_CYCLIC_SECOND").ok().as_deref(),
                Some("1") | Some("horizontal")
            ) {
                let physical_second = |linear: &Polynomial, momentum_squared: i64| {
                    linear
                        .multiply(&z)
                        .scale(-1)
                        .add(
                            &linear
                                .multiply(linear)
                                .multiply(&z.power(2))
                                .scale(3 * momentum_squared),
                        )
                };
                let cyclic_trace = sum(&[
                    physical_second(&linear_1, p1s),
                    physical_second(&linear_2, p2s),
                    physical_second(&linear_3, p3s),
                ]);
                let mut classes = vec![(
                    // Twice the physical K^(-1/2) second coefficient, traced
                    // over the three labelled momentum-normal occurrences.
                    "cyclic_trace_2*K^-1/2",
                    cyclic_trace.clone(),
                )];
                if std::env::var("CM_CYCLIC_SECOND").ok().as_deref() == Some("horizontal") {
                    let momenta = [p1s, p2s, p3s];
                    for direction in 0..3 {
                        let samples: Vec<_> = (0..4)
                            .map(|step| {
                                let mut shifted = momenta;
                                shifted[direction] += step;
                                cm_k_and_linears(shifted[0], shifted[1], shifted[2])
                            })
                            .collect();
                        let k_values = [
                            samples[0].0.clone(),
                            samples[1].0.clone(),
                            samples[2].0.clone(),
                            samples[3].0.clone(),
                        ];
                        let dk = cubic_parameter_derivative(&k_values);
                        let mut da = Polynomial::constant(0);
                        for occurrence in 0..3 {
                            let line_values = [
                                samples[0].1[occurrence].clone(),
                                samples[1].1[occurrence].clone(),
                                samples[2].1[occurrence].clone(),
                                samples[3].1[occurrence].clone(),
                            ];
                            let dl = cubic_parameter_derivative(&line_values);
                            let l = &samples[0].1[occurrence];
                            let delta_p = if occurrence == direction { 1 } else { 0 };
                            da = da.add(&dl.multiply(&z).scale(-1));
                            da = da.add(&l.multiply(&dk).multiply(&z.power(2)));
                            da = da.add(
                                &l.multiply(l)
                                    .multiply(&z.power(2))
                                    .scale(3 * delta_p),
                            );
                            da = da.add(
                                &l.multiply(&dl)
                                    .multiply(&z.power(2))
                                    .scale(6 * momenta[occurrence]),
                            );
                            da = da.add(
                                &l.multiply(l)
                                    .multiply(&dk)
                                    .multiply(&z.power(3))
                                    .scale(-6 * momenta[occurrence]),
                            );
                        }
                        // Gauss--Manin derivative of A*K^(-1/2).
                        let covariant = da.subtract(
                            &cyclic_trace
                                .multiply(&dk)
                                .multiply(&z)
                                .scale(inverse(2)),
                        );
                        let name = match direction {
                            0 => "nabla_p1sq_cyclic_trace",
                            1 => "nabla_p2sq_cyclic_trace",
                            _ => "nabla_p3sq_cyclic_trace",
                        };
                        classes.push((name, covariant));
                    }
                }
                classes
            } else {
                Vec::new()
            };
        if std::env::var("CM_DUAL_GROEBNER_AUDIT").ok().as_deref() == Some("1") {
            let direction = std::env::var("CM_DUAL_DIRECTION")
                .ok()
                .and_then(|value| value.parse::<usize>().ok())
                .unwrap_or(0);
            assert!(direction < 3, "CM_DUAL_DIRECTION must be 0, 1, or 2");
            let dk = cm_parameter_derivative([p1s, p2s, p3s], direction);
            dual_groebner_audit(&k, &dk);
        }
        if std::env::var("CM_DUAL_RANK7_MATRICES").ok().as_deref() == Some("1") {
            let variation = std::env::var("CM_DUAL_DIRECTION")
                .ok()
                .and_then(|value| value.parse::<usize>().ok())
                .unwrap_or(0);
            assert!(variation < 3, "CM_DUAL_DIRECTION must be 0, 1, or 2");
            let (dual_matrices, pivots) =
                dual_rank_seven_matrices([p1s, p2s, p3s], variation);
            let values = dual_matrices
                .iter()
                .map(|matrix| {
                    matrix
                        .iter()
                        .map(|row| row.iter().map(|entry| entry.value).collect::<Vec<_>>())
                        .collect::<Vec<_>>()
                })
                .collect::<Vec<_>>();
            let tangents = dual_matrices
                .iter()
                .map(|matrix| {
                    matrix
                        .iter()
                        .map(|row| row.iter().map(|entry| entry.tangent).collect::<Vec<_>>())
                        .collect::<Vec<_>>()
                })
                .collect::<Vec<_>>();
            println!("DUAL_RANK7_VALUES={values:?}");
            println!("DUAL_RANK7_TANGENTS={tangents:?}");
            println!("DUAL_RANK7_PIVOTS={pivots:?}");
        }
        if std::env::var("CM_CONORMAL_KS_PACKET").ok().as_deref() == Some("1") {
            let (sections, pairs, triple, ranks) =
                conormal_kodaira_spencer_packet(&k, [p1s, p2s, p3s]);
            println!("CONORMAL_KS_SECTIONS={sections:?}");
            println!("CONORMAL_KS_PAIRS={pairs:?}");
            println!("CONORMAL_KS_TRIPLE={triple:?}");
            println!("CONORMAL_KS_RANKS={ranks:?}");
        }
        let mode = std::env::var("NORMAL_TOWER").expect("normal tower mode");
        let labels = labelled_coefficients
            .iter()
            .chain(direct_localized_classes.iter())
            .map(|(name, _)| *name)
            .collect::<Vec<_>>();
        let (cohomology_rank, class_rank, output_labels, kernel, elapsed_ms) = if mode == "restricted" {
            let q_g12 = sum(&[c.clone(), Polynomial::constant(x1 + x2 + x3)]);
            let (rank, class_rank, kernel, elapsed_ms) =
                restricted_normal_tower_class_rank(&k, &q_g12, &denominators, &labelled_coefficients);
            (rank, class_rank, labels.clone(), kernel, elapsed_ms)
        } else {
            let (rank, class_rank, computed_labels, kernel, elapsed_ms) =
                normal_tower_class_rank(&k, &[], &labelled_coefficients, &direct_localized_classes);
            (rank, class_rank, computed_labels, kernel, elapsed_ms)
        };
        println!(
            "prime={} point={point} normal_tower_mode={mode} cohomology_rank={cohomology_rank} labelled_class_rank={class_rank} label_count={} elapsed_ms={elapsed_ms}",
            prime(), output_labels.len()
        );
        println!("NORMAL_TOWER_LABELS={output_labels:?}");
        println!("NORMAL_TOWER_KERNEL={kernel:?}");
        return;
    }
    if std::env::var("TANGENTIAL_WALL").ok().as_deref() == Some("q_g1") {
        // q_g23 restricts to the nonzero constant X2+X3-X1 on q_g1, hence it
        // contributes no tangential logarithmic derivative.
        let tangential_marks =
            std::env::var("TANGENTIAL_MARKS").unwrap_or_else(|_| "full".to_owned());
        let selected = match tangential_marks.as_str() {
            "full" => vec![denominators[1].clone(), denominators[2].clone()],
            "q_g2" => vec![denominators[1].clone()],
            "q_g3" => vec![denominators[2].clone()],
            "none" => Vec::new(),
            _ => panic!("TANGENTIAL_MARKS must be none, q_g2, q_g3, or full"),
        };
        let tangential_k_weight =
            std::env::var("TANGENTIAL_K_WEIGHT").unwrap_or_else(|_| "generic".to_owned());
        let k_exponent = match tangential_k_weight.as_str() {
            "generic" => 5,
            "half" => inverse(2),
            _ => panic!("TANGENTIAL_K_WEIGHT must be generic or half"),
        };
        let (monomials, basis_size, elapsed_ms) =
            tangential_wall_basis(&k, k_exponent, &denominators[0].polynomial, &selected);
        let expected_rank = match tangential_marks.as_str() {
            "none" => 5,
            "q_g2" | "q_g3" => 6,
            "full" => 8,
            _ => unreachable!(),
        };
        assert_eq!(monomials.len(), expected_rank);
        println!(
            "prime={} point={point} tangential_wall=q_g1 k_weight={tangential_k_weight} marks={tangential_marks} rank={} basis_size={basis_size} elapsed_ms={elapsed_ms}",
            prime(), monomials.len(),
        );
        println!(
            "STANDARD_MONOMIALS={:?}",
            monomials.into_iter().collect::<Vec<_>>()
        );
        return;
    }
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
        let names = selected
            .iter()
            .map(|factor| factor.name)
            .collect::<Vec<_>>();
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
        if matches!(point.as_str(), "A" | "B") {
            assert_eq!(
                closed,
                [7, 12, 12, 18, 12, 18, 18, 26, 12, 17, 18, 24, 18, 24, 26, 34]
            );
            assert_eq!(proper, [7, 5, 5, 1, 5, 1, 1, 1, 5, 0, 1, 0, 1, 0, 1, 0]);
        } else if matches!(point.as_str(), "HOMA" | "HOMB") {
            assert_eq!(
                closed,
                [7, 8, 8, 9, 8, 9, 9, 11, 11, 12, 12, 13, 12, 13, 13, 15]
            );
            assert_eq!(proper, [7, 1, 1, 0, 1, 0, 0, 1, 4, 0, 0, 0, 0, 0, 0, 0]);
        }
        println!("DELETION_CLOSED={closed:?}");
        println!("PROPER_SUPPORT_GRADES={proper:?}");
    }
}
