use std::collections::BTreeMap;

#[derive(Clone, Copy, Debug, Default)]
struct C {
    re: f64,
    im: f64,
}

impl C {
    fn new(re: f64, im: f64) -> Self { Self { re, im } }
    fn abs(self) -> f64 { (self.re * self.re + self.im * self.im).sqrt() }
}

impl std::ops::Add for C {
    type Output = Self;
    fn add(self, rhs: Self) -> Self { Self::new(self.re + rhs.re, self.im + rhs.im) }
}
impl std::ops::Mul for C {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self {
        Self::new(self.re * rhs.re - self.im * rhs.im, self.re * rhs.im + self.im * rhs.re)
    }
}
impl std::ops::Mul<f64> for C {
    type Output = Self;
    fn mul(self, rhs: f64) -> Self { Self::new(self.re * rhs, self.im * rhs) }
}
impl std::ops::Div for C {
    type Output = Self;
    fn div(self, rhs: Self) -> Self {
        let d = rhs.re * rhs.re + rhs.im * rhs.im;
        Self::new(
            (self.re * rhs.re + self.im * rhs.im) / d,
            (self.im * rhs.re - self.re * rhs.im) / d,
        )
    }
}

#[derive(Clone, Copy)]
struct Term {
    f1: [i32; 3],
    f2: [i32; 3],
    n1: i32,
    n2: i32,
    coefficient: C,
}

