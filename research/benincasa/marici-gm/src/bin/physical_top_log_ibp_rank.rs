use std::collections::{BTreeMap, HashMap};
use std::sync::OnceLock;

const VARIABLES: usize = 3;
type Monomial = [u8; VARIABLES];
type Row = BTreeMap<usize, i64>;

fn prime() -> i64 {
    static PRIME: OnceLock<i64> = OnceLock::new();
    *PRIME.get_or_init(|| {
        std::env::var("PRIME")
            .ok()
            .map(|raw| raw.parse().expect("PRIME must be an integer"))
            .unwrap_or(32_003)
    })
}

fn mul(left: i64, right: i64) -> i64 {
    ((left as i128 * right as i128) % prime() as i128) as i64
}

fn pow_mod(mut base: i64, mut exponent: i64) -> i64 {
    let mut result = 1;
    while exponent > 0 {
        if exponent & 1 == 1 {
            result = mul(result, base);
        }
        base = mul(base, base);
        exponent >>= 1;
    }
    result
}

fn inverse(value: i64) -> i64 {
    pow_mod(value.rem_euclid(prime()), prime() - 2)
}

#[derive(Clone, Default)]
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
            let next =
                (result.0.get(monomial).copied().unwrap_or(0) + coefficient).rem_euclid(prime());
            if next == 0 {
                result.0.remove(monomial);
            } else {
                result.0.insert(*monomial, next);
            }
        }
        result
    }

    fn scale(&self, scalar: i64) -> Self {
        let mut result = Self::default();
        for (monomial, coefficient) in &self.0 {
            let next = mul(*coefficient, scalar.rem_euclid(prime()));
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
                let next = (result.0.get(&monomial).copied().unwrap_or(0)
                    + mul(*left_coefficient, *right_coefficient))
                .rem_euclid(prime());
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
                result = result.add(&Self::term(derived, mul(*coefficient, i64::from(exponent))));
            }
        }
        result
    }

    fn degree(&self) -> usize {
        self.0
            .keys()
            .map(|monomial| monomial.iter().map(|value| usize::from(*value)).sum())
            .max()
            .unwrap_or(0)
    }
}

fn sum(polynomials: &[Polynomial]) -> Polynomial {
    polynomials
        .iter()
        .fold(Polynomial::default(), |left, right| left.add(right))
}

fn monomials_through(degree: usize) -> Vec<Monomial> {
    let mut result = Vec::new();
    for total in 0..=degree {
        for c in 0..=total {
            for a in 0..=total - c {
                let b = total - c - a;
                result.push([c as u8, a as u8, b as u8]);
            }
        }
    }
    result
}

fn normalize_row(mut row: Row, pivots: &BTreeMap<usize, Row>) -> Option<Row> {
    loop {
        let (&column, &coefficient) = row.iter().next()?;
        let Some(pivot) = pivots.get(&column) else {
            let scale = inverse(coefficient);
            for value in row.values_mut() {
                *value = mul(*value, scale);
            }
            return Some(row);
        };
        for (&pivot_column, &pivot_coefficient) in pivot {
            let next = (row.get(&pivot_column).copied().unwrap_or(0)
                - mul(coefficient, pivot_coefficient))
            .rem_euclid(prime());
            if next == 0 {
                row.remove(&pivot_column);
            } else {
                row.insert(pivot_column, next);
            }
        }
    }
}

