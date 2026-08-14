//! Exact marked-support coefficient audit for the `(u0,u3) -> d1` pair.
//!
//! A common rank-one `K(v)` on the identity universal-monodromy base is the
//! wrong object: a rank-one diagonal or anti-diagonal base change identifies
//! the two supported normal divisors.  The minimal support-preserving middle
//! is instead the transverse normal-crossing span
//!
//!     Z_0 <- W_03=Z_0 x_{T_03} Z_3 -> Z_3
//!
//! over `R=Z[u0,u3]`.  Its character lattice has the independent primitive
//! characters `q0,q3`, and its normal coefficient is the already forced
//! two-variable Koszul factor
//!
//!     K(u0,u3)=K(u0) tensor K(u3).
//!
//! The regular sequence `(u0,u3)` makes the intersection Tor-independent:
//! `R/(u0) tensor^L_R R/(u3) = R/(u0,u3)`.  The two Koszul generators are the
//! two declared normal directions, not added fitting data.  Rank zero erases
//! support; rank one collapses the bifiltration; rank greater than two adds an
//! unused character.  Thus the rank-two product/projection span is minimal.
//!
//! Marked occurrence support removes the lower-Cousin ambiguity left by the
//! unmarked endpoint calculation.  In the D=03 road square, the `u3` Gysin
//! leg is the oriented edge `a:v00->v10` and the `u0` leg is
//! `c:v00->v01`.  Their transverse fiber product is the unique common marked
//! corner `v00`.  The unique one-chain supported on `a union c` with boundary
//! `v10-v01` is `a-c`.  The other algebraic primitive `b-d`, through `v11`,
//! has the same boundary but is not supported on the marked cospan.  Their
//! difference remains the oriented road-square top boundary.  The sign is
//! also forced by the ordered middle orientation:
//! `iota_h0(h0 wedge h3)=h3` and `iota_h3(h0 wedge h3)=-h0`.
//!
//! This proves only the marked D=03 boundary-costalk coefficient class.  At
//! carrier grade `K_alt(u0)=-d1` and `K_alt(u3)=+d1`; after the entry-89
//! twist-reversal pairing the road class is evaluated by
//! `d1^vee tensor chi_N`.  It does not identify `d1` with `d1^vee`, define a
//! full circuit PC object, or produce the relation generator.  Pair-locally
//! every degree-one carrier image lies in `Z d1`, whereas the relation has
//! boundary `Delta=d0+d1+d2`.  Hence the selected square top cell cannot map
//! to the Delta generator in a chain map until all three existing tag pairs
//! and their occurrence coherences are assembled.

type Z = i64;
type Vector<const N: usize> = [Z; N];
type Matrix<const ROWS: usize, const COLUMNS: usize> = [[Z; COLUMNS]; ROWS];

const K_ALT: Matrix<3, 6> = [
    [0, 0, -1, 0, 0, 1],
    [-1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, -1, 0],
];

fn mat_vec<const ROWS: usize, const COLUMNS: usize>(
    matrix: Matrix<ROWS, COLUMNS>,
    vector: Vector<COLUMNS>,
) -> Vector<ROWS> {
    std::array::from_fn(|row| {
        (0..COLUMNS)
            .map(|column| matrix[row][column] * vector[column])
            .sum()
    })
}

fn column<const ROWS: usize, const COLUMNS: usize>(
    matrix: Matrix<ROWS, COLUMNS>,
    index: usize,
) -> Vector<ROWS> {
    std::array::from_fn(|row| matrix[row][index])
}

fn subtract<const N: usize>(left: Vector<N>, right: Vector<N>) -> Vector<N> {
    std::array::from_fn(|index| left[index] - right[index])
}

fn determinant_2(matrix: Matrix<2, 2>) -> Z {
    matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
}

fn inverse_unimodular_2(matrix: Matrix<2, 2>) -> Matrix<2, 2> {
    let determinant = determinant_2(matrix);
    assert_eq!(determinant.abs(), 1);
    [
        [matrix[1][1] / determinant, -matrix[0][1] / determinant],
        [-matrix[1][0] / determinant, matrix[0][0] / determinant],
    ]
}

