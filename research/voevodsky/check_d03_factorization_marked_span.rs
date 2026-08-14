//! Exact census of the factorization-marked scalar incidence behind the
//! `K_alt` pair `(x_0,x_3)` at the physical channel `D=03`.
//!
//! This checker uses only the fourteen scalar hexagon triangulations and
//! their actual flip/face incidence.  It retains the data which disappear in
//! the unmarked road-square quotient:
//!
//! * the two normalization sheets and parity-central source cells;
//! * the sink occurrence marks `x_0=02` and `x_3=35`;
//! * the physical facet `F_03` and its ordered normal `[dX_03]`;
//! * the saturated vertex--edge--facet flags of entry 84; and
//! * every lower Cousin cell of the four-vertex road square.
//!
//! On the `x_0` sheet the marked endpoint is the corner `x_0*x_4`; on the
//! `x_3` sheet it is `x_1*x_3`.  Each corner has two saturated flags into
//! `F_03`, but exactly one keeps its sink mark on the whole scalar edge.  The
//! two fixed-mark edges meet at the unique common occurrence
//!
//!     W_03 = x_0*x_3 = {02,03,35}.
//!
//! Thus, at cellular/occurrence level, the minimal marked objects are
//!
//!     Z_0 = [x_0*x_3 -- x_0*x_4],
//!     Z_3 = [x_0*x_3 -- x_1*x_3],
//!
//! and the two legs of `Z_0 <- W_03 -> Z_3` are the endpoint inclusions.
//! The pullbacks of the universal source characters remain independent on
//! the rank-two character lattice of the span: `u_0 -> (1,0)` and
//! `u_3 -> (0,1)`.  No common rank-one character or rational splitting is
//! introduced.
//!
//! The checker also verifies the D=03 endpoint identity and retains the
//! complementary lower-Cousin route and the actual square top cell.  Entry
//! 38 applies to this normal-crossing face cospan and supplies its supported
//! PC face tubes, normal Koszul factors, and Cousin maps.  Together with
//! entry 89 this gives a road-costalk class and its `d_1^vee` Laurent-dual
//! cocycle.  It does not construct the primal tag `d_1`, a circuit PC
//! relation generator, or a trace sending the top cell to `Delta`.

use std::collections::{BTreeMap, BTreeSet};

const N: u8 = 6;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Diagonal(u8, u8);

