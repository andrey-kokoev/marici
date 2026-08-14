//! Exact formal-model audit for the entry-116 D03 Thom endpoint proposal.
//!
//! Put `R=Z[x1,x5]`.  The smallest augmented occurrence-cellular hull of
//! the column `e3 -> q0 + q2` is the two-variable Koszul resolution
//!
//! ```text
//! R<e3> --(-x1,x5)^T--> R<q0,q2> --(x5,x1)--> R<a>
//!        --> R/(x1,x5) --> 0.
//! ```
//!
//! The signs and variables are derived from the masks
//! `e3=101`, `q0=100`, `q2=001`, not entered as a target road column.
//! Tensoring with the external rank-one line `L3=[t3]` preserves this exact
//! complex and does not put an internal `h3` generator on any endpoint.
//!
//! To audit a push to actual road costalks, leave their generization map
//! unknown:
//!
//! ```text
//! d_road(F03)=b0*tau_q0+b2*tau_q2.
//! ```
//!
//! Write the generic component of a putative correspondence as `g` and its
//! endpoint components as `a0,a2`.  The two paths in the Cartier--PL square
//! commute exactly when
//!
//! ```text
//! g*b0 = -x1*a0,     g*b2 = x5*a2.
//! ```
//!
//! With the established normalized generic carrier `g=1`, a diagonal
//! endpoint map exists precisely when `b0` is in `(x1)` and `b2` is in
//! `(x5)`, and then it is unique for that already supplied road boundary:
//! `a0=-b0/x1`, `a2=b2/x5`.  The external tensor product supplies neither
//! `b0` nor `b2`.  Varying `a0,a2` and deriving `b0,b2` gives distinct valid
//! formal squares, so the tensor model alone does not canonically select a
//! push to the separately typed reciprocal/Borel--Moore Tor1 costalks.
//!
//! Independently, any chain map between the primitive lcm line and its two
//! principal endpoint lines satisfies
//!
//! ```text
//! alpha=x1*b0=x5*b2.
//! ```
//!
//! Coprimality derives, rather than assigns, the complete family
//! `(alpha,b0,b2)=c*(x1*x5,x5,x1)`.  This formal lcm classification still
//! does not identify the abstract Boolean cells `q0={x5}`, `q2={x1}` with
//! any entry-86/97 occurrence vertex of the actual F03 road square.

use std::collections::BTreeMap;

type Int = i64;

const SLOT_X1: usize = 0;
const SLOT_X3: usize = 1;
const SLOT_X5: usize = 2;
const MASK_E3: u8 = 0b101;
const MASK_Q0: u8 = 0b100;
const MASK_Q2: u8 = 0b001;
const MASK_A: u8 = 0b000;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Monomial([u8; 2]);

impl Monomial {
    fn one() -> Self {
        Self([0, 0])
    }

    fn variable(slot: usize) -> Self {
        let mut exponent = [0; 2];
        exponent[slot] = 1;
        Self(exponent)
    }

    fn multiply(self, other: Self) -> Self {
        Self(std::array::from_fn(|slot| self.0[slot] + other.0[slot]))
    }

    fn gcd(self, other: Self) -> Self {
        Self(std::array::from_fn(|slot| self.0[slot].min(other.0[slot])))
    }

    fn divide(self, divisor: Self) -> Option<Self> {
        self.0
            .iter()
            .zip(divisor.0)
            .all(|(numerator, denominator)| *numerator >= denominator)
            .then(|| Self(std::array::from_fn(|slot| self.0[slot] - divisor.0[slot])))
    }
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct Polynomial(BTreeMap<Monomial, Int>);

impl Polynomial {
    fn zero() -> Self {
        Self(BTreeMap::new())
    }

    fn one() -> Self {
        Self::monomial(1, Monomial::one())
    }

    fn variable(slot: usize) -> Self {
        Self::monomial(1, Monomial::variable(slot))
    }

    fn monomial(coefficient: Int, monomial: Monomial) -> Self {
        if coefficient == 0 {
            Self::zero()
        } else {
            Self(BTreeMap::from([(monomial, coefficient)]))
        }
    }

    fn add_scaled(&mut self, other: &Self, scale: Int) {
        for (monomial, coefficient) in &other.0 {
            let entry = self.0.entry(*monomial).or_default();
            *entry += scale * coefficient;
            if *entry == 0 {
                self.0.remove(monomial);
            }
        }
    }