fn quotient_dimension(
    k: &Polynomial,
    denominators: &[Polynomial],
    mask: u8,
    cutoff: usize,
) -> (usize, usize) {
    let selected: Vec<_> = denominators
        .iter()
        .enumerate()
        .filter(|(index, _)| mask & (1 << index) != 0)
        .map(|(_, denominator)| denominator.clone())
        .collect();
    let d = selected
        .iter()
        .fold(Polynomial::constant(1), |product, factor| {
            product.multiply(factor)
        });
    let kd = k.multiply(&d);
    let target = monomials_through(cutoff);
    let columns: HashMap<_, _> = target
        .iter()
        .enumerate()
        .map(|(index, monomial)| (*monomial, index))
        .collect();
    let generator_degree = kd.degree().saturating_sub(1);
    let source_degree = cutoff.saturating_sub(generator_degree);
    let source = monomials_through(source_degree);
    let inv_two = inverse(2);
    let mut pivots = BTreeMap::new();

    for variable in 0..VARIABLES {
        let exact_base = d
            .multiply(&k.derivative(variable))
            .scale(-inv_two)
            .add(&k.multiply(&d.derivative(variable)).scale(-1));
        for monomial in &source {
            let m = Polynomial::term(*monomial, 1);
            let divergence = if monomial[variable] == 0 {
                Polynomial::default()
            } else {
                let mut derived = *monomial;
                let exponent = derived[variable];
                derived[variable] -= 1;
                Polynomial::term(derived, i64::from(exponent))
            };
            let exact = kd.multiply(&divergence).add(&m.multiply(&exact_base));
            let mut row = Row::new();
            for (term, coefficient) in exact.0 {
                if let Some(&column) = columns.get(&term) {
                    row.insert(column, coefficient);
                } else {
                    panic!("exact numerator escaped cutoff");
                }
            }
            if let Some(reduced) = normalize_row(row, &pivots) {
                let pivot_column = *reduced.keys().next().unwrap();
                pivots.insert(pivot_column, reduced);
            }
        }
    }
    (target.len() - pivots.len(), pivots.len())
}

fn main() {
    let c = Polynomial::variable(0);
    let a = Polynomial::variable(1);
    let b = Polynomial::variable(2);
    let c2 = c.power(2);
    let a2 = a.power(2);
    let b2 = b.power(2);
    let point = std::env::var("KINEMATIC_POINT").unwrap_or_else(|_| "A".to_owned());
    let (x, y, z) = match point.as_str() {
        "A" => (2_i64, 3_i64, 4_i64),
        "B" => (3_i64, 5_i64, 6_i64),
        _ => panic!("KINEMATIC_POINT must be A or B"),
    };
    let (x2, y2, z2) = (x * x, y * y, z * z);
    let h = x2 + y2 - z2;
    let k = sum(&[
        a.power(4).scale(x2),
        a2.multiply(&b2).scale(-h),
        b.power(4).scale(y2),
        a2.scale(x2 * (x2 - y2 - z2)),
        c2.multiply(&a2).scale(-x2 + y2 - z2),
        b2.scale(y2 * (y2 - x2 - z2)),
        c2.multiply(&b2).scale(-y2 + x2 - z2),
        c.power(4).scale(z2),
        c2.scale(z2 * (-x2 - y2 + z2)),
        Polynomial::constant(z2 * x2 * y2),
    ]);
    let denominators = [
        sum(&[c.clone(), b, Polynomial::constant(x)]),
        sum(&[c.clone(), a, Polynomial::constant(y)]),
        c.add(&Polynomial::constant(x + y + z)),
    ];
    let cutoffs: Vec<usize> = std::env::var("CUTOFFS")
        .unwrap_or_else(|_| "8,10,12,14,16,18".to_owned())
        .split(',')
        .map(|raw| {
            raw.parse()
                .expect("CUTOFFS must be comma-separated integers")
        })
        .collect();
    let only = std::env::var("ONLY_MASK")
        .ok()
        .map(|raw| u8::from_str_radix(&raw, 2).expect("ONLY_MASK must be binary"));
    let masks: Vec<u8> = only.map_or_else(|| (0..8).collect(), |mask| vec![mask]);
    println!(
        "schema=physical-top-log-ibp-rank-v1 prime={} point={point} xyz=({x},{y},{z})",
        prime()
    );
    println!("model=fixed-simple-pole-polynomial-vector-fields gamma=-1/2");
    for cutoff in cutoffs {
        for &mask in &masks {
            let (quotient, exact_rank) = quotient_dimension(&k, &denominators, mask, cutoff);
            println!(
                "cutoff={cutoff} mask={mask:03b} quotient_dim={quotient} exact_rank={exact_rank}"
            );
        }
    }
}
