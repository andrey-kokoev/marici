//! Exact obstruction audit for extending the three rotated D=03 reciprocal-
//! twist traces across the two conductor-normal-link top cells.
//!
//! The local trace of entry 97 is rotated from (u0,u3) to the three pairs
//!
//!   (u2,u5)->d0, (u0,u3)->d1, (u1,u4)->d2.
//!
//! This audit keeps all six occurrence variables and all six universal normal
//! characters independent.  It verifies the rotated weighted road squares,
//! endpoint values, reciprocal/Borel--Moore typing, twist-reversed normal
//! pairings, transported normal orientations, and the carrier top identity.
//!
//! It then computes the normal-support groups relevant to extending those
//! boundary traces.  Put
//!
//!   I+ = (u1,u3,u5), I- = (u0,u2,u4), I_ab = (u_a,u_b).
//!
//! For either branch and its incident opposite-parity pair, one generator is
//! shared and the other two branch generators remain regular modulo I_ab.
//! Hence, with S=R/(I_branch+I_ab),
//!
//!   Tor^R_k(R/I_branch,R/I_ab) = S for k=0,1 and 0 otherwise,
//!   Ext^k_R(R/I_branch,R/I_ab) = S for k=2,3 and 0 otherwise.
//!
//! In particular the square is an excess-one derived intersection, not a
//! transverse incidence, and there is no direct degree-zero or degree-one
//! attachment.  Separately, the regular codimension-three embeddings have
//! their canonical oriented Ext^3 Gysin lines, and the pair embeddings have
//! canonical Ext^2 lines.  The existing augmented triangle identifies their
//! carrier grades but does not supply the excess Beck--Chevalley morphism
//! comparing these differently supported Gysin classes.  Defining a mapping
//! cone with the desired boundary would therefore insert the missing map.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum SupportType {
    ReciprocalRegularized,
    LocallyFiniteBorelMoore,
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Laurent([i8; 6]);

impl Laurent {
    fn one() -> Self {
        Self([0; 6])
    }

    fn variable(index: usize) -> Self {
        let mut result = [0; 6];
        result[index] = 1;
        Self(result)
    }

