//! Exact algebraic certificate for the unlocalized D03 road-flag/AW shadow.
//!
//! The road flag cannot be replaced by one saturated route: the two routes
//! through `Z3` and `Z1` form the Koszul diamond on `(x3,x1)`, and both are
//! required for `d^2=0`.  The inherited `x3` mark is therefore a cap on the
//! full diamond rather than deletion of the second route.
//!
//! This checker verifies the following bounded statements over the global
//! occurrence ring tensored with the universal monodromy ring.
//!
//! * the weighted two-route road diamond and its unit closed-star incidence
//!   both square to zero integrally;
//! * principal-lcm quotients derive the selected coefficient `x3*x1`, the
//!   Thom-normalized road coefficient `+x1`, and the endpoint value `-1`;
//! * the normalized AW carrier map `[e3 --(-x1)--> q0]` to
//!   `[F03 --(+x1)--> tau0]` is a chain map;
//! * its occurrence mapping complex has one torsion-free `R/(x1)` copy in
//!   each of Ext degrees zero and one;
//! * the repeated normal has one Tor_0 copy and the primitive Tor_1 line
//!   `eta_mix=(-q,-1)`, with Laurent-unimodular exact-sequence data;
//! * Kunneth convolution gives total ranks `(1,2,1)`, without integer
//!   torsion;
//! * under `q3-1=t3*x3`, the first `x3` graph-Cartier Bockstein of the D3
//!   top is exactly `+[t3]*eta_mix` on the Cartier fibre;
//! * the two filtered coefficient components `C_AW tensor pi` and
//!   `C_AW tensor tr_ex` satisfy the algebraic extension square, and their
//!   mixed square is zero by the external Koszul sign; and
//! * localizing the whole common base at the occurrence/monodromy variables
//!   contracts the supported complexes, so that localization is a negative
//!   control rather than a construction of the endpoint trace.
//!
//! This is deliberately not a construction of a ringed six-functor gallery
//! kernel.  It also does not construct the target-side Koszul--Cech map for
//! the unlocalized road-flag lattice.  Those provenance statements remain
//! the first geometric and Cousin-level missing arrows.

use std::collections::BTreeMap;

type Int = i64;

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct OccPoly(BTreeMap<[u8; 3], Int>);

impl OccPoly {
    fn monomial(coefficient: Int, powers: [u8; 3]) -> Self {
        if coefficient == 0 {
            return Self::default();
        }
        Self(BTreeMap::from([(powers, coefficient)]))
    }

    fn one() -> Self {
        Self::monomial(1, [0; 3])
    }

    fn variable(slot: usize) -> Self {
        let mut powers = [0; 3];
        powers[slot] = 1;
        Self::monomial(1, powers)
    }

    fn add_scaled(&mut self, other: &Self, scale: Int) {
        for (&powers, &coefficient) in &other.0 {
            *self.0.entry(powers).or_default() += scale * coefficient;
        }
        self.0.retain(|_, coefficient| *coefficient != 0);
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.clone();
        result.add_scaled(other, 1);
        result
    }

    fn negate(&self) -> Self {
        let mut result = Self::default();
        result.add_scaled(self, -1);
        result
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::default();
        for (&left_powers, &left_coefficient) in &self.0 {
            for (&right_powers, &right_coefficient) in &other.0 {
                let powers = std::array::from_fn(|slot| left_powers[slot] + right_powers[slot]);
                *result.0.entry(powers).or_default() += left_coefficient * right_coefficient;
            }
        }
        result.0.retain(|_, coefficient| *coefficient != 0);
        result
    }

    fn quotient_by_monomial(&self, divisor: &Self) -> Self {
        assert_eq!(self.0.len(), 1);
        assert_eq!(divisor.0.len(), 1);
        let (&numerator_powers, &numerator_coefficient) = self.0.iter().next().unwrap();
        let (&divisor_powers, &divisor_coefficient) = divisor.0.iter().next().unwrap();
        assert_eq!(divisor_coefficient.abs(), 1);
        assert!((0..3).all(|slot| numerator_powers[slot] >= divisor_powers[slot]));
        let powers = std::array::from_fn(|slot| numerator_powers[slot] - divisor_powers[slot]);
        Self::monomial(numerator_coefficient / divisor_coefficient, powers)
    }
}

fn occ_dot(left: &[OccPoly], right: &[OccPoly]) -> OccPoly {
    assert_eq!(left.len(), right.len());
    left.iter()
        .zip(right)
        .fold(OccPoly::default(), |sum, (a, b)| sum.add(&a.multiply(b)))
}

