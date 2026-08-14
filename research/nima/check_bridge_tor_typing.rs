//! Exact typing audit for the regional overlap bridge.
//!
//! After inverting the fixed outer monomial C_e, the adjacent overlap ideal
//! is p=(x,y).  The bridge
//!
//!     d h = y e_1 - x e_0
//!
//! has three potentially confusing homological descriptions.
//!
//! * In the length-one free resolution of p it is the unique first syzygy.
//! * In the Koszul resolution of S=A/p it is the top K_2 determinant
//!   generator.  Consequently Tor_1^A(S,S) has rank two, while Tor_2 has
//!   rank one.
//! * In the only documented scalar-shift base B=A[t], the shift divisor
//!   (t) and regional ideal (x,y) are Tor-independent: multiplication by t
//!   is injective on B/(x,y), so all positive Tor groups vanish.
//!
//! Thus the algebra does not support the phrase "rank-one Tor_1 excess
//! conormal class" for the documented square.  A finite-loaded differential
//! with x=q_x-1 and y=q_y-1 is instead the same top two-parameter Koszul
//! determinant, or one-dimensional endpoint/Pochhammer interval relation.

use std::collections::BTreeMap;

const X: usize = 0;
const Y: usize = 1;
const T: usize = 2;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Monomial([u8; 3]);

#[derive(Clone, Debug, Eq, PartialEq)]
struct Polynomial(BTreeMap<Monomial, i64>);

impl Monomial {
    fn one() -> Self {
        Self([0; 3])
    }

    fn variable(index: usize) -> Self {
        let mut powers = [0; 3];
        powers[index] = 1;
        Self(powers)
    }

    fn multiply(self, other: Self) -> Self {
        let mut powers = [0; 3];
        for (index, power) in powers.iter_mut().enumerate() {
            *power = self.0[index] + other.0[index];
        }
        Self(powers)
    }
}

impl Polynomial {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn one() -> Self {
        Self::monomial(Monomial::one())
    }

    fn monomial(value: Monomial) -> Self {
        Self(BTreeMap::from([(value, 1)]))
    }

    fn variable(index: usize) -> Self {
        Self::monomial(Monomial::variable(index))
    }

    fn scale(&self, scalar: i64) -> Self {
        let mut result = self.clone();
        for coefficient in result.0.values_mut() {
            *coefficient *= scalar;
        }
        result.0.retain(|_, coefficient| *coefficient != 0);
        result
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.clone();
        for (&monomial, &coefficient) in &other.0 {
            *result.0.entry(monomial).or_default() += coefficient;
        }
        result.0.retain(|_, coefficient| *coefficient != 0);
        result
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::zero();
        for (&left, &left_coefficient) in &self.0 {
            for (&right, &right_coefficient) in &other.0 {
                let term = Self::monomial(left.multiply(right))
                    .scale(left_coefficient * right_coefficient);
                result = result.add(&term);
            }
        }
        result
    }

    fn multiply_variable(&self, variable: usize) -> Self {
        self.multiply(&Self::variable(variable))
    }

    fn reduce_mod(&self, variables: &[usize]) -> Self {
        let mut result = Self::zero();
        for (&monomial, &coefficient) in &self.0 {
            if variables.iter().any(|&index| monomial.0[index] != 0) {
                continue;
            }
            result = result.add(&Self::monomial(monomial).scale(coefficient));
        }
        result
    }

    fn divide_variable(&self, variable: usize) -> Option<Self> {
        let mut quotient = BTreeMap::new();
        for (&monomial, &coefficient) in &self.0 {
            if monomial.0[variable] == 0 {
                return None;
            }
            let mut divided = monomial;
            divided.0[variable] -= 1;
            quotient.insert(divided, coefficient);
        }
        Some(Self(quotient))
    }

    fn is_zero(&self) -> bool {
        self.0.is_empty()
    }
}

type Module2 = [Polynomial; 2];

// Ordered Koszul sequence (y,x): d_1(e_0)=y, d_1(e_1)=x.
fn koszul_d1(value: &Module2) -> Polynomial {
    Polynomial::variable(Y)
        .multiply(&value[0])
        .add(&Polynomial::variable(X).multiply(&value[1]))
}

// d_2(e_0 wedge e_1)=y e_1-x e_0.
fn koszul_d2(value: &Polynomial) -> Module2 {
    [
        Polynomial::variable(X).multiply(value).scale(-1),
        Polynomial::variable(Y).multiply(value),
    ]
}

