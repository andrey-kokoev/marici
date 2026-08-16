//! Exact certificate for the homogeneous three-site marked-relative Q test.
//!
//! Provenance used by this checker is deliberately limited to the frozen
//! arXiv:2408.16386v2 source and ledger entries 148--152.  In particular, the
//! frozen source prints Q but does not print the P in (P+sqrt(Q))/(P-sqrt(Q))
//! or attach that letter to a particular denominator/boundary section.  The
//! final report therefore leaves that last geometric identification open.

use std::collections::BTreeMap;
use std::fmt;

const NV: usize = 9;
const X: usize = 0;
const Y: usize = 1;
const Z: usize = 2;
const ET: usize = 3;
const C: usize = 4; // y_12
const AA: usize = 5; // y_23
const BB: usize = 6; // y_31
const U: usize = 7;
const S: usize = 8;
const VAR_NAMES: [&str; NV] = ["X1", "X2", "X3", "E_T", "y12", "a", "b", "u", "s"];

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
        let mut exponent = [0; NV];
        exponent[index] = 1;
        let mut terms = BTreeMap::new();
        terms.insert(exponent, 1);
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
        if scalar == 0 {
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
                for i in 0..NV {
                    monomial[i] = left_monomial[i]
                        .checked_add(right_monomial[i])
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

    fn derivative(&self, variable: usize) -> Self {
        let mut result = Self::zero();
        for (&mut_monomial, &coefficient) in &self.terms {
            let exponent = mut_monomial[variable];
            if exponent == 0 {
                continue;
            }
            let mut monomial = mut_monomial;
            monomial[variable] -= 1;
            let differentiated = coefficient
                .checked_mul(i128::from(exponent))
                .expect("integer overflow in derivative");
            result = result.add(&Self::from_term(monomial, differentiated));
        }
        result
    }

    fn substitute(&self, variable: usize, replacement: &Self) -> Self {
        let mut result = Self::zero();
        for (&monomial, &coefficient) in &self.terms {
            let exponent = monomial[variable];
            let mut residual = monomial;
            residual[variable] = 0;
            let term = Self::from_term(residual, coefficient).mul(&replacement.pow(exponent));
            result = result.add(&term);
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

    fn component_in(&self, variables: &[usize], degree: u8) -> Self {
        let mut result = Self::zero();
        for (&monomial, &coefficient) in &self.terms {
            let actual_degree: u8 = variables
                .iter()
                .map(|&variable| monomial[variable])
                .fold(0u8, |acc, item| {
                    acc.checked_add(item).expect("degree overflow")
                });
            if actual_degree == degree {
                result = result.add(&Self::from_term(monomial, coefficient));
            }
        }
        result
    }

    fn from_term(monomial: Monomial, coefficient: i128) -> Self {
        if coefficient == 0 {
            return Self::zero();
        }
        let mut terms = BTreeMap::new();
        terms.insert(monomial, coefficient);
        Self { terms }
    }

    fn is_zero(&self) -> bool {
        self.terms.is_empty()
    }

    fn degree_in(&self, variable: usize) -> Option<u8> {
        self.terms.keys().map(|monomial| monomial[variable]).max()
    }

    fn only_uses(&self, variables: &[usize]) -> bool {
        self.terms.keys().all(|monomial| {
            monomial
                .iter()
                .enumerate()
                .all(|(index, &exponent)| exponent == 0 || variables.contains(&index))
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
        if self.terms.is_empty() {
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

fn product(polynomials: &[Poly]) -> Poly {
    polynomials
        .iter()
        .fold(Poly::one(), |accumulator, item| accumulator.mul(item))
}

fn determinant(matrix: &[Vec<Poly>]) -> Poly {
    assert!(
        !matrix.is_empty(),
        "empty determinant is not used by this certificate"
    );
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

fn sylvester_resultant(f: &[Poly], g: &[Poly]) -> Poly {
    assert!(
        f.len() >= 2 && g.len() >= 2,
        "resultant needs positive degrees"
    );
    let f_degree = f.len() - 1;
    let g_degree = g.len() - 1;
    let size = f_degree + g_degree;
    let mut matrix = vec![vec![Poly::zero(); size]; size];
    for row in 0..g_degree {
        for (offset, coefficient) in f.iter().enumerate() {
            matrix[row][row + offset] = coefficient.clone();
        }
    }
    for row in 0..f_degree {
        for (offset, coefficient) in g.iter().enumerate() {
            matrix[g_degree + row][row + offset] = coefficient.clone();
        }
    }
    determinant(&matrix)
}

fn coefficients_descending(polynomial: &Poly, variable: usize) -> Vec<Poly> {
    let degree = polynomial
        .degree_in(variable)
        .expect("the zero polynomial has no coefficient vector");
    (0..=degree)
        .rev()
        .map(|exponent| polynomial.coefficient(variable, exponent))
        .collect()
}

fn derivative_resultant(polynomial: &Poly, variable: usize) -> Poly {
    let derivative = polynomial.derivative(variable);
    assert!(
        !derivative.is_zero(),
        "a constant polynomial has no branch nontransversality resultant"
    );
    sylvester_resultant(
        &coefficients_descending(polynomial, variable),
        &coefficients_descending(&derivative, variable),
    )
}

fn variable_power(variable: usize, exponent: u8) -> Poly {
    Poly::var(variable).pow(exponent)
}

/// Fraction-free pseudo-remainder in one variable.  Vanishing is equivalent
/// to divisibility over the fraction field of the coefficient domain.
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
        remainder = remainder.mul(&divisor_lead).sub(
            &divisor
                .mul(&remainder_lead)
                .mul(&variable_power(variable, shift)),
        );
    }
    remainder
}

#[derive(Clone)]
struct AffineLine {
    name: &'static str,
    alpha: i128,
    beta: i128,
    gamma: Poly,
    active_in_residue: bool,
}

impl AffineLine {
    fn polynomial(&self, a: &Poly, b: &Poly) -> Poly {
        sum(&[a.scale(self.alpha), b.scale(self.beta), self.gamma.clone()])
    }

    fn restrict(&self, polynomial: &Poly, a: &Poly, b: &Poly) -> (Poly, usize) {
        if self.beta == 1 || self.beta == -1 {
            let b_value = a.scale(self.alpha).add(&self.gamma).scale(-self.beta);
            (polynomial.substitute(BB, &b_value), AA)
        } else {
            assert!(
                self.alpha == 1 || self.alpha == -1,
                "line must have a unit coefficient"
            );
            let a_value = b.scale(self.beta).add(&self.gamma).scale(-self.alpha);
            (polynomial.substitute(AA, &a_value), BB)
        }
    }

    fn specialize(&self, variable: usize, replacement: &Poly) -> Self {
        Self {
            name: self.name,
            alpha: self.alpha,
            beta: self.beta,
            gamma: self.gamma.substitute(variable, replacement),
            active_in_residue: self.active_in_residue,
        }
    }
}

fn same_affine_line(left: &AffineLine, right: &AffineLine) -> bool {
    (left.alpha == right.alpha && left.beta == right.beta && left.gamma == right.gamma)
        || (left.alpha == -right.alpha
            && left.beta == -right.beta
            && left.gamma == right.gamma.neg())
}

fn affine_intersection(left: &AffineLine, right: &AffineLine) -> Option<(Poly, Poly)> {
    let determinant = left.alpha * right.beta - right.alpha * left.beta;
    if determinant == 0 {
        return None;
    }
    assert!(
        determinant == 1 || determinant == -1,
        "source-line intersection unexpectedly requires a nonintegral coordinate"
    );
    let a_value = left
        .gamma
        .scale(-right.beta)
        .add(&right.gamma.scale(left.beta))
        .scale(determinant);
    let b_value = right
        .gamma
        .scale(-left.alpha)
        .add(&left.gamma.scale(right.alpha))
        .scale(determinant);
    Some((a_value, b_value))
}

struct Checker {
    assertions: usize,
}

impl Checker {
    fn new() -> Self {
        Self { assertions: 0 }
    }

    fn equal(&mut self, label: &str, actual: &Poly, expected: &Poly) {
        self.assertions += 1;
        if actual != expected {
            let difference = actual.sub(expected);
            panic!("FAIL [{label}] exact polynomial difference: {difference}");
        }
    }

    fn condition(&mut self, label: &str, condition: bool) {
        self.assertions += 1;
        assert!(condition, "FAIL [{label}]");
    }
}

fn triangle_cm(left: &Poly, right: &Poly, opposite: &Poly) -> Poly {
    let sum_side = left.add(right);
    let difference_side = left.sub(right);
    sum_side
        .pow(2)
        .sub(&opposite.pow(2))
        .mul(&difference_side.pow(2).sub(&opposite.pow(2)))
}

fn infinity_branch_value(f_homogeneous: &Poly, alpha_a: i128, alpha_b: i128) -> Poly {
    // alpha_a*a + alpha_b*b + lower terms = 0 has direction [a:b]=[alpha_b:-alpha_a].
    f_homogeneous
        .substitute(AA, &Poly::constant(alpha_b))
        .substitute(BB, &Poly::constant(-alpha_a))
}

fn main() {
    let mut check = Checker::new();

    let x = Poly::var(X);
    let y = Poly::var(Y);
    let z = Poly::var(Z);
    let et = Poly::var(ET);
    let c = Poly::var(C);
    let a = Poly::var(AA);
    let b = Poly::var(BB);
    let u = Poly::var(U);
    let s = Poly::var(S);
    let one = Poly::one();
    let zero = Poly::zero();

    let x2 = x.pow(2);
    let y2 = y.pow(2);
    let z2 = z.pow(2);
    let c2 = c.pow(2);
    let a2 = a.pow(2);
    let b2 = b.pow(2);
    let total_energy = sum(&[x.clone(), y.clone(), z.clone()]);
    let total_energy2 = total_energy.pow(2);
    let h = x2.add(&y2).sub(&z2);
    let a_discriminant = x.sub(&y).pow(2).sub(&z2);
    let b_discriminant = x.add(&y).pow(2).sub(&z2);

    // Vertex order: apex; the y12, y23, y31 base vertices.  The fixed base
    // edges opposite y23, y31, y12 are X1, X2, X3 as dictated by the graph.
    let cm = vec![
        vec![
            zero.clone(),
            one.clone(),
            one.clone(),
            one.clone(),
            one.clone(),
        ],
        vec![
            one.clone(),
            zero.clone(),
            c2.clone(),
            a2.clone(),
            b2.clone(),
        ],
        vec![
            one.clone(),
            c2.clone(),
            zero.clone(),
            y2.clone(),
            x2.clone(),
        ],
        vec![
            one.clone(),
            a2.clone(),
            y2.clone(),
            zero.clone(),
            z2.clone(),
        ],
        vec![
            one.clone(),
            b2.clone(),
            x2.clone(),
            z2.clone(),
            zero.clone(),
        ],
    ];
    let d_cm = determinant(&cm);

    let f_homogeneous = sum(&[
        x2.mul(&a.pow(4)),
        h.mul(&a2).mul(&b2).neg(),
        y2.mul(&b.pow(4)),
    ]);
    let g_a_general = x2
        .sub(&c2)
        .mul(&x2.sub(&y2).sub(&z2))
        .sub(&c2.mul(&z2).scale(2));
    let g_b_general = y2
        .sub(&c2)
        .mul(&y2.sub(&x2).sub(&z2))
        .sub(&c2.mul(&z2).scale(2));
    let h_general = z2.mul(&c2.sub(&y2).mul(&c2.sub(&x2)).add(&c2.mul(&z2)));
    let k_general = sum(&[
        f_homogeneous.clone(),
        g_a_general.mul(&a2),
        g_b_general.mul(&b2),
        h_general,
    ]);
    check.equal("Cayley-Menger scale D_CM=-2K", &d_cm, &k_general.scale(-2));

    // The frozen source literally has q_G12=E+y12, so dq/dy12=1 and the
    // residue is c=y12=-E.  No factor of two is inferred from the caption.
    let q_g12_deleted = total_energy.add(&c);
    check.equal("dq_G12/dy12=1", &q_g12_deleted.derivative(C), &one);
    let k0 = k_general.substitute(C, &total_energy.neg());

    let g_a = h
        .mul(&x2.add(&total_energy2))
        .sub(&x2.mul(&y2.add(&total_energy2)).scale(2));
    let g_b = h
        .mul(&y2.add(&total_energy2))
        .sub(&y2.mul(&x2.add(&total_energy2)).scale(2));
    let h0 = z2.mul(
        &total_energy2
            .sub(&y2)
            .mul(&total_energy2.sub(&x2))
            .add(&total_energy2.mul(&z2)),
    );
    let ledger_k0 = sum(&[
        f_homogeneous.clone(),
        g_a.mul(&a2),
        g_b.mul(&b2),
        h0.clone(),
    ]);
    check.equal("q_G12 residue K0", &k0, &ledger_k0);
    check.equal(
        "K0 tangential degree four",
        &k0.component_in(&[AA, BB], 4),
        &f_homogeneous,
    );
    check.equal(
        "K0 tangential degree two",
        &k0.component_in(&[AA, BB], 2),
        &g_a.mul(&a2).add(&g_b.mul(&b2)),
    );
    check.equal(
        "K0 tangential degree zero",
        &k0.component_in(&[AA, BB], 0),
        &h0,
    );

    // All ten source denominators, including the two-site subgraphs derived
    // from the source's universal "sites plus departing edges" definition.
    let denominators: Vec<(&str, Poly, Poly)> = vec![
        ("q_G", total_energy.clone(), total_energy.clone()),
        ("q_g1", x.add(&c).add(&b), b.sub(&y).sub(&z)),
        ("q_g2", y.add(&c).add(&a), a.sub(&x).sub(&z)),
        ("q_g3", z.add(&a).add(&b), z.add(&a).add(&b)),
        (
            "q_g12",
            x.add(&y).add(&a).add(&b),
            x.add(&y).add(&a).add(&b),
        ),
        ("q_g23", y.add(&z).add(&c).add(&b), b.sub(&x)),
        ("q_g31", z.add(&x).add(&c).add(&a), a.sub(&y)),
        ("q_G12", q_g12_deleted.clone(), zero.clone()),
        ("q_G23", total_energy.add(&a), total_energy.add(&a)),
        ("q_G31", total_energy.add(&b), total_energy.add(&b)),
    ];
    for (name, original, expected_residue) in &denominators {
        check.equal(
            &format!("denominator restriction {name}"),
            &original.substitute(C, &total_energy.neg()),
            expected_residue,
        );
    }

    // The ten-denominator union leaves eight nonconstant lines after taking
    // q_G12=0 (q_G is then a kinematic constant and q_G12 is the residue).
    // The actual q_G12 term of the printed integration form is narrower:
    // q_g1*q_g2*q_g3 times (1/q_g23 + 1/q_g31).  Thus each summand has four
    // nonconstant poles and their union has the following active five.
    let source_lines = vec![
        AffineLine {
            name: "q_g1",
            alpha: 0,
            beta: 1,
            gamma: y.add(&z).neg(),
            active_in_residue: true,
        },
        AffineLine {
            name: "q_g2",
            alpha: 1,
            beta: 0,
            gamma: x.add(&z).neg(),
            active_in_residue: true,
        },
        AffineLine {
            name: "q_g3",
            alpha: 1,
            beta: 1,
            gamma: z.clone(),
            active_in_residue: true,
        },
        AffineLine {
            name: "q_g12",
            alpha: 1,
            beta: 1,
            gamma: x.add(&y),
            active_in_residue: false,
        },
        AffineLine {
            name: "q_g23",
            alpha: 0,
            beta: 1,
            gamma: x.neg(),
            active_in_residue: true,
        },
        AffineLine {
            name: "q_g31",
            alpha: 1,
            beta: 0,
            gamma: y.neg(),
            active_in_residue: true,
        },
        AffineLine {
            name: "q_G23",
            alpha: 1,
            beta: 0,
            gamma: total_energy.clone(),
            active_in_residue: false,
        },
        AffineLine {
            name: "q_G31",
            alpha: 0,
            beta: 1,
            gamma: total_energy.clone(),
            active_in_residue: false,
        },
    ];
    let active_five: Vec<&str> = source_lines
        .iter()
        .filter(|line| line.active_in_residue)
        .map(|line| line.name)
        .collect();
    check.condition(
        "full nonconstant line union has eight members",
        source_lines.len() == 8,
    );
    check.condition(
        "actual q_G12 residue has five active nonconstant pole lines",
        active_five == vec!["q_g1", "q_g2", "q_g3", "q_g23", "q_g31"],
    );

    // The four triangular 2-faces and all their linear boundary branches.
    let face_ca = triangle_cm(&c, &a, &y).substitute(C, &total_energy.neg());
    let face_cb = triangle_cm(&c, &b, &x).substitute(C, &total_energy.neg());
    let face_ab = triangle_cm(&a, &b, &z);
    let face_xyz = triangle_cm(&x, &y, &z);
    let expected_face_ca = product(&[
        a.sub(&total_energy).sub(&y),
        a.sub(&total_energy).add(&y),
        a.add(&total_energy).sub(&y),
        a.add(&total_energy).add(&y),
    ]);
    let expected_face_cb = product(&[
        b.sub(&total_energy).sub(&x),
        b.sub(&total_energy).add(&x),
        b.add(&total_energy).sub(&x),
        b.add(&total_energy).add(&x),
    ]);
    let expected_face_ab = product(&[
        a.add(&b).sub(&z),
        a.add(&b).add(&z),
        a.sub(&b).sub(&z),
        a.sub(&b).add(&z),
    ]);
    check.equal("face (y12,y23;X2) restriction", &face_ca, &expected_face_ca);
    check.equal("face (y12,y31;X1) restriction", &face_cb, &expected_face_cb);
    check.equal("face (y23,y31;X3) restriction", &face_ab, &expected_face_ab);
    check.equal(
        "fixed base face",
        &face_xyz,
        &a_discriminant.mul(&b_discriminant),
    );

    // On every signed triangle-boundary branch the tetrahedral branch
    // polynomial becomes an exact square.  These sixteen identities retain
    // all face branches rather than choosing physical signs after residue.
    let signs = [-1i128, 1i128];
    for &s1 in &signs {
        for &s2 in &signs {
            let a_on_face = c.scale(s1).add(&y.scale(s2));
            let ca_root = c
                .mul(&a2.add(&b2).sub(&z2))
                .sub(&a.scale(s1).mul(&c2.add(&b2).sub(&x2)));
            check.equal(
                &format!("square collision face ca signs {s1},{s2}"),
                &k_general.substitute(AA, &a_on_face),
                &ca_root.substitute(AA, &a_on_face).pow(2),
            );

            let b_on_face = c.scale(s1).add(&x.scale(s2));
            let cb_root = c
                .mul(&a2.add(&b2).sub(&z2))
                .sub(&b.scale(s1).mul(&c2.add(&a2).sub(&y2)));
            check.equal(
                &format!("square collision face cb signs {s1},{s2}"),
                &k_general.substitute(BB, &b_on_face),
                &cb_root.substitute(BB, &b_on_face).pow(2),
            );

            let b_on_face_ab = a.scale(s1).add(&z.scale(s2));
            let ab_root = a
                .mul(&c2.add(&b2).sub(&x2))
                .sub(&b.scale(s1).mul(&c2.add(&a2).sub(&y2)));
            check.equal(
                &format!("square collision face ab signs {s1},{s2}"),
                &k_general.substitute(BB, &b_on_face_ab),
                &ab_root.substitute(BB, &b_on_face_ab).pow(2),
            );

            let z_on_base = x.scale(s1).add(&y.scale(s2));
            let epsilon = -s1 * s2;
            let base_root = y
                .mul(&x2.add(&c2).sub(&b2))
                .sub(&x.scale(epsilon).mul(&y2.add(&c2).sub(&a2)));
            check.equal(
                &format!("square collision fixed base signs {s1},{s2}"),
                &k_general.substitute(Z, &z_on_base),
                &base_root.substitute(Z, &z_on_base).pow(2),
            );
        }
    }

    // Retain the twelve signed face branches as explicit affine lines with
    // their reduced square roots.  These data drive both the finite
    // elimination audit and the exact source-line coincidence census.
    let sign_pairs = [(-1i128, -1i128), (-1, 1), (1, -1), (1, 1)];
    let ca_names = ["ca--", "ca-+", "ca+-", "ca++"];
    let cb_names = ["cb--", "cb-+", "cb+-", "cb++"];
    let ab_names = ["ab--", "ab-+", "ab+-", "ab++"];
    let mut face_lines_with_roots: Vec<(AffineLine, Poly)> = Vec::new();
    for (index, &(s1, s2)) in sign_pairs.iter().enumerate() {
        let ca_line = AffineLine {
            name: ca_names[index],
            alpha: 1,
            beta: 0,
            gamma: total_energy.scale(s1).sub(&y.scale(s2)),
            active_in_residue: false,
        };
        let ca_root = c
            .mul(&a2.add(&b2).sub(&z2))
            .sub(&a.scale(s1).mul(&c2.add(&b2).sub(&x2)))
            .substitute(C, &total_energy.neg());
        let (ca_root_restricted, _) = ca_line.restrict(&ca_root, &a, &b);
        let (ca_k_restricted, _) = ca_line.restrict(&k0, &a, &b);
        check.equal(
            &format!("retained square root {}", ca_line.name),
            &ca_k_restricted,
            &ca_root_restricted.pow(2),
        );
        face_lines_with_roots.push((ca_line, ca_root_restricted));

        let cb_line = AffineLine {
            name: cb_names[index],
            alpha: 0,
            beta: 1,
            gamma: total_energy.scale(s1).sub(&x.scale(s2)),
            active_in_residue: false,
        };
        let cb_root = c
            .mul(&a2.add(&b2).sub(&z2))
            .sub(&b.scale(s1).mul(&c2.add(&a2).sub(&y2)))
            .substitute(C, &total_energy.neg());
        let (cb_root_restricted, _) = cb_line.restrict(&cb_root, &a, &b);
        let (cb_k_restricted, _) = cb_line.restrict(&k0, &a, &b);
        check.equal(
            &format!("retained square root {}", cb_line.name),
            &cb_k_restricted,
            &cb_root_restricted.pow(2),
        );
        face_lines_with_roots.push((cb_line, cb_root_restricted));

        let ab_line = AffineLine {
            name: ab_names[index],
            alpha: -s1,
            beta: 1,
            gamma: z.scale(-s2),
            active_in_residue: false,
        };
        let ab_root = a
            .mul(&c2.add(&b2).sub(&x2))
            .sub(&b.scale(s1).mul(&c2.add(&a2).sub(&y2)))
            .substitute(C, &total_energy.neg());
        let (ab_root_restricted, _) = ab_line.restrict(&ab_root, &a, &b);
        let (ab_k_restricted, _) = ab_line.restrict(&k0, &a, &b);
        check.equal(
            &format!("retained square root {}", ab_line.name),
            &ab_k_restricted,
            &ab_root_restricted.pow(2),
        );
        face_lines_with_roots.push((ab_line, ab_root_restricted));
    }
    check.condition(
        "twelve signed simplex face lines retained",
        face_lines_with_roots.len() == 12,
    );

    let expected_generic_face_matches: [Option<&str>; 12] = [
        Some("q_g2"),
        Some("q_g1"),
        Some("q_g3"),
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ];
    for ((face_line, _), expected_match) in face_lines_with_roots
        .iter()
        .zip(expected_generic_face_matches)
    {
        let matches: Vec<&str> = source_lines
            .iter()
            .filter(|source_line| same_affine_line(face_line, source_line))
            .map(|source_line| source_line.name)
            .collect();
        let expected: Vec<&str> = expected_match.into_iter().collect();
        check.condition(
            &format!("generic source coincidence for {}", face_line.name),
            matches == expected,
        );
    }

    // Branch/branch collision: first in u=t^2, then for the full even quartic.
    let branch_u = sum(&[x2.mul(&u.pow(2)), h.mul(&u).neg(), y2.clone()]);
    let branch_u_derivative = branch_u.derivative(U);
    let branch_resultant =
        sylvester_resultant(&[x2.clone(), h.neg(), y2.clone()], &[x2.scale(2), h.neg()]);
    check.equal(
        "branch quadratic resultant",
        &branch_resultant,
        &x2.mul(&a_discriminant).mul(&b_discriminant).neg(),
    );
    check.equal(
        "explicit derivative agrees with resultant coefficients",
        &branch_u_derivative,
        &x2.mul(&u).scale(2).sub(&h),
    );
    let quartic_resultant = sylvester_resultant(
        &[x2.clone(), zero.clone(), h.neg(), zero.clone(), y2.clone()],
        &[x2.scale(4), zero.clone(), h.scale(-2), zero.clone()],
    );
    let expected_quartic_resultant = x2
        .pow(2)
        .mul(&y2)
        .mul(&a_discriminant.pow(2))
        .mul(&b_discriminant.pow(2))
        .scale(16);
    check.equal(
        "even quartic resultant",
        &quartic_resultant,
        &expected_quartic_resultant,
    );

    // Every nonconstant, nonresidue source denominator has one projective
    // infinity direction.  Exact substitution into F records its branch
    // collision factor; none supplies generic Q support there.
    let denominator_directions: [(&str, i128, i128, &Poly); 8] = [
        ("q_g1", 0, 1, &x2),
        ("q_g2", 1, 0, &y2),
        ("q_g3", 1, 1, &z2),
        ("q_g12", 1, 1, &z2),
        ("q_g23", 0, 1, &x2),
        ("q_g31", 1, 0, &y2),
        ("q_G23", 1, 0, &y2),
        ("q_G31", 0, 1, &x2),
    ];
    for (name, alpha_a, alpha_b, expected) in denominator_directions {
        check.equal(
            &format!("infinity mark/branch collision {name}"),
            &infinity_branch_value(&f_homogeneous, alpha_a, alpha_b),
            expected,
        );
    }

    // All twelve signed side-face branches have the same three direction
    // types.  This checks every boundary/branch collision at infinity.
    for index in 0..4 {
        check.equal(
            &format!("face ca infinity collision branch {index}"),
            &infinity_branch_value(&f_homogeneous, 1, 0),
            &y2,
        );
        check.equal(
            &format!("face cb infinity collision branch {index}"),
            &infinity_branch_value(&f_homogeneous, 0, 1),
            &x2,
        );
        let diagonal_sign = if index < 2 { 1 } else { -1 };
        check.equal(
            &format!("face ab infinity collision branch {index}"),
            &infinity_branch_value(&f_homogeneous, 1, diagonal_sign),
            &z2,
        );
    }

    // Ledger identity and the two affine charts of its conjugate-mark
    // quadratic.  This proves the collision polynomial Q without pretending
    // that the frozen source identifies the geometric section.
    let q_identity = a_discriminant
        .mul(&b_discriminant)
        .scale(4)
        .sub(&a_discriminant.add(&b_discriminant).sub(&et.pow(2)).pow(2));
    let mark_middle = a_discriminant.add(&b_discriminant).sub(&et.pow(2)).neg();
    let mark_resultant_a_chart = sylvester_resultant(
        &[
            a_discriminant.clone(),
            mark_middle.clone(),
            b_discriminant.clone(),
        ],
        &[a_discriminant.scale(2), mark_middle.clone()],
    );
    check.equal(
        "marked-section resultant on A chart",
        &mark_resultant_a_chart,
        &a_discriminant.mul(&q_identity),
    );
    let mark_resultant_b_chart = sylvester_resultant(
        &[
            b_discriminant.clone(),
            mark_middle.clone(),
            a_discriminant.clone(),
        ],
        &[b_discriminant.scale(2), mark_middle],
    );
    check.equal(
        "marked-section resultant on B chart",
        &mark_resultant_b_chart,
        &b_discriminant.mul(&q_identity),
    );

    let q_source = sum(&[
        x.pow(4).scale(3),
        x.pow(3).mul(&y.add(&z)).scale(4),
        x2.mul(&sum(&[y2.scale(7), y.mul(&z).scale(2), z2.scale(3)]))
            .scale(-2),
        x.mul(&y.sub(&z.scale(3))).mul(&y.add(&z).pow(2)).scale(4),
        y.scale(3).sub(&z.scale(5)).mul(&y.add(&z).pow(3)),
    ]);
    check.equal(
        "source quartic Q",
        &q_identity.substitute(ET, &total_energy),
        &q_source,
    );

    // Exact generic-Q slice used for the finite provenance sweep.  If the
    // multivariate source Q divided any collision polynomial P,
    // then Q(1,2,X3) would divide P(1,2,X3).  A nonzero fraction-free
    // remainder therefore falsifies Q as a component.  X1=1, X2=2 is
    // admissible because X1*X2*(X1+X2)=6 and the specialized Q is degree four
    // and square-free.
    let specialize_xy = |polynomial: &Poly| {
        polynomial
            .substitute(X, &Poly::constant(1))
            .substitute(Y, &Poly::constant(2))
    };
    let q_slice = specialize_xy(&q_source);
    let q_slice_expected = sum(&[
        Poly::constant(35),
        z.scale(12),
        z2.scale(-70),
        z.pow(3).scale(-36),
        z.pow(4).scale(-5),
    ]);
    check.equal("generic Q slice", &q_slice, &q_slice_expected);
    let q_slice_squarefree_resultant = derivative_resultant(&q_slice, Z);
    check.equal(
        "generic Q slice square-free resultant",
        &q_slice_squarefree_resultant,
        &Poly::constant(23_739_760_640),
    );

    let mut finite_line_reports = Vec::<String>::new();
    let mut q_component_rejections = 0usize;
    for line in &source_lines {
        let line_polynomial = line.polynomial(&a, &b);
        let (line_zero, _) = line.restrict(&line_polynomial, &a, &b);
        check.equal(&format!("line solver {}", line.name), &line_zero, &zero);

        let (restricted_k, free_variable) = line.restrict(&k0, &a, &b);
        check.condition(
            &format!("nonzero finite restriction {}", line.name),
            !restricted_k.is_zero(),
        );
        let forced_root = face_lines_with_roots
            .iter()
            .find(|(face_line, _)| same_affine_line(line, face_line))
            .map(|(_, root)| root.clone());
        let reduced = if let Some(root) = &forced_root {
            check.equal(
                &format!("remove source-forced square {}", line.name),
                &restricted_k,
                &root.pow(2),
            );
            root.clone()
        } else {
            restricted_k.clone()
        };
        let reduced_slice = specialize_xy(&reduced);
        check.condition(
            &format!("slice preserves line degree {}", line.name),
            reduced.degree_in(free_variable) == reduced_slice.degree_in(free_variable),
        );
        check.condition(
            &format!("slice variables for {}", line.name),
            reduced_slice.only_uses(&[Z, free_variable]),
        );
        let resultant_slice = derivative_resultant(&reduced_slice, free_variable);
        check.condition(
            &format!("finite nontransversality resultant {}", line.name),
            !resultant_slice.is_zero() && resultant_slice.only_uses(&[Z]),
        );
        let q_remainder = pseudo_remainder(&resultant_slice, &q_slice, Z).primitive_part();
        check.condition(
            &format!("Q is absent from finite line collision {}", line.name),
            !q_remainder.is_zero(),
        );
        q_component_rejections += 1;
        let restricted_factor = if let Some(root) = &forced_root {
            format!("({root})^2")
        } else {
            restricted_k.to_string()
        };
        finite_line_reports.push(format!(
            "FINITE_LINE {} active={} forced_square={} free={} K|line={} Res_slice={} Qrem_primitive={}",
            line.name,
            line.active_in_residue,
            forced_root.is_some(),
            VAR_NAMES[free_variable],
            restricted_factor,
            resultant_slice,
            q_remainder
        ));
    }

    let mut boundary_line_reports = Vec::<String>::new();
    for (face_line, reduced_root) in &face_lines_with_roots {
        let (_, free_variable) = face_line.restrict(&k0, &a, &b);
        let root_slice = specialize_xy(reduced_root);
        check.condition(
            &format!("slice preserves boundary degree {}", face_line.name),
            reduced_root.degree_in(free_variable) == root_slice.degree_in(free_variable),
        );
        let resultant_slice = derivative_resultant(&root_slice, free_variable);
        check.condition(
            &format!("finite boundary resultant {}", face_line.name),
            !resultant_slice.is_zero() && resultant_slice.only_uses(&[Z]),
        );
        let q_remainder = pseudo_remainder(&resultant_slice, &q_slice, Z).primitive_part();
        check.condition(
            &format!("Q is absent from boundary collision {}", face_line.name),
            !q_remainder.is_zero(),
        );
        q_component_rejections += 1;
        boundary_line_reports.push(format!(
            "FINITE_BOUNDARY {} K|line=({})^2 Res_reduced_slice={} Qrem_primitive={}",
            face_line.name, reduced_root, resultant_slice, q_remainder
        ));
    }

    // Test all 21 nonparallel pairs among the eight source lines.  For a pair
    // meeting a signed face line, K is checked through the corresponding
    // reduced square root; otherwise K itself is tested.  Universal zero
    // intersections are recorded separately and do not define a Q divisor.
    let mut pair_reports = Vec::<String>::new();
    let mut parallel_pairs = 0usize;
    let mut nonparallel_pairs = 0usize;
    let mut universal_branch_pairs = 0usize;
    for left_index in 0..source_lines.len() {
        for right_index in (left_index + 1)..source_lines.len() {
            let left = &source_lines[left_index];
            let right = &source_lines[right_index];
            let Some((a_value, b_value)) = affine_intersection(left, right) else {
                parallel_pairs += 1;
                continue;
            };
            nonparallel_pairs += 1;
            check.equal(
                &format!("pair point lies on {}", left.name),
                &left
                    .polynomial(&a, &b)
                    .substitute(AA, &a_value)
                    .substitute(BB, &b_value),
                &zero,
            );
            check.equal(
                &format!("pair point lies on {}", right.name),
                &right
                    .polynomial(&a, &b)
                    .substitute(AA, &a_value)
                    .substitute(BB, &b_value),
                &zero,
            );
            let k_at_pair = k0.substitute(AA, &a_value).substitute(BB, &b_value);
            let forced_root = face_lines_with_roots
                .iter()
                .find(|(face_line, _)| {
                    same_affine_line(left, face_line) || same_affine_line(right, face_line)
                })
                .map(|(_, root)| root.substitute(AA, &a_value).substitute(BB, &b_value));
            let reduced_pair_value = if let Some(root_value) = &forced_root {
                check.equal(
                    &format!("pair source square {} x {}", left.name, right.name),
                    &k_at_pair,
                    &root_value.pow(2),
                );
                root_value.clone()
            } else {
                k_at_pair.clone()
            };
            if reduced_pair_value.is_zero() {
                universal_branch_pairs += 1;
                pair_reports.push(format!(
                    "FINITE_PAIR {} x {}: universal reduced branch intersection",
                    left.name, right.name
                ));
                continue;
            }
            let pair_slice = specialize_xy(&reduced_pair_value);
            check.condition(
                &format!("pair slice variables {} x {}", left.name, right.name),
                pair_slice.only_uses(&[Z]),
            );
            let q_remainder = pseudo_remainder(&pair_slice, &q_slice, Z).primitive_part();
            check.condition(
                &format!("Q absent from pair {} x {}", left.name, right.name),
                !q_remainder.is_zero(),
            );
            q_component_rejections += 1;
            pair_reports.push(format!(
                "FINITE_PAIR {} x {} reduced={} Qrem_primitive={}",
                left.name, right.name, reduced_pair_value, q_remainder
            ));
        }
    }
    check.condition("seven parallel source-line pairs", parallel_pairs == 7);
    check.condition(
        "twenty-one nonparallel source-line pairs",
        nonparallel_pairs == 21,
    );

    // This is the exhaustive direct elimination/projection attempt authorized
    // by the frozen data: eight source lines, twelve signed simplex faces, and
    // every nonparallel source-line pair.  No candidate has Q as a component.
    check.condition(
        "direct finite Q-component sweep is complete",
        q_component_rejections
            == source_lines.len() + face_lines_with_roots.len() + nonparallel_pairs
                - universal_branch_pairs,
    );

    // Normal expansion keeps E_T independent and puts X3=E_T-X1-X2.
    let z_from_et = et.sub(&x).sub(&y);
    let q_et = q_identity.substitute(Z, &z_from_et);
    let q_et_expected = sum(&[
        x2.mul(&y2).scale(-16),
        x.mul(&y).mul(&et.pow(2)).scale(-8),
        x.add(&y).mul(&et.pow(3)).scale(8),
        et.pow(4).scale(-5),
    ]);
    check.equal("complete E_T expansion", &q_et, &q_et_expected);
    check.equal(
        "gr0_E_T Q",
        &q_et.coefficient(ET, 0),
        &x2.mul(&y2).scale(-16),
    );
    check.equal("gr1_E_T Q=0", &q_et.coefficient(ET, 1), &zero);
    check.equal(
        "gr2_E_T Q=-8 X1 X2",
        &q_et.coefficient(ET, 2),
        &x.mul(&y).scale(-8),
    );
    check.equal("gr3_E_T Q", &q_et.coefficient(ET, 3), &x.add(&y).scale(8));
    check.equal("gr4_E_T Q", &q_et.coefficient(ET, 4), &Poly::constant(-5));

    // Exact total-energy central fiber.  Homogenizing a=alpha/s,
    // b=beta/s gives Kbar_0=R^2 with the requested normalization.
    let z_flat = x.add(&y).neg();
    let kbar = sum(&[
        f_homogeneous.clone(),
        g_a.mul(&a2).mul(&s.pow(2)),
        g_b.mul(&b2).mul(&s.pow(2)),
        h0.mul(&s.pow(4)),
    ]);
    let kbar_flat = kbar.substitute(Z, &z_flat);
    let r_flat = x
        .mul(&a2)
        .add(&y.mul(&b2))
        .sub(&x.mul(&y).mul(&x.add(&y)).mul(&s.pow(2)));
    check.equal("E_T=0 compactified Kbar_0=R^2", &kbar_flat, &r_flat.pow(2));
    let r_affine_flat = r_flat.substitute(S, &one);
    let k0_flat = k0.substitute(Z, &z_flat);
    check.equal(
        "E_T=0 affine K0=R_affine^2",
        &k0_flat,
        &r_affine_flat.pow(2),
    );

    let full_eight_flat_expected = vec![
        b.add(&x),
        a.add(&y),
        a.add(&b).sub(&x).sub(&y),
        a.add(&b).add(&x).add(&y),
        b.sub(&x),
        a.sub(&y),
        a.clone(),
        b.clone(),
    ];
    let source_lines_flat: Vec<AffineLine> = source_lines
        .iter()
        .map(|line| line.specialize(Z, &z_flat))
        .collect();
    for ((line, expected), original) in source_lines_flat
        .iter()
        .zip(&full_eight_flat_expected)
        .zip(&source_lines)
    {
        check.equal(
            &format!("E_T=0 full-eight specialization {}", line.name),
            &line.polynomial(&a, &b),
            expected,
        );
        check.condition(
            &format!("E_T=0 activity retained {}", line.name),
            line.active_in_residue == original.active_in_residue,
        );
    }
    let active_five_flat: Vec<Poly> = source_lines_flat
        .iter()
        .filter(|line| line.active_in_residue)
        .map(|line| line.polynomial(&a, &b))
        .collect();
    check.condition(
        "E_T=0 active-five specializations",
        active_five_flat
            == vec![
                b.add(&x),
                a.add(&y),
                a.add(&b).sub(&x).sub(&y),
                b.sub(&x),
                a.sub(&y),
            ],
    );

    // On E_T=0 the signed minors pair up and six of the twelve branches
    // coincide with the indicated source lines (with multiplicities shown).
    let expected_flat_face_matches: [Option<&str>; 12] = [
        Some("q_g2"),
        Some("q_g1"),
        Some("q_g3"),
        Some("q_g31"),
        Some("q_g23"),
        Some("q_g12"),
        Some("q_g2"),
        Some("q_g1"),
        None,
        Some("q_g31"),
        Some("q_g23"),
        None,
    ];
    for ((face_line, _), expected_match) in
        face_lines_with_roots.iter().zip(expected_flat_face_matches)
    {
        let face_flat = face_line.specialize(Z, &z_flat);
        let matches: Vec<&str> = source_lines_flat
            .iter()
            .filter(|source_line| same_affine_line(&face_flat, source_line))
            .map(|source_line| source_line.name)
            .collect();
        let expected: Vec<&str> = expected_match.into_iter().collect();
        check.condition(
            &format!("E_T=0 signed-minor coincidence {}", face_line.name),
            matches == expected,
        );
    }

    // The four finite corners combine a=+/-X2 with b=+/-X1.  They are the
    // intersections of the four active axial pole lines and all lie on the
    // reduced branch R=0 exactly.
    for &a_sign in &signs {
        for &b_sign in &signs {
            let corner_a = y.scale(a_sign);
            let corner_b = x.scale(b_sign);
            check.equal(
                &format!("E_T=0 reduced branch corner {a_sign},{b_sign}"),
                &r_affine_flat
                    .substitute(AA, &corner_a)
                    .substitute(BB, &corner_b),
                &zero,
            );
            check.equal(
                &format!("E_T=0 K0 branch corner {a_sign},{b_sign}"),
                &k0_flat.substitute(AA, &corner_a).substitute(BB, &corner_b),
                &zero,
            );
        }
    }

    let qg3_flat_b = x.add(&y).sub(&a);
    check.equal(
        "E_T=0 q_g3 reduced tangency",
        &r_affine_flat.substitute(BB, &qg3_flat_b),
        &x.add(&y).mul(&a.sub(&y).pow(2)),
    );
    check.equal(
        "E_T=0 q_g3 K0 contact order four",
        &k0_flat.substitute(BB, &qg3_flat_b),
        &x.add(&y).pow(2).mul(&a.sub(&y).pow(4)),
    );
    let qg12_flat_b = x.add(&y).add(&a).neg();
    check.equal(
        "E_T=0 q_g12 reduced tangency",
        &r_affine_flat.substitute(BB, &qg12_flat_b),
        &x.add(&y).mul(&a.add(&y).pow(2)),
    );

    let r_at_infinity = r_flat.substitute(S, &zero);
    check.equal(
        "E_T=0 horizontal-line infinity avoidance",
        &r_at_infinity.substitute(AA, &one).substitute(BB, &zero),
        &x,
    );
    check.equal(
        "E_T=0 vertical-line infinity avoidance",
        &r_at_infinity.substitute(AA, &zero).substitute(BB, &one),
        &y,
    );
    check.equal(
        "E_T=0 diagonal-line infinity avoidance",
        &r_at_infinity
            .substitute(AA, &one)
            .substitute(BB, &one.neg()),
        &x.add(&y),
    );
    let infinity_avoidance_localizer = x.mul(&y).mul(&x.add(&y));
    check.condition(
        "generic infinity avoidance localizer is nonzero",
        !infinity_avoidance_localizer.is_zero(),
    );
    check.equal(
        "generic Q slice obeys infinity avoidance",
        &specialize_xy(&infinity_avoidance_localizer),
        &Poly::constant(6),
    );

    // No source map to M_A is printed, and the exhaustive direct candidates
    // above do not produce Q.  Record absence, not an invented projection.
    let source_map_to_abstract_mark: Option<&'static str> = None;
    check.condition(
        "abstract M_A source map remains absent",
        source_map_to_abstract_mark.is_none(),
    );

    // Lower-dimensional simplex-domain boundaries are the six edge lengths.
    // On the residue they are a=0, b=0, E=0, X1=0, X2=0, X3=0.
    check.equal(
        "edge y12 restriction",
        &c.substitute(C, &total_energy.neg()),
        &total_energy.neg(),
    );
    check.equal("edge a retained", &a.substitute(C, &total_energy.neg()), &a);
    check.equal("edge b retained", &b.substitute(C, &total_energy.neg()), &b);

    check.condition(
        "source denominator census has ten members",
        denominators.len() == 10,
    );
    check.condition(
        "nonconstant nonresidue denominator census has eight infinity directions",
        denominator_directions.len() == 8,
    );
    check.equal(
        "fixed edge X1 retained",
        &x.substitute(C, &total_energy.neg()),
        &x,
    );
    check.equal(
        "fixed edge X2 retained",
        &y.substitute(C, &total_energy.neg()),
        &y,
    );
    check.equal(
        "fixed edge X3 retained",
        &z.substitute(C, &total_energy.neg()),
        &z,
    );

    println!("MARKED-RELATIVE-Q EXACT CERTIFICATE: DERIVABLE IDENTITIES PASS");
    println!("assertions={}", check.assertions);
    println!("CM normalization: D_CM=-2*K; q_G12=E+y12, so y12=-E and residue Jacobian=1");
    println!("K0=F+Ga*a^2+Gb*b^2+H");
    println!("F=X1^2*a^4-(X1^2+X2^2-X3^2)*a^2*b^2+X2^2*b^4");
    println!("Ga=-2*X1^2*(X2^2+E^2)+(X1^2+X2^2-X3^2)*(X1^2+E^2)");
    println!("Gb=(X1^2+X2^2-X3^2)*(X2^2+E^2)-2*X2^2*(X1^2+E^2)");
    println!("H=X3^2*((E^2-X2^2)*(E^2-X1^2)+E^2*X3^2), E=X1+X2+X3");
    println!("denominator restrictions: qG=E; qg1=b-X2-X3; qg2=a-X1-X3; qg3=a+b+X3; qg12=a+b+X1+X2; qg23=b-X1; qg31=a-X2; qG12=0; qG23=a+E; qG31=b+E");
    println!("face factors: H_ca=prod[a-E-X2,a-E+X2,a+E-X2,a+E+X2]");
    println!("face factors: H_cb=prod[b-E-X1,b-E+X1,b+E-X1,b+E+X1]");
    println!("face factors: H_ab=prod[a+b-X3,a+b+X3,a-b-X3,a-b+X3]; H_xyz=A*B");
    println!("edge-boundary factors on the residue: a, b, E, X1, X2, X3");
    println!(
        "face/branch collisions: every one of 16 signed face branches gives K|face=L^2 exactly"
    );
    println!(
        "branch collision: A=(X1-X2)^2-X3^2; B=(X1+X2)^2-X3^2; Disc_t(F)=16*X1^2*X2^2*(A*B)^2"
    );
    println!("source-mark/infinity branch factors: qg1,qg23,qG31 -> X1^2; qg2,qg31,qG23 -> X2^2; qg3,qg12 -> X3^2");
    println!("simplex-boundary/infinity branch factors: ca -> X2^2 (four); cb -> X1^2 (four); ab -> X3^2 (four); base -> A*B");
    println!("mark collision: M_A(u)=A*u^2-(A+B-E_T^2)*u+B has Res(M_A,M_A')=A*Q; reciprocal chart gives B*Q");
    println!("Q=4*A*B-(A+B-E_T^2)^2");
    println!("Q|X3=E_T-X1-X2=-16*X1^2*X2^2-8*X1*X2*E_T^2+8*(X1+X2)*E_T^3-5*E_T^4");
    println!("grades: gr1=0; gr2=-8*X1*X2");
    println!("FULL_EIGHT_LINES: qg1,qg2,qg3,qg12,qg23,qg31,qG23,qG31");
    println!("ACTIVE_FIVE_POLES: qg1,qg2,qg3,qg23,qg31 (qg23 and qg31 occur in separate summands; qG is constant on the residue)");
    println!("GENERIC_FACE_COINCIDENCES: ca--=qg2; cb--=qg1; ab--=qg3; other nine=none");
    println!(
        "Q_SLICE: X1=1,X2=2; Qs={q_slice}; Res(Qs,Qs')={q_slice_squarefree_resultant}=2^24*5*283"
    );
    for report in &finite_line_reports {
        println!("{report}");
    }
    for report in &boundary_line_reports {
        println!("{report}");
    }
    for report in &pair_reports {
        println!("{report}");
    }
    println!(
        "FINITE_PAIR_CENSUS: parallel={parallel_pairs}; nonparallel={nonparallel_pairs}; universal_reduced_branch={universal_branch_pairs}; Q-component rejections={q_component_rejections}"
    );
    println!("DIRECT_MARK_ELIMINATION: eight source lines + twelve signed face lines + every nonparallel source-line pair; no collision polynomial has Q as a component on the exact generic slice");
    println!("E_T_ZERO: Kbar0=R^2, R=X1*alpha^2+X2*beta^2-X1*X2*(X1+X2)*s^2");
    println!("E_T_ZERO_FULL_EIGHT: b+X1; a+X2; a+b-X1-X2; a+b+X1+X2; b-X1; a-X2; a; b");
    println!("E_T_ZERO_ACTIVE_FIVE: b+X1; a+X2; a+b-X1-X2; b-X1; a-X2");
    println!("E_T_ZERO_FACE_COINCIDENCES: ca--/ca+-=qg2, ca-+/ca++=qg31; cb--/cb+-=qg1, cb-+/cb++=qg23; ab--=qg3, ab-+=qg12, ab+-/ab++=none");
    println!("E_T_ZERO_CORNERS: (+X2,+X1)=qg31∩qg23; (+X2,-X1)=qg31∩qg1; (-X2,+X1)=qg2∩qg23; (-X2,-X1)=qg2∩qg1; all lie on R=0");
    println!("E_T_ZERO_TANGENCY: R|qg3=(X1+X2)*(a-X2)^2 and K0|qg3=(X1+X2)^2*(a-X2)^4");
    println!("E_T_ZERO_INFINITY: axial/diagonal direction values X1,X2,X1+X2; localize at X1*X2*(X1+X2)!=0");
    println!("UNRESOLVED_PROVENANCE (fail-closed classification): frozen source prints Q but neither P nor a denominator/simplex-boundary map to M_A; no geometric source mark is guessed");
}
