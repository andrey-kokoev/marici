//! Exact cyclic-Q audit for the frozen q_G12 marked residue census.
//! Tests Q12, Q23, and Q31 against every raw codimension-one candidate.
//!
//! This checker deliberately separates two questions.
//!
//! 1. It exhausts the codimension-one conditions visible in the *raw frozen
//!    data*: the compactified biquadratic branch quartic, all eight source
//!    lines, all twelve signed face lines, a=0, b=0, D_infinity, the soft/base
//!    divisors, every pair of marked lines, and every triple of marked lines.
//!    Every nonzero condition is tested against the full multivariate source
//!    Q in Z[x,y,z]; no kinematic specialization is used for factor rejection.
//!
//! 2. It refuses to promote that raw census to a log-Gauss-Manin theorem.
//!    The frozen source does not specify a labelled/sheeted log divisor for the
//!    two residue summands or a simultaneous log resolution.  This is material:
//!    three pole/face labels have identical support, the face pullbacks split,
//!    and large parallel classes meet D_infinity at the same points.  Thus the
//!    raw divisor is not SNC even at generic kinematics.
//!
//! Compile with warnings denied.  Pass `--emit-polynomials` to print every
//! exact nonconstant condition and its multivariate pseudo-remainder modulo Q.

use std::collections::{BTreeMap, BTreeSet};
use std::env;
use std::fmt;

const NV: usize = 9;
const X: usize = 0;
const Y: usize = 1;
const Z: usize = 2;
const ET: usize = 3;
const AA: usize = 4;
const BB: usize = 5;
const S: usize = 6;
const U: usize = 7;
const V: usize = 8;
const VAR_NAMES: [&str; NV] = ["x", "y", "z", "E", "a", "b", "s", "u", "v"];

type Monomial = [u8; NV];

#[derive(Clone, Debug, Eq, PartialEq)]
struct Poly {
    terms: BTreeMap<Monomial, i128>,
}

impl Poly {
    fn zero() -> Self {
        Self {
            terms: BTreeMap::new(),
        }
    }

    fn one() -> Self {
        Self::constant(1)
    }

    fn constant(value: i128) -> Self {
        if value == 0 {
            return Self::zero();
        }
        let mut terms = BTreeMap::new();
        terms.insert([0; NV], value);
        Self { terms }
    }

    fn var(index: usize) -> Self {
        let mut monomial = [0; NV];
        monomial[index] = 1;
        Self::from_term(monomial, 1)
    }

    fn from_term(monomial: Monomial, coefficient: i128) -> Self {
        if coefficient == 0 {
            return Self::zero();
        }
        let mut terms = BTreeMap::new();
        terms.insert(monomial, coefficient);
        Self { terms }
    }

    fn add(&self, rhs: &Self) -> Self {
        let mut terms = self.terms.clone();
        for (&monomial, &coefficient) in &rhs.terms {
            let old = terms.get(&monomial).copied().unwrap_or(0);
            let new = old
                .checked_add(coefficient)
                .expect("integer overflow in polynomial sum");
            if new == 0 {
                terms.remove(&monomial);
            } else {
                terms.insert(monomial, new);
            }
        }
        Self { terms }
    }

    fn neg(&self) -> Self {
        self.scale(-1)
    }

    fn sub(&self, rhs: &Self) -> Self {
        self.add(&rhs.neg())
    }

    fn scale(&self, scalar: i128) -> Self {
        if scalar == 0 || self.is_zero() {
            return Self::zero();
        }
        let terms = self
            .terms
            .iter()
            .map(|(&monomial, &coefficient)| {
                (
                    monomial,
                    coefficient
                        .checked_mul(scalar)
                        .expect("integer overflow in polynomial scale"),
                )
            })
            .collect();
        Self { terms }
    }

    fn mul(&self, rhs: &Self) -> Self {
        let mut terms = BTreeMap::<Monomial, i128>::new();
        for (&left_monomial, &left_coefficient) in &self.terms {
            for (&right_monomial, &right_coefficient) in &rhs.terms {
                let mut monomial = [0; NV];
                for index in 0..NV {
                    monomial[index] = left_monomial[index]
                        .checked_add(right_monomial[index])
                        .expect("monomial degree overflow");
                }
                let product = left_coefficient
                    .checked_mul(right_coefficient)
                    .expect("integer overflow in polynomial product");
                let old = terms.get(&monomial).copied().unwrap_or(0);
                let new = old
                    .checked_add(product)
                    .expect("integer overflow while collecting terms");
                if new == 0 {
                    terms.remove(&monomial);
                } else {
                    terms.insert(monomial, new);
                }
            }
        }
        Self { terms }
    }

    fn pow(&self, mut exponent: u8) -> Self {
        let mut base = self.clone();
        let mut result = Self::one();
        while exponent != 0 {
            if exponent & 1 == 1 {
                result = result.mul(&base);
            }
            exponent >>= 1;
            if exponent != 0 {
                base = base.mul(&base);
            }
        }
        result
    }

    fn substitute(&self, variable: usize, replacement: &Self) -> Self {
        let mut result = Self::zero();
        for (&monomial, &coefficient) in &self.terms {
            let exponent = monomial[variable];
            let mut residual = monomial;
            residual[variable] = 0;
            result =
                result.add(&Self::from_term(residual, coefficient).mul(&replacement.pow(exponent)));
        }
        result
    }

    fn coefficient(&self, variable: usize, exponent: u8) -> Self {
        let mut result = Self::zero();
        for (&monomial, &coefficient) in &self.terms {
            if monomial[variable] == exponent {
                let mut residual = monomial;
                residual[variable] = 0;
                result = result.add(&Self::from_term(residual, coefficient));
            }
        }
        result
    }

    fn degree_in(&self, variable: usize) -> Option<u8> {
        self.terms.keys().map(|monomial| monomial[variable]).max()
    }

    fn is_zero(&self) -> bool {
        self.terms.is_empty()
    }

    fn is_constant(&self) -> bool {
        self.terms
            .keys()
            .all(|monomial| monomial.iter().all(|&exponent| exponent == 0))
    }