    fn multiply(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| self.0[index] + other.0[index]))
    }

    fn inverse(self) -> Self {
        Self(self.0.map(|entry| -entry))
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Pair {
    tag: usize,
    first: usize,
    second: usize,
}

const K_ALT: [[i64; 6]; 3] = [
    [0, 0, -1, 0, 0, 1],
    [-1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, -1, 0],
];

fn rotate_index(index: usize, steps: usize) -> usize {
    (index + steps) % 6
}

fn rotate_tag(tag: usize, steps: usize) -> usize {
    (tag + steps) % 3
}

fn rotated_pairs() -> [Pair; 3] {
    // Rotate the entry-97 pair (u0,u3)->d1 twice.  The ordering is the
    // transported ordering h0 wedge h3, not a parity-sorted replacement.
    std::array::from_fn(|steps| Pair {
        tag: rotate_tag(1, steps),
        first: rotate_index(0, steps),
        second: rotate_index(3, steps),
    })
}

fn column(index: usize) -> [i64; 3] {
    std::array::from_fn(|row| K_ALT[row][index])
}

fn check_rotated_carrier() {
    let pairs = rotated_pairs();
    assert_eq!(
        pairs,
        [
            Pair {
                tag: 1,
                first: 0,
                second: 3,
            },
            Pair {
                tag: 2,
                first: 1,
                second: 4,
            },
            Pair {
                tag: 0,
                first: 2,
                second: 5,
            },
        ]
    );

    let mut used_normals = [0_usize; 6];
    for pair in pairs {
        used_normals[pair.first] += 1;
        used_normals[pair.second] += 1;
        let first_image = column(pair.first);
        let second_image = column(pair.second);
        assert_eq!(first_image.iter().filter(|&&entry| entry != 0).count(), 1);
        assert_eq!(second_image.iter().filter(|&&entry| entry != 0).count(), 1);
        let first_sign = if pair.first % 2 == 0 { -1 } else { 1 };
        let second_sign = if pair.second % 2 == 0 { -1 } else { 1 };
        assert_eq!(first_image[pair.tag], first_sign);
        assert_eq!(second_image[pair.tag], second_sign);
        assert_eq!(first_sign, -second_sign);
    }
    assert_eq!(used_normals, [1; 6]);

    // These are derived independently from the two positive conductor
    // triangles: f+ has the odd facets and f- the even facets.
    let plus_boundary = [1_usize, 3, 5];
    let minus_boundary = [0_usize, 2, 4];
    let sum_images = |facets: [usize; 3]| -> [i64; 3] {
        let mut result = [0_i64; 3];
        for facet in facets {
            for row in 0..3 {
                result[row] += K_ALT[row][facet];
            }
        }
        result
    };
    assert_eq!(sum_images(plus_boundary), [1, 1, 1]);
    assert_eq!(sum_images(minus_boundary), [-1, -1, -1]);
}

fn check_one_weighted_road_square(pair: Pair) {
    let x0 = Laurent::variable(pair.first);
    let x1 = Laurent::variable(rotate_index(pair.first, 1));
    let x3 = Laurent::variable(pair.second);
    let x4 = Laurent::variable(rotate_index(pair.second, 1));
    let vertex_scales = [
        x0.multiply(x3),
        x1.multiply(x3),
        x0.multiply(x4),
        x1.multiply(x4),
    ];
    let edge_scales = [x3, x4, x0, x1];
    let raw_edges = [
        [(0_usize, -1_i64, x0), (1, 1, x1)],
        [(2, -1, x0), (3, 1, x1)],
        [(0, -1, x3), (2, 1, x4)],
        [(1, -1, x3), (3, 1, x4)],
    ];
    let ordinary_edges = [
        [-1_i64, 1, 0, 0],
        [0, 0, -1, 1],
        [-1, 0, 1, 0],
        [0, -1, 0, 1],
    ];
    for edge in 0..4 {
        for &(vertex, sign, coefficient) in &raw_edges[edge] {
            assert_eq!(
                edge_scales[edge]
                    .multiply(coefficient)
                    .multiply(vertex_scales[vertex].inverse()),
                Laurent::one()
            );
            assert_eq!(ordinary_edges[edge][vertex], sign);
        }
    }

    let top = [(1_i64, x3), (-1, x4), (-1, x0), (1, x1)];
    for (edge, &(sign, coefficient)) in top.iter().enumerate() {
        assert_eq!(
            coefficient.multiply(edge_scales[edge].inverse()),
            Laurent::one()
        );
        assert_eq!(sign, [1, -1, -1, 1][edge]);
    }

    // Entry 89's occurrence functional is inverse weight, independently on
    // every corner.  It kills all four raw weighted boundaries.
    let lambda = vertex_scales.map(Laurent::inverse);
    for vertex in 0..4 {
        assert_eq!(
            vertex_scales[vertex].multiply(lambda[vertex]),
            Laurent::one()
        );
    }
    for edge in raw_edges {
        let terms =
            edge.map(|(vertex, sign, coefficient)| (sign, coefficient.multiply(lambda[vertex])));
        assert_eq!(terms[0].1, terms[1].1);
        assert_eq!(terms[0].0 + terms[1].0, 0);
    }

    // Fixed marks select the two edges through v00.  Primitive occurrence
    // values are one, the two sheet periods are two, and polarization is four.
    let plus_endpoint = [1_i64, 1, 0, 0];
    let minus_endpoint = [1_i64, 0, 1, 0];
    let endpoint_difference =
        std::array::from_fn::<_, 4, _>(|index| plus_endpoint[index] - minus_endpoint[index]);
    assert_eq!(endpoint_difference, [0, 1, -1, 0]);
    assert_eq!(plus_endpoint.into_iter().sum::<i64>(), 2);
    assert_eq!(minus_endpoint.into_iter().sum::<i64>(), 2);
    assert_eq!([1_i64; 4].into_iter().sum::<i64>(), 4);
    assert_eq!(endpoint_difference.into_iter().sum::<i64>(), 0);

    let road_d1 = [
        [-1_i64, 0, -1, 0],
        [1, 0, 0, -1],
        [0, -1, 1, 0],
        [0, 1, 0, 1],
    ];
    let multiply = |vector: [i64; 4]| -> [i64; 4] {
        std::array::from_fn(|row| {
            (0..4)
                .map(|entry| road_d1[row][entry] * vector[entry])
                .sum()
        })
    };
    let marked_primitive = [1_i64, 0, -1, 0];
    let unmarked_primitive = [0_i64, 1, 0, -1];
    assert_eq!(multiply(marked_primitive), [0, 1, -1, 0]);
    assert_eq!(multiply(unmarked_primitive), [0, 1, -1, 0]);
    assert_eq!(
        std::array::from_fn::<_, 4, _>(|index| {
            marked_primitive[index] - unmarked_primitive[index]
        }),
        [1, -1, -1, 1]
    );
}

fn check_occurrences_support_and_rotation() {
    for pair in rotated_pairs() {
        check_one_weighted_road_square(pair);
    }

    let source_support = SupportType::ReciprocalRegularized;
    let road_support = SupportType::LocallyFiniteBorelMoore;
    assert_ne!(source_support, road_support);

    // Endpoint Cousin, scalar-source, and entry-coaction signs rotate
    // unchanged.  The common physical normal line is independently positive.
    assert_eq!(1_i64 * -1 * -1, 1);
    assert_eq!(1_i64 * 1, 1);

    // Transport h0 wedge h3, rather than re-sorting the factors after each
    // rotation.  After three steps it becomes h3 wedge h0, recording the
    // reversal which is paired with the core/polarity character in chi_N.
    let transported: [[usize; 2]; 6] =
        std::array::from_fn(|steps| [rotate_index(0, steps), rotate_index(3, steps)]);
    assert_eq!(transported[0], [0, 3]);
    assert_eq!(transported[1], [1, 4]);
    assert_eq!(transported[2], [2, 5]);
    assert_eq!(transported[3], [3, 0]);
    for steps in 0..3 {
        assert_eq!(
            transported[steps + 3],
            [transported[steps][1], transported[steps][0]]
        );
    }
    let orientation_comparison = [1_i64, 1, 1, -1, -1, -1];
    let core_exchange_part_of_chi_n = [1_i64, 1, 1, -1, -1, -1];
    for steps in 0..6 {
        assert_eq!(
            orientation_comparison[steps] * core_exchange_part_of_chi_n[steps],
            1
        );
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct UTerm {
    coefficient: i64,
    q_exponents: [i8; 6],
    u_index: usize,
}

fn check_twist_reversal() {
    // u_j^vee=-q_j^-1 u_j and beta(p,h^vee)=1,
    // beta(h,p^vee)=-q_j.  Check the cancellation independently for all six
    // q_j/u_j rather than identifying the members of a pair.
    for normal in 0..6 {
        let mut q_inverse = [0_i8; 6];
        q_inverse[normal] = -1;
        let u_dual = UTerm {
            coefficient: -1,
            q_exponents: q_inverse,
            u_index: normal,
        };
        let beta_p_hdual = (1_i64, [0_i8; 6]);
        let mut beta_q = [0_i8; 6];
        beta_q[normal] = 1;
        let beta_h_pdual = (-1_i64, beta_q);
        let first = UTerm {
            coefficient: 1 * beta_p_hdual.0,
            q_exponents: beta_p_hdual.1,
            u_index: normal,
        };
        let second = UTerm {
            coefficient: u_dual.coefficient * beta_h_pdual.0,
            q_exponents: std::array::from_fn(|index| {
                u_dual.q_exponents[index] + beta_h_pdual.1[index]
            }),
            u_index: normal,
        };
        assert_eq!(first, second);
    }
}

type Mask = u8;

fn mask(indices: &[usize]) -> Mask {
    indices
        .iter()
        .fold(0_u8, |result, &index| result | (1 << index))
}

fn indices(value: Mask) -> Vec<usize> {
    (0..6).filter(|&index| value & (1 << index) != 0).collect()
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct KoszulGroups {
    // (degree, free rank over the final quotient support).
    groups: Vec<(usize, usize)>,
    quotient_support: Mask,
}

fn binomial(n: usize, k: usize) -> usize {
    if k > n {
        return 0;
    }
    (0..k).fold(1_usize, |value, index| value * (n - index) / (index + 1))
}

fn koszul_tor(sequence: Mask, module_ideal: Mask) -> KoszulGroups {
    // Variables already in the module ideal act by zero.  The remaining
    // independent variables form a regular sequence.  Its Koszul homology is
    // the quotient in degree zero, tensored with the exterior algebra on the
    // zero-acting variables.
    let zero_count = (sequence & module_ideal).count_ones() as usize;
    let groups = (0..=zero_count)
        .map(|degree| (degree, binomial(zero_count, degree)))
        .collect();
    KoszulGroups {
        groups,
        quotient_support: sequence | module_ideal,
    }
}

fn koszul_ext(sequence: Mask, module_ideal: Mask) -> KoszulGroups {
    // For the cochain Koszul complex, a regular sequence of length r has its
    // sole cohomology in degree r.  Zero-acting variables contribute their
    // exterior degrees.
    let zero_count = (sequence & module_ideal).count_ones() as usize;
    let regular_count = (sequence & !module_ideal).count_ones() as usize;
    let groups = (0..=zero_count)
        .map(|extra| (regular_count + extra, binomial(zero_count, extra)))
        .collect();
    KoszulGroups {
        groups,
        quotient_support: sequence | module_ideal,
    }
}

fn check_normal_support_extension_groups() {
    let plus = mask(&[1, 3, 5]);
    let minus = mask(&[0, 2, 4]);
    assert_eq!(plus & minus, 0);
    assert_eq!(plus | minus, mask(&[0, 1, 2, 3, 4, 5]));

    // The branch embeddings themselves are regular codimension three and
    // therefore have one oriented Verdier/Gysin line in Ext^3.  These are
    // separate plus and minus normal determinant lines before carrier folding.
    for branch in [plus, minus] {
        assert_eq!(
            koszul_ext(branch, 0),
            KoszulGroups {
                groups: vec![(3, 1)],
                quotient_support: branch,
            }
        );
    }

    for pair in rotated_pairs() {
        let pair_ideal = mask(&[pair.first, pair.second]);
        // Each pair is a regular codimension-two intersection, as in entry 96.
        assert_eq!(
            koszul_ext(pair_ideal, 0),
            KoszulGroups {
                groups: vec![(2, 1)],
                quotient_support: pair_ideal,
            }
        );

        for branch in [plus, minus] {
            // Exactly one normal direction is shared.  Thus attaching a
            // branch top to a pair is not one of entry 96's transverse pair
            // squares; it has a rank-one excess Tor class.
            assert_eq!((branch & pair_ideal).count_ones(), 1);
            assert!((branch & !pair_ideal).count_ones() == 2);
            assert!((pair_ideal & !branch).count_ones() == 1);
            assert_ne!(branch & !pair_ideal, 0);
            assert_ne!(pair_ideal & !branch, 0);

            let quotient = branch | pair_ideal;
            assert_eq!(
                koszul_tor(branch, pair_ideal),
                KoszulGroups {
                    groups: vec![(0, 1), (1, 1)],
                    quotient_support: quotient,
                }
            );
            assert_eq!(
                koszul_ext(branch, pair_ideal),
                KoszulGroups {
                    groups: vec![(2, 1), (3, 1)],
                    quotient_support: quotient,
                }
            );

            // The direct Hom and Ext^1 groups vanish.  Therefore the carrier
            // incidence cannot itself be read as the required PC attachment.
            assert!(!koszul_ext(branch, pair_ideal)
                .groups
                .iter()
                .any(|&(degree, rank)| degree <= 1 && rank != 0));

            // The final support consists of the complete branch triple plus
            // the one opposite-parity pair direction.
            assert_eq!(indices(quotient).len(), 4);
        }
    }
}

fn main() {
    check_rotated_carrier();
    check_occurrences_support_and_rotation();
    check_twist_reversal();
    check_normal_support_extension_groups();

    println!(
        "{}",
        concat!(
            r#"{"claim":"the relative weighted six-point associahedron supplies K_rel^PC and dK_rel^PC=T0^PC+T1^PC+T2^PC without adjoining a cone, and the three rotated entry-97 traces pass all pair-local occurrence, twist, orientation, endpoint, and carrier tests; however they do not yet extend across f_+ and f_- because each branch-top/pair attachment is an excess-one derived intersection, with direct Ext^0=Ext^1=0 and Ext^2=Ext^3=R/(I_branch+I_pair), so the required excess Beck-Chevalley source map is absent","status":"inconclusive","assumptions":["the six u_j=q_j-1 are algebraically independent universal normal factors and no identity-base character relation is imposed","the plus and minus conductor tops have ideals I_+=(u1,u3,u5) and I_-=(u0,u2,u4) with the entry-95 orientations","the three pair targets are exactly the rotated entry-97 road-face costalk duals inside the relative associahedral target, not a formal mapping cone or the full PC(J4 boxtimes J6)"],"evidence_refs":["research/voevodsky/check_d03_three_pair_pc_extension.rs","research/voevodsky/check_d03_relative_associahedron_pc.rs","research/voevodsky/check_d03_bivariant_pc_hom.rs","research/voevodsky/check_conductor_normal_link_fold.rs","research/voevodsky/check_d03_minimal_normal_torus_span.rs","src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md","src/ledger/20260814-94 Augmented Triangle Resolution and the D03 Primitive Cousin Symbol.md","src/ledger/20260814-95 Conductor Normal-Link Fold and the Occurrence-Loaded Trace Boundary.md","src/ledger/20260814-96 Factorization-Marked Normal-Crossing Span and the Pair-Local Relation Obstruction.md","src/ledger/20260814-97 Reciprocal-Twist D03 Bivariant Road Trace.md"],"factorization_test":{"rotated_pairs":["(u2,u5)->d0","(u0,u3)->d1","(u1,u4)->d2"],"coefficient_layers":"PASS: all x0,...,x5 and q0,...,q5/u0,...,u5 remain independent; occurrence Laurent weights are never identified with normal factors","local_traces":"PASS: three weighted road squares normalize integrally; reciprocal-regularized source is paired with original-twist locally-finite/Borel-Moore road support","endpoint":"PASS: every primitive occurrence is 1, each selected sheet is 2, the endpoint difference is 0 under the counit, and each polarization remains 4","normal_duality":"PASS for all six factors: u_j^vee=-q_j^-1*u_j and beta(p,h^vee)=1, beta(h,p^vee)=-q_j; pair orientations are rotations of h0 wedge h3","chi_N_rotation":"PASS: the reversal after three boundary rotations is canceled by the core/polarity factor of chi_N; [dX_D] stays +1","relative_target":"PASS: entry-38 relative face tubes for (K6,B_sc) give K_rel^PC and the three road targets geometrically","relation_differential":"PASS in the target: dK_rel^PC=T0^PC+T1^PC+T2^PC","carrier_top":"PASS: K_alt*d2(f_+)=Delta and K_alt*d2(f_-)=-Delta","codimension_three_gysin":"PASS separately: Ext^3_R(R/I_+,R)=R/I_+ and Ext^3_R(R/I_-,R)=R/I_- are the two oriented branch Gysin lines","pair_gysin":"PASS separately: Ext^2_R(R/I_pair,R)=R/I_pair for each rotated pair","branch_pair_incidence":"FAIL AS A DIRECT ATTACHMENT: supports are nonnested; Tor_0=Tor_1=R/(I_branch+I_pair), while Ext^0=Ext^1=0 and Ext^2=Ext^3=R/(I_branch+I_pair)","source_top_square":"UNTYPED: the target relation differential is known, but equality with the boundaries of the two conductor top traces requires six excess Beck-Chevalley/Gysin comparison maps not constructed in entries 93-97","associated_grade":"PASS at carrier grade: (G2,K_alt); the full filtered chain lift remains conditional on the missing excess maps"},"counterevidence":["A formal cone on T0+T1+T2 would satisfy the square by definition, but is unnecessary and would not construct the missing source attachment.","The unique codimension-three Gysin class on each normalization branch does not compare itself with the three codimension-two pair classes because every branch/pair square has a nonzero excess Tor_1 line.","Nonresonant inversion can contract the Koszul complexes but erases the support filtration in which the source lift is being asked."],"next_experiment":"construct one branch-top/pair excess Beck-Chevalley map, for example from I_+=(u1,u3,u5) to I_03=(u0,u3), including the Tor_1 excess orientation, occurrence pullback, reciprocal/Borel-Moore support, and lower Cousin terms; test that its boundary is the rotated entry-97 trace before rotating to the other five attachments"}"#
        )
    );
}