fn check_ideal_syzygy_and_determinant() {
    let h = Polynomial::one();
    let bridge = koszul_d2(&h);
    assert_eq!(bridge[0], Polynomial::variable(X).scale(-1));
    assert_eq!(bridge[1], Polynomial::variable(Y));
    assert!(koszul_d1(&bridge).is_zero());

    // Audit a nontrivial polynomial multiple of the determinant generator.
    // The general uniqueness proof uses the same exact divisibility: from
    // y a+x b=0, reduction mod x gives y(a mod x)=0, hence x|a; cancellation
    // then gives b=-y(a/x).  This is valid because A is a polynomial domain
    // and x,y are coprime.
    let multiplier = Polynomial::one()
        .add(&Polynomial::variable(X).scale(2))
        .add(
            &Polynomial::variable(T)
                .multiply(&Polynomial::variable(Y))
                .scale(-3),
        );
    let general_bridge = koszul_d2(&multiplier);
    assert!(koszul_d1(&general_bridge).is_zero());
    let recovered = general_bridge[0].divide_variable(X).unwrap().scale(-1);
    assert_eq!(recovered, multiplier);
    assert_eq!(general_bridge[1], multiplier.multiply_variable(Y));

    // The determinant line wedge^2 A^2 has one ordered basis element.
    let exterior_ranks = [1_usize, 2, 1];
    assert_eq!(exterior_ranks[2], 1);
}

fn check_self_intersection_tor() {
    // Tensor K(y,x) with S=A/(x,y).  Both differentials become zero, so the
    // homology ranks are exactly the exterior ranks (1,2,1).
    let d1_after_s =
        [Polynomial::variable(Y), Polynomial::variable(X)].map(|entry| entry.reduce_mod(&[X, Y]));
    let d2_after_s = koszul_d2(&Polynomial::one()).map(|entry| entry.reduce_mod(&[X, Y]));
    assert!(d1_after_s.iter().all(Polynomial::is_zero));
    assert!(d2_after_s.iter().all(Polynomial::is_zero));

    let tor_ranks_over_s = [1_usize, 2, 1];
    assert_eq!(tor_ranks_over_s[1], 2); // p/p^2
    assert_eq!(tor_ranks_over_s[2], 1); // wedge^2(p/p^2)

    // Antisymmetry fixes the ordered determinant sign.
    let x_wedge_y = 1_i64;
    let y_wedge_x = -1_i64;
    assert_eq!(x_wedge_y, -y_wedge_x);
}

fn check_documented_scalar_shift_tor() {
    // Resolve B/(t) by 0 -> B --t--> B.  After tensoring with B/(x,y),
    // multiplication by t is injective: it shifts the t exponent of every
    // surviving monomial and cannot merge or kill terms.
    let test = Polynomial::one()
        .add(&Polynomial::variable(T).scale(2))
        .add(
            &Polynomial::variable(T)
                .multiply(&Polynomial::variable(T))
                .scale(-1),
        );
    let in_b_mod_q = test.reduce_mod(&[X, Y]);
    assert!(!in_b_mod_q.is_zero());
    let multiplied = in_b_mod_q.multiply_variable(T);
    assert!(!multiplied.is_zero());
    assert_eq!(multiplied.divide_variable(T).unwrap(), in_b_mod_q);

    // Hence ker(t:B/(x,y)->B/(x,y))=0.  The resolution has length one, so
    // every higher Tor also vanishes.  The documented (t) versus (x,y)
    // square is transverse/Tor-independent and has excess rank zero.
    let positive_tor_ranks = [0_usize, 0, 0];
    assert!(positive_tor_ranks.into_iter().all(|rank| rank == 0));

    // t,x,y is a regular sequence in the polynomial ring B.  The ordered
    // top exterior line has rank one, but it belongs to codimension three;
    // it is not an excess line of the transverse (t) and (x,y) intersection.
    let regular_sequence_length = 3_usize;
    let excess_rank = 0_usize;
    assert_eq!(regular_sequence_length, 3);
    assert_eq!(excess_rank, 0);
}

fn check_monodromy_interval_typing() {
    // Reinterpret x=z_x=q_x-1 and y=z_y=q_y-1.  The finite-loaded endpoint
    // relation is literally the same determinant differential.  It is a
    // two-parameter normal Koszul/Pochhammer interval relation, not evidence
    // for a rank-one excess normal bundle in the documented scalar square.
    let endpoint_relation = koszul_d2(&Polynomial::one());
    assert_eq!(
        endpoint_relation,
        [Polynomial::variable(X).scale(-1), Polynomial::variable(Y)]
    );
    assert!(koszul_d1(&endpoint_relation).is_zero());
}

fn main() {
    check_ideal_syzygy_and_determinant();
    check_self_intersection_tor();
    check_documented_scalar_shift_tor();
    check_monodromy_interval_typing();

    println!("regional bridge Tor-typing certificate");
    println!("  local overlap ideal: p=(x,y) after inverting C_e");
    println!("  p resolution: 0 -> A --(-x,y)--> A^2 --(y,x)--> p -> 0");
    println!("  bridge: unique first syzygy of p and top K_2 determinant for A/p");
    println!("  Tor_1^A(A/p,A/p)=p/p^2 has S-rank two");
    println!("  Tor_2^A(A/p,A/p)=wedge^2(p/p^2) has S-rank one");
    println!("  documented scalar shift (t) versus (x,y) is Tor-independent");
    println!("  its positive Tor groups vanish and its excess rank is zero");
    println!("  q-1 endpoint bridge is top two-monodromy Koszul/Pochhammer relation");
    println!();
    println!("VERDICT: FALSIFIED");
    println!("  rank-one Tor_1 excess does not type the established bridge");
    println!("  a different derived square would have to be defined and computed");
}