fn add_frequency(a: [i32; 3], b: [i32; 3]) -> [i32; 3] {
    [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
}

fn multiply(left: &[Term], right: &[Term]) -> Vec<Term> {
    let mut output = Vec::new();
    for x in left {
        for y in right {
            output.push(Term {
                f1: add_frequency(x.f1, y.f1),
                f2: add_frequency(x.f2, y.f2),
                n1: x.n1 + y.n1,
                n2: x.n2 + y.n2,
                coefficient: x.coefficient * y.coefficient,
            });
        }
    }
    output
}

// External BD Wightman from the observation point eta to one bulk vertex.
fn external(second_vertex: bool, greater: bool, p: f64, eta: f64) -> Vec<Term> {
    let sign = if greater { 1 } else { -1 };
    let phase = -(sign as f64) * p * eta;
    let base = C::new(phase.cos(), phase.sin())
        * C::new(1.0, sign as f64 * p * eta)
        * (1.0 / p.powi(3));
    let mut frequency = [0; 3];
    frequency[0] = sign;
    let linear = C::new(0.0, -(sign as f64) * p);
    if second_vertex {
        vec![
            Term { f1: [0; 3], f2: frequency, n1: 0, n2: 0, coefficient: base },
            Term { f1: [0; 3], f2: frequency, n1: 0, n2: 1, coefficient: base * linear },
        ]
    } else {
        vec![
            Term { f1: frequency, f2: [0; 3], n1: 0, n2: 0, coefficient: base },
            Term { f1: frequency, f2: [0; 3], n1: 1, n2: 0, coefficient: base * linear },
        ]
    }
}

// Ordinary BD internal Wightman.  The label selects q or k.
fn bd_internal(label: usize, greater: bool, momentum: f64) -> Vec<Term> {
    let sign = if greater { -1 } else { 1 };
    let mut f1 = [0; 3];
    let mut f2 = [0; 3];
    f1[label] = sign;
    f2[label] = -sign;
    let base = C::new(1.0 / momentum.powi(3), 0.0);
    let linear1 = C::new(0.0, -(sign as f64) * momentum);
    let linear2 = C::new(0.0, (sign as f64) * momentum);
    vec![
        Term { f1, f2, n1: 0, n2: 0, coefficient: base },
        Term { f1, f2, n1: 1, n2: 0, coefficient: base * linear1 },
        Term { f1, f2, n1: 0, n2: 1, coefficient: base * linear2 },
        Term { f1, f2, n1: 1, n2: 1, coefficient: base * linear1 * linear2 },
    ]
}

// Coefficient of beta_q in either G_q^> or G_q^<.  The anomalous product
// h_q^*(t1)h_q^*(t2) is symmetric, so it is independent of contour ordering.
fn beta_q_internal(q: f64) -> Vec<Term> {
    let f1 = [0, 1, 0];
    let f2 = [0, 1, 0];
    let base = C::new(1.0 / q.powi(3), 0.0);
    let linear = C::new(0.0, -q);
    vec![
        Term { f1, f2, n1: 0, n2: 0, coefficient: base },
        Term { f1, f2, n1: 1, n2: 0, coefficient: base * linear },
        Term { f1, f2, n1: 0, n2: 1, coefficient: base * linear },
        Term { f1, f2, n1: 1, n2: 1, coefficient: base * linear * linear },
    ]
}

fn omega(frequency: [i32; 3], p: f64, q: f64, k: f64) -> f64 {
    frequency[0] as f64 * p + frequency[1] as f64 * q + frequency[2] as f64 * k
}

fn falling(n: i32, length: usize) -> f64 {
    (0..length).map(|j| f64::from(n - j as i32)).product()
}

fn primitive_coefficient(n: i32, r: usize, frequency: f64) -> C {
    let sign = if r % 2 == 0 { 1.0 } else { -1.0 };
    C::new(sign * falling(n, r), 0.0)
        / (0..=r).fold(C::new(1.0, 0.0), |z, _| z * C::new(0.0, frequency))
}

fn add<K: Ord>(map: &mut BTreeMap<K, C>, key: K, value: C) {
    let entry = map.entry(key).or_default();
    *entry = *entry + value;
}

fn boundary_weight(branch: i32, energy_sum: f64) -> Vec<Term> {
    let (leading, subleading) = if branch == 1 {
        (C::new(-1.0 / energy_sum.powi(2), 0.0), C::new(0.0, 1.0 / energy_sum))
    } else {
        (C::new(1.0 / energy_sum.powi(2), 0.0), C::new(0.0, 1.0 / energy_sum))
    };
    vec![
        Term { f1: [0; 3], f2: [0; 3], n1: 0, n2: -3, coefficient: leading },
        Term { f1: [0; 3], f2: [0; 3], n1: 0, n2: -2, coefficient: subleading },
    ]
}

fn anomalous_mixed_lower(p: f64, q: f64, k: f64, eta: f64) -> BTreeMap<([i32; 3], i32), C> {
    let mut raw = Vec::new();
    let energy_sum = p + q + k;
    for bulk_branch in [1, -1] {
        for boundary_branch in [1, -1] {
            let bulk = vec![Term {
                f1: [0; 3], f2: [0; 3], n1: -2, n2: 0,
                coefficient: C::new(bulk_branch as f64, 0.0),
            }];
            let product = multiply(
                &multiply(
                    &multiply(
                        &multiply(&bulk, &boundary_weight(boundary_branch, energy_sum)),
                        &external(false, bulk_branch == 1, p, eta),
                    ),
                    &external(true, boundary_branch == 1, p, eta),
                ),
                &multiply(&beta_q_internal(q), &bd_internal(2, boundary_branch == 1, k)),
            );
            raw.extend(product);
        }
    }
    let mut lower = BTreeMap::new();
    for term in raw {
        let frequency = omega(term.f1, p, q, k);
        assert!(frequency.abs() > 1e-10);
        for r in 0..=10 {
            let power = term.n1 - r as i32 + term.n2;
            if power < 0 { break; }
            add(
                &mut lower,
                (add_frequency(term.f1, term.f2), power),
                term.coefficient * primitive_coefficient(term.n1, r, frequency) * -1.0,
            );
        }
    }
    let spatial = (p * p + q * q + k * k).powi(2);
    for value in lower.values_mut() { *value = *value * spatial; }
    lower.retain(|_, value| value.abs() > 1e-9);
    lower
}

fn anomalous_boundary_boundary(p: f64, q: f64, k: f64, eta: f64) -> BTreeMap<([i32; 3], i32), C> {
    let energy_sum = p + q + k;
    let mut output = BTreeMap::new();
    for left_branch in [1, -1] {
        for right_branch in [1, -1] {
            let left_weight: Vec<Term> = boundary_weight(left_branch, energy_sum)
                .into_iter()
                .map(|term| Term { n1: term.n2, n2: 0, ..term })
                .collect();
            let equal_k = vec![
                Term { f1: [0; 3], f2: [0; 3], n1: 0, n2: 0, coefficient: C::new(1.0 / k.powi(3), 0.0) },
                Term { f1: [0; 3], f2: [0; 3], n1: 2, n2: 0, coefficient: C::new(1.0 / k, 0.0) },
            ];
            let product = multiply(
                &multiply(
                    &multiply(
                        &multiply(
                            &multiply(&left_weight, &boundary_weight(right_branch, energy_sum)),
                            &external(false, left_branch == 1, p, eta),
                        ),
                        &external(true, right_branch == 1, p, eta),
                    ),
                    &beta_q_internal(q),
                ),
                &equal_k,
            );
            for term in product {
                let grade = term.n1 + term.n2;
                if grade >= 0 {
                    add(
                        &mut output,
                        (add_frequency(term.f1, term.f2), grade),
                        term.coefficient,
                    );
                }
            }
        }
    }
    let spatial = (p * p + q * q + k * k).powi(2);
    for value in output.values_mut() { *value = *value * -spatial; }
    output.retain(|_, value| value.abs() > 1e-9);
    output
}

fn main() {
    let p = std::env::var("MARICI_P").ok().and_then(|x| x.parse().ok()).unwrap_or(1.1);
    let q = std::env::var("MARICI_Q").ok().and_then(|x| x.parse().ok()).unwrap_or(4.7);
    let k = std::env::var("MARICI_K").ok().and_then(|x| x.parse().ok()).unwrap_or(3.9);
    let eta = std::env::var("MARICI_ETA").ok().and_then(|x| x.parse().ok()).unwrap_or(-0.15);
    let weight = vec![Term {
        f1: [0; 3], f2: [0; 3], n1: -2, n2: -2, coefficient: C::new(1.0, 0.0),
    }];
    let mut raw = Vec::new();

    // Frozen nested-commutator sector sum.  Only the q occurrence is varied.
    for outer_greater in [true, false] {
        for inner_greater in [true, false] {
            let outer_sign = if outer_greater { 1.0 } else { -1.0 };
            let inner_sign = if inner_greater { 1.0 } else { -1.0 };
            let product = multiply(
                &multiply(
                    &multiply(
                        &external(false, outer_greater, p, eta),
                        &external(true, inner_greater, p, eta),
                    ),
                    &beta_q_internal(q),
                ),
                &bd_internal(2, inner_greater, k),
            );
            for mut term in multiply(&weight, &product) {
                term.coefficient = term.coefficient * (outer_sign * inner_sign);
                raw.push(term);
            }
        }
    }

    let mut lower: BTreeMap<([i32; 3], i32), C> = BTreeMap::new();
    let mut observation: BTreeMap<([i32; 3], i32, [i32; 3], i32, usize), C> = BTreeMap::new();
    let mut logarithms: BTreeMap<[i32; 3], C> = BTreeMap::new();
    let max_r = 10usize;
    for term in &raw {
        let w1 = omega(term.f1, p, q, k);
        let w2 = omega(term.f2, p, q, k);
        let summed_frequency = add_frequency(term.f1, term.f2);
        let summed_omega = w1 + w2;
        assert!(w1.abs() > 1e-10 && w2.abs() > 1e-10);
        for r2 in 0..=max_r {
            let a2 = primitive_coefficient(term.n2, r2, w2);
            let n = term.n1 + term.n2 - r2 as i32;
            if summed_omega.abs() > 1e-10 {
                for r3 in 0..=max_r {
                    let power = n - r3 as i32;
                    if power < 0 { break; }
                    add(
                        &mut lower,
                        (summed_frequency, power),
                        term.coefficient * a2 * primitive_coefficient(n, r3, summed_omega) * -1.0,
                    );
                }
            } else if n == -1 {
                add(&mut logarithms, summed_frequency, term.coefficient * a2 * -1.0);
            } else {
                let power = n + 1;
                if power >= 0 {
                    add(
                        &mut lower,
                        (summed_frequency, power),
                        term.coefficient * a2 * (-1.0 / f64::from(n + 1)),
                    );
                }
            }
            for r1 in 0..=max_r {
                let power = term.n2 - r2 as i32 + term.n1 - r1 as i32;
                if power < 0 { break; }
                add(
                    &mut lower,
                    (summed_frequency, power),
                    term.coefficient * a2 * primitive_coefficient(term.n1, r1, w1),
                );
            }
            let power = term.n2 - r2 as i32;
            if power >= 0 {
                add(
                    &mut observation,
                    (term.f2, power, term.f1, term.n1, r2),
                    term.coefficient * a2 * -1.0,
                );
            }
        }
    }

    let spatial = (p * p + q * q + k * k).powi(2);
    for value in lower.values_mut() { *value = *value * -spatial; }
    for value in observation.values_mut() { *value = *value * -spatial; }
    for value in logarithms.values_mut() { *value = *value * -spatial; }
    lower.retain(|_, value| value.abs() > 1e-9);
    observation.retain(|_, value| value.abs() > 1e-9);
    logarithms.retain(|_, value| value.abs() > 1e-9);

    let mixed_lower = anomalous_mixed_lower(p, q, k, eta);
    let boundary_boundary = anomalous_boundary_boundary(p, q, k, eta);
    let mut bulk_plus_mixed = lower.clone();
    for (key, value) in &mixed_lower { add(&mut bulk_plus_mixed, *key, *value); }
    bulk_plus_mixed.retain(|_, value| value.abs() > 1e-8);
    let residual_l1: f64 = bulk_plus_mixed.values().map(|value| value.abs()).sum();
    let bulk_l1: f64 = lower.values().map(|value| value.abs()).sum();
    let mut full_endpoint = bulk_plus_mixed.clone();
    for (key, value) in &boundary_boundary { add(&mut full_endpoint, *key, *value); }
    full_endpoint.retain(|_, value| value.abs() > 1e-8);
    let full_residual_l1: f64 = full_endpoint.values().map(|value| value.abs()).sum();
    let internal_frequency_retained = full_endpoint
        .keys()
        .all(|(frequency, _)| frequency[1] == 2 && frequency[2] == 0);
    let local_counterterm_support_disjoint = full_endpoint
        .keys()
        .all(|(frequency, _)| frequency[1] != 0 || frequency[2] != 0);
    assert!(internal_frequency_retained && local_counterterm_support_disjoint);

    let max_lower_grade = lower.keys().map(|(_, grade)| *grade).max().unwrap_or(-1);
    let max_observation_grade = observation.keys().map(|(_, grade, _, _, _)| *grade).max().unwrap_or(-1);
    let mut lower_counts = BTreeMap::new();
    let mut lower_norms = BTreeMap::new();
    for ((_, grade), coefficient) in &lower {
        *lower_counts.entry(*grade).or_insert(0usize) += 1;
        *lower_norms.entry(*grade).or_insert(0.0f64) += coefficient.abs();
    }
    let mut observation_counts = BTreeMap::new();
    let mut observation_norms = BTreeMap::new();
    for ((_, grade, _, _, _), coefficient) in &observation {
        *observation_counts.entry(*grade).or_insert(0usize) += 1;
        *observation_norms.entry(*grade).or_insert(0.0f64) += coefficient.abs();
    }

    println!("{{");
    println!("  \"schema\": \"marici.gaussian_anomalous_endpoint_recurrence.v1\",");
    println!("  \"varied_internal_occurrence\": \"q\",");
    println!("  \"frequency_letters\": [\"q-k\", \"q+k\"],");
    println!("  \"raw_terms\": {},", raw.len());
    println!("  \"lower_endpoint_counts_by_grade\": \"{:?}\",", lower_counts);
    println!("  \"lower_endpoint_l1_norms_by_grade\": \"{:?}\",", lower_norms);
    println!("  \"lower_endpoint_frequency_labels\": \"{:?}\",", lower.keys().collect::<Vec<_>>());
    println!("  \"observation_endpoint_counts_by_grade\": \"{:?}\",", observation_counts);
    println!("  \"observation_endpoint_l1_norms_by_grade\": \"{:?}\",", observation_norms);
    println!("  \"max_lower_endpoint_grade\": {max_lower_grade},");
    println!("  \"max_observation_endpoint_grade\": {max_observation_grade},");
    println!("  \"logarithmic_zero_frequency_classes\": {},", logarithms.len());
    println!("  \"mixed_lower_endpoint_classes\": {},", mixed_lower.len());
    println!("  \"bulk_plus_mixed_residual_classes\": {},", bulk_plus_mixed.len());
    println!("  \"bulk_plus_mixed_relative_l1_residual\": {:.17e},", residual_l1 / bulk_l1);
    println!("  \"boundary_boundary_endpoint_classes\": {},", boundary_boundary.len());
    println!("  \"full_endpoint_residual_classes\": {},", full_endpoint.len());
    println!("  \"full_endpoint_relative_l1_residual\": {:.17e},", full_residual_l1 / bulk_l1);
    println!("  \"internal_frequency_retained\": {internal_frequency_retained},");
    println!("  \"local_counterterm_support_disjoint\": {local_counterterm_support_disjoint},");
    println!("  \"positive_lower_endpoint_grades_cancel\": {},", max_lower_grade <= 0);
    println!("  \"positive_observation_endpoint_grades_cancel\": {},", max_observation_grade <= 0);
    println!("  \"zero_frequency_logarithms_cancel\": {}", logarithms.is_empty());
    println!("}}");

    assert!(logarithms.is_empty());
}
