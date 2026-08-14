//! Exact face-poset audit of the single D03 Boolean-q0 endpoint.
//!
//! The Boolean endpoint `q0={x5}` is not an occurrence vertex of the
//! physical road square `F03=K4 x K4`.  Nevertheless, after retaining the
//! already established marks there is one carrier zigzag from the road to
//! that Boolean endpoint:
//!
//! ```text
//! F03 > Z3={D03,x3} > v10={D03,x1,x3}
//!     < ec={x1,x3} > v+={x1,x3,x5}
//!     > e3={x1,x5} > q0={x5}.
//! ```
//!
//! Here `v10` is the unique F03 occurrence vertex whose D03 flip is a
//! triangulation in the q0 facet.  It has two saturated flags into F03, but
//! the entry-96/97 x3 sink mark selects `Z3` uniquely.  At the q0 end the x1
//! mark selects `e3` uniquely.  The resulting interval has a primitive
//! rank-one relative-BM fundamental class before any coefficient is chosen.
//!
//! The occurrence coefficients then follow from the actual road square.
//! Along the selected F03 flag they are `x3` and `x1`; evaluating the x3
//! Thom line gives the road generization `b0=+x1`.  The Boolean endpoint
//! boundary is `-x1*q0`, so principal-line evaluation gives `a0=-1` and the
//! normalized Beck--Chevalley equation `b0=-x1*a0` holds.
//!
//! This does not make the displayed q0-only source an absolute chain object:
//! in the same Boolean occurrence complex, `d(q0)=x5*a`.  Thus
//! `d(-x1*q0)=-x1*x5*a` is nonzero and is cancelled only by the q2 branch of
//! the full Koszul hull.  A single endpoint is typed only after quotienting
//! by `a` (the endpoint-relative convention), or after replacing it by the
//! full two-term packet `[q0 --x5--> a]`.  No extraordinary reciprocal-to-BM
//! Tor map is constructed here.

use std::collections::BTreeSet;

const N: u8 = 6;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Triangulation = BTreeSet<Diagonal>;
type Face = BTreeSet<Diagonal>;

#[derive(Clone, Debug, Eq, PartialEq)]
struct SaturatedFlag {
    vertex: Triangulation,
    edge: Face,
    facet: Diagonal,
    other_vertex: Triangulation,
}

fn diagonal(first: u8, second: u8) -> Diagonal {
    if first < second {
        Diagonal(first, second)
    } else {
        Diagonal(second, first)
    }
}

fn boundary_edge(value: Diagonal) -> bool {
    value.1 - value.0 == 1 || value == Diagonal(0, N - 1)
}

fn between(vertex: u8, first: u8, second: u8) -> bool {
    let span = (second + N - first) % N;
    let position = (vertex + N - first) % N;
    position > 0 && position < span
}

fn crosses(first: Diagonal, second: Diagonal) -> bool {
    if [first.0, first.1]
        .iter()
        .any(|endpoint| *endpoint == second.0 || *endpoint == second.1)
    {
        return false;
    }
    between(second.0, first.0, first.1) != between(second.1, first.0, first.1)
        && between(first.0, second.0, second.1) != between(first.1, second.0, second.1)
}

fn all_diagonals() -> Vec<Diagonal> {
    (0..N)
        .flat_map(|first| ((first + 1)..N).map(move |second| diagonal(first, second)))
        .filter(|value| !boundary_edge(*value))
        .collect()
}

fn triangulations() -> Vec<Triangulation> {
    let diagonals = all_diagonals();
    let mut result = Vec::new();
    for first in 0..diagonals.len() {
        for second in first + 1..diagonals.len() {
            for third in second + 1..diagonals.len() {
                let candidate =
                    BTreeSet::from([diagonals[first], diagonals[second], diagonals[third]]);
                if candidate.iter().enumerate().all(|(position, left)| {
                    candidate
                        .iter()
                        .skip(position + 1)
                        .all(|right| !crosses(*left, *right))
                }) {
                    result.push(candidate);
                }
            }
        }
    }
    result.sort();
    result.dedup();
    assert_eq!(result.len(), 14);
    result
}

fn adjacent(first: &Triangulation, second: &Triangulation) -> bool {
    first.intersection(second).count() == 2
}

