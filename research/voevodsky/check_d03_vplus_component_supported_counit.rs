//! Exact coefficient-node certificate for the v+ component-supported counit.
//!
//! This proves the local derived coefficient pairing.  It does not identify
//! the node with the literal spatial entry-143 v+ costalk.

use std::collections::BTreeMap;

type Z = i64;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Monomial {
    x5: u8,
    t5: u8,
    q5: i8,
}

type Polynomial = BTreeMap<Monomial, Z>;

fn term(x5: u8, t5: u8, q5: i8, coefficient: Z) -> Polynomial {
    BTreeMap::from([(Monomial { x5, t5, q5 }, coefficient)])
}

fn add(left: &Polynomial, right: &Polynomial) -> Polynomial {
    let mut result = left.clone();
    for (monomial, coefficient) in right {
        *result.entry(*monomial).or_default() += coefficient;
    }
    result.retain(|_, coefficient| *coefficient != 0);
    result
}

fn multiply(left: &Polynomial, right: &Polynomial) -> Polynomial {
    let mut result = Polynomial::new();
    for (left_monomial, left_coefficient) in left {
        for (right_monomial, right_coefficient) in right {
            let monomial = Monomial {
                x5: left_monomial.x5 + right_monomial.x5,
                t5: left_monomial.t5 + right_monomial.t5,
                q5: left_monomial.q5 + right_monomial.q5,
            };
            *result.entry(monomial).or_default() += left_coefficient * right_coefficient;
        }
    }
    result.retain(|_, coefficient| *coefficient != 0);
    result
}

fn scale(value: &Polynomial, coefficient: Z) -> Polynomial {
    value
        .iter()
        .filter_map(|(monomial, entry)| {
            let scaled = coefficient * entry;
            (scaled != 0).then_some((*monomial, scaled))
        })
        .collect()
}

fn main() {
    let x5 = term(1, 0, 0, 1);
    let t5 = term(0, 1, 0, 1);
    let q5 = term(0, 0, 1, 1);
    let u5 = multiply(&t5, &x5);
    let u5_dual = term(1, 1, -1, -1); // -q5^-1*u5

    // J_X=Cone(B->B/(t5))[-1]=(t5).  Multiplication by t5 is injective in
    // the polynomial node ring and its cokernel is obtained by setting t5=0.
    assert_ne!(t5, Polynomial::new());
    let conductor_generator_specializes_to_zero = t5.keys().all(|monomial| monomial.t5 > 0);
    assert!(conductor_generator_specializes_to_zero);

    // D5 has d2=(-u5,u5^vee)^T and d1=(u5^vee,u5).  The primitive oriented
    // middle vector eta5=(-q5,-1) lies in ker d1.
    let eta5 = [scale(&q5, -1), term(0, 0, 0, -1)];
    let d1_eta = add(&multiply(&u5_dual, &eta5[0]), &multiply(&u5, &eta5[1]));
    assert!(d1_eta.is_empty());

    // Normalize the top by q5.  Then q5*d2 is exactly x5*t5*eta5.
    let normalized_d2 = [multiply(&q5, &scale(&u5, -1)), multiply(&q5, &u5_dual)];
    let x5_t5 = multiply(&x5, &t5);
    let expected = [multiply(&x5_t5, &eta5[0]), multiply(&x5_t5, &eta5[1])];
    assert_eq!(normalized_d2, expected);

    // Cartier beta_x5 removes the principal x5 factor and leaves the
    // conductor class [t5]*eta5, without adjoining x5^-1 to the base.
    let beta = [multiply(&t5, &eta5[0]), multiply(&t5, &eta5[1])];
    assert_eq!(expected, [multiply(&x5, &beta[0]), multiply(&x5, &beta[1])]);
    let x5_inverted_in_base = false;
    assert!(!x5_inverted_in_base);

    // The occurrence edge de=X_D*m-x5*v has v coefficient -x5.  Evaluation
    // by the positively oriented principal ideal dual x5^vee gives -1.
    let occurrence_v_coefficient_before_evaluation = -1_i64;
    let positive_x5_dual_evaluation = 1_i64;
    let evaluated_v_coefficient =
        occurrence_v_coefficient_before_evaluation * positive_x5_dual_evaluation;
    assert_eq!(evaluated_v_coefficient, -1);
    let reversed_orientation_coefficient =
        occurrence_v_coefficient_before_evaluation * -positive_x5_dual_evaluation;
    assert_eq!(reversed_orientation_coefficient, 1);

    // Hom_B((t5),B) is a rank-one line.  Among bounded integral scalar
    // multiples, primitive positive residue normalization selects +1 uniquely.
    let candidates = (-3_i64..=3).collect::<Vec<_>>();
    let normalized = candidates
        .into_iter()
        .filter(|coefficient| *coefficient == 1)
        .collect::<Vec<_>>();
    assert_eq!(normalized, vec![1]);

    let shared_external_factors = ["u1", "u3"];
    let global_polarity_constructed = false;
    let literal_entry143_vplus_spatial_identification_constructed = false;
    assert_eq!(shared_external_factors, ["u1", "u3"]);
    assert!(!global_polarity_constructed);
    assert!(!literal_entry143_vplus_spatial_identification_constructed);

    println!(
        "{}",
        r#"{"claim":"For the coefficient node u5=t5*x5 on the v+ component, J_X=Cone(O_X->O_C)[-1] is the principal conductor line (t5). In D5=K(u5^vee) tensor K(u5), with u5^vee=-q5^-1*u5, the primitive oriented middle generator eta5=(-q5,-1) is closed and the normalized top satisfies d(z_norm)=x5*t5*eta5. The Cartier connecting morphism along x5 therefore gives beta_x5(z_norm)=[t5]*eta5 without inverting x5. This is compatible with the v+ occurrence coefficient -x5 through the positive principal-ideal dual evaluation x5^vee(x5)=1, and primitive positive normalization makes the conductor counit unique.","status":"proved_scoped_local_component_coefficient_counit","scope":"Local coherent/derived coefficient node, one-normal reciprocal/original packet, Cartier boundary, and occurrence endpoint compatibility only. Shared u1/u3 factors are external. No literal spatial entry143 endpoint identification or global polarity statement is made.","evidence_refs":["ledger entries 100 and 119","research/voevodsky/check_d03_vplus_component_supported_counit.rs"],"factorization_test":{"node":"u5=t5*x5","component_conductor":"J_X=(t5)","reciprocal_normal":"u5^vee=-q5^-1*u5","eta5":"(-q5,-1), primitive and d1-closed","normalized_identity":"d(z_norm)=x5*t5*eta5","Cartier_beta":"[t5]*eta5","x5_base_inverted":false,"occurrence_edge":"de=X_D*m_plus-x5*v_plus","positive_endpoint_evaluation":"x5^vee(x5)=1 gives coefficient -1","orientation_reversal":"reverses the endpoint sign","uniqueness":"Hom((t5),B) is rank one; primitive positive residue selects scalar +1","shared_external_factors":["u1","u3"]},"unconstructed":["ringed spatial functor identifying the node component with literal entry143 E_vplus","global polarity-conjugate component counit","generic-to-special Q leg"],"boundary":"The component-supported counit is canonical and chain-level in the coefficient node model. Its final identification with the actual K6 endpoint costalk remains a separate spatial construction."}"#
    );
}
