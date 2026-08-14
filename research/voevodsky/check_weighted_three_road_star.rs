//! Exact algebraic certificate for the corrected weighted three-road star.
//!
//! The base ring is
//!
//!   R0=Z[q0^+-1,...,q5^+-1], uj=qj-1.
//!
//! No uj is inverted in R0.  Negative u powers below occur only in explicitly
//! labelled support-Cech localization summands.  Put
//!
//!   A=(u1,u3,u5), tau_A=1/(u1*u3*u5), E=(u4,u0,u2).
//!
//! The raw source is K(E), in the based form
//!
//!   f=h4*h0*h2,
//!   e1=p4*h0*h2, e3=-h4*p0*h2, e5=h4*h0*p2,
//!   q0=p4*p0*h2, q1=p4*h0*p2, q2=h4*p0*p2,
//!   a=p4*p0*p2.
//!
//! The candidate target is the relative three-road star with Cech
//! coefficients.  This certificate checks the formal map
//!
//!   f  |-> tau_A Krel,
//!   e1 |-> tau_A/u4 T2,
//!   e3 |-> tau_A/u0 T1,
//!   e5 |-> tau_A/u2 T0,
//!   q0,q1,q2,a |-> 0.
//!
//! It proves the raw Koszul identities, the top chain square, every lower
//! zero-target square, and D3 covariance with all basis signs.  It does not
//! construct the intrinsic supported arrow f->Krel, nor attach entry 100's
//! local excess, occurrence, and physical-normal lines to the three displayed
//! road terms.  The result is therefore conditional/inconclusive as a PC map.

use std::collections::BTreeMap;

type Int = i64;
type Mask = u8;