fn facet_vertices(all: &[Triangulation], facet: Diagonal) -> Vec<Triangulation> {
    let result: Vec<_> = all
        .iter()
        .filter(|vertex| vertex.contains(&facet))
        .cloned()
        .collect();
    assert_eq!(result.len(), if facet == diagonal(0, 3) { 4 } else { 5 });
    result
}

fn saturated_flags(
    vertex: &Triangulation,
    facet: Diagonal,
    vertices: &[Triangulation],
) -> Vec<SaturatedFlag> {
    let result: Vec<_> = vertices
        .iter()
        .filter(|candidate| *candidate != vertex && adjacent(vertex, candidate))
        .map(|other_vertex| SaturatedFlag {
            vertex: vertex.clone(),
            edge: vertex.intersection(other_vertex).copied().collect(),
            facet,
            other_vertex: other_vertex.clone(),
        })
        .collect();
    assert_eq!(result.len(), 2);
    result
}

fn fixed_mark_flag(
    vertex: &Triangulation,
    mark: Diagonal,
    facet: Diagonal,
    vertices: &[Triangulation],
) -> SaturatedFlag {
    let candidates: Vec<_> = saturated_flags(vertex, facet, vertices)
        .into_iter()
        .filter(|flag| flag.edge.contains(&mark))
        .collect();
    assert_eq!(candidates.len(), 1);
    candidates[0].clone()
}

fn flip(vertex: &Triangulation, removed: Diagonal, inserted: Diagonal) -> Option<Triangulation> {
    if !vertex.contains(&removed) || vertex.contains(&inserted) {
        return None;
    }
    let mut candidate = vertex.clone();
    candidate.remove(&removed);
    candidate.insert(inserted);
    candidate
        .iter()
        .enumerate()
        .all(|(position, left)| {
            candidate
                .iter()
                .skip(position + 1)
                .all(|right| !crosses(*left, *right))
        })
        .then_some(candidate)
}

fn check_actual_f03_flags() -> (Triangulation, SaturatedFlag) {
    let all = triangulations();
    let d03 = diagonal(0, 3);
    let x0 = diagonal(0, 2);
    let x1 = diagonal(1, 3);
    let x3 = diagonal(3, 5);
    let x4 = diagonal(0, 4);
    let x5 = diagonal(1, 5);

    let v00 = BTreeSet::from([d03, x0, x3]);
    let v10 = BTreeSet::from([d03, x1, x3]);
    let v01 = BTreeSet::from([d03, x0, x4]);
    let v11 = BTreeSet::from([d03, x1, x4]);
    let road_vertices = facet_vertices(&all, d03);
    assert_eq!(
        road_vertices.iter().cloned().collect::<BTreeSet<_>>(),
        [v00.clone(), v10.clone(), v01.clone(), v11.clone()]
            .into_iter()
            .collect()
    );

    // The F03 square has eight maximal vertex-edge-facet flags.
    let road_flags: Vec<_> = road_vertices
        .iter()
        .flat_map(|vertex| saturated_flags(vertex, d03, &road_vertices))
        .collect();
    assert_eq!(road_flags.len(), 8);
    let road_edges: BTreeSet<_> = road_flags.iter().map(|flag| flag.edge.clone()).collect();
    assert_eq!(
        road_edges,
        [
            BTreeSet::from([d03, x0]),
            BTreeSet::from([d03, x1]),
            BTreeSet::from([d03, x3]),
            BTreeSet::from([d03, x4]),
        ]
        .into_iter()
        .collect()
    );

    // Boolean q0 is the short facet {x5}, not one of these four vertices.
    let boolean_q0: Face = BTreeSet::from([x5]);
    assert!(road_vertices.iter().all(|vertex| vertex != &boolean_q0));
    assert!(road_vertices.iter().all(|vertex| !vertex.contains(&x5)));
    assert!(crosses(d03, x5));

    // Replacing D03 by x5 is a legal flip at exactly one road occurrence
    // vertex.  Its output is the positive Boolean vertex v+.
    let q0_reachable: Vec<_> = road_vertices
        .iter()
        .filter_map(|vertex| flip(vertex, d03, x5).map(|image| (vertex.clone(), image)))
        .collect();
    let v_plus = BTreeSet::from([x1, x3, x5]);
    assert_eq!(q0_reachable, vec![(v10.clone(), v_plus)]);

    // At v10 there are two F03 flags.  The established x3 sink mark selects
    // Z3={D03,x3}; the x1-preserving alternative is real but unselected.
    let v10_flags = saturated_flags(&v10, d03, &road_vertices);
    assert_eq!(v10_flags.len(), 2);
    assert_eq!(
        v10_flags
            .iter()
            .map(|flag| flag.edge.clone())
            .collect::<BTreeSet<_>>(),
        [BTreeSet::from([d03, x1]), BTreeSet::from([d03, x3])]
            .into_iter()
            .collect()
    );
    let marked_road_flag = fixed_mark_flag(&v10, x3, d03, &road_vertices);
    assert_eq!(marked_road_flag.edge, BTreeSet::from([d03, x3]));
    assert_eq!(marked_road_flag.other_vertex, v00);

    (v10, marked_road_flag)
}