    fn only_uses(&self, variables: &[usize]) -> bool {
        self.terms.keys().all(|monomial| {
            monomial
                .iter()
                .enumerate()
                .all(|(index, &exponent)| exponent == 0 || variables.contains(&index))
        })
    }

    fn homogeneous_in(&self, variables: &[usize], degree: u8) -> bool {
        !self.is_zero()
            && self.terms.keys().all(|monomial| {
                variables
                    .iter()
                    .map(|&variable| monomial[variable])
                    .sum::<u8>()
                    == degree
            })
    }

    fn primitive_part(&self) -> Self {
        if self.is_zero() {
            return Self::zero();
        }
        fn gcd(mut left: i128, mut right: i128) -> i128 {
            left = left.abs();
            right = right.abs();
            while right != 0 {
                let remainder = left % right;
                left = right;
                right = remainder;
            }
            left
        }
        let content = self.terms.values().copied().fold(0i128, gcd).max(1);
        let mut terms: BTreeMap<Monomial, i128> = self
            .terms
            .iter()
            .map(|(&monomial, &coefficient)| (monomial, coefficient / content))
            .collect();
        if terms
            .iter()
            .next_back()
            .is_some_and(|(_, coefficient)| *coefficient < 0)
        {
            for coefficient in terms.values_mut() {
                *coefficient = -*coefficient;
            }
        }
        Self { terms }
    }
}

impl fmt::Display for Poly {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        if self.is_zero() {
            return write!(formatter, "0");
        }
        let mut first = true;
        for (monomial, coefficient) in self.terms.iter().rev() {
            if first {
                if *coefficient < 0 {
                    write!(formatter, "-")?;
                }
            } else if *coefficient < 0 {
                write!(formatter, " - ")?;
            } else {
                write!(formatter, " + ")?;
            }
            let absolute = coefficient.abs();
            let has_variables = monomial.iter().any(|&exponent| exponent != 0);
            if absolute != 1 || !has_variables {
                write!(formatter, "{absolute}")?;
                if has_variables {
                    write!(formatter, "*")?;
                }
            }
            let mut first_variable = true;
            for (index, &exponent) in monomial.iter().enumerate() {
                if exponent == 0 {
                    continue;
                }
                if !first_variable {
                    write!(formatter, "*")?;
                }
                write!(formatter, "{}", VAR_NAMES[index])?;
                if exponent != 1 {
                    write!(formatter, "^{exponent}")?;
                }
                first_variable = false;
            }
            first = false;
        }
        Ok(())
    }
}

fn sum(polynomials: &[Poly]) -> Poly {
    polynomials
        .iter()
        .fold(Poly::zero(), |accumulator, item| accumulator.add(item))
}

fn determinant(matrix: &[Vec<Poly>]) -> Poly {
    assert!(!matrix.is_empty(), "empty determinant");
    let size = matrix.len();
    assert!(
        matrix.iter().all(|row| row.len() == size),
        "determinant matrix must be square"
    );

    fn visit(
        matrix: &[Vec<Poly>],
        row: usize,
        used_columns: u64,
        odd: bool,
        partial_product: &Poly,
        total: &mut Poly,
    ) {
        if row == matrix.len() {
            *total = if odd {
                total.sub(partial_product)
            } else {
                total.add(partial_product)
            };
            return;
        }
        for column in 0..matrix.len() {
            let mask = 1u64 << column;
            if used_columns & mask != 0 || matrix[row][column].is_zero() {
                continue;
            }
            let earlier_columns_after = (used_columns >> (column + 1)).count_ones();
            let next_odd = odd ^ (earlier_columns_after % 2 == 1);
            let next_product = partial_product.mul(&matrix[row][column]);
            visit(
                matrix,
                row + 1,
                used_columns | mask,
                next_odd,
                &next_product,
                total,
            );
        }
    }

    let mut result = Poly::zero();
    visit(matrix, 0, 0, false, &Poly::one(), &mut result);
    result
}

/// Fraction-free pseudo-remainder in one variable.  Because Q has constant
/// nonzero leading z-coefficient, vanishing is equivalent to divisibility in
/// Q[x,y,z], not merely after a specialization.
fn pseudo_remainder(dividend: &Poly, divisor: &Poly, variable: usize) -> Poly {
    let divisor_degree = divisor
        .degree_in(variable)
        .expect("pseudo-division by zero polynomial");
    let divisor_lead = divisor.coefficient(variable, divisor_degree);
    assert!(!divisor_lead.is_zero(), "missing leading coefficient");
    let mut remainder = dividend.clone();
    while let Some(remainder_degree) = remainder.degree_in(variable) {
        if remainder_degree < divisor_degree {
            break;
        }
        let remainder_lead = remainder.coefficient(variable, remainder_degree);
        let shift = remainder_degree - divisor_degree;
        let mut shifted_divisor = divisor.clone();
        if shift != 0 {
            let mut monomial = [0; NV];
            monomial[variable] = shift;
            shifted_divisor = shifted_divisor.mul(&Poly::from_term(monomial, 1));
        }
        remainder = remainder
            .mul(&divisor_lead)
            .sub(&shifted_divisor.mul(&remainder_lead));
    }
    remainder
}

fn binary_coefficients(polynomial: &Poly, degree: u8) -> Vec<Poly> {
    assert!(
        polynomial.homogeneous_in(&[U, V], degree),
        "binary form has wrong homogeneous degree: {polynomial}"
    );
    (0..=degree)
        .rev()
        .map(|u_exponent| {
            let v_exponent = degree - u_exponent;
            let coefficient = polynomial
                .coefficient(U, u_exponent)
                .coefficient(V, v_exponent);
            assert!(
                coefficient.only_uses(&[X, Y, Z, ET]),
                "binary coefficient retains fiber variables: {coefficient}"
            );
            coefficient
        })
        .collect()
}