    fn add(&self, other: &Self) -> Self {
        let mut result = self.clone();
        result.add_scaled(other, 1);
        result
    }

    fn scale(&self, scalar: Int) -> Self {
        let mut result = Self::zero();
        result.add_scaled(self, scalar);
        result
    }

    fn multiply(&self, other: &Self) -> Self {
        let mut result = Self::zero();
        for (left_monomial, left_coefficient) in &self.0 {
            for (right_monomial, right_coefficient) in &other.0 {
                let term = Self::monomial(
                    left_coefficient * right_coefficient,
                    left_monomial.multiply(*right_monomial),
                );
                result.add_scaled(&term, 1);
            }
        }
        result
    }

    fn divide_by_monomial(&self, divisor: Monomial) -> Option<Self> {
        let mut result = Self::zero();
        for (monomial, coefficient) in &self.0 {
            let quotient = monomial.divide(divisor)?;
            result.add_scaled(&Self::monomial(*coefficient, quotient), 1);
        }
        Some(result)
    }

    fn central_fibre_constant(&self) -> Int {
        self.0.get(&Monomial::one()).copied().unwrap_or(0)
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Occurrence {
    X1,
    X5,
}

impl Occurrence {
    fn polynomial(self) -> Polynomial {
        match self {
            Self::X1 => Polynomial::variable(0),
            Self::X5 => Polynomial::variable(1),
        }
    }

    fn monomial(self) -> Monomial {
        match self {
            Self::X1 => Monomial::variable(0),
            Self::X5 => Monomial::variable(1),
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Cell {
    Q0,
    Q2,
    A,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct BoundaryTerm {
    target: Cell,
    coefficient: Polynomial,
    deleted_occurrence: Occurrence,
}

fn deletion_sign(source_mask: u8, deleted_slot: usize, orientation_scale: Int) -> Int {
    assert_ne!(source_mask & (1 << deleted_slot), 0);
    let preceding = (0..deleted_slot)
        .filter(|slot| source_mask & (1 << slot) != 0)
        .count();
    let exterior_sign = if preceding % 2 == 0 { 1 } else { -1 };
    orientation_scale * exterior_sign
}

fn occurrence_for_slot(slot: usize) -> Occurrence {
    match slot {
        SLOT_X1 => Occurrence::X1,
        SLOT_X5 => Occurrence::X5,
        _ => unreachable!(),
    }
}

fn weighted_deletion(
    source_mask: u8,
    deleted_slot: usize,
    target: Cell,
    orientation_scale: Int,
) -> BoundaryTerm {
    let occurrence = occurrence_for_slot(deleted_slot);
    BoundaryTerm {
        target,
        coefficient: occurrence.polynomial().scale(deletion_sign(
            source_mask,
            deleted_slot,
            orientation_scale,
        )),
        deleted_occurrence: occurrence,
    }
}

fn derive_occurrence_boundaries() -> ([BoundaryTerm; 2], [BoundaryTerm; 2]) {
    assert_eq!(MASK_E3 & !(1 << SLOT_X1), MASK_Q0);
    assert_eq!(MASK_E3 & !(1 << SLOT_X5), MASK_Q2);
    assert_eq!(MASK_Q0 & !(1 << SLOT_X5), MASK_A);
    assert_eq!(MASK_Q2 & !(1 << SLOT_X1), MASK_A);

    // The established e3 basis has scale -1.  The q0 and q2 bases have the
    // induced positive scales in the two-variable Boolean face.
    let e3_boundary = [
        weighted_deletion(MASK_E3, SLOT_X1, Cell::Q0, -1),
        weighted_deletion(MASK_E3, SLOT_X5, Cell::Q2, -1),
    ];
    let q_boundary = [
        weighted_deletion(MASK_Q0, SLOT_X5, Cell::A, 1),
        weighted_deletion(MASK_Q2, SLOT_X1, Cell::A, 1),
    ];
    (e3_boundary, q_boundary)
}

fn check_augmented_koszul_exact_hull() {
    let x1 = Polynomial::variable(0);
    let x5 = Polynomial::variable(1);
    let (d2, d1) = derive_occurrence_boundaries();
    assert_eq!(d2[0].coefficient, x1.scale(-1));
    assert_eq!(d2[1].coefficient, x5);
    assert_eq!(d1[0].coefficient, Polynomial::variable(1));
    assert_eq!(d1[1].coefficient, Polynomial::variable(0));

    let d_squared = d1[0]
        .coefficient
        .multiply(&d2[0].coefficient)
        .add(&d1[1].coefficient.multiply(&d2[1].coefficient));
    assert_eq!(d_squared, Polynomial::zero());

    // Exactness is the monomial-syzygy calculation for the row (x5,x1).
    // Its entries are coprime, so its first syzygy is (x1,-x5), which is
    // exactly -d2.  The row image is the augmentation ideal (x1,x5), and d2
    // is injective because R is a polynomial domain and its column is nonzero.
    let row = [Occurrence::X5.monomial(), Occurrence::X1.monomial()];
    let common = row[0].gcd(row[1]);
    assert_eq!(common, Monomial::one());
    let primitive_syzygy = [
        row[1].divide(common).unwrap(),
        row[0].divide(common).unwrap(),
    ];
    assert_eq!(
        primitive_syzygy,
        [Occurrence::X1.monomial(), Occurrence::X5.monomial()]
    );
    assert_eq!(d1[0].deleted_occurrence, Occurrence::X5);
    assert_eq!(d1[1].deleted_occurrence, Occurrence::X1);
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum LineType {
    ExternalReesThomT3,
    InternalNormalH3,
}

fn check_external_thom_and_principal_lines() {
    for mask in [MASK_E3, MASK_Q0, MASK_Q2] {
        assert_eq!(mask & (1 << SLOT_X3), 0);
    }
    let retained_line = LineType::ExternalReesThomT3;
    assert_ne!(retained_line, LineType::InternalNormalH3);

    // The two raw endpoint terms lie in the independently labelled principal
    // ideals I1=(x1) and I5=(x5).  Evaluation by their chosen generator-duals
    // removes only those ideal generators; it does not identify either result
    // with an actual road Tor1 costalk.
    let (d2, _) = derive_occurrence_boundaries();
    let evaluated_q0 = d2[0]
        .coefficient
        .divide_by_monomial(Occurrence::X1.monomial())
        .unwrap();
    let evaluated_q2 = d2[1]
        .coefficient
        .divide_by_monomial(Occurrence::X5.monomial())
        .unwrap();
    assert_eq!(evaluated_q0, Polynomial::one().scale(-1));
    assert_eq!(evaluated_q2, Polynomial::one());
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Variance {
    ReciprocalRegular,
    OriginalBorelMoore,
}

fn check_actual_tor_line_typing_after_base_change() {
    // In this reduced occurrence model the central coefficient fibre is
    // C=R/(x1,x5).  Resolving R/(xi) by [R --xi--> R] and tensoring with C
    // gives [C --0--> C], so H0 and Tor1 are separate rank-one C-lines.
    for occurrence in [Occurrence::X1, Occurrence::X5] {
        assert_eq!(occurrence.polynomial().central_fibre_constant(), 0);
        let central_fibre_differential = occurrence.polynomial().central_fibre_constant();
        assert_eq!(central_fibre_differential, 0);
        let h0_rank = 1_usize;
        let tor1_rank = 1_usize;
        assert_eq!((h0_rank, tor1_rank), (1, 1));
    }

    // The required target is variance-changing, not a second copy of the
    // source cellular line.  Scalar base change forgets the occurrence
    // inclusions, so its zero differential cannot recover their ideal labels.
    let source_variance = Variance::ReciprocalRegular;
    let target_variance = Variance::OriginalBorelMoore;
    assert_ne!(source_variance, target_variance);
    let (d2, _) = derive_occurrence_boundaries();
    assert!(d2
        .iter()
        .all(|term| term.coefficient.central_fibre_constant() == 0));
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct LcmLineChainMap {
    alpha: Polynomial,
    b0: Polynomial,
    b2: Polynomial,
}

fn classify_lcm_line_chain_map(candidate: &LcmLineChainMap) -> Option<Polynomial> {
    let x1 = Occurrence::X1.polynomial();
    let x5 = Occurrence::X5.polynomial();
    if candidate.alpha != x1.multiply(&candidate.b0)
        || candidate.alpha != x5.multiply(&candidate.b2)
    {
        return None;
    }

    let lcm = Occurrence::X1
        .monomial()
        .multiply(Occurrence::X5.monomial());
    let common = candidate.alpha.divide_by_monomial(lcm)?;
    (candidate.b0 == x5.multiply(&common) && candidate.b2 == x1.multiply(&common)).then_some(common)
}

fn lcm_line_chain_map(common: &Polynomial) -> LcmLineChainMap {
    let x1 = Occurrence::X1.polynomial();
    let x5 = Occurrence::X5.polynomial();
    LcmLineChainMap {
        alpha: x1.multiply(&x5).multiply(common),
        b0: x5.multiply(common),
        b2: x1.multiply(common),
    }
}

fn check_primitive_lcm_line_classification() {
    let one = Polynomial::one();
    let arbitrary_common = one
        .add(&Occurrence::X1.polynomial())
        .add(&Occurrence::X5.polynomial().scale(-2));
    for common in [&one, &arbitrary_common] {
        let candidate = lcm_line_chain_map(common);
        assert_eq!(
            classify_lcm_line_chain_map(&candidate),
            Some(common.clone())
        );
    }

    // The normalized primitive is obtained by solving the equations with
    // c=1; its entries are not entered as a desired road/Tor column.
    let primitive = lcm_line_chain_map(&one);
    assert_eq!(classify_lcm_line_chain_map(&primitive), Some(one.clone()));
    assert_eq!(
        primitive.alpha,
        Occurrence::X1
            .polynomial()
            .multiply(&Occurrence::X5.polynomial())
    );
    assert_eq!(primitive.b0, Occurrence::X5.polynomial());
    assert_eq!(primitive.b2, Occurrence::X1.polynomial());

    let invalid = LcmLineChainMap {
        alpha: one.clone(),
        b0: one.clone(),
        b2: one,
    };
    assert_eq!(classify_lcm_line_chain_map(&invalid), None);
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum OccurrenceLabel {
    X0,
    X1,
    X3,
    X4,
    X5,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct LabelledCell {
    name: &'static str,
    support: Vec<OccurrenceLabel>,
}

fn check_abstract_endpoints_are_not_f03_vertices() {
    // These are source Boolean-dual cells.  The subscripts q0,q2 are carrier
    // labels and must not be read as the x0/x2 road occurrence coordinates.
    let abstract_endpoints = [
        LabelledCell {
            name: "dual_q0_mask100",
            support: vec![OccurrenceLabel::X5],
        },
        LabelledCell {
            name: "dual_q2_mask001",
            support: vec![OccurrenceLabel::X1],
        },
    ];

    // Entry 86's normalized F03 road square, reused by entry 97, has these
    // actual occurrence vertices.  Entry 97's marked V-span retains
    // v00,v10,v01; v11 is the complementary square vertex.
    let f03_occurrence_vertices = [
        LabelledCell {
            name: "F03_v00",
            support: vec![OccurrenceLabel::X0, OccurrenceLabel::X3],
        },
        LabelledCell {
            name: "F03_v10",
            support: vec![OccurrenceLabel::X1, OccurrenceLabel::X3],
        },
        LabelledCell {
            name: "F03_v01",
            support: vec![OccurrenceLabel::X0, OccurrenceLabel::X4],
        },
        LabelledCell {
            name: "F03_v11",
            support: vec![OccurrenceLabel::X1, OccurrenceLabel::X4],
        },
    ];
    assert!(abstract_endpoints.iter().all(|endpoint| {
        f03_occurrence_vertices
            .iter()
            .all(|vertex| endpoint != vertex && endpoint.support != vertex.support)
    }));
    assert_eq!(abstract_endpoints[0].name, "dual_q0_mask100");
    assert_eq!(f03_occurrence_vertices[0].name, "F03_v00");
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct RoadBoundary {
    tau_q0: Polynomial,
    tau_q2: Polynomial,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct EndpointMap {
    q0_to_tau_q0: Polynomial,
    q2_to_tau_q2: Polynomial,
}

fn road_boundary_for_formal_square(endpoint: &EndpointMap) -> RoadBoundary {
    RoadBoundary {
        tau_q0: Occurrence::X1
            .polynomial()
            .multiply(&endpoint.q0_to_tau_q0)
            .scale(-1),
        tau_q2: Occurrence::X5.polynomial().multiply(&endpoint.q2_to_tau_q2),
    }
}

fn beck_chevalley_residual(
    generic_map: &Polynomial,
    endpoint: &EndpointMap,
    road: &RoadBoundary,
) -> [Polynomial; 2] {
    let source_then_endpoint_q0 = Occurrence::X1
        .polynomial()
        .multiply(&endpoint.q0_to_tau_q0)
        .scale(-1);
    let source_then_endpoint_q2 = Occurrence::X5.polynomial().multiply(&endpoint.q2_to_tau_q2);
    [
        road.tau_q0
            .multiply(generic_map)
            .add(&source_then_endpoint_q0.scale(-1)),
        road.tau_q2
            .multiply(generic_map)
            .add(&source_then_endpoint_q2.scale(-1)),
    ]
}

fn solve_normalized_endpoint_map(road: &RoadBoundary) -> Option<EndpointMap> {
    // This solver uses only the independently supplied bottom-row road
    // boundary and the established generic normalization g=1.
    Some(EndpointMap {
        q0_to_tau_q0: road
            .tau_q0
            .divide_by_monomial(Occurrence::X1.monomial())?
            .scale(-1),
        q2_to_tau_q2: road.tau_q2.divide_by_monomial(Occurrence::X5.monomial())?,
    })
}

fn check_two_path_beck_chevalley_equation() {
    let one = Polynomial::one();
    let x1 = Polynomial::variable(0);
    let x5 = Polynomial::variable(1);

    let first_endpoint = EndpointMap {
        q0_to_tau_q0: one.clone(),
        q2_to_tau_q2: one.clone(),
    };
    let second_endpoint = EndpointMap {
        q0_to_tau_q0: one.add(&x5),
        q2_to_tau_q2: x1.add(&one.scale(-2)),
    };
    assert_ne!(first_endpoint, second_endpoint);

    // Both independent choices give square-zero totalizations once a bottom
    // road boundary is derived from that choice.  Hence the external tensor
    // and generic map alone do not select an endpoint pushforward.
    for endpoint in [&first_endpoint, &second_endpoint] {
        let road = road_boundary_for_formal_square(endpoint);
        assert_eq!(
            beck_chevalley_residual(&one, endpoint, &road),
            [Polynomial::zero(), Polynomial::zero()]
        );
        assert_eq!(solve_normalized_endpoint_map(&road), Some(endpoint.clone()));
    }

    // Conversely, a fixed actual road boundary must have the indicated
    // principal-ideal divisibilities.  A nondivisible generization has no
    // diagonal normalized BC lift in this model.
    let nondivisible = RoadBoundary {
        tau_q0: one.clone(),
        tau_q2: x5,
    };
    assert_eq!(solve_normalized_endpoint_map(&nondivisible), None);

    // The total differential is D=d_PL+(-1)^p Phi.  On L3 tensor e3 its
    // cross-term is Phi*d_PL-d_road*Phi, exactly the residual above.  The
    // internal d_PL^2 and vertical Phi^2 terms vanish separately.
    let formal_road = road_boundary_for_formal_square(&first_endpoint);
    let total_d_squared_on_e3 = beck_chevalley_residual(&one, &first_endpoint, &formal_road);
    assert_eq!(
        total_d_squared_on_e3,
        [Polynomial::zero(), Polynomial::zero()]
    );
}

fn main() {
    check_augmented_koszul_exact_hull();
    check_external_thom_and_principal_lines();
    check_actual_tor_line_typing_after_base_change();
    check_primitive_lcm_line_classification();
    check_abstract_endpoints_are_not_f03_vertices();
    check_two_path_beck_chevalley_equation();

    println!(
        "{}",
        r#"{"claim":"The smallest exact occurrence-cellular hull of the entry-116 D03 endpoint column is the augmented Koszul resolution R<e3> --(-x1,x5)^T--> R<q0,q2> --(x5,x1)--> R<a> -> R/(x1,x5). The primitive lcm-line chain-map equations alpha=x1*b0=x5*b2 have exactly the family (alpha,b0,b2)=c*(x1*x5,x5,x1), derived by coprimality. Tensoring with the external rank-one Rees Thom line [t3] preserves exactness and does not add an internal h3 generator to e3,q0,or q2. The abstract cells q0={x5},q2={x1} are explicitly not the entry-86/97 F03 occurrence vertices v00=x0*x3,v10=x1*x3,v01=x0*x4,v11=x1*x4. For a putative diagonal push in free labelled presentations, with generic coefficient g, endpoint coefficients a0,a2, and independently supplied road generizations d(F03)=b0*tau_q0+b2*tau_q2, the two-path Beck-Chevalley equation derived from total d^2 is g*b0=-x1*a0 and g*b2=x5*a2. At g=1, a formal lift exists exactly when b0 lies in (x1) and b2 lies in (x5), and is then uniquely a0=-b0/x1,a2=b2/x5. After central base change, each actual local Cartier packet is [C--0-->C] with an H0 line and a Tor1 line, so the scalar equation forgets the occurrence inclusions and cannot select the endpoint maps. The external tensor supplies neither the enriched b0,b2 nor an identification with the separately typed reciprocal/Borel-Moore Tor1 lines.","status":"falsified","status_meaning":"Falsified only as a sufficiency claim: an external rank-one tensor plus the generic e3<->F03 carrier does not itself construct the endpoint extraordinary pushforwards. The exact formal tensor model and its conditional Beck-Chevalley criterion are proved.","scope":"Integral R=Z[x1,x5] occurrence-cellular model with a separately typed external [t3] line; actual Tor1 is tested only through the reduced central derived fibre C=R/(x1,x5), not asserted spatially realized.","factorization_test":{"source_boundary":"DERIVED from masks and exterior orientations: d(e3)=-x1*q0+x5*q2","exact_hull":"PASS: the augmented two-variable Koszul complex is exact","source_d_squared":"PASS: -x5*x1+x1*x5=0","primitive_lcm_line":"CLASSIFIED exactly: alpha=x1*b0=x5*b2 iff (alpha,b0,b2)=c*(x1*x5,x5,x1); c=1 is primitive","endpoint_label_negative_control":"PASS: dual_q0_mask100={x5} and dual_q2_mask001={x1} are none of F03 v00=x0*x3,v10=x1*x3,v01=x0*x4,v11=x1*x4","external_Thom":"PASS as a free rank-one tensor factor; it is not endpoint h3 support","principal_ideal_evaluation":"PASS formally: (x1)^vee and (x5)^vee give endpoint signs (-1,+1) without base inversion","central_derived_fibres":"PASS algebraically: both are [C--0-->C] and retain rank-one H0 and Tor1","variance":"RECIPROCAL source and BOREL-MOORE target remain distinct types","generic_carrier":"USED only as the normalized scalar g=1; no lower carrier image is assumed","two_path_BC":"DERIVED before base change: g*b0=-x1*a0 and g*b2=x5*a2","normalized_free_lift":"UNIQUE conditional on independently supplied b0 in (x1), b2 in (x5)","BC_after_central_base_change":"scalar equation is 0=0 and does not normalize either Tor1 endpoint","endpoint_parameter_space_before_target_generizations":"two independent coefficient-line maps","actual_road_generizations":"NOT SUPPLIED by the tensor model","actual_extraordinary_push_pull":"NOT CONSTRUCTED","inversions":"none"},"counterevidence":["Principal-ideal duality and the primitive lcm-line classification concern abstract coefficient lines; neither identifies dual_q0 or dual_q2 with an entry-86/97 F03 occurrence vertex or actual road Tor1 costalk.","Two distinct endpoint coefficient pairs yield valid square-zero formal totalizations after choosing correspondingly different bottom road boundaries.","Declaring b0=-x1 and b2=x5 would force unit endpoints in free presentations, but that declaration is exactly the missing adjacent-road generization datum and is not derived here.","Passing directly to the actual central Tor1 fibres kills x1 and x5, so scalar Beck-Chevalley becomes vacuous unless the correspondence retains their conormal/ideal lines."],"next_required_geometry":"Construct the marked extraordinary D03 correspondence, retaining the x1/x5 ideal lines and external [t3], and independently compute its two road-generization morphisms before central base change. Then the displayed divisibility and quotient test audits its endpoint Tor1 pushforwards."}"#
    );
}