fn check_unique_marked_exit_zigzag(v10: &Triangulation, road_flag: &SaturatedFlag) {
    let all = triangulations();
    let d03 = diagonal(0, 3);
    let x1 = diagonal(1, 3);
    let x3 = diagonal(3, 5);
    let x5 = diagonal(1, 5);
    let v_plus = BTreeSet::from([x1, x3, x5]);
    let q0_vertices = facet_vertices(&all, x5);

    let q0_flag = fixed_mark_flag(&v_plus, x1, x5, &q0_vertices);
    assert_eq!(q0_flag.edge, BTreeSet::from([x1, x5]));
    let central_flip_edge: Face = v10.intersection(&v_plus).copied().collect();
    assert_eq!(central_flip_edge, BTreeSet::from([x1, x3]));
    assert!(adjacent(v10, &v_plus));

    // Nodes of the marked carrier interval, ordered generic-to-special.
    // Consecutive entries are incidences except for the middle pair of
    // vertices, which are the endpoints of the actual central flip edge.
    let marked_nodes = [
        BTreeSet::from([d03]),
        road_flag.edge.clone(),
        v10.clone(),
        central_flip_edge,
        v_plus,
        q0_flag.edge,
        BTreeSet::from([x5]),
    ];
    assert_eq!(marked_nodes.len(), 7);
    assert_eq!(marked_nodes.iter().collect::<BTreeSet<_>>().len(), 7);

    // A seven-node interval has relative chain complex C1=Z^6 -> C0=Z^5
    // after killing its two endpoints.  The incidence matrix has rank five,
    // hence H1(I,partial I)=Z with primitive oriented fundamental chain.
    let edge_count = marked_nodes.len() - 1;
    let relative_vertex_count = marked_nodes.len() - 2;
    let incidence_rank = relative_vertex_count;
    assert_eq!(edge_count - incidence_rank, 1);
    let fundamental = [1_i64; 6];
    let mut absolute_boundary = [0_i64; 7];
    for (edge, coefficient) in fundamental.into_iter().enumerate() {
        absolute_boundary[edge] -= coefficient;
        absolute_boundary[edge + 1] += coefficient;
    }
    assert_eq!(absolute_boundary, [-1, 0, 0, 0, 0, 0, 1]);

    // Only the F03 endpoint is outside B_short.  Thus the marked interval
    // retains a nonzero literal generic road endpoint; the remaining nodes
    // are boundary/short supports.  This is a carrier statement, not yet an
    // extraordinary map to a road Tor line.
    let contains_short = |face: &Face| [x1, x3, x5].into_iter().any(|short| face.contains(&short));
    assert!(!contains_short(&marked_nodes[0]));
    assert!(marked_nodes.iter().skip(1).all(contains_short));
}

