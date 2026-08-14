//! Exact Ward-quotient audit for one- and two-edge physical closure.
//!
//! This checker separates three facts:
//! 1. on-shell null momentum alone does not make projector sewing independent
//!    of its reference vector;
//! 2. the aligned Ward identities make the one-edge result equal to the
//!    metric contraction plus the two scalar longitudinal coefficients;
//! 3. two disjoint projector contractions commute even when their nested
//!    longitudinal term is nonzero.

use std::fmt;

type Int = i128;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Rat {
    numerator: Int,
    denominator: Int,
}

impl Rat {
    fn new(mut numerator: Int, mut denominator: Int) -> Self {
        assert_ne!(denominator, 0);
        if denominator < 0 {
            numerator = -numerator;
            denominator = -denominator;
        }
        let divisor = gcd(numerator.abs(), denominator);
        Self {
            numerator: numerator / divisor,
            denominator: denominator / divisor,
        }
    }

    fn integer(value: Int) -> Self {
        Self::new(value, 1)
    }

    fn add(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )
    }

    fn multiply(self, other: Self) -> Self {
        Self::new(
            self.numerator * other.numerator,
            self.denominator * other.denominator,
        )
    }
}

impl fmt::Display for Rat {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        if self.denominator == 1 {
            write!(formatter, "{}", self.numerator)
        } else {
            write!(formatter, "{}/{}", self.numerator, self.denominator)
        }
    }
}

fn gcd(mut first: Int, mut second: Int) -> Int {
    while second != 0 {
        let remainder = first % second;
        first = second;
        second = remainder;
    }
    first.max(1)
}

#[derive(Clone, Copy, Debug)]
struct Vector([Int; 4]);

fn dot(first: Vector, second: Vector) -> Int {
    first.0[0] * second.0[0]
        - first.0[1] * second.0[1]
        - first.0[2] * second.0[2]
        - first.0[3] * second.0[3]
}

/// Contraction of Pi(p;q) with the decomposable tensor a tensor b.
fn projector_outer(p: Vector, q: Vector, a: Vector, b: Vector) -> Rat {
    let metric = Rat::integer(-dot(a, b));
    let longitudinal = Rat::new(dot(p, a) * dot(q, b) + dot(q, a) * dot(p, b), dot(p, q));
    metric.add(longitudinal)
}

fn metric_outer(a: Vector, b: Vector) -> Rat {
    Rat::integer(-dot(a, b))
}

fn longitudinal_outer(p: Vector, q: Vector, a: Vector, b: Vector) -> Rat {
    Rat::new(dot(p, a) * dot(q, b) + dot(q, a) * dot(p, b), dot(p, q))
}

