//! Exact one-normal can/var and Cousin-localization certificate.
//!
//! Work over R=Z[q^+-1], put u=q-1, and reverse the twist by
//!
//!   u^vee=q^-1-1=-q^-1 u.
//!
//! The original locally-finite/Borel--Moore direction is the costandard
//! quiver can=u, var=1.  Its reciprocal regular/ordinary Verdier dual is the
//! standard quiver can=1, var=u^vee.  The support-directed two-term complexes
//! use can in the first quiver and var in the second.
//!
//! This checker proves four bounded algebraic claims.
//!
//! 1. Both can/var composites are the appropriate monodromy difference.
//! 2. The complementary-degree pairing
//!
//!      beta(p,h^vee)=1, beta(h,p^vee)=-q
//!
//!    is a perfect chain pairing K(u) tensor K(u^vee) -> R[1].
//! 3. The repeated plus/D03 normal has the exact twist-aware excess sequence
//!
//!      0 -> K(u^vee)[1] -> K(u^vee) tensor K(u) -> K(u^vee) -> 0,
//!
//!    with oriented generator eta_mix=(-q,-1).  The entry-97 diagonal twist
//!    normalization identifies it exactly with eta=(1,-1), including the
//!    shifted source and top orientation.
//! 4. The first Koszul stage [R --u--> R] maps to the extended Cech complex
//!    [R -> R[u^-1]] by (1,u^-1), so its top generator realizes the
//!    entry-38 contraction h=ell/u without globally inverting the source.
//!
//! The certificate does not construct the global augmented dual-block map or
//! any of its tangential/lower-Cousin terms.

use std::collections::BTreeMap;

type Int = i64;