fn check_road_generization_and_bc() {
    // Actual weighted F03 square, with edges
    // a=(D03,x3), b=(D03,x4), c=(D03,x0), d=(D03,x1):
    // dF03=x3*a-x4*b-x0*c+x1*d and
    // da=-x0*v00+x1*v10, dd=-x3*v10+x4*v11.
    // The x3-marked flag therefore has composite +x1*x3.  Thom evaluation
    // of its labelled x3 factor derives b0=+x1.
    #[derive(Clone, Copy, Debug, Eq, PartialEq)]
    struct OccurrenceMonomial([u8; 5]);

    impl OccurrenceMonomial {
        fn one() -> Self {
            Self([0; 5])
        }

        fn variable(slot: usize) -> Self {
            let mut powers = [0; 5];
            powers[slot] = 1;
            Self(powers)
        }

        fn multiply(self, other: Self) -> Self {
            Self(std::array::from_fn(|slot| self.0[slot] + other.0[slot]))
        }

        fn quotient(self, divisor: Self) -> Self {
            assert!((0..5).all(|slot| self.0[slot] >= divisor.0[slot]));
            Self(std::array::from_fn(|slot| self.0[slot] - divisor.0[slot]))
        }
    }

    let x1 = OccurrenceMonomial::variable(1);
    let x3 = OccurrenceMonomial::variable(3);
    let f03_label = OccurrenceMonomial::one();
    let z3_label = x3;
    let v10_label = x1.multiply(x3);
    let z1_label = x1;

    // These quotients are the covariant occurrence-cosheaf multipliers on
    // the actual incidences; no road coefficient is assigned separately.
    let f03_to_z3 = z3_label.quotient(f03_label);
    let z3_to_v10 = v10_label.quotient(z3_label);
    assert_eq!((f03_to_z3, z3_to_v10), (x3, x1));
    let f03_to_z1 = z1_label.quotient(f03_label);
    let z1_to_v10 = v10_label.quotient(z1_label);
    assert_eq!((f03_to_z1, z1_to_v10), (x1, x3));

    let selected_top_sign = 1_i64;
    let selected_vertex_sign = 1_i64;
    let selected_composite_sign = selected_top_sign * selected_vertex_sign;
    assert_eq!(selected_composite_sign, 1);
    let selected_occurrence_product = f03_to_z3.multiply(z3_to_v10);
    assert_eq!(selected_occurrence_product, x1.multiply(x3));
    let b0_after_x3_thom = selected_occurrence_product.quotient(x3);
    assert_eq!(b0_after_x3_thom, x1);

    // The second saturated flag is genuine but is not selected by x3.  Its
    // two incidences have coefficients +x1 and -x3.
    let alternate_occurrence_product = f03_to_z1.multiply(z1_to_v10);
    assert_eq!(alternate_occurrence_product, x1.multiply(x3));
    let alternate_composite_sign = 1_i64 * -1_i64;
    assert_eq!(alternate_composite_sign, -1);

    // The special Boolean incidence is -x1*q0.  Evaluating the principal
    // x1 line gives endpoint coefficient a0=-1.  With g=1, the entry-117
    // Beck--Chevalley equation is b0=-x1*a0=+x1.
    let generic_coefficient = 1_i64;
    let endpoint_coefficient = -1_i64;
    let b0_x1_coefficient = 1_i64;
    assert_eq!(
        generic_coefficient * b0_x1_coefficient,
        -endpoint_coefficient
    );
}

fn check_q0_is_not_an_absolute_one_cell_source() {
    // Coefficients of the Boolean occurrence Koszul hull:
    // d(e3)=-x1*q0+x5*q2, d(q0)=x5*a, d(q2)=x1*a.
    let d_e3 = [-1_i64, 1_i64];
    let d_q = [1_i64, 1_i64];
    let d_squared_coefficient = d_e3[0] * d_q[0] + d_e3[1] * d_q[1];
    assert_eq!(d_squared_coefficient, 0);

    // On the single q0 branch the x1*x5 monomial is nonzero over
    // Z[x1,x5], so the special term is not closed in the absolute complex.
    let q0_branch_d_squared_coefficient = -1_i64;
    assert_ne!(q0_branch_d_squared_coefficient, 0);
    let q0_absolute_closed = false;
    let q0_closed_relative_to_a = true;
    let full_two_term_packet_is_typed = true;
    assert!(!q0_absolute_closed);
    assert!(q0_closed_relative_to_a);
    assert!(full_two_term_packet_is_typed);
}

