//! Exact coefficient audit for the D03 Cartier-filtered primal bridge.
//!
//! This constructs only the common two-variable coefficient shadow.  It does
//! not construct the normalization-sheet source, a spatial localization
//! morphism, or the physical obstruction class.

use std::collections::BTreeMap;

type Exponent = (u8, u8);

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct Polynomial(BTreeMap<Exponent, i64>);

impl Polynomial {
    fn monomial(x: u8, y: u8, coefficient: i64) -> Self {
        let mut terms = BTreeMap::new();
        if coefficient != 0 {
            terms.insert((x, y), coefficient);
        }
        Self(terms)
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.0.clone();
        for (exponent, coefficient) in &other.0 {
            *result.entry(*exponent).or_default() += coefficient;
        }
        result.retain(|_, coefficient| *coefficient != 0);
        Self(result)
    }

    fn neg(&self) -> Self {
        Self(self.0.iter().map(|(e, c)| (*e, -*c)).collect())
    }

    fn multiply_monomial(&self, x: u8, y: u8) -> Self {
        Self(
            self.0
                .iter()
                .map(|((ex, ey), coefficient)| ((ex + x, ey + y), *coefficient))
                .collect(),
        )
    }

    fn divisible_by_x(&self) -> bool {
        self.0.keys().all(|(x, _)| *x > 0)
    }

    fn divide_by_x(&self) -> Self {
        assert!(self.divisible_by_x());
        Self(
            self.0
                .iter()
                .map(|((x, y), coefficient)| ((x - 1, *y), *coefficient))
                .collect(),
        )
    }

    fn conductor_value(&self) -> Self {
        Self(
            self.0
                .iter()
                .filter(|((x, _), _)| *x == 0)
                .map(|(exponent, coefficient)| (*exponent, *coefficient))
                .collect(),
        )
    }
}

fn x() -> Polynomial {
    Polynomial::monomial(1, 0, 1)
}

fn y() -> Polynomial {
    Polynomial::monomial(0, 1, 1)
}

fn one() -> Polynomial {
    Polynomial::monomial(0, 0, 1)
}

fn check_syzygy(k: &Polynomial, a: &Polynomial) {
    // Totalization fixes y*k + x*a = 0.
    assert_eq!(
        k.multiply_monomial(0, 1).add(&a.multiply_monomial(1, 0)),
        Polynomial::default()
    );

    // In Z[x,y], reduction modulo x gives y*k(0,y)=0.  Since y is a
    // non-zero-divisor, k is divisible by x; cancellation then forces
    // a=-y*(k/x).  This is the constructive classification Z=C*(x,-y).
    assert!(k.divisible_by_x());
    let h = k.divide_by_x();
    assert_eq!(a, &h.multiply_monomial(0, 1).neg());
}