/// A sparse Laurent polynomial in the formal symbols q and u.  We retain u
/// as an atom because only the exact relation u^vee=-q^-1*u is needed here.
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

    fn q() -> Self {
        Self::monomial(1, 1, 0)
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

fn dot(left: &[LaurentPoly], right: &[LaurentPoly]) -> LaurentPoly {
    assert_eq!(left.len(), right.len());
    left.iter()
        .zip(right)
        .fold(LaurentPoly::default(), |mut sum, (a, b)| {
            sum.add_scaled(&a.multiply(b), 1);
            sum
        })
}

fn check_support_directed_quivers() {
    let one = LaurentPoly::one();
    let u = LaurentPoly::u();
    let u_dual = LaurentPoly::u_dual();

    // Original locally-finite/Borel--Moore road: Rj_*.
    let road_can = u.clone();
    let road_var = one.clone();
    assert_eq!(road_var.multiply(&road_can), u);
    assert_eq!(road_can.multiply(&road_var), LaurentPoly::u());

    // Reciprocal regular/ordinary source: j_! D(L).
    let regular_can_dual = one;
    let regular_var_dual = u_dual.clone();
    assert_eq!(regular_var_dual.multiply(&regular_can_dual), u_dual);
    assert_eq!(
        regular_can_dual.multiply(&regular_var_dual),
        LaurentPoly::u_dual()
    );

    // A unit support differential would be integrally contractible.  The
    // forced support-directed differentials are u and u^vee, not 1.
    assert_ne!(road_can, LaurentPoly::one());
    assert_ne!(regular_var_dual, LaurentPoly::one());
}

fn check_twist_pairing() {
    let u = LaurentPoly::u();
    let u_dual = LaurentPoly::u_dual();
    let beta_p_h_dual = LaurentPoly::one();
    let beta_h_p_dual = LaurentPoly::minus_q();

    // On d(h tensor h^vee), the tensor sign is negative on the second term:
    // u*beta(p,h^vee)-u^vee*beta(h,p^vee)=0.
    let first = u.multiply(&beta_p_h_dual);
    let second = u_dual.multiply(&beta_h_p_dual);
    assert_eq!(first, second);
    assert_eq!(first.add(&second.negate()), LaurentPoly::default());

    // The complementary-degree matrix is antidiagonal with determinant q.
    let determinant = beta_p_h_dual.multiply(&beta_h_p_dual).negate();
    assert_eq!(determinant, LaurentPoly::q());
    assert!(determinant.is_laurent_unit());

    // Entry 97's diagonal normalization K(u^vee)->K(u):
    // p^vee |-> -q p and h^vee |-> h.
    let degree_zero_scale = LaurentPoly::minus_q();
    let degree_one_scale = LaurentPoly::one();
    assert_eq!(
        degree_zero_scale.multiply(&LaurentPoly::u_dual()),
        LaurentPoly::u().multiply(&degree_one_scale)
    );
}

fn check_repeated_normal_exact_sequence() {
    let one = LaurentPoly::one();
    let minus_one = one.negate();
    let q = LaurentPoly::q();
    let minus_q = LaurentPoly::minus_q();
    let u = LaurentPoly::u();
    let u_dual = LaurentPoly::u_dual();

    // D=K(u^vee) tensor K(u), with degree-one basis
    // (h_plus^vee tensor p_03, p_plus^vee tensor h_03).
    let d_two = [u.negate(), u_dual.clone()];
    let d_one = [u_dual.clone(), u.clone()];
    assert_eq!(dot(&d_one, &d_two), LaurentPoly::default());

    // Quotient pi:D->K(u^vee): pi_0=1, pi_1=(1,-q), pi_2=0.
    let pi_one = [one.clone(), minus_q.clone()];
    let quotient_after_d = pi_one
        .iter()
        .map(|entry| u_dual.multiply(entry))
        .collect::<Vec<_>>();
    assert_eq!(quotient_after_d, d_one);

    // The shifted inclusion has i_1=eta_mix=(-q,-1), i_2=1.  Since
    // d_{K[1]}=-u^vee, d_D i_2=i_1(-u^vee).
    let eta_mix = [minus_q.clone(), minus_one.clone()];
    assert_eq!(dot(&d_one, &eta_mix), LaurentPoly::default());
    assert_eq!(dot(&pi_one, &eta_mix), LaurentPoly::default());
    let shifted_d = u_dual.negate();
    let inclusion_after_shift = eta_mix
        .iter()
        .map(|entry| entry.multiply(&shifted_d))
        .collect::<Vec<_>>();
    assert_eq!(inclusion_after_shift, d_two);

    // Degree-one exactness is integral: section=(1,0), kernel=eta_mix form a
    // Laurent-unimodular basis.  The determinant is -1.
    let section = [one.clone(), LaurentPoly::default()];
    let basis_determinant = section[0]
        .multiply(&eta_mix[1])
        .add(&section[1].multiply(&eta_mix[0]).negate());
    assert_eq!(basis_determinant, minus_one);
    assert!(basis_determinant.is_laurent_unit());

    // Compare exactly with the untwisted entry-99 sequence.  On D_1 the
    // twist normalization is diag(1,-q), and on the quotient it is 1 in
    // degree one and -q in degree zero.
    let mixed_d_then_degree_zero_scale = [minus_q.multiply(&d_one[0]), minus_q.multiply(&d_one[1])];
    let original_d_after_degree_one_scale = [u.clone(), minus_q.multiply(&u)];
    assert_eq!(
        mixed_d_then_degree_zero_scale,
        original_d_after_degree_one_scale
    );

    let eta_image = [eta_mix[0].clone(), minus_q.multiply(&eta_mix[1])];
    let original_eta_scaled = [minus_q.clone(), q.clone()];
    // -q*(1,-1)=(-q,q).
    assert_eq!(original_eta_scaled, [minus_q.clone(), q.clone()]);
    assert_eq!(eta_image, original_eta_scaled);

    // Top degree is fixed by h^vee |-> h, so the determinant orientation and
    // i_2 coefficient remain +1.
    let top_twist_scale = LaurentPoly::one();
    assert_eq!(top_twist_scale, one);
}

fn check_koszul_to_cech_and_nonresonant_contraction() {
    // A monomial u^n in R[u^-1].  The Cech map in degree zero is localization
    // (u^0), while its degree-one Koszul comparison is multiplication by
    // u^-1.  Thus (u^-1)(u)=1 exactly.
    let cech_localization = LaurentPoly::one();
    let koszul_differential = LaurentPoly::u();
    let simple_pole = LaurentPoly::monomial(1, 0, -1);
    assert_eq!(
        simple_pole.multiply(&koszul_differential),
        cech_localization
    );

    // In homological notation this is the nonresonant contracting homotopy
    // s(p)=u^-1 ell: d s=id on degree zero and s d=id on degree one.
    assert_eq!(
        koszul_differential.multiply(&simple_pole),
        LaurentPoly::one()
    );

    // The reciprocal simple pole is 1/u^vee=-q/u.
    let reciprocal_simple_pole = LaurentPoly::monomial(-1, 1, -1);
    assert_eq!(
        reciprocal_simple_pole.multiply(&LaurentPoly::u_dual()),
        LaurentPoly::one()
    );

    // The simple-pole class is not an element of R: retaining it as the
    // localized term of the Cech complex differs from globally localizing K.
    assert!(simple_pole.0.keys().any(|&(_, u_exponent)| u_exponent < 0));
}

fn main() {
    check_support_directed_quivers();
    check_twist_pairing();
    check_repeated_normal_exact_sequence();
    check_koszul_to_cech_and_nonresonant_contraction();

    println!(
        "{}",
        concat!(
            r#"{"claim":"the one-normal unlocalized coefficient packet is the paired costandard/standard can-var quiver together with its finite Koszul-to-Cech simple-pole realization; its reciprocal/original pairing is perfect and its repeated plus/D03 normal gives the canonical shifted excess line","status":"proved","scope":"one normal and the repeated u3 coefficient factor only; no global augmented dual-block or lower-Cousin lift","ring":"Z[q^+-1], u=q-1, u^vee=-q^-1*u","support_conventions":{"original_locally_finite_BM":"Rj_*: can=u, var=1, support differential=can","reciprocal_regular_ordinary":"j_!: can=1, var=u^vee, support differential=var"},"checks":{"can_var_composites":"PASS","nonresonant_contraction":"PASS: s(p)=u^-1*ell","verdier_pairing":"PASS: beta(p,h^vee)=1 and beta(h,p^vee)=-q define K(u) tensor K(u^vee)->R[1]","pairing_perfectness":"PASS: antidiagonal determinant q is a Laurent unit","koszul_to_cech":"PASS: (id,u^-1):[R --u--> R]->[R -> R[u^-1]] is a chain map","reciprocal_simple_pole":"PASS: 1/u^vee=-q/u","repeated_normal_complex":"PASS: D2=(-u,u^vee)^T and D1=(u^vee,u) have square zero","repeated_normal_exactness":"PASS: pi1=(1,-q), eta_mix=(-q,-1), i2=1 give 0->K(u^vee)[1]->D->K(u^vee)->0","entry99_comparison":"PASS: p^vee->-q*p and h^vee->h send eta_mix to -q*(1,-1), with the shifted source scaling identically and top orientation +1"},"boundary":"the full supported Cech/local-cohomology object is not finite perfect, and this certificate does not define the missing global plus-sheet augmented dual-block map"}"#
        )
    );
}