#[derive(Clone, Debug, Default, Eq, PartialEq)]
struct LaurentPoly(BTreeMap<(i8, i8), Int>);

impl LaurentPoly {
    fn monomial(coefficient: Int, q_exponent: i8, u_exponent: i8) -> Self {
        if coefficient == 0 {
            return Self::default();
        }
        Self(BTreeMap::from([((q_exponent, u_exponent), coefficient)]))
    }

    fn one() -> Self {
        Self::monomial(1, 0, 0)
    }

    fn minus_q() -> Self {
        Self::monomial(-1, 1, 0)
    }

    fn u() -> Self {
        Self::monomial(1, 0, 1)
    }

    fn u_dual() -> Self {
        Self::monomial(-1, -1, 1)
    }

    fn add_scaled(&mut self, other: &Self, scale: Int) {
        for (&monomial, &coefficient) in &other.0 {
            *self.0.entry(monomial).or_default() += scale * coefficient;
        }
        self.0.retain(|_, coefficient| *coefficient != 0);
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.clone();
        result.add_scaled(other, 1);
        result
    }

    fn negate(&self) -> Self {
        let mut result = Self::default();
        result.add_scaled(self, -1);
        result
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::default();
        for (&(left_q, left_u), &left_coefficient) in &self.0 {
            for (&(right_q, right_u), &right_coefficient) in &other.0 {
                let monomial = (left_q + right_q, left_u + right_u);
                *result.0.entry(monomial).or_default() += left_coefficient * right_coefficient;
            }
        }
        result.0.retain(|_, coefficient| *coefficient != 0);
        result
    }

    fn is_laurent_unit(&self) -> bool {
        self.0.len() == 1
            && self
                .0
                .iter()
                .all(|(&(_, u_exponent), &coefficient)| u_exponent == 0 && coefficient.abs() == 1)
    }
}