const NORMALS: usize = 6;
const EVEN_SEQUENCE: [usize; 3] = [4, 0, 2];
const ODD_SUPPORT: [usize; 3] = [1, 3, 5];

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum SourceBasis {
    F,
    E1,
    E3,
    E5,
    Q0,
    Q1,
    Q2,
    Augmentation,
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum TargetBasis {
    Krel,
    T0,
    T1,
    T2,
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Monomial {
    u: [i8; NORMALS],
}

impl Monomial {
    fn one() -> Self {
        Self { u: [0; NORMALS] }
    }

    fn u(index: usize, exponent: i8) -> Self {
        let mut result = Self::one();
        result.u[index] = exponent;
        result
    }

    fn multiply(self, other: Self) -> Self {
        Self {
            u: std::array::from_fn(|index| self.u[index] + other.u[index]),
        }
    }

    fn permute(self, permutation: fn(usize) -> usize) -> Self {
        let mut result = Self::one();
        for index in 0..NORMALS {
            result.u[permutation(index)] = self.u[index];
        }
        result
    }
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct CechCoefficient {
    localization: Mask,
    monomial: Monomial,
}

impl CechCoefficient {
    fn multiply_by_u(mut self, normal: usize) -> Self {
        self.monomial.u[normal] += 1;
        self
    }

    fn permute(self, permutation: fn(usize) -> usize) -> Self {
        let mut localization = 0_u8;
        for normal in 0..NORMALS {
            if self.localization & (1 << normal) != 0 {
                localization |= 1 << permutation(normal);
            }
        }
        Self {
            localization,
            monomial: self.monomial.permute(permutation),
        }
    }

    fn denominators_are_legal(self) -> bool {
        (0..NORMALS)
            .all(|normal| self.monomial.u[normal] >= 0 || self.localization & (1 << normal) != 0)
    }
}

type SourceCombination = BTreeMap<(SourceBasis, Monomial), Int>;
type TargetCombination = BTreeMap<(TargetBasis, CechCoefficient), Int>;

fn add_source(
    value: &mut SourceCombination,
    basis: SourceBasis,
    monomial: Monomial,
    coefficient: Int,
) {
    *value.entry((basis, monomial)).or_default() += coefficient;
    value.retain(|_, entry| *entry != 0);
}

fn add_target(
    value: &mut TargetCombination,
    basis: TargetBasis,
    coefficient_data: CechCoefficient,
    coefficient: Int,
) {
    *value.entry((basis, coefficient_data)).or_default() += coefficient;
    value.retain(|_, entry| *entry != 0);
}

fn source_data(basis: SourceBasis) -> (Mask, Int) {
    match basis {
        SourceBasis::F => (0b111, 1),
        SourceBasis::E1 => (0b110, 1),
        SourceBasis::E3 => (0b101, -1),
        SourceBasis::E5 => (0b011, 1),
        SourceBasis::Q0 => (0b100, 1),
        SourceBasis::Q1 => (0b010, 1),
        SourceBasis::Q2 => (0b001, 1),
        SourceBasis::Augmentation => (0b000, 1),
    }
}

fn source_basis_for_mask(mask: Mask) -> SourceBasis {
    match mask {
        0b111 => SourceBasis::F,
        0b110 => SourceBasis::E1,
        0b101 => SourceBasis::E3,
        0b011 => SourceBasis::E5,
        0b100 => SourceBasis::Q0,
        0b010 => SourceBasis::Q1,
        0b001 => SourceBasis::Q2,
        0b000 => SourceBasis::Augmentation,
        _ => panic!("invalid three-generator mask"),
    }
}

fn source_boundary(basis: SourceBasis) -> SourceCombination {
    let (mask, source_scale) = source_data(basis);
    let mut result = SourceCombination::new();
    let mut exterior_position = 0_usize;
    for (slot, &normal) in EVEN_SEQUENCE.iter().enumerate() {
        if mask & (1 << slot) == 0 {
            continue;
        }
        let face = mask & !(1 << slot);
        let target_basis = source_basis_for_mask(face);
        let (_, target_scale) = source_data(target_basis);
        let exterior_sign = if exterior_position % 2 == 0 { 1 } else { -1 };
        add_source(
            &mut result,
            target_basis,
            Monomial::u(normal, 1),
            source_scale * exterior_sign * target_scale,
        );
        exterior_position += 1;
    }
    result
}

fn source_boundary_of_combination(value: &SourceCombination) -> SourceCombination {
    let mut result = SourceCombination::new();
    for (&(basis, monomial), &coefficient) in value {
        for ((target_basis, boundary_monomial), boundary_coefficient) in source_boundary(basis) {
            add_source(
                &mut result,
                target_basis,
                monomial.multiply(boundary_monomial),
                coefficient * boundary_coefficient,
            );
        }
    }
    result
}

fn tau_a() -> CechCoefficient {
    let mut localization = 0_u8;
    let mut monomial = Monomial::one();
    for normal in ODD_SUPPORT {
        localization |= 1 << normal;
        monomial.u[normal] = -1;
    }
    CechCoefficient {
        localization,
        monomial,
    }
}

fn simple_pole(even_normal: usize) -> CechCoefficient {
    let mut result = tau_a();
    result.localization |= 1 << even_normal;
    result.monomial.u[even_normal] = -1;
    result
}

fn star_map(basis: SourceBasis) -> TargetCombination {
    let mut result = TargetCombination::new();
    match basis {
        SourceBasis::F => add_target(&mut result, TargetBasis::Krel, tau_a(), 1),
        SourceBasis::E1 => add_target(&mut result, TargetBasis::T2, simple_pole(4), 1),
        SourceBasis::E3 => add_target(&mut result, TargetBasis::T1, simple_pole(0), 1),
        SourceBasis::E5 => add_target(&mut result, TargetBasis::T0, simple_pole(2), 1),
        SourceBasis::Q0 | SourceBasis::Q1 | SourceBasis::Q2 | SourceBasis::Augmentation => {}
    }
    result
}

fn star_map_of_source_combination(value: &SourceCombination) -> TargetCombination {
    let mut result = TargetCombination::new();
    for (&(basis, monomial), &coefficient) in value {
        for ((target_basis, target_coefficient), map_coefficient) in star_map(basis) {
            let mut multiplied = target_coefficient;
            multiplied.monomial = multiplied.monomial.multiply(monomial);
            add_target(
                &mut result,
                target_basis,
                multiplied,
                coefficient * map_coefficient,
            );
        }
    }
    result
}

fn target_boundary(value: &TargetCombination) -> TargetCombination {
    let mut result = TargetCombination::new();
    for (&(basis, coefficient_data), &coefficient) in value {
        if basis != TargetBasis::Krel {
            continue;
        }
        for (road, even_normal) in [
            (TargetBasis::T0, 2_usize),
            (TargetBasis::T1, 0_usize),
            (TargetBasis::T2, 4_usize),
        ] {
            let mut localized = coefficient_data;
            localized.localization |= 1 << even_normal;
            add_target(&mut result, road, localized, coefficient);
        }
    }
    result
}

fn check_raw_koszul_differential() {
    assert_eq!(
        source_boundary(SourceBasis::F),
        BTreeMap::from([
            ((SourceBasis::E1, Monomial::u(4, 1)), 1),
            ((SourceBasis::E3, Monomial::u(0, 1)), 1),
            ((SourceBasis::E5, Monomial::u(2, 1)), 1),
        ])
    );
    assert_eq!(
        source_boundary(SourceBasis::E1),
        BTreeMap::from([
            ((SourceBasis::Q0, Monomial::u(0, 1)), 1),
            ((SourceBasis::Q1, Monomial::u(2, 1)), -1),
        ])
    );
    assert_eq!(
        source_boundary(SourceBasis::E3),
        BTreeMap::from([
            ((SourceBasis::Q0, Monomial::u(4, 1)), -1),
            ((SourceBasis::Q2, Monomial::u(2, 1)), 1),
        ])
    );
    assert_eq!(
        source_boundary(SourceBasis::E5),
        BTreeMap::from([
            ((SourceBasis::Q1, Monomial::u(4, 1)), 1),
            ((SourceBasis::Q2, Monomial::u(0, 1)), -1),
        ])
    );
    assert_eq!(
        source_boundary(SourceBasis::Q0),
        BTreeMap::from([((SourceBasis::Augmentation, Monomial::u(2, 1)), 1)])
    );
    assert_eq!(
        source_boundary(SourceBasis::Q1),
        BTreeMap::from([((SourceBasis::Augmentation, Monomial::u(0, 1)), 1)])
    );
    assert_eq!(
        source_boundary(SourceBasis::Q2),
        BTreeMap::from([((SourceBasis::Augmentation, Monomial::u(4, 1)), 1)])
    );
    assert!(source_boundary(SourceBasis::Augmentation).is_empty());

    for basis in [
        SourceBasis::F,
        SourceBasis::E1,
        SourceBasis::E3,
        SourceBasis::E5,
        SourceBasis::Q0,
        SourceBasis::Q1,
        SourceBasis::Q2,
        SourceBasis::Augmentation,
    ] {
        assert!(source_boundary_of_combination(&source_boundary(basis)).is_empty());
    }
}

fn check_cech_values_and_chain_map() {
    let tau = tau_a();
    assert!(tau.denominators_are_legal());
    for normal in [4_usize, 0, 2] {
        let pole = simple_pole(normal);
        assert!(pole.denominators_are_legal());
        assert_eq!(pole.multiply_by_u(normal).monomial, tau.monomial);
    }

    assert_eq!(
        star_map(SourceBasis::F),
        BTreeMap::from([((TargetBasis::Krel, tau), 1)])
    );
    assert_eq!(
        star_map(SourceBasis::E1),
        BTreeMap::from([((TargetBasis::T2, simple_pole(4)), 1)])
    );
    assert_eq!(
        star_map(SourceBasis::E3),
        BTreeMap::from([((TargetBasis::T1, simple_pole(0)), 1)])
    );
    assert_eq!(
        star_map(SourceBasis::E5),
        BTreeMap::from([((TargetBasis::T0, simple_pole(2)), 1)])
    );

    // The top identity is exactly ui*(tau/ui)=tau in the indicated road
    // localization, together with dKrel=T0+T1+T2.
    assert_eq!(
        target_boundary(&star_map(SourceBasis::F)),
        star_map_of_source_combination(&source_boundary(SourceBasis::F))
    );

    // The relative target has no groups below its three roads.  Sending all
    // q's and the augmentation to zero makes every remaining square strict.
    for basis in [
        SourceBasis::E1,
        SourceBasis::E3,
        SourceBasis::E5,
        SourceBasis::Q0,
        SourceBasis::Q1,
        SourceBasis::Q2,
        SourceBasis::Augmentation,
    ] {
        assert_eq!(
            target_boundary(&star_map(basis)),
            star_map_of_source_combination(&source_boundary(basis))
        );
    }

    assert!(star_map(SourceBasis::Q0).is_empty());
    assert!(star_map(SourceBasis::Q1).is_empty());
    assert!(star_map(SourceBasis::Q2).is_empty());
    assert!(star_map(SourceBasis::Augmentation).is_empty());
}

fn rotation_normal(normal: usize) -> usize {
    (normal + 2) % NORMALS
}

fn reflection_normal(normal: usize) -> usize {
    (2 + NORMALS - normal) % NORMALS
}

fn rotation_source(basis: SourceBasis) -> (SourceBasis, Int) {
    (
        match basis {
            SourceBasis::F => SourceBasis::F,
            SourceBasis::E1 => SourceBasis::E3,
            SourceBasis::E3 => SourceBasis::E5,
            SourceBasis::E5 => SourceBasis::E1,
            SourceBasis::Q0 => SourceBasis::Q2,
            SourceBasis::Q2 => SourceBasis::Q1,
            SourceBasis::Q1 => SourceBasis::Q0,
            SourceBasis::Augmentation => SourceBasis::Augmentation,
        },
        1,
    )
}

fn reflection_source(basis: SourceBasis) -> (SourceBasis, Int) {
    match basis {
        SourceBasis::F => (SourceBasis::F, -1),
        SourceBasis::E1 => (SourceBasis::E1, -1),
        SourceBasis::E3 => (SourceBasis::E5, -1),
        SourceBasis::E5 => (SourceBasis::E3, -1),
        SourceBasis::Q0 => (SourceBasis::Q1, 1),
        SourceBasis::Q1 => (SourceBasis::Q0, 1),
        SourceBasis::Q2 => (SourceBasis::Q2, 1),
        SourceBasis::Augmentation => (SourceBasis::Augmentation, 1),
    }
}

fn rotation_target(basis: TargetBasis) -> (TargetBasis, Int) {
    (
        match basis {
            TargetBasis::Krel => TargetBasis::Krel,
            TargetBasis::T2 => TargetBasis::T1,
            TargetBasis::T1 => TargetBasis::T0,
            TargetBasis::T0 => TargetBasis::T2,
        },
        1,
    )
}

fn reflection_target(basis: TargetBasis) -> (TargetBasis, Int) {
    match basis {
        TargetBasis::Krel => (TargetBasis::Krel, -1),
        TargetBasis::T2 => (TargetBasis::T2, -1),
        TargetBasis::T1 => (TargetBasis::T0, -1),
        TargetBasis::T0 => (TargetBasis::T1, -1),
    }
}

fn transform_source_combination(
    value: &SourceCombination,
    basis_action: fn(SourceBasis) -> (SourceBasis, Int),
    normal_action: fn(usize) -> usize,
) -> SourceCombination {
    let mut result = SourceCombination::new();
    for (&(basis, monomial), &coefficient) in value {
        let (image, sign) = basis_action(basis);
        add_source(
            &mut result,
            image,
            monomial.permute(normal_action),
            coefficient * sign,
        );
    }
    result
}

fn transform_target_combination(
    value: &TargetCombination,
    basis_action: fn(TargetBasis) -> (TargetBasis, Int),
    normal_action: fn(usize) -> usize,
) -> TargetCombination {
    let mut result = TargetCombination::new();
    for (&(basis, coefficient_data), &coefficient) in value {
        let (image, sign) = basis_action(basis);
        add_target(
            &mut result,
            image,
            coefficient_data.permute(normal_action),
            coefficient * sign,
        );
    }
    result
}

fn apply_source_action(
    basis: SourceBasis,
    action: fn(SourceBasis) -> (SourceBasis, Int),
) -> (SourceBasis, Int) {
    action(basis)
}

fn compose_source_actions(
    basis: SourceBasis,
    actions: &[fn(SourceBasis) -> (SourceBasis, Int)],
) -> (SourceBasis, Int) {
    actions
        .iter()
        .fold((basis, 1_i64), |(present, sign), action| {
            let (next, next_sign) = apply_source_action(present, *action);
            (next, sign * next_sign)
        })
}

fn compose_target_actions(
    basis: TargetBasis,
    actions: &[fn(TargetBasis) -> (TargetBasis, Int)],
) -> (TargetBasis, Int) {
    actions
        .iter()
        .fold((basis, 1_i64), |(present, sign), action| {
            let (next, next_sign) = action(present);
            (next, sign * next_sign)
        })
}

fn check_d3_covariance() {
    let bases = [
        SourceBasis::F,
        SourceBasis::E1,
        SourceBasis::E3,
        SourceBasis::E5,
        SourceBasis::Q0,
        SourceBasis::Q1,
        SourceBasis::Q2,
        SourceBasis::Augmentation,
    ];

    // r^3=s^2=1 and srs=r^-1 on every signed source basis.
    for basis in bases {
        assert_eq!(
            compose_source_actions(
                basis,
                &[rotation_source as fn(SourceBasis) -> (SourceBasis, Int); 3],
            ),
            (basis, 1)
        );
        assert_eq!(
            compose_source_actions(
                basis,
                &[reflection_source as fn(SourceBasis) -> (SourceBasis, Int); 2],
            ),
            (basis, 1)
        );
        assert_eq!(
            compose_source_actions(
                basis,
                &[reflection_source, rotation_source, reflection_source]
            ),
            compose_source_actions(basis, &[rotation_source, rotation_source])
        );
    }

    for basis in [
        TargetBasis::Krel,
        TargetBasis::T0,
        TargetBasis::T1,
        TargetBasis::T2,
    ] {
        assert_eq!(
            compose_target_actions(
                basis,
                &[rotation_target as fn(TargetBasis) -> (TargetBasis, Int); 3],
            ),
            (basis, 1)
        );
        assert_eq!(
            compose_target_actions(
                basis,
                &[reflection_target as fn(TargetBasis) -> (TargetBasis, Int); 2],
            ),
            (basis, 1)
        );
        assert_eq!(
            compose_target_actions(
                basis,
                &[reflection_target, rotation_target, reflection_target]
            ),
            compose_target_actions(basis, &[rotation_target, rotation_target])
        );
    }

    // Both source differential and the candidate star map are D3-covariant.
    for basis in bases {
        for (source_action, target_action, normal_action) in [
            (
                rotation_source as fn(SourceBasis) -> (SourceBasis, Int),
                rotation_target as fn(TargetBasis) -> (TargetBasis, Int),
                rotation_normal as fn(usize) -> usize,
            ),
            (
                reflection_source as fn(SourceBasis) -> (SourceBasis, Int),
                reflection_target as fn(TargetBasis) -> (TargetBasis, Int),
                reflection_normal as fn(usize) -> usize,
            ),
        ] {
            let (image_basis, image_sign) = source_action(basis);
            let mut boundary_after_action = source_boundary(image_basis);
            for coefficient in boundary_after_action.values_mut() {
                *coefficient *= image_sign;
            }
            assert_eq!(
                boundary_after_action,
                transform_source_combination(&source_boundary(basis), source_action, normal_action)
            );

            let mut map_after_action = star_map(image_basis);
            for coefficient in map_after_action.values_mut() {
                *coefficient *= image_sign;
            }
            assert_eq!(
                map_after_action,
                transform_target_combination(&star_map(basis), target_action, normal_action)
            );
        }
    }
}

fn main() {
    check_raw_koszul_differential();
    check_cech_values_and_chain_map();
    check_d3_covariance();

    println!(
        "{}",
        concat!(
            r#"{"claim":"the corrected weighted three-road star is an exact D3-covariant chain map after defining the supported top value tau_A*Krel and the three localized road values, with q and augmentation sent to zero; the checker does not intrinsically construct that top arrow or attach the established local excess/occurrence/physical data","status":"inconclusive","conditional_theorem":"if the intrinsic supported arrow f_plus->tau_A*Krel exists and restricts to the three labelled entry-100 road traces, the displayed weighted star is a strict D3-equivariant chain map","ring":{"base":"R0=Z[q0^+-1,...,q5^+-1], uj=qj-1","base_inversions":"none: no uj or integer is inverted in R0","cech_rule":"negative uj powers occur only in a localization summand whose support mask contains j","tau_A":"1/(u1*u3*u5) in the A=(u1,u3,u5) Cech summand"},"source":{"complex":"K(u4,u0,u2)","bases":{"degree3":"f=h4*h0*h2","degree2":["e1=p4*h0*h2","e3=-h4*p0*h2","e5=h4*h0*p2"],"degree1":["q0=p4*p0*h2","q1=p4*h0*p2","q2=h4*p0*p2"],"degree0":"a=p4*p0*p2"},"differential":{"f":"u4*e1+u0*e3+u2*e5","e1":"u0*q0-u2*q1","e3":"-u4*q0+u2*q2","e5":"u4*q1-u0*q2","q0":"u2*a","q1":"u0*a","q2":"u4*a","a":"0"},"d_squared":"zero on all eight bases"},"target":{"relative_bases":{"degree3":"Krel","degree2":["T0","T1","T2"],"lower":"zero"},"differential":"dKrel=T0+T1+T2, with localization into the appropriate road Cech summand","map":{"f":"tau_A*Krel","e1":"tau_A/u4*T2","e3":"tau_A/u0*T1","e5":"tau_A/u2*T0","q0_q1_q2_a":"0"},"top_identity":"G(df)=tau_A*(T2+T1+T0)=d(tau_A*Krel), using uj*(tau_A/uj)=tau_A inside each indicated Cech summand","lower_identity":"all edge, q, and augmentation squares commute because the relative target is zero below road degree"},"D3":{"rotation":{"normals":"4->0->2->4 and 1->3->5->1","source_edges":"e1->e3->e5->e1","target_roads":"T2->T1->T0->T2","top_sign":"+1"},"reflection":{"normals":"0<->2, 4 fixed; 3<->5, 1 fixed","source":"f,e1,e3,e5 carry the exterior orientation signs (-,-,-,-), with e3<->e5; q0<->q1 and q2 fixed","target":"Krel and all road orientations carry -1, with T1<->T0 and T2 fixed"},"relations":"r^3=s^2=1 and srs=r^-1; differential and candidate map are covariant"},"checks":{"raw_Koszul_differential":"PASS","raw_d_squared":"PASS","Cech_denominator_legality":"PASS","four_displayed_Koszul_to_Cech_values":"PASS","top_chain_identity":"PASS","q_and_augmentation_zero_compatibility":"PASS","D3_group_relations_and_signs":"PASS","D3_differential_covariance":"PASS","D3_map_covariance":"PASS"},"typing_boundary":{"intrinsic_supported_top_arrow":"NOT SUPPLIED: tau_A*Krel is the candidate value being assumed, not derived by entries 93-100","local_attachment":"NOT SUPPLIED: this coefficient checker does not identify its three road terms with the mixed excess generators, occurrence counits, or separate physical normal evaluations of entry 100","PC_status":"CONDITIONAL/INCONCLUSIVE, not a constructed global PC/Gysin map"},"next_experiment":"construct the intrinsic supported f_plus-to-Krel arrow from the normalization-conductor/relative-face geometry and prove that its three restrictions are exactly the labelled local excess traces with occurrence and physical-normal factors retained"}"#
        )
    );
}