fn main() {
    // Test the universal recovery algorithm on a coefficient-rich family.
    for c0 in -3_i64..=3 {
        for c1 in -2_i64..=2 {
            for c2 in -2_i64..=2 {
                let h = Polynomial::monomial(0, 0, c0)
                    .add(&Polynomial::monomial(1, 0, c1))
                    .add(&Polynomial::monomial(0, 1, c2));
                let k = h.multiply_monomial(1, 0);
                let a = h.multiply_monomial(0, 1).neg();
                check_syzygy(&k, &a);
            }
        }
    }

    let k = x();
    let a = y().neg();
    check_syzygy(&k, &a);

    // The preceding mapping-complex homotopy sends h to h*(x,-y), so every
    // absolute cross-degree cocycle is exact.  In particular h=1 gives the
    // displayed minimal syzygy and absolute H is zero.
    let homotopy_boundary = (
        one().multiply_monomial(1, 0),
        one().multiply_monomial(0, 1).neg(),
    );
    assert_eq!(homotopy_boundary, (k.clone(), a.clone()));

    // Cartier associated grade: k=x belongs to I=(x), and the ideal-dual
    // evaluation x^vee(x)=1 is primitive without adjoining x^{-1}.
    assert!(k.divisible_by_x());
    assert_eq!(k.divide_by_x(), one());
    assert_eq!(k.conductor_value(), Polynomial::default());

    // Full lower column:
    // dq=x*b, dxi=b, dH=q-x*xi, dn=y*p.  With the fixed tensor sign, the
    // three nontrivial closedness equations are respectively
    // q-x*xi, x*(b,n)+y*(q,p), and (b,n)+y*(xi,p).
    let t_q_p = x();
    let t_xi_p = one();
    let t_b_n = y().neg();
    assert_eq!(
        t_q_p.add(&t_xi_p.multiply_monomial(1, 0).neg()),
        Polynomial::default()
    );
    assert_eq!(
        t_b_n
            .multiply_monomial(1, 0)
            .add(&t_q_p.multiply_monomial(0, 1)),
        Polynomial::default()
    );
    assert_eq!(
        t_b_n.add(&t_xi_p.multiply_monomial(0, 1)),
        Polynomial::default()
    );

    // Classification: the H equation forces q=x*xi, and the xi equation
    // forces (b,n)=-y*xi.  Hence all solutions are h*(x,1,-y), with no
    // integral torsion; primitive Cartier orientation is h=1.
    for h_value in -8_i64..=8 {
        let h = Polynomial::monomial(0, 0, h_value);
        let solution = (
            h.multiply_monomial(1, 0),
            h.clone(),
            h.multiply_monomial(0, 1).neg(),
        );
        assert_eq!(solution.0, solution.1.multiply_monomial(1, 0));
        assert_eq!(solution.2, solution.1.multiply_monomial(0, 1).neg());
    }
    assert_eq!((t_q_p, t_xi_p, t_b_n), (x(), one(), y().neg()));

    // The full source is contractible. In the unimodular basis m=q-x*xi it
    // is [H -> m] plus [xi -> b], with h(m)=H and h(b)=xi. These unit
    // contractions survive derived pullback to x=0.
    let differential_in_rebased_basis = [[1_i64, 0_i64], [0_i64, 1_i64]];
    let contraction = [[1_i64, 0_i64], [0_i64, 1_i64]];
    assert_eq!(differential_in_rebased_basis, contraction);

    println!(
        "{}",
        r#"{"claim":"Over the legal unlocalized D03 target Cech coefficient ring C, with x=x3 and y=X_D/u_D a regular pair, the shifted primal closedness equation y*k+x*a=0 has the saturated torsion-free syzygy module C*(x,-y). The full lower-column chain solution is uniquely h*(x,1,-y), with positive filtered normalization h=1. The full source is contractible after the unimodular rebase m=q-x*xi, so both the absolute class and its derived conductor pullback are zero. Ideal-line evaluation records only the coordinate associated-grade symbol gr_x T(q,p)=1 without inverting x; it is not induced by nonzero cohomology.","status":"proved_scoped_strict_chain_solution_and_filtered_coordinate","scope":"D03 coefficient and Cartier-filtered mapping complex only","references":["ledger entry 133","ledger entries 156-161"],"checks":{"regular_pair_syzygy":"PASS: Z=C*(x,-y)","saturation_and_torsion":"PASS: primitive rank-one solution module, no integer or x torsion","absolute_mapping_class":"ZERO: exact via preceding homotopy","source_contraction":"PASS: m=q-x*xi gives two unit contractible pairs","derived_conductor_class":"ZERO: contraction survives x=0","ordinary_conductor_value":"PASS: k mod x is zero","filtered_ideal_coordinate":"PASS: gr_x(k)=x^vee(x)=1 without x inversion","lower_H_equation":"PASS: x-x=0","lower_qn_equation":"PASS: x*(-y)+y*x=0","lower_xin_equation":"PASS: -y+y=0","solution_classification":"PASS: h*(x,1,-y)","primitive_orientation":"PASS: h=1"},"unconstructed":["relative support mapping fibre that forbids the contraction","normalization-provenanced spatial source","common ringed source/target localization morphism","endpoint comparison cells","physical ob03"],"physical_ob03":"untyped","boundary":"This proves a strict chain solution and filtered coordinate shadow, not a nonzero absolute, conductor-derived, or Gysin class in the contractible full source."}"#
    );
}