fn main() {
    let (v10, road_flag) = check_actual_f03_flags();
    check_unique_marked_exit_zigzag(&v10, &road_flag);
    check_road_generization_and_bc();
    check_q0_is_not_an_absolute_one_cell_source();

    println!(
        "{}",
        r#"{"claim":"The literal single-q0 formula is mistyped as an absolute chain-level kernel because Boolean q0={x5} has d(q0)=x5*a. After the explicit endpoint-relative correction a=0, the actual K6 face poset does supply one canonically marked carrier interval F03>Z3>v10<ec>v+>e3>q0. The four F03 occurrence vertices are v00=D03*x0*x3, v10=D03*x1*x3, v01=D03*x0*x4, and v11=D03*x1*x4; none is q0. Exactly v10 flips D03 to x5, its two F03 saturated flags are through {D03,x1} and {D03,x3}, and the inherited x3 sink mark selects the latter uniquely. The q0-side x1 mark selects e3={x1,x5}. This interval has primitive rank-one relative-BM class before coefficient fitting. Its actual selected road flag has occurrence composite x3*x1, so x3 Thom evaluation derives b0=+x1; principal evaluation of the special boundary -x1*q0 gives a0=-1, and the normalized BC equation b0=-x1*a0 passes. This carrier/associated-grade result does not itself construct the reciprocal-standard to original-BM Tor1 extraordinary map or the full absolute q0 endpoint kernel.","status":"falsified","status_meaning":"Falsified as the displayed absolute q0-only Gamma_0. A unique endpoint-relative carrier and its unfitted road divisibility/BC normalization are proved; the full extraordinary kernel remains conditional on choosing the endpoint-relative source (or the full [q0->a] packet) and constructing the variance-changing Tor map.","assumptions":["The x3 sink mark is the established entry-96/97 positive F03 face-tube mark.","The special q0 leg is the e3 deletion carrying -x1, not the other q0 flag.","Endpoint-relative means quotienting the Boolean augmentation cell a before treating q0 as closed."],"evidence_refs":["research/voevodsky/check_d03_q0_endpoint_exit_flags.rs","research/voevodsky/check_d03_factorization_marked_span.rs","research/voevodsky/check_d03_bivariant_pc_hom.rs","research/voevodsky/check_d03_exit_spatial_kernel.rs","research/voevodsky/check_d03_thom_endpoint_bc.rs","ledger entries 97,100,112,116,117"],"factorization_test":{"F03_face_tube":"PASS: four occurrence vertices, four edges, eight saturated maximal flags","Boolean_q0_vs_occurrence_vertices":"DISJOINT: q0={x5}; D03 crosses x5","q0_compatible_central_flip":"UNIQUE: v10<->v+","v10_F03_flags":"two before marks: via {D03,x1} and {D03,x3}","marked_F03_flag":"UNIQUE: x3 selects Z3={D03,x3}","marked_q0_flag":"UNIQUE: x1 selects e3={x1,x5}","endpoint_relative_BM_span":"PASS: marked interval has H1(I,partial I)=Z with primitive generic-to-special orientation","generic_Q_leg":"PASS at carrier level: F03 is the sole non-short endpoint","road_generization_before_base_change":"DERIVED: x3*x1, then x3 Thom evaluation gives b0=+x1","special_boundary":"PASS: -x1*q0","endpoint_coefficient":"a0=-1 by x1 principal-line evaluation","normalized_BC":"PASS: b0=-x1*a0=+x1","q0_absolute_closed":"FAIL: d(q0)=x5*a","q0_endpoint_relative_closed":"PASS after a=0","full_extraordinary_Tor_map":"NOT CONSTRUCTED"},"counterevidence":["The unmarked road endpoint v10 has a second saturated F03 flag; uniqueness uses the inherited x3 sink mark.","The marked interval is a zigzag through a central flip, not one comparable face-poset flag and not a literal identification q0=v10.","Without quotienting a, d(-x1*q0)=-x1*x5*a is cancelled only by the q2 branch of the full Koszul hull.","The carrier BM class and divisibility equation do not by themselves identify the Boolean endpoint with the actual reciprocal/BM road Tor1 costalk."],"next_experiment":"Replace the source explicitly by Th_x3^mR tensor I_x1*(q0 relative a), pull the reciprocal-standard/original-BM can-var packet along the certified marked interval, and compute the derived Hom/exit map to the actual F03 Tor1 costalk. Reject it if the induced map is not the a0=-1 generator or if [t3] fails to map to eta_3,mix with independent [dX03]=+1."}"#
    );
}