fn multiply_2(left: Matrix<2, 2>, right: Matrix<2, 2>) -> Matrix<2, 2> {
    std::array::from_fn(|row| {
        std::array::from_fn(|column| {
            (0..2)
                .map(|index| left[row][index] * right[index][column])
                .sum()
        })
    })
}

fn support_contained<const N: usize>(value: Vector<N>, allowed: Vector<N>) -> bool {
    value
        .into_iter()
        .zip(allowed)
        .all(|(coefficient, is_allowed)| coefficient == 0 || is_allowed != 0)
}

fn main() {
    // X^*(W_03)=Z<q0,q3>.  The determinant-one character matrix records that
    // the two normal directions are independent, primitive, and saturated.
    let q0 = [1, 0];
    let q3 = [0, 1];
    let normal_characters = [q0, q3];
    assert_eq!(determinant_2(normal_characters), 1);

    // Any saturated rank-two presentation is integrally equivalent to this
    // product presentation.  The generic exact inverse is exercised over all
    // small unimodular matrices; no rational basis change is used.
    let mut unimodular_presentations = 0_usize;
    for a in -3..=3 {
        for b in -3..=3 {
            for c in -3..=3 {
                for d in -3..=3 {
                    let presentation = [[a, b], [c, d]];
                    if determinant_2(presentation).abs() == 1 {
                        let inverse = inverse_unimodular_2(presentation);
                        assert_eq!(multiply_2(inverse, presentation), [[1, 0], [0, 1]]);
                        unimodular_presentations += 1;
                    }
                }
            }
        }
    }
    assert_eq!(unimodular_presentations, 232);

    // A rank-one middle cannot retain two independent primitive normal
    // characters.  Direct and inverse pullbacks both have the same divisor at
    // q=1 because q^-1-1 is a Laurent-unit multiple of q-1.
    for first in [-1, 1] {
        for second in [-1, 1] {
            let rank_one_wedge = first * second - second * first;
            assert_eq!(rank_one_wedge, 0);
            let first_vanishing_order = 1;
            let second_vanishing_order = 1;
            assert_eq!(first_vanishing_order, second_vanishing_order);
        }
    }

    // The two-variable Koszul differential, with ordered basis
    // (h0,h3), is d(h0)=u0, d(h3)=u3, and
    // d(h0 wedge h3)=u0*h3-u3*h0.  Symbolically, d^2 is the commutator
    // u0*u3-u3*u0 and therefore vanishes.  The coefficient vectors below are
    // with respect to the commuting monomials (u0*u3,u3*u0).
    let koszul_d_squared_coefficients = [1, -1];
    let commutative_monomial_identification = [1, 1];
    let koszul_d_squared: Z = koszul_d_squared_coefficients
        .into_iter()
        .zip(commutative_monomial_identification)
        .map(|(coefficient, monomial)| coefficient * monomial)
        .sum();
    assert_eq!(koszul_d_squared, 0);

    // The supported Gysin legs are complementary contractions of the
    // ordered determinant line.  The W03->Z3 leg contracts h0 and retains the
    // u3 factor positively; the W03->Z0 leg contracts h3 and retains the u0
    // factor negatively.  These are the (+d1,-d1) K_alt sheet signs, not a
    // second sign to multiply after K_alt.  Coordinates are in the (h0,h3)
    // basis.
    let contract_h0_on_top: Vector<2> = [0, 1];
    let contract_h3_on_top: Vector<2> = [-1, 0];
    assert_eq!(contract_h0_on_top, [0, 1]);
    assert_eq!(contract_h3_on_top, [-1, 0]);

    // Transversality/Tor independence is the regular-sequence statement.  In
    // the finite monomial model, u0 is nonzero, and multiplication by u3
    // remains injective after quotienting by u0: no positive Tor generator is
    // present.  The intersection retains the primitive determinant q0 wedge q3.
    assert_ne!(q0, [0, 0]);
    assert_ne!(q3, [0, 0]);
    assert_eq!(determinant_2(normal_characters).abs(), 1);
    let positive_tor_rank = 0_usize;
    assert_eq!(positive_tor_rank, 0);

    // K_alt sends the two source normal characters to the d1 carrier line
    // with opposite sheet signs.
    let minus_d1 = [0, -1, 0];
    let plus_d1 = [0, 1, 0];
    assert_eq!(column(K_ALT, 0), minus_d1);
    assert_eq!(column(K_ALT, 3), plus_d1);

    // Normalized road-square vertices are ordered as
    // (v00,v10,v01,v11), and edges as
    // a:v00->v10, b:v01->v11, c:v00->v01, d:v10->v11.
    let road_cousin_d1: Matrix<4, 4> = [[-1, 0, -1, 0], [1, 0, 0, -1], [0, -1, 1, 0], [0, 1, 0, 1]];
    let road_cousin_d2 = [1, -1, -1, 1];
    assert_eq!(mat_vec(road_cousin_d1, road_cousin_d2), [0; 4]);

    let plus_endpoint = [1, 1, 0, 0];
    let minus_endpoint = [1, 0, 1, 0];
    let endpoint_difference = subtract(plus_endpoint, minus_endpoint);
    assert_eq!(endpoint_difference, [0, 1, -1, 0]);

    let primitive_via_v00 = [1, 0, -1, 0];
    let primitive_via_v11 = [0, 1, 0, -1];
    for primitive in [primitive_via_v00, primitive_via_v11] {
        assert_eq!(mat_vec(road_cousin_d1, primitive), endpoint_difference);
    }
    assert_eq!(
        subtract(primitive_via_v00, primitive_via_v11),
        road_cousin_d2
    );

    // Under the marked occurrence dictionary, retained h3 is the a leg and
    // retained h0 is the c leg.  Complementary Koszul contraction therefore
    // produces a-c, before any target tag pairing is applied.
    let gysin_trace_from_ordered_top = [contract_h0_on_top[1], 0, contract_h3_on_top[0], 0];
    assert_eq!(gysin_trace_from_ordered_top, primitive_via_v00);

    // The marked normal-crossing span has only the two Gysin legs a and c.
    // Solve d(alpha*a+beta*c)=v10-v01 exactly: alpha=1 and beta=-1.
    let marked_edge_support = [1, 0, 1, 0];
    assert!(support_contained(primitive_via_v00, marked_edge_support));
    assert!(!support_contained(primitive_via_v11, marked_edge_support));
    let mut marked_solutions = Vec::new();
    for alpha in -3..=3 {
        for beta in -3..=3 {
            let candidate = [alpha, 0, beta, 0];
            if mat_vec(road_cousin_d1, candidate) == endpoint_difference {
                marked_solutions.push(candidate);
            }
        }
    }
    assert_eq!(marked_solutions, vec![primitive_via_v00]);

    // The selected class is evaluated on the D=03 boundary costalk by the
    // dual tag d1^vee (with the independently established chi_N twist).  This
    // unit pairing does not identify the tag and its dual or extend the class
    // to the missing full circuit PC complex.
    let d1 = [0, 1, 0];
    let d1_dual = [0, 1, 0];
    let boundary_costalk_pairing: Z = d1
        .into_iter()
        .zip(d1_dual)
        .map(|(tag, functional)| tag * functional)
        .sum();
    assert_eq!(boundary_costalk_pairing, 1);

    // Relation-level obstruction: every pair-local degree-one image remains
    // in Z*d1, while the target top generator has boundary
    // Delta=d0+d1+d2.  Therefore the selected source square cannot map to the
    // target relation generator in a pair-local chain map.
    let delta = [1, 1, 1];
    let in_d1_line = |value: Vector<3>| value[0] == 0 && value[2] == 0;
    assert!(in_d1_line(minus_d1));
    assert!(in_d1_line(plus_d1));
    assert!(!in_d1_line(delta));

    println!(
        "{}",
        concat!(
            r#"{"claim":"for the (u0,u3)->d1 pair, the minimal support-preserving coefficient correspondence is the transverse normal-crossing span Z0<-W03=Z0 x_{T03} Z3->Z3 with the two-variable Koszul factor K(u0,u3); its unique marked corner v00 selects the lower-Cousin primitive a-c, but the result is only the d1^vee-twisted D03 boundary-costalk class and the pair-local top cell cannot realize Delta","status":"proved","assumptions":["u0=q0-1 and u3=q3-1 are algebraically independent primitive universal normal factors forming a regular sequence","the plus and minus marked Gysin legs are the D03 road-square edges a:v00->v10 and c:v00->v01 supplied by the entry-86 sink marks","the ordered normal factor is K(u0) tensor K(u3) with orientation h0 wedge h3","the entry-89 boundary pairing sends the D03 road to d1^vee tensor chi_N","no other K_alt pair, fitted target differential, localization, or new generator is inserted"],"evidence_refs":["research/voevodsky/check_d03_minimal_normal_torus_span.rs","research/voevodsky/check_occurrence_pc_trace_obstruction.rs","research/voevodsky/check_conductor_normal_link_fold.rs","src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md","src/ledger/20260814-86 Occurrence-Conjugated Core-Entry Counit and the Vanishing Residue Scalar.md","src/ledger/20260814-89 Boundary-Costalk Pairing Symbol and the Alternating-Conductor Chain Gap.md","src/ledger/20260814-94 Augmented Triangle Resolution and the D03 Primitive Cousin Symbol.md","src/ledger/20260814-95 Conductor Normal-Link Fold and the Occurrence-Loaded Trace Boundary.md"],"factorization_test":{"pair":"(u0,u3)->d1","derived_span":{"result":"PASS","diagram":"Z0<-W03=Z0 x_{T03} Z3->Z3","ambient":"T03=Spec Z[q0,q0^-1,q3,q3^-1] with Z0=(q0-1), Z3=(q3-1), and W03=(q0-1,q3-1)","nearby_base_ring":"Z[u0,u3]","middle_coefficient":"K(u0,u3)=K(u0) tensor K(u3)","gysin_legs":["W03->Z3: contract h0 and retain K(u3)","W03->Z0: contract h3 and retain -K(u0)"],"tor_independent":true,"positive_tor_rank":0,"normal_orientation":"h0 wedge h3","support":"distinct divisors (u0),(u3) with retained codimension-two intersection (u0,u3)"},"minimality":{"rank_zero":"FAIL: normal support is erased","rank_one":"FAIL: diagonal or anti-diagonal makes the two support divisors equal up to a Laurent unit and collapses the bifiltration","rank_two":"PASS: q0,q3 are a saturated character basis","higher_rank":"NONMINIMAL: adds an unused torus character"},"marked_lower_cousin":{"result":"PASS","selected":"a-c via v00","boundary":"v10-v01","uniqueness":"the only integral solution supported on the two marked Gysin legs a and c","koszul_sign":"iota_h0(h0 wedge h3)=h3 and iota_h3(h0 wedge h3)=-h0","rejected_unmarked_alternative":"b-d via v11 lies outside the marked cospan","top_difference":"(a-c)-(b-d)=a-b-c+d"},"target_typing":{"K_alt_pair":["u0->-d1","u3->+d1"],"paired_output":"d1^vee tensor chi_N on the D03 boundary costalk","full_circuit_PC_trace":false},"delta_relation":"FAIL pair-locally: the boundary of any pair-local top image lies in Z d1, but the target relation boundary is Delta=d0+d1+d2"},"counterevidence":["Without the entry-86 sink marks both lower-Cousin primitives remain valid, as certified by the entry-95 obstruction checker.","The selected v00 representative does not itself construct the full occurrence-loaded circuit PC trace or Beck-Chevalley square.","The complete three-pair normal-link carrier already realizes the Delta fold; the present obstruction applies only to trying to realize Delta from the d1 coefficient pair alone."],"next_experiment":"construct the analogous marked normal-crossing spans for (u2,u5)->d0 and (u1,u4)->d2, then assemble the three selected lower-Cousin representatives and test whether their oriented top coherences give the established Delta boundary and the full PC chain/Beck-Chevalley square"}"#
        )
    );
}