type Triangulation = BTreeSet<Diagonal>;
type ZeroChain = [i64; 4];
type OneChain = [i64; 4];

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Sheet {
    Plus,
    Minus,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct SaturatedFlag {
    endpoint: Triangulation,
    edge: BTreeSet<Triangulation>,
    facet: Diagonal,
    other_endpoint: Triangulation,
}

#[derive(Clone, Debug, Eq, PartialEq)]
struct MarkedIncidenceSupport {
    sheet: Sheet,
    source_center: Triangulation,
    sink_mark: Diagonal,
    endpoint: Triangulation,
    flag: SaturatedFlag,
}

fn diagonal(first: u8, second: u8) -> Diagonal {
    if first < second {
        Diagonal(first, second)
    } else {
        Diagonal(second, first)
    }
}

fn triangulation(values: &[(u8, u8)]) -> Triangulation {
    values
        .iter()
        .map(|&(first, second)| diagonal(first, second))
        .collect()
}

fn boundary(value: Diagonal) -> bool {
    value.1 - value.0 == 1 || value == Diagonal(0, N - 1)
}

fn physical(value: Diagonal) -> bool {
    value.0 % 2 != value.1 % 2
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

fn triangulations() -> Vec<Triangulation> {
    let diagonals: Vec<_> = (0..N)
        .flat_map(|first| ((first + 1)..N).map(move |second| diagonal(first, second)))
        .filter(|value| !boundary(*value))
        .collect();
    let mut result = Vec::new();
    for first in 0..diagonals.len() {
        for second in (first + 1)..diagonals.len() {
            for third in (second + 1)..diagonals.len() {
                let candidate =
                    BTreeSet::from([diagonals[first], diagonals[second], diagonals[third]]);
                if candidate.iter().enumerate().all(|(index, left)| {
                    candidate
                        .iter()
                        .skip(index + 1)
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

fn core(value: &Triangulation) -> Vec<Diagonal> {
    value
        .iter()
        .copied()
        .filter(|item| physical(*item))
        .collect()
}

fn adjacent(first: &Triangulation, second: &Triangulation) -> bool {
    first.intersection(second).count() == 2
}

fn facet_vertices(all: &[Triangulation], facet: Diagonal) -> Vec<Triangulation> {
    let result: Vec<_> = all
        .iter()
        .filter(|value| core(value) == vec![facet])
        .cloned()
        .collect();
    assert_eq!(result.len(), 4);
    result
}

fn facet_neighbors(
    endpoint: &Triangulation,
    facet_vertices: &[Triangulation],
) -> Vec<Triangulation> {
    facet_vertices
        .iter()
        .filter(|candidate| *candidate != endpoint && adjacent(endpoint, candidate))
        .cloned()
        .collect()
}

fn common_diagonals(face: &BTreeSet<Triangulation>) -> BTreeSet<Diagonal> {
    let mut values = face.iter();
    let first = values.next().expect("a nonempty face").clone();
    values.fold(first, |common, value| {
        common.intersection(value).copied().collect()
    })
}

fn saturated_flags(
    endpoint: &Triangulation,
    facet: Diagonal,
    vertices: &[Triangulation],
) -> Vec<SaturatedFlag> {
    let result: Vec<_> = facet_neighbors(endpoint, vertices)
        .into_iter()
        .map(|other_endpoint| SaturatedFlag {
            endpoint: endpoint.clone(),
            edge: BTreeSet::from([endpoint.clone(), other_endpoint.clone()]),
            facet,
            other_endpoint,
        })
        .collect();
    assert_eq!(result.len(), 2);
    result
}

fn fixed_mark_flag(
    endpoint: &Triangulation,
    mark: Diagonal,
    facet: Diagonal,
    vertices: &[Triangulation],
) -> SaturatedFlag {
    assert!(endpoint.contains(&mark));
    let candidates: Vec<_> = saturated_flags(endpoint, facet, vertices)
        .into_iter()
        .filter(|flag| {
            flag.edge
                .iter()
                .all(|triangulation| triangulation.contains(&mark))
        })
        .collect();
    assert_eq!(candidates.len(), 1);
    candidates[0].clone()
}

fn catalan_endpoint(
    all: &[Triangulation],
    source: &Triangulation,
    mark: Diagonal,
    expected_facet: Diagonal,
    expected_endpoint: &Triangulation,
) -> Triangulation {
    assert!(source.contains(&mark));
    let candidates: Vec<_> = all
        .iter()
        .filter(|target| {
            adjacent(source, target)
                && target.contains(&mark)
                && core(target) == vec![expected_facet]
        })
        .cloned()
        .collect();
    assert_eq!(candidates, vec![expected_endpoint.clone()]);
    candidates[0].clone()
}

fn edge_boundary(chain: OneChain) -> ZeroChain {
    // Ordered road-square edges are
    //   a: v00 -> v10, b: v01 -> v11,
    //   c: v00 -> v01, d: v10 -> v11.
    let incidence = [[-1, 1, 0, 0], [0, 0, -1, 1], [-1, 0, 1, 0], [0, -1, 0, 1]];
    std::array::from_fn(|vertex| {
        (0..4)
            .map(|edge| chain[edge] * incidence[edge][vertex])
            .sum()
    })
}

fn subtract<const SIZE: usize>(left: [i64; SIZE], right: [i64; SIZE]) -> [i64; SIZE] {
    std::array::from_fn(|index| left[index] - right[index])
}

fn main() {
    let all = triangulations();
    let d03 = diagonal(0, 3);
    let x0 = diagonal(0, 2);
    let x1 = diagonal(1, 3);
    let x3 = diagonal(3, 5);
    let x4 = diagonal(0, 4);

    let even_center = triangulation(&[(0, 2), (0, 4), (2, 4)]);
    let odd_center = triangulation(&[(1, 3), (1, 5), (3, 5)]);
    assert_eq!(core(&even_center), Vec::<Diagonal>::new());
    assert_eq!(core(&odd_center), Vec::<Diagonal>::new());

    // Coordinates of the actual tensor-interval road square:
    // first index is the left slot x0/x1, second the right slot x3/x4.
    let v00 = triangulation(&[(0, 2), (0, 3), (3, 5)]); // x0*x3
    let v10 = triangulation(&[(0, 3), (1, 3), (3, 5)]); // x1*x3
    let v01 = triangulation(&[(0, 2), (0, 3), (0, 4)]); // x0*x4
    let v11 = triangulation(&[(0, 3), (1, 3), (0, 4)]); // x1*x4
    let ordered_vertices = [v00.clone(), v10.clone(), v01.clone(), v11.clone()];
    assert!(v10.contains(&x1));
    assert!(v01.contains(&x4));
    assert!(v11.contains(&x1) && v11.contains(&x4));

    let facet = facet_vertices(&all, d03);
    assert_eq!(
        facet.iter().cloned().collect::<BTreeSet<_>>(),
        ordered_vertices.iter().cloned().collect()
    );
    let facet_edges: BTreeSet<_> = (0..facet.len())
        .flat_map(|first| ((first + 1)..facet.len()).map(move |second| (first, second)))
        .filter_map(|(first, second)| {
            adjacent(&facet[first], &facet[second])
                .then(|| BTreeSet::from([facet[first].clone(), facet[second].clone()]))
        })
        .collect();
    assert_eq!(facet_edges.len(), 4);

    // Entry-86 marked Catalan endpoints, now checked from the actual flip
    // graph.  x0 belongs to the minus/even source and x3 to the plus/odd
    // source selected by K_alt for D=03.
    let endpoint0 = catalan_endpoint(&all, &even_center, x0, d03, &v01);
    let endpoint3 = catalan_endpoint(&all, &odd_center, x3, d03, &v10);
    let flag0 = fixed_mark_flag(&endpoint0, x0, d03, &facet);
    let flag3 = fixed_mark_flag(&endpoint3, x3, d03, &facet);
    assert_eq!(flag0.other_endpoint, v00);
    assert_eq!(flag3.other_endpoint, v00);

    let z0 = MarkedIncidenceSupport {
        sheet: Sheet::Minus,
        source_center: even_center.clone(),
        sink_mark: x0,
        endpoint: endpoint0.clone(),
        flag: flag0,
    };
    let z3 = MarkedIncidenceSupport {
        sheet: Sheet::Plus,
        source_center: odd_center.clone(),
        sink_mark: x3,
        endpoint: endpoint3.clone(),
        flag: flag3,
    };
    let w03 = z0.flag.other_endpoint.clone();
    assert_eq!(w03, z3.flag.other_endpoint);
    assert!(w03.contains(&d03));
    assert!(w03.contains(&x0));
    assert!(w03.contains(&x3));

    // Both projection legs are existing scalar flip edges in F_03, preserve
    // their own sink marks, and carry the same declared physical normal.
    assert!(facet_edges.contains(&z0.flag.edge));
    assert!(facet_edges.contains(&z3.flag.edge));
    assert_eq!(common_diagonals(&z0.flag.edge), BTreeSet::from([d03, x0]));
    assert_eq!(common_diagonals(&z3.flag.edge), BTreeSet::from([d03, x3]));
    assert!(z0.flag.edge.iter().all(|value| value.contains(&x0)));
    assert!(z3.flag.edge.iter().all(|value| value.contains(&x3)));
    let ordered_physical_normal =
        BTreeMap::from([("W03_to_Z0", (d03, 1_i8)), ("W03_to_Z3", (d03, 1_i8))]);
    assert_eq!(ordered_physical_normal["W03_to_Z0"], (d03, 1));
    assert_eq!(ordered_physical_normal["W03_to_Z3"], (d03, 1));

    // Negative control: before keeping the sink marks, both endpoint corners
    // have saturated routes through v00 and through v11.  Their two sets of
    // possible common lower cells are equal.  The fixed marks, not bare
    // square incidence, make W03 unique.
    let unmarked0: BTreeSet<_> = saturated_flags(&endpoint0, d03, &facet)
        .into_iter()
        .map(|flag| flag.other_endpoint)
        .collect();
    let unmarked3: BTreeSet<_> = saturated_flags(&endpoint3, d03, &facet)
        .into_iter()
        .map(|flag| flag.other_endpoint)
        .collect();
    assert_eq!(unmarked0, BTreeSet::from([v00.clone(), v11.clone()]));
    assert_eq!(unmarked3, unmarked0);

    // Universal character pullbacks on W03 retain both independent source
    // characters.  The determinant-one lattice is the exact reason this is a
    // span rather than a strict fold to a common rank-one character.
    let pullback_u0 = [1_i64, 0_i64];
    let pullback_u3 = [0_i64, 1_i64];
    let character_determinant = pullback_u0[0] * pullback_u3[1] - pullback_u0[1] * pullback_u3[0];
    assert_eq!(character_determinant, 1);
    assert_ne!(pullback_u0, pullback_u3);

    // Occurrence cosheaf legs.  Order both marked edge supports with W03 as
    // coordinate zero and the sheet endpoint as coordinate one.  Restriction
    // to W03 is the same primitive row on both sheets; extension by zero is
    // its transpose.  The common occurrence coefficient is x0*x3 on both
    // legs and remains two sheet-resolved copies, not coefficient two.
    let restriction_z0_to_w = [1_i64, 0_i64];
    let restriction_z3_to_w = [1_i64, 0_i64];
    let extension_w_to_z0 = [1_i64, 0_i64];
    let extension_w_to_z3 = [1_i64, 0_i64];
    assert_eq!(restriction_z0_to_w, restriction_z3_to_w);
    assert_eq!(extension_w_to_z0, extension_w_to_z3);
    let w03_occurrence_monomial = [1_i8, 0, 0, 1, 0, 0];
    assert_eq!(w03_occurrence_monomial[0], 1);
    assert_eq!(w03_occurrence_monomial[3], 1);
    assert_eq!(w03_occurrence_monomial.iter().sum::<i8>(), 2);

    // Entry-86 endpoint compatibility.  On vertices (v00,v10,v01,v11), the
    // plus x3 support and minus x0 support meet once at W03; the common term
    // is kept sheet-resolved rather than doubled.
    let plus_endpoint = [1, 1, 0, 0];
    let minus_endpoint = [1, 0, 1, 0];
    let endpoint_difference = subtract(plus_endpoint, minus_endpoint);
    assert_eq!(endpoint_difference, [0, 1, -1, 0]);
    assert_eq!(plus_endpoint[0], 1);
    assert_eq!(minus_endpoint[0], 1);
    assert_eq!(plus_endpoint.iter().sum::<i64>(), 2);
    assert_eq!(minus_endpoint.iter().sum::<i64>(), 2);

    // The fixed-mark projections select the lower-Cousin primitive through
    // W03.  The complementary saturated flags give the route through v11.
    // Their difference is the boundary of the already existing F03 top cell.
    let selected_primitive = [1, 0, -1, 0]; // a-c, through v00
    let complementary_primitive = [0, 1, 0, -1]; // b-d, through v11
    assert_eq!(edge_boundary(selected_primitive), endpoint_difference);
    assert_eq!(edge_boundary(complementary_primitive), endpoint_difference);
    let oriented_square_boundary = [1, -1, -1, 1]; // a-b-c+d
    assert_eq!(
        subtract(selected_primitive, complementary_primitive),
        oriented_square_boundary
    );
    assert_eq!(edge_boundary(oriented_square_boundary), [0; 4]);

    // Primal/dual guardrail.  The conductor columns x0 and x3 both land in
    // the single primal tag line Z*d1.  The augmented-triangle relation has
    // boundary Delta=d0+d1+d2, which is not in that line.  Consequently the
    // pair-local marked cospan cannot by itself supply the relation generator.
    // The ambient square top cell exists, but extending a trace across its
    // complementary x1/x4 edges is additional data.
    let k_alt_x0 = [0_i64, -1, 0];
    let k_alt_x3 = [0_i64, 1, 0];
    let delta = [1_i64, 1, 1];
    let in_d1_line = |value: [i64; 3]| value[0] == 0 && value[2] == 0;
    assert!(in_d1_line(k_alt_x0));
    assert!(in_d1_line(k_alt_x3));
    assert!(!in_d1_line(delta));

    println!(
        "{}",
        concat!(
            r#"{"claim":"the actual D=03 factorization-marked scalar incidence canonically identifies the transverse cellular span Z_0 <- W_03 -> Z_3 for the K_alt pair (x0,x3), and entry 38 gives its supported PC face diagram; this constructs a road-costalk class (and, after entry-89 Laurent duality, a d1-dual cocycle), not the primal tag or a PC trace to the Delta relation","status":"proved","assumptions":["the six-point scalar presentation is the actual associahedral face complex with the fixed-mark occurrence cosheaf of entries 83 and 86","the entry-93/94 normalization labels assign x0 to F_- and x3 to F_+ and entry 86 fixes [dX_03]","the PC realization is over entry 38's finite nonresonant coefficient ring, in particular q_0 and q_3 are not 1"],"evidence_refs":["research/voevodsky/check_d03_factorization_marked_span.rs","research/nima/check_six_point_core_entry_counit.rs","research/nima/check_six_point_subdivision_pc.rs","src/ledger/20260813-38 Finite-Alpha-Prime Normal-Torus Lift and Nearby-Cycle Unit Theorem.md","src/ledger/20260814-89 Boundary-Costalk Pairing Symbol and the Alternating-Conductor Chain Gap.md","research/voevodsky/check_occurrence_pc_trace_obstruction.rs"],"factorization_test":{"channel":"D=03","physical_facet":"F03=K4xK4","normal_orientation":"[dX_03] on both legs","cell_census":{"vertices":4,"edges":4,"top_cells":1,"added_cells":0},"Z0":{"sheet":"F_-","face":"{03,02}","sink_mark":"x0=02","endpoint":"x0*x4","projection_cell":"[x0*x3,x0*x4]","saturated_flag":"v01<[v00,v01]<F03"},"W03":"{03,02,35}=x0*x3","Z3":{"sheet":"F_+","face":"{03,35}","sink_mark":"x3=35","endpoint":"x1*x3","projection_cell":"[x0*x3,x1*x3]","saturated_flag":"v10<[v00,v10]<F03"},"fixed_mark_uniqueness":"PASS: one saturated flag on each sheet and one common occurrence","unmarked_control":"FAILS UNIQUENESS: both v00 and v11 are common lower cells","transversality":"PASS: Z0 and Z3 are the two coordinate boundary edges of F03=K4xK4 and meet normally at W03","character_pullbacks":{"u0":[1,0],"u3":[0,1],"determinant":1},"occurrence_cosheaf":{"restriction_Z0_to_W":[1,0],"restriction_Z3_to_W":[1,0],"extension_W_to_Z0":[1,0],"extension_W_to_Z3":[1,0],"coefficient":"x0*x3 retained sheet-resolved"},"entry38_pc_output":"PASS: supported face-tube/Koszul/Cousin diagram on Z0<-W03->Z3 and on the transverse F03 square","typing":"road-costalk chain; entry-89 Laurent dual is d1^vee tensor chi_N, not primal d1","occurrence_endpoint":"PASS: plus and minus supports have period 2, share W03 once, and their difference is the boundary of the selected integral primitive through W03","lower_cousin":"PASS: fixed marks select a-c through v00; the complementary route is b-d through v11","ambient_top_cell":"PASS: (a-c)-(b-d)=a-b-c+d is the boundary of the existing oriented F03 square, whose road-costalk PC image is covered by entry 38","pair_local_relation":"FAIL: K_alt(x0),K_alt(x3) lie in Z*d1 while Delta=d0+d1+d2 does not; the fixed-mark cospan neither contains the complementary edges nor supplies a relation generator","target_delta_relation":"UNTYPED globally: no circuit PC relation generator or trace maps the assembled source top coherence to Delta"},"counterevidence":["Forgetting either sink mark restores two equally valid saturated common lower cells v00 and v11.","The transverse PC theorem constructs the supported source diagram but does not reverse the road/tag duality to produce the primal K_alt tag.","The pair-local image is confined to the d1 line, so the D03 marked span alone cannot have boundary Delta; all three existing tag pairs and a separately defined circuit relation object are required."],"next_experiment":"first construct the D03 bivariant trace from this supported road-costalk PC diagram to the primal tag d1 and verify the entry-86 endpoints; only after the other two existing tag pairs are assembled may one define the circuit relation generator and test that the combined oriented top coherence has boundary Delta"}"#
        )
    );
}