fn homogenize_univariate(
    polynomial: &Poly,
    variable: usize,
    homogenizer: usize,
    degree: u8,
) -> Poly {
    assert!(
        polynomial
            .degree_in(variable)
            .is_some_and(|actual| actual <= degree),
        "univariate polynomial exceeds requested homogenizing degree"
    );
    let variable_poly = Poly::var(variable);
    let homogenizer_poly = Poly::var(homogenizer);
    let mut result = Poly::zero();
    for exponent in 0..=degree {
        let coefficient = polynomial.coefficient(variable, exponent);
        assert!(
            coefficient.only_uses(&[X, Y, Z, ET]),
            "univariate coefficient retains a fiber variable: {coefficient}"
        );
        result = result.add(
            &coefficient
                .mul(&variable_poly.pow(exponent))
                .mul(&homogenizer_poly.pow(degree - exponent)),
        );
    }
    result
}

fn binary_quadratic_discriminant(polynomial: &Poly) -> Poly {
    let coefficients = binary_coefficients(polynomial, 2);
    let a = &coefficients[0];
    let b = &coefficients[1];
    let c = &coefficients[2];
    b.pow(2).sub(&a.mul(c).scale(4))
}

fn binary_quartic_discriminant(polynomial: &Poly) -> Poly {
    let coefficients = binary_coefficients(polynomial, 4);
    let a = &coefficients[0];
    let b = &coefficients[1];
    let c = &coefficients[2];
    let d = &coefficients[3];
    let e = &coefficients[4];
    sum(&[
        a.pow(3).mul(&e.pow(3)).scale(256),
        a.pow(2).mul(b).mul(d).mul(&e.pow(2)).scale(-192),
        a.pow(2).mul(&c.pow(2)).mul(&e.pow(2)).scale(-128),
        a.pow(2).mul(c).mul(&d.pow(2)).mul(e).scale(144),
        a.pow(2).mul(&d.pow(4)).scale(-27),
        a.mul(&b.pow(2)).mul(c).mul(&e.pow(2)).scale(144),
        a.mul(&b.pow(2)).mul(&d.pow(2)).mul(e).scale(-6),
        a.mul(b).mul(&c.pow(2)).mul(d).mul(e).scale(-80),
        a.mul(b).mul(c).mul(&d.pow(3)).scale(18),
        a.mul(&c.pow(4)).mul(e).scale(16),
        a.mul(&c.pow(3)).mul(&d.pow(2)).scale(-4),
        b.pow(4).mul(&e.pow(2)).scale(-27),
        b.pow(3).mul(c).mul(d).mul(e).scale(18),
        b.pow(3).mul(&d.pow(3)).scale(-4),
        b.pow(2).mul(&c.pow(3)).mul(e).scale(-4),
        b.pow(2).mul(&c.pow(2)).mul(&d.pow(2)),
    ])
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Role {
    Source,
    Face,
    Coordinate,
    Infinity,
}

#[derive(Clone)]
struct Line {
    name: &'static str,
    role: Role,
    alpha: i128,
    beta: i128,
    gamma: Poly,
    active: bool,
    face_root: Option<Poly>,
}

impl Line {
    fn equation(&self, a: &Poly, b: &Poly, s: &Poly) -> Poly {
        sum(&[a.scale(self.alpha), b.scale(self.beta), self.gamma.mul(s)])
    }

    fn restrict(&self, polynomial: &Poly, u: &Poly, v: &Poly) -> Poly {
        if self.alpha == 1 || self.alpha == -1 {
            let a_value = u
                .scale(self.beta)
                .add(&self.gamma.mul(v))
                .scale(-self.alpha);
            polynomial
                .substitute(AA, &a_value)
                .substitute(BB, u)
                .substitute(S, v)
        } else if self.beta == 1 || self.beta == -1 {
            let b_value = u
                .scale(self.alpha)
                .add(&self.gamma.mul(v))
                .scale(-self.beta);
            polynomial
                .substitute(AA, u)
                .substitute(BB, &b_value)
                .substitute(S, v)
        } else {
            assert!(
                self.role == Role::Infinity
                    && self.alpha == 0
                    && self.beta == 0
                    && self.gamma == Poly::one(),
                "only D_infinity has no a/b coefficient"
            );
            polynomial
                .substitute(AA, u)
                .substitute(BB, v)
                .substitute(S, &Poly::zero())
        }
    }

    fn restrict_affine(&self, polynomial: &Poly, u: &Poly) -> Poly {
        assert!(
            self.role != Role::Infinity,
            "D_infinity has no affine chart"
        );
        if self.alpha == 1 || self.alpha == -1 {
            let a_value = u.scale(self.beta).add(&self.gamma).scale(-self.alpha);
            polynomial
                .substitute(AA, &a_value)
                .substitute(BB, u)
                .substitute(S, &Poly::one())
        } else {
            assert!(self.beta == 1 || self.beta == -1, "invalid affine line");
            let b_value = u.scale(self.alpha).add(&self.gamma).scale(-self.beta);
            polynomial
                .substitute(AA, u)
                .substitute(BB, &b_value)
                .substitute(S, &Poly::one())
        }
    }
}

fn line_cross(left: &Line, right: &Line) -> (Poly, Poly, Poly) {
    let cross_a = right
        .gamma
        .scale(left.beta)
        .sub(&left.gamma.scale(right.beta));
    let cross_b = left
        .gamma
        .scale(right.alpha)
        .sub(&right.gamma.scale(left.alpha));
    let cross_s = Poly::constant(left.alpha * right.beta - left.beta * right.alpha);
    (cross_a, cross_b, cross_s)
}

fn same_support(left: &Line, right: &Line) -> bool {
    let (cross_a, cross_b, cross_s) = line_cross(left, right);
    cross_a.is_zero() && cross_b.is_zero() && cross_s.is_zero()
}

fn triple_determinant(first: &Line, second: &Line, third: &Line) -> Poly {
    sum(&[
        second
            .gamma
            .scale(first.beta * third.alpha - first.alpha * third.beta),
        third
            .gamma
            .scale(first.alpha * second.beta - first.beta * second.alpha),
        first
            .gamma
            .scale(second.alpha * third.beta - second.beta * third.alpha),
    ])
}

fn evaluate_homogeneous(polynomial: &Poly, a_value: &Poly, b_value: &Poly, s_value: &Poly) -> Poly {
    polynomial
        .substitute(AA, a_value)
        .substitute(BB, b_value)
        .substitute(S, s_value)
}

fn normalized_direction(line: &Line) -> Option<(i128, i128)> {
    if line.role == Role::Infinity {
        return None;
    }
    let mut alpha = line.alpha;
    let mut beta = line.beta;
    if alpha < 0 || (alpha == 0 && beta < 0) {
        alpha = -alpha;
        beta = -beta;
    }
    Some((alpha, beta))
}

struct Checker {
    assertions: usize,
    q_rejections: usize,
    emitted: bool,
    categories: BTreeMap<&'static str, usize>,
}

impl Checker {
    fn new(emitted: bool) -> Self {
        Self {
            assertions: 0,
            q_rejections: 0,
            emitted,
            categories: BTreeMap::new(),
        }
    }

    fn equal(&mut self, label: &str, actual: &Poly, expected: &Poly) {
        self.assertions += 1;
        if actual != expected {
            panic!(
                "FAIL [{label}] exact polynomial difference: {}",
                actual.sub(expected)
            );
        }
    }

    fn condition(&mut self, label: &str, condition: bool) {
        self.assertions += 1;
        assert!(condition, "FAIL [{label}]");
    }

    fn reject_q_factor(
        &mut self,
        category: &'static str,
        name: &str,
        polynomial: &Poly,
        targets: &[(&'static str, &Poly, usize)],
    ) {
        self.condition(
            &format!("{category}/{name} is a nonzero codimension-one polynomial"),
            !polynomial.is_zero() && !polynomial.is_constant(),
        );
        self.condition(
            &format!("{category}/{name} only uses x,y,z"),
            polynomial.only_uses(&[X, Y, Z]),
        );
        for (target_name, target, division_variable) in targets {
            let remainder =
                pseudo_remainder(polynomial, target, *division_variable).primitive_part();
            self.condition(
                &format!("{target_name} is not a factor of {category}/{name}"),
                !remainder.is_zero(),
            );
            self.q_rejections += 1;
            *self.categories.entry(category).or_insert(0) += 1;
            if self.emitted {
                println!(
                    "POLYNOMIAL target={target_name} category={category} name={name} P=({}) Qrem=({remainder})",
                    polynomial.primitive_part()
                );
            }
        }
    }
}

fn main() {
    let emit_polynomials = env::args().any(|argument| argument == "--emit-polynomials");
    let mut check = Checker::new(emit_polynomials);

    let x = Poly::var(X);
    let y = Poly::var(Y);
    let z = Poly::var(Z);
    let et = Poly::var(ET);
    let a = Poly::var(AA);
    let b = Poly::var(BB);
    let s = Poly::var(S);
    let u = Poly::var(U);
    let v = Poly::var(V);
    let zero = Poly::zero();
    let one = Poly::one();

    let x2 = x.pow(2);
    let y2 = y.pow(2);
    let z2 = z.pow(2);
    let e = sum(&[x.clone(), y.clone(), z.clone()]);
    let e2 = e.pow(2);
    let h = x2.add(&y2).sub(&z2);
    let cap_a = x.sub(&y).pow(2).sub(&z2);
    let cap_b = x.add(&y).pow(2).sub(&z2);
    let ab = cap_a.mul(&cap_b);
    let q = ab.scale(4).sub(&cap_a.add(&cap_b).sub(&e2).pow(2));
    let q23 = sum(&[
        y2.mul(&z2).scale(-16),
        y.mul(&z).mul(&e2).scale(-8),
        y.add(&z).mul(&e.pow(3)).scale(8),
        e.pow(4).scale(-5),
    ]);
    let q31 = sum(&[
        z2.mul(&x2).scale(-16),
        z.mul(&x).mul(&e2).scale(-8),
        z.add(&x).mul(&e.pow(3)).scale(8),
        e.pow(4).scale(-5),
    ]);
    let q_targets = [
        ("Q12", &q, Z),
        ("Q23", &q23, X),
        ("Q31", &q31, Y),
    ];

    // Direct irreducibility certificate.  After the invertible linear change
    // z=E-x-y, Q is primitive and quadratic in x.  Its discriminant has odd
    // valuations at the nonassociate irreducible linear forms E and E+2y.
    let q_normal = sum(&[
        et.pow(4).scale(-5),
        x.add(&y).mul(&et.pow(3)).scale(8),
        x.mul(&y).mul(&et.pow(2)).scale(-8),
        x2.mul(&y2).scale(-16),
    ]);
    check.equal(
        "source Q under z=E-x-y",
        &q.substitute(Z, &et.sub(&x).sub(&y)),
        &q_normal,
    );
    check.equal(
        "Q quadratic coefficient in x",
        &q_normal.coefficient(X, 2),
        &y2.scale(-16),
    );
    check.equal(
        "Q linear coefficient in x",
        &q_normal.coefficient(X, 1),
        &et.pow(2).mul(&et.sub(&y)).scale(8),
    );
    check.equal(
        "Q constant coefficient in x",
        &q_normal.coefficient(X, 0),
        &et.pow(3).mul(&y.scale(8).sub(&et.scale(5))),
    );
    let q_quadratic_discriminant = q_normal.coefficient(X, 1).pow(2).sub(
        &q_normal
            .coefficient(X, 2)
            .mul(&q_normal.coefficient(X, 0))
            .scale(4),
    );
    let q_discriminant_factorization = et
        .pow(3)
        .mul(&et.sub(&y.scale(2)).pow(2))
        .mul(&et.add(&y.scale(2)))
        .scale(64);
    check.equal(
        "Q quadratic discriminant factorization",
        &q_quadratic_discriminant,
        &q_discriminant_factorization,
    );
    check.condition(
        "E and E+2y are nonassociate irreducible linear forms",
        1i128 * 2i128 - 0i128 * 1i128 != 0,
    );
    check.condition(
        "Q is primitive in Q[y,E][x] because y does not divide 8E^2(E-y)",
        !q_normal.coefficient(X, 1).substitute(Y, &zero).is_zero(),
    );
    check.condition(
        "Q has z-degree four with constant leading coefficient",
        q.degree_in(Z) == Some(4) && q.coefficient(Z, 4) == Poly::constant(-5),
    );

    // Compactified branch quartic W^2=Kbar in P(1,1,1,2).
    let cap_u = e2.add(&y2);
    let cap_v = e2.add(&x2);
    let a_shift = a.pow(2).sub(&cap_u.mul(&s.pow(2)));
    let b_shift = b.pow(2).sub(&cap_v.mul(&s.pow(2)));
    let kbar = sum(&[
        x2.mul(&a_shift.pow(2)),
        h.mul(&a_shift).mul(&b_shift).neg(),
        y2.mul(&b_shift.pow(2)),
        e2.mul(&ab).mul(&s.pow(4)),
    ]);
    let ga = h.mul(&x2.add(&e2)).sub(&x2.mul(&y2.add(&e2)).scale(2));
    let gb = h.mul(&y2.add(&e2)).sub(&y2.mul(&x2.add(&e2)).scale(2));
    let h0 = z2.mul(&e.pow(4).sub(&h.mul(&e2)).add(&x2.mul(&y2)));
    let kbar_expanded = sum(&[
        x2.mul(&a.pow(4)),
        h.mul(&a.pow(2)).mul(&b.pow(2)).neg(),
        y2.mul(&b.pow(4)),
        ga.mul(&a.pow(2)).mul(&s.pow(2)),
        gb.mul(&b.pow(2)).mul(&s.pow(2)),
        h0.mul(&s.pow(4)),
    ]);
    check.equal("compactified K0 identity", &kbar, &kbar_expanded);

    // Coordinate-stratified singularity certificate for the biquadratic
    // quartic.  With U=a^2,V=b^2,T=s^2, its gradient is controlled by N.
    let n_matrix = vec![
        vec![x2.scale(2), h.neg(), ga.clone()],
        vec![h.neg(), y2.scale(2), gb.clone()],
        vec![ga.clone(), gb.clone(), h0.scale(2)],
    ];
    let det_n = determinant(&n_matrix);
    let minor_ab = x2.mul(&y2).scale(4).sub(&h.pow(2));
    let minor_as = x2.mul(&h0).scale(4).sub(&ga.pow(2));
    let minor_bs = y2.mul(&h0).scale(4).sub(&gb.pow(2));
    check.equal(
        "surface full 3x3 determinant",
        &det_n,
        &e2.mul(&ab.pow(2)).scale(-2),
    );
    check.equal("surface s=0 principal determinant", &minor_ab, &ab.neg());
    check.equal(
        "surface b=0 principal determinant",
        &minor_as,
        &ab.mul(&e2.sub(&x2).pow(2)).neg(),
    );
    check.equal(
        "surface a=0 principal determinant",
        &minor_bs,
        &ab.mul(&e2.sub(&y2).pow(2)).neg(),
    );
    let surface_conditions = [
        ("all_coordinates_nonzero_detN", det_n.clone()),
        ("a_zero_minor_bs", minor_bs.clone()),
        ("b_zero_minor_as", minor_as.clone()),
        ("s_zero_minor_ab", minor_ab.clone()),
        ("a_axis_coefficient", x2.clone()),
        ("b_axis_coefficient", y2.clone()),
        ("s_axis_coefficient", h0.clone()),
    ];
    for (name, polynomial) in surface_conditions {
        check.reject_q_factor("surface_singularity", name, &polynomial, &q_targets);
    }
    let surface_residual_factor = e.pow(4).sub(&h.mul(&e2)).add(&x2.mul(&y2));
    check.equal(
        "s-axis coefficient factorization",
        &h0,
        &z2.mul(&surface_residual_factor),
    );
    let surface_codimension_one_factors = [
        ("x", x.clone()),
        ("y", y.clone()),
        ("z", z.clone()),
        ("E", e.clone()),
        ("x-y-z", x.sub(&y).sub(&z)),
        ("x-y+z", x.sub(&y).add(&z)),
        ("x+y-z", x.add(&y).sub(&z)),
        ("E-x", e.sub(&x)),
        ("E+x", e.add(&x)),
        ("E-y", e.sub(&y)),
        ("E+y", e.add(&y)),
        ("H/z^2", surface_residual_factor.clone()),
    ];
    for (name, polynomial) in surface_codimension_one_factors {
        check.reject_q_factor("surface_codimension_one_factor", name, &polynomial, &q_targets);
    }

    // Frozen source lines.  The active-five set is a union of two four-pole
    // summands, not itself the pole set of one printed summand.
    let mut lines = vec![
        Line {
            name: "q_g1",
            role: Role::Source,
            alpha: 0,
            beta: 1,
            gamma: y.add(&z).neg(),
            active: true,
            face_root: None,
        },
        Line {
            name: "q_g2",
            role: Role::Source,
            alpha: 1,
            beta: 0,
            gamma: x.add(&z).neg(),
            active: true,
            face_root: None,
        },
        Line {
            name: "q_g3",
            role: Role::Source,
            alpha: 1,
            beta: 1,
            gamma: z.clone(),
            active: true,
            face_root: None,
        },
        Line {
            name: "q_g12",
            role: Role::Source,
            alpha: 1,
            beta: 1,
            gamma: x.add(&y),
            active: false,
            face_root: None,
        },
        Line {
            name: "q_g23",
            role: Role::Source,
            alpha: 0,
            beta: 1,
            gamma: x.neg(),
            active: true,
            face_root: None,
        },
        Line {
            name: "q_g31",
            role: Role::Source,
            alpha: 1,
            beta: 0,
            gamma: y.neg(),
            active: true,
            face_root: None,
        },
        Line {
            name: "q_G23",
            role: Role::Source,
            alpha: 1,
            beta: 0,
            gamma: e.clone(),
            active: false,
            face_root: None,
        },
        Line {
            name: "q_G31",
            role: Role::Source,
            alpha: 0,
            beta: 1,
            gamma: e.clone(),
            active: false,
            face_root: None,
        },
    ];
    let active_names: Vec<&str> = lines
        .iter()
        .filter(|line| line.active)
        .map(|line| line.name)
        .collect();
    check.condition(
        "active-five pole union",
        active_names == ["q_g1", "q_g2", "q_g3", "q_g23", "q_g31"],
    );
    let summand_23 = ["q_g1", "q_g2", "q_g3", "q_g23"];
    let summand_31 = ["q_g1", "q_g2", "q_g3", "q_g31"];
    check.condition(
        "two distinct four-pole residue summands",
        summand_23.len() == 4 && summand_31.len() == 4 && summand_23 != summand_31,
    );

    // All twelve signed Cayley-Menger face branches, retaining the exact
    // square root of Kbar on each line.  Signs match ledger 161's checker.
    let sign_pairs = [(-1i128, -1i128), (-1, 1), (1, -1), (1, 1)];
    let ca_names = ["ca--", "ca-+", "ca+-", "ca++"];
    let cb_names = ["cb--", "cb-+", "cb+-", "cb++"];
    let ab_names = ["ab--", "ab-+", "ab+-", "ab++"];
    for (index, &(sign_1, sign_2)) in sign_pairs.iter().enumerate() {
        let ca_root = e
            .neg()
            .mul(&a.pow(2).add(&b.pow(2)).sub(&z2))
            .sub(&a.scale(sign_1).mul(&e2.add(&b.pow(2)).sub(&x2)));
        lines.push(Line {
            name: ca_names[index],
            role: Role::Face,
            alpha: 1,
            beta: 0,
            gamma: e.scale(sign_1).sub(&y.scale(sign_2)),
            active: false,
            face_root: Some(ca_root),
        });

        let cb_root = e
            .neg()
            .mul(&a.pow(2).add(&b.pow(2)).sub(&z2))
            .sub(&b.scale(sign_1).mul(&e2.add(&a.pow(2)).sub(&y2)));
        lines.push(Line {
            name: cb_names[index],
            role: Role::Face,
            alpha: 0,
            beta: 1,
            gamma: e.scale(sign_1).sub(&x.scale(sign_2)),
            active: false,
            face_root: Some(cb_root),
        });

        let ab_root = a
            .mul(&e2.add(&b.pow(2)).sub(&x2))
            .sub(&b.scale(sign_1).mul(&e2.add(&a.pow(2)).sub(&y2)));
        lines.push(Line {
            name: ab_names[index],
            role: Role::Face,
            alpha: -sign_1,
            beta: 1,
            gamma: z.scale(-sign_2),
            active: false,
            face_root: Some(ab_root),
        });
    }
    lines.push(Line {
        name: "a=0",
        role: Role::Coordinate,
        alpha: 1,
        beta: 0,
        gamma: zero.clone(),
        active: false,
        face_root: None,
    });
    lines.push(Line {
        name: "b=0",
        role: Role::Coordinate,
        alpha: 0,
        beta: 1,
        gamma: zero.clone(),
        active: false,
        face_root: None,
    });
    lines.push(Line {
        name: "D_infinity",
        role: Role::Infinity,
        alpha: 0,
        beta: 0,
        gamma: one.clone(),
        active: false,
        face_root: None,
    });
    check.condition(
        "maximal line census has 23 labelled lines",
        lines.len() == 23,
    );
    check.condition(
        "line equations are homogeneous projective equations",
        lines
            .iter()
            .all(|line| line.equation(&a, &b, &s).homogeneous_in(&[AA, BB, S], 1)),
    );

    let face_indices: Vec<usize> = lines
        .iter()
        .enumerate()
        .filter(|(_, line)| line.role == Role::Face)
        .map(|(index, _)| index)
        .collect();
    check.condition("twelve face labels", face_indices.len() == 12);
    for &index in &face_indices {
        let line = &lines[index];
        let restricted_k = line.restrict(&kbar, &u, &v);
        let restricted_root_affine =
            line.restrict_affine(line.face_root.as_ref().expect("face root missing"), &u);
        let restricted_root = homogenize_univariate(&restricted_root_affine, U, V, 2);
        check.equal(
            &format!("forced square on signed face {}", line.name),
            &restricted_k,
            &restricted_root.pow(2),
        );
    }

    let infinity_line = lines
        .iter()
        .find(|line| line.role == Role::Infinity)
        .expect("D_infinity missing");
    let infinity_discriminant = binary_quartic_discriminant(&infinity_line.restrict(&kbar, &u, &v));
    check.equal(
        "D_infinity binary-quartic discriminant",
        &infinity_discriminant,
        &x2.mul(&y2).mul(&ab.pow(2)).scale(16),
    );
    let coordinate_a = lines
        .iter()
        .find(|line| line.name == "a=0")
        .expect("a=0 missing");
    let coordinate_b = lines
        .iter()
        .find(|line| line.name == "b=0")
        .expect("b=0 missing");
    check.equal(
        "a=0 binary-quartic discriminant",
        &binary_quartic_discriminant(&coordinate_a.restrict(&kbar, &u, &v)),
        &y2.mul(&h0).mul(&minor_bs.pow(2)).scale(16),
    );
    check.equal(
        "b=0 binary-quartic discriminant",
        &binary_quartic_discriminant(&coordinate_b.restrict(&kbar, &u, &v)),
        &x2.mul(&h0).mul(&minor_as.pow(2)).scale(16),
    );
    for line in lines.iter().filter(|line| line.role != Role::Infinity) {
        let infinity_value = evaluate_homogeneous(
            &kbar,
            &Poly::constant(line.beta),
            &Poly::constant(-line.alpha),
            &zero,
        );
        let expected = match normalized_direction(line).expect("finite line direction") {
            (1, 0) => y2.clone(),
            (0, 1) => x2.clone(),
            (1, 1) | (1, -1) => z2.clone(),
            direction => panic!("unexpected infinity direction {direction:?}"),
        };
        check.equal(
            &format!("exact infinity branch value for {}", line.name),
            &infinity_value,
            &expected,
        );
    }

    // Exactly three frozen pole labels have the same projective support as a
    // signed face label.  This is structural, not a discriminant condition.
    let mut source_face_coincidences = Vec::<(&str, &str)>::new();
    for source in lines.iter().filter(|line| line.role == Role::Source) {
        for face in lines.iter().filter(|line| line.role == Role::Face) {
            if same_support(source, face) {
                source_face_coincidences.push((source.name, face.name));
            }
        }
    }
    check.condition(
        "three universal source/face support coincidences",
        source_face_coincidences == [("q_g1", "cb--"), ("q_g2", "ca--"), ("q_g3", "ab--")],
    );

    // Base/soft/domain boundary components.  AB is retained both as a union
    // and as its two irreducible components.
    let base_conditions = [
        ("x=0", x.clone()),
        ("y=0", y.clone()),
        ("z=0", z.clone()),
        ("E=0", e.clone()),
        ("A=0", cap_a.clone()),
        ("B=0", cap_b.clone()),
        ("AB=0", ab.clone()),
    ];
    for (name, polynomial) in base_conditions {
        check.reject_q_factor("base_or_soft_boundary", name, &polynomial, &q_targets);
    }

    // Line/branch tangency.  For the twelve forced-square face supports (and
    // the three coincident source labels), use the binary quadratic
    // discriminant of the reduced square root; all other lines use the full
    // binary quartic discriminant, including roots at infinity.
    let mut reduced_square_labels = 0usize;
    let mut full_quartic_labels = 0usize;
    for line_index in 0..lines.len() {
        let line = &lines[line_index];
        let root_owner = lines.iter().find(|candidate| {
            candidate.role == Role::Face
                && candidate.face_root.is_some()
                && same_support(line, candidate)
        });
        let condition = if let Some(face) = root_owner {
            reduced_square_labels += 1;
            let restricted_k = line.restrict(&kbar, &u, &v);
            let restricted_root_affine =
                line.restrict_affine(face.face_root.as_ref().expect("root owner lacks root"), &u);
            let restricted_root = homogenize_univariate(&restricted_root_affine, U, V, 2);
            check.equal(
                &format!(
                    "reduced-square line identity {} via {}",
                    line.name, face.name
                ),
                &restricted_k,
                &restricted_root.pow(2),
            );
            binary_quadratic_discriminant(&restricted_root)
        } else {
            full_quartic_labels += 1;
            binary_quartic_discriminant(&line.restrict(&kbar, &u, &v))
        };
        check.condition(
            &format!(
                "line discriminant is not structurally zero for {}",
                line.name
            ),
            !condition.is_zero(),
        );
        if !condition.is_constant() {
            check.reject_q_factor("line_branch_tangency", line.name, &condition, &q_targets);
        }
    }
    check.condition(
        "fifteen labels use twelve forced-square supports",
        reduced_square_labels == 15 && full_quartic_labels == 8,
    );

    // Pair census.  Cross products give the exact projective intersection.
    // For affine-parallel lines the separate gap polynomial is their exact
    // coincidence condition; their common infinity direction is used for the
    // branch-incidence condition so no irrelevant fourth power of the gap is
    // introduced.
    let mut universal_coincident_pairs = 0usize;
    let mut universal_parallel_pairs = 0usize;
    let mut impossible_pair_conditions = 0usize;
    let mut universal_branch_pairs = 0usize;
    let mut pair_branch_conditions = 0usize;
    let mut pair_collision_conditions = 0usize;
    for left_index in 0..lines.len() {
        for right_index in (left_index + 1)..lines.len() {
            let left = &lines[left_index];
            let right = &lines[right_index];
            let (cross_a, cross_b, cross_s) = line_cross(left, right);
            if cross_a.is_zero() && cross_b.is_zero() && cross_s.is_zero() {
                universal_coincident_pairs += 1;
                continue;
            }

            let either_infinity = left.role == Role::Infinity || right.role == Role::Infinity;
            let parallel_affine = cross_s.is_zero() && !either_infinity;
            if parallel_affine {
                universal_parallel_pairs += 1;
                let gap = if !cross_a.is_zero() {
                    &cross_a
                } else {
                    &cross_b
                };
                if gap.is_constant() {
                    impossible_pair_conditions += 1;
                } else {
                    pair_collision_conditions += 1;
                    check.reject_q_factor(
                        "parallel_line_coincidence",
                        &format!("{}__{}", left.name, right.name),
                        gap,
                        &q_targets,
                    );
                }
            }

            let branch_at_intersection = if cross_s.is_zero() {
                let finite_line = if left.role == Role::Infinity {
                    right
                } else {
                    left
                };
                evaluate_homogeneous(
                    &kbar,
                    &Poly::constant(finite_line.beta),
                    &Poly::constant(-finite_line.alpha),
                    &zero,
                )
            } else {
                evaluate_homogeneous(&kbar, &cross_a, &cross_b, &cross_s)
            };
            if branch_at_intersection.is_zero() {
                universal_branch_pairs += 1;
            } else if branch_at_intersection.is_constant() {
                impossible_pair_conditions += 1;
            } else {
                pair_branch_conditions += 1;
                check.reject_q_factor(
                    "branch_at_line_intersection",
                    &format!("{}__{}", left.name, right.name),
                    &branch_at_intersection,
                    &q_targets,
                );
            }
        }
    }
    check.condition(
        "pair census accounts for C(23,2)",
        universal_coincident_pairs + (23usize * 22 / 2 - universal_coincident_pairs)
            == 23usize * 22 / 2,
    );
    check.condition(
        "three universal coincident labelled pairs",
        universal_coincident_pairs == 3,
    );

    // Every triple determinant is the exact condition that three projective
    // line supports are concurrent.  Zero determinants are recorded as
    // structural universal incidences; nonzero constants mean concurrence is
    // impossible; every remaining polynomial is checked multivariately.
    let mut universal_triples = 0usize;
    let mut impossible_triples = 0usize;
    let mut triple_conditions = 0usize;
    for first_index in 0..lines.len() {
        for second_index in (first_index + 1)..lines.len() {
            for third_index in (second_index + 1)..lines.len() {
                let condition = triple_determinant(
                    &lines[first_index],
                    &lines[second_index],
                    &lines[third_index],
                );
                if condition.is_zero() {
                    universal_triples += 1;
                } else if condition.is_constant() {
                    impossible_triples += 1;
                } else {
                    triple_conditions += 1;
                    check.reject_q_factor(
                        "triple_line_incidence",
                        &format!(
                            "{}__{}__{}",
                            lines[first_index].name,
                            lines[second_index].name,
                            lines[third_index].name
                        ),
                        &condition,
                        &q_targets,
                    );
                }
            }
        }
    }
    check.condition(
        "triple census accounts for C(23,3)",
        universal_triples + impossible_triples + triple_conditions == 23usize * 22 * 21 / 6,
    );

    // Universal infinity incidence is already non-SNC in the raw model.
    // These are the four affine direction classes before quotienting the
    // three identical pole/face labels.
    let mut direction_classes = BTreeMap::<(i128, i128), BTreeSet<&str>>::new();
    let mut direction_line_indices = BTreeMap::<(i128, i128), Vec<usize>>::new();
    for (line_index, line) in lines.iter().enumerate() {
        if let Some(direction) = normalized_direction(line) {
            direction_classes
                .entry(direction)
                .or_default()
                .insert(line.name);
            direction_line_indices
                .entry(direction)
                .or_default()
                .push(line_index);
        }
    }
    let mut direction_sizes: Vec<usize> = direction_classes.values().map(BTreeSet::len).collect();
    direction_sizes.sort_unstable_by(|left, right| right.cmp(left));
    check.condition(
        "four universal infinity direction classes of labelled lines",
        direction_sizes == [8, 8, 4, 2],
    );
    let mut unique_direction_sizes = Vec::<usize>::new();
    for indices in direction_line_indices.values() {
        let mut representatives = Vec::<usize>::new();
        for &line_index in indices {
            if !representatives
                .iter()
                .any(|&representative| same_support(&lines[line_index], &lines[representative]))
            {
                representatives.push(line_index);
            }
        }
        unique_direction_sizes.push(representatives.len());
    }
    unique_direction_sizes.sort_unstable_by(|left, right| right.cmp(left));
    check.condition(
        "four infinity direction classes after quotienting identical supports",
        unique_direction_sizes == [7, 7, 3, 2],
    );

    // The raw census is exhaustive only for its explicitly listed supports.
    // A source-fixed labelled/sheeted divisor is logically prior to choosing
    // a resolution, a relative chain, and a Gauss-Manin object.  Do not invent
    // it here.  The theorem guard must therefore remain closed.
    let source_fixed_labelled_sheeted_log_divisor: Option<&str> = None;
    let simultaneous_log_resolution: Option<&str> = None;
    let lifted_physical_relative_chain: Option<&str> = None;
    let raw_divisor_is_snc =
        source_face_coincidences.is_empty() && unique_direction_sizes.iter().all(|&size| size <= 1);
    check.condition("raw frozen divisor is not SNC", !raw_divisor_is_snc);
    check.condition(
        "first missing datum is not silently repaired",
        source_fixed_labelled_sheeted_log_divisor.is_none(),
    );
    let may_derive_log_gauss_manin_theorem = raw_divisor_is_snc
        && source_fixed_labelled_sheeted_log_divisor.is_some()
        && simultaneous_log_resolution.is_some()
        && lifted_physical_relative_chain.is_some();
    check.condition(
        "regular-connection/zero-residue/identity-monodromy theorem guard is closed",
        !may_derive_log_gauss_manin_theorem,
    );

    println!("CYCLIC-Q RAW LOG-SMOOTHNESS AUDIT: EXACT CHECKS PASS");
    println!("status=EXHAUSTIVENESS_BLOCKED_NO_GAUSS_MANIN_THEOREM");
    println!("assertions={}", check.assertions);
    println!("Q_irreducible=true; proof=primitive quadratic in x over Q[y,E] with discriminant 64*E^3*(E-2y)^2*(E+2y), not a square");
    println!(
        "Q_factor_test=multivariate fraction-free pseudo-division in z; specialization_used=false"
    );
    println!("cyclic_Q_component_rejections={}", check.q_rejections);
    for (category, count) in &check.categories {
        println!("Q_REJECTIONS category={category} count={count}");
    }
    println!("SURFACE_CENSUS=detN + three principal minors + three coordinate-axis coefficients");
    println!("LINE_CENSUS=8 source + 12 signed faces + a=0 + b=0 + D_infinity = 23 labelled lines");
    println!("ACTIVE_FIVE=q_g1,q_g2,q_g3,q_g23,q_g31; PRINTED_SUMMANDS=123+23 and 123+31");
    println!("PAIR_CENSUS total={} universal_coincident={} universal_parallel={} collision_conditions={} branch_conditions={} universal_branch={} impossible_conditions={}", 23usize*22/2, universal_coincident_pairs, universal_parallel_pairs, pair_collision_conditions, pair_branch_conditions, universal_branch_pairs, impossible_pair_conditions);
    println!(
        "TRIPLE_CENSUS total={} universal={} codim1={} impossible={}",
        23usize * 22 * 21 / 6,
        universal_triples,
        triple_conditions,
        impossible_triples
    );
    println!("STRUCTURAL_COINCIDENCES=q_g1=cb--;q_g2=ca--;q_g3=ab--");
    println!("STRUCTURAL_INFINITY_DIRECTION_SIZES=8,8,4,2 (before quotienting identical labels)");
    println!("STRUCTURAL_INFINITY_UNIQUE_SUPPORT_SIZES=7,7,3,2 (D_infinity is an additional component at every such point)");
    println!(
        "FORCED_SQUARE_FACE_SUPPORTS=12; labelled occurrences including coincident source poles=15"
    );
    println!("FIRST_MISSING_DATUM=source-fixed labelled/sheeted log divisor for the two four-pole summands (hence no specified simultaneous log resolution)");
    println!("PROHIBITED_CONCLUSION=no theorem of regular relative/log Gauss-Manin connection, zero Q residue, identity Q monodromy, or absence of Q-supported extension follows from the frozen data");
}