fn main() {
    let p = Vector([1, 0, 0, 1]);
    let q_opposite = Vector([1, 0, 0, -1]);
    let q_tilted = Vector([1, 1, 0, 0]);
    let r = Vector([1, 0, 0, 0]);

    assert_eq!(dot(p, p), 0);
    assert_eq!(dot(q_opposite, q_opposite), 0);
    assert_eq!(dot(q_tilted, q_tilted), 0);
    assert_ne!(dot(p, q_opposite), 0);
    assert_ne!(dot(p, q_tilted), 0);

    // On-shellness alone is insufficient: r tensor r violates the aligned
    // Ward condition and has reference-dependent physical sewing.
    let bad_opposite = projector_outer(p, q_opposite, r, r);
    let bad_tilted = projector_outer(p, q_tilted, r, r);
    assert_eq!(bad_opposite, Rat::integer(0));
    assert_eq!(bad_tilted, Rat::integer(1));

    // Even the double contraction p.B.p = 0 is not enough to imply aligned
    // Ward identities.  For B = r tensor t, p.B.p vanishes because p.t=0,
    // while p.B=(p.r)t is not proportional to p.
    let t = Vector([0, 1, 0, 0]);
    assert_eq!(dot(p, t), 0);
    let double_ward_opposite = projector_outer(p, q_opposite, r, t);
    let double_ward_tilted = projector_outer(p, q_tilted, r, t);
    assert_eq!(dot(p, r) * dot(p, t), 0);
    assert_eq!(double_ward_opposite, Rat::integer(0));
    assert_eq!(double_ward_tilted, Rat::integer(-1));

    // B = r tensor p + p tensor r + t tensor t obeys
    // p.B = (p.r) p and B.p = (p.r) p.  Hence the projector result is
    // -tr(B) + N + N', independently of q.
    let sew_aligned = |q| {
        projector_outer(p, q, r, p)
            .add(projector_outer(p, q, p, r))
            .add(projector_outer(p, q, t, t))
    };
    let naive_metric = metric_outer(r, p)
        .add(metric_outer(p, r))
        .add(metric_outer(t, t));
    let ward_coefficients = Rat::integer(dot(p, r) + dot(p, r));
    let ward_formula = naive_metric.add(ward_coefficients);
    assert_eq!(sew_aligned(q_opposite), Rat::integer(1));
    assert_eq!(sew_aligned(q_tilted), Rat::integer(1));
    assert_eq!(ward_formula, Rat::integer(1));

    // A two-edge decomposable tensor makes the interchange law transparent.
    // The second null pair is independent of the first one.
    let k = Vector([1, 0, 1, 0]);
    let h = Vector([1, 0, -1, 0]);
    assert_eq!(dot(k, k), 0);
    assert_eq!(dot(h, h), 0);
    assert_ne!(dot(k, h), 0);

    let first_full = projector_outer(p, q_opposite, r, r);
    let second_full = projector_outer(k, h, r, r);
    let close_first_then_second = first_full.multiply(second_full);
    let close_second_then_first = second_full.multiply(first_full);
    assert_eq!(close_first_then_second, close_second_then_first);

    // Coherence does not require the nested longitudinal contribution to
    // vanish.  Here it is exactly one, and cancels against the mixed pieces.
    let first_metric = metric_outer(r, r);
    let second_metric = metric_outer(r, r);
    let first_longitudinal = longitudinal_outer(p, q_opposite, r, r);
    let second_longitudinal = longitudinal_outer(k, h, r, r);
    let nested = first_longitudinal.multiply(second_longitudinal);
    assert_eq!(nested, Rat::integer(1));
    let expanded = first_metric
        .multiply(second_metric)
        .add(first_longitudinal.multiply(second_metric))
        .add(first_metric.multiply(second_longitudinal))
        .add(nested);
    assert_eq!(expanded, close_first_then_second);

    // The pure-gauge second pair shows why intermediate representatives must
    // remain quotient-valued.  Closing the first pair depends on q, but the
    // final double closure is zero because Pi(k;h) annihilates k tensor k.
    let second_pure_gauge = projector_outer(k, h, k, k);
    assert_eq!(second_pure_gauge, Rat::integer(0));
    assert_eq!(bad_opposite.multiply(second_pure_gauge), Rat::integer(0));
    assert_eq!(bad_tilted.multiply(second_pure_gauge), Rat::integer(0));

    println!("One-edge Ward-quotient closure audit");
    println!("====================================");
    println!("  unaligned one-edge sewing for q_opposite: {bad_opposite}");
    println!("  unaligned one-edge sewing for q_tilted:   {bad_tilted}");
    println!("  p.B.p=0 but unaligned, q_opposite:        {double_ward_opposite}");
    println!("  p.B.p=0 but unaligned, q_tilted:          {double_ward_tilted}");
    println!("  aligned Ward formula, both references:    {ward_formula}");
    println!("  two-edge nested longitudinal term:        {nested}");
    println!("  two closure orders:                       {close_first_then_second}");
    println!();
    println!("VERDICT");
    println!("  null on-shell momentum alone does not imply a one-edge closure lemma");
    println!("  aligned Ward identities factor out all reference dependence");
    println!("  disjoint physical closures commute with a nonzero nested term");
    println!("  quotient-valued intermediates are required for closure induction");
}