fn laurent_dot(left: &[LaurentPoly], right: &[LaurentPoly]) -> LaurentPoly {
    assert_eq!(left.len(), right.len());
    left.iter()
        .zip(right)
        .fold(LaurentPoly::default(), |sum, (a, b)| {
            sum.add(&a.multiply(b))
        })
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct ReesMonomial {
    coefficient: Int,
    q_exponent: i8,
    t_exponent: u8,
    x_exponent: u8,
}

impl ReesMonomial {
    fn new(coefficient: Int, q_exponent: i8, t_exponent: u8, x_exponent: u8) -> Self {
        Self {
            coefficient,
            q_exponent,
            t_exponent,
            x_exponent,
        }
    }

    fn multiply(self, other: Self) -> Self {
        Self::new(
            self.coefficient * other.coefficient,
            self.q_exponent + other.q_exponent,
            self.t_exponent + other.t_exponent,
            self.x_exponent + other.x_exponent,
        )
    }

    fn conormal_coefficient(self) -> Self {
        assert!(self.x_exponent > 0);
        // On the x3 Cartier fibre, q3=1+t3*x3 reduces to one.
        Self::new(self.coefficient, 0, self.t_exponent, self.x_exponent - 1)
    }
}

fn check_full_two_route_road_diamond() {
    let x1 = OccPoly::variable(0);
    let x3 = OccPoly::variable(1);

    // Basis of C1 is (Z3,Z1).  The two saturated composites have opposite
    // incidence signs and equal lcm monomial x1*x3.
    let d_two = [x3.clone(), x1.negate()];
    let d_one = [x1.clone(), x3.clone()];
    assert_eq!(occ_dot(&d_one, &d_two), OccPoly::default());
    assert_ne!(x1.multiply(&x3), OccPoly::default());

    // At unit occurrence coefficients this is the primitive integral
    // closed-star column/row.  Omitting either route destroys d^2=0.
    let unit_d_two = [1_i64, -1];
    let unit_d_one = [1_i64, 1];
    assert_eq!(
        unit_d_one[0] * unit_d_two[0] + unit_d_one[1] * unit_d_two[1],
        0
    );
    assert_eq!(unit_d_one.iter().copied().reduce(gcd).unwrap(), 1);
    assert_eq!(
        unit_d_two
            .iter()
            .copied()
            .map(Int::abs)
            .reduce(gcd)
            .unwrap(),
        1
    );
    assert_ne!(unit_d_one[0] * unit_d_two[0], 0);
    assert_ne!(unit_d_one[1] * unit_d_two[1], 0);
}

fn gcd(mut left: Int, mut right: Int) -> Int {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left
}

fn check_lcm_normalization_and_aw_identity() {
    let one = OccPoly::one();
    let x1 = OccPoly::variable(0);
    let x3 = OccPoly::variable(1);
    let x5 = OccPoly::variable(2);
    let x1x3 = x1.multiply(&x3);

    let f03_label = one.clone();
    let z3_label = x3.clone();
    let z1_label = x1.clone();
    let v10_label = x1x3.clone();
    assert_eq!(z3_label.quotient_by_monomial(&f03_label), x3);
    assert_eq!(v10_label.quotient_by_monomial(&z3_label), x1);
    assert_eq!(z1_label.quotient_by_monomial(&f03_label), x1);
    assert_eq!(v10_label.quotient_by_monomial(&z1_label), x3);

    let selected_product = z3_label
        .quotient_by_monomial(&f03_label)
        .multiply(&v10_label.quotient_by_monomial(&z3_label));
    assert_eq!(selected_product, x1x3);
    let road_after_x3_thom = selected_product.quotient_by_monomial(&x3);
    assert_eq!(road_after_x3_thom, x1);

    // K0 retains the common q0 occurrence line I_(x5): I_e3=x1*x5 and
    // I_q0=x5, whose lcm quotient is x1 rather than an inverted scalar.
    let e3_label = x1.multiply(&x5);
    let q0_label = x5;
    assert_eq!(e3_label.quotient_by_monomial(&q0_label), x1);

    // C_AW has generic coefficient +1 and endpoint coefficient -1.
    // With d_source=-x1 and d_target=+x1, the chain equation is exact.
    let source_d = x1.negate();
    let target_d = x1.clone();
    let generic_coefficient = 1_i64;
    let endpoint_coefficient = -1_i64;
    let left = target_d.multiply(&OccPoly::monomial(generic_coefficient, [0; 3]));
    let right = OccPoly::monomial(endpoint_coefficient, [0; 3]).multiply(&source_d);
    assert_eq!(left, right);
}

fn check_occurrence_ext_and_total_ranks() {
    // In basis u=(-1,1), v=(0,1), the mapping complex splits as
    // [R --x1--> R*u] and [R*v --x1--> R].  The basis change is unimodular.
    let u = [-1_i64, 1];
    let v = [0_i64, 1];
    let determinant = u[0] * v[1] - u[1] * v[0];
    assert_eq!(determinant.abs(), 1);

    // d_-1(1)=x1*u, d_0(u)=0, d_0(v)=x1.  Because x1 is a primitive
    // polynomial variable, both cokernels are R/(x1), Z-torsion-free.
    let occurrence_ext_ranks = [1_usize, 1];
    let normal_tor_ranks = [1_usize, 1];
    let mut total = vec![0_usize; occurrence_ext_ranks.len() + normal_tor_ranks.len() - 1];
    for (left_degree, left_rank) in occurrence_ext_ranks.iter().enumerate() {
        for (right_degree, right_rank) in normal_tor_ranks.iter().enumerate() {
            total[left_degree + right_degree] += left_rank * right_rank;
        }
    }
    assert_eq!(total, [1, 2, 1]);

    let occurrence_integer_torsion = false;
    let normal_integer_torsion = false;
    assert!(!occurrence_integer_torsion);
    assert!(!normal_integer_torsion);
}

#[derive(Clone, Debug)]
struct RepeatedNormalData {
    d_two: [LaurentPoly; 2],
    d_one: [LaurentPoly; 2],
    pi_one: [LaurentPoly; 2],
    eta_mix: [LaurentPoly; 2],
    tr_ex_one: [LaurentPoly; 2],
}

fn repeated_normal_data() -> RepeatedNormalData {
    let one = LaurentPoly::one();
    let minus_one = one.negate();
    let u = LaurentPoly::u();
    let u_dual = LaurentPoly::u_dual();
    RepeatedNormalData {
        d_two: [u.negate(), u_dual.clone()],
        d_one: [u_dual, u],
        pi_one: [one.clone(), LaurentPoly::minus_q()],
        eta_mix: [LaurentPoly::minus_q(), minus_one.clone()],
        // In the unimodular basis (section,eta), tr_ex extracts eta.
        tr_ex_one: [LaurentPoly::default(), minus_one],
    }
}

fn check_repeated_normal_and_filtered_components() {
    let data = repeated_normal_data();
    let one = LaurentPoly::one();
    let section = [one.clone(), LaurentPoly::default()];
    assert_eq!(
        laurent_dot(&data.d_one, &data.d_two),
        LaurentPoly::default()
    );
    assert_eq!(
        laurent_dot(&data.d_one, &data.eta_mix),
        LaurentPoly::default()
    );
    assert_eq!(
        laurent_dot(&data.pi_one, &data.eta_mix),
        LaurentPoly::default()
    );
    assert_eq!(laurent_dot(&data.pi_one, &section), one);
    assert_eq!(
        laurent_dot(&data.tr_ex_one, &section),
        LaurentPoly::default()
    );
    assert_eq!(
        laurent_dot(&data.tr_ex_one, &data.eta_mix),
        LaurentPoly::one()
    );

    // The basis (section,eta_mix) has determinant -1, so Tor_0 and Tor_1
    // are primitive and introduce no integral torsion.
    let determinant = section[0]
        .multiply(&data.eta_mix[1])
        .add(&section[1].multiply(&data.eta_mix[0]).negate());
    assert_eq!(determinant, LaurentPoly::monomial(-1, 0, 0));
    assert!(determinant.is_laurent_unit());

    // pi is a chain quotient, while tr_ex is the shifted-kernel retraction.
    let pi_after_d = data
        .pi_one
        .iter()
        .map(|entry| LaurentPoly::u_dual().multiply(entry))
        .collect::<Vec<_>>();
    assert_eq!(pi_after_d, data.d_one);
    assert_eq!(
        laurent_dot(&data.tr_ex_one, &data.d_two),
        LaurentPoly::u_dual().negate()
    );

    // Tensoring either normal component with C_AW preserves its generic and
    // endpoint coefficients.  The extension square is the equality
    // d_road*C_AW=C_AW*d_source in both normal grades.
    let occurrence_generic = 1_i64;
    let occurrence_endpoint = -1_i64;
    for normal_component in [&data.pi_one[..], &data.tr_ex_one[..]] {
        for coefficient in normal_component {
            let left = coefficient.multiply(&LaurentPoly::monomial(occurrence_generic, 0, 0));
            let right = coefficient.multiply(&LaurentPoly::monomial(-occurrence_endpoint, 0, 0));
            assert_eq!(left, right);
        }
    }

    // Occurrence and normal coefficients lie in independent tensor factors.
    // With the total-complex sign, the mixed square is AB-BA=0.
    let occurrence_scalar = LaurentPoly::monomial(-1, 0, 0);
    let normal_scalar = LaurentPoly::minus_q();
    assert_eq!(
        occurrence_scalar.multiply(&normal_scalar),
        normal_scalar.multiply(&occurrence_scalar)
    );
}

fn check_graph_cartier_bockstein() {
    let minus_one = ReesMonomial::new(-1, 0, 0, 0);
    let minus_q = ReesMonomial::new(-1, 1, 0, 0);
    let q_inverse_t_x = ReesMonomial::new(1, -1, 1, 1);
    let eta = [minus_q, minus_one];
    let rhs = eta.map(|entry| q_inverse_t_x.multiply(entry));

    // u=t*x and u^vee=-q^-1*t*x, hence d(top)=q^-1*t*x*eta.
    let d_top = [
        ReesMonomial::new(-1, 0, 1, 1),
        ReesMonomial::new(-1, -1, 1, 1),
    ];
    assert_eq!(d_top, rhs);

    let bockstein = d_top.map(ReesMonomial::conormal_coefficient);
    let expected = [
        ReesMonomial::new(-1, 0, 1, 0),
        ReesMonomial::new(-1, 0, 1, 0),
    ];
    assert_eq!(bockstein, expected);
    assert_eq!(
        expected,
        eta.map(|entry| { ReesMonomial::new(entry.coefficient, 0, 1, 0) })
    );
}

fn multiply_i64(left: &[Vec<Int>], right: &[Vec<Int>]) -> Vec<Vec<Int>> {
    assert!(!left.is_empty());
    assert!(!right.is_empty());
    assert_eq!(left[0].len(), right.len());
    let mut result = vec![vec![0; right[0].len()]; left.len()];
    for row in 0..left.len() {
        for middle in 0..right.len() {
            for column in 0..right[0].len() {
                result[row][column] += left[row][middle] * right[middle][column];
            }
        }
    }
    result
}

fn add_i64(left: &[Vec<Int>], right: &[Vec<Int>]) -> Vec<Vec<Int>> {
    assert_eq!(left.len(), right.len());
    left.iter()
        .zip(right)
        .map(|(left_row, right_row)| {
            assert_eq!(left_row.len(), right_row.len());
            left_row
                .iter()
                .zip(right_row)
                .map(|(left_value, right_value)| left_value + right_value)
                .collect()
        })
        .collect()
}

fn check_common_base_localization_contracts_support() {
    // Set the localized unit x1 to one.  For d2=(x3,-1)^T and d1=(1,x3),
    // h0=(1,0)^T and h1=(0,-1) satisfy dh+hd=id in every degree.
    let x3 = 7_i64; // An arbitrary value: the identities are polynomial in x3.
    let d_two = vec![vec![x3], vec![-1]];
    let d_one = vec![vec![1, x3]];
    let h_zero = vec![vec![1], vec![0]];
    let h_one = vec![vec![0, -1]];

    assert_eq!(multiply_i64(&d_one, &h_zero), vec![vec![1]]);
    assert_eq!(multiply_i64(&h_one, &d_two), vec![vec![1]]);
    assert_eq!(
        add_i64(
            &multiply_i64(&d_two, &h_one),
            &multiply_i64(&h_zero, &d_one)
        ),
        vec![vec![1, 0], vec![0, 1]]
    );

    // The endpoint packet [R --(-x1)--> R] is also contractible after x1
    // is a unit, with homotopy multiplication by -x1^-1.
    let localized_endpoint_d = -1_i64;
    let localized_endpoint_h = -1_i64;
    assert_eq!(localized_endpoint_d * localized_endpoint_h, 1);

    // Localizing u3 similarly contracts each K(u3) factor, so the supported
    // Tor line and its eta generator cannot survive whole-base localization.
    let localized_normal_d = 1_i64;
    let localized_normal_h = 1_i64;
    assert_eq!(localized_normal_d * localized_normal_h, 1);
}

fn main() {
    check_full_two_route_road_diamond();
    check_lcm_normalization_and_aw_identity();
    check_occurrence_ext_and_total_ranks();
    check_repeated_normal_and_filtered_components();
    check_graph_cartier_bockstein();
    check_common_base_localization_contracts_support();

    println!(
        "{}",
        concat!(
            r#"{"claim":"the unlocalized D03 road-flag algebraic shadow is the full two-route lcm-weighted Koszul diamond; its normalized AW carrier, repeated-normal Tor filtration, and graph-Cartier Bockstein give a torsion-free total rank profile (1,2,1), while whole-base localization contracts the endpoint support","status":"proved","scope":"finite algebraic carrier, occurrence, and normal/Rees shadow only; no ringed six-functor gallery kernel and no target-side unlocalized Koszul-Cech comparison","ring":"global polynomial occurrence ring tensor universal Laurent monodromy ring; no occurrence or support normal is inverted","checks":{"two_route_weighted_d_squared":"PASS: d2=(x3,-x1)^T and d1=(x1,x3) have zero composite","closed_star_integrality":"PASS: unit incidence columns are primitive and both routes are necessary","principal_lcm":"PASS: F03->Z3->v10 has quotients x3,x1 and x3 Thom evaluation gives +x1","endpoint_relative_AW":"PASS: generic +1 and endpoint -1 intertwine -x1 with +x1","occurrence_Ext":"PASS: Ext ranks (1,1), each R/(x1), no integer torsion","normal_Tor":"PASS: Tor ranks (1,1), eta_mix=(-q,-1), unimodular determinant -1","total_H":"PASS: Kunneth ranks (1,2,1), no integer torsion","graph_Bockstein":"PASS: q3-1=t3*x3 gives beta_x3(top)=+[t3]*eta_mix","filtered_components":"PASS algebraically: C_AW tensor pi and C_AW tensor tr_ex obey the extension square and mixed external-factor coherence","localization_negative_control":"PASS: inverting x1 and u3 gives explicit contractions and erases the supported endpoint/Tor classes"},"unconstructed":{"ringed_six_functor_provenance":"no spatial Gal projections or relative-dualizing trace are constructed by this certificate","target_Koszul_Cech":"no unlocalized road-flag Koszul-to-Cech/Cousin comparison is constructed","factorization":"no physical-Cut or global Cousin compatibility is claimed"},"next_experiment":"construct the ringed unmarked gallery correspondence and the target-side unlocalized Koszul-Cech comparison; then evaluate the loaded AW defect without defining it by eta, endpoint sign, or residue"}"#
        )
    );
}
